"""Pin how scripts/render-meet.py picks a parent when `refines:` is a list.

`refines:` has allowed a list since 2026-09-24, meaning two incomparable
parents. The meet renderer aligns two products when they share an immediate
parent, so with two parents it had no "the" parent and refused rather than
pick, on the ground that picking arbitrarily makes two products align or not
depending on which entry survived.

Aligning by the functional parent removes the arbitrariness rather than the choice:
"align by the functional parent". The convention carrying it is positional --
entry one is the alignment parent -- so the source declares it and the reader
does not guess. These tests pin that it reads entry one, that it still accepts
the plain string, and that it still refuses a one-element list.
"""

import importlib.util
from pathlib import Path

import pytest

SCRIPT = Path(__file__).parent.parent / "scripts" / "render-meet.py"


def _load():
    spec = importlib.util.spec_from_file_location("render_meet", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


render_meet = _load()


def test_string_refines_is_unchanged():
    """The normal form still works and is still the normal form."""
    assert render_meet.parents({"a": {"refines": "b"}}) == {"a": "b"}


def test_list_aligns_on_the_first_entry():
    """Entry one is the functional parent. The chassis is entry two and is ignored."""
    S = {"ahsl-sensing-cell": {"refines": ["sensing-cell", "cell-s30-popc"]},
         "atc-sensing-cell": {"refines": ["sensing-cell", "cell-base-cytosol-popc-chol"]}}
    par = render_meet.parents(S)
    assert par == {"ahsl-sensing-cell": "sensing-cell",
                   "atc-sensing-cell": "sensing-cell"}


def test_two_cells_on_different_chassis_still_align():
    """The point of the rule. These two differ in chassis and must still share a
    slot, because the chassis is what differs between demos and the functional
    parent is the axis they can be compared on."""
    S = {"ahsl-sensing-cell": {"refines": ["sensing-cell", "cell-s30-popc"]},
         "atc-sensing-cell": {"refines": ["sensing-cell", "cell-base-cytosol-popc-chol"]}}
    par = render_meet.parents(S)
    assert render_meet.slot_key("ahsl-sensing-cell", par) == \
           render_meet.slot_key("atc-sensing-cell", par)


def test_order_is_load_bearing():
    """Putting the chassis first changes the slot. The convention is positional,
    so a source that orders it wrongly gets a different figure rather than a
    warning -- which is why the schema states the rule where the key is defined."""
    par = render_meet.parents({"x": {"refines": ["cell-s30-popc", "sensing-cell"]}})
    assert par == {"x": "cell-s30-popc"}


def test_one_element_list_is_refused():
    """`minItems: 2` means a one-element list can only be a second spelling of
    the string form, so it is an error rather than a silent equivalent."""
    with pytest.raises(ValueError, match="second spelling"):
        render_meet.parents({"x": {"refines": ["sensing-cell"]}})


def test_module_with_no_refines_is_absent():
    """A root has no parent and keys to itself in slot_key, which is a finding
    rather than a merge."""
    assert render_meet.parents({"cell": {}}) == {}
