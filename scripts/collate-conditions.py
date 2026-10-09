#!/usr/bin/env python3
"""Collate every id a sensitivity or an imposition names, and say what each one is.

WHY IT EXISTS. Jon, 2026-10-05: "where are we keeping track of all the functions
implemented? does it make sense for us to have a big table in a page somewhere? an a
script that walks all the .yml files to collate all the functions?"

Nowhere was the answer. A condition id reaches a `spec.yml` through three keys and
nothing joined them:

    sensitivities[].to          what an object is subject to
    impositions[].id            what a class, or a step, inflicts
    process_steps[].process.abstract   which process a step's process refines

THEY ARE MATCHED AS BARE STRINGS, which is the reason this script is worth running.
check-conflicts.py computes a Conflict by comparing an imposition id against a
sensitivity's `to`. A typo on either side is SILENT: the pair never meets, and the
corpus reports zero conflicts, which is what it would report if there were none. An id
used once, on one side only, is the shape a typo takes.

WHAT AN ID MAY NAME, and this is the part that was got wrong first. Jon: "requirements
can be defined as any axiom over composition OR functions. the sensitivity is to the
component `dmso` and to `theophylline` itself, their presence."

So there are two legitimate kinds and an earlier version of this script reported one of
them as a defect:

  COMPOSITION    the id names a component, and the axiom is about its presence.
                 `membrane` is sensitive to `dmso`; `reporter-lacz` to `theophylline`.
  FUNCTION       the id names what something DOES, and the implementer is whatever
                 does it. `protein` is sensitive to `proteolysis`, implemented by
                 proteases, of which Proteinase K is one.

THE KIND IS DECLARED NOW, AND THE INFERENCE IS KEPT TO CHECK IT. `sensitivities[].kind`
landed in the schema on 2026-10-07, so a source says which of the two it means instead
of this script guessing. The guess is still computed and a disagreement is reported,
because the guess is the only thing that can catch a `kind:` nobody updated.

THE GUESS IS WHETHER THE ID IS AN INPUT ID ANYWHERE, which is to say whether the corpus
has ever put that thing in a tube. It is a better test than a word list because it is a
fact about the corpus rather than about English. Note that a class page named for a
function -- `lysis` -- has a page but is never an input, so it does not false-positive.

IT IS ALSO WRONG ON A NEW COMPONENT, which is why the declaration wins. `detergent` is a
class whose members are components; the class itself is an input id nowhere, so the
guess files it under FUNCTION. The source says `kind: presence` and that is the answer.

REQUIREMENTS ARE A SECOND PAIR, and they are reported apart from the first. A
module-level `requires:` names an operation a class's Function needs, and `provides:`
names an operation a Module makes available. They meet by name: a bare `transcribe`
is met by any provider of `transcribe`, and `transcribe[pT7]` only by a provider with
the same bracket. Like a Conflict, whether a requirement is met in a given composite is
computed and never declared, and this script does not compute it: it says only whether
any provider exists anywhere, which is where a misspelling would show.

    python3 scripts/collate-conditions.py
    python3 scripts/collate-conditions.py --unjoined   # only the ids that meet nothing
"""
import argparse
import collections
import glob
import sys

import yaml

SPECS = sorted(glob.glob("docs/modules/*/spec.yml"))
# PROCESS SOURCES ARE A THIRD HOME, as of 2026-10-05. Six impositions moved off module
# steps and onto the processes they belong to, and a collation that reads only modules
# would have reported them as having vanished.
PROCESSES = sorted(glob.glob("docs/processes/*/spec.yml"))


def load(paths=None):
    for path in (paths if paths is not None else SPECS):
        doc = yaml.safe_load(open(path))
        if isinstance(doc, dict):
            yield path, doc


def component_ids():
    """Every id the corpus has ever used as an input: the things that go in a tube."""
    ids = set()
    for _, doc in load():
        ids |= set((doc.get("inputs") or {}).keys())
    return ids


def walk():
    for path, doc in load():
        slug = path.split("/")[2]
        for s in doc.get("sensitivities") or []:
            yield s.get("to"), "sensitivity", slug, s.get("kind") or "imposition"
        for i in doc.get("impositions") or []:
            yield i.get("id"), "imposition", slug, None
        for step in doc.get("process_steps") or []:
            if not isinstance(step, dict):
                continue
            for i in step.get("impositions") or []:
                yield i.get("id"), "imposition", slug, None
            abstract = (step.get("process") or {}).get("abstract")
            if abstract:
                yield abstract, "process-refinement", slug, None
    for path, doc in load(PROCESSES):
        slug = path.split("/")[2]
        for i in doc.get("impositions") or []:
            yield i.get("id"), "imposition", slug, None
        r = doc.get("refines")
        for parent in ([r] if isinstance(r, str) else (r or [])):
            yield parent, "process-refinement", slug, None


def operation(name):
    """`transcribe[pT7]` -> (`transcribe`, `pT7`); a bare name has no restriction."""
    op, _, rest = name.partition("[")
    return op, (rest.rstrip("]") or None)


def meets(provided, required):
    """Whether a provider of `provided` meets a requirement for `required`.

    A bare requirement takes any provider of that operation. A restricted one takes
    only the same restriction: a provider is never less specific than what it meets.
    """
    pop, pr = operation(provided)
    rop, rr = operation(required)
    return pop == rop and (rr is None or pr == rr)


def requirements():
    """(required id, module) and (provided id, module), from the module sources."""
    req, prov = [], []
    for path, doc in load():
        slug = path.split("/")[2]
        req += [(r.get("id"), slug) for r in doc.get("requires") or []]
        prov += [(p.get("id"), slug) for p in doc.get("provides") or []]
    return req, prov


def report_requirements(unjoined_only):
    req, prov = requirements()
    print(f"\n==== requirements, and what provides them — {len(req)} required, "
          f"{len(prov)} provided ====")
    unmet = 0
    for rid, slug in sorted(req):
        by = sorted({f"{m} ({p})" for p, m in prov if meets(p, rid)})
        if not by:
            unmet += 1
        if unjoined_only and by:
            continue
        print(f"  {rid:34s} required by {slug}: "
              + ("met by " + ", ".join(by) if by else "NO PROVIDER declared anywhere"))
    for pid, slug in sorted(prov):
        if not unjoined_only and not any(meets(pid, r) for r, _ in req):
            print(f"  {pid:34s} provided by {slug}: nothing requires it yet")
    return unmet


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--unjoined", action="store_true",
                    help="list only ids that appear on one side of a Conflict")
    args = ap.parse_args()

    components = component_ids()
    rows = collections.defaultdict(
        lambda: {"roles": set(), "sources": set(), "declared": set()})
    for name, role, slug, declared in walk():
        if not name:
            continue
        rows[name]["roles"].add(role)
        rows[name]["sources"].add(slug)
        if declared:
            rows[name]["declared"].add(declared)

    COMPOSITION = "composition: the axiom is this component's presence"
    FUNCTION = "function or condition: the axiom is what happens"
    groups = collections.defaultdict(list)
    disagreed = []
    for name, r in rows.items():
        guess = COMPOSITION if name in components else FUNCTION
        declared = r["declared"]
        if "process-refinement" in r["roles"] and len(r["roles"]) == 1:
            kind = "a process, not a condition"
        elif "presence" in declared:
            kind = COMPOSITION
        elif "imposition" in declared:
            kind = FUNCTION
        else:
            kind = guess
        # THE GUESS IS KEPT IN ORDER TO CHECK THE DECLARATION. A `kind:` nobody updated
        # is the failure this catches, and it is invisible once the declaration wins.
        if declared and kind != guess:
            disagreed.append((name, kind, guess))
        groups[kind].append((name, r))

    unjoined = 0
    for kind in ("function or condition: the axiom is what happens",
                 "composition: the axiom is this component's presence",
                 "a process, not a condition"):
        if not groups[kind]:
            continue
        print(f"\n==== {kind} — {len(groups[kind])} ====")
        for name, r in sorted(groups[kind]):
            sens = "sensitivity" in r["roles"]
            imps = "imposition" in r["roles"]
            if kind.startswith("a process"):
                state = "—"
            elif sens and imps:
                state = "joins"
            else:
                state = "sensitivity only" if sens else "imposition only"
                unjoined += 1
            if args.unjoined and state in ("joins", "—"):
                continue
            print(f"  {name:34s} {len(r['sources']):>2} source(s)  {state}")

    print(f"\n{len(rows)} distinct id(s) across {len(SPECS)} module source(s) and "
          f"{len(PROCESSES)} process source(s).")
    if unjoined:
        print(f"{unjoined} meet nothing on the other side. That is not a fault by "
              f"itself -- a sensitivity with no imposition means nobody has written the "
              f"step that would trigger it -- but it is where a typo would hide.")
    unmet = report_requirements(args.unjoined)
    if unmet:
        print(f"\n{unmet} requirement(s) have no provider anywhere. Not a fault by "
              f"itself -- a provider may simply be undeclared -- but a misspelled id "
              f"looks exactly like this.")
    for name, kind, guess in sorted(disagreed):
        print(f"\nDECLARED vs INFERRED: `{name}` is declared {kind.split(':')[0]} and "
              f"this script would have inferred {guess.split(':')[0]}.")
        print("  The declaration wins and the row above uses it. Reported because an "
              "id that stops being an input anywhere, or starts being one, changes the "
              "inference and nothing else would say so.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
