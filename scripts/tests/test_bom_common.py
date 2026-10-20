"""Tests for scripts/bom_common.py — the shared BOM-pipeline module (issue #114).

Every BOM-pipeline bug found so far was caught by *running* the tools, not by
review (PR #111's TODO-string shadowing, the page-matching-itself enrichment
bug). These are execution- and data-dependent failures that read-through review
structurally misses, so this suite locks the load-bearing invariants of the one
module all four consumers import.
"""

import importlib.util
from pathlib import Path

import bom_common as bc
from bom_common import (
    PLACEHOLDERS,
    canon_csv,
    clean_link,
    csv_to_table_rows,
    index_materials,
    is_placeholder,
    parse_table_header,
    row_to_material,
    split_row,
    table_to_csv,
    _clean_cell,
)


def _load_enrich_bom():
    """Import enrich-bom.py by path (its filename has a hyphen, so it is not a
    normal importable module name)."""
    path = Path(__file__).resolve().parent.parent / "enrich-bom.py"
    spec = importlib.util.spec_from_file_location("enrich_bom", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# --------------------------------------------------------------------------- #
# Round-trip stability (table <-> CSV)
# --------------------------------------------------------------------------- #

def test_csv_roundtrip_is_stable():
    """table_to_csv(csv_to_table_rows(x)) re-canonicalizes x, and a second pass
    is a fixed point — the guarantee the agreement check relies on."""
    csv_in = (
        "Name,Manufacturer,Part #,Link\r\n"
        "Tris base,Sigma,T1503,https://example.com/p\r\n"
    )
    once = table_to_csv(csv_to_table_rows(csv_in))
    twice = table_to_csv(csv_to_table_rows(once))
    assert once == twice


def test_roundtrip_preserves_url_encoded_comma():
    """A %2C in a URL (the documented Vale/CSV hazard) must survive the
    table->CSV path and not be split into two cells or decoded."""
    url = "https://www.sigmaaldrich.com/US/en/product/sigma/t1503%2Cfoo"
    rows = csv_to_table_rows(f"Name,Link\nTris,{url}\n")
    out = table_to_csv(rows)
    assert "%2C" in out
    # %2C stayed inside a single cell -> the data row still has exactly 2 fields.
    data_line = [ln for ln in out.splitlines() if ln.startswith("Tris")][0]
    assert data_line.count(",") == 1


def test_clean_cell_reduces_markdown_link_and_bold():
    assert _clean_cell("[Sigma](https://x.com/p)") == "https://x.com/p"
    assert _clean_cell("**T1503**") == "T1503"
    assert _clean_cell("[Sigma](https://x.com/p%2C1)") == "https://x.com/p%2C1"


# --------------------------------------------------------------------------- #
# Agreement equality (inline table vs uploaded CSV)
# --------------------------------------------------------------------------- #

def test_inline_link_and_bare_url_csv_agree():
    """An inline `[text](url)` cell and a bare-URL uploaded CSV normalize equal
    — the basis of check-bom-labels' inline-vs-CSV agreement check."""
    inline_rows = [
        "| Name | Manufacturer | Part # | Link |",
        "| --- | --- | --- | --- |",
        "| Tris base | Sigma | T1503 | [Sigma](https://x.com/t1503) |",
    ]
    inline_norm = canon_csv(table_to_csv(inline_rows))

    uploaded_csv = (
        "Name,Manufacturer,Part #,Link\n"
        "Tris base,Sigma,T1503,https://x.com/t1503\n"
    )
    uploaded_norm = canon_csv(uploaded_csv)

    assert inline_norm == uploaded_norm


def test_canon_csv_trims_trailing_empties_and_drops_separator():
    csv_text = (
        "Name,Part #,,\n"
        "---,---,---,---\n"
        "Tris,T1503,,\n"
        "\n"
    )
    assert canon_csv(csv_text) == [["Name", "Part #"], ["Tris", "T1503"]]


# --------------------------------------------------------------------------- #
# Placeholder handling — one definition, no drift (locks #114 step 2a)
# --------------------------------------------------------------------------- #

def test_is_placeholder_covers_full_set_case_and_space_insensitive():
    for token in PLACEHOLDERS:
        assert is_placeholder(token)
        assert is_placeholder(f"  {token}  ")
        assert is_placeholder(token.upper())
    for real in ("T1503", "Sigma-Aldrich", "deGFP", "0", "10 mM"):
        assert not is_placeholder(real)


def test_clean_link_treats_every_placeholder_as_empty():
    """clean_link used to carry its own placeholder tuple missing `na`/en-dash;
    it must now agree with bom_common.PLACEHOLDERS for every member."""
    for token in PLACEHOLDERS:
        assert clean_link(token) == "", f"clean_link({token!r}) should be empty"
    assert clean_link("https://x.com/p") == "https://x.com/p"


def test_enrich_fillable_agrees_with_placeholder_set():
    """enrich-bom._is_fillable used to carry its own set missing `na`/`#`/en-dash;
    it must now treat every bom_common placeholder (bare and as a link target)
    as fillable."""
    enrich = _load_enrich_bom()
    for token in PLACEHOLDERS:
        assert enrich._is_fillable(token), f"{token!r} should be fillable"
        assert enrich._is_fillable(f"[link]({token})"), f"link({token!r}) fillable"
    assert not enrich._is_fillable("T1503")
    assert not enrich._is_fillable("[Sigma](https://x.com/p)")


# --------------------------------------------------------------------------- #
# Header-aware row parsing
# --------------------------------------------------------------------------- #

def test_clean_cell_strips_a_code_span():
    """A part number whose pack-size suffix is lowercase -- `PSB-440-5g` --
    trips `nucleus.magnitude-unit-spacing`, so a page writes it as a code span
    to keep Vale quiet. `norm_key` only collapses whitespace and casefolds, so
    before 2026-10-12 the backticks survived into the dedup key and the same
    part number keyed two ways. Bold was stripped here from the start and
    backticks were not. Found by the Gel Control Experiments session.
    """
    assert _clean_cell("`PSB-440-5g`") == "PSB-440-5g"
    assert bc.norm_key(_clean_cell("`PSB-440-5g`")) == bc.norm_key("PSB-440-5g")
    assert bc.norm_key(_clean_cell("**PSB-440-5g**")) == bc.norm_key("PSB-440-5g")
    # A code span inside prose loses its markup and keeps its words.
    assert _clean_cell("`a` and `b`") == "a and b"


def test_parse_table_header_maps_retired_aliases():
    """The parser stays permissive where the allowlist is strict.

    Jon ruled one allowed title per column on 2026-10-12. Deleting a spelling a
    page still uses would drop that column from the reference -- the opposite of
    what the ruling is for -- so a retired spelling keeps parsing and
    check-materials-tables.py reports it. Measured on main the same day over 131
    table headers in 44 files: `reagent` 21, `material` 4, `storage conditions`
    1. The aliases go when that count reaches zero.
    """
    cols = parse_table_header("| Reagent | Supplier | Part number | Storage Conditions |")
    assert cols is not None
    assert cols["name"] == 0          # Reagent -> name
    assert cols["manufacturer"] == 1  # Supplier -> manufacturer
    assert cols["part"] == 2          # Part number -> part
    assert cols["storage"] == 3       # Storage Conditions -> storage

    cols = parse_table_header("| Material | Manufacturer | Part # |")
    assert cols is not None and cols["name"] == 0   # Material -> name

    cols = parse_table_header("| Item | Manufacturer | Part # |")
    assert cols is not None and cols["name"] == 0   # Item -> name


def test_deleted_aliases_are_gone():
    """DELETED 2026-10-12: `vendor`, `product name`, `part#`, `cat #`,
    `catalog #`, `catalog number`.

    Swept every ref in the repo -- 39 of them, origin branches plus the local
    pH demo -- counting only a pipe row followed by a `| --- |` separator.
    Zero header uses of all six. Removing a spelling nothing writes costs no
    page edit, and that is the whole of what "collapse most of them" can do for
    free. If one of these ever comes back, it should come back as a page edit
    rather than as an alias.
    """
    for spelling in ("Vendor", "Product Name", "Part#", "Cat #",
                     "Catalog #", "Catalog Number"):
        assert bc._header_field(spelling) is None, spelling

    # The deleted part-number spellings mean this header no longer parses --
    # which is the point: check-materials-tables.py reports it as job 1.
    assert parse_table_header("| Reagent | Vendor | Cat # |") is None


def test_parse_table_header_requires_manufacturer_and_part():
    # No part-number column -> not a BOM-like table.
    assert parse_table_header("| Name | Manufacturer | Price |") is None
    # No manufacturer column -> not a BOM-like table.
    assert parse_table_header("| Name | Part # | Price |") is None


# --------------------------------------------------------------------------- #
# row_to_material — placeholder nullification & part-# gating
# --------------------------------------------------------------------------- #

def test_row_to_material_drops_rows_with_placeholder_part():
    cols = parse_table_header("| Name | Manufacturer | Part # |")
    assert row_to_material(split_row("| Tris | Sigma | TODO |"), cols) is None
    assert row_to_material(split_row("| Tris | Sigma | — |"), cols) is None


def test_row_to_material_nullifies_placeholder_cells():
    cols = parse_table_header("| Name | Category | Manufacturer | Part # |")
    mat = row_to_material(split_row("| Tris | TODO | Sigma | T1503 |"), cols)
    assert mat is not None
    assert mat["part"] == "T1503"
    assert mat["category"] == ""  # TODO nullified, not carried into the index


# --------------------------------------------------------------------------- #
# Self-exclusion during indexing (the page-matches-itself bug)
# --------------------------------------------------------------------------- #

_BOM_PAGE = (
    "| Name | Manufacturer | Part # | Link |\n"
    "| --- | --- | --- | --- |\n"
    "| Tris base | Sigma | T1503 | https://x.com/t1503 |\n"
)


def _write_page(root: Path, slug: str, body: str) -> Path:
    d = root / slug
    d.mkdir(parents=True)
    page = d / "main.md"
    page.write_text(body, encoding="utf-8")
    return page


def test_index_materials_excludes_the_target_page(tmp_path):
    page_a = _write_page(tmp_path, "pagea", _BOM_PAGE)
    _write_page(tmp_path, "pageb", _BOM_PAGE)

    index, _ = index_materials(tmp_path, exclude=page_a)
    key = (bc.norm_key("Sigma"), bc.norm_key("T1503"))
    assert key in index
    # The excluded page is never indexed against itself.
    assert "pagea" not in index[key]["used_in"]
    assert index[key]["used_in"] == ["pageb"]


def test_index_materials_without_exclude_sees_both_pages(tmp_path):
    _write_page(tmp_path, "pagea", _BOM_PAGE)
    _write_page(tmp_path, "pageb", _BOM_PAGE)

    index, _ = index_materials(tmp_path)
    key = (bc.norm_key("Sigma"), bc.norm_key("T1503"))
    assert sorted(index[key]["used_in"]) == ["pagea", "pageb"]
