#!/usr/bin/env python3
"""
gen-module-diagrams.py — generate a composition diagram for each Module spec.

Implements issue #209: "By tracing the Composition path of a module (i.e., Base
Cell from composition of Base Cytosol and Base Membrane), we can construct an
integration requirements diagram for each module."

The graph is read from each page's `# Constituent Modules` section, so the diagram
is derived from the docs rather than maintained alongside them. Regenerating after
a composition change is therefore a no-op unless the composition actually changed.

Output is a plain ```mermaid block wrapped in marker comments:

    <!-- gen:composition-diagram -->
    ```mermaid
    ...
    ```
    <!-- /gen:composition-diagram -->

Rewriting is idempotent: an existing block between the markers is replaced, and
nothing outside them is touched.

Usage:
    python3 scripts/gen-module-diagrams.py                 # dry run -> tmp/proposed-diagrams/
    python3 scripts/gen-module-diagrams.py --write         # insert into pages
    python3 scripts/gen-module-diagrams.py --check         # exit 1 if any page is stale
"""

import re
import subprocess
import sys
from pathlib import Path


def repo_root():
    """The docs repository, resolved from the working directory.

    This script lives in the skills repo and runs against a docs repo, so the
    root can never be derived from `__file__`.
    """
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True)
    if out.returncode:
        sys.exit("not inside a git repository — run this from the docs repo")
    root = Path(out.stdout.strip())
    if not (root / "docs" / "modules").is_dir():
        sys.exit(f"no docs/modules under {root} — run this from the docs repo")
    return root


REPO = repo_root()

BEGIN = "<!-- gen:composition-diagram -->"
END = "<!-- /gen:composition-diagram -->"

# Mermaid node ids must not contain spaces or punctuation. A previous terminology
# sweep broke two diagrams by substituting a spaced phrase into a node id, so ids
# are derived mechanically here and never from prose.
def node_id(slug: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "_", slug).upper()


def frontmatter_title(text: str, fallback: str) -> str:
    m = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', text, re.M)
    return m.group(1).strip() if m else fallback


def constituents(text: str) -> list[str]:
    """Slugs listed under '# Constituent Modules', in order."""
    m = re.search(r"^#+\s*Constituent Modules\s*$(.*?)(?=^#|\Z)", text, re.M | re.S)
    if not m:
        return []
    out = []
    # Only bullet-list links count. A prose link inside the section is a mention,
    # not a constituent declaration.
    for line in m.group(1).splitlines():
        if not line.lstrip().startswith(("-", "*")):
            continue
        link = re.search(r"\]\(\.\./([A-Za-z0-9._-]+)/spec\.md", line)
        if link and link.group(1) not in out:
            out.append(link.group(1))
    return out


def load_graph():
    """slug -> {title, constituents, path}. Only tracked pages."""
    tracked = subprocess.run(
        ["git", "-C", str(REPO), "ls-files", "docs/modules"],
        capture_output=True, text=True, check=True).stdout.split()
    graph = {}
    for rel in tracked:
        if not rel.endswith("/spec.md"):
            continue
        p = REPO / rel
        slug = p.parent.name
        text = p.read_text(encoding="utf-8")
        graph[slug] = {
            "title": frontmatter_title(text, slug),
            "constituents": constituents(text),
            "path": p,
        }
    return graph


def descendants(slug, graph, seen=None):
    """Every module reachable downward through composition. Cycle-safe."""
    seen = seen or set()
    if slug in seen:
        return set()
    seen.add(slug)
    out = set()
    for c in graph.get(slug, {}).get("constituents", []):
        out.add(c)
        out |= descendants(c, graph, seen)
    return out


def build_diagram(slug, graph):
    """Mermaid block for one module's composition tree, or None if it has none."""
    root = graph[slug]
    if not root["constituents"]:
        return None

    involved = {slug} | descendants(slug, graph)
    # keep only nodes we actually have pages for
    involved = {s for s in involved if s in graph}

    lines = [
        "```mermaid",
        "%%{init: {'theme': 'base', 'themeVariables': "
        "{'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%",
        "flowchart TD",
    ]

    for s in sorted(involved):
        label = graph[s]["title"].replace('"', "'")
        lines.append(f'    {node_id(s)}["{label}"]')

    lines.append("")
    edges = []
    for s in sorted(involved):
        for c in graph[s]["constituents"]:
            if c in involved:
                edges.append(f"    {node_id(c)} --> {node_id(s)}")
    lines += edges

    lines.append("")
    lines.append("    classDef constituent fill:#6B7280,color:#ffffff,stroke:#4B5563;")
    lines.append("    classDef this fill:#374151,color:#ffffff,stroke:#111827;")
    others = sorted(involved - {slug})
    if others:
        lines.append("    class " + ",".join(node_id(s) for s in others) + " constituent;")
    lines.append(f"    class {node_id(slug)} this;")

    lines.append("")
    for s in sorted(involved):
        lines.append(f"    click {node_id(s)} \"/docs/modules/{s}/spec\"")

    lines.append("```")
    return "\n".join(lines)


def wrap(diagram, title):
    """A tab-item, fenced at 4 colons to sit inside a 5-colon tab-set.

    Emits the diagram and nothing else. Three explanatory paragraphs used to
    follow it — how to read the arrows, a note that composition is not a claim
    about integration, and a line telling the reader this block is generated.
    They were removed because docs pages address the compositional biology
    community, who are reading them as reference documentation: the first
    restated what a clickable flowchart already shows, and the other two spoke
    to editors rather than to that audience. The BEGIN/END markers already mark
    the block as generated for anyone editing the source.
    """
    return (
        f"{BEGIN}\n"
        f"::::{{tab-item}} Module Dependencies\n\n"
        f"{diagram}\n\n"
        f"::::\n"
        f"{END}"
    )


def existing_block(text):
    m = re.search(re.escape(BEGIN) + r".*?" + re.escape(END), text, re.S)
    return m


def main():
    write = "--write" in sys.argv
    check = "--check" in sys.argv
    graph = load_graph()

    have, skipped, stale = [], [], []
    outdir = REPO / "tmp" / "proposed-diagrams"
    if not (write or check):
        outdir.mkdir(parents=True, exist_ok=True)

    for slug in sorted(graph):
        diagram = build_diagram(slug, graph)
        if diagram is None:
            skipped.append(slug)
            continue
        have.append(slug)
        block = wrap(diagram, graph[slug]["title"])
        p = graph[slug]["path"]
        text = p.read_text(encoding="utf-8")
        m = existing_block(text)

        if check:
            if not m or m.group(0) != block:
                stale.append(slug)
            continue
        if write:
            if m:
                p.write_text(text[:m.start()] + block + text[m.end():], encoding="utf-8")
            else:
                stale.append(slug)  # no marker yet: needs manual placement
            continue
        (outdir / f"{slug}.md").write_text(block + "\n", encoding="utf-8")

    if check:
        print(f"{len(have)} module(s) with a composition path")
        if stale:
            print(f"STALE or missing block ({len(stale)}):")
            for s in stale:
                print(f"  {s}")
            return 1
        print("✅ all composition diagrams current")
        return 0

    print(f"modules with a composition path : {len(have)}")
    for s in have:
        n = len(descendants(s, graph) & set(graph))
        print(f"    {s}  ({n} constituent(s), transitive)")
    print(f"\nno constituents, skipped        : {len(skipped)}")
    if write:
        placed = len(have) - len(stale)
        print(f"\nwritten into {placed} page(s)")
        if stale:
            print(f"no {BEGIN} marker found, so NOT written ({len(stale)}):")
            for s in stale:
                print(f"  {s}")
            print("\nAdd the marker pair inside the page's tab-set, then re-run --write.")
    else:
        print(f"\nproposals written to {outdir.relative_to(REPO)}/ (nothing in docs/ touched)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
