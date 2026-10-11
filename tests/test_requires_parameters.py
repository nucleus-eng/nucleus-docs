"""Pin what a `requires:` entry's `parameters:` may say, and the module-level `parameters:`.

An observation requirement names its operation by a bare id, `observe_fluorescence`,
and carries its parameters as keys: `ex` and `em`, each a closed interval in a length
unit. A class states a peak by naming one of its `member_properties` keys, and each
member states the value, in a step or, for a leaf with no step, in its own
`parameters:`.

Built from in-memory sources, so these need neither the corpus nor jsonschema. The
schema tests use jsonschema when it is installed and skip otherwise.
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


def doc(module="fluorophore", **extra):
    d = {"module": module, "title": module, "inputs": {}, "process_steps": []}
    d.update(extra)
    return d


def rules(findings):
    return [f[0] for f in findings]


def test_a_literal_interval_with_its_ends_the_right_way_round_passes():
    d = doc(requires=[{"id": "observe_fluorescence", "why": "x",
                       "parameters": {"ex": {"low": 496, "high": 516, "unit": "nm"}}}])
    assert css.requires_parameter_findings(d) == []


def test_a_low_end_above_the_high_end_is_reported():
    d = doc(requires=[{"id": "observe_fluorescence", "why": "x",
                       "parameters": {"ex": {"low": 516, "high": 496, "unit": "nm"}}}])
    assert rules(css.requires_parameter_findings(d)) == ["requires-parameter-interval"]


def test_a_unit_that_is_not_a_length_is_reported():
    pytest.importorskip("pint")
    d = doc(requires=[{"id": "observe_fluorescence", "why": "x",
                       "parameters": {"ex": {"low": 1, "high": 2, "unit": "mM"}}}])
    assert rules(css.requires_parameter_findings(d)) == ["requires-parameter-unit"]


def test_any_length_unit_is_accepted():
    pytest.importorskip("pint")
    d = doc(requires=[{"id": "observe_fluorescence", "why": "x",
                       "parameters": {"ex": {"low": 0.496, "high": 0.516, "unit": "um"}}}])
    assert css.requires_parameter_findings(d) == []


def test_a_peak_must_name_a_member_property_the_class_makes_members_state():
    ok = doc(member_properties=[{"keys": ["excitation_peak"], "title": "x", "unit": "nm"}],
             requires=[{"id": "observe_fluorescence", "why": "x",
                        "parameters": {"ex": {"peak": "excitation_peak", "bandwidth": 20, "unit": "nm"}}}])
    bad = doc(requires=[{"id": "observe_fluorescence", "why": "x",
                         "parameters": {"ex": {"peak": "excitation_peak", "bandwidth": 20, "unit": "nm"}}}])
    assert css.requires_parameter_findings(ok) == []
    assert rules(css.requires_parameter_findings(bad)) == ["requires-parameter-peak"]


def test_a_leaf_with_no_step_states_a_member_property_in_its_own_parameters():
    cls = ("docs/modules/fluorophore/spec.yml",
           doc(member_properties=[{"keys": ["excitation_peak"], "title": "x", "unit": "nm"}]))
    leaf = ("docs/modules/dye/spec.yml", doc("dye", refines="fluorophore", parameters={"excitation_peak": 506}))
    bare = ("docs/modules/bare/spec.yml", doc("bare", refines="fluorophore"))
    findings, checked = css.member_property_findings([cls, leaf, bare])
    assert checked == 2
    assert [f[1] for f in findings] == ["member-property"]
    assert "bare" in findings[0][3]


def test_a_step_value_wins_over_the_module_value():
    cls = ("docs/modules/fluorophore/spec.yml",
           doc(member_properties=[{"keys": ["a", "b"], "title": "x"}]))
    leaf = doc("dye", refines="fluorophore", parameters={"a": 9, "b": 1})
    leaf["process_steps"] = [{"id": "make", "parameters": {"a": 1, "b": 2}}]
    findings, _ = css.member_property_findings([cls, ("docs/modules/dye/spec.yml", leaf)])
    assert findings == []


jsonschema = pytest.importorskip("jsonschema")


def _validate(requires_entry):
    schema = yaml.safe_load(SCHEMA.read_text())
    sub = schema["properties"]["requires"]["items"]
    return list(jsonschema.Draft202012Validator(sub).iter_errors(requires_entry))


def test_the_id_may_carry_an_underscore():
    assert _validate({"id": "observe_fluorescence", "why": "x"}) == []


def test_parameters_take_either_shape_and_nothing_else():
    lit = {"id": "observe_fluorescence", "why": "x",
           "parameters": {"ex": {"low": 1, "high": 2, "unit": "nm"}}}
    peak = {"id": "observe_fluorescence", "why": "x",
            "parameters": {"ex": {"peak": "excitation_peak", "bandwidth": 20, "unit": "nm"}}}
    mixed = {"id": "observe_fluorescence", "why": "x",
             "parameters": {"ex": {"low": 1, "peak": "p", "unit": "nm"}}}
    non_ascii = {"id": "observe_absorbance", "why": "x",
                 "parameters": {"λ": {"low": 1, "high": 2, "unit": "nm"}}}
    assert _validate(lit) == [] and _validate(peak) == []
    assert _validate(mixed) != [] and _validate(non_ascii) != []


def test_optional_is_a_boolean():
    assert _validate({"id": "observe_fluorescence", "why": "x", "optional": True}) == []
    assert _validate({"id": "observe_fluorescence", "why": "x", "optional": "yes"}) != []
