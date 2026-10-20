#!/usr/bin/env python3
"""Validate every docs/processes/*/spec.yml against scripts/process-yml-schema.yml.

AND CHECK THE THINGS JSON SCHEMA CANNOT. Three rules live here rather than in the
schema because they are about the corpus rather than about one file:

  1. `process:` must match its own directory name. A source that names a different
     process is matched by nothing, because a module step's `process.abstract` resolves
     by directory.
  2. `refines:` must name a process directory that exists. The module-side equivalent
     is how `check-spec-schema.py` already treats `refines:` on a Module.
  3. An id in `impositions` must not ALSO be declared on a module step for a step that
     runs this process. That is the half-migrated state R20 warned about: two
     declarations of one fact, and a checker that cannot tell which is authoritative.

WRITTEN BEFORE ANY SOURCE EXISTS, deliberately. A checker added after the files it
checks has to be right about data that is already there; a checker added first is the
thing the first file is written against.
"""
import glob
import os
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import orders as ORDERS  # the one published-order loader; see scripts/orders.py

try:
    import jsonschema
except ImportError:
    print("⛔️ jsonschema is not installed", file=sys.stderr)
    sys.exit(2)

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = os.path.join(HERE, "scripts/process-yml-schema.yml")


def module_step_impositions():
    """Every (imposition id, process directory) a MODULE step declares."""
    out = []
    for path in glob.glob(os.path.join(HERE, "docs/**/spec.yml"), recursive=True):
        if "/processes/" in path:
            continue
        doc = yaml.safe_load(open(path))
        if not isinstance(doc, dict):
            continue
        for step in doc.get("process_steps") or []:
            if not isinstance(step, dict):
                continue
            proc = step.get("process") or {}
            page = proc.get("page")
            where = page.split("/")[-2] if page else proc.get("abstract")
            for imp in step.get("impositions") or []:
                out.append((imp.get("id"), where, path))
    return out


def main():
    schema = yaml.safe_load(open(SCHEMA))
    jsonschema.Draft202012Validator.check_schema(schema)
    validator = jsonschema.Draft202012Validator(schema)

    sources = sorted(glob.glob(os.path.join(HERE, "docs/processes/*/spec.yml")))
    # A PROCESS DIRECTORY IS ONE WITH A MARKDOWN PAGE IN IT. `docs/processes/resources/`
    # holds three PNGs and nothing else: it is shared artwork, not a process, and
    # counting it made the inventory report a source that will never be written.
    # Measured 2026-10-05: 27 directories, 26 with markdown.
    dirs = {os.path.basename(os.path.dirname(p))
            for p in glob.glob(os.path.join(HERE, "docs/processes/*/"))
            if glob.glob(os.path.join(p, "*.md"))}
    # A PARENT MAY BE A FUNCTION PAGE. `hold` is a coarser Process than any one Function, and
    # THE PUBLISHED ORDERS, through the one loader. scripts/orders.py, 2026-10-12.
    #
    # These two blocks each opened docs/type-order.yml and decided for themselves
    # what membership meant. Both were wrong at different times and in different
    # ways, and each fix landed in one place and not the other:
    #   the generated file  -- this read docs/type-system.posets.yml, which
    #                          render-posets.py builds FROM the `refines:` values
    #                          this check validates. Ten of eleven process sources
    #                          named a parent that is neither a page nor a
    #                          published Process, measured on e724d566, and all ten
    #                          passed because the generated file listed them and it
    #                          listed them because they named them. It rejected
    #                          `embed`, which is real, and accepted `assay`, which
    #                          is not: it taught authors the wrong value.
    #   edges, not nodes    -- edges is keyed by child, so a Process that refines
    #                          nothing and is refined by nothing never appeared.
    #                          Nine of forty-one at 15bcb95. On that basis a source
    #                          here was told to carry no `refines:` at all, when
    #                          `anneal` had been profiled upstream since 2026-10-05
    #                          and was exactly its parent.
    # Both rules now live in one module with tests that can fail.
    orders = ORDERS.load(HERE)
    type_nodes = ORDERS.type_nodes(orders)
    order_nodes = ORDERS.process_nodes(orders)


    # encapsulate and embed refine it, so `refines: hold` names a directory under
    # docs/functions/ and none under docs/processes/. Jon, 2026-10-10.
    fdirs = {os.path.basename(os.path.dirname(p))
             for p in glob.glob(os.path.join(HERE, "docs/functions/*/"))
             if glob.glob(os.path.join(p, "main.md"))}
    step_imps = module_step_impositions()
    findings = 0

    for path in sources:
        rel = os.path.relpath(path, HERE)
        doc = yaml.safe_load(open(path))
        for err in sorted(validator.iter_errors(doc), key=lambda e: e.path):
            findings += 1
            where = "/".join(str(x) for x in err.path) or "(root)"
            print(f"⛔️ {rel} [schema] {where}: {err.message}", file=sys.stderr)
        if not isinstance(doc, dict):
            continue

        own = os.path.basename(os.path.dirname(path))
        if doc.get("process") != own:
            findings += 1
            print(f"⛔️ {rel}: `process: {doc.get('process')}` does not match its "
                  f"directory `{own}`. A step's `process.abstract` resolves by "
                  f"directory, so this source would be matched by nothing.",
                  file=sys.stderr)

        # SIGNATURE TYPES RESOLVE AGAINST THE PUBLISHED TYPE ORDER, 2026-10-11. The
        # pattern that used to constrain them came off when the order's spelling stopped
        # being lowercase; this is what replaces it, rather than nothing.
        sig = doc.get("signature") or {}
        positions = [("takes", i, t) for i, t in enumerate(sig.get("takes") or [])]
        if sig.get("produces"):
            positions.append(("produces", None, sig["produces"]))
        for where, idx, pos in positions:
            t = (pos or {}).get("type")
            at = f"signature/{where}" + (f"[{idx}]" if idx is not None else "")
            if t is not None and t not in type_nodes:
                findings += 1
                print(f"⛔️ {rel}: `{at}/type: {t}` is not a node of "
                      f"docs/type-order.yml's type order.", file=sys.stderr)

        parents = doc.get("refines")
        for parent in ([parents] if isinstance(parents, str) else (parents or [])):
            # AN ABSTRACT PROCESS NEED NOT HAVE A PAGE, 2026-10-11. Jon: "embed does not
            # get a page." So a parent that is a node of the published process order is
            # valid whether or not a directory exists for it -- `embed-gel` is the case
            # that forced this, an abstraction whose page was dropped with the gel class
            # pages. The order is the authority; the filesystem is not.
            if parent not in dirs and parent not in fdirs and parent not in order_nodes:
                # FAILS AGAIN FROM 2026-10-12. This was downgraded to a warning
                # "UNTIL `make` AND `assay` ARE RULED ON", and Jon ruled on
                # 2026-10-12: the make-* sources repoint to `prepare` and
                # `purify`, `assay` to `observe` and `observe_absorbance`, and
                # `assemble-cytosol` became a real Process upstream. The
                # antecedent is spent.
                #
                # THE COUNT REACHED ZERO FIRST, which is the condition this repo
                # uses for every report-only check. Measured 2026-10-12 against
                # the republished order on #293: 0 findings of this kind. On THIS
                # branch alone it is 10, because this branch carries main's old
                # docs/type-order.yml, which predates the ruling -- so this check
                # is red here and green the moment #293 lands. Merge order is
                # #293 then this PR, and no workflow runs this checker either
                # way; the PR that wires it into CI lands last, after both.
                #
                # LEFT AS A WARNING THE CHECK COULD NOT REJECT A TYPO AT ALL. Any
                # misspelled parent counted toward a number nobody was gating on.
                findings += 1
                print(f"⛔️ {rel}: `refines: {parent}` names no directory under "
                      f"docs/processes/ or docs/functions/, and is not a node of "
                      f"docs/type-order.yml's published process order.",
                      file=sys.stderr)

        for imp in doc.get("impositions") or []:
            dupes = [p for i, w, p in step_imps if i == imp["id"] and w == own]
            if dupes:
                findings += 1
                print(f"⛔️ {rel}: `{imp['id']}` is declared here AND on "
                      f"{len(dupes)} module step(s) that run this process. One fact, "
                      f"two homes: move the step declarations or drop this one.",
                      file=sys.stderr)
                for d in dupes[:3]:
                    print(f"     {os.path.relpath(d, HERE)}", file=sys.stderr)

    print(f"{len(sources)} process source(s) checked against "
          f"scripts/process-yml-schema.yml")
    print(f"{len(dirs)} process director(ies); "
          f"{len(dirs) - len(sources)} still have no source.")
    if not findings:
        print("✅ no findings.")
    else:
        print(f"⛔️ {findings} finding(s).", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
