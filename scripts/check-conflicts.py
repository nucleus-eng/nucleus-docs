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


SENS = {m: {x["to"]: x for x in (d.get("sensitivities") or [])}
        for m, d in SRC.items()}

rows, tally = [], collections.Counter()
for mod, d in SRC.items():
    for step in d.get("process_steps") or []:
        for imp in step.get("impositions") or []:
            tally["impositions"] += 1
            for operand in operand_ids(step):
                inside = constituents(operand) - {operand}
                if imp["id"] in SENS.get(operand, {}):
                    rows.append(("CONFLICT", mod, step["id"], imp["id"], operand, None))
                for held in sorted(inside):
                    if imp["id"] in SENS.get(held, {}):
                        rows.append(("reach", mod, step["id"], imp["id"], operand, held))

for kind in ("CONFLICT", "reach"):
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
print(f"conflicts {tally['CONFLICT']} | reach {tally['reach']} | "
      f"requires {req_total} declared, {len(req_rows)} unsatisfied")
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
