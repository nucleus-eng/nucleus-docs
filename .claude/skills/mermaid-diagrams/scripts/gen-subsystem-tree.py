#!/usr/bin/env python3
"""
gen-subsystem-tree.py — dependency flowchart for a subsystem, from declared roots.

Expands the given root modules transitively through the composition graph and
emits a greyscale Mermaid flowchart containing only those modules.

Rules this encodes, each of which came from getting it wrong first:

  * Roots are declared, never scraped from links. Pages legitimately link to
    modules they do not depend on — to explain an absence, or to contrast against
    a different implementation. Scraping every link produces phantom nodes.
  * Every node ends up a dependency of something in the diagram.
  * Requirement edges ("must be present") are a different relation from
    composition edges ("is made of"), and are drawn differently.
  * Composition only. The diagram never asserts an integration is confirmed.
  * Greyscale.

Usage:
    gen-subsystem-tree.py NAME ROOT [ROOT ...]
    gen-subsystem-tree.py --orphans          # list modules nothing references

    # a requirement edge: LEFT requires RIGHT
    gen-subsystem-tree.py NAME ROOT --requires reporter:substrate

    # drop a composition edge, e.g. a proposed alternative not actually used
    gen-subsystem-tree.py NAME ROOT --exclude cascade:alt-reporter

Run it twice for two subsystems, then diff the node lists to check one is a
subset of the other.

Output goes to tmp/proposed-diagrams/ by default. Nothing in the docs tree is
touched — insertion into pages is a separate, reviewed step.
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

MODULES_DIR = "docs/modules"
OUT_DIR = "tmp/proposed-diagrams"


def node_id(slug):
    """Mermaid ids cannot contain spaces. Derive mechanically, never from prose."""
    return re.sub(r"[^A-Za-z0-9]", "_", slug).upper()


def repo_root():
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True)
    if out.returncode:
        sys.exit("not inside a git repository")
    return Path(out.stdout.strip())


def load_graph(repo, exclude):
    """slug -> {title, cons}. Tracked files only, so build artifacts stay out."""
    tracked = subprocess.run(["git", "-C", str(repo), "ls-files", MODULES_DIR],
                             capture_output=True, text=True, check=True).stdout.split()
    graph = {}
    for rel in tracked:
        if not rel.endswith("/spec.md"):
            continue
        path = repo / rel
        slug = path.parent.name
        text = path.read_text(encoding="utf-8")
        title = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', text, re.M)
        section = re.search(r"^#+\s*Constituent Modules\s*$(.*?)(?=^#|\Z)",
                            text, re.M | re.S)
        cons = []
        if section:
            # Only bullet-list links count. A prose sentence inside the section
            # ("both paths terminate at X") is not a constituent declaration —
            # counting it inflates the graph with things the module merely
            # mentions.
            for line in section.group(1).splitlines():
                if not line.lstrip().startswith(("-", "*")):
                    continue
                link = re.search(r"\]\(\.\./([A-Za-z0-9._-]+)/spec\.md", line)
                if not link:
                    continue
                c = link.group(1)
                if c not in cons and (slug, c) not in exclude:
                    cons.append(c)
        graph[slug] = {"title": title.group(1).strip() if title else slug,
                       "cons": cons}
    return graph


def closure(roots, graph, requires):
    seen, stack = set(), list(roots)
    while stack:
        slug = stack.pop()
        if slug in seen or slug not in graph:
            continue
        seen.add(slug)
        stack.extend(graph[slug]["cons"])
        stack.extend(r for m, r in requires if m == slug)
    return seen


def emit(nodes, graph, requires, caption):
    out = ["```mermaid",
           "%%{init: {'theme': 'base', 'themeVariables': "
           "{'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%",
           "flowchart TD"]

    for slug in sorted(nodes):
        out.append(f'    {node_id(slug)}["{graph[slug]["title"]}"]')
    out.append("")

    for slug in sorted(nodes):
        for c in graph[slug]["cons"]:
            if c in nodes:
                out.append(f"    {node_id(c)} --> {node_id(slug)}")
    for m, r in sorted(requires):
        if m in nodes and r in nodes:
            out.append(f"    {node_id(r)} -.->|requires| {node_id(m)}")
    out.append("")

    leaves = sorted(s for s in nodes if not graph[s]["cons"])
    composed = sorted(s for s in nodes if graph[s]["cons"])
    out.append("    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;")
    out.append("    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;")
    if leaves:
        out.append("    class " + ",".join(node_id(s) for s in leaves) + " leaf;")
    if composed:
        out.append("    class " + ",".join(node_id(s) for s in composed) + " composed;")
    out.append("")

    for slug in sorted(nodes):
        out.append(f'    click {node_id(slug)} "/docs/modules/{slug}/spec"')
    out.append("```")
    out.append("")
    out.append(caption)
    return "\n".join(out)


def pairs(values):
    result = set()
    for v in values or []:
        if ":" not in v:
            sys.exit(f"expected LEFT:RIGHT, got {v!r}")
        a, b = v.split(":", 1)
        result.add((a.strip(), b.strip()))
    return result


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("name", nargs="?", help="subsystem name, used in the caption")
    ap.add_argument("roots", nargs="*", help="module slugs to expand from")
    ap.add_argument("--requires", action="append", metavar="LEFT:RIGHT")
    ap.add_argument("--exclude", action="append", metavar="LEFT:RIGHT")
    ap.add_argument("--orphans", action="store_true",
                    help="list modules nothing references — candidate roots")
    args = ap.parse_args()

    repo = repo_root()
    graph = load_graph(repo, pairs(args.exclude))
    requires = pairs(args.requires)

    if args.orphans:
        referenced = {c for v in graph.values() for c in v["cons"]}
        tops = sorted(s for s in graph if s not in referenced)
        print(f"referenced by nothing ({len(tops)}) — candidate roots:")
        for s in tops:
            print(f"    {s}  ({len(graph[s]['cons'])} constituent(s))")
        return 0

    if not args.name or not args.roots:
        ap.print_help()
        return 2

    unknown = [r for r in args.roots if r not in graph]
    if unknown:
        sys.exit(f"unknown root(s): {unknown}")

    nodes = closure(args.roots, graph, requires)
    caption = (f"Module dependency tree for {args.name}. Every node is a dependency "
               f"of something shown. This diagram shows composition only — it does "
               f"not assert that any integration is confirmed.")

    outdir = repo / OUT_DIR
    outdir.mkdir(parents=True, exist_ok=True)
    slug = re.sub(r"[^a-z0-9]+", "-", args.name.lower()).strip("-")
    dest = outdir / f"tree-{slug}.md"
    dest.write_text(emit(nodes, graph, requires, caption) + "\n", encoding="utf-8")

    print(f"{args.name}: {len(nodes)} module(s)")
    for s in sorted(nodes):
        print(f"    {s}")
    print(f"\nwritten to {dest.relative_to(repo)}")
    print("nothing in the docs tree was touched")
    return 0


if __name__ == "__main__":
    sys.exit(main())
