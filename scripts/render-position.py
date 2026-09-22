#!/usr/bin/env python3
"""Render a Module's position in the refinement order, from `refines:`.

WHY THIS EXISTS. `Abstract:` came off the class titles on Jon's ruling of
2026-09-21: "they all exist within their own poset somewhere, so they're all
some level of abstract vs concrete, not some binary." The prefix did one job a
bare title does not, which is warn a reader on arrival that the page has no
implementation. Removing it and putting nothing back would be a net loss of
signal, so the replacement ships in the same tranche. Jon: "both, and ship the
position line with it."

WHAT IT REPLACES THE WORD WITH IS MORE THAN THE WORD CARRIED. A title prefix is
one bit. A position names the parent above and every child below, which is the
order itself rather than a flag over it. Four of the seven sourced classes are
BOTH a parent and a child, so a binary has to pick a side for the majority of
them and no pick is correct. That is the ruling stated as arithmetic.

`refines:` IS A SINGLE UPWARD POINTER AND THE DOWNWARD HALF IS DERIVED. There is
no `refined_by` key and there must not be, because it would be a second source
for one fact. This builds the reverse index in one pass.

AN OMITTED `refines:` IS TWO DIFFERENT THINGS AND THIS CANNOT TELL THEM APART.
The schema allows a Module to omit the key when it is a root, and ALSO when its
immediate parent has no page on the branch it sits on. Both look identical here,
so the line says "nothing declared" rather than "a root". Unknown is not a pass.

    python3 scripts/render-position.py                       # every module
    python3 scripts/render-position.py docs/modules/pore      # one
    python3 scripts/render-position.py --embed                # write the blocks
"""
import collections
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent / "docs" / "modules"
BEGIN = "<!-- gen:position -->"
END = "<!-- /gen:position -->"


def load() -> tuple[dict[str, str], dict[str, list[str]]]:
    """(parent by module, children by module). Sources only; a page with no
    source has no declared position and is reported as such rather than skipped."""
    parent: dict[str, str] = {}
    for d in sorted(ROOT.iterdir()):
        f = d / "spec.yml"
        if not f.is_file():
            continue
        doc = yaml.safe_load(f.read_text()) or {}
        if doc.get("refines"):
            parent[d.name] = doc["refines"]
    children: dict[str, list[str]] = collections.defaultdict(list)
    for k, v in parent.items():
        children[v].append(k)
    return parent, {k: sorted(v) for k, v in children.items()}


def ancestors(slug: str, parent: dict) -> list[str]:
    """`slug` first, then up to its root. A NODE IS ITS OWN ANCESTOR.

    That is not a convenience. It is what makes `meet(gel, gel-ulga)` return
    `gel` rather than `container`: where two operands agree, the meet IS the one
    they agree on, and a chain that started at the parent would skip it.
    """
    out, seen = [], set()
    while slug and slug not in seen:
        out.append(slug)
        seen.add(slug)
        slug = parent.get(slug)
    return out


def meet(slugs, parent: dict) -> str | None:
    """The deepest class every one of `slugs` refines, or None.

    None MEANS NO COMMON ANCESTOR AT ALL, not "the root". `meet(detector-ph,
    gel-ulga)` is None because they sit in different trees, and a caller that
    collapses that into a root has turned a failure into an answer. The meet
    renderer marks it; it does not fill it in.

    CORRECT ONLY BECAUSE `refines:` IS A SINGLE STRING. One parent per node makes
    this a forest, where a meet is unique or absent. The day the key becomes a
    list this returns a plausible wrong answer and says nothing, so the
    assumption is stated here rather than in a commit message.
    """
    chains = [ancestors(s, parent) for s in slugs]
    if not chains:
        return None
    for cand in chains[0]:                    # deepest first
        if all(cand in c for c in chains[1:]):
            return cand
    return None


def both_parent_and_child(parent: dict, children: dict) -> list[str]:
    """Classes in the middle of a chain. A binary label has to pick a side for
    each of these and no pick is correct, which is the whole naming ruling."""
    return sorted(n for n in children if n in parent)


def one_member_classes(children: dict) -> list[str]:
    """A class with exactly one member is a rename wearing a class page.

    Jon, 2026-09-21: a gel class with one member is not a gel class. Empty today,
    which is the point of printing the denominator beside it: an empty result is
    a measurement only when you know what was measured.
    """
    return sorted(n for n, k in children.items() if len(k) == 1)


def link(slug: str) -> str:
    return f"[`{slug}`](../{slug}/spec.md)"


def line(slug: str, parent: dict, children: dict) -> str:
    up = f"Refines {link(parent[slug])}." if slug in parent else \
         "Refines nothing declared."
    kids = children.get(slug) or []
    down = ("Refined by " + ", ".join(link(k) for k in kids) + "."
            if kids else "Refined by nothing on this branch.")
    return f"**Position.** {up} {down}"


def embed(slug: str, text: str) -> bool | None:
    """Rewrite the marked block. None if the page carries no markers, which is a
    finding rather than a crash: nobody decided where the line goes."""
    page = ROOT / slug / "spec.md"
    if not page.is_file():
        return None
    t = page.read_text()
    if BEGIN not in t or END not in t:
        return None
    i, j = t.index(BEGIN), t.index(END) + len(END)
    new = t[:i] + f"{BEGIN}\n{text}\n{END}" + t[j:]
    if new == t:
        return False
    page.write_text(new)
    return True


if __name__ == "__main__":
    parent, children = load()
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    slugs = ([Path(a.rstrip("/")).name for a in args] if args
             else sorted(d.name for d in ROOT.iterdir()
                         if (d / "spec.yml").is_file()))
    if "--embed" in sys.argv:
        counts: collections.Counter = collections.Counter()
        for s in slugs:
            counts[{None: "no markers", True: "updated",
                    False: "unchanged"}[embed(s, line(s, parent, children))]] += 1
        for k, v in sorted(counts.items()):
            print(f"{v:4}  {k}")
    else:
        for s in slugs:
            print(f"{s}\n  {line(s, parent, children)}")
    # THE DENOMINATOR, EVERY RUN. A module with no position is not a leaf and is
    # not a root. It is a module nothing has placed.
    placed = {s for s in slugs if s in parent or s in children}
    print(f"\n{len(placed)} of {len(slugs)} sources have a declared position; "
          f"{len(slugs) - len(placed)} are placed by nothing.", file=sys.stderr)
    both = both_parent_and_child(parent, children)
    print(f"{len(both)} of {len(children)} parents are also children: "
          f"{', '.join(both) or 'none'}", file=sys.stderr)
    solo = one_member_classes(children)
    print(f"{len(solo)} of {len(children)} classes have exactly one member: "
          f"{', '.join(solo) or 'none'}", file=sys.stderr)
