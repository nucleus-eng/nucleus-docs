"""Pin each check in scripts/check-step-quantities.py to a case whose answer is known.

Every check passes on the corpus today, so a corpus run alone cannot tell a working
check from one that never fires. Each test plants one error in a small source and
asserts the checker catches it, or plants a case it must not fail on and asserts that
it does not.

Two tests earn the file. A bare `C` and `mol%` both parse in pint without an error,
as coulombs and as moles times percent, so a checker that only asked "does it parse"
would pass both. And 17 of the 23 rows compared on the corpus take their stock from an
input rather than from the step, so a checker reading only the step would pass all 17
without looking at them.
"""

import subprocess
import sys
import textwrap
from pathlib import Path

SCRIPT = Path(__file__).parent.parent / "scripts" / "check-step-quantities.py"


def run(tmp_path, body):
    src = tmp_path / "spec.yml"
    src.write_text(textwrap.dedent(body), encoding="utf-8")
    p = subprocess.run([sys.executable, str(SCRIPT), str(src)],
                       capture_output=True, text=True)
    return p.returncode, p.stdout


STEP = """
    module: plant
    inputs:
      salt: {{title: Salt, stock: {{value: 100, unit: mM}}}}
    process_steps:
      - id: mix
        operator: mixing
        operands: [salt, water]
{extra}
"""


def step(extra):
    return STEP.format(extra=textwrap.indent(textwrap.dedent(extra), " " * 8))


def test_a_fraction_that_disagrees_with_its_input_stock_fails(tmp_path):
    code, out = run(tmp_path, step("""
        fractions: {salt: 0.05}
        finals: {salt: {value: 6, unit: mM}}
        balance: water
    """))
    assert code == 1
    assert "salt fraction x stock = 5 mM" in out


def test_a_fraction_that_agrees_with_its_input_stock_passes(tmp_path):
    code, out = run(tmp_path, step("""
        fractions: {salt: 0.05}
        finals: {salt: {value: 5, unit: mM}}
        balance: water
    """))
    assert code == 0
    assert "1 fraction x stock row(s) compared" in out


def test_units_of_one_dimension_are_converted_before_comparing(tmp_path):
    # 0.05 x 100 mM is 5000 µM. A literal comparison of the unit text would skip it.
    code, out = run(tmp_path, step("""
        fractions: {salt: 0.05}
        finals: {salt: {value: 5000, unit: µM}}
        balance: water
    """))
    assert code == 0
    assert "1 fraction x stock row(s) compared" in out


def test_different_dimensions_are_reported_and_never_failed(tmp_path):
    code, out = run(tmp_path, step("""
        fractions: {salt: 0.05}
        finals: {salt: {value: 5, unit: mg/mL}}
        balance: water
    """))
    assert code == 0
    assert "salt NOT COMPARED" in out and "different dimensions" in out


def test_ratio_units_of_different_kinds_are_not_converted(tmp_path):
    # pint would turn 50 mmol/mol into 50 g/kg without complaint.
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [salt, water]
            fractions: {salt: 0.5}
            stocks: {salt: {value: 100, unit: mmol/mol}}
            finals: {salt: {value: 50, unit: g/kg}}
            balance: water
    """)
    assert code == 0
    assert "ratios of different kinds" in out


def test_a_bare_c_fails_although_pint_reads_it(tmp_path):
    code, out = run(tmp_path, step("""
        finals: {salt: {value: 37, unit: C}}
    """))
    assert code == 1
    assert "electric quantity" in out


def test_mol_percent_fails_although_pint_reads_it(tmp_path):
    code, out = run(tmp_path, step("""
        finals: {salt: {value: 90, unit: mol%}}
    """))
    assert code == 1
    assert "a % carries no information" in out


def test_a_unit_pint_cannot_read_fails(tmp_path):
    code, out = run(tmp_path, step("""
        finals: {salt: {value: 1, unit: x}}
    """))
    assert code == 1
    assert "pint cannot read it" in out


def test_fold_is_defined_and_converts(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [premix, water]
            fractions: {premix: 0.4}
            stocks: {premix: {value: 2.5, unit: fold}}
            finals: {premix: {value: 1, unit: fold}}
            balance: water
    """)
    assert code == 0
    assert "1 fraction x stock row(s) compared" in out


def test_fractions_above_one_fail(tmp_path):
    code, out = run(tmp_path, step("""
        fractions: {salt: 0.7, water: 0.5}
    """))
    assert code == 1
    assert "fractions sum to 1.20000, above 1" in out


def test_amount_fractions_that_miss_1000_fail(tmp_path):
    code, out = run(tmp_path, step("""
        finals:
          salt: {value: 900, unit: mmol/mol}
          water: {value: 50, unit: mmol/mol}
    """))
    assert code == 1
    assert "mmol/mol finals sum to 950, not 1000" in out


def test_an_operand_with_no_amount_is_reported_and_not_failed(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [salt, sugar, water]
            fractions: {salt: 0.05}
    """)
    assert code == 0
    assert "1 of 3 operand(s) have no amount — sugar" in out


# ---- ITEM 4: coverage on every mixing step, all constituents, keys, and the balance

def test_a_step_with_no_amounts_is_now_read(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [salt, sugar]
    """)
    assert code == 0
    assert "2 of 2 operand(s) have no amount" in out
    assert "1 mixing step(s) with more than one operand stating no amount" in out


def test_a_packing_step_is_not_checked_for_coverage(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: pack
            operator: packing
            operands: [salt, sugar]
            fractions: {salt: 0.05}
    """)
    assert code == 0
    assert "have no amount" not in out


def test_every_constituent_must_have_an_amount(tmp_path):
    # ../docs/modules/s30-lysate/spec.yml has four inputs. One is not enough.
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [s30-lysate, water]
            fractions: {s30-premix: 0.4}
    """)
    assert code == 0
    assert "s30-lysate (no amount for amino-acid-mix, rnase-inhibitor, s30-extract)" in out


def test_all_constituents_cover_their_operand(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [s30-lysate, water]
            fractions: {s30-premix: 0.4, s30-extract: 0.3, amino-acid-mix: 0.1, rnase-inhibitor: 0.02}
    """)
    assert code == 0
    assert "have no amount" not in out


def test_a_key_that_names_nothing_is_reported_and_not_failed(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [s30-lysate, water]
            fractions: {premix: 0.4}
    """)
    assert code == 0
    assert "fractions.premix names no operand of this step and no constituent of one" in out


def test_a_named_balance_that_is_no_operand_fails(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [salt, sugar]
            fractions: {salt: 0.05, sugar: 0.1}
            balance: water
    """)
    assert code == 1
    assert "balance water is not an operand of this step" in out


def test_a_remainder_with_no_water_operand_is_reported_and_not_failed(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [salt, sugar]
            fractions: {salt: 0.05, sugar: 0.1}
    """)
    assert code == 0
    assert "the default balance, water, is not an operand" in out


def test_water_is_the_default_balance(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        process_steps:
          - id: mix
            operator: mixing
            operands: [salt, sugar, water]
            fractions: {salt: 0.05, sugar: 0.1}
    """)
    assert code == 0
    assert "have no amount" not in out
    assert "default balance" not in out


def test_the_corpus_has_no_failing_finding():
    p = subprocess.run([sys.executable, str(SCRIPT)], capture_output=True, text=True)
    assert p.returncode == 0, p.stdout


def test_an_optional_operand_needs_no_amount(tmp_path):
    code, out = run(tmp_path, """
        module: plant
        inputs:
          salt: {title: Salt}
          detergent: {title: Detergent, optional: true}
        process_steps:
          - id: mix
            operator: mixing
            operands: [salt, detergent, water]
            fractions: {salt: 0.05}
    """)
    assert code == 0
    assert "have no amount" not in out
