"""Tests for scripts/orders.py, and for the rule it implements.

THESE TESTS CAN FAIL, which is the point of writing them. The five worked
examples under `provides:` in scripts/spec-yml-schema.yml are encoded here
verbatim. Four of them pass against plain string equality on the bracket, which
is what collate-conditions.py has always done; the fifth does not, and it is the
only one of the five that needs the type order at all. A checker that has never
been shown able to fail has not been shown to work.

The order used below is SYNTHETIC and small, so a failure points at the rule
rather than at today's corpus. The live order is exercised separately.
"""
import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import orders as O  # noqa: E402


# The slice of the published type order the schema's own examples need.
ORDERS = {
    "type_refinement": {
        "nodes": ["NucleicAcid", "DNA", "RNA", "linearDNA", "dsDNA", "ssDNA", "pT7",
                  "sigma70"],
        "edges": {
            "DNA": ["NucleicAcid"],
            "RNA": ["NucleicAcid"],
            "linearDNA": ["DNA"],
            "dsDNA": ["DNA"],
            "ssDNA": ["DNA"],
        },
    },
    "process_refinement": {
        "nodes": ["degrade", "transcribe", "anneal"],
        "edges": {"degrade": ["transcribe"]},
    },
}


# --- membership -------------------------------------------------------------

def test_nodes_include_things_with_no_edge():
    """`anneal` refines nothing and is refined by nothing.

    Reading `edges` alone made nine of forty-one Processes invisible on
    2026-10-12, and this session told another session a published Process did
    not exist because of it.
    """
    assert "anneal" in O.process_nodes(ORDERS)


def test_nodes_include_both_ends_of_an_edge():
    assert {"degrade", "transcribe"} <= O.process_nodes(ORDERS)


def test_absent_order_is_empty_not_an_error(tmp_path):
    assert O.load(str(tmp_path)) == {}
    assert O.type_nodes(O.load(str(tmp_path))) == set()


# --- the order ---------------------------------------------------------------

def test_ancestors_are_transitive():
    assert O.ancestors(ORDERS, "type_refinement", "linearDNA") == {"DNA", "NucleicAcid"}


def test_refines_is_reflexive():
    assert O.refines(ORDERS, "type_refinement", "DNA", "DNA")


def test_refines_is_not_symmetric():
    assert O.refines(ORDERS, "type_refinement", "linearDNA", "DNA")
    assert not O.refines(ORDERS, "type_refinement", "DNA", "linearDNA")


def test_unrelated_types_do_not_refine_each_other():
    assert not O.refines(ORDERS, "type_refinement", "RNA", "DNA")


# --- the five worked examples ------------------------------------------------
# scripts/spec-yml-schema.yml, under `provides:`, lines 326-337. Each row is
# (provided, required, expected), with the schema's own reason.

SCHEMA_EXAMPLES = [
    # "repressor-detector needs transcription AVAILABLE in its compartment,
    #  which any route supplies"
    ("transcribe[pT7]", "transcribe", True),
    # "a T7 promoter needs T7 polymerase"
    ("transcribe[sigma70]", "transcribe[pT7]", False),
    # "an exonuclease needs a free end, so the circular plasmid survives"
    ("degrade[linearDNA]", "degrade[DNA]", False),
    # "met by degrade[DNA], which is wider" -- THE ONE STRING EQUALITY GETS WRONG
    ("degrade[DNA]", "degrade[linearDNA]", True),
    # "rna refines nucleic-acid, so RNase covers part of it"
    ("degrade[RNA]", "degrade[NucleicAcid]", False),
]


@pytest.mark.parametrize("provided,required,expected", SCHEMA_EXAMPLES)
def test_schema_worked_examples(provided, required, expected):
    assert O.meets(ORDERS, provided, required) is expected


def test_string_equality_fails_exactly_one_of_the_five():
    """The measurement that justifies this module, kept as a test.

    If this ever reports a number other than 1, either the schema gained an
    example or the rule changed, and the comment in orders.meets() is stale.
    """
    def string_equality(provided, required):
        pop, pr = O.operation(provided)
        rop, rr = O.operation(required)
        return pop == rop and (rr is None or pr == rr)

    disagreements = [
        (p, r) for p, r, want in SCHEMA_EXAMPLES if string_equality(p, r) is not want
    ]
    assert disagreements == [("degrade[DNA]", "degrade[linearDNA]")]


def test_a_bare_requirement_is_not_the_top_type():
    """`requires: degrade` takes anything; `requires: degrade[NucleicAcid]` does not."""
    assert O.meets(ORDERS, "degrade[RNA]", "degrade")
    assert not O.meets(ORDERS, "degrade[RNA]", "degrade[NucleicAcid]")


def test_a_bare_provider_meets_only_a_bare_requirement():
    """A provider that names no type has not said it covers a narrowed one."""
    assert O.meets(ORDERS, "degrade", "degrade")
    assert not O.meets(ORDERS, "degrade", "degrade[DNA]")


def test_different_operations_never_meet():
    assert not O.meets(ORDERS, "transcribe[pT7]", "degrade[pT7]")


# --- the flat spelling ------------------------------------------------------
# docs/type-order.yml gained `bracket_aliases` on 2026-10-12, because an operation
# id matches `[A-Za-z0-9]+` and so cannot spell a type named `DNA[linear]`. Three
# sources write `degrade[linearDNA]` and the order publishes `DNA[linear]`.

ALIAS = {"linearDNA": "DNA[linear]"}

BRACKETED = {
    "type_refinement": {
        "nodes": ["NucleicAcid", "DNA", "DNA[linear]", "DNA[circular]"],
        "edges": {"DNA": ["NucleicAcid"], "DNA[linear]": ["DNA"],
                  "DNA[circular]": ["DNA"]},
    },
}


def test_the_fifth_example_fails_without_the_alias():
    """The control. This is the state PR 293 found and the map fixes."""
    assert not O.meets(BRACKETED, "degrade[DNA]", "degrade[linearDNA]")


def test_the_fifth_example_passes_with_the_alias():
    assert O.meets(BRACKETED, "degrade[DNA]", "degrade[linearDNA]", ALIAS)


def test_the_alias_does_not_make_a_narrow_provider_wide():
    """Resolving a spelling must not change the ORDER, only the name."""
    assert not O.meets(BRACKETED, "degrade[linearDNA]", "degrade[DNA]", ALIAS)


def test_an_unaliased_bracketed_type_is_still_unresolved():
    """`DNA[circular]` has no alias because nothing writes one. It stays unmet,
    and that is a finding for the caller rather than something to guess at."""
    assert not O.meets(BRACKETED, "degrade[DNA]", "degrade[circularDNA]", ALIAS)


def test_an_absent_alias_map_is_the_old_behaviour():
    assert not O.meets(BRACKETED, "degrade[DNA]", "degrade[linearDNA]", {})
    assert not O.meets(BRACKETED, "degrade[DNA]", "degrade[linearDNA]", None)
