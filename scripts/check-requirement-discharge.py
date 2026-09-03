#!/usr/bin/env python3
"""
check-requirement-discharge.py — a Requirement whose own example satisfier is
already inside the page should say so.

`# Requirements` names what a composer must supply. When a composed Module
writes

    Requires a lipid compartment for PLA1 to lyse (e.g. [Chicago Chassis](...))

and the Chicago Chassis is one of its own constituents, the page is asking the
reader for something it already contains. The reader cannot tell that from the
text, so the Module reads as harder to use than it is — and a composition check
reading the same line cannot tell a Requirement that was met from one that was
dropped.

Two pages already write the met case correctly, which is where the wording
below comes from:

    Requires pT7 transcription and translation (e.g. [Base Cytosol](...)),
    supplied here by the [Chicago Chassis](...).

So this check has a positive control built into the corpus: if it ever reports
`atc-sensing-cell` or `theophylline-sensing-cell` for pT7, the matcher broke.

Scope. Only `e.g.` links count as satisfiers. A `see` link is a cross-reference
to the Module that *imposes* the constraint — `reporter-lacz` is the source of
the LacZ/CPRG separation requirement, not a thing that meets it — and reporting
those would be wrong. Pages that use `e.g.` where they mean `see` will show up
here; that is also worth fixing, and the fix is the same edit.

Waivers go on the page as an HTML comment naming the module and the reason:

    <!-- requirement-discharge: chicago-chassis (the composer may substitute
         their own chassis, so the requirement stays open) -->

Usage:
    python3 scripts/check-requirement-discharge.py
    python3 scripts/check-requirement-discharge.py docs/modules/atc-cascade/
"""

import re
import sys
from pathlib import Path

MODULES_ROOT = Path("docs/modules")

SPEC_LINK = r'\]\(\.\./([a-z0-9-]+)/spec\.md'
# "supplied here by", "as supplied by" — the page saying the requirement is met.
DISCHARGED = re.compile(r"supplied here by|as supplied by|provided here by", re.I)
WAIVER = re.compile(r"<!--\s*requirement-discharge:\s*([a-z0-9-]+)")


def section(text, name):
    m = re.search(r"^# " + name + r"\s*\n(.*?)(?=^# |\Z)", text, re.S | re.M)
    return m.group(1) if m else ""


def constituents(text):
    return [m.group(1) for m in re.finditer(SPEC_LINK, section(text, "Constituent Modules"))]


def closure(name, graph, seen=None):
    seen = set() if seen is None else seen
    for child in graph.get(name, []):
        if child not in seen:
            seen.add(child)
            closure(child, graph, seen)
    return seen


def atoms(requirements):
    """Top-level paragraphs, with admonition blocks removed."""
    out, depth = [], 0
    for line in requirements.split("\n"):
        if re.match(r"^:{3,}\{", line):
            depth += 1
            continue
        if re.match(r"^:{3,}\s*$", line):
            depth = max(0, depth - 1)
            continue
        if depth == 0:
            out.append(line)
    return [p.strip() for p in "\n".join(out).split("\n\n") if p.strip()]


def satisfiers(atom):
    """Modules named as an example satisfier — `e.g. [X](../x/spec.md)`.

    Bounded to the clause the `e.g.` opens, so a later `see [Y]` in the same
    paragraph is not swept in.
    """
    found = []
    for m in re.finditer(r"e\.g\.,?\s*", atom):
        clause = atom[m.end():]
        cut = re.search(r"\)\s*[.;]|\bsee\b", clause)
        if cut:
            clause = clause[: cut.start() + 1]
        found += re.findall(SPEC_LINK, clause)
    return found


def main(argv=None):
    argv = sys.argv[1:] if argv is None else list(argv)
    if not MODULES_ROOT.is_dir():
        print("error: run from the repository root", file=sys.stderr)
        return 2

    specs = {p.parent.name: p for p in MODULES_ROOT.glob("*/spec.md")}
    if not specs:
        print("error: no module specs found", file=sys.stderr)
        return 2

    texts = {name: path.read_text(encoding="utf-8") for name, path in specs.items()}
    graph = {name: constituents(text) for name, text in texts.items()}

    targets = sorted(specs)
    if argv:
        wanted = {Path(a.rstrip("/")).name for a in argv}
        targets = [t for t in targets if t in wanted]
        if not targets:
            print(f"error: no module spec matched {sorted(wanted)}", file=sys.stderr)
            return 2

    findings, checked, positive_control = [], 0, 0
    for name in targets:
        if not graph.get(name):
            continue  # a leaf discharges nothing
        checked += 1
        own = closure(name, graph)
        waived = set(WAIVER.findall(texts[name]))
        for atom in atoms(section(texts[name], "Requirements")):
            inside = sorted({s for s in satisfiers(atom) if s in own} - waived)
            if not inside:
                continue
            if DISCHARGED.search(atom):
                positive_control += 1
                continue
            first = atom.split("\n")[0]
            head = first if len(first) <= 90 else first[:87] + "..."
            findings.append(
                f"{name}: requires something its own {', '.join(inside)} supplies, "
                f"but does not say so\n         {head}"
            )

    for f in findings:
        print(f"error: {f}")

    if findings:
        pages = len({f.split(":")[0] for f in findings})
        print(
            f"\n{len(findings)} undischarged Requirement(s) across {pages} page(s). "
            'Add "supplied here by [X]", or drop the line if the composer never '
            "supplies it."
        )
        return 1

    if not checked:
        # A scan that reports zero has to be shown capable of reporting non-zero.
        # No composed Modules means the corpus this check is for is not here —
        # on `main` today the DevCells specs are unmerged — so a green tick would
        # be a clean number that measured nothing.
        print(
            "error: no composed Module pages found, so this check proved nothing. "
            "It needs specs with both `# Constituent Modules` and `# Requirements`.",
            file=sys.stderr,
        )
        return 2

    note = f" {positive_control} already marked as supplied." if positive_control else ""
    print(f"✅ No undischarged Requirements. {checked} composed page(s) checked.{note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
