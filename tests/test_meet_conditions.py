"""Pin the condition boxes render-meet.py draws: P1 impositions, P2 requirements.

`D3` ruled that both are nodes with a heavy border rather than edges, because an
edge-relation must compose and joint consistency does not. `Q1` ruled that the
spec wins over the hand figure, so the generator draws what a source declares and
names what it cannot on stderr.

THE INHERITANCE IS THE PART WORTH PINNING. `IQ4n` (a) declares separation once,
on color-change, so no cascade can forget it and a fourth enzyme gets it free.
IQ4n's own wording offered the `refines:` chain as the route and that route does
not exist: every cascade's reporter operand is reporter-lacz-enzyme, which refines
`lacz`, and `lacz` refines nothing. The route that works is the `substrates:` walk
the same proposal also named. If someone rewires the reporter classes, these tests
are what says whether the box still arrives.

These run the real script over the real corpus, as the dropped-leg tests do. A
corpus change can therefore make them fail, which is the point: the box arriving
is a claim about the sources, not about the renderer alone.
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent
SCRIPT = REPO / "scripts" / "render-meet.py"
SEPARATION = "REQ_ENZYME_AND_SUBSTRATE_IN_DIFFERENT_COMPARTMENTS"


def _run(*cascades):
    return subprocess.run([sys.executable, str(SCRIPT), *cascades],
                          capture_output=True, text=True, cwd=REPO)


def _box(stdout, nid):
    return next((l for l in stdout.split("\n") if l.strip().startswith(nid)), None)


def test_an_imposition_with_a_bound_draws_the_bound():
    """`thermal-hold` is one of two declarations carrying a `bound:`, so it is the
    case that shows a reader what the step actually inflicts."""
    r = _run("atc-cascade", "ph-cascade")
    line = _box(r.stdout, "IMP_THERMAL_HOLD")
    assert line and "temperature ≥ lga-powder.gel_point_max_c" in line


def test_an_imposition_with_no_bound_draws_its_id():
    """Six of the eight declarations carry no bound. They still get a box: the
    step inflicts something, and saying only its name beats saying nothing."""
    r = _run("atc-cascade", "ph-cascade")
    line = _box(r.stdout, "IMP_UV_EXPOSURE")
    assert line and "uv-exposure" in line


def test_a_requirement_with_notation_draws_it_verbatim():
    """IQ3 (b). The symbols come from the source, not from a mapping in here."""
    r = _run("atc-cascade", "ph-cascade")
    line = _box(r.stdout, SEPARATION)
    assert line and "C₁{Enzyme}" in line and "C₂{Substrate}" in line


def test_a_requirement_with_no_notation_falls_back_to_its_id():
    r = _run("atc-cascade", "ph-cascade")
    line = _box(r.stdout, "REQ_ENZYME_ENCAPSULATED_SUBSTRATE_OUTSIDE")
    assert line and "enzyme-encapsulated-substrate-outside" in line


def test_the_pipe_is_escaped_for_mermaid():
    """`|` is edge-label syntax. Unescaped, the separation box breaks the diagram."""
    r = _run("atc-cascade", "ph-cascade")
    line = _box(r.stdout, SEPARATION)
    assert line and "#124;" in line and "|" not in line


def test_the_class_requirement_reaches_every_leg_that_pairs():
    """No cascade declares it. All three get it, and the box says where from."""
    r = _run("atc-cascade", "ph-cascade", "luxr-lacz-cascade")
    line = _box(r.stdout, SEPARATION)
    assert line and "inherited from Color Change" in line
    # inherited, so it is not reported as held by only some of the legs
    assert "of 3 legs declare this" not in line


def test_one_box_per_condition_not_one_per_leg():
    """Two legs declaring `thermal-hold` make one claim. Two boxes would say
    they make two, and the meet would assert a difference that is not there."""
    r = _run("atc-cascade", "ph-cascade", "luxr-lacz-cascade")
    assert sum(1 for l in r.stdout.split("\n")
               if l.strip().startswith("IMP_THERMAL_HOLD[")) == 1


def test_a_box_only_some_legs_declare_says_so():
    r = _run("atc-cascade", "ph-cascade", "luxr-lacz-cascade")
    line = _box(r.stdout, "REQ_ENZYME_ENCAPSULATED_SUBSTRATE_OUTSIDE")
    assert line and "only 1 of 3 legs declare this" in line


def test_the_undeclared_hand_figure_box_is_a_note_and_not_a_warning():
    """It is true on every run, so sharing the word with the dropped-leg warning
    would teach a reader to skip both. tests/test_dropped_leg_warning.py pins the
    other half: a clean run prints no WARNING at all."""
    r = _run("atc-cascade", "ph-cascade")
    assert "NOTE:" in r.stderr and "osmotic-matching" in r.stderr
    assert "WARNING" not in r.stderr


def test_the_condition_boxes_are_not_counted_as_slots():
    """Nothing is met over a condition. Counting them would inflate the
    denominator the concrete/abstract/unmet split is read against.

    THE TOTAL MOVED 17 TO 16 ON 2026-10-04 AND THE DROP IS THE POINT, NOT NOISE.
    Both legs used to name `effector-pla1` and met on it as a concrete slot.
    Each now names its own gated construct -- `pT7-tetO-PLA1` for aTc,
    `pT7-toehold9-PLA1` for pH -- which are different molecules, so the legs no
    longer agree there and concrete fell 5 to 4. A meet that still reported
    agreement would be asserting the two legs share a construct they do not.
    What this test pins is that conditions stay out of the denominator; the
    denominator itself is free to move when the sources do."""
    r = _run("atc-cascade", "ph-cascade")
    assert "16 slot(s)" in r.stderr
    assert "2 requirement box(es) and 3 imposition box(es)" in r.stderr


def test_a_box_hangs_off_the_process_it_constrains():
    """D3 makes it a node, and a node outside the graph is a node nobody reads."""
    r = _run("atc-cascade", "ph-cascade")
    assert "IMP_THERMAL_HOLD --> PROC_EMBED_HYDROGEL_0" in r.stdout
