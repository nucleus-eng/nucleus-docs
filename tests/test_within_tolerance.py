"""Pin how scripts/check-conflicts.py orders two `within` bounds on one condition.

`_tighter` decides which of a class's bound and a member's bound wins, and the
strictest wins by every route. For `at-most` the smaller value is stricter, and for
`at-least` the larger. A `within` bound is a tolerance around a setpoint, so the
smaller tolerance is the stricter one, which is the `at-most` order and not the
fallback it used to take. Two different setpoints are two designed differences, so
neither is stricter than the other.

No source declares two `within` bounds on one id yet, so the corpus cannot show
either case. It will the first time a class states a tolerance that a member
sharpens.
"""

import contextlib
import importlib.util
import io
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


CLASS = {"quantity": "osmolality", "sense": "within", "unit": "mOsm/kg",
         "setpoint": 125, "value": 25}


def test_a_smaller_tolerance_is_tighter(cc):
    member = dict(CLASS, value=10)
    assert cc._tighter(member, CLASS) == ("a", None)
    assert cc._tighter(CLASS, member) == ("b", None)


def test_a_larger_tolerance_is_looser(cc):
    assert cc._tighter(dict(CLASS, value=40), CLASS) == ("b", None)


def test_two_setpoints_do_not_compare(cc):
    keep, why = cc._tighter(dict(CLASS, setpoint=0), CLASS)
    assert keep is None
    assert "setpoint" in why


def test_the_other_senses_are_unchanged(cc):
    hot = {"quantity": "temperature", "sense": "at-most", "unit": "°C"}
    assert cc._tighter(dict(hot, value=30), dict(hot, value=37)) == ("a", None)
    floor = {"quantity": "temperature", "sense": "at-least", "unit": "°C"}
    assert cc._tighter(dict(floor, value=30), dict(floor, value=37)) == ("b", None)
