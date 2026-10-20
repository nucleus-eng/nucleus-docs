#!/usr/bin/env python3
"""
bom_common.py — shared helpers for the lab-ready BOM pipeline (issue #10, #108).

One definition of "a BOM table", how to read it, how to turn it into CSV (and
back), and how to index every material across the distribution. Imported by:

  - ``build-protocols.py``        — generate per-process BOM PDFs / CSVs
  - ``check-bom-labels.py``       — enforce label/download/agreement conventions
  - ``enrich-bom.py``             — fill a page's BOM columns from other pages
  - ``build-materials-reference.py`` — aggregate one distribution-wide reference

Keeping the parse/normalize/index logic here means check, generator, enrichment,
and reference all share one definition of "equal" — so the agreement check can't
drift from what the generator actually emits.
"""

import csv
import io
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# A markdown table row.
TABLE_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
# A markdown table separator row (e.g. "| --- | --- |").
TABLE_SEP_RE = re.compile(r"^\s*\|[\s:|-]+\|\s*$")
# A directive option line carrying a label (e.g. ":label: bom-make-1pot").
LABEL_RE = re.compile(r"^\s*:label:\s*(\S+)\s*$")


# --------------------------------------------------------------------------- #
# Cell / table <-> CSV plumbing
# --------------------------------------------------------------------------- #

def _clean_cell(cell: str) -> str:
    """Strip markdown markup from a table cell for clean CSV output:
    bold (`**x**` -> `x`), links (`[text](url)` -> `url`) and code spans
    (```x``` -> `x`).

    The code span is not cosmetic. A part number whose pack-size suffix is
    lowercase -- ``PSB-440-5g`` -- trips ``nucleus.magnitude-unit-spacing``, so
    the page writes it as a code span to keep Vale quiet. ``norm_key`` only
    collapses whitespace and casefolds, so before 2026-10-12 the backticks
    survived into the dedup key and ``` `psb-440-5g` ``` did not match
    ``psb-440-5g``; they were also copied verbatim into the reference's Part #
    cell. Bold was handled here from the start and backticks were not.
    Found by the Gel Control Experiments session."""
    cell = re.sub(r"\[[^\]]*\]\(([^)]+)\)", r"\1", cell)  # link -> url
    cell = re.sub(r"\*\*(.+?)\*\*", r"\1", cell)          # **bold** -> bold
    cell = re.sub(r"`([^`]*)`", r"\1", cell)              # `code` -> code
    return cell.strip()


def split_row(row: str) -> List[str]:
    """Split a markdown table row into its raw (uncleaned) cell strings."""
    return [c.strip() for c in row.strip().strip("|").split("|")]


def table_to_csv(rows: List[str]) -> str:
    """Convert markdown table rows to CSV text, dropping the separator row and
    cleaning markdown markup out of every cell."""
    buf = io.StringIO()
    writer = csv.writer(buf)
    for row in rows:
        if TABLE_SEP_RE.match(row):
            continue
        writer.writerow([_clean_cell(c) for c in split_row(row)])
    return buf.getvalue()


def csv_to_table_rows(csv_text: str) -> List[str]:
    """Inverse of ``table_to_csv``: turn CSV text into markdown table rows.

    Cells are emitted verbatim (no ``_clean_cell``); a ``| --- | ... |``
    separator is injected after the header so ``build_bom_markdown`` renders the
    table. Empty/whitespace rows and any embedded markdown-separator rows are
    skipped. Returns ``[]`` for empty input.

    Guarantee: ``table_to_csv(csv_to_table_rows(x))`` re-canonicalizes ``x`` —
    i.e. round-trips an uploaded CSV through the same normalization the inline
    path uses.
    """
    data_rows: List[List[str]] = []
    for cells in csv.reader(io.StringIO(csv_text)):
        if not cells or all(c.strip() == "" for c in cells):
            continue
        # Drop a markdown-separator row that may have been pasted into the CSV.
        if all(c.strip() and set(c.strip()) <= set("-: ") for c in cells):
            continue
        data_rows.append([c.strip() for c in cells])
    if not data_rows:
        return []
    width = len(data_rows[0])
    out = ["| " + " | ".join(data_rows[0]) + " |",
           "| " + " | ".join(["---"] * width) + " |"]
    for cells in data_rows[1:]:
        out.append("| " + " | ".join(cells) + " |")
    return out


def extract_bom_table(body: str, slug: str) -> Optional[List[str]]:
    """Return the markdown table rows belonging to the table labeled
    ``bom-<slug>``, or None if absent."""
    lines = body.splitlines()
    label = f"bom-{slug}"
    label_idx = None
    for i, line in enumerate(lines):
        if line.strip() == f":label: {label}":
            label_idx = i
            break
    if label_idx is None:
        return None
    rows = []
    started = False
    for line in lines[label_idx + 1:]:
        if TABLE_ROW_RE.match(line):
            started = True
            rows.append(line.strip())
        elif started:
            break
    return rows or None


# --------------------------------------------------------------------------- #
# Normalization (one definition of "equal")
# --------------------------------------------------------------------------- #

def canon_csv(csv_text: str) -> List[List[str]]:
    """Normalize CSV text to a list of rows for equality comparison: parse,
    drop markdown-separator rows, strip cells, right-trim trailing empty cells,
    and drop fully-empty rows. Used by the agreement check so an inline table
    and an uploaded CSV compare equal iff they carry the same data."""
    out: List[List[str]] = []
    for cells in csv.reader(io.StringIO(csv_text)):
        cells = [c.strip() for c in cells]
        while cells and cells[-1] == "":
            cells.pop()
        if not cells:
            continue
        if all(c and set(c) <= set("-: ") for c in cells):
            continue
        out.append(cells)
    return out


def norm_key(value: str) -> str:
    """Normalize a manufacturer or part-number token for keying/matching:
    strip, collapse internal whitespace, casefold."""
    return re.sub(r"\s+", " ", (value or "").strip()).casefold()


def norm_name(value: str) -> str:
    """Normalize a chemical/product name for near-match detection: as
    ``norm_key`` but also drop a trailing parenthetical (e.g. concentration) and
    surrounding punctuation."""
    v = re.sub(r"\([^)]*\)", "", value or "")
    v = re.sub(r"\s+", " ", v.strip().strip(".,;:")).casefold()
    return v


# --------------------------------------------------------------------------- #
# Header-aware row parsing
# --------------------------------------------------------------------------- #

# THE ONE ALLOWED SPELLING OF EACH COLUMN TITLE. Jon ruled this on 2026-10-12:
# "it should ideally be one allowed title per column, with a bunch of optional
# columns and a set of required ones", then "required three is fine" on the set
# below, then "go with recommend" on keeping `description`, `used for` and
# `molecular weight` allowed on a page and OUT of the distribution-wide
# reference. ``check-materials-tables.py`` enforces this; the parser below does
# not, and the split is deliberate -- see RETIRED_ALIASES.
ALLOWED_TITLES = {
    # required
    "name": "Name",
    "manufacturer": "Manufacturer",
    "part": "Part #",
    # optional, aggregated into the reference
    "category": "Category",
    "product": "Product",
    "price": "Price",
    "storage": "Storage",
    "link": "Link",
    # optional, allowed on a page and deliberately NOT aggregated
    "description": "Description",
    "used for": "Used for",
    "molecular weight": "Molecular weight",
}

REQUIRED_FIELDS = ("name", "manufacturer", "part")

# Spellings the PARSER still accepts and the CHECKER reports. Deleting them here
# would drop a column on every page still using one, which lowers the reference
# row count -- the opposite of what this change is for. So the map stays
# permissive, the allowlist stays strict, and the aliases go when the checker's
# count reaches zero. Same shape as the report-only guards in
# compositional-biology-theory: a rule runs before it blocks.
#
# Measured on main 2026-10-12 over 131 table headers in 44 files, counting only
# a row followed by a `| --- |` separator: `reagent` 21, `description` 16,
# `material` 4, `storage conditions` 1, and `item`, `supplier`, `part number`,
# `used for`, `molecular weight` all 0.
#
# `reagent` at 21 is why the map stays permissive. Most of those are recipe
# tables with no Manufacturer or Part # column, which `parse_table_header`
# rejects anyway -- but the count is a migration either way, not a tidy-up.
# `part number` is 0 here and 1 on the demo tree, where `embed-photocrosslinking`
# uses it; it is kept so a branch carrying that page does not break on merge.
RETIRED_ALIASES = {
    "reagent": "name",
    "material": "name",
    "item": "name",
    "supplier": "manufacturer",
    "part number": "part",
    "storage conditions": "storage",
}

# Map a normalized header cell to a canonical field name.
#
# DELETED 2026-10-12: `vendor`, `product name`, `part#`, `cat #`, `catalog #`,
# `catalog number`. Six spellings, zero header uses on main and zero on the demo
# tree, so removing them costs no page edit. That is the whole of what
# "collapse most of them" can do for free; the rest is RETIRED_ALIASES above.
_HEADER_ALIASES = {
    **{title.lower(): field for field, title in ALLOWED_TITLES.items()},
    **RETIRED_ALIASES,
}

# Carried into the distribution-wide reference. `description`, `used for` and
# `molecular weight` are allowed on a page and absent here on purpose: Q2,
# ruled 2026-10-12. Adding one means growing a table every Node reads.
CANON_FIELDS = ["name", "category", "product", "manufacturer",
                "part", "price", "storage", "link"]

# Cell values that mean "not filled in" — treated as empty so a page's own TODO
# placeholders never pollute the index (and so the reference omits them).
PLACEHOLDERS = {"", "todo", "tbd", "n/a", "na", "—", "-", "–", "#"}


def is_placeholder(value: str) -> bool:
    return (value or "").strip().lower() in PLACEHOLDERS


def _header_field(cell: str) -> Optional[str]:
    key = re.sub(r"\s+", " ", _clean_cell(cell).strip().lower())
    return _HEADER_ALIASES.get(key)


def parse_table_header(header_row: str) -> Optional[Dict[str, int]]:
    """Map canonical field name -> column index for a table header row, or None
    if the row is not a recognizable materials header (needs a manufacturer and
    a part-number column to be a BOM-like table)."""
    fields: Dict[str, int] = {}
    for idx, cell in enumerate(split_row(header_row)):
        field = _header_field(cell)
        if field and field not in fields:
            fields[field] = idx
    if "manufacturer" in fields and "part" in fields:
        return fields
    return None


def clean_link(raw_cell: str) -> str:
    """Extract a bare URL from a link cell, robust to the markup variants in the
    docs: ``[link](url)``, the legacy double-bracket ``[[link](url)]``, a bare
    bracketed ``[url]``, or a plain URL. Returns "" for a placeholder."""
    raw = (raw_cell or "").strip()
    m = re.search(r"\]\(([^)]+)\)", raw)  # markdown link target
    url = m.group(1).strip() if m else raw.strip("[] ").strip()
    if is_placeholder(url):
        return ""
    return url


def row_to_material(cells: List[str], cols: Dict[str, int]) -> Optional[dict]:
    """Turn a data row into a material dict keyed by canonical field, using the
    column map from ``parse_table_header``. Returns None if it has no part #."""
    def get(field: str) -> str:
        idx = cols.get(field)
        if idx is None or idx >= len(cells):
            return ""
        return _clean_cell(cells[idx])

    def get_raw(field: str) -> str:
        idx = cols.get(field)
        if idx is None or idx >= len(cells):
            return ""
        return cells[idx]

    part = get("part")
    if is_placeholder(part):
        return None
    # Nullify placeholder cells so a page's TODOs don't shadow real values
    # from other pages during indexing/enrichment.
    mat = {f: ("" if is_placeholder(get(f)) else get(f)) for f in CANON_FIELDS}
    mat["link"] = clean_link(get_raw("link"))
    return mat


# --------------------------------------------------------------------------- #
# Distribution-wide material index
# --------------------------------------------------------------------------- #

def iter_tables(text: str):
    """Yield (header_row, [data_rows]) for each markdown table in `text`.
    A table is a run of consecutive table rows; the first is the header, the
    second (a separator) is skipped, the rest are data rows."""
    lines = text.splitlines()
    i = 0
    n = len(lines)
    while i < n:
        if TABLE_ROW_RE.match(lines[i]) and not TABLE_SEP_RE.match(lines[i]):
            block = []
            while i < n and TABLE_ROW_RE.match(lines[i]):
                block.append(lines[i].strip())
                i += 1
            if len(block) >= 2 and TABLE_SEP_RE.match(block[1]):
                yield block[0], block[2:]
        else:
            i += 1


def index_materials(docs_root: Path,
                    exclude: Optional[Path] = None
                    ) -> Tuple[Dict[Tuple[str, str], dict], List[dict]]:
    """Scan every ``.md`` file under ``docs_root`` for materials tables (any
    table with Manufacturer + Part # columns, whether ``bom-<slug>`` or a legacy
    ``tbl:critical-materials``-style table) and build an index keyed by
    ``(norm manufacturer, norm part#)``.

    Returns ``(index, conflicts)`` where each index value is::

        {name, category, product, manufacturer, part, price, storage, link,
         used_in: [slug, ...]}

    and ``conflicts`` records cases where the same key carried a different
    non-empty value for a field across pages (for QA reporting). The first
    non-empty value wins in the index; later differing values are logged.
    """
    index: Dict[Tuple[str, str], dict] = {}
    conflicts: List[dict] = []
    exclude_resolved = exclude.resolve() if exclude else None

    for path in sorted(docs_root.rglob("*.md")):
        # Skip gitignored derived intermediates (generated/<slug>-bom.md etc.) —
        # they would re-index the same materials under a bogus "generated" slug.
        if "generated" in path.parts:
            continue
        if exclude_resolved and path.resolve() == exclude_resolved:
            continue
        slug = path.parent.name
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            continue
        for header, data_rows in iter_tables(text):
            cols = parse_table_header(header)
            if not cols:
                continue
            for row in data_rows:
                cells = split_row(row)
                mat = row_to_material(cells, cols)
                if not mat:
                    continue
                key = (norm_key(mat["manufacturer"]), norm_key(mat["part"]))
                if key not in index:
                    entry = dict(mat)
                    entry["used_in"] = [slug]
                    index[key] = entry
                    continue
                entry = index[key]
                if slug not in entry["used_in"]:
                    entry["used_in"].append(slug)
                for field in CANON_FIELDS:
                    new = mat[field]
                    old = entry[field]
                    if not new:
                        continue
                    if not old:
                        entry[field] = new
                    elif norm_key(old) != norm_key(new):
                        conflicts.append({
                            "key": key, "field": field,
                            "kept": old, "other": new,
                            "slug": slug, "file": str(path),
                        })
    return index, conflicts
