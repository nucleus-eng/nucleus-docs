#!/usr/bin/env python3
"""
check-bom-labels.py — enforce the lab-ready pipeline's download/label
conventions on process pages (see issue #10).

The lab-ready pipeline (scripts/build-protocols.py) generates a protocol PDF, a
Bill of Materials PDF, and a materials CSV from each process page; download
buttons point at the generated artifacts under ``generated/<slug>-*.pdf`` where
``<slug>`` is the process's directory name. This check enforces:

  1. A ``bom-<...>`` table label must match its directory — ``bom-<dir-name>``.
     A renamed directory with a stale label silently stops generating the BOM.
  2. A page that links a generated BOM download (``generated/<slug>-bom.pdf``)
     must have a ``bom-<slug>`` table, or the download dangles / the build fails.
  3. Any protocol-PDF download button must point at ``generated/<slug>-protocol.pdf``
     — not a ``TODO``/placeholder path or some other page's PDF. (Catches the
     stale-button class that slipped through the initial rollout: a page that
     migrated from stub or template still pointing at the old target.)

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
# Any `download <target>` reference, to inspect the target.
DOWNLOAD_RE = re.compile(r"download\s*<([^>]+)>")


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

    # Rule 3: a protocol-PDF download button must point at the generated path.
    expected_protocol = f"generated/{slug}-protocol.pdf"
    for i, line in enumerate(lines, start=1):
        for target in DOWNLOAD_RE.findall(line):
            target = target.strip()
            is_protocol_ref = "protocol" in target.lower() and (
                target.lower().endswith(".pdf") or "todo" in target.lower()
            )
            if is_protocol_ref and target != expected_protocol:
                violations.append(
                    (i, f"protocol download '{target}' should be '{expected_protocol}'")
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
        print(f"\n❌ {total} download/label convention violation(s) found.")
        return 1
    print(f"✅ {len(pages)} process page(s) OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
