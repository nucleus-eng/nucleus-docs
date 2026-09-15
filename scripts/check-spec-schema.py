#!/usr/bin/env python3
"""Validate docs/modules/*/spec.yml against scripts/spec-yml-schema.yml.

Local-only, deliberately — per Jon's Q6 ruling on
STAGED-2026-09-11-spec-yml-drift-check: "build the tooling to generate the
warnings, but let's not use it yet." Wiring it into qa.yml is phase 4, and needs
jsonschema added beside pyyaml there.

Two passes. The schema pass catches shape. The reference pass catches what a schema
cannot express: an operand naming nothing, a page path that does not exist, a module
key disagreeing with its own directory.

Prints the paths searched and the file count, because a validator that reports zero
findings over zero files looks identical to a clean run.
"""
import sys, glob, os, argparse

try:
    import yaml
except ImportError:
    sys.exit("needs pyyaml: pip install pyyaml")

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "spec-yml-schema.yml")


def schema_findings(doc, schema):
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        return None  # caller reports the skip rather than passing silently
    v = Draft202012Validator(schema)
    out = []
    for e in sorted(v.iter_errors(doc), key=lambda e: list(e.path)):
        where = "/".join(str(p) for p in e.path) or "<root>"
        out.append(("schema", where, e.message))
    return out


def reference_findings(path, doc):
    """What the schema cannot say."""
    out = []
    d = os.path.dirname(path)
    expect = os.path.basename(d)
    if doc.get("module") != expect:
        out.append(("module-key", "module",
                    f'is "{doc.get("module")}" but the directory is "{expect}"'))

    known = set((doc.get("inputs") or {}).keys())
    for i, s in enumerate(doc.get("steps") or []):
        sid = s.get("id", f"#{i}")
        for op in s.get("operands") or []:
            if op not in known:
                out.append(("operand", f"steps/{sid}/operands",
                            f'"{op}" names no input and no earlier step'))
        # a step's product is available to later steps
        pid = (s.get("produces") or {}).get("id")
        if pid:
            if pid in known:
                out.append(("duplicate-id", f"steps/{sid}/produces/id",
                            f'"{pid}" is already an input or an earlier product'))
            known.add(pid)

    # abstract: must name a real process directory. Existence only — whether it is
    # the IMMEDIATE parent needs the process tree, which lives in prose in
    # processes-main.md. One value was wrong by one hop when the rule was ruled.
    for i, s in enumerate(doc.get("steps") or []):
        sid = s.get("id", f"#{i}")
        ab = (s.get("process") or {}).get("abstract")
        if ab and not os.path.isdir(os.path.join(REPO, "docs/processes", ab)):
            out.append(("abstract", f"steps/{sid}/process/abstract",
                        f'"{ab}" names no directory under docs/processes/'))

    # every page: path must resolve, relative to the yml's own directory
    def pages(node, where):
        if isinstance(node, dict):
            for k, v in node.items():
                if k == "page" and isinstance(v, str):
                    if not os.path.exists(os.path.normpath(os.path.join(d, v))):
                        out.append(("page", where + "/page", f'"{v}" does not exist'))
                else:
                    pages(v, f"{where}/{k}")
        elif isinstance(node, list):
            for j, v in enumerate(node):
                pages(v, f"{where}/{j}")

    pages(doc, "")
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=None,
                    help="spec.yml files; default is every one under docs/modules/")
    ap.add_argument("--quiet", action="store_true")
    a = ap.parse_args()

    pattern = os.path.join(REPO, "docs/modules/*/spec.yml")
    files = a.paths or sorted(glob.glob(pattern))
    searched = " ".join(a.paths) if a.paths else pattern

    if not files:
        print(f"⛔️ nothing to check. searched: {searched}")
        return 2

    schema = yaml.safe_load(open(SCHEMA))
    total, checked, no_jsonschema = 0, 0, False

    for f in files:
        try:
            doc = yaml.safe_load(open(f))
        except yaml.YAMLError as e:
            print(f"⛔️ {os.path.relpath(f, REPO)}: unparsable — {e}")
            total += 1
            continue
        checked += 1
        sf = schema_findings(doc, schema)
        if sf is None:
            no_jsonschema = True
            sf = []
        for kind, where, msg in sf + reference_findings(f, doc):
            print(f"⛔️ {os.path.relpath(f, REPO)} [{kind}] {where}: {msg}")
            total += 1

    # scope, always — a clean run over the wrong scope reads the same as a clean run
    print(f"\nsearched: {searched}")
    print(f"{checked} source(s) checked against {os.path.relpath(SCHEMA, REPO)}")
    if no_jsonschema:
        print("⚠️  jsonschema not installed — shape pass SKIPPED, reference pass ran")
    print("✅ no findings." if total == 0 else f"⛔️ {total} finding(s).")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
