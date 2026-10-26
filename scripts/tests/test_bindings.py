"""Tests for `binds:` -- rulings.md D210.

EVERY PASS IS PAIRED WITH THE FAILURE IT WOULD BE CONFUSED WITH. This check
FAILS rather than reports, by Jon's ruling: "agree, should fail". A binding only
exists because somebody wrote it, so one that does not fit is a wrong statement
rather than an unfilled gap, and there is nothing to grandfather -- the key's
instance count starts at zero.

Jon's own three cases are the first three tests: Color Change filled by the SUV
substrate passes, filled by a bare liposome fails, filled by the enzyme fails.
"""
import importlib.util as _u
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent.parent
_s = _u.spec_from_file_location("css", REPO / "scripts" / "check-spec-schema.py")
css = _u.module_from_spec(_s)
_s.loader.exec_module(css)

LIPO, SUV_LIPO = "Vesicle[liposome]", "Vesicle[SUV, liposome]"


def docs(bind_value, slot_type=LIPO, slot="substrate"):
    """A cascade binding a slot of `reporter`, plus two members to bind to."""
    return [
        ("docs/modules/suv/spec.yml",
         {"module": "suv", "type": SUV_LIPO, "title": "S", "inputs": {}, "process_steps": []}),
        ("docs/modules/enzyme/spec.yml",
         {"module": "enzyme", "type": "ColorChangeEnzyme", "title": "E",
          "inputs": {}, "process_steps": []}),
        ("docs/modules/reporter/spec.yml",
         {"module": "reporter", "type": "ColorReporter", "title": "R",
          "inputs": {slot: ({"title": "s", "type": slot_type} if slot_type
                            else {"title": "s", "page": "../suv/spec.md"})},
          "process_steps": []}),
        ("docs/modules/cascade/spec.yml",
         {"module": "cascade", "type": "Cascade", "title": "C",
          "inputs": {"reporter": {"title": "R", "page": "../reporter/spec.md",
                                  "binds": {slot: bind_value}}},
          "process_steps": []}),
    ]


def kinds(d):
    return [k for _, k, _, _ in css.binding_findings(d)]


def test_a_member_that_refines_the_slot_fits():
    assert kinds(docs("../suv/spec.md")) == []


def test_a_module_may_bind_a_type_rather_than_a_page():
    """Jon: "it's okay for a Module to bind a type"."""
    assert kinds(docs(SUV_LIPO)) == []


def test_a_bare_container_does_not_fit_a_loaded_slot():
    """THE CONTROL from #312's asymmetry, now with a caller."""
    assert kinds(docs(LIPO, slot_type=f"{LIPO}{{Substrate}}")) == ["binds-does-not-fit"]


def test_the_wrong_kind_of_member_does_not_fit():
    """Filled by the enzyme: ColorChangeEnzyme does not refine a liposome."""
    assert kinds(docs("../enzyme/spec.md")) == ["binds-does-not-fit"]


def test_a_slot_that_does_not_exist_is_reported():
    d = docs("../suv/spec.md")
    d[3][1]["inputs"]["reporter"]["binds"] = {"nosuch": "../suv/spec.md"}
    assert kinds(d) == ["binds-unknown-slot"]


def test_a_concrete_slot_has_nothing_to_bind():
    """Jon confirmed the read: a page slot already names one thing."""
    assert kinds(docs("../suv/spec.md", slot_type=None)) == ["binds-a-concrete-slot"]


def test_an_unresolvable_value_is_reported():
    assert kinds(docs("../nosuch/spec.md")) == ["binds-unresolvable"]


def test_no_binding_is_not_a_finding():
    """Silence is not an error: six class slots carry no binding today."""
    d = docs("../suv/spec.md")
    del d[3][1]["inputs"]["reporter"]["binds"]
    assert kinds(d) == []
