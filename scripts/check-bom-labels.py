#!/usr/bin/env python3
"""
check-bom-labels.py — enforce the lab-ready pipeline's BOM conventions on
process pages (see issue #10).

The lab-ready pipeline (scripts/build-protocols.py) generates a Bill of
Materials PDF + materials CSV from a table labeled ``bom-<slug>``, where
``<slug>`` is the process's directory name. Download buttons point at the
generated artifacts. Two things must hold or the build breaks / artifacts go
missing:

  1. A ``bom-<...>`` table label must match its directory — ``bom-<dir-name>``.
     A renamed directory with a stale label silently stops generating the BOM.
  2. A page that links a generated BOM download (``generated/<slug>-bom.pdf``)
     must have a ``bom-<slug>`` table, or the download dangles / the build fails.

Reports violations as ``file:line`` and exits non-zero if any are found.

Usage:
    python3 scripts/check-bom-labels.py [paths...]
    python3 scripts/check-bom-labels.py            # all of docs/processes/
"""

import re
import sys
from pathlib import Path

PROCESSES_ROOT = Path("docs/processes")

BOM_LABEL_RE = re.compile(r"^\s*:label:\s*(bom-[A-Za-z0-9._-]+)\s*$")
BOM_DOWNLOAD_RE = re.compile(r"download\s*<generated/([A-Za-z0-9._-]+)-bom\.pdf>")


def find_pages(args):
    targets = [Path(a) for a in args] if args else [PROCESSES_ROOT]
    pages = []
    for target in targets:
        if target.is_file() and target.suffix == ".md":
            pages.append(target)
            continue
        for pattern in ("**/main.md", "**/*-main.md"):
            pages.extend(target.glob(pattern))
    return sorted(set(pages))


def check_page(path):
    """Return a list of (line, message) violations for one page."""
    slug = path.parent.name
    expected = f"bom-{slug}"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    violations = []
    has_matching_label = False

    for i, line in enumerate(lines, start=1):
        m = BOM_LABEL_RE.match(line)
        if m:
            label = m.group(1)
            if label == expected:
                has_matching_label = True
            else:
                violations.append(
                    (i, f"BOM table label '{label}' does not match directory — expected '{expected}'")
                )

    for i, line in enumerate(lines, start=1):
        d = BOM_DOWNLOAD_RE.search(line)
        if d and not has_matching_label:
            violations.append(
                (i, f"links a BOM download but the page has no '{expected}' labeled table")
            )

    return violations


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not PROCESSES_ROOT.exists() and not args:
        print(f"ERROR: '{PROCESSES_ROOT}' not found — run from the repo root.")
        return 1

    pages = find_pages(args)
    total = 0
    for page in pages:
        for line, msg in check_page(page):
            print(f"{page}:{line}  {msg}")
            total += 1

    if total:
        print(f"\n❌ {total} BOM-label violation(s) found.")
        return 1
    print(f"✅ {len(pages)} process page(s) OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
