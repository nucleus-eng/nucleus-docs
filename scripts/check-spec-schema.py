#!/usr/bin/env python3
"""Validate docs/modules/*/spec.yml against scripts/spec-yml-schema.yml.

Local-only, deliberately: the tooling is built before it is enforced. Wiring it
into qa.yml is phase 4, and needs
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

    # `refines:` MAY BE A LIST since 2026-09-24. Every entry is checked, because a
    # schema that only validates the first would let a typo through on the second.
    refines = doc.get("refines")
    parents = ([refines] if isinstance(refines, str) else list(refines or []))
    for parent in parents:
        if parent == doc.get("module"):
            out.append(("refines", "refines",
                        f'names its own module, "{parent}"'))
        elif not os.path.exists(os.path.join(REPO, "docs", "modules", parent, "spec.md")):
            out.append(("refines", "refines",
                        f'names "{parent}" but docs/modules/{parent}/spec.md does not exist'))
    if len(parents) != len(set(parents)):
        out.append(("refines", "refines", "names the same parent twice"))

    known = set((doc.get("inputs") or {}).keys())
    for i, s in enumerate(doc.get("process_steps") or []):
        sid = s.get("id", f"#{i}")
        for op in s.get("operands") or []:
            if op not in known:
                out.append(("operand", f"process_steps/{sid}/operands",
                            f'"{op}" names no input and no earlier step'))
        # a step's product is available to later steps
        pid = (s.get("produces") or {}).get("id")
        if pid:
            if pid in known:
                out.append(("duplicate-id", f"process_steps/{sid}/produces/id",
                            f'"{pid}" is already an input or an earlier product'))
            known.add(pid)

    # operator_pairs operands must be operands OF THE STEP. Nothing checked this
    # until 2026-09-21 and a typo proved it: a rename turned
    # `outer-solution-glutamate` into `outer-solution-glutamate-london` inside a pair
    # exception, the name matched no operand, and the exception silently stopped
    # applying. check-operator-pairs.py reads the list and has no way to know a
    # name in it is not in the step, so a disabled exception reads as a step that
    # never had one. A pair naming a non-operand is a claim about a pair that does
    # not exist.
    for i, s in enumerate(doc.get("process_steps") or []):
        sid = s.get("id", f"#{i}")
        ops = set(s.get("operands") or [])
        for j, ov in enumerate(s.get("operator_pairs") or []):
            for name in (ov.get("operands") or []):
                if name not in ops:
                    out.append((
                        "operator_pairs",
                        f"process_steps/{sid}/operator_pairs/{j}",
                        f'"{name}" is not an operand of this step'))

    # abstract: must name a real process directory, and must not name this step's own
    # process. Whether it is the IMMEDIATE parent in general needs the process tree,
    # which this file cannot read — but a step whose `page` resolves to process X and
    # whose `abstract` is X is self-referential ON THE STEP'S OWN EVIDENCE, with no tree
    # required. `abstract` is the immediate parent by the 2026-09-15 ruling, and nothing
    # is its own parent.
    #
    # ADDED 2026-10-05 on the theory session's F2, after it walked all 85 sources and
    # found 7 self-loops this check could not see. Six were fixed in `3f04ca2e`; the
    # seventh was introduced hours later by a repoint that fixed a different bug, which
    # is exactly the case a checker is for. The sub-case covers 7 of 7 historical hits.
    for i, s in enumerate(doc.get("process_steps") or []):
        sid = s.get("id", f"#{i}")
        proc = s.get("process") or {}
        ab = proc.get("abstract")
        if ab and not os.path.isdir(os.path.join(REPO, "docs/processes", ab)):
            out.append(("abstract", f"process_steps/{sid}/process/abstract",
                        f'"{ab}" names no directory under docs/processes/'))
        own = [l["page"].split("/")[-2]
               for l in (proc.get("composed_of") or [proc]) if l.get("page")]
        if ab and ab in own:
            out.append(("abstract", f"process_steps/{sid}/process/abstract",
                        f'"{ab}" is this step\'s own process, so it names itself as its '
                        f'parent. `abstract` is the IMMEDIATE parent; drop the key if '
                        f'the process is a root.'))

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


def quantity_findings(docs):
    """One `quantity` per imposition id, across the whole corpus.

    JSON Schema validates a file at a time and this is a claim about the set, so it
    lives here. Without it one `thermal-hold` could carry °C on one step and mM on
    another, and check-conflicts.py would compare different dimensions and report a
    number. Same discipline as check-operator-pairs.py's seed table: the meaning
    belongs to the id rather than to the use.
    """
    seen = {}          # imposition id -> (quantity, first file, first step)
    out = []
    for path, doc in docs:
        for step in (doc.get("process_steps") or []):
            for imp in (step.get("impositions") or []):
                b = imp.get("bound")
                if not b:
                    continue
                iid, q = imp["id"], b["quantity"]
                if iid not in seen:
                    seen[iid] = (q, path, step.get("id"))
                elif seen[iid][0] != q:
                    q0, f0, s0 = seen[iid]
                    out.append((path, "quantity",
                                f"impositions/{iid}",
                                f"quantity '{q}' here against '{q0}' at "
                                f"{f0}:{s0}. One quantity per imposition id."))
    return out


def restated_findings(docs):
    """A step that restates a parameter of the module it PRODUCES, and disagrees.

    A second claim about the set, so it lives beside the one above rather than in
    the schema. Four cascade steps each state the osmolarity and the Tris-HEPES
    fraction of the outer solution they produce, and the outer solution states them
    too. SEVEN RESTATEMENTS AT `27e7abc` AND ZERO DISAGREEMENTS, which is exactly
    why this reports only the disagreement: a step describing what it makes is
    legitimate documentation, and the same figure in two files with nothing keeping
    them equal is the hazard. The hazard becomes a defect the day one is edited.

    IT IS QUIET UNTIL THEN, DELIBERATELY. Reporting seven agreeing copies every run
    would train a reader to skip the line that matters. The restatement count prints
    as scope instead, the way this file prints the search path: a zero here means
    nothing diverged, not that nothing is duplicated.
    """
    S = {d.get("module"): d for _, d in docs}
    def params_of(m):
        out = {}
        for st in (S.get(m, {}).get("process_steps") or []):
            out.update(st.get("parameters") or {})
        return out
    out, restated = [], 0
    for path, doc in docs:
        for step in (doc.get("process_steps") or []):
            page = (step.get("produces") or {}).get("page")
            tgt = page.rstrip("/").split("/")[-2] if page and page.endswith("spec.md") else None
            if not tgt or tgt == doc.get("module") or tgt not in S:
                continue
            theirs = params_of(tgt)
            for k, v in (step.get("parameters") or {}).items():
                if k not in theirs:
                    continue
                restated += 1
                if str(v) != str(theirs[k]):
                    out.append((path, "restated",
                                f"process_steps/{step.get('id')}/parameters/{k}",
                                f"'{v}' here against '{theirs[k]}' on {tgt}, "
                                f"which this step produces."))
    return out, restated


def _parents(doc):
    refines = doc.get("refines")
    return [refines] if isinstance(refines, str) else list(refines or [])


def _levels(start, step):
    """Modules reachable from `start` through `step`, one list per hop, nearest
    first. Each module appears once, so a cycle in `refines:` ends the walk
    rather than looping."""
    seen, levels, frontier = {start}, [], [start]
    while frontier:
        nxt = []
        for m in frontier:
            for n in step(m):
                if n not in seen:
                    seen.add(n)
                    nxt.append(n)
        if nxt:
            levels.append(nxt)
        frontier = nxt
    return levels


def _graph(docs):
    """Each module's (path, doc), and the modules that refine it."""
    by_name = {d.get("module"): (p, d) for p, d in docs}
    children = {}
    for m, (_, d) in by_name.items():
        for parent in _parents(d):
            children.setdefault(parent, []).append(m)
    return by_name, children


def _is_number(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool)


def member_property_findings(docs):
    """Every member of a class that declares `member_properties:` states each key.

    The class names a quantity and its members state the values, in a step's
    `parameters:`, which is where impositions already read figures such as
    `gel_point_max_c`. So no figure is written twice, and this check is what
    makes the class's list a requirement rather than a description.

    THE MEMBERS CHECKED ARE THE LEAVES BELOW THE CLASS. A subclass between them
    is skipped, because it is abstract and states no values of its own; its
    members are checked instead. A member may inherit a value from any module
    between it and the class, so a subclass that does state a key passes it on.

    For a two-key range it also reports a low end above the high end, when both
    are numbers. A value that is not a number is not compared.

    Returns (findings, members checked).
    """
    by_name, children = _graph(docs)
    out, checked = [], 0
    for cls, (_, cdoc) in sorted(by_name.items()):
        declared = cdoc.get("member_properties") or []
        if not declared:
            continue
        below = {m for lvl in _levels(cls, lambda m: children.get(m, [])) for m in lvl}
        for m in sorted(below):
            if children.get(m) or m not in by_name:
                continue
            checked += 1
            path, _ = by_name[m]
            up = [a for lvl in _levels(m, lambda x: _parents(by_name[x][1]) if x in by_name else [])
                  for a in lvl if a in below]
            values = {}
            for source in [m] + up:
                for st in (by_name[source][1].get("process_steps") or []):
                    for k, v in (st.get("parameters") or {}).items():
                        if v is not None:
                            values.setdefault(k, v)
            for prop in declared:
                keys = prop.get("keys") or []
                missing = [k for k in keys if k not in values]
                for k in missing:
                    out.append((path, "member-property", f"parameters/{k}",
                                f"{m} refines {cls}, which requires {k}; "
                                f"no step states it."))
                if len(keys) == 2 and not missing:
                    lo, hi = values[keys[0]], values[keys[1]]
                    if _is_number(lo) and _is_number(hi) and lo > hi:
                        out.append((path, "member-property", f"parameters/{keys[0]}",
                                    f"{keys[0]} is {lo} and {keys[1]} is {hi}: the low "
                                    f"end of the range {cls} requires is above the high end."))
    return out, checked


# THE ONE PAIRING CLASS, NAMED HERE BECAUSE NOTHING IN A SOURCE MARKS ONE. Color
# Change is the class whose members pair an enzyme with its substrate. A second
# pairing class would be added to this tuple, not inferred.
PAIRING_CLASSES = ("color-change",)


def _page_target(path, page):
    """The module a `page:` points at, or None. Relative to the yml's directory."""
    if not page:
        return None
    parts = os.path.normpath(os.path.join(os.path.dirname(path), page)).split(os.sep)
    if len(parts) >= 3 and parts[-1] == "spec.md" and parts[-3] == "modules":
        return parts[-2]
    return None


def _same_page(path_a, page_a, path_b, page_b):
    a = os.path.normpath(os.path.join(os.path.dirname(path_a), page_a))
    b = os.path.normpath(os.path.join(os.path.dirname(path_b), page_b))
    return a == b


def substrate_findings(docs):
    """Every member of a pairing class pairs its enzyme with one of its substrates.

    An enzyme module lists what it acts on in `substrates:`, and a module that
    refines it inherits the list: the substrates belong to the enzyme however it
    is supplied. So the valid pairs follow from those lists, and a new enzyme
    brings its own list without the pairing class changing.

    For each member of a class in PAIRING_CLASSES, directly or through a
    subclass: an input whose `page:` is a module with a list, its own or the
    nearest one up its `refines:` chain, is an enzyme. Another input must match
    an entry on that list, by page when both have one and by title otherwise.

    A MEMBER NONE OF WHOSE INPUTS HAS A LIST IS NOT CHECKED, and that is what lets
    this check land before any enzyme declares one. It also means a member whose
    enzyme input has `page: null` is not checked. A substrate held inside a
    carrier, rather than named as an input, does not match.

    Returns (findings, members checked).
    """
    by_name, children = _graph(docs)

    def substrates_of(m):
        """(declaring path, entry) pairs from m's own list, else the nearest
        level of ancestors that declares one. None if nothing does."""
        for lvl in [[m]] + _levels(m, lambda x: _parents(by_name[x][1]) if x in by_name else []):
            found = [a for a in lvl if a in by_name and by_name[a][1].get("substrates") is not None]
            if found:
                return [(by_name[a][0], e) for a in found for e in by_name[a][1]["substrates"]]
        return None

    out, checked = [], 0
    for cls in PAIRING_CLASSES:
        if cls not in by_name:
            continue
        for m in sorted({x for lvl in _levels(cls, lambda x: children.get(x, [])) for x in lvl}):
            if m not in by_name:
                continue
            path, doc = by_name[m]
            inputs = doc.get("inputs") or {}
            enzymes = {}
            for k, v in inputs.items():
                target = _page_target(path, (v or {}).get("page"))
                subs = substrates_of(target) if target in by_name else None
                if subs is not None:
                    enzymes[k] = (target, subs)
            if not enzymes:
                continue
            checked += 1
            for ek, (target, subs) in enzymes.items():
                def matches(inp, decl_path, entry):
                    ip, ep = (inp or {}).get("page"), entry.get("page")
                    if ip and ep:
                        return _same_page(path, ip, decl_path, ep)
                    return ((inp or {}).get("title") or "").strip().casefold() == \
                           (entry.get("title") or "").strip().casefold()
                if not any(matches(v, dp, e) for k, v in inputs.items() if k != ek
                           for dp, e in subs):
                    names = ", ".join(e.get("title", "?") for _, e in subs) or "an empty list"
                    out.append((path, "substrate", f"inputs/{ek}",
                                f"{m} pairs {target} with none of its substrates ({names})."))
    return out, checked


def _load_corpus(pattern):
    """Every parsable source, for context. An unparsable one is reported by the
    main loop when it is named, and skipped here."""
    out = []
    for f in sorted(glob.glob(pattern)):
        try:
            out.append((os.path.relpath(f, REPO), yaml.safe_load(open(f))))
        except yaml.YAMLError:
            continue
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
    loaded = []

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
        loaded.append((os.path.relpath(f, REPO), doc))

    for path, kind, where, msg in quantity_findings(loaded):
        print(f"⛔️ {path} [{kind}] {where}: {msg}")
        total += 1

    restated_out, restated_n = restated_findings(loaded)
    for path, kind, where, msg in restated_out:
        print(f"⛔️ {path} [{kind}] {where}: {msg}")
        total += 1

    # THE TWO CLASS-WIDE CHECKS READ THE WHOLE CORPUS EVEN WHEN FILES ARE NAMED,
    # because a member's class is rarely among them, and a check that cannot see
    # the class reports nothing and looks clean. They report on the named files only.
    context = loaded if not a.paths else _load_corpus(pattern)
    scope = {p for p, _ in loaded}
    member_out, member_n = member_property_findings(context)
    substrate_out, substrate_n = substrate_findings(context)
    for path, kind, where, msg in member_out + substrate_out:
        if path in scope:
            print(f"⛔️ {path} [{kind}] {where}: {msg}")
            total += 1

    # scope, always — a clean run over the wrong scope reads the same as a clean run
    print(f"\nsearched: {searched}")
    print(f"{checked} source(s) checked against {os.path.relpath(SCHEMA, REPO)}")
    print(f"{restated_n} step parameter(s) restate one of the module they produce; "
          f"{len(restated_out)} disagree")
    print(f"{member_n} member(s) checked against a class's member_properties; "
          f"{substrate_n} pairing member(s) checked against an enzyme's substrates")
    if no_jsonschema:
        print("⚠️  jsonschema not installed — shape pass SKIPPED, reference pass ran")
    print("✅ no findings." if total == 0 else f"⛔️ {total} finding(s).")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
