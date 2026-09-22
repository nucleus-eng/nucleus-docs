#!/usr/bin/env python3
"""Render a module's spec.yml to a Mermaid flowchart.

Reads the machine-readable composition source (#248) and writes the diagram
into the `gen:composition-diagram` markers on that module's spec.md (#249).
Idempotent: re-running with no source change rewrites the same block.

This is the only generator that may write those markers here. A second one,
`gen-module-diagrams.py` in `nucleus-skills`, derives its graph from the
`# Constituent Modules` bullet list and writes the same markers, so running it
against this repository reverts every page to a parts list. Issue #250 closed
on 2026-09-21 by naming this script rather than merging the two.

Follows the house style in the `mermaid-diagrams` skill:
  - Modules are boxes, processes are stadiums `([...])`. Never diamonds or
    hexagons: a diamond reads as a decision point.
  - Grayscale. Two shades — lighter for leaves, darker for things built from
    other things. Shape already separates modules from processes, so color
    would be encoding nothing.
  - Ids are UPPER_SNAKE, derived mechanically, never taken from prose.
  - Arrows run from constituent to container.
  - No status claims. `-->` only. `-.->` and `--x` mean "proposed" and
    "blocked", so using either decoratively asserts something unchecked.

Depth. A module page shows `--depth 1` by default: anything you can obtain is a
leaf, and only what this module builds on the way to its own result is
expanded. Base Cytosol is a leaf at depth 1 for the same reason S30 Lysate is —
it is a thing you can have, and its own page says how. `--depth 2` follows each
leaf's own spec.yml where one exists, and so on. Deeper renders are for
review material, not for module pages.

    python3 scripts/render-composition.py docs/modules/london-cascade/spec.yml
    python3 scripts/render-composition.py <path>/spec.yml --embed
    python3 scripts/render-composition.py <path>/spec.yml --depth 3
"""
import collections
import re
import sys
from pathlib import Path

import yaml

STYLE = """
    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
"""


def node_id(slug: str) -> str:
    return re.sub(r"[^A-Za-z0-9]", "_", slug).upper()


def esc(s: str) -> str:
    return s.replace('"', "'")


def click_path(page: str | None) -> str | None:
    """`../s30-lysate/spec.md` -> `/docs/modules/s30-lysate/spec`.

    Matches the form the existing generated diagrams already use.
    """
    if not page:
        return None
    p = re.sub(r"\.md$", "", page)
    p = re.sub(r"^\.\./\.\./", "/docs/", p)
    p = re.sub(r"^\.\./", "/docs/modules/", p)
    return p


def chain(step: dict) -> list[dict]:
    """The processes a step runs, in order. Usually one."""
    return step["process"].get("composed_of") or [step["process"]]


def expand(doc: dict, depth: int, root: Path, only: set[str] | None = None,
           seen: set[str] | None = None) -> dict:
    """Splice each leaf's own spec.yml in, `depth - 1` times over.

    `only` names the modules that may expand, by directory name. `--depth` alone
    is a moving target: it expands whatever happens to have a source that week,
    so the same command drew 5 process nodes for London in September and 13
    today, purely because the corpus grew from 17 sources to 56. A diagram whose
    shape changes when an unrelated module gains a `spec.yml` cannot be reissued.
    Naming the module makes the command reproducible.

    A leaf qualifies if it names a module page and that module has a source of
    its own. Its final step produces the leaf, so that product is renamed to
    the id the parent already uses and the two graphs join at one node.
    """
    if depth <= 1:
        return doc
    # SPLICE EACH MODULE ONCE, ACROSS THE WHOLE RECURSION AND NOT PER LEVEL.
    # Two sensor cytosols both take base-cytosol, so before 2026-09-21 Chicago
    # drew THREE "Assemble Base Cytosol" stadiums with identical operands, all
    # arrowing into one Base Cytosol box. That reads as the step running three
    # times. It does not: one Module was expanded once per parent that consumes
    # it. The product node carries the parent's key either way, so skipping the
    # repeat leaves every edge pointing where it already pointed.
    if seen is None:
        seen = set()
    inputs = dict(doc.get("inputs") or {})
    steps = list(doc["process_steps"])
    for key, v in list(inputs.items()):
        page = v.get("page")
        if not page:
            continue
        sub_path = (root / page).resolve().parent / "spec.yml"
        if not sub_path.is_file():
            continue
        if only is not None and sub_path.parent.name not in only:
            continue
        if sub_path.parent.name in seen:
            continue
        seen.add(sub_path.parent.name)
        sub = expand(yaml.safe_load(sub_path.read_text()), depth - 1,
                     sub_path.parent, only, seen)
        # A SOURCE MAY COMPOSE NOTHING, and this crashed on the first one.
        # `minItems: 1` came off `process_steps` on Jon's ruling, 2026-09-20,
        # and eight sources now name inputs and run no step. There is no
        # sub-graph to splice: the module IS a leaf however deep you ask, so it
        # stays an input rather than becoming an empty expansion.
        if not (sub.get("process_steps") or []):
            continue
        # The leaf stops being an input; the sub-graph produces it instead.
        del inputs[key]
        produced = sub["process_steps"][-1]["produces"]["id"]
        for s in sub["process_steps"]:
            if s["produces"]["id"] == produced:
                s["produces"] = {**s["produces"], "id": key}
            s["operands"] = [key if o == produced else o for o in s["operands"]]
        inputs.update(sub.get("inputs") or {})
        steps = sub["process_steps"] + steps
    return {**doc, "inputs": inputs, "process_steps": steps}


def render(doc: dict) -> str:
    L = ["flowchart TD"]
    leaves, composed, procs, clicks = [], [], [], []

    def declare(nid, label, page, bucket, shape="box"):
        body = f'(["{esc(label)}"])' if shape == "stadium" else f'["{esc(label)}"]'
        L.append(f"    {nid}{body}")
        bucket.append(nid)
        if (c := click_path(page)):
            clicks.append((nid, c))

    for key, v in (doc.get("inputs") or {}).items():
        declare(node_id(key), v["title"], v.get("page"), leaves)

    L.append("")
    for i, s in enumerate(doc["process_steps"], 1):
        pn = f"P{i}_{node_id(s['id'])}"
        # The operator rides on the process node, because it is a property of
        # the process rather than of any one edge.
        # A step may run a chain of processes. Each gets its own node, so each
        # keeps its own page link — a node takes only one click target.
        for k, sub in enumerate(chain(s)):
            # The step's operator belongs to whichever sub-process performs the
            # composition, which is the first unless one says otherwise. A later
            # link in the chain that composes nothing shows no operator, which
            # is the honest reading rather than a borrowed one.
            op = sub.get("operator", s["operator"] if k == 0 else None)
            # A STEP MAY BE HETEROGENEOUS, and until 2026-09-21 this drew it as
            # though it were not. `operator_pairs` lists the pairs that take the
            # OTHER operator, so any entry means the single label above is the
            # default rather than the whole claim, and a node showing only the
            # default asserts something the source does not.
            #
            # WHICH pairs is not drawable here. An arrow into a process node
            # carries no operator, which is the same reason the operator sits on
            # the node at all. The count is the honest summary and points a
            # reader at the spec.yml for the pairs themselves.
            if op and k == 0 and (ov := s.get("operator_pairs") or []):
                by = collections.Counter(o.get("operator") for o in ov)
                op += "".join(f", {n} pairs {name}" for name, n in sorted(by.items()))
            label = f'{sub["title"]} ({op})' if op else sub["title"]
            # "no page" is stated in words. A dashed border would say
            # "proposed", a status claim this diagram has not checked.
            if not sub.get("page"):
                label += " — no page"
            declare(f"{pn}_{k}", label, sub.get("page"), procs, shape="stadium")
        out = s["produces"]
        declare(node_id(out["id"]), out["title"], out.get("page"), composed)

    L.append("")
    for i, s in enumerate(doc["process_steps"], 1):
        pn = f"P{i}_{node_id(s['id'])}"
        n = len(chain(s))
        # Operands feed the first process; the chain runs; the last produces.
        for op in s["operands"]:
            L.append(f"    {node_id(op)} --> {pn}_0")
        for k in range(n - 1):
            L.append(f"    {pn}_{k} --> {pn}_{k + 1}")
        lbl = f'|"{s["ratio"]}"|' if s.get("ratio") else ""
        L.append(f'    {pn}_{n - 1} -->{lbl} {node_id(s["produces"]["id"])}')
        L.append("")

    # `measured_by` is deliberately not drawn. It produces no Module, so a plain
    # edge would read as composition, and a dashed one would assert status.

    L.append(STYLE.rstrip("\n"))
    for name, ids in (("leaf", leaves), ("composed", composed), ("process", procs)):
        if ids:
            L.append(f"    class {','.join(ids)} {name};")
    L.append("")
    L += [f'    click {n} "{p}"' for n, p in clicks]
    return "\n".join(L)


BEGIN = "<!-- gen:composition-diagram -->"
END = "<!-- /gen:composition-diagram -->"


def page_block(mermaid: str) -> str:
    """The tab-item the docs page carries, wrapped in the idempotency markers.

    Plain ```mermaid fence: the directive form renders blank in Obsidian, and
    this repo is 18 plain to 2 directive.
    """
    return (f"{BEGIN}\n::::{{tab-item}} Module Dependencies\n\n"
            f"```mermaid\n{mermaid}\n```\n\n::::\n{END}")


def embed(spec: Path, mermaid: str) -> bool | None:
    """Rewrite the marked block. None if the page carries no markers.

    A page with a composition source but no markers is a real finding, not a
    crash: it means nobody decided where its diagram goes.
    """
    t = spec.read_text()
    if BEGIN not in t or END not in t:
        return None
    i, j = t.index(BEGIN), t.index(END) + len(END)
    new = t[:i] + page_block(mermaid) + t[j:]
    if new == t:
        return False
    spec.write_text(new)
    return True


if __name__ == "__main__":
    src = Path(sys.argv[1])
    depth = 1
    if "--depth" in sys.argv:
        depth = int(sys.argv[sys.argv.index("--depth") + 1])
    # --expand NAME, repeatable. Implies a depth deep enough to reach them, so
    # the two flags do not have to agree by hand.
    only = {sys.argv[i + 1] for i, a in enumerate(sys.argv) if a == "--expand"}
    if only:
        depth = max(depth, len(only) + 1)
    doc = expand(yaml.safe_load(src.read_text()), depth, src.parent,
                 only or None)
    mermaid = render(doc)
    if "--embed" in sys.argv:
        spec = src.parent / "spec.md"
        r = embed(spec, mermaid)
        verdict = {None: "NO MARKERS — nowhere to put it",
                   True: "updated", False: "unchanged"}[r]
        print(f"{verdict}: {spec}")
    else:
        print(mermaid)
