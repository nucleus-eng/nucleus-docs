"""Tests for the contents type `A{B}`, read by scripts/check-spec-schema.py.

THESE TESTS CAN FAIL, and the ones that matter most are the negative ones.
`_type_refines` has NO CALLER in this repository yet -- it was built on a ruling
of 2026-10-20 -- so the only thing standing between it and silent rot is a test
that fails when the rule is broken. Every positive case below is paired with the
negative that a wrong implementation would also return True for.

THE ASYMMETRY IS THE WHOLE POINT. A loaded container refines a bare one and a
bare one does not refine a loaded one. An implementation that made the relation
symmetric would satisfy a slot wanting a loaded liposome with an empty one, which
is the under-specification the contents type exists to prevent.
"""
import importlib.util as _u
from pathlib import Path

import pytest

_SPEC = Path(__file__).resolve().parent.parent / "check-spec-schema.py"
_s = _u.spec_from_file_location("check_spec_schema", _SPEC)
css = _u.module_from_spec(_s)
_s.loader.exec_module(css)

# Names used below, all real nodes of the published order.
LIPO = "Vesicle[liposome]"
SUV_LIPO = "Vesicle[SUV, liposome]"


# --- the reader ------------------------------------------------------------

@pytest.mark.parametrize("name", [
    LIPO,                                    # a plain node still resolves
    f"{LIPO}{{Substrate}}",                  # one level
    f"Gel{{{LIPO}{{Substrate}}}}",           # nesting, the pH demo's arrangement
])
def test_a_contents_type_resolves_when_both_halves_do(name):
    assert css._type_resolves(name)


@pytest.mark.parametrize("name", [
    f"{LIPO}{{NotAType}}",     # payload is not a node
    "NotAType{Substrate}",     # container is not a node
    "NotAType",                # neither, and no braces
    f"Gel{{NotAType}}",        # nesting does not excuse the inner half
])
def test_a_contents_type_does_not_resolve_when_a_half_does_not(name):
    assert not css._type_resolves(name)


def test_the_reader_checks_the_payload_and_not_only_the_container():
    """The control for a reader that stops at the first half."""
    assert css._type_resolves(f"{LIPO}{{Substrate}}")
    assert not css._type_resolves(f"{LIPO}{{NotAType}}")


# --- the ordering ----------------------------------------------------------

def test_a_loaded_container_refines_the_bare_one():
    assert css._type_refines(f"{LIPO}{{Substrate}}", LIPO)


def test_a_bare_container_does_not_refine_a_loaded_one():
    """THE CONTROL. An empty liposome must not satisfy a slot wanting a loaded one.

    A symmetric implementation passes the test above and fails this one.
    """
    assert not css._type_refines(LIPO, f"{LIPO}{{Substrate}}")


def test_the_container_half_is_ordered_by_the_published_order():
    assert css._type_refines(f"{SUV_LIPO}{{Substrate}}", f"{LIPO}{{Substrate}}")
    assert not css._type_refines(f"{LIPO}{{Substrate}}", f"{SUV_LIPO}{{Substrate}}")


def test_the_payload_half_is_ordered_too():
    """Covariance: an unrelated payload does not refine, in either direction."""
    assert not css._type_refines(f"{LIPO}{{Substrate}}", f"{LIPO}{{Protein}}")
    assert not css._type_refines(f"{LIPO}{{Protein}}", f"{LIPO}{{Substrate}}")


def test_a_type_refines_itself():
    assert css._type_refines(f"{LIPO}{{Substrate}}", f"{LIPO}{{Substrate}}")
