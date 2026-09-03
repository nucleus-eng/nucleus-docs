#!/usr/bin/env python3
"""
check-implementations.py — the `# Implementations` section of a Module spec
lists Implementations, and lists all of them.

Two failures, both of which a read-through misses.

  CATEGORY: an entry under `# Implementations` that points at another Module.
  A cascade is a Module, not an Implementation, however composed it is. Only
  pages under docs/implementations/ belong in this section.

  COVERAGE: an Implementation names the Modules it is built from. Every one of
  those Modules should list it back. The relationship is symmetric and the
  reverse half is the one that rots — nobody revisits twelve Module pages when
  an Implementation gains a Module.

Coverage is advisory: an Implementation may legitimately use a Module in
passing without that Module wanting a backlink. Category is an error.

Links inside an admonition — note, warning, attention and their siblings — do not
count as usage: a note saying two Modules are *not* interchangeable names both,
and is a contrast rather than a claim. Declarative containers such as
``{table}``, ``{figure}`` and ``{card}`` are still read. So a real usage claim
written inside an admonition is invisible here.

Usage:
    python3 scripts/check-implementations.py
    python3 scripts/check-implementations.py --strict   # coverage fails too
"""

import re
import sys
from pathlib import Path

MODULES = Path("docs/modules")
IMPLS = Path("docs/implementations")

LINK = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


# Directives that carry commentary about a page rather than its content. A
# closed list on purpose: `{table}`, `{figure}`, `{tab-item}`, `{card}` and
# `{grid}` are declarative containers, and `:::{table}` with a `:label:` is this
# repo's dominant table convention — 117 of them across 52 files. Stripping
# every `:::` block would mean that giving an Implementation's Modules table a
# caption, which is how every mature page here is written, silently zeroed every
# usage claim on it and left this check reporting clean.
ADMONITIONS = {
    "attention", "caution", "danger", "hint",
    "note", "seealso", "tip", "warning",
}


def body(text: str) -> str:
    """The page with admonition blocks removed.

    A link inside a note or warning is commentary, not a claim. London DevCell
    links the IV-HSL Emitter inside a `:::{note}` in order to say the two are
    *not* interchangeable — different analyte, different receptor. Counting that
    as usage would have the checker demand a backlink asserting a relation the
    prose explicitly denies, and on an Implementation page there is no way to
    describe a contrast without naming what you are contrasting against.

    The consequence, which is the reason it is written down here: **a genuine
    usage claim inside an admonition is invisible to this check.** Put the claim
    in the body.
    """
    out, stack = [], []
    for line in text.splitlines():
        stripped = line.lstrip()
        opening = re.match(r"^:{3,}\{([a-z-]+)\}", stripped)
        if opening:
            stack.append(opening.group(1))
            continue
        if re.match(r"^:{3,}\s*$", stripped):
            if stack:
                stack.pop()
            continue
        if not any(d in ADMONITIONS for d in stack):
            out.append(line)
    return "\n".join(out)


def section(text: str, heading: str) -> str:
    if heading not in text:
        return ""
    return text.split(heading, 1)[1].split("\n# ", 1)[0]


def slug(target: str, kind: str) -> str | None:
    """Return the <name> of a docs/<kind>/<name>/ link, else None.

    Sibling links inside docs/modules/ are written `../other/spec.md`, with no
    `modules/` segment to match on, so those are recognized by shape.
    """
    m = re.search(rf"{kind}/([a-z0-9._-]+)/", target)
    if m:
        return m.group(1)
    if kind == "modules" and (m := re.fullmatch(r"\.\./([a-z0-9._-]+)/spec\.md", target)):
        return m.group(1)
    return None


def main() -> int:
    strict = "--strict" in sys.argv

    # what each Implementation says it is built from
    impl_uses: dict[str, set[str]] = {}
    for main_md in sorted(IMPLS.rglob("main.md")):
        name = main_md.parent.name
        text = main_md.read_text(encoding="utf-8")
        impl_uses[name] = {
            s for t in LINK.findall(body(text)) if (s := slug(t, "modules"))
        }

    # what each Module lists under # Implementations
    listed: dict[str, set[str]] = {}
    category = []
    for spec in sorted(MODULES.rglob("spec.md")):
        name = spec.parent.name
        sec = section(spec.read_text(encoding="utf-8"), "# Implementations")
        impls, mods = set(), set()
        for t in LINK.findall(sec):
            if s := slug(t, "implementations"):
                impls.add(s)
            elif s := slug(t, "modules"):
                mods.add(s)
        listed[name] = impls
        for m in sorted(mods):
            category.append(
                f"{spec}: lists Module '{m}' under # Implementations — "
                "a Module is not an Implementation"
            )

    coverage = []
    for impl, used in sorted(impl_uses.items()):
        for mod in sorted(used):
            if mod in listed and impl not in listed[mod]:
                coverage.append(
                    f"docs/modules/{mod}/spec.md: used by '{impl}' "
                    "but does not list it under # Implementations"
                )

    for f in category:
        print(f"error: {f}")
    for f in coverage:
        print(f"{'error' if strict else 'warning'}: {f}")

    if category or (strict and coverage):
        print(
            f"\n{len(category)} category error(s), {len(coverage)} coverage gap(s)."
        )
        return 1
    if coverage:
        print(
            f"\n{len(coverage)} coverage gap(s) (advisory). "
            f"{len(impl_uses)} implementation(s) checked."
        )
        return 0
    print(f"✅ Implementations sections are consistent. {len(listed)} module(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
