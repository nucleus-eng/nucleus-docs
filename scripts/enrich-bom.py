#!/usr/bin/env python3
"""
enrich-bom.py — fill a process page's BOM columns from other pages' BOM tables.

An authoring aid (NOT run in CI). For a target page's ``bom-<slug>`` table, it
fills only the EMPTY cells of each row from a distribution-wide index keyed by
``(manufacturer, part #)`` — never overwriting a non-empty cell. Exact part-#
matches are applied; rows whose chemical/product name matches an existing
material under a DIFFERENT part # are reported as "near matches" for manual
review (e.g. a different grade or pack size) and never auto-applied.

The intended workflow: author a row with the canonical Manufacturer + Part # (so
it matches an existing material), leave Product/Price/Storage/Link blank or
``TODO``, then run this to pull those columns from the page that already lists
the part. Cross-check the near-match report to decide whether to harmonize a
part # onto a canonical one first.

Dry-run by default; pass ``--write`` to apply.

Usage:
    python3 scripts/enrich-bom.py docs/processes/make-1pot/main.md
    python3 scripts/enrich-bom.py docs/processes/make-1pot/main.md --write
"""

import re
import sys
from pathlib import Path

from bom_common import (  # noqa: E402  (sibling module, resolved via sys.path[0])
    CANON_FIELDS,
    extract_bom_table,
    index_materials,
    norm_key,
    norm_name,
    parse_table_header,
    split_row,
)

DOCS_ROOT = Path("docs")
FILLABLE_PLACEHOLDERS = {"", "todo", "tbd", "n/a", "—", "-"}


def _is_fillable(cell: str) -> bool:
    c = cell.strip().lower()
    if c in FILLABLE_PLACEHOLDERS:
        return True
    # A placeholder link like [link](TODO) or [link](#) is also fillable.
    m = re.fullmatch(r"\[[^\]]*\]\(([^)]*)\)", cell.strip())
    if m and m.group(1).strip().lower() in (FILLABLE_PLACEHOLDERS | {"#"}):
        return True
    return False


def _rebuild_row(cells):
    return "| " + " | ".join(cells) + " |"


def enrich(page: Path, write: bool) -> int:
    slug = page.parent.name
    text = page.read_text(encoding="utf-8")
    rows = extract_bom_table(text, slug)
    if not rows:
        print(f"No 'bom-{slug}' table found in {page}.")
        return 1
    if len(rows) < 2:
        print(f"'bom-{slug}' table in {page} has no data rows.")
        return 1

    header, sep, data_rows = rows[0], rows[1], rows[2:]
    cols = parse_table_header(header)
    if not cols:
        print(f"'bom-{slug}' table header is not a recognizable materials "
              f"header (needs Manufacturer + Part # columns).")
        return 1

    # Exclude the target page so its own (mostly empty) row never matches itself
    # and its attributions point at the donor pages.
    index, _conflicts = index_materials(DOCS_ROOT, exclude=page)

    # Build a name -> [keys] map for near-match reporting.
    by_name = {}
    for key, entry in index.items():
        for nm in {norm_name(entry["name"]), norm_name(entry["product"])}:
            if nm:
                by_name.setdefault(nm, set()).add(key)

    man_idx = cols["manufacturer"]
    part_idx = cols["part"]

    fills = []        # (row_label, field, value, source_slug)
    near = []         # (row_label, our_part, suggestion)
    new_data_rows = list(data_rows)

    for ri, row in enumerate(data_rows):
        cells = split_row(row)
        # pad to header width
        while len(cells) < len(split_row(header)):
            cells.append("")
        label = cells[cols.get("name", 0)] if cols.get("name") is not None else cells[0]
        manufacturer = cells[man_idx] if man_idx < len(cells) else ""
        part = cells[part_idx] if part_idx < len(cells) else ""

        key = (norm_key(manufacturer), norm_key(part))
        entry = index.get(key)

        changed = False
        if entry:
            for field, ci in cols.items():
                if field in ("manufacturer", "part"):
                    continue  # these are the match keys; never touch
                if field not in CANON_FIELDS:
                    continue
                if ci < len(cells) and _is_fillable(cells[ci]) and entry.get(field):
                    value = entry[field]
                    if field == "link" and value:
                        value = f"[link]({value})"
                    cells[ci] = value
                    src = entry["used_in"][0] if entry["used_in"] else "?"
                    fills.append((label, field, value, src))
                    changed = True

        # Near-match report: same chemical/product name, different part #.
        nm = norm_name(label)
        prod_nm = norm_name(cells[cols["product"]]) if cols.get("product") is not None \
            and cols["product"] < len(cells) else ""
        candidate_keys = set()
        for n in (nm, prod_nm):
            if n:
                candidate_keys |= by_name.get(n, set())
        for ck in sorted(candidate_keys):
            if ck == key:
                continue
            cand = index[ck]
            if norm_key(cand["part"]) != norm_key(part):
                near.append((label, part or "(none)",
                             f"{cand['name']} — {cand['manufacturer']} "
                             f"{cand['part']} (${cand['price'] or '?'}; "
                             f"used in {', '.join(cand['used_in'])})"))

        if changed:
            new_data_rows[ri] = _rebuild_row(cells)

    # Report.
    print(f"\n=== enrich-bom: {page} (bom-{slug}) ===")
    if fills:
        print(f"\nProposed fills ({len(fills)}):")
        for label, field, value, src in fills:
            short = value if len(value) <= 60 else value[:57] + "..."
            print(f"  • {label:<22} {field:<11} = {short}   (from {src})")
    else:
        print("\nNo empty cells could be filled by exact part-# match.")

    if near:
        print(f"\nNear matches for manual review ({len(near)}) — "
              f"same name, different part #:")
        seen = set()
        for label, our_part, suggestion in near:
            line = (label, suggestion)
            if line in seen:
                continue
            seen.add(line)
            print(f"  ? {label:<22} (ours: {our_part}) -> {suggestion}")

    if not write:
        print("\n(dry-run — re-run with --write to apply the fills above)")
        return 0

    if not fills:
        print("\nNothing to write.")
        return 0

    new_table = "\n".join([header, sep] + new_data_rows)
    old_table = "\n".join(rows)
    new_text = text.replace(old_table, new_table, 1)
    if new_text == text:
        print("\n⚠️  Could not splice the rebuilt table back into the page "
              "(table text not found verbatim); no changes written.")
        return 1
    page.write_text(new_text, encoding="utf-8")
    print(f"\n✓ Wrote {len(fills)} fill(s) to {page}.")
    return 0


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    write = "--write" in sys.argv[1:]
    if not args:
        print(__doc__)
        return 1
    rc = 0
    for a in args:
        rc |= enrich(Path(a), write)
    return rc


if __name__ == "__main__":
    sys.exit(main())
