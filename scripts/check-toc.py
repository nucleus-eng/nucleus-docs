#!/usr/bin/env python3
"""
check-toc.py — validate myst.yml TOC against the docs/ file tree.

Two checks:

  STRICT (error, exit 1): every file: entry in myst.yml must resolve to an
  existing file. Broken TOC references are always wrong — zero false positives.

  ADVISORY (warning, exit 0): every .md file under docs/ should appear in the
  TOC. Files excluded by naming convention (protocol-*.md, bom-*.md) or by an
  inline allowlist of known intentional non-sidebar pages are skipped.

  HUB (error, exit 1): every page in the TOC must also be linked from its
  section's hub page — docs/modules/modules-main.md and its siblings. Adding a
  page is two table-of-contents updates, not one, and only the myst.yml half
  was ever checked. CLAUDE.md states the duty for Modules; Processes and
  Implementations have identical hub pages and no stated rule, and drifted the
  same way, so this checks all three.

hidden: true entries ARE real TOC entries — their files must exist.
title:-only nodes (no file: key) are skipped.

Usage:
    python3 scripts/check-toc.py
    python3 scripts/check-toc.py myst.yml
"""

import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: pyyaml is required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

MYST_YML = Path("myst.yml")
DOCS_ROOT = Path("docs")

# Files intentionally not in the sidebar (known stragglers).
# Paths relative to repo root.
ADVISORY_ALLOWLIST = {
    "docs/processes/make-36pot/assemble-pmix/main.md",
    "docs/modules/reporter-degfp/bom-cells.md",
    "docs/modules/reporter-degfp/bom-cytosol.md",
    "docs/modules/reporter-degfp/protocol-cells.md",
    "docs/modules/reporter-degfp/protocol-cytosol.md",
}

# Naming-convention exclusions (basename patterns).
ADVISORY_EXCLUDE_PREFIXES = ("protocol-", "bom-")
ADVISORY_EXCLUDE_SUFFIXES = ("-main.md",)  # index pages that are TOC roots themselves


def collect_toc_files(node, base: Path) -> list[tuple[str, Path]]:
    """Recursively collect (raw_ref, resolved_path) from a TOC node or list."""
    results = []
    if isinstance(node, list):
        for item in node:
            results.extend(collect_toc_files(item, base))
    elif isinstance(node, dict):
        if "file" in node:
            raw = node["file"]
            resolved = (base / raw).resolve()
            results.append((raw, resolved))
        for key in ("children",):
            if key in node:
                results.extend(collect_toc_files(node[key], base))
    return results


def advisory_excluded(path: Path) -> bool:
    name = path.name.lower()
    if any(name.startswith(p) for p in ADVISORY_EXCLUDE_PREFIXES):
        return True
    if any(name.endswith(s) for s in ADVISORY_EXCLUDE_SUFFIXES):
        return True
    rel = str(path).replace("\\", "/")
    if rel in ADVISORY_ALLOWLIST:
        return True
    return False


LINK_RE = re.compile(r"\]\(([^)#]+?\.md)(?:#[^)]*)?\)")

# Section roots that carry a hub page listing their content pages.
HUB_SECTIONS = ("modules", "processes", "implementations")

# Pages in the TOC with no hub row. Paths from repo root.
#
# These two are the pre-existing debt this check was written to find, not
# exemptions — both already have a hub row on docs/devcells-integration-pages.
# DELETE BOTH ENTRIES when that branch merges; the check then has an empty
# allowlist and enforces for everything.
HUB_ALLOWLIST: set[str] = {
    "docs/modules/detector-laci_iptg/spec.md",
    "docs/implementations/emitter-ivhsl/main.md",
}


def hub_linked(hub: Path) -> set[Path]:
    """Every .md a hub page links to, resolved."""
    if not hub.exists():
        return set()
    text = hub.read_text(encoding="utf-8")
    return {(hub.parent / raw).resolve() for raw in LINK_RE.findall(text)}


def check_hubs(toc_resolved: set[Path]) -> list[str]:
    """TOC pages whose section hub does not link them."""
    findings = []
    for section in HUB_SECTIONS:
        root = DOCS_ROOT / section
        hub = root / f"{section}-main.md"
        if not hub.exists():
            continue
        linked = hub_linked(hub)
        for page in sorted(root.glob("*/*.md")):
            if page.name.startswith(ADVISORY_EXCLUDE_PREFIXES):
                continue
            if str(page).replace("\\", "/") in HUB_ALLOWLIST:
                continue
            if page.resolve() not in toc_resolved:
                continue  # not published; myst.yml is the gate for that
            if page.resolve() not in linked:
                findings.append(
                    f"{page}: in myst.yml but not linked from {hub} — "
                    "adding a page is two TOC updates, not one"
                )
    return findings


def main() -> int:
    myst_path = Path(sys.argv[1]) if len(sys.argv) > 1 else MYST_YML
    if not myst_path.exists():
        print(f"error: {myst_path} not found", file=sys.stderr)
        return 1

    config = yaml.safe_load(myst_path.read_text(encoding="utf-8"))
    toc = config.get("project", {}).get("toc") or config.get("toc", [])
    base = myst_path.parent

    toc_entries = collect_toc_files(toc, base)
    toc_resolved = {p for _, p in toc_entries}

    # --- STRICT: every TOC entry must resolve ---
    strict_errors = 0
    for raw, resolved in toc_entries:
        if not resolved.exists():
            # Report relative to repo root
            try:
                rel = resolved.relative_to(base.resolve())
            except ValueError:
                rel = resolved
            print(f"{myst_path}:  broken TOC reference: {raw!r} → {rel} does not exist")
            strict_errors += 1

    if strict_errors:
        print(f"\n{strict_errors} broken TOC reference(s). Fix myst.yml.")
        return 1

    # --- HUB: every published page must be linked from its section hub ---
    hub_findings = check_hubs(toc_resolved)
    for f in hub_findings:
        print(f"error: {f}")

    # --- ADVISORY: every docs/ .md should appear in the TOC ---
    advisory_warnings = 0
    try:
        ls = subprocess.run(
            ["git", "ls-files", str(DOCS_ROOT)],
            capture_output=True, text=True, check=True,
        )
        all_docs_md = sorted(
            Path(p) for p in ls.stdout.splitlines()
            if p.endswith(".md") and "generated" not in Path(p).parts
        )
    except subprocess.CalledProcessError:
        all_docs_md = []
    for md in all_docs_md:
        if "generated" in md.parts:
            continue
        if advisory_excluded(md):
            continue
        resolved = md.resolve()
        if resolved not in toc_resolved:
            print(f"warning: {md}  not in myst.yml TOC (advisory)")
            advisory_warnings += 1

    if advisory_warnings:
        print(f"\n{advisory_warnings} advisory: file(s) not in TOC. Add to myst.yml or allowlist.")

    if hub_findings:
        pages = len({f.split(":")[0] for f in hub_findings})
        print(f"\n{len(hub_findings)} page(s) missing a hub row, across {pages} file(s).")
        return 1

    if not advisory_warnings:
        print(f"✅ TOC valid. {len(toc_entries)} entries checked, "
              f"{len(all_docs_md)} docs/ files scanned, "
              f"{len(HUB_SECTIONS)} hub page(s) cross-checked.")

    return 0  # Advisory warnings do not fail CI


if __name__ == "__main__":
    sys.exit(main())
