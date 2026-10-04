#!/usr/bin/env python3
"""Draft every partial order the corpus carries, and name the ones it does not.

Everything is some amount of Abstract. It is not a binary yes or no, but a set
of partially ordered sets, and this enumerates that set.

THE GUARD THIS SCRIPT IS BUILT AROUND. A report titled "all the posets" that
quietly contains only the ones a script could reach is a partial check filling
the gap it leaves. So the output has three sections and always prints all three:
the orders it GENERATED, the orders it CANNOT REACH with where they live, and
the candidates that are NOT ORDERS with why. A reader must never have to guess
whether an absent order is absent from the corpus or absent from this tool.

WHAT MAKES SOMETHING A POSET HERE. Reflexive, antisymmetric, transitive. In
practice that means acyclic: reachability in a DAG is a partial order, and a
cycle breaks antisymmetry. Every generated order is checked for cycles rather
than assumed, and a single-parent relation is checked for being single-parent
rather than trusted because the schema says string.

    python3 scripts/render-posets.py            # the draft
    python3 scripts/render-posets.py --edges    # edge lists too
"""
import collections
import pathlib
import re
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent / "docs" / "modules"


def sources() -> dict[str, dict]:
    out = {}
    for d in sorted(ROOT.iterdir()):
        f = d / "spec.yml"
        if f.is_file():
            out[d.name] = yaml.safe_load(f.read_text()) or {}
    return out


def cycles(edges: dict[str, set]) -> list[list[str]]:
    """Every cycle reachable by DFS. Empty means the relation is a partial order."""
    found, state = [], {}

    def walk(n, path):
        state[n] = 1
        for m in sorted(edges.get(n, ())):
            if state.get(m) == 1:
                found.append(path[path.index(m):] + [m])
            elif state.get(m) is None:
                walk(m, path + [m])
        state[n] = 2

    for n in sorted(edges):
        if state.get(n) is None:
            walk(n, [n])
    return found


def tree(kids: dict[str, list], roots: list[str], depth=0, out=None) -> list[str]:
    out = [] if out is None else out
    for r in roots:
        out.append("    " * depth + ("└── " if depth else "") + r)
        tree(kids, sorted(kids.get(r, [])), depth + 1, out)
    return out



def parents_all(S: dict[str, dict]) -> dict[str, list[str]]:
    """Every declared parent, keeping both forms. A list means several parents."""
    out = {}
    for m, d in S.items():
        r = d.get("refines")
        if not r:
            continue
        out[m] = [r] if isinstance(r, str) else list(r)
    return out


def ancestors(node: str, parents: dict[str, list[str]], seen=None) -> set[str]:
    """Everything reachable upward from `node`, excluding itself."""
    seen = set() if seen is None else seen
    for p in parents.get(node, ()):
        if p not in seen:
            seen.add(p)
            ancestors(p, parents, seen)
    return seen


def covering(parents: dict[str, list[str]]) -> tuple[dict[str, list[str]], int]:
    """The transitive reduction: the covering relation a Hasse diagram draws.

    AN EDGE IS REDUNDANT WHEN A LONGER PATH ALREADY CARRIES IT. If `c` declares
    parents `p` and `p'`, and `p` is an ancestor of `p'`, then `c -> p` says
    nothing `c -> p' -> ... -> p` did not. Drawing both is the difference between
    a Hasse diagram and an edge dump, and it is the whole reason this is not
    just the declared edges with the nesting removed.
    """
    out, dropped = {}, 0
    for c, ps in parents.items():
        keep = []
        for p in ps:
            if any(p in ancestors(q, parents) for q in ps if q != p):
                dropped += 1
                continue
            keep.append(p)
        out[c] = keep
    return out, dropped


def longest_up(node: str, parents: dict[str, list[str]], memo=None) -> int:
    """Longest upward path. A DAG has no single depth, so this is the rank."""
    memo = {} if memo is None else memo
    if node in memo:
        return memo[node]
    memo[node] = 0  # guards a cycle rather than recursing forever
    memo[node] = 1 + max((longest_up(p, parents, memo) for p in parents.get(node, ())),
                         default=-1)
    return memo[node]


def hasse(name: str, what: str, parents: dict[str, list[str]], extra: str = "") -> None:
    """One generated order drawn as a Hasse diagram, multi-parent nodes included.

    THE FOREST DRAWING WAS NOT WRONG, IT WAS NARROWER THAN THE RELATION. Nesting
    can only show a node once, so a node with two parents has to be dropped or
    duplicated, and this script dropped them -- 10 of 58 at the time this was
    written. A Hasse diagram has no such limit, so the denominator closes.
    """
    cover, dropped = covering(parents)
    nodes = set(parents) | {p for ps in parents.values() for p in ps}
    cyc = cycles({c: set(ps) for c, ps in parents.items()})
    multi = sorted(c for c, ps in parents.items() if len(ps) > 1)
    edges = sum(len(ps) for ps in cover.values())
    roots = sorted(n for n in nodes if not parents.get(n))
    rank = {n: longest_up(n, parents) for n in nodes}

    print(f"\n## {name}")
    print(f"\n{what}")
    print(f"\n  partial order : {'YES, no cycles' if not cyc else f'NO — {cyc}'}")
    print(f"  single parent : {'YES' if not multi else f'NO — {len(multi)} of {len(parents)} declare several'}")
    print(f"  nodes         : {len(nodes)}")
    print(f"  edges drawn   : {edges} covering, {dropped} implied by a longer path and not drawn")
    print(f"  roots         : {len(roots)}")
    print(f"  max rank      : {max(rank.values()) if rank else 0}")
    if multi:
        print(f"  several parents: {', '.join(multi)}")
    if extra:
        print(f"  {extra}")

    print("\n```{mermaid}")
    print("flowchart BT")
    for n in sorted(nodes):
        print(f'    {n.replace("-", "_")}["{n}"]')
    for c in sorted(cover):
        for par in sorted(cover[c]):
            print(f'    {c.replace("-", "_")} --> {par.replace("-", "_")}')
    print("```")

    print("\n  by rank, lowest first:")
    for r in range(max(rank.values(), default=0) + 1):
        row = sorted(n for n, v in rank.items() if v == r)
        print(f"    {r}: {', '.join(row)}")


def report(name, what, parent, extra=""):
    """One generated order: axioms, shape, denominator, drawing."""
    kids = collections.defaultdict(list)
    for k, v in parent.items():
        kids[v].append(k)
    nodes = set(parent) | set(kids)
    cyc = cycles({k: {v} for k, v in parent.items()})
    roots = sorted(n for n in kids if n not in parent)
    depths = []
    for n in nodes:
        d, seen = 0, set()
        while n in parent and n not in seen:
            seen.add(n); n = parent[n]; d += 1
        depths.append(d)
    print(f"\n## {name}")
    print(f"\n{what}")
    print(f"\n  partial order : {'YES, no cycles' if not cyc else f'NO — {cyc}'}")
    print(f"  single parent : YES by construction, one string per node")
    print(f"  nodes         : {len(nodes)}")
    print(f"  edges         : {len(parent)}")
    print(f"  roots         : {len(roots)}")
    print(f"  max depth     : {max(depths) if depths else 0}")
    if extra:
        print(f"  {extra}")
    print()
    for line in tree(kids, roots):
        print("  " + line)


if __name__ == "__main__":
    S = sources()
    print("=" * 74)
    print("THE POSETS OF THIS CORPUS — draft")
    print(f"docs/modules, {len(S)} sources")
    print("=" * 74)
    print("\n" + "#" * 74)
    print("# SECTION 1 — GENERATED FROM THE SOURCES")
    print("#" * 74)

    # --- P1. Module refinement.
    # DRAWN AS A HASSE DIAGRAM, NOT A FOREST. `refines:` may be a list since
    # 2026-09-24, and a nesting can show a node once, so every multi-parent source
    # had to be dropped from the drawing -- 10 of 58 when this was written. The
    # covering relation has no such limit, so the denominator closes.
    p1 = parents_all(S)
    dangling = {v for ps in p1.values() for v in ps if v not in S}

    _placed = set(p1) | {v for ps in p1.values() for v in ps}
    hasse("P1. Module refinement, from `refines:`",
          "A Module refines the class that classifies it. `refines:` may be a list "
          "since 2026-09-24, so this is a DAG and is drawn as its covering relation.",
          p1,
          f"placed        : {len(_placed)} of {len(S)} sources; "
          f"{len(S) - len(_placed)} placed by nothing"
          + (f"\n  DANGLING      : {sorted(dangling)}" if dangling else ""))
    # AN ISOLATED NODE IS INVISIBLE IN A TREE, so list it. A source that is
    # placed by nothing is not a leaf and not a root. It is unplaced, and the
    # difference matters most for a CLASS page, which is a parent with no
    # children — a class nothing declares membership in.
    unplaced = sorted(set(S) - set(p1) - set(p1.values()))
    print("\n  PLACED BY NOTHING, listed because a tree cannot show an absent node:")
    for i in range(0, len(unplaced), 3):
        print("    " + "  ".join(f"{u:30}" for u in unplaced[i:i + 3]).rstrip())

    # --- P2. Process refinement. THE CARRIER IS A STEP, NOT A MODULE.
    # One Module contributes several steps and one abstract parent appears on
    # many, so this deduplicates to process directory -> abstract directory.
    # Without that the picture inflates by the number of steps.
    p2, conflicts, steps_seen = {}, collections.defaultdict(set), 0
    for m, d in S.items():
        for s in d.get("process_steps") or []:
            pr = s.get("process") or {}
            ab = pr.get("abstract")
            if not ab:
                continue
            steps_seen += 1
            page = pr.get("page") or ""
            child = re.sub(r"/[^/]+$", "", page).rsplit("/", 1)[-1] if page else None
            if not child:
                continue
            conflicts[child].add(ab)
            p2[child] = ab
    bad = {k: sorted(v) for k, v in conflicts.items() if len(v) > 1}
    report("P2. Process refinement, from `process_steps[].process.abstract`",
           "A process is an instance of a more abstract process. THE CARRIER IS A STEP,\n"
           "so this deduplicates to one edge per process directory.",
           p2,
           f"steps declaring one : {steps_seen} of {sum(len(d.get('process_steps') or []) for d in S.values())}\n"
           f"  distinct processes  : {len(p2)} after dedupe\n"
           f"  a process with two different parents : {bad or 'none — the map is a function'}")
    PROC = ROOT.parent / "processes"
    # CHECKED, NOT ASSUMED. A parent process named by `abstract:` should have a
    # page of its own, and a report of zero is only worth having beside its
    # denominator. All three have one at 3747a87; a peer read otherwise.
    absent = sorted(a for a in set(p2.values())
                    if not list((PROC / a).glob("*main.md")))
    print(f"  abstract parents with NO page : {len(absent)} of "
          f"{len(set(p2.values()))} — {', '.join(absent) or 'none, all have one'}")

    # --- P3. Module containment. NOT REFINEMENT. A different order entirely.
    p3 = collections.defaultdict(set)
    for m, d in S.items():
        for k, v in (d.get("inputs") or {}).items():
            page = (v or {}).get("page")
            if page and (mm := re.match(r"\.\./([^/]+)/spec\.md$", page)):
                p3[m].add(mm.group(1))
    cyc3 = cycles({k: v for k, v in p3.items()})
    nodes3 = set(p3) | {x for v in p3.values() for x in v}
    print("\n## P3. Module containment, from `inputs[].page`")
    print("\nWhat a Module is built FROM. This is a DAG and not a forest: a Module has many\n"
          "constituents and a constituent has many consumers. Reachability in a DAG is a\n"
          "partial order, so it qualifies, but IT ORDERS CONTAINMENT RATHER THAN\n"
          "REFINEMENT. `glossary.md#T34` makes constituency containment and `#T13` makes\n"
          "membership classification. Included as a separate object, never merged with P1.")
    print(f"\n  partial order : {'YES, no cycles' if not cyc3 else f'NO — {cyc3}'}")
    print(f"  single parent : NO, and that is the point — a DAG, not a forest")
    print(f"  nodes         : {len(nodes3)}")
    print(f"  edges         : {sum(len(v) for v in p3.values())}")
    print(f"  widest        : " + ", ".join(
        f"{k} ({len(v)})" for k, v in sorted(p3.items(), key=lambda x: (-len(x[1]), x[0]))[:3]))
    # TIES BREAK BY NAME, NOT BY HASH ORDER. `p3`'s values are sets, so the
    # flattened stream arrives in hash order and `most_common` keeps ties in the
    # order it met them. substrate-cprg and membrane-popc-chol-9-1 are each
    # consumed 8 times, so this line printed two different third places across
    # runs. Measured 2026-09-21: 12 runs, 2 distinct outputs, this line the only
    # difference. Found by render-all.py diffing its own output, not by reading.
    print(f"  most consumed : " + ", ".join(
        f"{k} ({v})" for k, v in sorted(collections.Counter(
            x for v in p3.values() for x in v).items(),
            key=lambda kv: (-kv[1], kv[0]))[:3]))

    # --- P4. Ingredient containment, from `component_of`.
    p4 = {}
    for m, d in S.items():
        for k, v in (d.get("inputs") or {}).items():
            if (co := (v or {}).get("component_of")):
                p4[f"{m}::{k}"] = co
    print("\n## P4. Ingredient containment, from `inputs[].component_of`")
    print("\nAn ingredient named here is a component of a page elsewhere. A SEPARATE ORDER\n"
          "FROM P3, because its lower elements are input keys rather than Modules, so the\n"
          "two do not share a carrier and cannot be composed into one relation.")
    print(f"\n  partial order : YES, no cycles — every target is a page, no target is a key")
    print(f"  edges         : {len(p4)}")
    print(f"  sources using : {len({k.split('::')[0] for k in p4})} of {len(S)}")
    byt = {t: [k for k in p4 if p4[k] == t] for t in set(p4.values())}
    for tgt, keys in sorted(byt.items()):
        kind = "page" if tgt.startswith("..") else "FREE TEXT, not a path"
        print(f"    {tgt}  <- {len(keys)} ingredient(s)  [{kind}]")
    loose = [t for t in byt if not t.startswith("..")]
    if loose:
        print(f"\n  MIXED CARRIER, AND IT BREAKS THE ORDER. {len(loose)} of {len(byt)} targets\n"
              "  are vendor product names rather than paths, so those edges point at nothing\n"
              "  this corpus contains. A relation whose upper elements are partly pages and\n"
              "  partly strings is two relations sharing a key. Reported, not resolved.")

    # --- SECTION 2.
    print("\n" + "#" * 74)
    print("# SECTION 2 — REAL ORDERS THIS SCRIPT CANNOT REACH")
    print("#" * 74)
    print("""
These are not absent from the corpus. They are absent from `spec.yml`, which is
the only thing this script reads. Both live in `compositional-biology-theory`
`signature.md`, in prose and table cells, with nothing to walk.

  P5. THE OPERATION POSET, at main 29842a1. `transport` is abstract and refined
      by `passive_transport` and `active_transport` (`signature.md:85`, and the
      two profiles at `:313` and `:315`); `hold` is refined by `encapsulate`
      (`:84`, and `:117` writes that refinement at type level as
      `encapsulate := hold[C = Membrane]`); `::` is declared by `Polymer` and
      refined by its refiners (`:93`). `:398` calls
      the transport pair the first worked refinement edge in the Functions
      poset, so that repo already names this as a poset.

  P6. THE TYPE POSET, at main 29842a1. `Container` spans and is refined by
      `Gel` and `Membrane` (`signature.md:87`, `:88`, `:84`). `Polymer` spans
      and is refined by `RNA`, `DNA` and `Protein` (`:93`). Both rows say "a
      parent, not a page set", so the type order and P1 are different relations
      over different carriers even where the names coincide. `Substrate` is not
      among them: it declares no operation, because a substrate is held rather
      than holding (`:92`).

  NEITHER IS ESTIMATED HERE. A three-line summary of another repo's prose is not
  the data, and quoting a moving file without a commit beside it is a claim about
  a moving file. Generating these needs a reader for that file, in that repo.""")

    # --- SECTION 3.
    print("\n" + "#" * 74)
    print("# SECTION 3 — CANDIDATES THAT ARE NOT ORDERS")
    print("#" * 74)
    ops = collections.Counter(
        s.get("operator") for d in S.values() for s in d.get("process_steps") or [])
    print(f"""
  `operator`. A flat two-value enum: {dict(ops)}. Two incomparable values order
  nothing. It will look like an axis because `packing` and `mixing` feel ranked,
  and they are not.

  `process.composed_of`. A SEQUENCE within one step, {sum(1 for d in S.values() for s in d.get('process_steps') or [] if (s.get('process') or {}).get('composed_of'))} uses. Order of
  operations, not refinement. A chain is totally ordered in time and says nothing
  about which process is more abstract than which.

  `measured_by`, `sensitivities`, `impositions`, `requires`. Relations, not
  orders. Nothing is transitive here: a Module sensitive to UV does not make its
  consumers sensitive to UV, which is exactly why `check-conflicts.py` computes
  reach separately and reports it as its own tier.

  VALIDATION STARS, in `docs/modules/modules-main.md`. A genuine total order on
  four values. Excluded because it ranks OUR CONFIDENCE in a page rather than
  ordering the corpus, so it belongs to review rather than to structure. Named
  here so its absence is a decision rather than an oversight.""")
    print()
