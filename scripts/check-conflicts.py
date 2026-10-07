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

ABSENCE IS NOT A PASS AND IS NOT A CLAIM. An omitted `sensitivities` key means
no constraints have been declared, not that the Module has none. So a clean run over an undeclared corpus is silence, not
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
    `luxr-lacz-cascade/embed-ulga`. No step imposes anything during operation, so
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

def _class_impositions(m, seen=None):
    """An imposition declared on a CLASS is carried by every member's step.

    ADDED 2026-10-05, the same day the key existed. `impositions` was a step-only key
    until Jon ruled: "as a class all members impose lysis. so there should be a class
    level imposition i think." The key went into the schema and THIS FILE WAS NOT
    TAUGHT TO READ IT, so `Lysis` declared an imposition that was never computed:
    declared data, silent checker, and a corpus still reporting zero conflicts.

    Found by scripts/collate-conditions.py, which reported `lysis` as imposition-only
    with nothing on the other side, and then still reported no conflict once
    ../membrane declared the matching sensitivity. The second report is what gave it
    away: a join that exists in the data and not in the output.

    Follows `refines:` exactly as `_inherited` does for sensitivities. A member
    implementing a Function carries what that Function imposes.
    """
    seen = seen or set()
    if m in seen:
        return []
    seen.add(m)
    out = list((SRC.get(m) or {}).get("impositions") or [])
    r = (SRC.get(m) or {}).get("refines")
    for parent in ([r] if isinstance(r, str) else (r or [])):
        out += _class_impositions(parent, seen)
    return out


ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROC = {}
for _p in glob.glob(os.path.join(ROOT, "docs/processes/*/spec.yml")):
    _d = yaml.safe_load(open(_p))
    if isinstance(_d, dict):
        PROC[_d.get("process")] = _d


def _process_impositions(step, seen=None):
    """What the PROCESS a step runs inflicts, resolved through process `refines:`.

    ADDED 2026-10-05 IN THE SAME COMMIT THAT MOVED SIX IMPOSITIONS ONTO PROCESSES.
    Without it the move would have silently dropped them: this file read
    `step.impositions` and nothing else, so six declarations would have existed in the
    corpus and computed nothing, and the summary line would still have said zero
    conflicts. That is the same blindness the class-level key had an hour earlier.

    THREE WAYS A STEP NAMES A PROCESS and all three are followed: `process.page`,
    `process.abstract`, and `process.composed_of`, which is a chain of links run as one
    step. The chain matters: both `proteolysis` declarations sit on steps whose SECOND
    link is Degrade Exterior LacZ, so a lookup by `page` alone finds nothing.
    """
    seen = seen or set()
    names = []
    proc = step.get("process") or {}
    for link in (proc.get("composed_of") or [proc]):
        if link.get("page"):
            names.append(link["page"].split("/")[-2])
    if proc.get("abstract"):
        names.append(proc["abstract"])
    out = []
    while names:
        n = names.pop()
        if n in seen or n not in PROC:
            continue
        seen.add(n)
        out += list(PROC[n].get("impositions") or [])
        r = PROC[n].get("refines")
        names += [r] if isinstance(r, str) else (r or [])
    return out


def _ancestors(m, seen=None):
    """Every class `m` sits under, transitively. Membership, not containment."""
    seen = seen if seen is not None else set()
    for par in _parents(m):
        if par not in seen:
            seen.add(par)
            _ancestors(par, seen)
    return seen


def _satisfies(candidate, target):
    """Is `candidate` the thing a presence sensitivity named, or a member of it?"""
    return candidate == target or target in _ancestors(candidate)


def _compartments(step):
    """Which operands of one step share a compartment, as a list of sets.

    THE OPERATOR DECIDES IT, which is the whole reason the corpus records one.
    `mixing` puts everything in one compartment: one tube, one phase, everything
    touching everything. `packing` builds a boundary, so its operands do NOT all
    touch -- that separation is what the step is for.

    A MEMBRANE TOUCHES BOTH SIDES OF ITSELF AND NEITHER SIDE TOUCHES THE OTHER.
    Jon, 2026-10-07: "Membranes meet any solution containing them, as well as any
    solution that they contain. consider `Sol{M1{A} + M2{B}}`. M1 is touching Sol
    and A, but not B." So a packing step yields one compartment per boundary,
    holding that boundary and the operands it separates -- and a sibling's lumen
    is in a different compartment, which is why co-encapsulating two populations
    does not put one's cargo against the other's membrane.

    A PACKING STEP WITH NO BOUNDARY YIELDS NOTHING rather than falling back to
    one compartment. Three such steps exist and each packs a thing into a thing
    without naming the bilayer; guessing a boundary would invent co-location that
    the source does not state.
    """
    ops = operand_ids(step)
    if step.get("operator") == "mixing":
        return [set(ops)]
    bounds = [o for o in ops if _satisfies(o, "membrane")]
    rest = set(ops) - set(bounds)
    return [{b} | rest for b in bounds]


# PRESENCE: A COMPONENT IN THE SAME COMPARTMENT, WHICH IS NOT AN IMPOSITION.
# `sensitivities[].kind: presence` names a component rather than something a morphism
# inflicts, so the imposition walk above cannot find it: nothing imposes DMSO, it is
# simply in the tube. Added 2026-10-07 on Jon's ruling, after the detergent case --
# a purified TetR stock carrying Tween 80 into a reaction with liposomes in it.
#
# NO BOUND, BY RULING. "report ANY presence as a conflict!" Where the level that
# matters is unmeasured, reporting every presence is the honest reading and a bound
# invented to quiet the report would be a figure nobody measured.
presence_rows = []
for mod, d in SRC.items():
    for step in d.get("process_steps") or []:
        for shared in _compartments(step):
            present = set()
            for o in shared:
                present |= constituents(o)
            for o in sorted(shared):
                for holder in sorted(constituents(o)):
                    for sid, sens in (SENS.get(holder) or {}).items():
                        if sens.get("kind") != "presence":
                            continue
                        for p in sorted(present):
                            if p == holder or not _satisfies(p, sens["to"]):
                                continue
                            presence_rows.append(
                                (mod, step["id"], holder, o, p, sens))

rows, tally = [], collections.Counter()
for mod, d in SRC.items():
    carried = _class_impositions(mod)
    for step in d.get("process_steps") or []:
        for imp in (list(step.get("impositions") or [])
                    + carried + _process_impositions(step)):
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

for kind in ("CONFLICT", "moderate", "reach", "incomparable"):
    for k, mod, sid, iid, operand, held in rows:
        # SEVERITY SPLITS THE REPORT AND NOT THE COMPUTATION. A `moderate` meet is a
        # real meet -- reading a chromophore does bleach it -- and it is listed apart
        # so that routine reads do not bury a meet that destroys a Function.
        if SENS[held or operand][iid].get("severity") == "moderate":
            k = "moderate" if k == "CONFLICT" else k
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

# A READOUT IMPOSES ON WHAT IT READS, and `measured_by:` is where a Module names its
# readout. Added 2026-10-07 with `illumination`. Without it the two readout processes
# would declare an imposition that met nothing: a readout is not a `process_steps:`
# entry, because reading a Module is not a step in building one, so the walk above
# never reaches it. Same shape as the class-level and process-level keys, which each
# declared data this file could not yet read.
measured_rows = []
for mod, d in SRC.items():
    for entry in d.get("measured_by") or []:
        proc = (entry or {}).get("process") or {}
        for imp in _process_impositions({"process": proc}):
            for held in sorted(constituents(mod)):
                sens = (SENS.get(held) or {}).get(imp["id"])
                if sens:
                    measured_rows.append((mod, proc.get("title") or "?", imp, held, sens))

for mod, title, imp, held, sens in measured_rows:
    sev = sens.get("severity", "blocking")
    where = mod if held == mod else f"{mod} holds {held}"
    print(f"{'MODERATE' if sev == 'moderate' else 'CONFLICT':9s} {mod} measured by {title}")
    print(f"          imposes {imp['id']} on {where}")
    print(f"          {sens['basis']}: {sens['why'].strip()[:96]}")
    print()
    tally["moderate" if sev == "moderate" else "CONFLICT"] += 1

for mod, sid, holder, operand, present, sens in presence_rows:
    where = operand if holder == operand else f"{operand} holds {holder}"
    print(f"PRESENCE  {mod}/{sid}")
    print(f"          {present} shares a compartment with {where}, which is "
          f"sensitive to {sens['to']}")
    print(f"          {sens['basis']}: {sens['why'].strip()[:96]}")
    print()

# WHAT A PRESENCE SENSITIVITY MEETING NOTHING MEANS, printed every run. Two of the
# three meet nothing, and neither is a typo: `dmso` is an operand only of a pore no
# composition names, and the theophylline path has no cascade page, so there is no
# step where the analyte joins its reporter. Both would report the moment one is
# built. Printing the denominator is the same discipline the summary line below
# keeps for sensitivities: a quiet pass over an unwritten composition is silence.
_presence_declared = sorted(
    {sid for m in SRC for sid, s in (SENS.get(m) or {}).items()
     if s.get("kind") == "presence"})
_presence_met = {r[5]["to"] for r in presence_rows}
for sid in _presence_declared:
    if sid not in _presence_met:
        print(f"UNMET     {sid} is declared as a presence condition and no step puts "
              f"it beside what it affects.")
        print("          Not a typo and not a pass: nothing is built with it yet.\n")

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
print(f"conflicts {tally['CONFLICT']} | moderate {tally['moderate']} | "
      f"presence {len(presence_rows)} met, "
      f"{len(_presence_declared) - len(_presence_met)} unmet | ok {tally['ok']} | "
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
