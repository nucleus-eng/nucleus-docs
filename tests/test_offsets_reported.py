"""Pin that check-conflicts REPORTS undeclared osmotic offsets and never fails on one.

An osmotic offset is per design: a GUV holding CPRG wants a different one from an
LUV holding CPRG or a GUV holding cytosol. So a design that declares none is not in
breach of anything — it is unmeasured, and a checker that failed on it would be
demanding fifteen numbers nobody has measured.

**The reason it is reported at all is that an absent setpoint must never default to
zero**, and the schema's rule to that effect is a sentence a reader has to go and
find. Two things go wrong with a defaulted zero:

- it marks every vesicle non-compliant on the corpus's own numbers, since the one
  design that states an offset states 125 with a tolerance of 25;
- **it is indistinguishable from a declared zero** — so whether a prep was *designed*
  at zero offset, a live bench question, would be answered by the schema instead of
  by an osmometer.

What is pinned here is the shape, not the count: that the pass runs, names both
sides, says silence is unmeasured rather than matched, and cannot turn a run red.
"""

import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).parent.parent
SCRIPT = REPO / "scripts" / "check-conflicts.py"


@pytest.fixture(scope="module")
def run():
    return subprocess.run([sys.executable, str(SCRIPT)], cwd=REPO,
                          capture_output=True, text=True)


def test_it_reports_the_split(run):
    assert "offsets:" in run.stdout
    line = next(l for l in run.stdout.splitlines() if l.startswith("offsets:"))
    assert "declare one" in line and "silent" in line


def test_a_declared_offset_is_shown_with_its_numbers(run):
    """A reader must be able to see what the one declared offset actually is."""
    declared = [l for l in run.stdout.splitlines() if l.strip().startswith("declared ")]
    assert declared, "the pass names no declared offset"
    assert all("setpoint" in l and "tolerance" in l for l in declared)


def test_silence_is_called_unmeasured_and_not_matched(run):
    """The wording is the point: 'silent' alone would read as 'no offset needed'."""
    assert "UNDECLARED, never 0" in run.stdout
    assert "unmeasured" in run.stdout
    assert "cannot be told from a declared one" in run.stdout


def test_it_never_fails_the_run(run):
    """Fifteen undeclared offsets must not turn a build red.

    This is the whole difference between a report and a rule. If this ever starts
    failing, somebody has turned an unmeasured quantity into a build error.
    """
    assert run.returncode == 0, run.stdout[-2000:]
