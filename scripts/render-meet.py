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

    python3 scripts/render-meet.py docs/modules/luxr-lacz-cascade/spec.yml \
                                   docs/modules/atc-cascade/spec.yml

FOUR RULES, each with the measurement that forced it.

1. A LEG IS NOT A FILE, AND THE PARTITION KEY IS THE DETECTOR. Measured against a
   multiplex source that held two legs while luxr-lacz-cascade holds one: walking back
   from each operand of the final step was right for the multiplex, whose `bond-gels`
   had two operands that separated the paths, and wrong for London, whose
   `embed-ulga` has five and would give five branches. A leg is a branch reaching
   exactly one detector. The multiplex source was retired 2026-10-03 and the rule
   outlives it: a meet is now asked for its legs by name.

   THE REACH SCANS THREE FIELDS, AND ONLY TWO OF THEM STILL EARN IT. Measured by
   disabling each in turn at this commit:

     inputs[].page          LOAD-BEARING. Without it London finds no detector at all
                            and Chicago finds one instead of two.
     produces.page          LOAD-BEARING. ph-cascade BUILDS its detector at
                            anneal-trigger-duplex rather than being handed one.
     inputs[].component_of  DEAD FOR LEGS, LOAD-BEARING FOR OPERAND SLOTS. Removing
                            it changes no leg in any cascade, and it is the only route
                            by which ph-cascade's ph-responsive-ssdna and
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
   with the cytosol slot, because assemble-solution sits on both.

3. A NODE IS ABSTRACT IFF THE LEGS DISAGREE. An abstract page earns its place
   only where there is a design decision to be made between implementations.
   Where the legs agree the meet IS that module and labelling it
   abstract asserts a choice nobody has.

   ABSTRACTNESS DOES NOT PROPAGATE ALONG EDGES. Seven of seven sensing-cell steps
   run Encapsulation: Phase Transfer, so that process node is concrete while every
   module flowing into it may be abstract.

4. RESOLVE EVERY OPERAND TO ITS PAGE, NEVER TO ITS KEY. `membrane-chicago` and
   `membrane-popc-chol-9-1` name one module, so a key-based walk reaches it
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

# A CANDIDATE SET IS A BARE BRACE, NOT A PARENTHESIS, under the attachment rule: a brace attached to a type contains, a bare
# brace with commas is a set. `(…)` applies a morphism — glossary.md and
# signature.md:214 at main 29842a1 — so `Detector(pH Detector, tetR-aTc Detector)` parsed as
# applying Detector to two arguments. That was wrong before the brace sweep and
# the sweep did not cause it.
#
# The rule is a measurement, not an invention: 127 headed `X{…}` uses across
# nucleus-docs and compositional-biology-theory, zero of them containing a comma.
#
# Three sites carry it, all of them a meet title over its members. The four that
# emit a bare comma-separated list with no wrapper were already the set form.

STYLE = """
    classDef concrete fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef abstract fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    classDef unmet    fill:#ffffff,stroke:#111827,color:#111827,stroke-dasharray:0;
    classDef partial  fill:#ffffff,stroke:#6b7280,color:#6b7280;
    classDef domain   fill:#ffffff,stroke:#6b7280,color:#6b7280,stroke-dasharray:4 3;
    classDef require  fill:#ffffff,stroke:#111827,color:#111827,stroke-width:3px;
    classDef impose   fill:#f3f4f6,stroke:#111827,color:#111827,stroke-width:3px;
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
    """One parent per module. A list aligns by its FIRST entry, and the source
    declares which that is.

    `refines:` may be a list since 2026-09-24. This function refused a list until
    2026-09-29, because `slot_key` below aligns two products when they share an
    immediate parent, and picking one of two arbitrarily makes two products align
    or not depending on which this function happened to keep.

    Aligning by the FUNCTIONAL parent removes the arbitrariness rather than the
    choice, on the reasoning that a chassis is what
    DIFFERS between two demos, so the axis they can be compared on is the other
    one. The convention that carries it is positional -- the first entry of the
    list is the alignment parent -- so the source states it and this function
    reads it. Nothing here sniffs a name to guess which parent is functional.

    A one-element list is still refused, because `minItems: 2` in the schema
    means it can only be a second spelling of the string form.
    """
    out = {}
    for m, d in S.items():
        r = d.get("refines")
        if not r:
            continue
        if isinstance(r, str):
            out[m] = r
            continue
        r = list(r)
        if len(r) < 2:
            raise ValueError(
                f"{m} refines {r}. A one-element list is a second spelling of the "
                "string form; the schema requires at least two entries.")
        out[m] = r[0]
    return out


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
    joins: dict[str, list[dict]] = {}
    asked: list[str] = []
    for a in args:
        name = Path(a.rstrip("/")).parent.name if a.endswith(".yml") else Path(a).name
        asked.append(name)
        for det, steps in legs_of(name, S, par).items():
            if det == "__join__":
                joins[name] = steps
            else:
                legs[f"{name}:{det}"] = (name, steps)

    # A CASCADE THAT CONTRIBUTES NO LEG IS REPORTED, NOT SWALLOWED. It warns and
    # does not refuse.
    #
    # The partition is by detector, so a cascade whose detector input carries
    # `page: null` resolves to nothing, produces only `__join__`, and adds no leg.
    # Before this, asking for four cascades and getting three printed "3 leg(s)",
    # exited 0, and never named the one that did not arrive -- which is the
    # false-clean shape this corpus has four recorded instances of in greps. The
    # run is still useful, so this warns and continues rather than refusing.
    contributed = {src for src, _ in legs.values()}
    dropped = [n for n in dict.fromkeys(asked) if n not in contributed]
    if dropped:
        print(
            "WARNING: %d of %d cascade(s) named on the command line contributed no leg "
            "and are absent from this meet:" % (len(dropped), len(dict.fromkeys(asked))),
            file=sys.stderr)
        for n in dropped:
            why = ("it resolves to no source" if n not in S
                   else "no step of it reaches a detector, so the partition key finds nothing "
                        "-- usually a detector input with `page: null`")
            print("  %s: %s" % (n, why), file=sys.stderr)

    # A STEP THAT REACHES NO DETECTOR IS SHARED, NOT ABSENT, AND DROPPING IT BROKE THE
    # DIAGRAM. The first Chicago draft drew both SUV: CPRG and CPRG substrate, and
    # a reader asked why both were in there.
    #
    # Because encapsulate-substrate-suv, the step that MAKES the SUV out of
    # substrate-cprg and a membrane, reaches no detector and went to __join__, which
    # this loop then threw away. So substrate-cprg appeared via the aTc leg's dosing
    # step, substrate-cprg-suv appeared via the pH leg's embed step, and the edge
    # showing that one is made from the other was gone. Two nodes that look unrelated
    # and are not.
    #
    # THE REAL DIFFERENCE SURVIVES THE FIX AND IS WORTH SEEING. The aTc leg doses CPRG
    # free into the set gel; the pH leg encapsulates it first. That is
    # color-change's own axis, "what varies across the class is which component is
    # encapsulated", showing up in a meet. Two slots is the right answer; two
    # DISCONNECTED slots was not.
    #
    # A join step is attributed to every leg that consumes its product, to fixpoint,
    # because a join step can feed another join step.
    for src_name, steps in joins.items():
        mine = {k: v for k, v in legs.items() if v[0] == src_name}
        for _ in range(len(steps) + 1):
            for s in steps:
                pid = s["produces"]["id"]
                pm = to_module(s["produces"].get("page")) or pid
                for leg, (_, lsteps) in mine.items():
                    if any(o == pid or operand_module(S[src_name], o, S, par) == pm
                           for ls in lsteps for o in ls["operands"]):
                        if s not in lsteps:
                            lsteps.insert(0, s)

    if not legs:
        print("no legs found — every branch reached zero or many detectors",
              file=sys.stderr)
        sys.exit(2)

    # --- P1 and P2: what each leg INFLICTS and what it REQUIRES
    #
    # D3 ruled that both are nodes with a heavy border rather than edges, because an
    # edge-relation must compose and joint consistency does not. So they are drawn as
    # nodes here and connected to the process they constrain.
    #
    # TWO KEYS, AND THEY ARE NOT THE SAME SHAPE. `impositions:` is one-sided: a step
    # inflicts one quantity, bounded by a property of one of its operands (#T22, an
    # Imposition is a property of a morphism). `requires:` is a condition that must
    # hold for the step to be defined (#T20). Q1 ruled the spec wins over the hand
    # figure, so this draws what is declared and nothing more.
    #
    # THE CLASS INVARIANT IS INHERITED, NOT COPIED ONTO EACH LEG. IQ4n (a). Separation
    # of enzyme from substrate is true of every colorimetric reporter, so it is
    # declared once on color-change and reached from a leg that realizes the pairing.
    #
    # AND THE `refines:` CHAIN IS NOT HOW IT IS REACHED, though IQ4n's wording offered
    # it first. Measured: every cascade's reporter operand is reporter-lacz-enzyme,
    # which refines `lacz`, and `lacz` refines nothing. No leg reaches color-change
    # that way. What does reach it is the OTHER walk the same proposal named, the one
    # check-spec-schema.py's substrate_findings uses: an operand whose `substrates:`
    # list, its own or the nearest one up its chain, names another operand of the same
    # leg. That fires on all four cascades.
    def _refines(m: str) -> list[str]:
        r = S.get(m, {}).get("refines")
        return [r] if isinstance(r, str) else list(r or [])

    def substrates_of(m: str, seen: frozenset = frozenset()) -> list | None:
        """m's own `substrates:` list, else the nearest one up its `refines:` chain."""
        if m in seen:
            return None
        if S.get(m, {}).get("substrates") is not None:
            return S[m]["substrates"]
        for parent in _refines(m):
            if (got := substrates_of(parent, seen | {m})) is not None:
                return got
        return None

    def pairing_class_of(mods: set[str]) -> str | None:
        """The class a set of modules realizes by holding an enzyme and one of its
        substrates. None when no pair is present, which is not a finding: a leg with
        no colorimetric readout inherits no colorimetric requirement."""
        for m in mods:
            if (subs := substrates_of(m)) is None:
                continue
            named = {to_module(e.get("page")) or e.get("title") for e in subs}
            if mods & {x for x in named if x}:
                for cls in ("color-change",):
                    if cls in S:
                        return cls
        return None

    def bound_text(i: dict) -> str:
        b = i.get("bound") or {}
        if not b:
            return i["id"]
        frm = b.get("from") or {}
        sense = {"at-least": "≥", "at-most": "≤", "equal": "="}.get(b.get("sense"), b.get("sense"))
        src_key = f"{frm.get('operand')}.{frm.get('key')}" if frm else "?"
        return f"{i['id']}: {b.get('quantity')} {sense} {src_key}"

    # id -> {leg: (label, step_id)}
    imps: dict[str, dict[str, tuple[str, str]]] = collections.defaultdict(dict)
    reqs: dict[str, dict[str, tuple[str, str]]] = collections.defaultdict(dict)
    inherited: dict[str, str] = {}
    for leg, (src_name, steps) in legs.items():
        src = S[src_name]
        for st in steps:
            for i in (st.get("impositions") or []):
                imps[i["id"]][leg] = (bound_text(i), st["id"])
            for r in (st.get("requires") or []):
                reqs[r["id"]][leg] = (r.get("notation") or r["id"], st["id"])
        mods = {operand_module(src, o, S, par) or o for st in steps for o in st["operands"]}
        mods |= {to_module(st["produces"].get("page")) or st["produces"]["id"] for st in steps}
        if (cls := pairing_class_of({m for m in mods if m})):
            for cst in (S[cls].get("process_steps") or []):
                for r in (cst.get("requires") or []):
                    # the leg's LAST step is where a class condition lands: it is the
                    # one that has to hold for the leg's own result to be defined.
                    reqs[r["id"]][leg] = (r.get("notation") or r["id"], steps[-1]["id"])
                    inherited[r["id"]] = cls

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
    def member_slot_of(leg: str, m: str) -> str | None:
        for kk in order:
            if slots[kk].get(leg) == m:
                return kk
        return None

    # A PRODUCED ID WITH NO PAGE STILL HAS A TITLE, on the step that makes it. Falling
    # back to the slug there leaked `outer-solution` and `chicago-outer-solution` into
    # figures that named everything else properly.
    id_titles: dict[str, str] = {}
    for d in S.values():
        for s in d.get("process_steps") or []:
            pr = s["produces"]
            id_titles.setdefault(pr["id"], pr.get("title") or pr["id"])
    proc_titles: dict[str, str] = {}
    for d in S.values():
        for s in d.get("process_steps") or []:
            for pr in ((s.get("process") or {}).get("composed_of")
                       or [s.get("process") or {}]):
                pg = pr.get("page") or ""
                if pg and pr.get("title"):
                    proc_titles.setdefault(
                        re.sub(r"/[^/]+$", "", pg).rsplit("/", 1)[-1], pr["title"])

    def title_of(m: str) -> str:
        """A node shows the page's title, never its slug. A slug is an address; a title is
        what the page calls itself, and a figure is read by people."""
        if m in S:
            return S[m].get("title", m)
        return id_titles.get(m, m)

    def shared_tail(titles: list[str]) -> str | None:
        """The trailing word every title shares, or None.

        THIS IS MEASURED, NOT COINED. The spec forbids inventing a parent name for a
        slot with no common ancestor, and it is right to. But "LuxR-LacZ Sensor Cascade", "aTc
        Cascade" and "pH Cascade" share the word Cascade in the titles their own pages
        carry, so reporting it states what the corpus already says rather than naming a
        class nobody wrote. The node still leads with the warning.
        """
        words = [x.split() for x in titles]
        if len(words) < 2 or not all(words):
            return None
        tail = words[0][-1]
        return tail if all(w[-1] == tail for w in words) else None

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
        shown = [title_of(m) for m in members]
        label_for = {"__outcome__": "the demo each leg produces",
                     "detector": "the sensing element"}.get(k, "")
        nid = nid_of(k)
        # A CONCRETE BOX MEANS EVERY LEG IN THE DOMAIN USES THIS EXACT MODULE.
        # A slot only some legs fill has one member for a different reason, and
        # painting it concrete reports agreement among legs that never met. That is
        # the same error as the three cascade roots, one category down.
        if len(slots[k]) < len(legs):
            # A PARTIAL SLOT CAN STILL BE A MEET. The legs that DO fill it may put
            # different modules in it, and naming the class they meet at is the whole
            # payoff of having written one. Without this the label listed two members
            # and hid the fact that they now have a parent.
            got = len(slots[k])
            head = ", ".join(shown)
            if len(members) > 1 and (mt := meet(members, par)):
                head = f'{title_of(mt)}<br/>{{{head}}}'
            L.append(f'    {nid}["{head}<br/>'
                     f'only {got} of {len(legs)} legs have this slot"]')
            partial.append(nid); tally["partial"] += 1
        elif len(members) == 1:
            m = members[0]
            L.append(f'    {nid}["{title_of(m)}"]')
            concrete.append(nid); tally["concrete"] += 1
            if m in S:
                L.append(f'    click {nid} "/docs/modules/{m}/spec"')
        elif (mt := meet(members, par)):
            L.append(f'    {nid}["{title_of(mt)}<br/>{{{", ".join(shown)}}}"]')
            abstract.append(nid); tally["abstract"] += 1
            if mt in S:
                L.append(f'    click {nid} "/docs/modules/{mt}/spec"')
        else:
            # THE FIGURE STILL NAMES THE THING. NO COMMON ANCESTOR is a good warning, but
            # the figure should still say Cascade, or name the cascades it spans.
            # A node a reader cannot
            # name is a node they skip, and the warning is worth less for it.
            tag = f" — {label_for}" if label_for else ""
            tail = shared_tail(shown)
            # NO PUNCTUATION: "Cascade", not "Cascade?". The question mark was doing work the
            # warning line below already does, and a name with a query on it reads as
            # uncertainty about the name rather than about the class.
            lead = f"{tail}<br/>" if tail else ""
            L.append(f'    {nid}["{lead}{", ".join(shown)}'
                     f'<br/>NO COMMON ANCESTOR{tag}"]')
            unmet.append(nid); tally["unmet"] += 1

    # PROCESS NODES, drawn as stadiums per the house style and classed by the same
    # three rules. ABSTRACTNESS DOES NOT PROPAGATE: a process every leg shares is
    # concrete even when every module flowing into it is abstract, which is why this
    # pass is separate rather than inherited from the operands.
    L.append("")
    for k in porder:
        members = sorted(set(pslots[k].values()))
        pshown = [proc_titles.get(m, m) for m in members]
        nid = nid_of(k)
        link = k.rsplit(":", 1)[1]
        tail = "" if link == "0" else f", link {int(link) + 1}"
        if len(pslots[k]) < len(legs):
            L.append(f'    {nid}(["{", ".join(pshown)}{tail}<br/>'
                     f'only {len(pslots[k])} of {len(legs)} legs run this"])')
            partial.append(nid); tally["proc_partial"] += 1
        elif len(members) == 1:
            L.append(f'    {nid}(["{pshown[0]}{tail}"])')
            procs.append(nid); tally["proc_concrete"] += 1
        elif (mt := meet(members, pproc)):
            L.append(f'    {nid}(["{proc_titles.get(mt, mt)}{tail}<br/>{{{", ".join(pshown)}}}"])')
            abstract.append(nid); tally["proc_abstract"] += 1
        else:
            L.append(f'    {nid}(["{", ".join(pshown)}{tail}'
                     f'<br/>NO COMMON ANCESTOR"])')
            unmet.append(nid); tally["proc_unmet"] += 1

    # P1 AND P2: THE BOXES. Drawn after the process stadiums so they read as
    # annotations on the spine rather than as part of it.
    #
    # A BOX IS ONE PER CONDITION, NOT ONE PER LEG. Two legs declaring `thermal-hold`
    # are making the same claim, and two boxes would say they are different. A box
    # only some legs declare says so on its own face, exactly as a partial slot does.
    #
    # MERMAID AND THE PIPE. `|` is edge-label syntax, so a notation carrying one is
    # written as the entity and the renderer prints it.
    reqnodes, impnodes = [], []

    def condition_nodes(store: dict, prefix: str, shape: tuple[str, str],
                        bucket: list, kind: str) -> None:
        for cid in sorted(store):
            per = store[cid]
            labels = sorted({t for t, _ in per.values()})
            text = "<br/>".join(labels).replace("|", "#124;")
            nid = nid_of(f"{prefix}:{cid}")
            note = ""
            if cid in inherited:
                note = f'<br/>inherited from {title_of(inherited[cid])}'
            elif len(per) < len(legs):
                note = f'<br/>only {len(per)} of {len(legs)} legs declare this'
            L.append(f'    {nid}{shape[0]}"{text}{note}"{shape[1]}')
            bucket.append(nid)
            tally[kind] += 1

    L.append("")
    condition_nodes(reqs, "req", ("{{", "}}"), reqnodes, "requirement")
    condition_nodes(imps, "imp", ("[/", "/]"), impnodes, "imposition")

    # WHAT THE HAND FIGURE DRAWS AND NO SOURCE DECLARES IS NAMED ON STDERR. Q1 ruled
    # the spec wins, so the figure is not patched to match the drawing -- but a silent
    # difference between the two is the defect this whole thread was about.
    #
    # IT IS A NOTE AND NOT A WARNING, AND THE DIFFERENCE IS LOAD-BEARING. A WARNING
    # here says something about THIS RUN that the reader could act on, which is what
    # the dropped-leg warning is and what tests/test_dropped_leg_warning.py pins. This
    # says the same thing on every run, because it is a standing limit of the schema
    # rather than a fact about the legs asked for. Sharing the word would have taught
    # a reader to skip both.
    HAND_FIGURE_BOXES = {
        "osmotic-matching": "osm(Outer Solution) = osm(SensorCytosol[X ⟶ PLA1]) — "
                            "a two-sided relation; `bound.from` names one operand, so "
                            "the schema cannot hold it and no source declares it",
    }
    for box, why in sorted(HAND_FIGURE_BOXES.items()):
        if box not in reqs and box not in imps:
            print(f"NOTE: the hand figure draws `{box}` and no source declares it, "
                  f"so this meet does not: {why}", file=sys.stderr)

    # CROSS-PASS AGREEMENT, c9d6a5's, and it is the free control one level up. The two
    # passes key differently on purpose: module slots align by the product's class,
    # process slots by process identity in their own poset. So a process slot CAN group
    # two steps whose products the module pass keeps apart, and that would assert one
    # source into two positions at once. Nothing else here would notice.
    cross_ok = cross_bad = 0
    for k in porder:
        prods = {}
        for leg in pslots[k]:
            src_name, steps = legs[leg]
            for s in steps:
                for pr in ((s.get("process") or {}).get("composed_of")
                           or [s.get("process") or {}]):
                    if (proc_dir(pr) or pr.get("title")) == pslots[k][leg]:
                        m = to_module(s["produces"].get("page")) or s["produces"]["id"]
                        prods[leg] = member_slot_of(leg, m)
        if len(prods) > 1:
            (cross_ok := cross_ok + 1) if len(set(prods.values())) == 1 else (
                cross_bad := cross_bad + 1)

    # EDGES RUN OPERAND -> PROCESS -> PRODUCT, the same spine render-composition.py
    # draws, projected onto slots. Routing them operand-to-product instead left every
    # process stadium floating unconnected on the right of the page, which is what the
    # first rendered draft showed: seven nodes with no edges, carrying real findings
    # nobody would read because they sat outside the graph.
    #
    # AN EDGE ONLY ONE LEG HAS IS STILL DRAWN. The meet is over the union of what the
    # legs do, and dropping a leg's edge would assert the others do not do it.
    proc_slot_of: dict[tuple[str, str, int], str] = {}
    for k in porder:
        li = int(k.rsplit(":", 1)[1])
        for leg, d in pslots[k].items():
            proc_slot_of[(leg, d, li)] = k

    edges: set[tuple[str, str]] = set()
    for leg, (src_name, steps) in legs.items():
        src = S[src_name]
        for s in steps:
            chain = ((s.get("process") or {}).get("composed_of")
                     or [s.get("process") or {}])
            pk = [proc_slot_of.get(
                    (leg, proc_dir(pr) or (pr.get("title") or "untitled"), i))
                  for i, pr in enumerate(chain)]
            pk = [x for x in pk if x]
            if not pk:
                continue
            for o in s["operands"]:
                om = operand_module(src, o, S, par) or o
                if (sk := member_slot_of(leg, om)):
                    edges.add((sk, pk[0]))
            for a, b in zip(pk, pk[1:]):
                edges.add((a, b))
            pm = to_module(s["produces"].get("page")) or s["produces"]["id"]
            if (dk := member_slot_of(leg, pm)):
                edges.add((pk[-1], dk))

    # A CONDITION BOX HANGS OFF THE PROCESS IT CONSTRAINS. Both keys sit on a step,
    # so the step's first process slot is where the box attaches. A box whose step
    # resolves to no process slot is still drawn, unattached, rather than dropped:
    # the condition is declared whether or not this figure can place it.
    step_proc: dict[tuple[str, str], str] = {}
    for leg, (src_name, steps) in legs.items():
        for st in steps:
            chain = ((st.get("process") or {}).get("composed_of")
                     or [st.get("process") or {}])
            for i, pr in enumerate(chain):
                k = proc_slot_of.get(
                    (leg, proc_dir(pr) or (pr.get("title") or "untitled"), i))
                if k:
                    step_proc.setdefault((leg, st["id"]), k)
                    break
    for prefix, store in (("req", reqs), ("imp", imps)):
        for cid, per in store.items():
            for leg, (_, step_id) in per.items():
                if (k := step_proc.get((leg, step_id))):
                    edges.add((f"{prefix}:{cid}", k))

    L.append("")
    for a, b in sorted(edges):
        L.append(f"    {nid_of(a)} --> {nid_of(b)}")

    L.append("")
    L.append(STYLE.rstrip("\n"))
    # THE DOMAIN NODE CARRIES A CLASS LIKE EVERY OTHER NODE. Without one it took
    # Mermaid's default fill, which is lavender, against the grayscale the
    # mermaid-diagrams skill sets as house style. It is drawn dashed because it
    # states what the figure is taken over rather than being a thing in it.
    for nm, ids in (("concrete", concrete), ("abstract", abstract),
                    ("unmet", unmet), ("partial", partial),
                    ("process", procs), ("require", reqnodes),
                    ("impose", impnodes), ("domain", ["DOMAIN"])):
        if ids:
            L.append(f"    class {','.join(ids)} {nm};")
    print("\n".join(L))

    # --- denominators, every run. The marker is kept from reading as a class by
    # this, not by the exit code.
    # THE SLOT DENOMINATOR EXCLUDES THE CONDITION BOXES. They are not slots:
    # nothing is met over them, and counting them would inflate the number the
    # concrete/abstract/unmet split is read against.
    n = sum(v for k, v in tally.items()
            if not k.startswith("proc_") and k not in ("requirement", "imposition"))
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
          f"{tally['requirement']} requirement box(es) and {tally['imposition']} "
          f"imposition box(es), {len(inherited)} of them inherited from a class "
          f"rather than declared on a leg\n"
          f"{cross_ok} cross-pass agreement(s), {cross_bad} disagreement(s): where a "
          f"process slot groups two legs' steps, their products land in one module slot\n"
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
