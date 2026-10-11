"""Pin the presence pass and the severity split in scripts/check-conflicts.py.

A presence condition is a component sitting in a compartment, not something a
morphism inflicts. That makes it a different computation from a Conflict, and the
thing worth pinning is not that it finds the detergent case but WHERE IT STOPS:
a membrane touches what it contains and what contains it, and not a sibling's
lumen. A pass that reported every operand of every packing step against every
other would also find the detergent case, and it would be wrong.

The negative test is the one that earns the file. `Sol{M1{A} + M2{B}}`: M1
touches Sol and A, not B. Co-encapsulating two populations is exactly that shape,
and it is a thing this corpus does.

These run the real script over the real corpus, as the meet tests do, so a corpus
change can fail them. That is the point: the detergent meeting the membrane is a
claim about the sources, not about the checker alone.
"""

import importlib.util
import io
import contextlib
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-conflicts.py"


@pytest.fixture(scope="module")
def cc():
    spec = importlib.util.spec_from_file_location("check_conflicts", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    with contextlib.redirect_stdout(io.StringIO()):
        try:
            spec.loader.exec_module(mod)
        except SystemExit:
            pass
    return mod


# ---------------------------------------------------------------- the compartments

def test_mixing_puts_every_operand_in_one_compartment(cc):
    step = {"operator": "mixing", "operands": ["a", "b", "c"]}
    assert cc._compartments(step) == [{"a", "b", "c"}]


def test_a_membrane_touches_both_sides_of_itself(cc):
    """The lumen and the medium are separated from each other and not from it."""
    step = {"operator": "packing",
            "operands": ["atc-sensor-cytosol", "membrane-popc-chol-9-1",
                         "outer-solution"]}
    assert cc._compartments(step) == [
        {"membrane-popc-chol-9-1", "atc-sensor-cytosol", "outer-solution"}]


def test_two_membranes_in_one_step_do_not_share_a_lumen(cc):
    """Jon's case: `Sol{M1{A} + M2{B}}`. M1 touches Sol and A, but not B.

    Each boundary gets its own compartment. B reaches M2 and never M1, which is
    why co-encapsulating two populations does not put one's cargo against the
    other's bilayer.
    """
    step = {"operator": "packing",
            "operands": ["membrane-popc", "membrane-popc-chol", "outer-solution"]}
    got = cc._compartments(step)
    assert len(got) == 2
    for compartment in got:
        assert len(compartment & {"membrane-popc", "membrane-popc-chol"}) == 1


def test_a_packing_step_with_no_boundary_yields_nothing(cc):
    """Rather than falling back to one compartment, which would invent co-location."""
    assert cc._compartments({"operator": "packing", "operands": ["a", "b"]}) == []


# ---------------------------------------------------------------- membership

def test_a_member_satisfies_the_class_its_page_names(cc):
    assert cc._satisfies("detergent-tween-80", "detergent")
    assert cc._satisfies("detergent", "detergent")


def test_an_unrelated_module_does_not(cc):
    assert not cc._satisfies("base-cytosol", "detergent")


# ---------------------------------------------------------------- the corpus

def test_the_tween_in_a_tetr_stock_meets_the_membrane_it_is_encapsulated_with(cc):
    """The case the pass was written for, and the only presence meet today.

    Both steps are the same shape: a cytosol holding the tetR-aTc Detector is
    packed inside a bilayer, and the Detector's stock carries Tween 80.
    """
    met = {(mod, step) for mod, step, _, _, present, _ in cc.presence_rows
           if present == "detergent-tween-80"}
    assert met == {("atc-cascade", "encapsulate"),
                   ("atc-sensing-cell", "encapsulate")}


def test_the_two_presence_conditions_that_meet_nothing_are_reported_as_unmet(cc):
    """Silence would read as a pass. Neither is a typo.

    `dmso` is an operand only of a Gramicidin stock no composition names, and the
    theophylline path has no cascade page, so no step puts the analyte beside the
    reporter it degrades. Both would report the moment one is built.
    """
    declared = {s["to"] for m in cc.SRC for s in (cc.SENS.get(m) or {}).values()
                if s.get("kind") == "presence"}
    met = {r[5]["to"] for r in cc.presence_rows}
    assert declared - met == {"dmso", "theophylline"}


def test_reading_a_chromophore_is_moderate_and_not_a_conflict(cc):
    """Severity splits the report and not the computation.

    Every meet below is real: illumination does bleach a chromophore. Counting
    them as Conflicts would put a routine plate read at the level of a
    crosslinking dose and bury anything that destroys a Function.
    """
    assert cc.measured_rows, "no readout imposes on what it reads"
    for _, _, imp, _, sens in cc.measured_rows:
        assert imp["id"] == "illumination"
        assert sens["severity"] == "moderate"
    assert cc.tally["CONFLICT"] == 0
