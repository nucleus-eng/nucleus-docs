#!/usr/bin/env python3
"""Flag markdown tables whose rows do not match their header's column count.

WHY THIS EXISTS. Suggested by the compositional-biology-theory session on
2026-09-29, after a seven-column row went into a five-column table there and all
six of that repo's guards passed. Nothing in this repo asserted table shape
either, and this corpus is table-heavy: composition tables, bills of materials,
Designs tables, the module index. A row with the wrong column count renders as a
dropped or shifted cell, which reads as a missing figure rather than as a broken
table.

WHAT IT DOES NOT DO. It does not check that a cell holds the right kind of
thing; check-composition.py and check-bom-labels.py do that for the two table
kinds that have a contract. This checks shape only.

Escaped pipes (\\|) and pipes inside inline code (`a|b`) are not separators, and
both appear in this corpus.
"""
from __future__ import annotations
import re, subprocess, sys
from pathlib import Path

DEFAULT_ROOTS = ["docs/", "templates/", "guides/", "style-guide/"]
SEP = re.compile(r"^\s*\|?[\s:\-|]+\|[\s:\-|]*$")


def cells(line: str) -> int:
    """Column count of one table row, ignoring pipes that do not separate."""
    # inline code first: a pipe inside backticks is content
    masked = re.sub(r"`[^`]*`", lambda m: "\x00" * len(m.group(0)), line)
    masked = masked.replace(r"\|", "\x00\x00")
    row = masked.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    return len(row.split("|"))


def check_file(path: Path) -> list[tuple[int, str]]:
    out: list[tuple[int, str]] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    header_n = None
    header_line = 0
    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if "|" not in stripped:
            header_n = None
            continue
        if SEP.match(stripped) and header_n is None and i >= 2 and "|" in lines[i - 2]:
            header_n = cells(lines[i - 2])
            header_line = i - 1
            continue
        if header_n is None:
            continue
        if SEP.match(stripped):
            continue
        n = cells(line)
        if n != header_n:
            out.append((i, f"row has {n} column(s), header at line {header_line} has {header_n}"))
    return out


def find_files(roots: list[str]) -> list[Path]:
    r = subprocess.run(["git", "ls-files"] + roots, capture_output=True, text=True)
    return sorted(
        Path(p) for p in r.stdout.splitlines()
        if p.endswith(".md") and "generated" not in Path(p).parts
    )


def main() -> int:
    roots = [a for a in sys.argv[1:] if not a.startswith("-")] or DEFAULT_ROOTS
    files = find_files(roots)
    errors = 0
    for f in files:
        if not f.exists():
            continue
        for lineno, msg in check_file(f):
            print(f"{f}:{lineno}  {msg}")
            errors += 1
    if errors:
        print(f"\n❌ {errors} malformed table row(s). A wrong column count drops or shifts a cell.")
        return 1
    print(f"✅ Every table row matches its header. {len(files)} file(s) checked.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
