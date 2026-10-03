"""Pin the alias guard in scripts/check-dna-refs.py.

A construct name that drops a qualifier is safe only when no sibling carries the
same stem. CLAUDE.md states the hazard with a worked pair: `LuxR-PLA1-linear.gb`
(2237 bp) and `pOpen-LuxR-PLA1.gb` (4175 bp) share a cassette, differ by a whole
backbone, and are not interchangeable. A docs name of `LuxR-PLA1` names either.

So the behavior worth pinning is not "it clears aliases" but the two conditions
under which it refuses to: a second file could be meant, or the one file that
could be meant is not the file the row links.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-dna-refs.py"


@pytest.fixture(scope="module")
def mod():
    spec = importlib.util.spec_from_file_location("check_dna_refs", SCRIPT)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


@pytest.fixture
def index(mod):
    def cf(rel, locus, bp=1000, names=()):
        return mod.ConstructFile(rel, locus, bp, names)
    return {
        # the ambiguous pair CLAUDE.md names
        "effectors/LuxR-PLA1-linear.gb": cf("effectors/LuxR-PLA1-linear.gb", "LuxR-PLA1-linear"),
        "effectors/pOpen-LuxR-PLA1.gb": cf("effectors/pOpen-LuxR-PLA1.gb", "pOpen-LuxR-PLA1"),
        # a construct with no sibling
        "detectors/pT7-toehold9-PLA1-linear.gb": cf(
            "detectors/pT7-toehold9-PLA1-linear.gb", "pT7-toehold9-PLA1-linear"),
        # a name whose only match is a DIFFERENT file from the one a row links
        "control/pOpen-deGFP-ssrA.gb": cf("control/pOpen-deGFP-ssrA.gb", "pOpen-deGFP-ssrA"),
        "control/pOpen-deGFP-CHis-ssrA.gb": cf(
            "control/pOpen-deGFP-CHis-ssrA.gb", "pOpen-pT7-deGFP-CHis-ss"),
    }


def test_ambiguous_name_is_not_unique(mod, index):
    """The pair CLAUDE.md names must never clear. Two files could be meant."""
    assert not mod._unique_in_repo("LuxR-PLA1", index, "effectors/LuxR-PLA1-linear.gb")


def test_unique_name_clears(mod, index):
    """No sibling carries the stem, so there is no second construct to confuse."""
    assert mod._unique_in_repo(
        "pT7-toehold9-PLA1", index, "detectors/pT7-toehold9-PLA1-linear.gb")


def test_unique_but_not_the_linked_file_does_not_clear(mod, index):
    """`pT7-deGFP-ssrA` matches exactly one file and it is not the one the row
    links. Clearing on uniqueness alone would silence a name that points at a
    different construct from its own link."""
    assert not mod._unique_in_repo(
        "pT7-deGFP-ssrA", index, "control/pOpen-deGFP-CHis-ssrA.gb")


def test_order_is_load_bearing(mod):
    """A promoter, an operator and a coding sequence appear in that order, so a
    reordered name is a different claim and must not match."""
    assert mod._subsequence(["pt7", "laco"], ["pt7", "laco", "utr1", "plamgfp"])
    assert not mod._subsequence(["laco", "pt7"], ["pt7", "laco", "utr1", "plamgfp"])


def test_a_feature_label_confirms_an_element(mod):
    """The file names its parts in /label=, which is where a full construct name
    usually lives. `pOpen-pT7-lacO.gb` has LOCUS `pT7-lacO` and a feature labelled
    `pT7-lacO-UTR1-plamGFP-t7hyb6`, so the file does confirm the plamGFP the docs
    name claims."""
    assert mod._names_related(
        "pT7-lacO-plamGFP", "pT7-lacO", "pOpen-pT7-lacO.gb",
        ("pT7-lacO-UTR1-plamGFP-t7hyb6",), False)


def test_a_claim_cannot_invent_an_element(mod):
    """Every token of the claim must appear. A name claiming a reporter no field
    of the file mentions stays a warning."""
    assert not mod._names_related(
        "pT7-lacO-mCherry", "pT7-lacO", "pOpen-pT7-lacO.gb",
        ("pT7-lacO-UTR1-plamGFP-t7hyb6",), False)
