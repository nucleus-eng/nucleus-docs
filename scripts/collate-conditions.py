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

THE TEST FOR THE FIRST IS WHETHER THE ID IS AN INPUT ID ANYWHERE, which is to say
whether the corpus has ever put that thing in a tube. It is a better test than a word
list because it is a fact about the corpus rather than about English. Note that a class
page named for a function -- `lysis` -- has a page but is never an input, so it does not
false-positive.

    python3 scripts/collate-conditions.py
    python3 scripts/collate-conditions.py --unjoined   # only the ids that meet nothing
"""
import argparse
import collections
import glob
import sys

import yaml

SPECS = sorted(glob.glob("docs/**/spec.yml", recursive=True))


def load():
    for path in SPECS:
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
            yield s.get("to"), "sensitivity", slug
        for i in doc.get("impositions") or []:
            yield i.get("id"), "imposition", slug
        for step in doc.get("process_steps") or []:
            if not isinstance(step, dict):
                continue
            for i in step.get("impositions") or []:
                yield i.get("id"), "imposition", slug
            abstract = (step.get("process") or {}).get("abstract")
            if abstract:
                yield abstract, "process-refinement", slug


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--unjoined", action="store_true",
                    help="list only ids that appear on one side of a Conflict")
    args = ap.parse_args()

    components = component_ids()
    rows = collections.defaultdict(lambda: {"roles": set(), "sources": set()})
    for name, role, slug in walk():
        if not name:
            continue
        rows[name]["roles"].add(role)
        rows[name]["sources"].add(slug)

    groups = collections.defaultdict(list)
    for name, r in rows.items():
        if "process-refinement" in r["roles"] and len(r["roles"]) == 1:
            kind = "a process, not a condition"
        elif name in components:
            kind = "composition: the axiom is this component's presence"
        else:
            kind = "function or condition: the axiom is what happens"
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

    print(f"\n{len(rows)} distinct id(s) across {len(SPECS)} source(s).")
    if unjoined:
        print(f"{unjoined} meet nothing on the other side. That is not a fault by "
              f"itself -- a sensitivity with no imposition means nobody has written the "
              f"step that would trigger it -- but it is where a typo would hide.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
