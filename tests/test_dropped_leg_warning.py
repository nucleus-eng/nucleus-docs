"""Pin that scripts/render-meet.py reports a cascade that contributes no leg.

The meet partitions legs by detector. A cascade whose detector input carries
`page: null` resolves to nothing, yields only `__join__`, and adds no leg. Until
2026-09-29 that was silent: naming four cascades and getting three printed
"3 leg(s)", exited 0, and never said which one did not arrive.

That is the false-clean shape -- the tool answers a question you did not ask and
calls it success. Jon ruled the remedy on 2026-09-29: "agree. warn, not refuse."
So the run still succeeds and still draws the meet it can draw. What is pinned
here is that it says so.

The fixture is deliberately not a cascade. craic-cascade was the live instance
when this was written, and writing docs/modules/detector-esar/ the same day fixed
it -- which is a good outcome and a bad test, since a passing corpus would have
made these tests vacuous without saying so. london-chassis has no detector at
all and is not a thing anybody is about to give one, so it is the stable case.
"""

import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).parent.parent
SCRIPT = REPO / "scripts" / "render-meet.py"


def _run(*cascades):
    return subprocess.run([sys.executable, str(SCRIPT), *cascades],
                          capture_output=True, text=True, cwd=REPO)


def test_a_cascade_with_no_leg_is_named_on_stderr():
    r = _run("atc-cascade", "ph-cascade", "london-chassis")
    assert "WARNING" in r.stderr
    assert "london-chassis" in r.stderr


def test_the_warning_says_how_many_of_how_many():
    """A bare "something was dropped" still leaves the reader counting."""
    r = _run("atc-cascade", "ph-cascade", "london-chassis")
    assert "1 of 3" in r.stderr


def test_it_warns_and_does_not_refuse():
    """Jon's ruling. The meet over the legs that did resolve is still worth having."""
    r = _run("atc-cascade", "ph-cascade", "london-chassis")
    assert r.returncode == 0
    assert "flowchart TD" in r.stdout


def test_a_clean_run_says_nothing():
    """The warning must not fire where every named cascade contributes, or it
    becomes noise and stops being read."""
    r = _run("atc-cascade", "ph-cascade")
    assert "WARNING" not in r.stderr
    assert r.returncode == 0


def test_the_drawn_meet_excludes_the_dropped_cascade():
    """The warning is worth nothing if the figure silently included it anyway.

    The leg count is on stderr with the rest of the summary; stdout carries only
    the mermaid. The figure states its own count in the DOMAIN node.
    """
    r = _run("atc-cascade", "ph-cascade", "london-chassis")
    assert "2 leg(s)" in r.stderr
    assert "Meet over 2 legs" in r.stdout
    assert "london-chassis" not in r.stdout
