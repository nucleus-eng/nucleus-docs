#!/usr/bin/env python3
"""Keep the figures written in bare mOsm audited, and flag any that are not.

WHAT A BARE mOsm MEANS. A figure from a recipe or a calculation is an osmolarity and
takes mOsm/L. A reading is an osmolality and takes mOsm/kg. A figure whose origin is not
recorded has no denominator, so it is written in mOsm and nothing more. That is the mark.

THE PROBLEM THE MARK HAS. A bare mOsm is also what somebody writes who forgot the unit.
Nothing in the text tells the two apart. So this script keeps a list, in
scripts/osmotic-unrecorded.yml, of every bare figure somebody has looked at and could not
trace. Bare means audited-and-unknown when it is on the list, and unaudited when it is not.

WHAT IT DOES. It counts each figure per file and compares the count with the list.
  - A bare figure beyond its listed count fails: either give it mOsm/L or mOsm/kg, or look
    for its origin and add it to the list when there is none.
  - A listed figure that is now fewer, or gone, is reported and does not fail. Remove the
    entry, because the figure has gained a unit or left the page.
  - A denominator other than /L or /kg fails (mOsm/mL, mOsm/g).
Counting per file and figure, not per line, so an edit that moves a line does not touch the
list. It reads .md and .yml under docs/. It does not see a figure written with no unit at
all ("negligible against 920"): no pattern can tell that number from any other.

It prints the files it read, and exits 2 when it read none, because a clean run over nothing
looks identical to a clean run.
"""
from __future__ import annotations
import argparse, re, sys
from collections import Counter
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml: pip install pyyaml")

REPO = Path(__file__).resolve().parent.parent
LEDGER = Path(__file__).resolve().parent / "osmotic-unrecorded.yml"
BARE = re.compile(r"(?<![\w.])(\d+(?:\.\d+)?)\s?mOsm(?![/\w])")
ODD = re.compile(r"mOsm/(?!L\b|kg\b)\S+")


def scan(root: Path):
    counts: Counter = Counter()
    odd: list[tuple[str, int, str]] = []
    files = 0
    for path in sorted(root.glob("docs/**/*")):
        if path.suffix not in (".md", ".yml") or "generated" in path.parts:
            continue
        files += 1
        rel = path.relative_to(root).as_posix()
        for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            for m in BARE.finditer(line):
                counts[(rel, m.group(1))] += 1
            for m in ODD.finditer(line):
                odd.append((rel, n, m.group(0)))
    return files, counts, odd


def load_ledger(path: Path) -> Counter:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    out: Counter = Counter()
    for e in data.get("unrecorded", []):
        out[(e["file"], str(e["figure"]))] += int(e["count"])
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", type=Path, default=REPO)
    ap.add_argument("--ledger", type=Path, default=LEDGER)
    ap.add_argument("--print-ledger", action="store_true",
                    help="print the current counts as ledger entries and exit")
    a = ap.parse_args(argv)
    files, counts, odd = scan(a.root)
    print(f"read {files} file(s) under {a.root / 'docs'}; {sum(counts.values())} bare figure(s) in {len(counts)} (file, figure) pair(s)")
    if files == 0:
        print("⛔️ read no files: a clean result over nothing is not a result")
        return 2
    if a.print_ledger:
        print("unrecorded:")
        for (f, fig), c in sorted(counts.items()):
            print(f"  - {{file: {f}, figure: \"{fig}\", count: {c}}}")
        return 0
    if not a.ledger.exists():
        print(f"⛔️ no ledger at {a.ledger}")
        return 2
    listed = load_ledger(a.ledger)
    bad = 0
    for key, c in sorted(counts.items()):
        if c > listed.get(key, 0):
            f, fig = key
            print(f"⛔️ {f}: {c - listed.get(key, 0)} bare {fig} mOsm not on the list. Give it mOsm/L or mOsm/kg, or add it to {a.ledger.name} once its origin has been looked for and not found.")
            bad += 1
    for f, n, t in odd:
        print(f"⛔️ {f}:{n}: '{t}' is not a denominator this corpus uses. Write mOsm/L or mOsm/kg.")
        bad += 1
    for key, c in sorted(listed.items()):
        if counts.get(key, 0) < c:
            print(f"ℹ️  {key[0]}: the list has {c} of {key[1]} mOsm and the page has {counts.get(key, 0)}. Remove or lower the entry.")
    if bad:
        print(f"⛔️ {bad} finding(s).")
        return 1
    print("✅ every bare figure is on the list.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
