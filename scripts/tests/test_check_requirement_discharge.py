"""Tests for scripts/check-requirement-discharge.py.

The motivating cases are on `docs/devcells-integration-pages`, not `main`: ten
Requirements name an example satisfier the page already contains, while two —
`atc-sensing-cell` and `theophylline-sensing-cell` — write the met case as
"supplied here by the Chicago Chassis". Those two are the positive control, and
a test locks them so a future matcher change cannot start flagging the correct
form.

The distinction the check turns on is `e.g.` against `see`. `e.g. [X]` names
something that satisfies the requirement; `see [X]` names the Module that
imposes it. The LacZ/CPRG separation lines link the reporter as the *source* of
the constraint, so reporting them would be wrong.
"""

import importlib.util
from pathlib import Path

import pytest


def _load_module():
    """Import check-requirement-discharge.py by path (hyphenated filename)."""
    path = Path(__file__).resolve().parent.parent / "check-requirement-discharge.py"
    spec = importlib.util.spec_from_file_location("check_requirement_discharge", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


crd = _load_module()


def _spec(constituents=(), requirements="", extra=""):
    out = ["---", 'title: "Test"', "---", "", "# Overview", "", "Test page.", ""]
    if requirements:
        out += ["# Requirements", "", requirements, ""]
    if constituents:
        out += ["# Constituent Modules", ""]
        out += [f"- [{c}](../{c}/spec.md) — a part" for c in constituents]
        out += [""]
    if extra:
        out += [extra, ""]
    return "\n".join(out)


@pytest.fixture
def corpus(tmp_path, monkeypatch):
    """Build a docs/modules tree and point the check at it."""

    def build(pages):
        root = tmp_path / "docs" / "modules"
        for name, text in pages.items():
            (root / name).mkdir(parents=True, exist_ok=True)
            (root / name / "spec.md").write_text(text, encoding="utf-8")
        monkeypatch.chdir(tmp_path)
        monkeypatch.setattr(crd, "MODULES_ROOT", Path("docs/modules"))
        return root

    return build


# --------------------------------------------------------------------------- #
# satisfiers(): e.g. means satisfied-by, see means cross-reference
# --------------------------------------------------------------------------- #


def test_eg_link_is_a_satisfier():
    atom = "Requires pT7 transcription (e.g. [Base Cytosol](../base-cytosol/spec.md))."
    assert crd.satisfiers(atom) == ["base-cytosol"]


def test_see_link_is_not_a_satisfier():
    """The reporter imposes the LacZ/CPRG constraint; it does not meet it."""
    atom = (
        "Must not be exposed to theophylline. See "
        "[LacZ Reporter](../reporter-lacz/spec.md) for the constraint."
    )
    assert crd.satisfiers(atom) == []


def test_see_after_eg_in_one_paragraph_is_not_swept_in():
    atom = (
        "Requires a membrane (e.g. [POPC](../membrane-popc/spec.md)); "
        "see [PLA1](../effector-pla1/spec.md) for why."
    )
    assert crd.satisfiers(atom) == ["membrane-popc"]


def test_two_satisfiers_in_one_clause():
    atom = (
        "Requires transcription (e.g. [Base Cytosol](../base-cytosol/spec.md), "
        "[S30 Lysate](../s30-lysate/spec.md))."
    )
    assert sorted(crd.satisfiers(atom)) == ["base-cytosol", "s30-lysate"]


# --------------------------------------------------------------------------- #
# atoms(): admonitions are not Requirements
# --------------------------------------------------------------------------- #


def test_admonition_content_is_excluded():
    req = (
        "Requires a membrane (e.g. [POPC](../membrane-popc/spec.md)).\n\n"
        ":::{attention} A caveat\n"
        "Requires something else (e.g. [Other](../other/spec.md)).\n"
        ":::\n"
    )
    found = [s for a in crd.atoms(req) for s in crd.satisfiers(a)]
    assert found == ["membrane-popc"]


# --------------------------------------------------------------------------- #
# End to end
# --------------------------------------------------------------------------- #


def test_flags_a_satisfier_inside_the_composite(corpus, capsys):
    corpus(
        {
            "chassis": _spec(),
            "cell": _spec(
                constituents=["chassis"],
                requirements="Requires a compartment (e.g. [Chassis](../chassis/spec.md)).",
            ),
        }
    )
    assert crd.main([]) == 1
    assert "cell: requires something its own chassis supplies" in capsys.readouterr().out


def test_supplied_here_by_is_not_flagged(corpus, capsys):
    """The positive control — the form atc-sensing-cell already uses."""
    corpus(
        {
            "chassis": _spec(),
            "cell": _spec(
                constituents=["chassis"],
                requirements=(
                    "Requires a compartment (e.g. [Chassis](../chassis/spec.md)), "
                    "supplied here by the [Chassis](../chassis/spec.md)."
                ),
            ),
        }
    )
    assert crd.main([]) == 0
    assert "1 already marked as supplied" in capsys.readouterr().out


def test_satisfier_outside_the_composite_is_not_flagged(corpus):
    """A genuinely open Requirement is the normal case and must stay quiet."""
    corpus(
        {
            "cytosol": _spec(),
            "chassis": _spec(),
            "cell": _spec(
                constituents=["chassis"],
                requirements="Requires transcription (e.g. [Cytosol](../cytosol/spec.md)).",
            ),
        }
    )
    assert crd.main([]) == 0


def test_transitive_constituent_counts(corpus):
    """cell -> chassis -> cytosol: the cytosol is inside the cell."""
    corpus(
        {
            "cytosol": _spec(),
            "chassis": _spec(constituents=["cytosol"]),
            "cell": _spec(
                constituents=["chassis"],
                requirements="Requires transcription (e.g. [Cytosol](../cytosol/spec.md)).",
            ),
        }
    )
    assert crd.main([]) == 1


def test_waiver_suppresses_the_finding(corpus):
    corpus(
        {
            "chassis": _spec(),
            "cell": _spec(
                constituents=["chassis"],
                requirements="Requires a compartment (e.g. [Chassis](../chassis/spec.md)).",
                extra="<!-- requirement-discharge: chassis (composer may substitute) -->",
            ),
        }
    )
    assert crd.main([]) == 0


def test_leaf_module_is_not_checked(corpus):
    """A Module with no constituents discharges nothing, so it is out of scope."""
    corpus(
        {
            "leaf": _spec(
                requirements="Requires a membrane (e.g. [POPC](../membrane-popc/spec.md)).",
            ),
        }
    )
    assert crd.main([]) == 2  # nothing composed to check — see below


def test_no_composed_pages_is_an_error_not_a_pass(corpus, capsys):
    """A scan that reports zero must be shown capable of reporting non-zero.

    `main` today has no composed Module pages, so a green tick there would be a
    clean number that measured nothing.
    """
    corpus({"leaf": _spec(requirements="Requires something.")})
    assert crd.main([]) == 2
    assert "proved nothing" in capsys.readouterr().err
