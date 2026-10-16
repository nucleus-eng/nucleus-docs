#!/usr/bin/env python3
"""
generate-module-graph.py — Layer 1+2 of the module-integration-map pipeline.

Layer 1 (not mine): composition structure, read the same way the
nucleus-skills `mermaid-diagrams` skill reads it — bullet-list links under
each page's own `# Constituent Modules` section. This script re-implements
that one parsing function rather than importing the vendored skill script,
since the skill scripts are CLI tools that write their own files; the
functions themselves are small and stable (see
.claude/skills/mermaid-diagrams/scripts/gen-subsystem-tree.py).

Layer 2 (this script's real job): merge in what the skill does not cover —
  - module class + validation stars, from the tables in modules-main.md
  - family membership: either a real composition closure from a declared
    root, or a declared flat list for pages that don't have a Constituent
    Modules section yet (see FAMILY_CONFIG below for which mode each
    family uses and why)

This script does NOT decide status (confirmed/proposed/blocked), draw
requirement edges, or add curated annotations (disambiguation notes,
substitute-module claims, conflict edges). That is Layer 3 — see
module-graph-annotations.yaml — merged in by render-module-graph.py.

Usage:
    python3 scripts/generate-module-graph.py --out module-report.json
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

DOCS_MODULES = Path("docs/modules")
MODULES_MAIN = DOCS_MODULES / "modules-main.md"

FRONTMATTER_TITLE_RE = re.compile(r'^title:\s*(?:"([^"]*)"|\'([^\']*)\'|(.*))$')
TABLE_ROW_RE = re.compile(
    r"^\|\s*([^|]*)\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*([^|]*)\|"
)
CONSTITUENT_SECTION_RE = re.compile(
    r"^#+\s*Constituent Modules\s*$(.*?)(?=^#|\Z)", re.M | re.S
)
CONSTITUENT_LINK_RE = re.compile(r"\]\(\.\./([A-Za-z0-9._-]+)/spec\.md")

# Family membership. `mode: closure` expands a declared root transitively
# through composition, same as gen-subsystem-tree.py would; `mode: flat`
# is a declared list for a family whose pages don't have a Constituent
# Modules section yet (see each family's "reason" for why it's flat
# rather than closure-derived -- nucleus-docs PR #221 fixed this for two
# pages, but that hasn't merged as of this writing).
FAMILY_CONFIG = {
    "shared": {
        "mode": "flat",
        "display_name": "Shared &amp; Base",
        "reason": "base modules predate the Constituent Modules "
        "convention -- base-cell is genuinely composed of Base Cytosol + "
        "Base Membrane (its Reference Composition table says so), but "
        "that isn't in a machine-readable bullet list yet, so a closure "
        "from it would see zero constituents. Left flat rather than "
        "silently rendering Base Cell as an unconnected leaf.",
        "members": [
            "base-cytosol",
            "membrane-popc-chol",
            "base-cell",
            "dye-liposomes",
            "reporter-degfp",
        ],
    },
    "purex": {
        "mode": "flat",
        "display_name": "PURExpress",
        "reason": "leaf modules with no constituents at all -- not "
        "composed into anything, so a closure has nothing to expand.",
        "members": [
            "detector-tetr_atc",
            "detector-laci_iptg",
            "emitter-ivhsl",
            "control-clpxp",
            "energy-ppk",
            "membrane-pore-ahly",
            "membrane-pore-cx43",
        ],
    },
}


def repo_root() -> Path:
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True
    )
    if out.returncode:
        sys.exit("not inside a git repository")
    return Path(out.stdout.strip())


def extract_title(text: str, fallback: str) -> str:
    if not text.startswith("---"):
        return fallback
    end = text.find("\n---", 3)
    if end == -1:
        return fallback
    for line in text[3:end].splitlines():
        m = FRONTMATTER_TITLE_RE.match(line.strip())
        if m:
            return next(g for g in m.groups() if g is not None).strip()
    return fallback


def constituents(text: str) -> list:
    """Slugs under '# Constituent Modules', bullet-list links only.

    Same rule as the mermaid-diagrams skill: a prose link inside the
    section is a mention, not a declared constituent.
    """
    m = CONSTITUENT_SECTION_RE.search(text)
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        if not line.lstrip().startswith(("-", "*")):
            continue
        link = CONSTITUENT_LINK_RE.search(line)
        if link and link.group(1) not in out:
            out.append(link.group(1))
    return out


def load_composition_graph(repo: Path) -> dict:
    """slug -> {title, constituents, path}. Tracked files only."""
    tracked = subprocess.run(
        ["git", "-C", str(repo), "ls-files", "docs/modules"],
        capture_output=True,
        text=True,
        check=True,
    ).stdout.split()
    graph = {}
    for rel in tracked:
        if not rel.endswith(".md") or rel.endswith("modules-main.md"):
            continue
        p = repo / rel
        stem = p.stem
        if stem != "spec" and not stem.endswith("-spec"):
            continue
        slug = p.parent.name if stem == "spec" else stem
        text = p.read_text(encoding="utf-8")
        graph[slug] = {
            "title": extract_title(text, slug),
            "constituents": constituents(text),
            "path": str(p.relative_to(repo)),
        }
    return graph


def descendants(slug: str, graph: dict, seen=None) -> set:
    seen = seen if seen is not None else set()
    if slug in seen:
        return set()
    seen.add(slug)
    out = set()
    for c in graph.get(slug, {}).get("constituents", []):
        out.add(c)
        out |= descendants(c, graph, seen)
    return out


def parse_modules_main(repo: Path) -> dict:
    path = repo / MODULES_MAIN
    if not path.exists():
        print(f"warning: {MODULES_MAIN} not found", file=sys.stderr)
        return {}
    result = {}
    current_chassis = None
    last_class = ""
    for line in path.read_text(encoding="utf-8").splitlines():
        heading = re.match(r"^##\s+(.+)$", line)
        if heading:
            current_chassis = heading.group(1).strip()
            last_class = ""
            continue
        m = TABLE_ROW_RE.match(line)
        if not m:
            continue
        module_class, _text, target, validation = m.groups()
        module_class = module_class.strip() or last_class
        if module_class:
            last_class = module_class
        if target.startswith("http"):
            continue
        slug = re.sub(r"^\./", "", target)
        slug = re.sub(r"/spec\.md.*$", "", slug)
        result[slug] = {
            "class": module_class,
            "validation": validation.strip(),
            "chassis": current_chassis,
        }
    return result


def resolve_families(graph: dict) -> dict:
    """family_name -> sorted list of member slugs, per FAMILY_CONFIG."""
    families = {}
    for name, cfg in FAMILY_CONFIG.items():
        if cfg["mode"] == "flat":
            families[name] = sorted(cfg["members"])
        elif cfg["mode"] == "closure":
            members = set(cfg["roots"])
            for root in cfg["roots"]:
                members |= descendants(root, graph)
            families[name] = sorted(s for s in members if s in graph)
        else:
            sys.exit(f"unknown family mode: {cfg['mode']}")
    return families


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, default=None)
    args = ap.parse_args()

    repo = repo_root()
    graph = load_composition_graph(repo)
    table_data = parse_modules_main(repo)
    families = resolve_families(graph)

    # sanity: every family member should actually exist in the composition
    # graph (i.e. we found a spec page for it)
    for name, members in families.items():
        missing = [s for s in FAMILY_CONFIG[name].get("members", members) if s not in graph]
        for s in missing:
            print(f"warning: family '{name}' declares '{s}' but no spec page was found", file=sys.stderr)

    modules = {}
    for slug, data in graph.items():
        meta = table_data.get(slug, {})
        modules[slug] = {
            "title": data["title"],
            "path": data["path"],
            "constituents": data["constituents"],
            "class": meta.get("class"),
            "validation": meta.get("validation"),
            "chassis": meta.get("chassis"),
            "in_modules_main": slug in table_data,
        }

    report = {
        "families": {
            name: {
                "mode": FAMILY_CONFIG[name]["mode"],
                "display_name": FAMILY_CONFIG[name].get("display_name", name),
                "direction": FAMILY_CONFIG[name].get("direction", "TD"),
                "reason": FAMILY_CONFIG[name].get("reason"),
                "roots": FAMILY_CONFIG[name].get("roots"),
                "members": members,
            }
            for name, members in families.items()
        },
        "modules": modules,
    }

    output = json.dumps(report, indent=2, sort_keys=True)
    if args.out:
        args.out.write_text(output + "\n", encoding="utf-8")
        print(f"wrote {args.out} ({len(modules)} modules, {len(families)} families)")
    else:
        print(output)


if __name__ == "__main__":
    main()
