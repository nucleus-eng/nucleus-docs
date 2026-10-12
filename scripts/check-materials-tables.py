#!/usr/bin/env python3
"""check-materials-tables.py — report materials tables that the BOM pipeline
cannot read, or that spell a column a second way.

WHY THIS EXISTS. The materials tables across docs/ were "kinda all over the
place" (Jon, 2026-10-12), and the cause was not sessions writing sloppy tables:
``templates/module-template/spec-functional.md`` shipped the header
``Material | Description | Manufacturer | Part #`` and neither ``Material`` nor
``Description`` was a title ``bom_common.py`` could read. Every page written
from that template lost two columns into the distribution-wide reference and
nothing reported it. E1 fixed the template, E2 taught the parser the retired
spellings, and this is the check that stops the next one.

THREE JOBS, in the order a failure matters:

  1. THE HEADER PARSES AT ALL. ``parse_table_header`` needs a Manufacturer and
     a Part # column. A table it rejects never reaches the reference, and
     nothing anywhere says so. This is the only check whose failure means a
     material is silently missing.

  2. EVERY TITLE IS ON THE ALLOWLIST AND THE REQUIRED THREE ARE PRESENT.
     Jon, 2026-10-12: "one allowed title per column, with a bunch of optional
     columns and a set of required ones", then "required three is fine".

  3. NO PROSE PLACEHOLDER IN Manufacturer OR Part #. ``"Not stated"`` is
     indexed as a real material under the key ('not stated', 'not stated'); an
     em dash is skipped. Found by the Gel Control Experiments session. It bites
     nothing today only because the page writing it is one whose header does
     not parse -- so jobs 1 and 2 are what make this defect reachable, and this
     is what stops it landing.

THE ALLOWLIST IS ``bom_common.py``'s, IMPORTED, NEVER A SECOND COPY. A column
this checker permits and the generator cannot name is silently dropped, which
is the defect being fixed. Four readers of one published order each decided
membership for itself in scripts/orders.py's absence and two were wrong.

REPORT-ONLY BY DEFAULT, counting toward zero. ``--strict`` exits 1 instead, for
when that count reaches zero and the check can block. A checker that has never
been able to fail has not been shown to work, so the fixtures in
scripts/tests/test_check_materials_tables.py fail one job each.

WHAT IT CANNOT SEE. A table with no materials label, no Manufacturer-ish column
and no Part-ish column is indistinguishable from a recipe table, so it is not
audited. ``Item | Used for | Supplier and part number`` is caught only by its
label.

Usage:
    python3 scripts/check-materials-tables.py [paths...]
    python3 scripts/check-materials-tables.py --strict
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Iterator, List, NamedTuple, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent))

from bom_common import (  # noqa: E402
    ALLOWED_TITLES,
    REQUIRED_FIELDS,
    RETIRED_ALIASES,
    _clean_cell,
    _header_field,
    is_placeholder,
    parse_table_header,
    split_row,
)

DEFAULT_ROOTS = ["docs", "templates", "guides"]
SKIP_PARTS = {"generated", "node_modules", ".git", "_build"}

TABLE_SEP = re.compile(r"^\|[\s\-:|]+\|$")
MATERIALS_LABEL = re.compile(r"^\s*:label:\s*(critical-materials|materials-[\w.-]+|bom-[\w.-]+)\s*$")

# A PROMPT TO LOOK, NEVER A VERDICT. A string match cannot know whether a cell
# is prose or a vendor whose name begins "Not"; it can only say the cell reads
# like an apology for a missing value. Kept tight on purpose.
PROSE_PLACEHOLDER = re.compile(
    r"^(not\s+\w+|none|unknown|unrecorded|undetermined|see\s+\w+|ask\s+\w+|\?+)\.?$",
    re.I,
)

# How far above a header row to look for its table's :label:.
LABEL_LOOKBACK = 12

# ALLOWED_TITLES is keyed by FIELD ("part") and valued by TITLE ("Part #"). A
# header cell is a title, so it is checked against the inverse. Keying the test
# on ALLOWED_TITLES directly passes `Name` and `Manufacturer` -- where field and
# title happen to coincide -- and reports `Part #` as off the allowlist on every
# page in the repo, templates included. That is what the first run of this file
# did, and it is why a checker ships with a fixture that fails.
_ALLOWED_BY_TITLE = {title.lower(): field for field, title in ALLOWED_TITLES.items()}


class Finding(NamedTuple):
    path: str
    line: int          # 1-based, the header row
    job: int           # 1, 2 or 3
    message: str


def _norm(cell: str) -> str:
    """A header cell as the alias map sees it: markup stripped, collapsed, cased down."""
    return re.sub(r"\s+", " ", _clean_cell(cell).strip().lower())


def iter_header_rows(lines: List[str]) -> Iterator[tuple]:
    """Yield (index, header_row, data_rows) for every markdown table.

    A header is a pipe row followed by a ``| --- |`` separator. Counting every
    pipe row instead reports cell values as headers -- a sweep on 2026-10-12 did
    exactly that and reported `Reagent` 19 times when it is a Category value.
    """
    for i, line in enumerate(lines[:-1]):
        if not line.strip().startswith("|"):
            continue
        if not TABLE_SEP.match(lines[i + 1].strip()):
            continue
        rows = []
        for j in range(i + 2, len(lines)):
            if not lines[j].strip().startswith("|"):
                break
            rows.append(lines[j])
        yield i, line, rows


def has_materials_label(lines: List[str], header_idx: int) -> bool:
    start = max(0, header_idx - LABEL_LOOKBACK)
    return any(MATERIALS_LABEL.match(l) for l in lines[start:header_idx])


def is_candidate(header: str, labelled: bool) -> bool:
    """A table worth auditing: it says it is a materials table, or it names a
    manufacturer or a part number. Anything else is a recipe table."""
    if labelled:
        return True
    fields = {_header_field(c) for c in split_row(header)}
    return "manufacturer" in fields or "part" in fields


def check_table(path: str, idx: int, header: str, rows: List[str],
                labelled: bool) -> List[Finding]:
    out: List[Finding] = []
    line = idx + 1
    cells = split_row(header)
    cols = parse_table_header(header)

    # --- job 1 -------------------------------------------------------------
    if cols is None:
        fields = {_header_field(c) for c in cells} - {None}
        missing = [f for f in ("manufacturer", "part") if f not in fields]
        out.append(Finding(
            path, line, 1,
            "header does not parse: no %s column, so nothing in this table "
            "reaches the materials reference" % " or ".join(missing)))
        return out  # jobs 2 and 3 need the column map

    # --- job 2 -------------------------------------------------------------
    for cell in cells:
        key = _norm(cell)
        if not key:
            continue
        if key in _ALLOWED_BY_TITLE:
            continue
        if key in RETIRED_ALIASES:
            want = ALLOWED_TITLES[RETIRED_ALIASES[key]]
            out.append(Finding(path, line, 2,
                               "column %r is a retired spelling of %r" % (cell.strip(), want)))
        else:
            out.append(Finding(path, line, 2,
                               "column %r is not on the allowlist" % cell.strip()))
    for field in REQUIRED_FIELDS:
        if field not in cols:
            out.append(Finding(path, line, 2,
                               "required column %r is missing" % ALLOWED_TITLES[field]))

    # --- job 3 -------------------------------------------------------------
    for offset, row in enumerate(rows, start=1):
        values = split_row(row)
        for field in ("manufacturer", "part"):
            i = cols.get(field)
            if i is None or i >= len(values):
                continue
            value = _clean_cell(values[i]).strip()
            if is_placeholder(value):
                continue
            if PROSE_PLACEHOLDER.match(value):
                out.append(Finding(
                    path, line + 1 + offset, 3,
                    "%s reads %r — prose in this column is indexed as a real "
                    "material; use an em dash" % (ALLOWED_TITLES[field], value)))
    return out


def check_file(path: Path) -> List[Finding]:
    try:
        lines = path.read_text(encoding="utf-8").split("\n")
    except (OSError, UnicodeDecodeError):
        return []
    out: List[Finding] = []
    for idx, header, rows in iter_header_rows(lines):
        labelled = has_materials_label(lines, idx)
        if not is_candidate(header, labelled):
            continue
        out.extend(check_table(str(path), idx, header, rows, labelled))
    return out


def walk(roots: List[str]) -> Iterator[Path]:
    for root in roots:
        base = Path(root)
        if base.is_file():
            yield base
            continue
        for p in sorted(base.rglob("*.md")):
            if SKIP_PARTS & set(p.parts):
                continue
            yield p


def main(argv: Optional[List[str]] = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*", default=None,
                    help="files or directories to check (default: %s)" % ", ".join(DEFAULT_ROOTS))
    ap.add_argument("--strict", action="store_true",
                    help="exit 1 on any finding (default: report only)")
    args = ap.parse_args(argv)

    findings: List[Finding] = []
    for path in walk(args.paths or DEFAULT_ROOTS):
        findings.extend(check_file(path))

    if not findings:
        print("✅ No materials-table findings.")
        return 0

    by_job = {1: [], 2: [], 3: []}
    for f in findings:
        by_job[f.job].append(f)

    titles = {
        1: "header does not parse — these materials reach nothing",
        2: "column title off the allowlist, or a required column missing",
        3: "prose placeholder where a value is indexed",
    }
    for job in (1, 2, 3):
        if not by_job[job]:
            continue
        print("\n--- job %d: %s ---" % (job, titles[job]))
        for f in by_job[job]:
            print("  %s:%d  %s" % (f.path, f.line, f.message))

    print("\n%d finding(s) in %d file(s)."
          % (len(findings), len({f.path for f in findings})))
    print("Report-only. `--strict` exits 1; flip CI to it when this count "
          "reaches zero.")
    return 1 if args.strict else 0


if __name__ == "__main__":
    raise SystemExit(main())
