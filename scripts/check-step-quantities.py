#!/usr/bin/env python3
"""Check the quantities a spec.yml source states: their units, and whether they agree.

A step states its composition without a scale: a volume fraction per component, a
stock per reagent, and a final concentration where a page states one. It needs no
per-component volume and no total, because the same composition is the same reaction
at 10 µL or at 500 µL. Some of those figures restate each other, so they can disagree,
and no other script in this repo compares them.

Seven checks. The first five fail the run. The last two report and do not fail.

  UNITS      Every `unit` in a source parses with pint. Two spellings parse to the
             wrong thing without an error, so both fail by rule: a unit holding `%`
             other than a bare `%` (pint reads `mol%` as moles times percent), and a
             unit with an electric-current dimension (pint reads a bare `C` as
             coulombs). `fold` is the one unit this script defines: a relative
             strength, as in a 2.5-fold stock used at 1 fold.
  AMOUNT     A step's `mmol/mol` finals sum to 1000: the amount-of-substance fractions
             of a lipid film.
  FRACTION   fraction x stock equals the stated final, within 0.5%, after pint puts
             both in one unit. The stock is the step's own `stocks:` entry or, where
             the step has none for that key, the input's `stock:`. Two figures of
             different dimensions, such as mg/mL against mM, are reported NOT
             COMPARED. So are two ratio units of different kinds: pint reduces
             mmol/mol, g/kg and mL/L all to plain numbers, and would convert one into
             another without complaint.
  SUM        A step's fractions sum to no more than 1.
  BALANCE    A step's `balance`, where it names one, is an operand of the step. With no
             `balance` the balance is water, and a step whose fractions leave a
             remainder with no water operand is reported rather than failed: on some
             steps the remainder is mostly another operand that has no fraction yet.
  COVERAGE   Every operand of a `mixing` step with more than one operand has an
             amount: a fraction, a final, or the balance. An operand that is itself a
             mixture also counts as covered when EVERY one of its non-optional
             constituents has an amount at this step. An operand whose input is
             `optional: true` is skipped, as an optional constituent is; a constituent is a key of that
             operand's own `inputs:`. Every mixing step is read, including steps that
             state no amount at all. Reported and not failed, because the gap is in the
             source data, not in the source's shape. A step on a source that another
             source refines is marked as a class step, since a class may state no
             amount on purpose.
             ONLY `mixing`. A fraction is a share of one compartment, and only `mixing`
             puts its operands in one. On a `packing` step the outer solution is the
             medium the product sits in, not a share of anything.
  KEYS       Every key under `fractions`, `stocks` and `finals` names an operand of
             the step or a constituent of one. Reported and not failed. A key that
             names nothing cannot be covered or compared, so the checks above pass it.

WHAT THIS DOES NOT CHECK. `total_volume` is compared with nothing: on a converted step
no other figure is a volume. Quantities still held as strings, under `parameters`, `headroom`, `ratio` and
`inputs[].range`, are not read at all. The scope line at the end says how much was
read, so a run over nothing cannot look like a clean run.

Exit 0 when clean, 1 on a failing finding, 2 when it read no source.
"""
import argparse
import glob
import os
import sys

import pint
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Relative. `3.33 fold` is a rounded 10/3 and must not fail against 1 fold.
TOLERANCE = 0.005
ICON = {"ok": "✅", "note": "ℹ️ ", "warn": "⚠️ ", "fail": "⛔️"}

UREG = pint.UnitRegistry()
# Its own dimension, so a fold can never convert into a concentration or a plain number.
UREG.define("fold = [relative_strength]")
# An osmole gets a dimension of its own, so mOsm/L can never compare equal to mM.
# It is not a mole: a salt that dissociates gives two osmoles per mole, so defining
# `osmol = mole` would make the checker assert something false about every salt in
# the corpus — and let the two units this tranche exists to separate match silently.
UREG.define("osmol = [osmotic_amount] = Osm")


def parse_unit(unit):
    """The pint unit, or None and the reason this corpus refuses the spelling."""
    if "%" in unit and unit.strip() != "%":
        return None, ("a % carries no information, so the kind of fraction goes in the "
                      "unit: mmol/mol, g/kg or mL/L")
    try:
        units = UREG.Quantity(1, unit).units
    except Exception:
        return None, "pint cannot read it"
    if "[current]" in units.dimensionality:
        return None, "pint reads it as an electric quantity; a temperature is °C"
    return units, None


def ratio_kind(unit):
    """For a ratio unit such as mmol/mol, the dimension of its numerator."""
    return str(UREG.Quantity(1, unit.split("/")[0].strip()).dimensionality)


def units_in(node, path=""):
    """Every (path, unit) in a source, wherever a mapping carries a `unit:` string."""
    if isinstance(node, dict):
        if isinstance(node.get("unit"), str):
            yield path, node["unit"]
        for k, v in node.items():
            yield from units_in(v, f"{path}/{k}" if path else str(k))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from units_in(v, f"{path}/{i}")


def stock_of(step, inputs, key):
    """The stock for one component: the step's own entry, else the input's."""
    s = (step.get("stocks") or {}).get(key)
    if s:
        return s
    inp = inputs.get(key)
    return inp.get("stock") if isinstance(inp, dict) else None


def compare(key, f, stock, final):
    """(level, message) for one fraction x stock = final row, or None when it agrees."""
    su, why_s = parse_unit(stock.get("unit", ""))
    fu, why_f = parse_unit(final.get("unit", ""))
    if su is None or fu is None:
        return None     # UNITS reports it
    derived = f * UREG.Quantity(stock["value"], su)
    stated = UREG.Quantity(final["value"], fu)
    if derived.dimensionality != stated.dimensionality:
        return ("note", f"{key} NOT COMPARED — the stock is in {stock['unit']} and the "
                        f"final in {final['unit']}, which are different dimensions")
    if derived.dimensionless and ratio_kind(stock["unit"]) != ratio_kind(final["unit"]):
        return ("note", f"{key} NOT COMPARED — {stock['unit']} and {final['unit']} are "
                        f"ratios of different kinds")
    d = derived.to(stated.units).magnitude
    if abs(d - stated.magnitude) > TOLERANCE * max(abs(stated.magnitude), 1e-9):
        return ("fail", f"{key} fraction x stock = {d:.4g} {final['unit']}, but the "
                        f"source states {final['value']:g}")
    return ("ok", None)


def corpus_index(files):
    """Module id -> (its non-optional input keys, all its input keys), and the set of
    modules some other module refines."""
    constituents, refined = {}, set()
    for path in files:
        with open(path, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        if not isinstance(doc, dict):
            continue
        inputs = doc.get("inputs") or {}
        if doc.get("module"):
            constituents[doc["module"]] = (
                {k for k, v in inputs.items() if not (isinstance(v, dict) and v.get("optional"))},
                set(inputs))
        r = doc.get("refines")
        refined.update([r] if isinstance(r, str) else (r or []))
    return constituents, refined


def check_step(where, step, inputs, constituents):
    """Every (level, message) for one step, and the number of rows compared."""
    finals = step.get("finals") or {}
    fractions = step.get("fractions") or {}
    operands = step.get("operands") or []
    out, compared = [], 0

    reachable = set(operands).union(*(constituents.get(o, (set(), set()))[1] for o in operands))
    for carrier in ("fractions", "stocks", "finals"):
        for key in step.get(carrier) or {}:
            if key not in reachable:
                out.append(("warn", f"{where}: {carrier}.{key} names no operand of this "
                            f"step and no constituent of one"))

    balance = step.get("balance")
    if balance is not None and balance not in operands:
        out.append(("fail", f"{where}: balance {balance} is not an operand of this step"))

    amounts = {k: v["value"] for k, v in finals.items()
               if isinstance(v, dict) and v.get("unit") == "mmol/mol"}
    if amounts:
        s = sum(amounts.values())
        if abs(s - 1000) > 0.1:
            out.append(("fail", f"{where}: mmol/mol finals sum to {s:g}, not 1000 — "
                        + ", ".join(f"{k}={v:g}" for k, v in amounts.items())))
        else:
            out.append(("ok", f"{where}: {len(amounts)} amount fractions summing {s:g} mmol/mol"))

    if step.get("operator") == "mixing" and len(operands) > 1:
        amounts_at = set(fractions) | set(finals) | {balance or "water"}
        missing = []
        for o in operands:
            if o in amounts_at or (isinstance(inputs.get(o), dict) and inputs[o].get("optional")):
                continue
            parts = constituents.get(o, (set(), set()))[0]
            if parts and parts <= amounts_at:
                continue
            missing.append(o + (f" (no amount for {', '.join(sorted(parts - amounts_at))})"
                                if parts & amounts_at else ""))
        if missing:
            out.append(("warn", f"{where}: {len(missing)} of {len(operands)} operand(s) "
                        f"have no amount — {'; '.join(missing)}"))

    if not fractions:
        return out, compared

    for key, f in fractions.items():
        stock, final = stock_of(step, inputs, key), finals.get(key)
        if not (stock and final):
            continue
        result = compare(key, f, stock, final)
        if result is None:
            continue
        level, msg = result
        if level == "note":
            out.append(("note", f"{where}: {msg}"))
            continue
        compared += 1
        if level == "fail":
            out.append(("fail", f"{where}: {msg}"))

    total = sum(fractions.values())
    if total > 1 + 0.0005:
        out.append(("fail", f"{where}: fractions sum to {total:.5f}, above 1"))
    else:
        out.append(("ok", f"{where}: {len(fractions)} fraction(s) summing {total:.5f}"
                    + (f", balance {balance}" if balance else "")))
        if balance is None and total < 1 - 0.0005 and "water" not in operands:
            out.append(("warn", f"{where}: the fractions leave {1 - total:.5f}, and the "
                        f"default balance, water, is not an operand — name the balance "
                        f"or give the other operands fractions"))
    return out, compared


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("paths", nargs="*",
                    help="spec.yml files; the default is every one under docs/")
    a = ap.parse_args()

    pattern = os.path.join(REPO, "docs", "**", "spec.yml")
    files = a.paths or sorted(glob.glob(pattern, recursive=True))
    searched = " ".join(a.paths) if a.paths else pattern
    if not files:
        print(f"⛔️ nothing to check. searched: {searched}")
        return 2

    # THE INDEX READS THE WHOLE CORPUS EVEN WHEN FILES ARE NAMED. An operand's
    # constituents live in its own source, which is rarely among the files named.
    constituents, refined = corpus_index(sorted(glob.glob(pattern, recursive=True)) or files)
    fails = steps = stating = compared = units = unstated = 0
    for path in files:
        with open(path, encoding="utf-8") as fh:
            doc = yaml.safe_load(fh)
        if not isinstance(doc, dict):
            continue
        slug = os.path.basename(os.path.dirname(os.path.abspath(path)))
        for where, unit in units_in(doc):
            units += 1
            if parse_unit(unit)[0] is None:
                fails += 1
                print(f"⛔️ {slug}: {where} has unit {unit!r} — {parse_unit(unit)[1]}")
        inputs = doc.get("inputs") or {}
        for step in doc.get("process_steps") or []:
            if not isinstance(step, dict):
                continue
            steps += 1
            if any(step.get(k) for k in ("fractions", "finals", "stocks")):
                stating += 1
            elif step.get("operator") == "mixing" and len(step.get("operands") or []) > 1:
                unstated += 1
            where = f"{slug}/{step.get('id')}" + (" (class step)" if doc.get("module") in refined else "")
            out, n = check_step(where, step, inputs, constituents)
            compared += n
            for level, msg in out:
                fails += level == "fail"
                print(f"{ICON[level]} {msg}")

    # SCOPE, ALWAYS. A clean run over the wrong scope reads the same as a clean run.
    print(f"\nsearched: {searched}")
    print(f"{len(files)} source(s), {units} unit(s) parsed, {steps} step(s), "
          f"{stating} stating a quantity, {compared} fraction x stock row(s) compared, "
          f"{unstated} mixing step(s) with more than one operand stating no amount")
    print("✅ no failing findings." if not fails else f"⛔️ {fails} failing finding(s).")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
