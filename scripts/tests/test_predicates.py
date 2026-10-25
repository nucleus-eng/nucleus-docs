"""Tests for `predicates:` and `kind: presence`, read by scripts/check-conflicts.py.

THE CONTROL IS A DESIGN THAT FAILS. Jon's requirement for this check, 2026-10-20,
was that "the resolvers we have need to be able to flag when a design fails this
criterion". So every passing design below is paired with the failing one it would
be confused with, and the test asserts the checker tells them apart.

These run the script against a SYNTHETIC docs tree rather than the corpus, so a
failure points at the rule and not at today's sources. `main` carries no
`predicates:` and no `kind: presence` at all, so there is nothing live to exercise.
"""
import subprocess
import sys
import textwrap
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent.parent
SCRIPT = REPO / "scripts" / "check-conflicts.py"


def run(tmp_path, sources):
    """Write a synthetic docs/modules tree and run the checker over it."""
    for slug, body in sources.items():
        d = tmp_path / "docs" / "modules" / slug
        d.mkdir(parents=True)
        (d / "spec.yml").write_text(textwrap.dedent(body))
    (tmp_path / "scripts").mkdir(exist_ok=True)
    for f in ("check-conflicts.py", "orders.py"):
        (tmp_path / "scripts" / f).write_text((REPO / "scripts" / f).read_text())
    (tmp_path / "docs" / "type-order.yml").write_text(
        (REPO / "docs" / "type-order.yml").read_text())
    r = subprocess.run([sys.executable, str(tmp_path / "scripts" / "check-conflicts.py")],
                       capture_output=True, text=True)
    return r.stdout


LOADED = """\
    module: loaded
    type: 'Vesicle[liposome]{Substrate}'
    title: Loaded
    inputs: {}
    process_steps: []
    """
EMPTY = """\
    module: empty
    type: 'Vesicle[liposome]'
    title: Empty
    inputs: {}
    process_steps: []
    """


def reporter(expr, pages):
    ins = "\n".join(f"      {k}:\n        title: {k}\n        page: ../{v}/spec.md"
                    for k, v in pages.items())
    return f"""\
    module: reporter
    type: ColorReporter
    title: Reporter
    inputs:
{ins}
    process_steps: []
    predicates:
      - id: held-apart
        expr: {expr}
        why: The enzyme and its substrate must start in different compartments.
    """


def test_a_design_that_satisfies_the_predicate_is_not_reported(tmp_path):
    out = run(tmp_path, {"loaded": LOADED, "empty": EMPTY,
                         "reporter": reporter("encapsulated(a) OR encapsulated(b)",
                                              {"a": "loaded", "b": "empty"})})
    assert "PREDICATE" not in out
    assert "predicates 1 declared, 0 false" in out


def test_a_design_that_fails_it_is_reported(tmp_path):
    """THE CONTROL. Both operands free, so the colour fires before any signal."""
    out = run(tmp_path, {"empty": EMPTY,
                         "reporter": reporter("encapsulated(a) OR encapsulated(b)",
                                              {"a": "empty", "b": "empty"})})
    assert "PREDICATE reporter" in out
    assert "predicates 1 declared, 1 false" in out


def test_either_operand_alone_satisfies_it(tmp_path):
    """The disjunction's whole point: three arrangements pass, one does not."""
    for pages in ({"a": "loaded", "b": "empty"}, {"a": "empty", "b": "loaded"},
                  {"a": "loaded", "b": "loaded"}):
        d = tmp_path / str(abs(hash(tuple(sorted(pages.items())))))
        out = run(d, {"loaded": LOADED, "empty": EMPTY,
                      "reporter": reporter("encapsulated(a) OR encapsulated(b)", pages)})
        assert "predicates 1 declared, 0 false" in out, pages


def test_an_unresolvable_operand_counts_as_not_encapsulated(tmp_path):
    """Unknown is not satisfied: reporting it is the point."""
    out = run(tmp_path, {"reporter": reporter("encapsulated(a)", {"a": "nosuch"})})
    assert "PREDICATE reporter" in out


def test_a_presence_sensitivity_meets_a_component_that_is_there(tmp_path):
    out = run(tmp_path, {
        "cprg": "module: cprg\ntype: Substrate\ntitle: CPRG\ninputs: {}\nprocess_steps: []\n",
        "enzyme": """\
            module: enzyme
            type: ColorChangeEnzyme
            title: Enzyme
            inputs: {}
            process_steps: []
            sensitivities:
              - id: not-co-located
                to: cprg
                kind: presence
                basis: rule
                why: Free substrate with the enzyme turns the colour over early.
            """,
        "mix": """\
            module: mix
            type: ColorReporter
            title: Mix
            inputs:
              enzyme: {title: E, page: ../enzyme/spec.md}
              cprg: {title: C, page: ../cprg/spec.md}
            process_steps:
              - id: mix
                process: {title: Mix, page: null}
                operator: mixing
                operands: [enzyme, cprg]
                produces: {id: mix, title: Mix, page: null}
            """})
    assert "PRESENCE  mix/mix" in out
    assert "presence 1 declared, 1 met" in out


def test_a_presence_sensitivity_that_meets_nothing_is_not_reported(tmp_path):
    """THE CONTROL. The schema says a sensitivity that meets nothing is not a defect."""
    out = run(tmp_path, {
        "enzyme": """\
            module: enzyme
            type: ColorChangeEnzyme
            title: Enzyme
            inputs: {}
            process_steps: []
            sensitivities:
              - id: not-co-located
                to: cprg
                kind: presence
                basis: rule
                why: Free substrate with the enzyme turns the colour over early.
            """})
    assert "PRESENCE" not in out
    assert "presence 1 declared, 0 met" in out
