#!/usr/bin/env python3
"""Compute the meet of several demo legs and draw it.

Implements the spec in compositional-biology-theory
tmp/STAGED-2026-09-21-what-the-meet-renderer-must-compute.md, written by session
c9d6a5 and handed to this repo. Their four rules are the deliverable; this is
the implementation.

THE DELTA FROM render-composition.py IS ARITY, NOT FEATURES. That script's input
is a module and it draws one graph. A meet's input is a SET OF LEGS, and every
computation here exists because the second has no meaning for the first. The
house style, the shapes, the click targets and the "— no page" wording are
reused unchanged.

    python3 scripts/render-meet.py docs/modules/london-cascade/spec.yml \
                                   docs/modules/chicago-cascade/spec.yml

FOUR RULES, each with the measurement that forced it.

1. A LEG IS NOT A FILE, AND THE PARTITION KEY IS THE DETECTOR. chicago-cascade
   holds two legs and london-cascade holds one. Walking back from each operand of
   the final step is right for Chicago, whose `bond-gels` has two operands that
   separate the paths, and wrong for London, whose `embed-ulga` has five and would
   give five branches. A leg is a branch reaching exactly one detector.

   THE REACH SCANS THREE FIELDS, AND ONLY TWO OF THEM STILL EARN IT. Measured by
   disabling each in turn at this commit:

     inputs[].page          LOAD-BEARING. Without it London finds no detector at all
                            and Chicago finds one instead of two.
     produces.page          LOAD-BEARING. ph-cascade BUILDS its detector at
                            anneal-trigger-duplex rather than being handed one.
     inputs[].component_of  DEAD FOR LEGS, LOAD-BEARING FOR OPERAND SLOTS. Removing
                            it changes no leg in any cascade, and it is the only route
                            by which chicago-cascade's ph-responsive-ssdna and
                            trigger-ssdna reach detector-ph when the operands are
                            slotted. One field, two passes, opposite answers.

   THE SPEC SAID component_of WAS THE ONLY ROUTE TO CHICAGO'S pH DETECTOR. That was
   true of leg extraction at 1522a3b and stopped being true when ph-trigger-duplex
   gained `refines: detector`, because it is a product and the produces route reaches
   it first. I recorded the field as exercised by nothing on that measurement, and
   slotting the operands falsified it within the hour: two of Chicago's operands reach
   the detector through component_of and through nothing else. The lesson is the
   narrower claim rather than the field — a route can be dead on one pass and the only
   route on another, so "exercised by nothing" needs to say by which pass.

2. SLOTS ALIGN BY THE PRODUCT'S CLASS, NOT BY PROCESS TITLE OR BY `abstract:`.
   Title fails after three steps: the Chicago legs share three processes and then
   diverge by design. `abstract:` is too coarse and merges the outer-solution slot
   with the cytosol slot, because assemble-aqueous-solution sits on both.

3. A NODE IS ABSTRACT IFF THE LEGS DISAGREE. Jon's rule: "we should only be using
   abstract pages when there's a design decision to be made between different
   implementations." Where the legs agree the meet IS that module and labelling it
   abstract asserts a choice nobody has.

   ABSTRACTNESS DOES NOT PROPAGATE ALONG EDGES. Seven of seven sensing-cell steps
   run Encapsulation: Phase Transfer, so that process node is concrete while every
   module flowing into it may be abstract.

4. RESOLVE EVERY OPERAND TO ITS PAGE, NEVER TO ITS KEY. `membrane-chicago` and
   `membrane-popc-chol-chicago` name one module, so a key-based walk reaches it
   twice and marks a slot abstract where the legs in fact agree. That failure
   manufactures a design decision rather than hiding one.

MARK, DO NOT FAIL, on four existing advisory checkers. A slot whose legs differ
with no common ancestor draws a marked node and the run still succeeds; --strict
fails on it. The marker is kept from reading as a class by printing the
denominators every run, not by the exit code.
"""
import collections
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent / "docs" / "modules"

STYLE = """
    classDef concrete fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef abstract fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    classDef unmet    fill:#ffffff,stroke:#111827,color:#111827,stroke-dasharray:0;
    classDef partial  fill:#ffffff,stroke:#6b7280,color:#6b7280;
"""


def load_sources() -> dict[str, dict]:
    out = {}
    for d in sorted(ROOT.iterdir()):
        f = d / "spec.yml"
        if f.is_file():
            out[d.name] = yaml.safe_load(f.read_text()) or {}
    return out


def to_module(page: str | None) -> str | None:
    """A page path to the module it names. RULE 4 lives here: every operand goes
    through this before it is counted, so two keys for one module collapse."""
    if not page:
        return None
    m = re.match(r"\.\./([^/]+)/spec\.md$", page)
    return m.group(1) if m else None


def parents(S: dict) -> dict[str, str]:
    return {m: d["refines"] for m, d in S.items() if d.get("refines")}


def ancestors(slug: str, par: dict) -> list[str]:
    """Self first, then up. A node is its own ancestor, so where legs agree the
    meet is that node rather than its parent."""
    out, seen = [], set()
    while slug and slug not in seen:
        out.append(slug); seen.add(slug); slug = par.get(slug)
    return out


def meet(slugs, par: dict) -> str | None:
    """Deepest common ancestor, or None for no common ancestor at all. None is a
    failure marker and must never collapse into a root."""
    chains = [ancestors(s, par) for s in slugs]
    if not chains:
        return None
    for cand in chains[0]:
        if all(cand in c for c in chains[1:]):
            return cand
    return None


def is_detector(mod: str | None, par: dict) -> bool:
    return bool(mod) and "detector" in ancestors(mod, par)


def operand_module(src: dict, key: str, S: dict, par: dict) -> str | None:
    """RULE 1's three fields, in one place. An operand key resolves through its
    own `page`, then through `component_of`, then through whatever step produced
    it. Each field is the only route for at least one source."""
    v = (src.get("inputs") or {}).get(key) or {}
    if (m := to_module(v.get("page"))):
        return m
    if (m := to_module(v.get("component_of"))):
        return m
    for s in src.get("process_steps") or []:
        if s["produces"]["id"] == key:
            return to_module(s["produces"].get("page")) or key
    return None


def legs_of(name: str, S: dict, par: dict) -> dict[str, list[dict]]:
    """Partition one source's steps by the detector each reaches. RULE 1."""
    src = S[name]
    reach: dict[str, set[str]] = {}
    for key in (src.get("inputs") or {}):
        m = operand_module(src, key, S, par)
        reach[key] = {m} if is_detector(m, par) else set()
    steps_by_leg: dict[str, list[dict]] = collections.defaultdict(list)
    shared: list[dict] = []
    for s in src.get("process_steps") or []:
        got: set[str] = set()
        for o in s["operands"]:
            got |= reach.get(o, set())
        pm = to_module(s["produces"].get("page"))
        if is_detector(pm, par):
            got |= {pm}
        reach[s["produces"]["id"]] = got
        (steps_by_leg[next(iter(got))] if len(got) == 1 else shared).append(s)
    if shared:
        steps_by_leg["__join__"] = shared
    return dict(steps_by_leg)


def slot_key(mod: str | None, par: dict) -> str:
    """RULE 2. Two products share a slot when they are the same module or share an
    immediate parent. An unsourced product keys to itself and aligns with nothing,
    which is a finding rather than a merge."""
    return par.get(mod, mod) if mod else "__unresolved__"


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    strict = "--strict" in sys.argv
    S = load_sources()
    par = parents(S)

    # --- legs
    legs: dict[str, tuple[str, list[dict]]] = {}
    for a in args:
        name = Path(a.rstrip("/")).parent.name if a.endswith(".yml") else Path(a).name
        for det, steps in legs_of(name, S, par).items():
            if det == "__join__":
                continue
            legs[f"{name}:{det}"] = (name, steps)

    if not legs:
        print("no legs found — every branch reached zero or many detectors",
              file=sys.stderr)
        sys.exit(2)

    # --- slots
    #
    # A SLOT IS FILLED BY WHATEVER OCCUPIES THAT POSITION, WHICH IS NOT ALWAYS A
    # PRODUCT. The pH leg BUILDS its detector at anneal-trigger-duplex; the other two
    # are SUPPLIED as inputs. A product-only pass sees one detector and calls the slot
    # concrete, which is the alias failure in a different costume: it reports agreement
    # where the legs in fact differ. So the detector slot is taken from the partition
    # keys, which already name one detector per leg by construction.
    #
    # AND THE OUTCOME SLOT IS STRUCTURAL RATHER THAN SEMANTIC. Each leg's terminal
    # product is that leg's answer, whatever its class, so the three align by position.
    # Keying them by class instead gave three concrete boxes, each asserting that the
    # legs agree, when what is true is that no Cascade class exists to meet them at.
    slots: dict[str, dict[str, str]] = collections.defaultdict(dict)
    order: list[str] = []

    def put(key: str, leg: str, member: str) -> None:
        if key not in slots:
            order.append(key)
        slots[key][leg] = member

    for leg in legs:
        put("detector", leg, leg.split(":", 1)[1])

    # CHANGE A, 2026-09-21, on c9d6a5's addendum. THE OPERANDS ARE SLOTS TOO, and
    # slotting only products drew the spine and nothing hanging off it: no membrane,
    # no gel, no outer solution, no effector. Five slots where a hand-drawn meet had
    # fifteen nodes.
    #
    # AND THE OPERANDS MUST GO THROUGH operand_module. This script defined that
    # function for leg extraction and then read produces.page directly here, which is
    # the bug they found by reading the code rather than the docstring. Resolving an
    # operand by key or by inputs[].page alone makes Chicago's pH detector unreachable:
    # ph-responsive-ssdna and trigger-ssdna reach it through component_of, and
    # ph-trigger-duplex through the step that builds it. The slot would then report NO
    # COMMON ANCESTOR for a class that exists, which is worse than missing the slot.
    #
    # THIS IS WHERE component_of EARNS ITS PLACE. It is dead for leg extraction,
    # measured, and load-bearing here. One field, two passes, opposite answers.
    produced_by: dict[tuple[str, str], dict] = {}
    agree_checks = 0
    for leg, (src_name, steps) in legs.items():
        src = S[src_name]
        for s in steps:
            mod = to_module(s["produces"].get("page")) or s["produces"]["id"]
            produced_by[(leg, mod)] = s
        if not steps:
            continue
        for s in steps[:-1]:
            mod = to_module(s["produces"].get("page"))
            if is_detector(mod, par):
                continue
            put(slot_key(mod, par) if mod else s["produces"]["id"],
                leg, mod or s["produces"]["id"])
        last = steps[-1]
        put("__outcome__", leg,
            to_module(last["produces"].get("page")) or last["produces"]["id"])
        for s in steps:
            for o in s["operands"]:
                m = operand_module(src, o, S, par)
                if m is None or is_detector(m, par):
                    continue          # unresolvable, or already in the detector slot
                k = slot_key(m, par)
                # A FREE POSITIVE CONTROL, c9d6a5's, AND IT ONLY WORKS IN THIS ORDER.
                # A module that is a product of one step and an operand of the next
                # must land in the same slot from both passes. The product pass runs
                # first for exactly this reason: run the operand pass first and the
                # check compares against an empty dict and reports zero, which reads
                # like a result and is an ordering bug.
                if (leg, m) in produced_by and k in slots and slots[k].get(leg) == m:
                    agree_checks += 1
                put(k, leg, m)

    # CHANGE B: MEET THE PROCESSES, LINK BY LINK. A step may run a chain, and the
    # chains align on their first link. The three encapsulate steps all begin with
    # Encapsulation: Phase Transfer; the aTc leg carries a second link the others
    # lack, which is a cleanup obligation rather than a difference to average away.
    #
    # PROCESSES MEET IN THEIR OWN POSET, not the module one. A process's parent is
    # `process.abstract`, so the meet walks that map and a process with no parent keys
    # to itself.
    pproc: dict[str, str] = {}
    for d in S.values():
        for s in d.get("process_steps") or []:
            for pr in ((s.get("process") or {}).get("composed_of")
                       or [s.get("process") or {}]):
                pg, ab = pr.get("page") or "", pr.get("abstract")
                if pg and ab:
                    pproc[re.sub(r"/[^/]+$", "", pg).rsplit("/", 1)[-1]] = ab

    def proc_dir(pr: dict) -> str | None:
        pg = pr.get("page") or ""
        return re.sub(r"/[^/]+$", "", pg).rsplit("/", 1)[-1] if pg else None

    pslots: dict[str, dict[str, str]] = collections.defaultdict(dict)
    porder: list[str] = []
    for leg, (src_name, steps) in legs.items():
        for si, s in enumerate(steps):
            chain = ((s.get("process") or {}).get("composed_of")
                     or [s.get("process") or {}])
            for li, pr in enumerate(chain):
                d = proc_dir(pr) or (pr.get("title") or "untitled")
                k = f"proc:{slot_key(d, pproc)}:{li}"
                if k not in pslots:
                    porder.append(k)
                pslots[k][leg] = d

    # --- the meet per slot
    def nid_of(k: str) -> str:
        return re.sub(r"[^A-Za-z0-9]", "_", k).upper()

    L = ["flowchart TD"]
    # RULE: THE DOMAIN IS PART OF THE OUTPUT, NOT A CAPTION. A meet is only
    # defined against the legs it was taken over, so the leg list is a node.
    L.append(f'    DOMAIN["Meet over {len(legs)} legs, partitioned by detector:'
             f'<br/>{"<br/>".join(sorted(legs))}"]')
    L.append("")
    concrete, abstract, unmet, partial, procs = [], [], [], [], []
    tally = collections.Counter()
    for k in order:
        members = sorted({v for v in slots[k].values()})
        label_for = {"__outcome__": "the demo each leg produces",
                     "detector": "the sensing element"}.get(k, "")
        nid = nid_of(k)
        # A CONCRETE BOX MEANS EVERY LEG IN THE DOMAIN USES THIS EXACT MODULE.
        # A slot only some legs fill has one member for a different reason, and
        # painting it concrete reports agreement among legs that never met. That is
        # the same error as the three cascade roots, one category down.
        if len(slots[k]) < len(legs):
            got = len(slots[k])
            L.append(f'    {nid}["{", ".join(members)}<br/>'
                     f'only {got} of {len(legs)} legs have this slot"]')
            partial.append(nid); tally["partial"] += 1
        elif len(members) == 1:
            m = members[0]
            title = (S.get(m) or {}).get("title", m)
            L.append(f'    {nid}["{title}"]')
            concrete.append(nid); tally["concrete"] += 1
            if m in S:
                L.append(f'    click {nid} "/docs/modules/{m}/spec"')
        elif (mt := meet(members, par)):
            title = (S.get(mt) or {}).get("title", mt)
            L.append(f'    {nid}["{title}<br/>({", ".join(members)})"]')
            abstract.append(nid); tally["abstract"] += 1
            if mt in S:
                L.append(f'    click {nid} "/docs/modules/{mt}/spec"')
        else:
            tag = f" — {label_for}" if label_for else ""
            L.append(f'    {nid}["NO COMMON ANCESTOR{tag}'
                     f'<br/>{", ".join(members)}"]')
            unmet.append(nid); tally["unmet"] += 1

    # PROCESS NODES, drawn as stadiums per the house style and classed by the same
    # three rules. ABSTRACTNESS DOES NOT PROPAGATE: a process every leg shares is
    # concrete even when every module flowing into it is abstract, which is why this
    # pass is separate rather than inherited from the operands.
    L.append("")
    for k in porder:
        members = sorted(set(pslots[k].values()))
        nid = nid_of(k)
        link = k.rsplit(":", 1)[1]
        tail = "" if link == "0" else f", link {int(link) + 1}"
        if len(pslots[k]) < len(legs):
            L.append(f'    {nid}(["{", ".join(members)}{tail}<br/>'
                     f'only {len(pslots[k])} of {len(legs)} legs run this"])')
            partial.append(nid); tally["proc_partial"] += 1
        elif len(members) == 1:
            L.append(f'    {nid}(["{members[0]}{tail}"])')
            procs.append(nid); tally["proc_concrete"] += 1
        elif (mt := meet(members, pproc)):
            L.append(f'    {nid}(["{mt}{tail}<br/>({", ".join(members)})"])')
            abstract.append(nid); tally["proc_abstract"] += 1
        else:
            L.append(f'    {nid}(["NO COMMON ANCESTOR{tail}'
                     f'<br/>{", ".join(members)}"])')
            unmet.append(nid); tally["proc_unmet"] += 1

    # EDGES ARE CONTAINMENT PROJECTED ONTO SLOTS. Slot A feeds slot B when, in some
    # leg, A's member is an operand of the step that produces B's member. An edge that
    # only one leg has is still drawn: the meet is over the union of what the legs do,
    # and dropping a leg's edge would assert the others do not do it.
    member_slot = {(leg, m): k for k in order for leg, m in slots[k].items()}
    edges: set[tuple[str, str]] = set()
    for leg, (src_name, _) in legs.items():
        src = S[src_name]
        for k in order:
            m = slots[k].get(leg)
            if m is None or (leg, m) not in produced_by:
                continue
            for o in produced_by[(leg, m)]["operands"]:
                om = operand_module(src, o, S, par) or o
                if (src_k := member_slot.get((leg, om))) and src_k != k:
                    edges.add((src_k, k))
    L.append("")
    for a, b in sorted(edges):
        L.append(f"    {nid_of(a)} --> {nid_of(b)}")

    L.append("")
    L.append(STYLE.rstrip("\n"))
    for nm, ids in (("concrete", concrete), ("abstract", abstract),
                    ("unmet", unmet), ("partial", partial),
                    ("process", procs)):
        if ids:
            L.append(f"    class {','.join(ids)} {nm};")
    print("\n".join(L))

    # --- denominators, every run. The marker is kept from reading as a class by
    # this, not by the exit code.
    n = sum(v for k, v in tally.items() if not k.startswith("proc_"))
    print(f"\npartition key: detector\n"
          f"{len(legs)} leg(s): {', '.join(sorted(legs))}\n"
          f"{n} slot(s): {tally['concrete']} concrete (legs agree), "
          f"{tally['abstract']} abstract (legs differ, class found), "
          f"{tally['unmet']} with NO COMMON ANCESTOR, "
          f"{tally['partial']} filled by only some legs\n"
          f"{sum(v for k, v in tally.items() if k.startswith('proc_'))} process slot(s): "
          f"{tally['proc_concrete']} concrete, {tally['proc_abstract']} abstract, "
          f"{tally['proc_unmet']} with NO COMMON ANCESTOR, "
          f"{tally['proc_partial']} run by only some legs\n"
          f"{agree_checks} product-and-operand agreement check(s) passed: a module that "
          f"is a product of one step and an operand of the next landed in the same slot "
          f"from both passes",
          file=sys.stderr)
    unsourced = sum(1 for k in order
                    for v in slots[k].values() if v not in S)
    print(f"{unsourced} product(s) across all legs resolve to no spec.yml, so they "
          f"align with nothing and cannot be met.\n"
          f"A marked slot is a finding about the sources, not about the design.",
          file=sys.stderr)
    if strict and (tally["unmet"] or tally["proc_unmet"]):
        sys.exit(1)
