#!/usr/bin/env python3
"""Render a Module's position in the refinement order into its page.

Each Module's spec.yml names its own position. `type:` is the functional parent, and
`refines:` holds any other parent. Both are nodes of docs/type-order.yml. This script
turns them into one line between the `gen:position` markers on the page:

    **Position.** Refines Reporter and Fluorophore. Refined by nothing declared.

Rules:

- The line reads the parents from spec.yml, so a page and its source cannot disagree.
- A type links to a page only when a Module page for that type exists. A type with no
  page prints as code, because a type need not have a page.
- A Module whose `type:` is its own class node (`color-change` is `ColorReporter`)
  refines the parents that the order gives that node.
- "Refined by" lists the Modules whose parents include this Module's own node.
- A Module with no `type:` reads "Refines nothing declared." This is a finding, not a
  root: the key was left out, or its parent has no page here.

Usage:

    python3 scripts/render-position.py                       # print every line
    python3 scripts/render-position.py docs/modules/pore     # print one
    python3 scripts/render-position.py --embed               # write the marked blocks
    python3 scripts/render-position.py --check               # exit 1 if a block is stale
    python3 scripts/render-position.py --insert              # add markers under # Overview

Run it with the nucleus-docs conda environment: it needs PyYAML.
"""
import collections
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
BEGIN = "<!-- gen:position -->"
END = "<!-- /gen:position -->"


def load_order(path: Path):
    """(edges, node_of): parents by type node, and the type node each class page is."""
    doc = yaml.safe_load(path.read_text()) or {}
    edges = (doc.get("orders", {}).get("type_refinement", {}) or {}).get("edges", {}) or {}
    edges = {str(k): [str(x) for x in (v or [])] for k, v in edges.items()}
    node_of = {str(k): str(v) for k, v in (doc.get("module_slugs") or {}).items() if v}
    return edges, node_of


def load_modules(modules: Path) -> dict:
    """Every Module that has a spec.yml: its title, type and extra parents."""
    out = {}
    for d in sorted(modules.iterdir()):
        f = d / "spec.yml"
        if not f.is_file():
            continue
        doc = yaml.safe_load(f.read_text()) or {}
        refines = doc.get("refines") or []
        out[d.name] = {
            "title": doc.get("title") or d.name,
            "type": doc.get("type"),
            "refines": [refines] if isinstance(refines, str) else list(refines),
        }
    return out


def parents(slug: str, mods: dict, edges: dict, node_of: dict) -> list:
    """The type nodes this Module refines, functional parent first."""
    m = mods[slug]
    t = m["type"]
    if not t:
        return []
    if node_of.get(slug) == t:
        return list(edges.get(t, []))
    out = [t]
    out += [r for r in m["refines"] if r not in out]
    return out


def children(slug: str, mods: dict, edges: dict, node_of: dict) -> list:
    """The Modules whose parents include this Module's own node."""
    own = node_of.get(slug)
    if not own:
        return []
    return sorted(s for s in mods
                  if s != slug and own in parents(s, mods, edges, node_of))


def label(node: str, mods: dict, node_of: dict) -> str:
    """A link when a Module page is that type, and code when no page is."""
    for s in sorted(node_of):
        if node_of[s] == node and s in mods:
            return f"[{mods[s]['title']}](../{s}/spec.md)"
    return f"`{node}`"


def line(slug: str, mods: dict, edges: dict, node_of: dict) -> str:
    # TWO PARENTS READ AS "AND". A list means the Module refines each of them, and
    # neither parent refines the other.
    ps = [label(p, mods, node_of) for p in parents(slug, mods, edges, node_of)]
    up = ("Refines " + (ps[0] if len(ps) == 1 else ", ".join(ps[:-1]) + " and " + ps[-1]) + "."
          if ps else "Refines nothing declared.")
    kids = children(slug, mods, edges, node_of)
    down = ("Refined by " + ", ".join(f"[{mods[k]['title']}](../{k}/spec.md)" for k in kids) + "."
            if kids else "Refined by nothing declared.")
    return f"**Position.** {up} {down}"


def embed(page: Path, text: str, write: bool = True):
    """Rewrite the marked block. None if the page has no markers, which is a finding."""
    if not page.is_file():
        return None
    t = page.read_text()
    if BEGIN not in t or END not in t:
        return None
    i, j = t.index(BEGIN), t.index(END) + len(END)
    new = t[:i] + f"{BEGIN}\n{text}\n{END}" + t[j:]
    if new == t:
        return False
    if write:
        page.write_text(new)
    return True


def insert(page: Path, text: str) -> bool:
    """Add the marked block as the first thing under `# Overview`. False if it
    already has one or has no Overview heading."""
    if not page.is_file():
        return False
    t = page.read_text()
    if BEGIN in t:
        return False
    lines = t.split("\n")
    for n, l in enumerate(lines):
        if l.strip() == "# Overview":
            block = [BEGIN, text, END, ""]
            lines[n + 1:n + 1] = [""] + block[:-1]
            page.write_text("\n".join(lines))
            return True
    return False


def main(argv: list, repo: Path = REPO) -> int:
    modules = repo / "docs" / "modules"
    edges, node_of = load_order(repo / "docs" / "type-order.yml")
    mods = load_modules(modules)
    args = [a for a in argv if not a.startswith("--")]
    slugs = [Path(a.rstrip("/")).name for a in args] if args else sorted(mods)
    check = "--check" in argv
    stale = 0
    if "--insert" in argv:
        n = sum(insert(modules / s / "spec.md", line(s, mods, edges, node_of)) for s in slugs if s in mods)
        print(f"{n:4}  inserted")
    elif "--embed" in argv or check:
        counts = collections.Counter()
        for s in slugs:
            r = embed(modules / s / "spec.md", line(s, mods, edges, node_of), write=not check)
            counts[{None: "no markers", True: "STALE" if check else "updated",
                    False: "unchanged"}[r]] += 1
        for k, v in sorted(counts.items()):
            print(f"{v:4}  {k}")
        stale = check and counts["STALE"]
    else:
        for s in slugs:
            print(f"{s}\n  {line(s, mods, edges, node_of)}")
    # THE DENOMINATOR, EVERY RUN. A Module with no `type:` is not a root. Nothing has
    # placed it.
    typed = [s for s in slugs if mods.get(s, {}).get("type")]
    print(f"\n{len(typed)} of {len(slugs)} sources declare a type; "
          f"{len(slugs) - len(typed)} are placed by nothing.", file=sys.stderr)
    return 1 if stale else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
