#!/usr/bin/env python3
"""Compute Layer C: Requirements checked, Conflicts computed, neither asserted.

compositional-biology-theory `glossary.md#T23` makes Conflict **derived** —
"Sensitivity meeting imposition. Computed, never asserted" — and files
"incompatibility (as a stated fact)" as its refused spelling. Its evidence
column reads "one constraint asserted on nine pages". This corpus measured the
same shape from the other side on 2026-09-21: six constraints, 36 lines, 24
files, each restated four to twelve times with nothing keeping the copies
agreeing.

So neither half asserts the join. `#T21` puts Sensitivity on an object, which is
a Module's `sensitivities:`. `#T22` puts Imposition on a morphism, which is a
step's `impositions:`. This walks every step and reports where an operand that
is sensitive to something meets a step that inflicts it.

  CONFLICT     a step imposes what one of its operands is sensitive to
  reach        the operand is not sensitive itself; something inside it is
  UNSATISFIED  a step requires something its composition cannot reach

`#T20` Requirement joins the other three on 2026-09-21: "a condition that must
hold for a morphism to be defined", so it is a step's `requires`. **It is not a
Conflict and cannot be one.** A Conflict is a meet of two declared halves, so it
can only say two things must not co-occur; a Requirement says something must be
PRESENT, and a missing step declares no half to take a meet over.

**Reachability is checked and the condition is not.** `requires[].of` must be
reachable in the step's composition, which is mechanical. Whether the prose in
`why` actually holds needs a placement model this corpus does not have, the same
limit as not knowing that a membrane blocks an imposition.

**`reach` IS NOT A DEFECT AND MUST NOT BE READ AS ONE.** This walks containment
and has no concept of a boundary stopping an imposition, which in a corpus built
out of compartments is the obvious gap. All three of today's `reach` findings are
the same true relation correctly neutralised: the aTc encapsulation steps dose
Proteinase K, the cytosol they act on holds LacZ, and LacZ is sensitive to it.
The membrane is why that is fine, and `degrade-exterior-lacz/main.md:38` says so
in as many words: proteinase K "digests LacZ (and other exterior protein) without
needing to enter the liposome". Teaching this checker that would mean deciding
which impositions cross which boundaries, which is a modeling question and not
a checker's to answer. So `reach` is reported, separated, and left.

ABSENCE IS NOT A PASS AND IS NOT A CLAIM. Jon, 2026-09-21: an omitted
`sensitivities` key "means that we haven't declared any constraints", not that
the Module has none. So a clean run over an undeclared corpus is silence, not
safety, and the denominator is printed every time for that reason.
"""
import collections
import glob
import os
import sys

import yaml

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

SRC = {}
for f in sorted(glob.glob("docs/modules/*/spec.yml")):
    SRC[f.split("/")[2]] = yaml.safe_load(open(f)) or {}


def operand_ids(step):
    out = []
    for o in step.get("operands") or []:
        out.append(o if isinstance(o, str) else o.get("module"))
    return [o for o in out if o]


def constituents(mod, seen=None):
    """Everything inside `mod`, transitively. A Conflict reaches what it holds."""
    seen = seen if seen is not None else set()
    if mod in seen or mod not in SRC:
        return seen
    seen.add(mod)
    d = SRC[mod]
    for key in (d.get("inputs") or {}):
        constituents(key, seen)
    for s in d.get("process_steps") or []:
        for o in operand_ids(s):
            constituents(o, seen)
    return seen


def resolve_bound(b, step, home):
    """A bound's value, or (None, reason) when it cannot be got.

    A literal states its own. A `from` reads the figure off an operand: resolve the
    operand to its module and search that module's step `parameters:` for the key.
    Ruled 2026-09-24 -- a literal would need one step per polymer, and one step per
    polymer is two processes, which is the thing the binding exists to avoid.

    NOT FINDING IT IS NOT A PASS. Every failure here returns a reason and the caller
    reports `incomparable`, because absence means undeclared everywhere else in this
    schema and a comparator that reads silence as agreement is worse than no
    comparator.
    """
    if "value" in b:
        return (b["value"], b.get("unit"), None)
    f = b.get("from") or {}
    operand, key = f.get("operand"), f.get("key")
    if operand not in operand_ids(step):
        return (None, None, f"`from` names {operand}, which is not an operand of this step")
    target = ((SRC.get(home, {}).get("inputs") or {}).get(operand) or {}).get("page")
    mod = None
    if target:
        mod = target.rstrip("/").split("/")[-2] if target.endswith("spec.md") else None
    if mod is None or mod not in SRC:
        return (None, None, f"{operand} resolves to no module page, so {key} cannot be read")
    for st in (SRC[mod].get("process_steps") or []):
        params = st.get("parameters") or {}
        if key in params:
            v = params[key]
            if not isinstance(v, (int, float)):
                return (None, None, f"{mod}.{key} is {v!r}, not a number")
            return (v, "C", None)
    return (None, None, f"{mod} declares no {key}")


def compare(imp_b, sens_b, iv, iu, sv, su):
    """CONFLICT, ok, or a reason it cannot be decided."""
    if imp_b.get("quantity") != sens_b.get("quantity"):
        return None, "different quantities"
    if iu != su:
        return None, f"units {iu!r} against {su!r} do not compare"
    isense, ssense = imp_b.get("sense"), sens_b.get("sense")
    if isense == "at-least" and ssense == "at-most":
        return (iv > sv), None
    if isense == "at-most" and ssense == "at-least":
        return (iv < sv), None
    return None, f"senses {isense} and {ssense} do not bracket"


def _own(m, entries):
    """One Module may declare two sensitivities to the same imposition.

    `cell` does: `thermal-stability` and `thermal-operating` both point at
    `thermal-hold`, because a cell being held is not a cell working. Keyed by
    `to` alone the second silently replaced the first. They carry the same figure
    today, so nothing was lost and nothing said so either. The strictest wins
    here too, and a pair that does not compare is reported rather than dropped.

    THE MERGE IS SAFE AND IT IS NOT RIGHT, and the gap has a name. `cell`'s two
    entries carry the same figure, so the strictest is either one. THE DAY THEY
    DIFFER THIS PICKS THE STRICTEST AND SAYS NOTHING, which would check an
    embedding step against an operating tolerance. That is never too permissive
    and it is the wrong predicate.

    WHAT IS MISSING IS ON THE STEP, NOT ON THE SENSITIVITY: which regime the step
    puts the Module in. The `compositional-biology-theory` session proposed this
    on 2026-09-25 and it reads right. MEASURED HERE THE SAME DAY, IT HAS ONE
    REGIME AND NOT TWO: all 10 declared impositions are `proteinase-k`,
    `uv-exposure`, `radical-acrylate-polymerization` or `thermal-hold`, and BOTH
    `thermal-hold` steps are embedding steps -- `ph-cascade/embed-agarose` and
    `london-cascade/embed-ulga`. No step imposes anything during operation, so
    `cell`'s `thermal-operating` is unreachable by any imposition in this corpus.
    A field with one attested value is not sized yet.
    """
    out = {}
    for x in entries:
        sid = x["to"]
        if sid in out:
            keep, why = _tighter(x.get("bound"), out[sid].get("bound"))
            if keep is None:
                INHERIT.append(("incomparable", m, sid,
                                f"its own {out[sid]['id']}", why))
                continue
            if keep == "b":
                continue
        out[sid] = x
    return out


def _parents(m):
    r = (SRC.get(m) or {}).get("refines")
    return [] if not r else ([r] if isinstance(r, str) else list(r))


INHERIT = []


def _tighter(a, b):
    """Of two bounds on one quantity, which tolerates less: "a", "b", or neither.

    A bound that reads its figure off an operand has no value until a step
    resolves it, so it cannot be ordered here. Returns (None, why) for every
    pair that does not compare, and the caller reports rather than guesses.
    """
    if not a or not b:
        return ("a" if a else "b"), None          # specificity, not tolerance
    if a.get("quantity") != b.get("quantity"):
        return None, (f"quantity {a.get('quantity')!r} against "
                      f"{b.get('quantity')!r}")
    if a.get("sense") != b.get("sense"):
        return None, f"sense {a.get('sense')} against {b.get('sense')}"
    if "value" not in a or "value" not in b:
        return None, "one side reads its figure off an operand and has no value yet"
    if a.get("unit") != b.get("unit"):
        return None, f"unit {a.get('unit')!r} against {b.get('unit')!r}"
    if a["sense"] == "at-most":
        return ("a" if a["value"] <= b["value"] else "b"), None
    return ("a" if a["value"] >= b["value"] else "b"), None


def _inherited(m, seen=None):
    """A sensitivity on a class is a claim about every member of it.

    ADDED 2026-09-24. This walked constituents only, which is glossary.md#T34
    containment, and missed glossary.md#T13 membership entirely. A sensitivity
    declared on the abstract `cell` reached none of the five cells that refine it,
    because refining is not containing. The class invariant is exactly the thing
    every member has, so the lookup follows `refines:` as well.

    THE STRICTEST BOUND WINS, by every route. `refines:` may be a list, so a
    Module may sit under two classes at once and must satisfy both invariants;
    the intersection is the only safe read. Ruled 2026-09-25 after the theory
    session found the hole in the first rule, which let a member's own entry win
    outright: if strictest-wins exists because a silent widening is unsafe, then
    a member widening locally is the same failure one level down.

    A MEMBER NARROWING IS CONSISTENT AND SILENT. The class says every member
    tolerates at most 37, this one reaches 30, and both statements hold.

    A MEMBER WIDENING CONTRADICTS ITS CLASS AND IS REPORTED. Either the class
    invariant is false or that Module is not a member, and swallowing the wider
    figure hides which. `basis` decides the repair: an observation against a rule
    says the mechanism claim is wrong, and an observation against an observation
    says the class enumerated and missed a case.
    """
    seen = seen if seen is not None else set()
    if m in seen:
        return {}
    seen.add(m)
    out = {}
    for par in _parents(m):
        for sid, s in _inherited(par, seen).items():
            if sid not in out:
                out[sid] = s
                continue
            keep, why = _tighter(out[sid].get("bound"), s.get("bound"))
            if keep is None:
                INHERIT.append(("incomparable", m, sid, par, why))
            elif keep == "b":
                out[sid] = s
    for sid, s in (_OWN.get(m) or {}).items():
        if sid in out:
            keep, why = _tighter(s.get("bound"), out[sid].get("bound"))
            if keep is None:
                INHERIT.append(("incomparable", m, sid, "its class", why))
            elif keep == "b":
                INHERIT.append(("widened", m, sid, "its class",
                                f"{s.get('basis')} here against "
                                f"{out[sid].get('basis')} on the class"))
                continue                      # the strictest still wins
        out[sid] = s
    return out


_OWN = {m: _own(m, d.get("sensitivities") or []) for m, d in SRC.items()}

SENS = {m: _inherited(m) for m in SRC}

def verdict(imp, sens, step, home):
    """Unvalued on either side keeps the old string-match answer, CONFLICT."""
    ib, sb = imp.get("bound"), sens.get("bound")
    if not ib or not sb:
        return "CONFLICT"
    iv, iu, why = resolve_bound(ib, step, home)
    if why:
        REASONS.append((home, step["id"], imp["id"], why))
        return "incomparable"
    sv, su, why = resolve_bound(sb, step, home)
    if why:
        REASONS.append((home, step["id"], imp["id"], why))
        return "incomparable"
    bad, why = compare(ib, sb, iv, iu, sv, su)
    if bad is None:
        REASONS.append((home, step["id"], imp["id"], why))
        return "incomparable"
    return "CONFLICT" if bad else "ok"


REASONS = []

rows, tally = [], collections.Counter()
for mod, d in SRC.items():
    for step in d.get("process_steps") or []:
        for imp in step.get("impositions") or []:
            tally["impositions"] += 1
            for operand in operand_ids(step):
                inside = constituents(operand) - {operand}
                if imp["id"] in SENS.get(operand, {}):
                    rows.append((verdict(imp, SENS[operand][imp["id"]], step, mod),
                                 mod, step["id"], imp["id"], operand, None))
                for held in sorted(inside):
                    if imp["id"] in SENS.get(held, {}):
                        v = verdict(imp, SENS[held][imp["id"]], step, mod)
                        rows.append(("reach" if v == "CONFLICT" else v,
                                     mod, step["id"], imp["id"], operand, held))

for k, *_ in rows:
    if k == "ok":
        tally["ok"] += 1

for kind in ("CONFLICT", "reach", "incomparable"):
    for k, mod, sid, iid, operand, held in rows:
        if k != kind:
            continue
        tally[k] += 1
        where = operand if held is None else f"{operand} holds {held}"
        s = SENS[held or operand][iid]
        print(f"{k:9s} {mod}/{sid}")
        print(f"          imposes {iid} on {where}")
        print(f"          {s['basis']}: {s['why'].strip()[:96]}")
        print()

for kind, m, sid, par, why in INHERIT:
    if kind == "widened":
        print(f"WIDENED   {m}")
        print(f"          declares {sid} wider than {par} allows, so one of the two is wrong")
        print(f"          {why}")
    else:
        print(f"INHERIT?  {m}")
        print(f"          {sid} from {par} does not compare with what it already has")
        print(f"          {why}")
    print()

req_rows, req_total = [], 0
for mod, d in SRC.items():
    for step in d.get("process_steps") or []:
        for r in step.get("requires") or []:
            req_total += 1
            reach = set()
            for operand in operand_ids(step):
                reach |= constituents(operand)
            if r["of"] not in reach:
                req_rows.append((mod, step["id"], r))
for mod, sid, r in req_rows:
    print(f"UNSATISFIED {mod}/{sid}")
    print(f"          requires {r['of']}, not reachable from its operands")
    print(f"          {r['why'].strip()[:96]}\n")

declared = sum(1 for m in SRC if SRC[m].get("sensitivities"))
steps = sum(len(d.get("process_steps") or []) for d in SRC.values())
print(f"{len(SRC)} sources: {declared} declare a sensitivity, {len(SRC) - declared} silent")
print(f"{steps} steps: {tally['impositions']} impositions declared")
wide = sum(1 for k, *_ in INHERIT if k == "widened")
print(f"conflicts {tally['CONFLICT']} | ok {tally['ok']} | "
      f"incomparable {tally['incomparable']} | reach {tally['reach']} | "
      f"requires {req_total} declared, {len(req_rows)} unsatisfied | "
      f"inheritance {wide} widened, {len(INHERIT) - wide} incomparable")
print("\nSilence is not safety: an undeclared Module makes no claim that it has "
      "no sensitivity,\nso a zero here counts what was declared and nothing else.")

# WHAT A ZERO HERE ACTUALLY BOUGHT, on the first run, 2026-09-21. No UV conflict
# is computed, and that is a result rather than an absence: `substrate-cprg` is
# sensitive to `uv-exposure`, four steps impose it, and CPRG is an operand of none
# of them. "Dose CPRG after crosslinking" is a decision the corpus states in prose
# on eleven pages, and this is the first thing that checks it holds. That is the
# difference #T23 is after between a Conflict computed and a Conflict asserted.
#
# Advisory, on check-operator-pairs.py's precedent. A computed Conflict is a
# finding about the design rather than an editable defect, and one of these is
# a route the Node already canceled: failing CI would demand a fix to a page
# that is correctly recording a dead end.
if "--strict" in sys.argv:
    sys.exit(1 if (tally["CONFLICT"] or req_rows) else 0)
if tally["CONFLICT"]:
    print(f"\nadvisory: {tally['CONFLICT']} conflict(s); pass --strict to fail on them.")
sys.exit(0)
