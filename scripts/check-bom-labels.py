#!/usr/bin/env python3
"""
check-bom-labels.py — enforce the lab-ready pipeline's BOM conventions on
process pages (issues #10, #108).

The lab-ready pipeline (scripts/build-protocols.py) generates a protocol PDF, a
Bill of Materials PDF, and a materials CSV from each process page. A page's BOM
may be supplied as EITHER an inline table labeled ``bom-<slug>`` OR an uploaded
``resources/<slug>-bom.csv`` (``<slug>`` = the process's directory name).
Download buttons point at ``generated/<slug>-*.pdf``. This fast, no-toolchain
check enforces:

  1. A ``bom-<...>`` table label must match its directory — ``bom-<dir-name>``.
     A renamed directory with a stale label silently stops generating the BOM.
  2. A page that links a generated BOM download must have a backing source —
     either a ``bom-<slug>`` table or ``resources/<slug>-bom.csv`` — or the
     download dangles / the build fails.
  3. A BOM download button must point at the canonical ``generated/<slug>-bom.pdf``
     — not a misnamed path. (Catches ``generated/bom-1onepot.pdf``, which the
     pipeline never produces, so it escaped the old canonical-only regex.)
  4. Any protocol-PDF download button must point at ``generated/<slug>-protocol.pdf``.
  5. **Agreement:** if a page has BOTH an inline ``bom-<slug>`` table AND a
     ``resources/<slug>-bom.csv``, the two must be row-for-row identical after
     normalization — otherwise the rendered page and the uploaded file disagree.
  6. **Orphans / misnaming:** a standalone ``bom-*.md`` file in a process dir
     (the pre-pipeline anti-pattern), or a ``resources/*bom*.csv`` not named
     ``<slug>-bom.csv``, is flagged. A BOM source on a page with no ``# Protocol``
     (so the pipeline skips it) is flagged too.

Reports violations as ``file:line`` and exits non-zero if any are found.

Usage:
    python3 scripts/check-bom-labels.py [paths...]
    python3 scripts/check-bom-labels.py            # all of docs/processes/
"""

import re
import sys
from pathlib import Path

# Shared definition of how a BOM table is read / what "equal" means.
from bom_common import (  # noqa: E402  (sibling module, resolved via sys.path[0])
    canon_csv,
    csv_to_table_rows,
    extract_bom_table,
    table_to_csv,
)

PROCESSES_ROOT = Path("docs/processes")

BOM_LABEL_RE = re.compile(r"^\s*:label:\s*(bom-[A-Za-z0-9._-]+)\s*$")
# Loose: any generated BOM-PDF download target, however (mis)named. Lets us
# recognize a misnamed BOM button as a BOM button and flag it (rule 3).
BOM_DOWNLOADISH_RE = re.compile(r"generated/[^>]*bom[^>]*\.pdf", re.IGNORECASE)
# Any `download <target>` reference, to inspect the target.
DOWNLOAD_RE = re.compile(r"download\s*<([^>]+)>")
# A standalone orphan BOM page filename (pre-pipeline anti-pattern).
ORPHAN_BOM_MD_RE = re.compile(r"^bom-.*\.md$", re.IGNORECASE)


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


def _has_protocol(text):
    return any(
        re.match(r"^#\s+protocol\s*$", line.strip(), re.IGNORECASE)
        for line in text.splitlines()
    )


def _label_line(lines, slug):
    """1-based line number of the ``:label: bom-<slug>`` line, or None."""
    for i, line in enumerate(lines, start=1):
        if line.strip() == f":label: bom-{slug}":
            return i
    return None


def check_agreement(inline_rows, csv_text, slug, label_line, path):
    """Compare an inline bom-<slug> table against resources/<slug>-bom.csv.
    Both go through one normalization (canon_csv over table_to_csv / the CSV
    text) so they compare equal iff they carry the same data. Returns a list of
    (line, message) violations anchored at the label line."""
    anchor = label_line or 1
    inline = canon_csv(table_to_csv(inline_rows))
    # Re-canonicalize the uploaded CSV through the same table path the generator
    # uses (csv -> table rows -> table_to_csv) so markup/formatting normalize the
    # same way on both sides.
    uploaded = canon_csv(table_to_csv(csv_to_table_rows(csv_text)))

    violations = []
    if len(inline) != len(uploaded):
        violations.append((anchor,
            f"BOM disagreement: inline table has {len(inline)} row(s) but "
            f"resources/{slug}-bom.csv has {len(uploaded)} — they must match"))
        return violations  # row counts differ; per-row diff would be noise

    diffs = []
    for r, (a, b) in enumerate(zip(inline, uploaded)):
        if len(a) != len(b):
            diffs.append(f"row {r + 1}: inline has {len(a)} column(s), "
                         f"CSV has {len(b)}")
            continue
        for c, (av, bv) in enumerate(zip(a, b)):
            if av != bv:
                diffs.append(f"row {r + 1} col {c + 1}: "
                             f"inline {av!r} != CSV {bv!r}")
                break
    for d in diffs[:5]:
        violations.append((anchor, f"BOM disagreement ({d})"))
    if len(diffs) > 5:
        violations.append((anchor,
            f"BOM disagreement: ...and {len(diffs) - 5} more row(s)"))
    return violations


def check_page(path):
    """Return a list of (line, message) violations for one process page."""
    slug = path.parent.name
    expected = f"bom-{slug}"
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()

    violations = []

    # Rule 1: any bom-<...> label on the page must match the directory.
    has_matching_label = False
    for i, line in enumerate(lines, start=1):
        m = BOM_LABEL_RE.match(line)
        if m:
            if m.group(1) == expected:
                has_matching_label = True
            else:
                violations.append((i,
                    f"BOM table label '{m.group(1)}' does not match directory "
                    f"— expected '{expected}'"))

    csv_path = path.parent / "resources" / f"{slug}-bom.csv"
    has_csv = csv_path.is_file()
    has_bom_source = has_matching_label or has_csv

    # Rules 2 & 3: BOM download buttons.
    canonical_bom = f"generated/{slug}-bom.pdf"
    for i, line in enumerate(lines, start=1):
        for target in DOWNLOAD_RE.findall(line):
            target = target.strip()
            if not BOM_DOWNLOADISH_RE.search(target):
                continue
            if target != canonical_bom:
                violations.append((i,
                    f"BOM download '{target}' should be '{canonical_bom}'"))
            elif not has_bom_source:
                violations.append((i,
                    f"links a BOM download but the page has no '{expected}' "
                    f"table and no resources/{slug}-bom.csv"))

    # Rule 4: protocol-PDF download buttons.
    expected_protocol = f"generated/{slug}-protocol.pdf"
    for i, line in enumerate(lines, start=1):
        for target in DOWNLOAD_RE.findall(line):
            target = target.strip()
            is_protocol_ref = "protocol" in target.lower() and (
                target.lower().endswith(".pdf") or "todo" in target.lower())
            if is_protocol_ref and target != expected_protocol:
                violations.append((i,
                    f"protocol download '{target}' should be '{expected_protocol}'"))

    # Rule 5: agreement when both sources exist.
    if has_matching_label and has_csv:
        inline_rows = extract_bom_table(text, slug)
        if inline_rows:
            try:
                csv_text = csv_path.read_text(encoding="utf-8")
            except (OSError, UnicodeDecodeError) as exc:
                violations.append((1, f"could not read {csv_path}: {exc}"))
            else:
                violations.extend(
                    check_agreement(inline_rows, csv_text, slug,
                                    _label_line(lines, slug), path))

    # Rule 6: a BOM source on a page the pipeline skips (no # Protocol).
    if has_bom_source and not _has_protocol(text):
        violations.append((1,
            f"page has a BOM source but no '# Protocol' heading — the pipeline "
            f"skips it, so no BOM is generated"))

    return violations


def check_directory(proc_dir, slug):
    """Directory-level checks: orphan bom-*.md pages and misnamed BOM CSVs.
    Returns a list of (path, line, message)."""
    out = []
    for child in sorted(proc_dir.glob("bom-*.md")):
        out.append((child, 1,
            f"orphan BOM page '{child.name}' — migrate it into an inline "
            f"bom-{slug} table on the process page or resources/{slug}-bom.csv "
            f"(standalone bom-*.md files are not picked up by the pipeline)"))
    res = proc_dir / "resources"
    if res.is_dir():
        for child in sorted(res.iterdir()):
            name = child.name
            if "bom" in name.lower() and name.lower().endswith(".csv") \
                    and name != f"{slug}-bom.csv":
                out.append((child, 1,
                    f"misnamed BOM CSV '{name}' — must be named '{slug}-bom.csv' "
                    f"to be picked up by the pipeline"))
    return out


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

    # Directory-level checks, once per process directory containing a page.
    seen_dirs = set()
    for page in pages:
        proc_dir = page.parent
        if proc_dir in seen_dirs:
            continue
        seen_dirs.add(proc_dir)
        for child, line, msg in check_directory(proc_dir, proc_dir.name):
            print(f"{child}:{line}  {msg}")
            total += 1

    if total:
        print(f"\n❌ {total} BOM convention violation(s) found.")
        return 1
    print(f"✅ {len(pages)} process page(s) OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
