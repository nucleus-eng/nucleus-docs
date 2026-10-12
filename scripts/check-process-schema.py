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
    # THE PUBLISHED PROCESS ORDER, read so that an abstraction with no page still
    # resolves. Empty if the file is absent, which degrades to the old behaviour.
    order_nodes = set()
    try:
        with open(os.path.join(HERE, "docs/type-system.posets.yml")) as fh:
            edges = (yaml.safe_load(fh) or {}).get("orders", {}) \
                      .get("process_refinement", {}).get("edges") or {}
        for child, ps in edges.items():
            order_nodes.add(str(child))
            order_nodes.update(str(x) for x in (ps or []))
    except FileNotFoundError:
        pass

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

        parents = doc.get("refines")
        for parent in ([parents] if isinstance(parents, str) else (parents or [])):
            # AN ABSTRACT PROCESS NEED NOT HAVE A PAGE, 2026-10-11. Jon: "embed does not
            # get a page." So a parent that is a node of the published process order is
            # valid whether or not a directory exists for it -- `embed-gel` is the case
            # that forced this, an abstraction whose page was dropped with the gel class
            # pages. The order is the authority; the filesystem is not.
            if parent not in dirs and parent not in fdirs and parent not in order_nodes:
                findings += 1
                print(f"⛔️ {rel}: `refines: {parent}` names no directory under "
                      f"docs/processes/ or docs/functions/, and is not a node of "
                      f"docs/type-system.posets.yml's process order.", file=sys.stderr)

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
          f"{os.path.relpath(SCHEMA, HERE)}")
    print(f"{len(dirs)} process director(ies); "
          f"{len(dirs) - len(sources)} still have no source.")
    if not findings:
        print("✅ no findings.")
    else:
        print(f"⛔️ {findings} finding(s).", file=sys.stderr)
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
