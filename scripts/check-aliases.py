#!/usr/bin/env python3
"""Report one thing wearing two names, over every carrier the corpus has.

REPLACES check-input-aliases.py, which asked this question of one carrier. The
predicate is the same in all four cases and the carriers keep arriving: writing
the Outer Solution class on 2026-09-21 found an alias the input-key version could
not see, and a second checker for it would have been a third the week after.

WHY THE PREDICATE MATTERS. A name is an identity. Operands reference it,
operator_pairs name it, and a diagram draws one node per name. Two names for one
thing make a leg walk reach it twice, so a slot where two demo legs AGREE counts
two members and gets marked abstract. That failure manufactures a design decision
rather than hiding one, which is the direction that wastes a reader's time.

FOUR CARRIERS, each found the hard way.

  KEY -> PAGE          Two input keys resolving to one module page. ULGA powder
                       was `ulga`, `ulga-powder` and `agarose` across four
                       sources. The third name was invisible while it carried
                       page: null, so Jon identifying the agarose as ULGA turned
                       a gap into a duplicate and no check noticed either event.

  ID -> COMPOSITION    Two produced ids from the same operands AND the same
                       parameters. london-cascade produced `outer-solution` and
                       gel-ulga produced `london-outer-solution` from the same
                       three solutes at the same osmolarity. The key check could
                       not see it: both carried page: null, so neither resolved
                       to anything to collide with.

                       PARAMETERS ARE PART OF THE COMPARISON AND THE MEMBRANES
                       ARE WHY. membrane-popc-chol and membrane-popc-chol-chicago
                       compose the identical three lipids and are different
                       Modules at 70:30 against 90:10. Operand-set alone reports
                       a rename that is not one.

  TITLE -> ID          Two ids carrying one title. This is the one a reader hits:
                       nodes are labelled with titles, so two different things
                       draw as two identical boxes. Jon, 2026-09-21, reading a
                       meet: "why are both in there?"

  DIR -> TITLE         One process directory called two things.
                       embed-ulga-hydrogel was `Hydrogel Embedding: ULGA` in three
                       sources and `ULGA Embedding` in a fourth, and the title
                       reaches the diagram because render-composition.py puts it
                       on the node.

ADVISORY, and the denominator prints every run. A carrier at zero today is not a
carrier that cannot fail: DIR -> TITLE is at zero only because its one case was
fixed hours before this was written.
"""
import collections
import glob
import os
import re
import sys

import yaml

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

SOURCES = sorted(glob.glob("docs/modules/*/spec.yml"))
docs = {os.path.basename(os.path.dirname(f)): (yaml.safe_load(open(f)) or {})
        for f in SOURCES}


def steps(d):
    return d.get("process_steps") or []


def chain(s):
    return (s.get("process") or {}).get("composed_of") or [s.get("process") or {}]


def proc_dir(pr):
    pg = pr.get("page") or ""
    return re.sub(r"/[^/]+$", "", pg).rsplit("/", 1)[-1] if pg else None


# --- carrier 1: input key -> module page
by_page = collections.defaultdict(set)
key_uses = collections.Counter()
unpaged = collections.Counter()
keys = 0
for mod, d in docs.items():
    here = os.path.join("docs/modules", mod)
    for key, v in (d.get("inputs") or {}).items():
        keys += 1
        page = (v or {}).get("page")
        if not page:
            unpaged[key] += 1
            continue
        target = os.path.normpath(os.path.join(here, page))
        by_page[target].add(key)
        key_uses[(target, key)] += 1

# --- carrier 2: produced id -> composition (operands AND parameters)
by_comp = collections.defaultdict(set)
comp_uses = collections.Counter()
comps = 0
for mod, d in docs.items():
    for s in steps(d):
        ops = frozenset(s["operands"])
        if len(ops) < 2:
            continue          # a one-operand step is too thin to call a duplicate
        sig = (ops, frozenset((s.get("parameters") or {}).items()))
        comps += 1
        by_comp[sig].add(s["produces"]["id"])
        comp_uses[(sig, s["produces"]["id"])] += 1

# --- carrier 3: produced title -> produced id
by_title = collections.defaultdict(set)
title_uses = collections.Counter()
titles = 0
for mod, d in docs.items():
    for s in steps(d):
        pr = s["produces"]
        if not pr.get("title"):
            continue
        titles += 1
        by_title[pr["title"]].add(pr["id"])
        title_uses[(pr["title"], pr["id"])] += 1

# --- carrier 5: module title -> module. ADDED AFTER A POSITIVE CONTROL FAILED.
# The control planted a duplicate module title, the check did not fire, and the
# reason was that no carrier read the top-level `title:` at all — only the titles
# on produced ids. The test assumed a carrier that was not there, which is the
# cheapest way this gap was ever going to surface.
by_modtitle = collections.defaultdict(set)
modtitle_uses = collections.Counter()
modtitles = 0
for mod, d in docs.items():
    if not d.get("title"):
        continue
    modtitles += 1
    by_modtitle[d["title"]].add(mod)
    modtitle_uses[(d["title"], mod)] += 1

# --- carrier 4: process directory -> title
by_dir = collections.defaultdict(set)
dir_uses = collections.Counter()
procs = 0
for mod, d in docs.items():
    for s in steps(d):
        for pr in chain(s):
            dn, t = proc_dir(pr), pr.get("title")
            if not (dn and t):
                continue
            procs += 1
            by_dir[dn].add(t)
            dir_uses[(dn, t)] += 1


def report(label, index, uses, fmt):
    """HOW LOPSIDED, not just how many. Two names says there is a rename to do;
    the per-name counts say which way it runs, and the cases so far run opposite
    ways. ULGA powder had `agarose` as the odd one out in two files; the Chicago
    membrane had the LONG id as the odd one out in one file against the short id
    in seven, so renaming toward the long name would touch seven files to fix one.
    Printing only the count hands that decision over with no evidence."""
    rows = {k: v for k, v in index.items() if len(v) > 1}
    for k, names in sorted(rows.items(), key=lambda x: fmt(x[0])):
        counts = sorted(((uses[(k, n)], n) for n in names), reverse=True)
        print(f"ALIAS [{label}]  {fmt(k)}")
        print("        " + ", ".join(
            f"{n} ({c} source{'s' if c != 1 else ''})" for c, n in counts))
        print()
    return rows


found = {}
found["key→page"] = report(
    "key→page", by_page, key_uses, lambda p: p)
found["id→composition"] = report(
    "id→composition", by_comp, comp_uses,
    lambda sig: "operands " + ", ".join(sorted(sig[0])))
found["title→id"] = report(
    "title→id", by_title, title_uses, lambda t: repr(t))
found["dir→title"] = report(
    "dir→title", by_dir, dir_uses, lambda d: d)
found["title→module"] = report(
    "title→module", by_modtitle, modtitle_uses, lambda t_: repr(t_))

# TWO CARRIERS FLAGGING ONE PAIR IS CORROBORATION, NOT TWO PROBLEMS. Saying so
# keeps the count honest: today's five rows are four distinct pairs, and a reader
# who fixes three does not have two left.
pairs = collections.Counter()
for car, rows in found.items():
    for names in rows.values():
        pairs[frozenset(names)] += 1
doubled = {p: n for p, n in pairs.items() if n > 1}

total = sum(len(v) for v in found.values())
print(f"{len(SOURCES)} source(s). One predicate, five carriers:\n")
print(f"  key→page         {len(by_page):4} page(s) referenced, "
      f"{len(found['key→page'])} with more than one name   ({keys} keys)")
print(f"  id→composition   {len(by_comp):4} composition(s), "
      f"{len(found['id→composition'])} with more than one id   ({comps} steps "
      f"with 2+ operands)")
print(f"  title→id         {len(by_title):4} title(s), "
      f"{len(found['title→id'])} naming more than one id   ({titles} products)")
print(f"  dir→title        {len(by_dir):4} process dir(s), "
      f"{len(found['dir→title'])} with more than one title   ({procs} links)")
print(f"  title→module     {len(by_modtitle):4} module title(s), "
      f"{len(found['title→module'])} naming more than one module   "
      f"({modtitles} sources with a title)")
print(f"\n{sum(unpaged.values())} input key(s) carry page: null and cannot collide "
      f"on the first carrier.")
print("An unpaged key is not a pass. It is a material nothing has identified, and\n"
      "identifying one is exactly what created the first alias this check caught.\n"
      "A carrier at zero is not a carrier that cannot fail: dir→title was at one\n"
      "the morning this was written.")

if doubled:
    print(f"\n{len(doubled)} pair(s) appear on more than one carrier, which is "
          f"corroboration rather than separate findings:")
    for pr, n in sorted(doubled.items(), key=lambda x: sorted(x[0])):
        print(f"  {', '.join(sorted(pr))} — flagged by {n} carriers")
    print(f"So {total} row(s) above are {len(pairs)} distinct pair(s).")

if "--strict" in sys.argv:
    sys.exit(1 if total else 0)
if total:
    print(f"\nadvisory: {total} alias(es) across "
          f"{sum(1 for v in found.values() if v)} carrier(s); "
          f"pass --strict to fail on them.")
sys.exit(0)
