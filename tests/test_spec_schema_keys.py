"""Pin the two class-wide checks in scripts/check-spec-schema.py.

`member_properties:` lets a class name the quantities every member states, and
`member_property_findings` is what makes that a requirement. `substrates:` lets an
enzyme module list what it acts on, and `substrate_findings` checks that every
member of a pairing class pairs its enzyme with one of them.

Both are built from in-memory sources, so these tests need neither the corpus
nor jsonschema. The last two use jsonschema when it is installed, to pin the
shape of the two schema blocks, and skip otherwise.
"""

import importlib.util
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent
SCRIPT = ROOT / "scripts" / "check-spec-schema.py"
SCHEMA = ROOT / "scripts" / "spec-yml-schema.yml"


def _load():
    spec = importlib.util.spec_from_file_location("check_spec_schema", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


css = _load()


def src(module, refines=None, params=None, inputs=None, **extra):
    """A minimal (path, doc) pair. `params` become one step's `parameters:`."""
    doc = {"module": module, "title": module, "inputs": inputs or {}, "process_steps": []}
    if refines:
        doc["refines"] = refines
    if params is not None:
        doc["process_steps"] = [{"id": "make", "parameters": params}]
    doc.update(extra)
    return (f"docs/modules/{module}/spec.yml", doc)


RANGE = [{"keys": ["gel_point_min_c", "gel_point_max_c"], "title": "Gelling range"},
         {"keys": ["melting_point_c"], "title": "Melting temperature"}]


# --- member_properties -------------------------------------------------------

def test_members_stating_every_key_pass():
    docs = [src("thermal-gel", member_properties=RANGE),
            src("gel-a", "thermal-gel", {"gel_point_min_c": 8, "gel_point_max_c": 17, "melting_point_c": 50}),
            src("gel-b", "thermal-gel", {"gel_point_min_c": 26, "gel_point_max_c": 30, "melting_point_c": 65})]
    out, checked = css.member_property_findings(docs)
    assert out == []
    assert checked == 2


def test_a_member_missing_a_key_is_reported():
    docs = [src("thermal-gel", member_properties=RANGE),
            src("gel-b", "thermal-gel", {"gel_point_max_c": 30, "melting_point_c": 65})]
    out, _ = css.member_property_findings(docs)
    assert len(out) == 1
    path, kind, where, msg = out[0]
    assert path == "docs/modules/gel-b/spec.yml" and kind == "member-property"
    assert "gel_point_min_c" in where and "requires gel_point_min_c" in msg


def test_a_low_end_above_the_high_end_is_reported():
    docs = [src("thermal-gel", member_properties=RANGE),
            src("gel-b", "thermal-gel", {"gel_point_min_c": 40, "gel_point_max_c": 30, "melting_point_c": 65})]
    out, _ = css.member_property_findings(docs)
    assert len(out) == 1 and "above the high end" in out[0][3]


def test_a_subclass_is_skipped_and_passes_its_values_down():
    # gel -> mid (states melting_point_c) -> leaf (states the range only).
    # mid is abstract below the class, so it is not checked itself, and leaf
    # inherits melting_point_c from it.
    docs = [src("gel", member_properties=RANGE),
            src("mid", "gel", {"melting_point_c": 65}),
            src("leaf", "mid", {"gel_point_min_c": 26, "gel_point_max_c": 30})]
    out, checked = css.member_property_findings(docs)
    assert out == [] and checked == 1


def test_a_refines_cycle_does_not_hang():
    docs = [src("a", "b", member_properties=RANGE), src("b", "a")]
    css.member_property_findings(docs)  # returns rather than looping


# --- substrates --------------------------------------------------------------

LACZ_LIST = [{"title": "CPRG", "page": "../substrate-cprg/spec.md"},
             {"title": "X-Gal", "page": "../substrate-xgal/spec.md"}]


def test_an_enzyme_paired_by_page_passes():
    docs = [src("color-change"), src("lacz", substrates=LACZ_LIST),
            src("reporter-lacz", "color-change", inputs={
                "lacz": {"title": "LacZ", "page": "../lacz/spec.md"},
                "substrate-cprg": {"title": "Substrate: CPRG", "page": "../substrate-cprg/spec.md"}})]
    out, checked = css.substrate_findings(docs)
    assert out == [] and checked == 1


def test_an_inherited_list_and_a_title_match_pass():
    # The enzyme input points at a module that refines the one with the list,
    # and the substrate has no page, so the match is by title, ignoring case.
    docs = [src("color-change"), src("xyle", substrates=[{"title": "Catechol", "page": None}]),
            src("xyle-dna", "xyle"),
            src("reporter-xyle", "color-change", inputs={
                "enzyme": {"title": "XylE DNA", "page": "../xyle-dna/spec.md"},
                "catechol": {"title": "catechol", "page": None}})]
    out, checked = css.substrate_findings(docs)
    assert out == [] and checked == 1


def test_a_substrate_not_on_the_list_is_reported():
    docs = [src("color-change"), src("lacz", substrates=LACZ_LIST),
            src("reporter-lacz", "color-change", inputs={
                "lacz": {"title": "LacZ", "page": "../lacz/spec.md"},
                "catechol": {"title": "Catechol", "page": None}})]
    out, _ = css.substrate_findings(docs)
    assert len(out) == 1
    path, kind, where, msg = out[0]
    assert path == "docs/modules/reporter-lacz/spec.yml" and kind == "substrate"
    assert where == "inputs/lacz" and "CPRG, X-Gal" in msg


def test_a_member_with_no_listed_enzyme_is_not_checked():
    docs = [src("color-change"),
            src("reporter-xyle", "color-change", inputs={
                "catecholase-dna": {"title": "Catecholase DNA template", "page": None},
                "catechol": {"title": "Catechol", "page": None}})]
    out, checked = css.substrate_findings(docs)
    assert out == [] and checked == 0


# --- the two schema blocks ---------------------------------------------------

def _validator():
    js = pytest.importorskip("jsonschema")
    return js.Draft202012Validator(yaml.safe_load(SCHEMA.read_text()))


def test_the_schema_accepts_both_keys():
    _, doc = src("thermal-gel", member_properties=RANGE,
                 substrates=[{"title": "Catechol", "page": None}])
    assert list(_validator().iter_errors(doc)) == []


def test_the_schema_rejects_a_three_key_range_and_an_untitled_substrate():
    v = _validator()
    _, a = src("x", member_properties=[{"keys": ["a", "b", "c"], "title": "t"}])
    _, b = src("y", substrates=[{"page": None}])
    assert list(v.iter_errors(a)) and list(v.iter_errors(b))
