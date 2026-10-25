"""Tests for scripts/check-requirements.py.

A checker that was never shown to fail has not been shown to work. So the key tests here
come in pairs: one runs the real code and expects a pass, and one runs a deliberately
broken copy of the code and expects the SAME assertions to fail. Three mutants stand for
the three ways this walker could silently turn into something that always agrees:

  - the matcher falls back to string equality (R1),
  - every constituent of a composite is treated as sharing one compartment (R3),
  - a child that says nothing is read as a child that denies (R5).

If a change makes one of those mutants pass, the check can no longer fail there, and the
test named `test_mutant_...` says which one.

The fixtures write small trees to tmp_path and never read the real corpus, except for one
smoke test that asserts nothing about what the corpus contains.
"""

import importlib.util
import json
from pathlib import Path

import pytest

# The CI job that runs this directory installs pytest and nothing else. Without pyyaml this
# module skips instead of breaking the whole run at collection.
yaml = pytest.importorskip("yaml")


def _load_module():
    """Import check-requirements.py by path (hyphenated filename)."""
    path = Path(__file__).resolve().parent.parent / "check-requirements.py"
    spec = importlib.util.spec_from_file_location("check_requirements", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


cr = _load_module()


# --------------------------------------------------------------------------- #
# Fixtures
# --------------------------------------------------------------------------- #

# A small order that holds the schema's own examples. `linearDNA` is a node here, which is
# what the schema says a requirer would force into being. `pT7` and `sigma70` have none.
TYPE_EDGES = {
    "RNA": ["NucleicAcid"],
    "DNA": ["NucleicAcid"],
    "linearDNA": ["DNA"],
    "NucleicAcid": ["Component"],
    "Container": ["Component"],
    "Solution": ["Container"],
    "Cytosol": ["Solution"],
    "Gel": ["Container"],
    "Chromophore": ["Component"],
}
PROC_EDGES = {"emit_fluorescence": ["emit_color"], "emit_color": ["emit"], "observe_absorbance": ["observe"]}
ORDER = {
    "orders": {
        "type_refinement": {"edges": TYPE_EDGES},
        "process_refinement": {"edges": PROC_EDGES},
    },
    "module_slugs": {"cytosol": "Cytosol", "solution": "Solution"},
}


def mod(slug, **kw):
    """The smallest module source the walker reads."""
    doc = {"module": slug, "type": kw.pop("type", "Component"), "title": slug, "inputs": {}, "process_steps": []}
    doc.update(kw)
    return doc


def proc(slug, **kw):
    doc = {"process": slug, "title": slug}
    doc.update(kw)
    return doc


def tree(root, modules=(), processes=(), order=ORDER):
    for kind, docs in (("modules", modules), ("processes", processes)):
        for doc in docs:
            d = root / "docs" / kind / doc.get("module", doc.get("process"))
            d.mkdir(parents=True, exist_ok=True)
            (d / "spec.yml").write_text(yaml.safe_dump(doc, sort_keys=False))
    if order is not None:
        (root / "docs").mkdir(parents=True, exist_ok=True)
        (root / "docs" / "type-order.yml").write_text(yaml.safe_dump(order))
    return root


def walk(tmp_path, **kw):
    return cr.walk(cr.Corpus.load(tree(tmp_path, **kw)))


def codes(items):
    return sorted((i.code, i.where) for i in items)


def own_gaps(res):
    """The gaps about the sources. An order without `type_declares` always adds one about itself."""
    return [c for c in codes(res.gaps) if c[0] != "type-declares-absent"]


# --------------------------------------------------------------------------- #
# R1: the schema's own worked examples, and the matcher that cannot pass the fifth
# --------------------------------------------------------------------------- #

# From scripts/spec-yml-schema.yml, `provides.description`. (provider, requirer, met?)
WORKED = [
    ("transcribe[pT7]", "transcribe", True),
    ("transcribe[sigma70]", "transcribe", True),
    ("transcribe[sigma70]", "transcribe[pT7]", False),
    ("degrade[linearDNA]", "degrade[DNA]", False),
    ("degrade[DNA]", "degrade[linearDNA]", True),
    ("degrade[RNA]", "degrade[NucleicAcid]", False),
]


def string_equality(provided, required):
    """The matcher that was in the repo: collate-conditions.py's `meets()`, retyped."""
    pop, _, prest = provided.partition("[")
    rop, _, rrest = required.partition("[")
    pr, rr = prest.rstrip("]") or None, rrest.rstrip("]") or None
    return pop == rop and (rr is None or pr == rr)


def disagreements(meets):
    return [(p, r, want) for p, r, want in WORKED if meets(p, r) != want]


def schema_meets(module):
    order = module.Order(TYPE_EDGES, PROC_EDGES)
    return lambda p, r: module.dispatch("operation", p, r, order).status == "met"


def test_string_equality_gets_exactly_one_worked_example_wrong():
    """The claim that started this, pinned. Four of five need no order, so they pass by luck."""
    assert disagreements(string_equality) == [("degrade[DNA]", "degrade[linearDNA]", True)]


def test_the_dispatcher_agrees_with_every_worked_example():
    assert disagreements(schema_meets(cr)) == []


def test_mutant_string_equality_is_caught_by_the_worked_examples(monkeypatch):
    """If the matcher were string equality, the assertion above would fail."""
    monkeypatch.setattr(
        cr, "cmp_operation", lambda p, r, order: cr.Verdict(cr.MET if string_equality(p, r) else cr.UNMET, "mutant")
    )
    assert disagreements(schema_meets(cr)) != []


def test_mutant_that_widens_the_wrong_way_is_caught(monkeypatch):
    """Covariance, which is the natural mistake: a narrower provider would meet a wider requirer."""
    real = cr.cmp_operation

    def flipped(provided, required, order):
        return real(required, provided, order)

    monkeypatch.setattr(cr, "cmp_operation", flipped)
    assert disagreements(schema_meets(cr)) != []


def test_the_fifth_example_is_decided_by_the_order_and_not_by_luck():
    """With no order, `linearDNA` has no node and compares only to itself."""
    empty = cr.Order()
    v = cr.dispatch("operation", "degrade[DNA]", "degrade[linearDNA]", empty)
    assert (v.status, v.via) == (cr.UNMET, "no node")
    with_order = cr.Order(TYPE_EDGES)
    assert cr.dispatch("operation", "degrade[DNA]", "degrade[linearDNA]", with_order).status == cr.MET


def test_a_bare_requirement_is_not_the_top_type():
    order = cr.Order(TYPE_EDGES)
    assert cr.dispatch("operation", "transcribe[pT7]", "transcribe", order).status == cr.MET
    # A provider that names no type says nothing about how wide it is.
    assert cr.dispatch("operation", "transcribe", "transcribe[pT7]", order).status == cr.UNDETERMINED


def test_a_different_operation_is_unmet_and_a_finer_one_meets_the_coarser():
    order = cr.Order(TYPE_EDGES, PROC_EDGES)
    assert cr.dispatch("operation", "translate", "transcribe", order).status == cr.UNMET
    v = cr.dispatch("operation", "emit_fluorescence", "emit_color", order)
    assert (v.status, v.via) == (cr.MET, "operation order")
    assert cr.dispatch("operation", "emit_color", "emit_fluorescence", order).status == cr.UNMET
    # The schema says nothing about a bracket crossing a refinement.
    assert cr.dispatch("operation", "emit_fluorescence", "emit_color[RNA]", order).status == cr.UNDETERMINED


def test_a_list_of_types_and_a_malformed_id_are_undetermined_and_never_a_pass():
    order = cr.Order(TYPE_EDGES)
    assert cr.dispatch("operation", "degrade[DNA,RNA]", "degrade[DNA]", order).status == cr.UNDETERMINED
    assert cr.dispatch("operation", "Degrade!", "degrade", order).status == cr.UNDETERMINED


def test_a_type_with_no_node_gets_a_hint_from_another_spelling_and_never_uses_it():
    """`linearDNA` against a published `DNA[linear]`: the same words, a different name."""
    order = cr.Order({"DNA[linear]": ["DNA"], "DNA": ["NucleicAcid"]})
    v = cr.dispatch("operation", "degrade[DNA]", "degrade[linearDNA]", order)
    assert v.status == cr.UNMET and "DNA[linear]" in v.hint


def test_the_published_order_is_read_for_nodes_listed_or_not():
    listed = cr.Order({"A": ["B"]}, type_nodes=["A", "B", "Lonely"])
    assert "Lonely" in listed.type_nodes and listed.nodes_listed
    derived = cr.Order({"A": ["B"]})
    assert derived.type_nodes == {"A", "B"} and not derived.nodes_listed


def test_a_cycle_in_the_published_order_is_a_finding(tmp_path):
    bad = {"orders": {"type_refinement": {"edges": {"A": ["B"], "B": ["A"]}}, "process_refinement": {"edges": {}}}}
    res = walk(tmp_path, modules=[mod("m")], order=bad)
    assert [i.code for i in res.findings] == ["order-cycle"]


def test_the_operation_order_alone_can_decide_a_bracket():
    """`degrade[RNA]` refines `degrade[NucleicAcid]` as published, with no type nodes at all."""
    order = cr.Order(proc_edges={"degrade[RNA]": ["degrade[NucleicAcid]"]})
    v = cr.dispatch("operation", "degrade[NucleicAcid]", "degrade[RNA]", order)
    assert (v.status, v.via) == (cr.MET, "operation order")
    assert cr.dispatch("operation", "degrade[RNA]", "degrade[NucleicAcid]", order).status == cr.UNMET


def test_a_type_name_resolves_exactly_then_by_slug_then_by_the_normalized_match_and_never_by_guess():
    order = cr.Order(
        {"ssDNA": ["DNA"], "Gel[thermally-set]": ["Gel"], "Solution": [], "Sol-ution": []},
        slugs={"outer-solution": "Solution"},
    )
    assert order.resolve_type("ssDNA") == "ssDNA"  # exact
    assert order.resolve_type("outer-solution") == "Solution"  # a slug the order maps
    assert order.resolve_type("ssdna") == "ssDNA"  # lowercase, hyphens dropped
    assert order.resolve_type("gel[thermallyset]") == "Gel[thermally-set]"
    assert order.resolve_type("solution") is None  # two nodes answer to it: no guess
    assert order.resolve_type("nonsense") is None


def test_r1_reports_who_meets_each_requirement_and_what_has_no_provider(tmp_path):
    res = walk(
        tmp_path,
        modules=[
            mod("detector", requires=[{"id": "transcribe", "why": "x"}, {"id": "observe", "why": "x"}]),
            mod("cyt", provides=[{"id": "transcribe[pT7]", "why": "x"}]),
        ],
    )
    assert ("no-provider", "detector") in codes(res.gaps)
    assert sum(1 for i in res.gaps if i.code == "no-provider") == 1  # only `observe`
    assert any("met by cyt" in line for line in res.sections["R1"])
    assert res.counts["bracket_types_without_node"] == 1  # pT7 has no node


def test_a_malformed_id_is_a_finding(tmp_path):
    res = walk(tmp_path, modules=[mod("m", requires=[{"id": "Not An Id", "why": "x"}])])
    assert [(i.code, i.where) for i in res.findings] == [("malformed-id", "m")]


# --------------------------------------------------------------------------- #
# R2: inheritance down refines:
# --------------------------------------------------------------------------- #


def test_a_member_has_what_its_class_requires_and_provides(tmp_path):
    corpus = cr.Corpus.load(
        tree(
            tmp_path,
            modules=[
                mod("cls", requires=[{"id": "transcribe", "why": "x"}], provides=[{"id": "translate", "why": "x"}]),
                mod("member", refines="cls"),
                mod("grandchild", refines="member"),
            ],
        )
    )
    got = {(e["id"], origin) for e, origin in corpus.effective("grandchild", "requires")}
    assert got == {("transcribe", "cls")}
    assert {(e["id"], o) for e, o in corpus.effective("grandchild", "provides")} == {("translate", "cls")}
    assert corpus.ancestors("module", "grandchild") == ["member", "cls"]


def test_a_refines_that_names_a_type_finds_its_class_through_the_order(tmp_path):
    corpus = cr.Corpus.load(
        tree(
            tmp_path,
            modules=[
                mod("cytosol", provides=[{"id": "translate", "why": "x"}]),
                mod("base-cytosol", refines="Cytosol"),
            ],
        )
    )
    assert corpus.parents("module", "base-cytosol") == (["cytosol"], [])


def test_a_refines_that_names_a_type_with_a_different_slug_is_found_only_through_the_slug_map(tmp_path):
    """`outer-solution` is `Solution`. Normalizing `Solution` gives `solution`, which is another slug."""
    order = {
        "orders": {"type_refinement": {"edges": {"Solution": ["Container"]}}, "process_refinement": {"edges": {}}},
        "module_slugs": {"outer-solution": "Solution"},
    }
    corpus = cr.Corpus.load(
        tree(
            tmp_path,
            modules=[
                mod("outer-solution", provides=[{"id": "hold", "why": "x"}]),
                mod("solution-member", refines="Solution"),
            ],
            order=order,
        )
    )
    assert corpus.parents("module", "solution-member") == (["outer-solution"], [])


def test_a_refines_with_no_source_is_a_gap_and_not_a_finding(tmp_path):
    res = walk(tmp_path, modules=[mod("m", refines="Vesicle[liposome]")])
    assert own_gaps(res) == [("refines-no-source", "m")] and not res.findings
    assert res.counts["refines_without_source"] == 1


@pytest.mark.parametrize("ring", [["a", "b"], ["a", "b", "c"], ["a"]])
def test_a_refines_cycle_terminates_and_is_one_finding(tmp_path, ring):
    nxt = {ring[i]: ring[(i + 1) % len(ring)] for i in range(len(ring))}
    res = walk(tmp_path, modules=[mod(s, refines=nxt[s]) for s in ring])
    assert [i.code for i in res.findings] == ["refines-cycle"]


# --------------------------------------------------------------------------- #
# R3: discharge in a composite
# --------------------------------------------------------------------------- #

CLASS = mod("repressor-detector", requires=[{"id": "transcribe", "why": "a repressor gates transcription"}])
MEMBER = mod("detector-x", refines="repressor-detector")
CYTOSOL = mod("cytosol-t7", provides=[{"id": "transcribe[pT7]", "why": "T7 polymerase"}])


def composite(slug, operator, operands=("det", "cyt"), extra_inputs=(), pairs=None, steps=None):
    inputs = {
        "det": {"title": "d", "page": "../detector-x/spec.md"},
        "cyt": {"title": "c", "page": "../cytosol-t7/spec.md"},
    }
    for name in extra_inputs:
        inputs[name] = {"title": name, "page": None}
    step = {
        "id": "s1",
        "process": {"title": "p", "page": None},
        "operator": operator,
        "operands": list(operands),
        "produces": {"id": slug, "title": slug, "page": None},
    }
    if pairs:
        step["operator_pairs"] = pairs
    return mod(slug, inputs=inputs, process_steps=steps or [step])


def scenario_packing_keeps_a_provider_apart(module, tmp_path):
    """The assertions R3 stands on. The mutant test runs these against a broken copy."""
    corpus = module.Corpus.load(
        tree(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, composite("together", "mixing"), composite("apart", "packing")])
    )
    res = module.walk(corpus)
    found = {(i.code, i.where) for i in res.findings}
    assert ("provider-in-another-compartment", "apart") in found
    assert not any(where == "together" for _, where in found)
    assert res.counts["discharged_in_composites"] == 1


def test_mixing_discharges_and_packing_does_not(tmp_path):
    scenario_packing_keeps_a_provider_apart(cr, tmp_path)


def test_mutant_one_compartment_for_everything_is_caught(tmp_path, monkeypatch):
    """If every constituent shared a compartment, packing could never fail to discharge."""
    monkeypatch.setattr(cr.Composite, "shares", lambda self, a, b: "yes")
    with pytest.raises(AssertionError):
        scenario_packing_keeps_a_provider_apart(cr, tmp_path)


def product_unit_composite(slug, pair_operator, requirer_in_pair):
    """A product whose page is the provider, made by `pair_operator` from `cyt` and a second operand."""
    inputs = {
        "det": {"title": "d", "page": "../detector-x/spec.md"},
        "cyt": {"title": "c", "page": None},
        "mem": {"title": "m", "page": None},
    }
    operands = ["det", "cyt"] if requirer_in_pair else ["cyt", "mem"]
    step = {
        "id": "make",
        "process": {"title": "p", "page": None},
        "operator": pair_operator,
        "operands": operands,
        "produces": {"id": "made", "title": "made", "page": "../cytosol-t7/spec.md"},
    }
    return mod(slug, inputs=inputs, process_steps=[step])


def test_a_provider_that_is_several_compartments_which_include_the_requirers_is_undetermined(tmp_path):
    """The product spans `det` and `cyt` kept apart. Which of its compartments is the provider's own is not stated."""
    res = walk(
        tmp_path, modules=[CLASS, MEMBER, CYTOSOL, product_unit_composite("spans", "packing", requirer_in_pair=True)]
    )
    assert not res.findings
    assert ("discharge-undetermined", "spans") in codes(res.gaps)


def test_a_provider_that_is_several_compartments_none_of_them_the_requirers_is_in_another_compartment(tmp_path):
    res = walk(
        tmp_path,
        modules=[CLASS, MEMBER, CYTOSOL, product_unit_composite("elsewhere", "packing", requirer_in_pair=False)],
    )
    assert [(i.code, i.where) for i in res.findings] == [("provider-in-another-compartment", "elsewhere")]


def test_a_requirement_inherited_through_refines_is_discharged_for_the_member(tmp_path):
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, composite("together", "mixing")])
    assert any("detector-x requires `transcribe`: DISCHARGED by cytosol-t7" in line for line in res.sections["R3"])


def test_an_exception_pair_can_put_two_operands_together_inside_a_packing_step(tmp_path):
    together = composite(
        "pair-mixed",
        "packing",
        operands=("det", "cyt", "other"),
        extra_inputs=("other",),
        pairs=[{"operands": ["det", "cyt"], "operator": "mixing"}],
    )
    apart = composite(
        "pair-not-mixed",
        "packing",
        operands=("det", "cyt", "other"),
        extra_inputs=("other",),
        pairs=[{"operands": ["det", "other"], "operator": "mixing"}],
    )
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, together, apart])
    found = {(i.code, i.where) for i in res.findings}
    assert ("provider-in-another-compartment", "pair-not-mixed") in found
    assert not any(where == "pair-mixed" for _, where in found)


def test_exceptions_that_contradict_through_a_third_operand_are_undetermined(tmp_path):
    """det mixes with other, cyt mixes with other, and the label says det and cyt stay apart."""
    odd = composite(
        "odd",
        "packing",
        operands=("det", "cyt", "other"),
        extra_inputs=("other",),
        pairs=[
            {"operands": ["det", "other"], "operator": "mixing"},
            {"operands": ["cyt", "other"], "operator": "mixing"},
        ],
    )
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, odd])
    assert not res.findings
    assert ("compartment-unknown", "odd") in codes(res.gaps)
    assert ("discharge-undetermined", "odd") in codes(res.gaps)


def test_mixing_a_unit_that_is_already_several_compartments_is_undetermined(tmp_path):
    inputs = {
        "det": {"title": "d", "page": "../detector-x/spec.md"},
        "cyt": {"title": "c", "page": "../cytosol-t7/spec.md"},
        "mem": {"title": "m", "page": None},
    }
    steps = [
        {
            "id": "encapsulate",
            "process": {"title": "p", "page": None},
            "operator": "packing",
            "operands": ["cyt", "mem"],
            "produces": {"id": "vesicle", "title": "v", "page": None},
        },
        {
            "id": "dose",
            "process": {"title": "p", "page": None},
            "operator": "mixing",
            "operands": ["det", "vesicle"],
            "produces": {"id": "cell", "title": "c", "page": None},
        },
    ]
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, mod("cell", inputs=inputs, process_steps=steps)])
    assert not res.findings
    assert ("compartment-unknown", "cell") in codes(res.gaps)


def test_an_operand_that_names_nothing_is_undetermined_and_does_not_crash(tmp_path):
    steps = [
        {
            "id": "s",
            "process": {"title": "p", "page": None},
            "operator": "mixing",
            "operands": ["det", "ghost"],
            "produces": {"id": "x", "title": "x", "page": None},
        }
    ]
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, composite("c", "mixing", steps=steps)])
    assert not res.findings
    assert ("compartment-unknown", "c") in codes(res.gaps)


def test_a_provider_that_is_optional_does_not_discharge(tmp_path):
    comp = composite("with-optional", "mixing")
    comp["inputs"]["cyt"]["optional"] = True
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, comp])
    assert not res.findings and ("discharge-undetermined", "with-optional") in codes(res.gaps)


def test_a_requirement_with_no_provider_anywhere_is_one_gap_and_never_a_finding_per_composite(tmp_path):
    """`observe` is met by an instrument, which is not a module. No composite could discharge it."""
    res = walk(
        tmp_path,
        modules=[
            mod("chromophore", requires=[{"id": "observe", "why": "x"}]),
            mod("dye", refines="chromophore"),
            mod(
                "c1",
                inputs={"d": {"title": "d", "page": "../dye/spec.md"}},
                process_steps=[
                    {
                        "id": "s",
                        "process": {"title": "p", "page": None},
                        "operator": "mixing",
                        "operands": ["d"],
                        "produces": {"id": "c1", "title": "c", "page": None},
                    }
                ],
            ),
        ],
    )
    assert not res.findings
    assert ("no-provider", "chromophore") in codes(res.gaps)
    assert res.counts["no_provider_anywhere_in_composites"] == 1


def test_an_optional_requirement_that_is_not_discharged_is_not_a_finding(tmp_path):
    cls = mod("repressor-detector", requires=[{"id": "transcribe", "why": "x", "optional": True}])
    res = walk(tmp_path, modules=[cls, MEMBER, CYTOSOL, composite("apart", "packing")])
    assert not res.findings


def test_a_composite_with_a_requirer_and_no_provider_at_all_is_a_finding_when_one_exists_elsewhere(tmp_path):
    alone = mod(
        "alone",
        inputs={"det": {"title": "d", "page": "../detector-x/spec.md"}},
        process_steps=[
            {
                "id": "s",
                "process": {"title": "p", "page": None},
                "operator": "mixing",
                "operands": ["det"],
                "produces": {"id": "alone", "title": "a", "page": None},
            }
        ],
    )
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, alone])
    assert [(i.code, i.where) for i in res.findings] == [("undischarged", "alone")]


def test_a_provider_of_the_wrong_route_does_not_discharge(tmp_path):
    """`requires transcribe[pT7]` is not met by `transcribe[sigma70]`, in one compartment or not."""
    cls = mod("promoter-detector", requires=[{"id": "transcribe[pT7]", "why": "x"}])
    mem = mod("detector-x", refines="promoter-detector")
    s30 = mod("cytosol-t7", provides=[{"id": "transcribe[sigma70]", "why": "host polymerase"}])
    res = walk(tmp_path, modules=[cls, mem, s30, composite("c", "mixing")])
    assert not res.findings  # nothing could meet it, so no finding
    assert ("no-provider", "promoter-detector") in codes(res.gaps)


# --------------------------------------------------------------------------- #
# R4: the numeric kinds, and what the sources can reach
# --------------------------------------------------------------------------- #


def test_an_interval_is_contained_in_a_band_closed_and_across_units():
    band = {"low": 480, "high": 520, "unit": "nm"}
    assert cr.dispatch("interval", band, {"low": 485, "high": 495, "unit": "nm"}).status == cr.MET
    assert cr.dispatch("interval", band, {"low": 480, "high": 520, "unit": "nm"}).status == cr.MET  # closed
    assert cr.dispatch("interval", band, {"low": 470, "high": 495, "unit": "nm"}).status == cr.UNMET
    assert (
        cr.dispatch(
            "interval", {"low": 0.48, "high": 0.52, "unit": "µm"}, {"low": 485, "high": 495, "unit": "nm"}
        ).status
        == cr.MET
    )


def test_an_interval_with_a_bad_bound_or_unit_is_undetermined():
    ok = {"low": 480, "high": 520, "unit": "nm"}
    assert cr.dispatch("interval", ok, {"low": 500, "high": 490, "unit": "nm"}).status == cr.UNDETERMINED
    assert cr.dispatch("interval", ok, {"low": 485, "high": 495, "unit": "furlong"}).status == cr.UNDETERMINED
    assert cr.dispatch("interval", ok, {"low": 485, "unit": "nm"}).status == cr.UNDETERMINED


BOUND = {"setpoint": 125, "value": 25, "unit": "mOsm/kg"}


def reading(v, unit="mOsm/kg"):
    return {"value": v, "unit": unit}


def test_within_compares_two_readings_to_a_setpoint_and_a_tolerance():
    assert cr.dispatch("within", BOUND, reading(1060), reading(935)).status == cr.MET  # gap 125
    assert cr.dispatch("within", BOUND, reading(1060), reading(910)).status == cr.MET  # gap 150, on the edge
    assert cr.dispatch("within", BOUND, reading(1060), reading(900)).status == cr.UNMET  # gap 160
    assert cr.dispatch("within", BOUND, reading(1060), reading(1060)).status == cr.UNMET  # matched, setpoint is 125


def test_within_never_passes_what_it_cannot_compute():
    assert (
        cr.dispatch("within", {"value": 25, "unit": "mOsm/kg"}, reading(1060), reading(935)).status == cr.UNDETERMINED
    )
    assert (
        cr.dispatch("within", {"setpoint": 125, "unit": "mOsm/kg"}, reading(1060), reading(935)).status
        == cr.UNDETERMINED
    )
    # mOsm/L and mOsm/kg are different quantities, and units are compared literally.
    assert cr.dispatch("within", BOUND, reading(1060, "mOsm/L"), reading(935)).status == cr.UNDETERMINED


def test_within_without_the_lumen_named_holds_only_if_both_orientations_agree():
    assert (
        cr.dispatch("within-unoriented", BOUND, reading(1060), reading(935)).status == cr.UNDETERMINED
    )  # one way only
    assert cr.dispatch("within-unoriented", BOUND, reading(1000), reading(1000)).status == cr.UNMET  # gap 0 either way
    assert (
        cr.dispatch(
            "within-unoriented", {"setpoint": 0, "value": 10, "unit": "mOsm/kg"}, reading(920), reading(925)
        ).status
        == cr.MET
    )


def test_an_unknown_kind_is_refused_and_not_guessed():
    with pytest.raises(ValueError):
        cr.dispatch("vibes", 1, 2)


def test_a_requirement_interval_resolves_to_a_band_for_each_member_that_states_its_peak(tmp_path):
    ask = {"ex": {"peak": "excitation_peak", "bandwidth": 20, "unit": "nm"}}
    res = walk(
        tmp_path,
        modules=[
            mod("fluorophore", requires=[{"id": "observe_fluorescence", "why": "x", "parameters": ask}]),
            mod("dye-a", refines="fluorophore", parameters={"excitation_peak": 488}),
            mod("dye-b", refines="fluorophore"),
        ],
    )
    assert res.counts["intervals_asked"] == 1 and res.counts["intervals_resolved"] == 1
    assert ("peak-not-stated", "dye-b") in codes(res.gaps)
    assert not res.findings


def test_a_malformed_requirement_interval_is_a_finding(tmp_path):
    bad = {"ex": {"low": 600, "high": 400, "unit": "nm"}, "em": {"peak": "p", "bandwidth": 0, "unit": "nm"}}
    res = walk(tmp_path, modules=[mod("m", requires=[{"id": "observe_fluorescence", "why": "x", "parameters": bad}])])
    assert [i.code for i in res.findings] == ["malformed-interval", "malformed-interval"]


def test_the_report_says_what_the_numeric_kinds_cannot_reach(tmp_path):
    sens = [
        {
            "id": "osmotic-balance",
            "to": "osmotic-shift",
            "basis": "observation",
            "why": "x",
            "bound": {"quantity": "osmolality", "sense": "within", "unit": "mOsm/kg", "setpoint": 125, "value": 25},
        }
    ]
    res = walk(tmp_path, modules=[mod("cell", sensitivities=sens)])
    assert ("within-no-readings", "cell") in codes(res.gaps)
    text = cr.render(res)
    assert "provider bands to compare them with: 0" in text


# --------------------------------------------------------------------------- #
# R5: a child must not contradict its parent
# --------------------------------------------------------------------------- #


def scenario_denial_fires_and_silence_does_not(module, tmp_path):
    """The five-row case, as processes. One row denies. Two are silent. One restates. One is the parent.

    This mirrors `Container` and its children: explicit, silent, silent, DENIES. The check
    must fire on the denial and on nothing else, and it must tell `False` from absence.
    """
    res = module.walk(
        module.Corpus.load(
            tree(
                tmp_path,
                processes=[
                    proc("parent", keeps_boundary=True),
                    proc("restates", refines="parent", keeps_boundary=True),
                    proc("silent", refines="parent"),
                    proc("grandchild-silent", refines="silent"),
                    proc("explicit-null", refines="parent", keeps_boundary=None),
                    proc("denies", refines="parent", keeps_boundary=False),
                ],
            )
        )
    )
    assert [(i.code, i.where) for i in res.findings] == [("contradiction", "denies")]


def test_a_denial_is_a_contradiction_and_a_silence_is_not(tmp_path):
    scenario_denial_fires_and_silence_does_not(cr, tmp_path)


def test_mutant_that_reads_silence_as_denial_is_caught(tmp_path, monkeypatch):
    """The wrong fix would be to require a child to restate. It would fire on two correct rows."""
    real = cr._r5

    def fires_on_silence(corpus, res):
        for s in corpus.of("process"):
            for parent_slug in corpus.parents("process", s.slug)[0]:
                parent = corpus.get("process", parent_slug)
                if "keeps_boundary" in parent.doc and s.doc.get("keeps_boundary") != parent.doc["keeps_boundary"]:
                    res.add("R5", "finding", "contradiction", s.slug, "mutant")
        real(corpus, cr.Result())

    monkeypatch.setattr(cr, "_r5", fires_on_silence)
    with pytest.raises(AssertionError):
        scenario_denial_fires_and_silence_does_not(cr, tmp_path)


@pytest.mark.parametrize(
    "key,parent,child",
    [
        ("operator", "mixing", "packing"),
        ("conserves", True, False),
        ("conserves", False, True),
        ("keeps_boundary", False, True),
    ],
)
def test_a_stated_value_that_differs_from_the_parents_is_a_contradiction(tmp_path, key, parent, child):
    res = walk(tmp_path, processes=[proc("p", **{key: parent}), proc("c", refines="p", **{key: child})])
    assert [(i.code, i.where) for i in res.findings] == [("contradiction", "c")]


def test_a_child_that_narrows_the_parents_codomain_is_fine_and_one_that_leaves_it_is_not(tmp_path):
    def sig(t):
        return {"takes": [{"type": "Component"}], "produces": {"type": t}}

    res = walk(
        tmp_path,
        processes=[
            proc("parent", signature=sig("Solution")),
            proc("narrower", refines="parent", signature=sig("Cytosol")),
            proc("same", refines="parent", signature=sig("Solution")),
            proc("outside", refines="parent", signature=sig("Gel")),
            proc("unknown", refines="parent", signature=sig("Mystery")),
        ],
    )
    assert [(i.code, i.where) for i in res.findings] == [("contradiction", "outside")]
    assert ("type-undetermined", "unknown") in codes(res.gaps)


def test_an_empty_list_is_not_a_denial_because_the_schema_does_not_call_it_a_claim(tmp_path):
    res = walk(
        tmp_path,
        modules=[
            mod("cls", provides=[{"id": "translate", "why": "x"}]),
            mod("member", refines="cls", provides=[]),
        ],
    )
    assert not res.findings and ("empty-list", "member") in codes(res.gaps)


# --------------------------------------------------------------------------- #
# The command line, the report, and the ruling that it only reports
# --------------------------------------------------------------------------- #


def corpus_with_a_finding(tmp_path):
    return tree(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, composite("apart", "packing")])


def test_the_default_is_report_only_even_when_there_is_a_finding(tmp_path, capsys):
    """Jon's ruling, 2026-10-12. No workflow runs this, and a failing walker would turn PRs red."""
    root = corpus_with_a_finding(tmp_path)
    assert cr.main(["--root", str(root)]) == 0
    assert "findings=1" in capsys.readouterr().out


def test_strict_exits_one_on_a_finding_and_zero_on_none(tmp_path, capsys):
    root = corpus_with_a_finding(tmp_path / "bad")
    assert cr.main(["--root", str(root), "--strict"]) == 1
    capsys.readouterr()
    clean = tree(tmp_path / "good", modules=[CLASS, MEMBER, CYTOSOL, composite("together", "mixing")])
    assert cr.main(["--root", str(clean), "--strict"]) == 0


def test_a_walk_over_no_module_source_is_an_error_and_not_a_clean_run(tmp_path, capsys):
    (tmp_path / "docs" / "modules").mkdir(parents=True)
    assert cr.main(["--root", str(tmp_path)]) == 2
    assert "not a clean run" in capsys.readouterr().err


def test_the_report_prints_what_it_read_and_every_section(tmp_path, capsys):
    cr.main(["--root", str(corpus_with_a_finding(tmp_path))])
    out = capsys.readouterr().out
    assert "3 module sources" in out or "4 module sources" in out
    assert "type-order.yml" in out
    for title in cr.TITLES.values():
        assert title in out


def test_a_missing_order_file_is_named_and_degrades_to_comparing_a_type_only_to_itself(tmp_path):
    corpus = cr.Corpus.load(tree(tmp_path, modules=[mod("m")], order=None))
    assert "absent" in corpus.order_note


def test_json_is_valid_and_carries_the_counts(tmp_path, capsys):
    cr.main(["--root", str(corpus_with_a_finding(tmp_path)), "--json"])
    data = json.loads(capsys.readouterr().out)
    assert data["counts"]["requires"] == 1 and len(data["findings"]) == 1


def test_a_source_that_does_not_parse_is_a_finding_and_does_not_stop_the_walk(tmp_path):
    root = tree(tmp_path, modules=[mod("ok")])
    bad = root / "docs" / "modules" / "bad"
    bad.mkdir()
    (bad / "spec.yml").write_text("a: [unclosed\n")
    res = cr.walk(cr.Corpus.load(root))
    assert [(i.code, i.rule) for i in res.findings] == [("unreadable", "read")]
    assert res.counts["modules"] == 1


def test_helpers():
    assert cr.page_slug("../base-cytosol/spec.md") == "base-cytosol"
    assert cr.page_slug("../../modules/x/spec.md") == "x"
    assert cr.page_slug(None) is None
    assert cr.norm("Detector-Repressor") == "detectorrepressor"
    assert cr.words("linearDNA") == cr.words("DNA[linear]")


# --------------------------------------------------------------------------- #
# Found by an independent review. Each one was reproduced before it was fixed.
# --------------------------------------------------------------------------- #


def step(sid, operator, operands, product, **kw):
    out = {
        "id": sid,
        "process": {"title": "p", "page": None},
        "operator": operator,
        "operands": operands,
        "produces": {"id": product, "title": product, "page": None},
    }
    out.update(kw)
    return out


def test_an_undetermined_provider_is_not_read_as_no_provider(tmp_path):
    """A list of types is undetermined. Dropping it said `no provider`, which is a different claim."""
    res = walk(
        tmp_path,
        modules=[
            mod("rq", requires=[{"id": "degrade[RNA]", "why": "x"}]),
            mod("lst", provides=[{"id": "degrade[DNA,RNA]", "why": "x"}]),
        ],
    )
    assert ("provider-undetermined", "rq") in codes(res.gaps)
    assert not any(i.code == "no-provider" for i in res.gaps)
    assert res.counts["providers_nobody_requires"] == 0  # a provider that might meet it is not idle


def test_a_composite_that_lacks_a_provider_that_might_exist_elsewhere_is_a_finding_and_not_a_corpus_gap(tmp_path):
    """`lst` may meet the requirement. It is not in this composite, so this composite cannot discharge it."""
    alone = mod(
        "alone",
        inputs={"req": {"title": "r", "page": "../req/spec.md"}},
        process_steps=[step("s", "mixing", ["req"], "alone")],
    )
    res = walk(
        tmp_path,
        modules=[
            mod("rq", requires=[{"id": "degrade[RNA]", "why": "x"}]),
            mod("req", refines="rq"),
            mod("lst", provides=[{"id": "degrade[DNA,RNA]", "why": "x"}]),
            alone,
        ],
    )
    assert [(i.code, i.where) for i in res.findings] == [("undischarged", "alone")]
    assert res.counts["no_provider_anywhere_in_composites"] == 0


def test_a_bare_provider_against_a_bracketed_requirement_is_also_undetermined_and_not_absent(tmp_path):
    res = walk(
        tmp_path,
        modules=[
            mod("rq", requires=[{"id": "degrade[RNA]", "why": "x"}]),
            mod("bare", provides=[{"id": "degrade", "why": "x"}]),
        ],
    )
    assert ("provider-undetermined", "rq") in codes(res.gaps) and not any(i.code == "no-provider" for i in res.gaps)


def test_an_undetermined_provider_in_the_requirers_compartment_blocks_a_finding_about_another_one(tmp_path):
    """`lst` may meet it and shares the compartment. `ex` meets it and is packed apart. Not a finding."""
    inputs = {n: {"title": n, "page": f"../{n}/spec.md"} for n in ("req", "lst", "ex")}
    res = walk(
        tmp_path,
        modules=[
            mod("rq", requires=[{"id": "degrade[RNA]", "why": "x"}]),
            mod("req", refines="rq"),
            mod("lst", provides=[{"id": "degrade[DNA,RNA]", "why": "x"}]),
            mod("ex", provides=[{"id": "degrade[RNA]", "why": "x"}]),
            mod(
                "x",
                inputs=inputs,
                process_steps=[step("s1", "mixing", ["req", "lst"], "p"), step("s2", "packing", ["p", "ex"], "x")],
            ),
        ],
    )
    assert not res.findings
    assert ("discharge-undetermined", "x") in codes(res.gaps)


def test_an_optional_requirer_that_is_not_discharged_is_a_gap_and_a_discharged_one_is_still_discharged(tmp_path):
    apart = composite("apart", "packing")
    apart["inputs"]["det"]["optional"] = True
    together = composite("together", "mixing")
    together["inputs"]["det"]["optional"] = True
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, apart, together])
    assert not res.findings
    assert ("requirer-optional", "apart") in codes(res.gaps)
    assert any("together: detector-x requires `transcribe`: DISCHARGED" in line for line in res.sections["R3"])


def test_a_denial_is_found_through_a_silent_middle_and_not_only_at_the_direct_parent(tmp_path):
    res = walk(
        tmp_path,
        processes=[
            proc("top", operator="mixing"),
            proc("middle", refines="top"),
            proc("bottom", refines="middle", operator="packing"),
            proc("bottom-ok", refines="middle", operator="mixing"),
        ],
    )
    assert [(i.code, i.where) for i in res.findings] == [("contradiction", "bottom")]


def test_a_child_with_two_parents_is_held_to_each_line_that_states_the_key(tmp_path):
    res = walk(
        tmp_path,
        processes=[
            proc("top", operator="mixing"),
            proc("mid", refines="top"),
            proc("side", operator="packing"),
            proc("child", refines=["mid", "side"], operator="mixing"),
        ],
    )
    found = [(i.code, i.where, "`side`" in i.text) for i in res.findings]
    assert found == [("contradiction", "child", True)]


def test_a_type_is_its_own_refinement_even_with_no_node():
    assert cr.dispatch("type", "Foo", "Foo", cr.Order()).status == cr.MET
    assert cr.dispatch("type", "Foo", "Bar", cr.Order()).status == cr.UNDETERMINED


def test_two_processes_that_produce_the_same_type_with_no_node_agree(tmp_path):
    def sig(t):
        return {"takes": [{"type": "Component"}], "produces": {"type": t}}

    res = walk(
        tmp_path,
        processes=[
            proc("parent", signature=sig("Observation")),
            proc("same", refines="parent", signature=sig("Observation")),
            proc("other", refines="parent", signature=sig("Reading")),
        ],
    )
    assert not res.findings
    assert own_gaps(res) == [("type-undetermined", "other")]


def test_length_units_are_read_by_name_and_both_micro_signs_are_one_unit():
    assert cr.length_factor("\u03bcm") == cr.length_factor("\u00b5m") == cr.length_factor("um") == 1e-6
    assert cr.length_factor("Angstrom") == 1e-10 and cr.length_factor("cm") == 1e-2
    assert cr.length_factor("furlong") is None and cr.length_factor(5) is None
    assert (
        cr.dispatch("interval", {"low": 0.5, "high": 2, "unit": "cm"}, {"low": 6, "high": 18, "unit": "mm"}).status
        == cr.MET
    )


def test_an_unknown_unit_is_a_gap_and_a_structural_error_is_still_a_finding(tmp_path):
    ask = lambda spec: [{"id": "observe", "why": "x", "parameters": {"ex": spec}}]
    odd = walk(tmp_path / "a", modules=[mod("m", requires=ask({"low": 1, "high": 2, "unit": "furlong"}))])
    assert ("unit-unknown", "m") in codes(odd.gaps) and not odd.findings
    for n, spec in enumerate(
        [{"low": 2, "high": 1, "unit": "nm"}, {"low": 1, "high": 2}, {"peak": "p", "bandwidth": -1, "unit": "nm"}]
    ):
        bad = walk(tmp_path / f"b{n}", modules=[mod("m", requires=ask(spec))])
        assert [i.code for i in bad.findings] == ["malformed-interval"], spec


def test_a_step_value_wins_over_the_modules_own_for_a_peak():
    doc = {"parameters": {"excitation_peak": 500}, "process_steps": [{"parameters": {"excitation_peak": "488 nm"}}]}
    assert cr._band(doc, "excitation_peak") == 488.0
    assert cr._band({"parameters": {"p": 5}}, "p") == 5.0 and cr._band({}, "p") is None


def test_a_product_that_reuses_an_input_id_is_noted_and_the_requirement_is_not_lost(tmp_path):
    res = walk(
        tmp_path,
        modules=[
            CLASS,
            MEMBER,
            CYTOSOL,
            mod(
                "x",
                inputs={"det": {"title": "d", "page": "../detector-x/spec.md"}},
                process_steps=[step("s", "mixing", ["det"], "det")],
            ),
        ],
    )
    assert ("compartment-unknown", "x") in codes(res.gaps)
    assert res.counts["requirements_in_composites"] == 1


def test_two_inputs_that_name_one_page_are_told_apart_in_the_report(tmp_path):
    comp = composite("twice", "packing")
    comp["inputs"]["det2"] = {"title": "second", "page": "../detector-x/spec.md"}
    comp["process_steps"][0]["operands"] = ["det", "det2", "cyt"]
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, comp])
    texts = {i.text.split(" requires")[0] for i in res.findings}
    assert texts == {"detector-x (`det`)", "detector-x (`det2`)"}
    # And it stays quiet when the slug alone is enough.
    one = walk(tmp_path / "one", modules=[CLASS, MEMBER, CYTOSOL, composite("once", "packing")])
    assert [i.text.split(" requires")[0] for i in one.findings] == ["detector-x"]


def test_stitching_joins_operands_as_mixing_does(tmp_path):
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, composite("stitched", "stitching")])
    assert any("stitched: detector-x requires `transcribe`: DISCHARGED" in line for line in res.sections["R3"])


def test_an_id_that_two_steps_use_is_two_portions_and_does_not_join_their_products(tmp_path):
    """`shared` goes into two steps. A model that treated it as one object would put `det` and `cyt` together."""
    inputs = {
        "det": {"title": "d", "page": "../detector-x/spec.md"},
        "cyt": {"title": "c", "page": "../cytosol-t7/spec.md"},
        "shared": {"title": "s", "page": None},
    }
    shared_twice = mod(
        "twice",
        inputs=inputs,
        process_steps=[
            step("s1", "mixing", ["det", "shared"], "a"),
            step("s2", "mixing", ["cyt", "shared"], "b"),
            step("s3", "packing", ["a", "b"], "twice"),
        ],
    )
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, shared_twice])
    assert [(i.code, i.where) for i in res.findings] == [("provider-in-another-compartment", "twice")]
    assert not any(i.code == "compartment-unknown" for i in res.gaps)


def test_the_first_use_of_an_id_is_the_one_the_report_asks_about(tmp_path):
    inputs = {
        "det": {"title": "d", "page": "../detector-x/spec.md"},
        "cyt": {"title": "c", "page": "../cytosol-t7/spec.md"},
        "other": {"title": "o", "page": None},
    }
    first = mod(
        "first",
        inputs=inputs,
        process_steps=[step("s1", "mixing", ["det", "cyt"], "p"), step("s2", "packing", ["det", "other"], "first")],
    )
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, first])
    assert any("first: detector-x requires `transcribe`: DISCHARGED" in line for line in res.sections["R3"])
    assert not res.findings and not any(i.code == "compartment-unknown" for i in res.gaps)


def test_two_vesicle_preparations_that_draw_on_the_same_stocks_are_not_already_together(tmp_path):
    """The shape of luxr-lacz-cascade: two encapsulations take the same membrane and outer solution."""
    inputs = {n: {"title": n, "page": None} for n in ("c1", "c2", "mem", "out")}
    two = mod(
        "two",
        inputs=inputs,
        process_steps=[
            step("e1", "packing", ["c1", "mem", "out"], "v1"),
            step("e2", "packing", ["c2", "mem", "out"], "v2"),
            step("embed", "packing", ["v1", "v2"], "two"),
        ],
    )
    res = walk(tmp_path, modules=[two])
    assert not any(i.code == "compartment-unknown" for i in res.gaps)


def test_a_unit_that_is_several_compartments_can_be_used_twice_and_a_repeated_operand_does_not_crash(tmp_path):
    inputs = {n: {"title": n, "page": None} for n in ("cyt", "mem", "a", "b")}
    twice = mod(
        "twice",
        inputs=inputs,
        process_steps=[
            step("e", "packing", ["cyt", "mem"], "ves"),
            step("s1", "packing", ["ves", "a"], "x1"),
            step("s2", "packing", ["ves", "b"], "x2"),
            step("s3", "mixing", ["a", "a"], "x3"),
        ],
    )
    res = walk(tmp_path, modules=[twice])
    assert not res.findings


def test_a_second_use_of_a_mixed_product_is_still_one_compartment(tmp_path):
    """The copy keeps the compartments among its leaves. If it did not, mixing it would look ambiguous."""
    inputs = {n: {"title": n, "page": None} for n in ("a", "b", "c", "d")}
    reused = mod(
        "reused",
        inputs=inputs,
        process_steps=[
            step("s1", "mixing", ["a", "b"], "p"),
            step("s2", "packing", ["p", "c"], "x1"),
            step("s3", "mixing", ["p", "d"], "x2"),
        ],
    )
    res = walk(tmp_path, modules=[reused])
    assert not any(i.code == "compartment-unknown" for i in res.gaps)


def test_a_copy_of_an_unknown_unit_is_unknown_too(tmp_path):
    """`t` is made ambiguous by step 2. Step 3 takes a second portion of it. That portion is no more certain."""
    inputs = {
        "det": {"title": "d", "page": "../detector-x/spec.md"},
        "t": {"title": "t", "page": None},
        "m1": {"title": "m", "page": None},
        "m2": {"title": "m", "page": None},
    }
    steps = [
        step("s1", "packing", ["m1", "m2"], "pk"),
        step("s2", "mixing", ["t", "pk"], "x"),
        {
            **step("s3", "mixing", ["t", "det"], "prodp"),
            "produces": {"id": "prodp", "title": "p", "page": "../cytosol-t7/spec.md"},
        },
    ]
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, mod("unknown-copy", inputs=inputs, process_steps=steps)])
    assert not any("DISCHARGED" in line for line in res.sections["R3"])
    assert ("discharge-undetermined", "unknown-copy") in codes(res.gaps)


BAD_SHAPES = [
    {"process_steps": {"x": 1}},
    {"process_steps": ["x"]},
    {"inputs": ["x"], "process_steps": [{"id": "s", "operator": "mixing", "operands": ["x"], "produces": {"id": "y"}}]},
    {"requires": [{"id": "observe", "why": "x", "parameters": [1]}]},
    {"sensitivities": ["x"]},
    {"sensitivities": [{"id": "s", "bound": "x"}]},
    {
        "inputs": {"x": {"title": "x", "page": None}, "y": {"title": "y", "page": None}},
        "process_steps": [
            step("s", "mixing", ["x", "y"], "z", operator_pairs=[{"operands": [["x"], "y"], "operator": "packing"}])
        ],
    },
    {"inputs": {"x": "not a mapping"}, "process_steps": [step("s", "mixing", ["x"], "z", produces="p")]},
]


@pytest.mark.parametrize("bad", BAD_SHAPES)
def test_a_malformed_source_does_not_stop_the_report(tmp_path, bad):
    """One bad file must not hide what the rest says. A crash is a finding, and silence never is."""
    res = walk(tmp_path, modules=[mod("bad", **bad), CLASS, MEMBER, CYTOSOL, composite("good", "mixing")])
    assert any("good: detector-x requires `transcribe`: DISCHARGED" in line for line in res.sections["R3"])


@pytest.mark.parametrize(
    "order",
    [
        {"orders": [1]},
        {"orders": {}, "module_slugs": [1]},
        {"orders": {"type_refinement": {"edges": {"A": "Bee"}, "nodes": "A"}}},
        [1, 2],
        "text",
    ],
)
def test_an_order_of_the_wrong_shape_does_not_stop_the_report(tmp_path, order):
    res = walk(tmp_path, modules=[mod("m")], order=order)
    assert res.counts["modules"] == 1


def test_an_order_file_that_does_not_parse_is_a_finding_and_the_walk_goes_on(tmp_path):
    root = tree(tmp_path, modules=[mod("m")], order=None)
    (root / "docs" / "type-order.yml").write_text("a: [unclosed\n")
    res = cr.walk(cr.Corpus.load(root))
    assert [(i.code, i.where) for i in res.findings] == [("unreadable", "type-order.yml")]


def test_guard_turns_a_crash_into_a_finding():
    res = cr.Result()
    with cr.guard(res, "R9", "somewhere"):
        raise RuntimeError("boom")
    assert [(i.kind, i.code, i.where) for i in res.items] == [("finding", "walk-error", "somewhere")]
    assert "RuntimeError: boom" in res.items[0].text


def test_a_declaration_that_is_not_a_list_of_mappings_with_string_ids_is_a_finding_and_not_ignored(tmp_path):
    res = walk(
        tmp_path,
        modules=[
            mod("a", requires="observe"),
            mod("b", requires=[{"id": 5, "why": "x"}]),
            mod("c", provides=["translate"]),
            mod("d", provides=[{"why": "no id"}]),
        ],
    )
    assert sorted((i.code, i.where) for i in res.findings) == [
        ("malformed-entry", "a"),
        ("malformed-entry", "c"),
        ("malformed-id", "b"),
        ("malformed-id", "d"),
    ]
    assert res.counts["requires"] == 0 and res.counts["provides"] == 0


# --------------------------------------------------------------------------- #
# The published order's two newer sections: bracket_aliases and type_declares
# --------------------------------------------------------------------------- #

# The shape the published order has now: the node is spelled `DNA[linear]`, and an operation id
# cannot nest a bracket, so a map says that `linearDNA` means it.
PUBLISHED_EDGES = {
    "DNA[linear]": ["DNA"],
    "DNA": ["NucleicAcid"],
    "RNA": ["NucleicAcid"],
    "NucleicAcid": ["Component"],
}


def test_the_schemas_six_examples_all_agree_on_the_published_spelling_through_the_alias():
    order = cr.Order(PUBLISHED_EDGES, aliases={"linearDNA": "DNA[linear]"})
    got = lambda p, r: cr.dispatch("operation", p, r, order).status == cr.MET
    assert disagreements(got) == []


def test_without_the_alias_the_fifth_example_is_unmet_and_the_hint_points_at_the_node():
    order = cr.Order(PUBLISHED_EDGES)
    got = lambda p, r: cr.dispatch("operation", p, r, order).status == cr.MET
    assert disagreements(got) == [("degrade[DNA]", "degrade[linearDNA]", True)]
    assert "DNA[linear]" in cr.dispatch("operation", "degrade[DNA]", "degrade[linearDNA]", order).hint


def test_the_verdict_says_when_an_alias_decided_it():
    order = cr.Order(PUBLISHED_EDGES, aliases={"linearDNA": "DNA[linear]"})
    v = cr.dispatch("operation", "degrade[DNA]", "degrade[linearDNA]", order)
    assert "linearDNA is DNA[linear] by alias" in v.why


def test_an_alias_to_something_that_is_not_a_node_is_ignored_and_never_shadows_a_node():
    order = cr.Order(PUBLISHED_EDGES, aliases={"linearDNA": "NotANode", "RNA": "DNA"})
    assert order.resolve_type("linearDNA") is None
    assert order.resolve_type("RNA") == "RNA"  # an exact node wins over an alias with its name
    assert cr.Order(PUBLISHED_EDGES, aliases=["not", "a", "map"]).aliases == {}


# The five rows, as types. Container declares `hold`. Gel says so. Membrane and Cytosol say nothing
# about it and inherit. Solution says it declares nothing, which is a claim, and it is wrong.
DECLARES_EDGES = {
    "Gel": ["Container"],
    "Membrane": ["Container"],
    "Solution": ["Container"],
    "Cytosol": ["Solution"],
    "Vesicle": ["Container"],  # says nothing, so it is absent from the map and inherits
    "Container": ["Component"],
}


def declares(**rows):
    return {k: {"kind": v[0], "names": list(v[1:]), "cell": "x"} for k, v in rows.items()}


def scenario_a_denial_is_found_and_a_silence_is_not(module):
    order = module.Order(
        DECLARES_EDGES,
        declares=declares(
            Container=("declares", "hold"),
            Gel=("declares", "hold"),
            Membrane=("position", "encapsulate"),
            Cytosol=("declares", "transcribe", "translate"),
            Solution=("none",),
        ),
    )
    assert order.denials() == [("Solution", "Container", ("hold",))]


def test_a_type_that_claims_none_below_one_that_declares_is_found_and_silent_children_are_not():
    scenario_a_denial_is_found_and_a_silence_is_not(cr)


def test_mutant_that_reads_a_missing_type_as_none_is_caught(monkeypatch):
    """The wrong fix: treat a type absent from the map as one that declares nothing."""
    real = cr.Order.denials

    def silence_as_none(self):
        both = dict(self.declares)
        for t in self.type_nodes:
            both.setdefault(t, {"kind": "none"})
        saved, self.declares = self.declares, both
        try:
            return real(self)
        finally:
            self.declares = saved

    monkeypatch.setattr(cr.Order, "denials", silence_as_none)
    with pytest.raises(AssertionError):
        scenario_a_denial_is_found_and_a_silence_is_not(cr)


def test_a_denial_is_found_through_a_type_that_says_nothing():
    order = cr.Order({"Mid": ["Top"], "Low": ["Mid"]}, declares=declares(Top=("declares", "hold"), Low=("none",)))
    assert order.denials() == [("Low", "Top", ("hold",))]


def test_none_with_no_declaring_ancestor_and_none_below_none_are_not_denials():
    order = cr.Order({"A": ["B"], "B": ["C"]}, declares=declares(A=("none",), B=("none",), C=("position", "x")))
    assert order.denials() == []


def test_a_type_is_held_to_the_nearest_declaring_ancestor_on_each_line():
    order = cr.Order(
        {"Child": ["Left", "Right"], "Left": ["Top"], "Right": ["Top"]},
        declares=declares(Top=("declares", "a"), Left=("declares", "b"), Child=("none",)),
    )
    assert order.denials() == [("Child", "Left", ("b",)), ("Child", "Top", ("a",))]


def test_the_published_file_is_read_end_to_end_for_aliases_and_declarations(tmp_path):
    published = {
        "orders": {
            "type_refinement": {"edges": DECLARES_EDGES, "nodes": sorted({*DECLARES_EDGES, "Component"})},
            "process_refinement": {"edges": {}},
        },
        "bracket_aliases": {"linearDNA": "DNA[linear]"},
        "type_declares": declares(Container=("declares", "hold"), Solution=("none",), Gel=("declares", "hold")),
    }
    res = walk(tmp_path, modules=[mod("m")], order=published)
    assert [(i.code, i.where) for i in res.findings] == [("type-denies-ancestor", "Solution")]
    assert res.counts["type_declarations"] == 3 and res.counts["types_claiming_none"] == 1
    assert "1 bracket aliases, 3 type declarations" in cr.render(res)


def test_an_order_with_no_type_declares_says_so_and_finds_nothing(tmp_path):
    res = walk(tmp_path, modules=[mod("m")])
    assert ("type-declares-absent", "type-order.yml") in codes(res.gaps) and not res.findings


def test_a_kind_this_walker_does_not_know_is_a_gap_and_not_a_guess(tmp_path):
    published = {
        "orders": {"type_refinement": {"edges": {"A": ["B"]}}, "process_refinement": {"edges": {}}},
        "type_declares": {"A": {"kind": "wishes", "names": []}, "B": {"kind": "declares", "names": ["x"]}},
    }
    res = walk(tmp_path, modules=[mod("m")], order=published)
    assert ("declares-kind-unknown", "A") in codes(res.gaps) and not res.findings


# --------------------------------------------------------------------------- #
# Narrowing the compartment claim, and naming what is missing
# --------------------------------------------------------------------------- #

PURIFY_ORDER = {
    "orders": {
        "type_refinement": {"edges": TYPE_EDGES},
        "process_refinement": {"edges": {**PROC_EDGES, "purify": ["prepare"], "passive_transport": ["transport"]}},
    },
    "module_slugs": {},
}


def test_a_step_whose_process_refines_purify_is_outside_the_compartment_model(tmp_path):
    """No operator separates anything, but `purify` does. The model must say so and not assume monotonic."""
    cleaned = composite("cleaned", "mixing")
    cleaned["process_steps"][0]["process"] = {"title": "p", "page": None, "abstract": "purify"}
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, cleaned, composite("plain", "mixing")], order=PURIFY_ORDER)
    lines = res.sections["R3"]
    assert any(l.startswith("plain: detector-x requires `transcribe`: DISCHARGED") for l in lines)
    assert not any(l.startswith("cleaned:") and "DISCHARGED" in l for l in lines)
    assert ("compartment-unknown", "cleaned") in codes(res.gaps)
    assert (
        "refines `purify`" in [i.text for i in res.gaps if i.where == "cleaned" and i.code == "compartment-unknown"][0]
    )
    assert res.counts["steps_purify"] == 1 and res.counts["outside_model_steps"] == 1 and not res.findings


def test_a_step_is_separating_through_its_process_page_and_that_sources_refines(tmp_path):
    """The step names a process page. That process source refines `purify`, which has no source of its own."""
    cleaned = composite("cleaned", "mixing")
    cleaned["process_steps"][0]["process"] = {"title": "p", "page": "../../processes/clean-up/main.md"}
    res = walk(
        tmp_path,
        modules=[CLASS, MEMBER, CYTOSOL, cleaned],
        processes=[proc("clean-up", refines="purify")],
        order=PURIFY_ORDER,
    )
    assert res.counts["steps_purify"] == 1


def test_an_ordinary_process_is_not_separating(tmp_path):
    other = composite("other", "mixing")
    other["process_steps"][0]["process"] = {"title": "p", "page": None, "abstract": "encapsulate"}
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, other], order=PURIFY_ORDER)
    assert res.counts["outside_model_steps"] == 0


def test_the_report_says_which_named_branches_have_no_source_to_test_them(tmp_path):
    none = walk(tmp_path / "a", modules=[CLASS, MEMBER, CYTOSOL, composite("c", "mixing")])
    assert none.counts["stitching_steps"] == 0
    line = [l for l in none.sections["R3"] if l.startswith("branches the model names")][0]
    assert "No source uses `stitching`, `purify`, `transport`" in line and "bounded by the corpus" in line
    some = walk(tmp_path / "b", modules=[CLASS, MEMBER, CYTOSOL, composite("c", "stitching")])
    line = [l for l in some.sections["R3"] if l.startswith("branches the model names")][0]
    assert some.counts["stitching_steps"] == 1 and "stitching 1" in line
    assert "No source uses `purify`, `transport`" in line and "`stitching`," not in line


def outside_composite(slug, abstract):
    comp = composite(slug, "mixing")
    comp["process_steps"][0]["process"] = {"title": "p", "page": None, "abstract": abstract}
    return comp


def test_transport_is_outside_the_model_too_and_so_is_a_refinement_of_it(tmp_path):
    """Cargo crosses a boundary that persists. That is neither a join nor a separation."""
    res = walk(
        tmp_path, modules=[CLASS, MEMBER, CYTOSOL, outside_composite("moved", "passive_transport")], order=PURIFY_ORDER
    )
    assert res.counts["steps_transport"] == 1 and res.counts["steps_purify"] == 0
    note = [i.text for i in res.gaps if i.where == "moved" and i.code == "compartment-unknown"][0]
    assert "refines `transport`" in note and "boundary that persists" in note
    assert not any("DISCHARGED" in l for l in res.sections["R3"])


def test_lyse_is_inside_the_model_because_destroying_a_compartment_is_a_join(tmp_path):
    order = {**PURIFY_ORDER, "orders": {**PURIFY_ORDER["orders"], "process_refinement": {"edges": {"lyse": ["hold"]}}}}
    res = walk(tmp_path, modules=[CLASS, MEMBER, CYTOSOL, outside_composite("burst", "lyse")], order=order)
    assert res.counts["outside_model_steps"] == 0


def test_the_coverage_sentence_goes_when_every_named_branch_has_a_source(tmp_path):
    res = walk(
        tmp_path,
        modules=[
            CLASS,
            MEMBER,
            CYTOSOL,
            composite("s", "stitching"),
            outside_composite("p", "purify"),
            outside_composite("t", "transport"),
        ],
        order=PURIFY_ORDER,
    )
    line = [l for l in res.sections["R3"] if l.startswith("branches the model names")][0]
    assert "stitching 1, purify 1, transport 1" in line and "No source uses" not in line


def test_a_contradicting_pair_names_itself_and_says_why(tmp_path):
    odd = composite(
        "odd",
        "packing",
        operands=("det", "cyt", "other"),
        extra_inputs=("other",),
        pairs=[
            {"operands": ["det", "other"], "operator": "mixing"},
            {"operands": ["cyt", "other"], "operator": "mixing"},
        ],
    )
    res = walk(tmp_path / "a", modules=[CLASS, MEMBER, CYTOSOL, odd])
    note = [i.text for i in res.gaps if i.code == "compartment-unknown"][0]
    assert "keeps `det` and `cyt` apart" in note and "the other pairs of this step" in note


def test_a_missing_observe_provider_names_the_kind_of_source_that_is_missing(tmp_path):
    res = walk(
        tmp_path,
        modules=[
            mod("substrate", requires=[{"id": "observe_absorbance", "why": "x"}]),
            mod("cls", requires=[{"id": "transcribe", "why": "x"}]),
        ],
    )
    texts = {i.where: i.text for i in res.gaps if i.code == "no-provider"}
    assert "An assay provides `observe`" in texts["substrate"]
    assert "assay" not in texts["cls"]


# --------------------------------------------------------------------------- #
# R6: an encapsulation's product states a vesicle size class, and never a diameter
# --------------------------------------------------------------------------- #

VESICLE_ORDER = {
    "orders": {
        "type_refinement": {
            "edges": {
                "Vesicle[GUV]": ["Vesicle"],
                "Vesicle[LUV]": ["Vesicle"],
                "Vesicle[SUV]": ["Vesicle"],
                "Vesicle[liposome]": ["Vesicle"],
                "Cell": ["Vesicle"],
                "Vesicle": ["Component"],
            }
        },
        "process_refinement": {"edges": {"encapsulate": ["hold"], "encapsulate[GUV]": ["encapsulate"]}},
    },
    "module_slugs": {"guv": "Vesicle[GUV]"},
}


def encapsulating(slug, product, abstract="encapsulate", page="../prod/spec.md", **kw):
    inputs = {"a": {"title": "a", "page": None}}
    s = step("make", "packing", ["a"], product or "prod", process={"title": "p", "page": None, "abstract": abstract})
    s["produces"]["page"] = page if product else None
    return mod(slug, inputs=inputs, process_steps=[s], **kw)


def r6(tmp_path, *modules, **kw):
    return walk(tmp_path, modules=list(modules), order=kw.pop("order", VESICLE_ORDER), **kw)


def test_a_product_that_states_a_size_through_its_type_passes_and_is_counted_as_such(tmp_path):
    res = r6(tmp_path, encapsulating("cell", "prod"), mod("prod", type="Vesicle[GUV]"))
    assert not res.findings
    assert (res.counts["size_via_type"], res.counts["size_via_refines"], res.counts["size_missing"]) == (1, 0, 0)


def test_a_product_that_states_a_size_through_a_refines_axis_passes_and_the_report_says_which_route(tmp_path):
    """A Cell's own type carries no size. Its `refines` does, which is how the corpus writes it today."""
    res = r6(
        tmp_path, encapsulating("cell", "prod"), mod("prod", type="Cell", refines=["Vesicle[GUV]", "Vesicle[liposome]"])
    )
    assert not res.findings and (res.counts["size_via_type"], res.counts["size_via_refines"]) == (0, 1)
    assert "through a `refines`: 1" in cr.render(res)


def test_a_size_slug_in_refines_resolves_through_the_published_slug_map(tmp_path):
    res = r6(tmp_path, encapsulating("cell", "prod"), mod("prod", refines=["guv", "liposome"]))
    assert not res.findings and res.counts["size_via_refines"] == 1


def test_a_size_reaches_a_product_through_a_source_it_refines(tmp_path):
    res = r6(
        tmp_path, encapsulating("cell", "prod"), mod("prod", refines="guv-class"), mod("guv-class", type="Vesicle[GUV]")
    )
    assert not res.findings and res.counts["size_missing"] == 0


def test_a_material_is_not_a_size_and_a_product_with_only_a_material_is_a_finding(tmp_path):
    res = r6(tmp_path, encapsulating("cell", "prod"), mod("prod", type="Cell", refines="Vesicle[liposome]"))
    assert [(i.code, i.where) for i in res.findings] == [("encapsulation-no-size", "cell")]
    assert "states no vesicle size class (GUV, LUV, SUV)" in res.findings[0].text


def test_a_product_with_no_page_is_a_gap_and_never_a_finding_because_only_a_page_can_fix_it(tmp_path):
    res = r6(tmp_path, encapsulating("cell", None))
    assert not res.findings and ("size-product-unknown", "cell") in codes(res.gaps)
    assert res.counts["size_product_unknown"] == 1


def test_an_abstract_class_is_open_on_purpose_and_is_skipped(tmp_path):
    """`vesicle` states no size and should not. Another source refines it, so it is a class."""
    res = r6(
        tmp_path, encapsulating("vesicle", "vesicle", page="../vesicle/spec.md"), mod("guv-member", refines="vesicle")
    )
    assert not res.findings and res.counts["size_classes_skipped"] == 1


def test_a_step_that_does_not_encapsulate_is_not_looked_at(tmp_path):
    res = r6(tmp_path, encapsulating("plain", "prod", abstract="assemble-cytosol"), mod("prod", type="Cell"))
    assert res.counts["encapsulations"] == 0 and not res.findings


def test_a_step_whose_process_page_refines_encapsulate_is_an_encapsulation(tmp_path):
    comp = encapsulating("cell", "prod", abstract="not-it")
    comp["process_steps"][0]["process"] = {"title": "p", "page": "../../processes/phase-transfer/main.md"}
    res = r6(tmp_path, comp, mod("prod", type="Cell"), processes=[proc("phase-transfer", refines="encapsulate")])
    assert res.counts["encapsulations"] == 1 and [i.code for i in res.findings] == ["encapsulation-no-size"]


def test_a_refinement_of_encapsulate_by_size_counts(tmp_path):
    res = r6(tmp_path, encapsulating("cell", "prod", abstract="encapsulate[GUV]"), mod("prod", type="Cell"))
    assert res.counts["encapsulations"] == 1


def test_no_diameter_is_asked_for(tmp_path):
    """No diameter is characterized for anything, so asking for one would fire everywhere and fix nothing."""
    res = r6(tmp_path, encapsulating("cell", "prod"), mod("prod", type="Vesicle[LUV]", parameters={}))
    assert not res.findings
    assert "never for a diameter" in cr.render(res)


def test_smoke_over_the_real_repo_reads_files_and_never_fails():
    """Asserts nothing about what the corpus contains, so a content change cannot break it."""
    assert cr.main([]) == 0
