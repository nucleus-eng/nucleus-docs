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
    dirs = {os.path.basename(os.path.dirname(p))
            for p in glob.glob(os.path.join(HERE, "docs/processes/*/"))}
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
            if parent not in dirs:
                findings += 1
                print(f"⛔️ {rel}: `refines: {parent}` names no directory under "
                      f"docs/processes/.", file=sys.stderr)

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
