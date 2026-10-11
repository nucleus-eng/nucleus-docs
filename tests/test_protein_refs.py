"""Pin scripts/check-protein-refs.py: what it reads, and what it refuses to pass.

The check exists because a UniProt link can resolve and still name the wrong
protein. deGFP against wild-type GFP is 98.7% identical over 225 residues
against the entry's 238 — close enough that a name match, a link check and an
eyeball all pass it. So the cases pinned here are the ones where something
*almost* matches.

These build their inputs in memory and never touch the network or the corpus.
The one thing they cannot cover is a construct that IS fully identical to a
cited entry, because no construct in nucleus-eng/DNA encodes one; the identity
path is exercised against a sequence aligned with itself instead.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-protein-refs.py"


def _load():
    spec = importlib.util.spec_from_file_location("check_protein_refs", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cpr = _load()

ENTRY = {"name": "Beta-galactosidase", "alt": [], "organism": "Escherichia coli (strain K12)",
         "length": 1024, "mass": 116483, "seq": "MTMITDSLAVVLQRRDWENPGVTQLNRLAAHPPFASWRNSEE",
         "genes": ["lacZ"]}


def claim(context, link_text="UniProt P00722", accession="P00722"):
    return cpr.Claim(Path("x.md"), 1, accession, link_text, context)


def levels(findings):
    return [lv for lv, _ in findings]


# --- the context unit

def test_a_paragraph_is_the_context_not_a_fixed_window():
    lines = ["Beta-galactosidase, 1024 aa,", "cited here.", "", "An unrelated 999 aa claim."]
    assert "1024" in cpr.paragraph(lines, 2)
    assert "999" not in cpr.paragraph(lines, 2)


def test_the_citation_line_itself_is_included():
    lines = ["intro", "", "the claim is 1024 aa here", ""]
    assert "1024" in cpr.paragraph(lines, 3)


def test_two_citations_in_one_paragraph_share_it():
    lines = ["P00722 and P04483 both appear, 1024 aa stated once."]
    assert cpr.paragraph(lines, 1) == lines[0]


# --- the accession pattern

def test_the_accession_pattern_captures_nothing():
    """It is embedded in CITATION; a group here shifts CITATION's group numbers."""
    import re
    assert re.compile(cpr.ACCESSION).groups == 0


@pytest.mark.parametrize("text,acc", [
    ("[UniProt P00722](https://www.uniprot.org/uniprotkb/P00722/entry)", "P00722"),
    ("[x](https://uniprot.org/uniprotkb/Q89VI2)", "Q89VI2"),
    ("[y](https://www.uniprot.org/uniprotkb/A0A1S4NYF2/entry)", "A0A1S4NYF2"),
])
def test_it_finds_the_accession_in_a_citation(text, acc):
    m = cpr.CITATION.search(text)
    assert m and m.group(2) == acc


# --- what blocks

def test_a_wrong_residue_count_blocks():
    out = cpr.check(claim("Beta-galactosidase is 999 aa."), ENTRY)
    assert cpr.BLOCKING in levels(out)


def test_the_right_residue_count_does_not():
    out = cpr.check(claim("Beta-galactosidase is 1024 aa."), ENTRY)
    assert cpr.BLOCKING not in levels(out)


def test_a_wrong_mass_blocks():
    out = cpr.check(claim("Beta-galactosidase weighs 55.0 kDa."), ENTRY)
    assert cpr.BLOCKING in levels(out)


def test_a_stated_n_mer_mass_is_allowed():
    """A page may legitimately give the active form's mass. LacZ's tetramer is
    465.9 kDa and the entry holds the monomer, so refusing it would block a
    correct page."""
    out = cpr.check(claim("Beta-galactosidase tetramer, 465.9 kDa."), ENTRY)
    assert cpr.BLOCKING not in levels(out)


def test_a_link_text_naming_a_different_accession_blocks():
    out = cpr.check(claim("Beta-galactosidase.", link_text="UniProt P04483"), ENTRY)
    assert cpr.BLOCKING in levels(out)


def test_an_unresolvable_accession_blocks():
    out = cpr.check(claim("anything"), {"_missing": True})
    assert levels(out) == [cpr.BLOCKING]


# --- what warns rather than blocks

def test_a_different_organism_warns():
    out = cpr.check(claim("Beta-galactosidase from *Homo sapiens*."), ENTRY)
    assert cpr.WARN in levels(out) and cpr.BLOCKING not in levels(out)


def test_a_gene_name_counts_as_naming_the_protein():
    """Pages say LacZ and TetR, not 'Beta-galactosidase' or 'Tetracycline
    repressor protein class B'. Warning on every one of those would make the
    check unreadable."""
    out = cpr.check(claim("LacZ is the enzyme here."), ENTRY)
    assert all("right protein" not in m for _, m in out)


def test_nothing_recognisable_near_the_citation_warns():
    out = cpr.check(claim("The thing we use."), ENTRY)
    assert any("right protein" in m for _, m in out)


# --- the alignment guard, which is the deGFP case

def test_an_identical_sequence_is_full_identity():
    s = ENTRY["seq"]
    assert cpr.align_identity(s, s) == pytest.approx(100.0)


def test_a_clean_truncation_aligns_at_full_identity_which_is_the_trap():
    """deGFP's shape, minus the substitutions. A local alignment of a clean
    subsequence is 100%, so identity alone would pass a variant that only lost
    residues. main() pairs it with a length comparison for exactly this."""
    parent = ENTRY["seq"]
    variant = parent[6:]
    assert cpr.align_identity(variant, parent) == pytest.approx(100.0)
    assert len(variant) != len(parent)


def test_a_substituted_variant_falls_below_identity():
    parent = ENTRY["seq"]
    variant = parent[:10] + "WWWWW" + parent[15:]
    assert cpr.align_identity(variant, parent) < 100.0
