#!/usr/bin/env python3
"""Report Module pages that explain themselves through the pages that use them.

A Module is defined by what it is made of and what it does, and those facts are
the same whoever takes it. A page that reaches FORWARD to a composite to say
what it is has inverted the dependency: the leaf then needs the composite to be
legible, while the composite already needs the leaf to exist, and nothing can be
retired, reused or read on its own. style-guide/principles.md § Write for an
unknown composer states the rule and its test.

Measured 2026-10-03 before the rule was written: 32 of 729 module-to-module
links pointed downstream, on 11 of 77 pages. Nineteen sat in a page's own
Composition, Behavior or Requirements, and the worst were tables keyed by
consumer. The cost was concrete -- retiring one composed Module meant rewriting
eight pages that were not being retired.

TWO AXES, AND ONLY ONE OF THEM IS CHECKED. `refines:` is abstraction and
`inputs:` is composition. A class listing its members, or a member naming its
class, is the abstraction axis and is never a finding -- including when a
subclass also takes its parent as an input, which several do. The abstraction
axis is resolved first for exactly that reason.

REPORTS, NEVER BLOCKS. Exit code is 0 whatever it finds. A rule with a backlog
behind it teaches a reader to skip the output, and the three exemptions below
are judgment calls that a reader, not this script, should be making.

Exempt:
  * `# Overview`             one sentence naming what a leaf composes into is
                             what sections.md asks for; a leaf has no generated
                             diagram, so it is the reader's only way forward.
  * `# Implementations`      check-implementations.py owns that section and
                             blocks on it. Two checks on one line is noise.
  * `# Credits`, frontmatter not prose about the Module.

It does NOT judge how a link is used. "Requires a sigma-70 promoter (e.g.
Detector: 3OC6-HSL)" names a downstream Module and passes the rule's own test:
delete the link and the requirement still says what it needs. Findings are
read, not swept.
"""
import sys, os, glob, re, argparse
from collections import defaultdict

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml: pip install pyyaml")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODULES = os.path.join(REPO, "docs", "modules")
EXEMPT_SECTIONS = {"Overview", "Implementations", "Credits"}


def load_sources():
    out = {}
    for f in sorted(glob.glob(os.path.join(MODULES, "*", "spec.yml"))):
        try:
            doc = yaml.safe_load(open(f)) or {}
        except yaml.YAMLError:
            continue
        out[doc.get("module") or os.path.basename(os.path.dirname(f))] = doc
    return out


def target_of(link, from_dir):
    """The module a relative link points at, or None."""
    if not link.endswith("spec.md"):
        return None
    parts = os.path.normpath(os.path.join(from_dir, link)).split(os.sep)
    return parts[-2] if len(parts) >= 3 and parts[-3] == "modules" else None


def graph(sources):
    """consumes[m] = what m takes directly; then the transitive closures."""
    consumes = defaultdict(set)
    for m, doc in sources.items():
        here = os.path.join(MODULES, m)
        for v in (doc.get("inputs") or {}).values():
            t = target_of((v or {}).get("page") or "", here)
            if t and t != m:
                consumes[m].add(t)

    def walk(start, step):
        seen, frontier = set(), [start]
        while frontier:
            nxt = [n for m in frontier for n in step(m) if n not in seen and n != start]
            seen.update(nxt)
            frontier = nxt
        return seen

    def parents(m):
        r = sources.get(m, {}).get("refines")
        return [r] if isinstance(r, str) else list(r or [])

    upstream = {m: walk(m, lambda x: consumes.get(x, ())) for m in sources}
    downstream = defaultdict(set)
    for m, ups in upstream.items():
        for u in ups:
            downstream[u].add(m)
    ancestors = {m: walk(m, parents) for m in sources}
    descendants = defaultdict(set)
    for m, above in ancestors.items():
        for a in above:
            descendants[a].add(m)
    return upstream, downstream, ancestors, descendants


GEN = re.compile(r"<!-- gen:.*?<!-- /gen:[a-z-]+ -->", re.S)
HEADING = re.compile(r"^#{1,3} (.+)$")
LINK = re.compile(r"\[([^\]]+)\]\((\.\.?/[^)#\s]*spec\.md)(#[^)\s]*)?\)")


def findings(sources, upstream, downstream, ancestors, descendants, paths):
    pages = {os.path.basename(os.path.dirname(f))
             for f in glob.glob(os.path.join(MODULES, "*", "spec.md"))}
    out = []
    for f in paths:
        m = os.path.basename(os.path.dirname(f))
        # a generated block is the renderer's output, not the author's prose.
        # Blank it but keep its newlines: deleting it shortened the text, and every
        # line number below came out short by that block's own length -- 36 lines on
        # base-cytosol, 33 on s30-lysate, so no constant offset recovered them.
        body = GEN.sub(lambda g: "\n" * g.group(0).count("\n"), open(f).read())
        section = None
        for n, line in enumerate(body.split("\n"), 1):
            h = HEADING.match(line)
            if h:
                section = h.group(1).strip()
                continue
            if section is None or section in EXEMPT_SECTIONS:
                continue
            for mt in LINK.finditer(line):
                t = target_of(mt.group(2), os.path.dirname(f))
                if not t or t == m or t not in pages:
                    continue
                # the abstraction axis is never a finding, and wins over composition
                if t in descendants.get(m, ()) or t in ancestors.get(m, ()):
                    continue
                if t in upstream.get(m, ()):
                    continue
                if t in downstream.get(m, ()):
                    out.append((os.path.relpath(f, REPO), n, section, t, mt.group(1)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*", help="module spec.md files; default is all")
    a = ap.parse_args()

    pattern = os.path.join(MODULES, "*", "spec.md")
    paths = [os.path.abspath(p) for p in a.paths] or sorted(glob.glob(pattern))
    searched = " ".join(a.paths) if a.paths else os.path.relpath(pattern, REPO)
    if not paths:
        print(f"⛔️ nothing to check. searched: {searched}")
        return 0

    sources = load_sources()
    out = findings(sources, *graph(sources), paths)
    for path, n, section, target, text in out:
        print(f"⚠️  {path}:{n} [{section}] links [{text}] -> {target}, "
              f"which is built from this Module.")

    # scope, always: a clean run over the wrong scope reads like a clean corpus
    print(f"\nsearched: {searched}")
    print(f"{len(paths)} page(s) checked against {len(sources)} source(s)")
    if out:
        print(f"⚠️  {len(out)} downstream link(s) outside # Overview. "
              f"Reporting only; see style-guide/principles.md.")
        print("   Delete the link. If the sentence no longer says what this Module "
              "is, does or needs, the content is on the wrong page.")
    else:
        print("✅ no page explains itself through what is built from it.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
