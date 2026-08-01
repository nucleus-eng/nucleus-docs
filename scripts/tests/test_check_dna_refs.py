"""Tests for scripts/check-dna-refs.py (issue #120).

The motivating bug for this check is already in `main`: reporter-degfp/spec.md
claims `pOpen-deGFP` is 2789 bp; the DNA repo's actual file is 2812 bp after a
correction commit. check-links.py cannot see this — the URL resolves fine.
These tests lock the checks that catch that class of error: a wrong bp claim,
a legacy-repo link, a filename-extension mismatch, and the "greedy link" name
mismatch (a claim naming an extra element the target file doesn't confirm).
"""

import importlib.util
from pathlib import Path

import pytest


def _load_module():
    """Import check-dna-refs.py by path (hyphenated filename)."""
    path = Path(__file__).resolve().parent.parent / "check-dna-refs.py"
    spec = importlib.util.spec_from_file_location("check_dna_refs", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cdr = _load_module()


GENBANK_HEADER = "LOCUS       {name}        {length} bp    DNA     circular SYN 31-JUL-2024\n"


def _write_gb(path: Path, name: str, length: int):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(GENBANK_HEADER.format(name=name, length=length) + "ORIGIN\n//\n")


# --------------------------------------------------------------------------- #
# DNA repo indexing
# --------------------------------------------------------------------------- #


def test_index_dna_repo_parses_locus_name_and_length(tmp_path):
    _write_gb(tmp_path / "reporters" / "pOpen-deGFP.gbk", "pOpen-T7-deGFP", 2812)
    index = cdr.index_dna_repo(tmp_path)
    entry = index["reporters/pOpen-deGFP.gbk"]
    assert entry.locus_name == "pOpen-T7-deGFP"
    assert entry.length_bp == 2812


def test_index_dna_repo_dna_extension_has_no_locus(tmp_path):
    path = tmp_path / "energy" / "pOpen-PPK-CHis.dna"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(b"\x00\x01SnapGene binary garbage")
    index = cdr.index_dna_repo(tmp_path)
    entry = index["energy/pOpen-PPK-CHis.dna"]
    assert entry.locus_name is None
    assert entry.length_bp is None


def test_index_dna_repo_ignores_non_sequence_files(tmp_path):
    (tmp_path / "README.md").write_text("hello")
    index = cdr.index_dna_repo(tmp_path)
    assert index == {}


# --------------------------------------------------------------------------- #
# Table parsing
# --------------------------------------------------------------------------- #


def test_find_tables_splits_header_and_rows():
    text = (
        "| **Name** | **Length (bp)** | **File** |\n"
        "| --- | --- | --- |\n"
        "| `pT7-lacI` | 2877 | [pOpen-lacI.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-lacI.gb) |\n"
    )
    tables = list(cdr.find_tables(text))
    assert len(tables) == 1
    header, rows = tables[0]
    assert header == ["**Name**", "**Length (bp)**", "**File**"]
    assert len(rows) == 1
    line_no, cells = rows[0]
    assert line_no == 3
    assert cells[0] == "`pT7-lacI`"


def test_find_tables_tolerates_missing_separator_row():
    # Malformed table with no --- separator: without the guard, row 1 would be
    # mistaken for the separator and silently dropped.
    text = (
        "| Name | File |\n"
        "| `pT7-lacI` | [pOpen-lacI.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-lacI.gb) |\n"
    )
    header, rows = next(cdr.find_tables(text))
    assert len(rows) == 1


def test_bp_column_detected_by_header_text():
    assert cdr._bp_column_index(["**Name**", "**Length (bp)**", "**File**"]) == 1
    assert cdr._bp_column_index(["Construct", "Size", "Description", "**File**"]) is None


# --------------------------------------------------------------------------- #
# Claim extraction
# --------------------------------------------------------------------------- #


def test_extract_claims_bp_from_dedicated_column():
    header = ["**Name**", "**Length (bp)**", "**File**"]
    rows = [(3, ["`pT7-lacI`", "2877", "[pOpen-lacI.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/pOpen-lacI.gb)"])]
    claims = cdr.extract_claims(header, rows, "spec.md")
    assert len(claims) == 1
    c = claims[0]
    assert c.name == "pT7-lacI"
    assert c.bp == 2877
    assert c.path == "detectors/pOpen-lacI.gb"
    assert c.repo == "nucleus-eng/DNA"
    assert c.kind == "blob"


def test_extract_claims_bp_self_describing_suffix_when_no_bp_header():
    header = ["Construct", "Size", "Description", "**File**"]
    rows = [
        (
            10,
            [
                "`pOpen-pT7-Cx43`",
                "3320 bp",
                "Expresses wild-type Cx43",
                "[pOpen-Cx43.gb](https://github.com/nucleus-eng/DNA/blob/main/pores/pOpen-Cx43.gb)",
            ],
        )
    ]
    claims = cdr.extract_claims(header, rows, "spec.md")
    assert claims[0].bp == 3320


def test_extract_claims_no_bp_claim_when_row_has_none():
    # A concentration row (plamGFP DNA, 120 ng/µL) — no "bp" header, no
    # self-describing "NNN bp" cell. Must not be misread as a bp claim.
    header = ["**Reagent**", "**Stock**", "**Unit**"]
    rows = [
        (
            5,
            [
                "[plamGFP DNA](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-plamGFP-PURE.gb)",
                "120",
                "ng/µL",
            ],
        )
    ]
    claims = cdr.extract_claims(header, rows, "spec.md")
    assert claims[0].bp is None
    assert claims[0].name is None


def test_extract_claims_flags_legacy_repo_and_tree_links():
    header = ["Name", "File"]
    rows = [
        (1, ["`X`", "[X.gb](https://github.com/bnext-bio/nucleus/blob/main/TODO)"]),
        (2, ["Y", "[DNA/PURE/expression](https://github.com/nucleus-eng/DNA/tree/main/PURE/expression)"]),
    ]
    claims = cdr.extract_claims(header, rows, "spec.md")
    assert claims[0].repo == "bnext-bio/nucleus"
    assert claims[1].kind == "tree"
    assert claims[1].path == "PURE/expression"


# --------------------------------------------------------------------------- #
# Validation — the actual checks
# --------------------------------------------------------------------------- #


def _claim(**kwargs):
    defaults = dict(
        file="spec.md",
        line=1,
        repo="nucleus-eng/DNA",
        kind="blob",
        path="reporters/pOpen-deGFP.gbk",
        link_text="pOpen-deGFP.gb",
        bp=2789,
        name="pOpen-deGFP",
    )
    defaults.update(kwargs)
    return cdr.Claim(**defaults)


def test_validate_claim_missing_file_is_blocking(tmp_path):
    index = {}
    findings = cdr.validate_claim(_claim(), index, tmp_path)
    assert any(f.level == cdr.BLOCKING and "not found" in f.message for f in findings)


def test_validate_claim_bp_mismatch_is_blocking_this_is_the_degfp_bug(tmp_path):
    index = {"reporters/pOpen-deGFP.gbk": cdr.ConstructFile("reporters/pOpen-deGFP.gbk", "pOpen-T7-deGFP", 2812)}
    findings = cdr.validate_claim(_claim(bp=2789), index, tmp_path)
    blocking = [f for f in findings if f.level == cdr.BLOCKING]
    assert len(blocking) == 1
    assert "2789" in blocking[0].message and "2812" in blocking[0].message


def test_validate_claim_bp_match_is_not_blocking(tmp_path):
    index = {"reporters/pOpen-deGFP.gbk": cdr.ConstructFile("reporters/pOpen-deGFP.gbk", "pOpen-T7-deGFP", 2812)}
    findings = cdr.validate_claim(_claim(bp=2812), index, tmp_path)
    assert not any(f.level == cdr.BLOCKING for f in findings)


def test_validate_claim_legacy_repo_is_blocking(tmp_path):
    findings = cdr.validate_claim(_claim(repo="bnext-bio/nucleus"), {}, tmp_path)
    assert len(findings) == 1
    assert findings[0].level == cdr.BLOCKING
    assert "legacy" in findings[0].message


def test_validate_claim_extension_mismatch_is_warn_not_blocking(tmp_path):
    index = {"reporters/pOpen-deGFP.gbk": cdr.ConstructFile("reporters/pOpen-deGFP.gbk", "pOpen-T7-deGFP", 2789)}
    findings = cdr.validate_claim(_claim(bp=2789, link_text="pOpen-deGFP.gb"), index, tmp_path)
    assert any(f.level == cdr.WARN and ".gb" in f.message and ".gbk" in f.message for f in findings)
    assert not any(f.level == cdr.BLOCKING for f in findings)


def test_validate_claim_tree_link_checks_directory_existence(tmp_path):
    (tmp_path / "PURE" / "expression").mkdir(parents=True)
    ok = cdr.validate_claim(_claim(kind="tree", path="PURE/expression"), {}, tmp_path)
    assert ok == []

    missing = cdr.validate_claim(_claim(kind="tree", path="PURE/missing"), {}, tmp_path)
    assert len(missing) == 1 and missing[0].level == cdr.BLOCKING


def test_validate_claim_dna_extension_is_unverifiable_info(tmp_path):
    index = {"energy/pOpen-PPK-CHis.dna": cdr.ConstructFile("energy/pOpen-PPK-CHis.dna", None, None)}
    findings = cdr.validate_claim(
        _claim(path="energy/pOpen-PPK-CHis.dna", link_text="pOpen-PPK-CHis.gb", bp=2915, name="pOpen-PPK"),
        index,
        tmp_path,
    )
    assert any(f.level == cdr.INFO and "cannot verify length" in f.message for f in findings)
    assert not any(f.level == cdr.BLOCKING for f in findings)


def test_validate_claim_no_bp_cell_is_info_not_blocking(tmp_path):
    index = {"reporters/pOpen-deGFP.gbk": cdr.ConstructFile("reporters/pOpen-deGFP.gbk", "pOpen-T7-deGFP", 2812)}
    findings = cdr.validate_claim(_claim(bp=None), index, tmp_path)
    assert any(f.level == cdr.INFO and "no length" in f.message for f in findings)
    assert not any(f.level == cdr.BLOCKING for f in findings)


# --------------------------------------------------------------------------- #
# Name-relatedness — the greedy-link smell detector (check 5)
# --------------------------------------------------------------------------- #


@pytest.mark.parametrize(
    "claim_name,locus_name,filename",
    [
        ("pT7-lacI", "lacI", "pOpen-lacI.gb"),  # promoter prefix only — same gene
        ("pT7-tetR", "tetR", "pOpen-tetR.gb"),
        ("pOpen-pT7-Cx43", "pOpen-Cx43", "pOpen-Cx43.gb"),  # exact bp match in practice
        ("pOpen-deGFP", "pOpen-T7-deGFP", "pOpen-deGFP.gbk"),
    ],
)
def test_names_related_when_only_prefix_decoration_differs(claim_name, locus_name, filename):
    assert cdr._names_related(claim_name, locus_name, filename)


@pytest.mark.parametrize(
    "claim_name,locus_name,filename",
    [
        # claim names an extra downstream element (a reporter) the target's
        # LOCUS name doesn't confirm — this is the shape of a greedy link.
        ("pT7-lacO-plamGFP", "pT7-lacO", "pOpen-pT7-lacO.gb"),
        ("pT7-tetO-plamGFP", "pT7-tetO", "pOpen-pT7-tetO.gb"),
        # claim is missing a tag present in the target — same asymmetry, other direction.
        ("pOpen-PPK", "pOpen-PPK-CHis", "pOpen-PPK-CHis.dna"),
    ],
)
def test_names_not_related_when_suffix_content_differs(claim_name, locus_name, filename):
    assert not cdr._names_related(claim_name, locus_name, filename)


def test_validate_claim_suffix_name_mismatch_is_warn_not_blocking(tmp_path):
    index = {"detectors/pOpen-pT7-lacO.gb": cdr.ConstructFile("detectors/pOpen-pT7-lacO.gb", "pT7-lacO", 2958)}
    findings = cdr.validate_claim(
        _claim(path="detectors/pOpen-pT7-lacO.gb", link_text="pOpen-pT7-lacO.gb", bp=2958, name="pT7-lacO-plamGFP"),
        index,
        tmp_path,
    )
    assert any(f.level == cdr.WARN and "pT7-lacO-plamGFP" in f.message for f in findings)
    assert not any(f.level == cdr.BLOCKING for f in findings)


# --------------------------------------------------------------------------- #
# End-to-end
# --------------------------------------------------------------------------- #


def test_check_end_to_end_reproduces_the_degfp_bug(tmp_path):
    dna_repo = tmp_path / "DNA"
    _write_gb(dna_repo / "reporters" / "pOpen-deGFP.gbk", "pOpen-T7-deGFP", 2812)

    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "spec.md").write_text(
        "| **Name** | **Length (bp)** | **File** |\n"
        "| --- | --- | --- |\n"
        "| `pOpen-deGFP` | 2789 | [pOpen-deGFP.gb](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk) |\n"
    )

    findings = cdr.check([str(docs)], dna_repo)
    blocking = [f for f in findings if f.level == cdr.BLOCKING]
    assert len(blocking) == 1
    assert "2789" in blocking[0].message and "2812" in blocking[0].message


def test_check_clean_corpus_has_no_blocking_findings(tmp_path):
    dna_repo = tmp_path / "DNA"
    _write_gb(dna_repo / "reporters" / "pOpen-deGFP.gbk", "pOpen-T7-deGFP", 2812)

    docs = tmp_path / "docs"
    docs.mkdir()
    (docs / "spec.md").write_text(
        "| **Name** | **Length (bp)** | **File** |\n"
        "| --- | --- | --- |\n"
        "| `pOpen-deGFP` | 2812 | [pOpen-deGFP.gbk](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk) |\n"
    )

    findings = cdr.check([str(docs)], dna_repo)
    assert not any(f.level == cdr.BLOCKING for f in findings)


def test_check_flags_legacy_repo_link_like_the_module_template(tmp_path):
    dna_repo = tmp_path / "DNA"
    dna_repo.mkdir()

    templates = tmp_path / "templates"
    templates.mkdir()
    (templates / "spec.md").write_text(
        "| **Name** | **Length (bp)** | **File** |\n"
        "| --- | --- | --- |\n"
        "| `TODO: pConstruct-Name` | TODO | [TODO: filename.gb](https://github.com/bnext-bio/nucleus/blob/main/TODO) |\n"
    )

    findings = cdr.check([str(templates)], dna_repo)
    assert any(f.level == cdr.BLOCKING and "legacy" in f.message for f in findings)


def test_find_dna_repo_uses_env_override(tmp_path, monkeypatch):
    monkeypatch.setenv("NUCLEUS_DNA_REPO", str(tmp_path))
    assert cdr.find_dna_repo() == tmp_path


def test_find_dna_repo_returns_none_when_missing(tmp_path, monkeypatch):
    monkeypatch.setenv("NUCLEUS_DNA_REPO", str(tmp_path / "does-not-exist"))
    assert cdr.find_dna_repo() is None
