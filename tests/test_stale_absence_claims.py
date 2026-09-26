"""Pin the stale-absence check in scripts/check-dna-refs.py.

The check exists because a page can assert a construct is *not* in
nucleus-eng/DNA, and that claim goes stale silently the moment the file lands.
Six such claims sat wrong for twelve days; no other check could see them,
because every other one validates rows that DO cite a file.

The behavior worth pinning is not "it finds matches" but "it reports a finding
and never a fix". A filename match is not an identity claim.
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
    return {
        "effectors/detector-3oc6-hsl/LuxR-PLA1-linear.gb": mod.ConstructFile(
            "effectors/detector-3oc6-hsl/LuxR-PLA1-linear.gb", "LuxR-PLA1-linear", 2237
        ),
        "detectors/pOpen-tetR.gb": mod.ConstructFile("detectors/pOpen-tetR.gb", "pT7-tetR", 2877),
    }


def _run(mod, index, text):
    return mod.find_stale_absence_claims(Path("page.md"), text, index)


@pytest.mark.parametrize(
    "text",
    [
        "@Editor: `LuxR-PLA1-linear` has no sequence file in nucleus-eng/DNA.",
        "| `LuxR-PLA1-linear` | not documented | not yet in `nucleus-eng/DNA` |",
        "@Editor: `LuxR-PLA1-linear` has no recorded length.",
    ],
)
def test_flags_a_claim_the_repo_contradicts(mod, index, text):
    findings = _run(mod, index, text)
    assert len(findings) == 1
    assert findings[0].level == mod.WARN


def test_matches_through_a_backbone_prefix(mod, index):
    """`pT7-tetR` on the page, pOpen-tetR.gb in the repo — the same construct."""
    findings = _run(mod, index, "@Editor: `pT7-tetR` is not yet in nucleus-eng/DNA.")
    assert len(findings) == 1


def test_says_verify_never_closeable(mod, index):
    """The whole point. A name match is not identity: the linear/circular pairs
    in this corpus share a cassette and differ by kilobases."""
    msg = _run(mod, index, "@Editor: `LuxR-PLA1-linear` has no sequence file.")[0].message
    assert "verify it is the same construct" in msg
    assert "closeable" not in msg.lower()


def test_silent_when_the_construct_really_is_absent(mod, index):
    assert _run(mod, index, "@Editor: `T7pro-PLA1-T7term` has no sequence file.") == []


def test_silent_without_an_absence_phrase(mod, index):
    """A row citing the file is another check's job, not this one's."""
    assert _run(mod, index, "| `LuxR-PLA1-linear` | 2237 | [file](...) |") == []


def test_ignores_paths_and_prose_in_backticks(mod, index):
    text = "@Editor: no sequence file yet. See `docs/modules/x/spec.md` and `tmp/`."
    assert _run(mod, index, text) == []
