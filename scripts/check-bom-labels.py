#!/usr/bin/env python3
"""
check-bom-labels.py — enforce the lab-ready pipeline's BOM conventions on
process pages and module spec pages (issues #10, #108).

The lab-ready pipeline (scripts/build-protocols.py) generates a protocol PDF, a
Bill of Materials PDF, and a materials CSV from each process page
(``docs/processes/**/main.md`` or ``*-main.md``), and a BOM PDF + materials CSV
(no protocol PDF) from each module spec page (``docs/modules/**/spec.md``) that
carries a BOM source. A page's BOM may be supplied as EITHER an inline table
labeled ``bom-<slug>`` OR an uploaded ``resources/<slug>-bom.csv`` (``<slug>``
= the page's containing directory name). Download buttons point at
``generated/<slug>-*.pdf``. This fast, no-toolchain check enforces:

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
  6. **Orphans / misnaming:** a standalone ``bom-*.md`` file in a process or
     module dir (the pre-pipeline anti-pattern), or a ``resources/*bom*.csv``
     not named ``<slug>-bom.csv``, is flagged. On a *process* page (not a
     module spec), a BOM source with no ``# Protocol`` heading is flagged too
     — the pipeline requires a Protocol section to generate anything for that
     page kind, so a BOM there would silently never be built.

Reports violations as ``file:line`` and exits non-zero if any are found.

Usage:
    python3 scripts/check-bom-labels.py [paths...]
    python3 scripts/check-bom-labels.py            # all of docs/processes/ + docs/modules/
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
MODULES_ROOT = Path("docs/modules")

BOM_LABEL_RE = re.compile(r"^\s*:label:\s*(bom-[A-Za-z0-9._-]+)\s*$")
# Loose: any generated BOM-PDF download target, however (mis)named. Lets us
# recognize a misnamed BOM button as a BOM button and flag it (rule 3).
BOM_DOWNLOADISH_RE = re.compile(r"generated/[^>]*bom[^>]*\.pdf", re.IGNORECASE)
# Any `download <target>` reference, to inspect the target.
DOWNLOAD_RE = re.compile(r"download\s*<([^>]+)>")
# A standalone orphan BOM page filename (pre-pipeline anti-pattern).
ORPHAN_BOM_MD_RE = re.compile(r"^bom-.*\.md$", re.IGNORECASE)


def find_pages(args):
    """Return (process_pages, module_pages). Process pages are matched by
    filename pattern under any target; module pages are ``spec.md`` files
    specifically under ``MODULES_ROOT`` (or an explicit target inside it)."""
    targets = [Path(a) for a in args] if args else [PROCESSES_ROOT, MODULES_ROOT]
    modules_root_resolved = MODULES_ROOT.resolve()

    process_pages = []
    module_pages = []
    for target in targets:
        under_modules = (
            target.resolve() == modules_root_resolved
            or modules_root_resolved in target.resolve().parents
        )
        if target.is_file() and target.suffix == ".md":
            (module_pages if under_modules else process_pages).append(target)
            continue
        if under_modules:
            module_pages.extend(target.glob("**/spec.md"))
        else:
            for pattern in ("**/main.md", "**/*-main.md"):
                process_pages.extend(target.glob(pattern))
    return sorted(set(process_pages)), sorted(set(module_pages))


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


def page_has_bom_source(path):
    """Whether `path` (a process or module page) has adopted the pipeline's BOM
    convention — a matching inline ``bom-<slug>`` label or a
    ``resources/<slug>-bom.csv``. Used both by ``check_page`` and by ``main`` to
    decide whether a directory's orphan-file checks apply (see ``main``)."""
    slug = path.parent.name
    expected = f"bom-{slug}"
    text = path.read_text(encoding="utf-8")
    has_matching_label = any(
        BOM_LABEL_RE.match(line) and BOM_LABEL_RE.match(line).group(1) == expected
        for line in text.splitlines()
    )
    has_csv = (path.parent / "resources" / f"{slug}-bom.csv").is_file()
    return has_matching_label or has_csv


def check_page(path, requires_protocol=True):
    """Return a list of (line, message) violations for one page. Rule 6's
    "no # Protocol" check only applies to process pages — module specs are
    valid BOM-only sources for the pipeline and never have a Protocol section."""
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

    # Rule 6: a BOM source on a process page the pipeline skips (no # Protocol).
    # Module spec pages are BOM-only by design and never have a Protocol section.
    if requires_protocol and has_bom_source and not _has_protocol(text):
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

    process_pages, module_pages = find_pages(args)
    total = 0

    for page in process_pages:
        for line, msg in check_page(page, requires_protocol=True):
            print(f"{page}:{line}  {msg}")
            total += 1
    for page in module_pages:
        for line, msg in check_page(page, requires_protocol=False):
            print(f"{page}:{line}  {msg}")
            total += 1

    # Directory-level checks (orphan bom-*.md, misnamed CSVs), once per
    # directory containing a page. Every process directory is checked
    # unconditionally (all process pages are expected to use the pipeline).
    # Module directories are only checked if their spec.md has already opted
    # into the pipeline (a bom-<slug> table or resources/<slug>-bom.csv) —
    # otherwise this would flag pre-pipeline legacy modules (e.g.
    # reporter-degfp's bom-cells.md/bom-cytosol.md, rendered through an
    # unrelated ad hoc typst template) that are out of scope to migrate here.
    seen_dirs = set()
    for page in process_pages:
        proc_dir = page.parent
        if proc_dir in seen_dirs:
            continue
        seen_dirs.add(proc_dir)
        for child, line, msg in check_directory(proc_dir, proc_dir.name):
            print(f"{child}:{line}  {msg}")
            total += 1
    for page in module_pages:
        mod_dir = page.parent
        if mod_dir in seen_dirs or not page_has_bom_source(page):
            continue
        seen_dirs.add(mod_dir)
        for child, line, msg in check_directory(mod_dir, mod_dir.name):
            print(f"{child}:{line}  {msg}")
            total += 1

    if total:
        print(f"\n❌ {total} BOM convention violation(s) found.")
        return 1
    print(f"✅ {len(process_pages) + len(module_pages)} page(s) OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
