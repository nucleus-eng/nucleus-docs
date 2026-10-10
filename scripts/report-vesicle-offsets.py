#!/usr/bin/env python3
"""Report which vesicle designs declare an osmotic setpoint, and which are silent.

`vesicle` states a Requirement with no number. A member sharpens it with a
`sensitivities:` entry on `to: osmotic-shift` whose bound carries a `setpoint`, the
offset between lumen and outer solution. Absence means undeclared, not zero, so a
silent design is a gap nobody has flagged. This lists them.

REPORT ONLY. It always exits 0 and is in no workflow: a job that cannot fail is
always green, so read the output instead. Run it by hand.

    python3 scripts/report-vesicle-offsets.py
"""
import glob
import os

import yaml

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

SRC = {}
for f in sorted(glob.glob("docs/modules/*/spec.yml")):
    SRC[f.split("/")[2]] = yaml.safe_load(open(f)) or {}


def parents(m):
    r = (SRC.get(m) or {}).get("refines")
    return [] if not r else ([r] if isinstance(r, str) else list(r))


def descends(m, root, seen=None):
    seen = seen if seen is not None else set()
    for p in parents(m):
        if p == root or (p not in seen and not seen.add(p) and descends(p, root, seen)):
            return True
    return False


def own_setpoint(m):
    """The setpoint this module itself declares on osmotic-shift, or None."""
    for s in (SRC.get(m) or {}).get("sensitivities") or []:
        if s.get("to") != "osmotic-shift":
            continue
        b = s.get("bound") or {}
        if b.get("setpoint") is not None:
            return b["setpoint"], b.get("value"), b.get("unit")
    return None


def inherited(m, seen=None):
    """(ancestor, setpoint) for the nearest ancestor below `vesicle` that declares one."""
    seen = seen if seen is not None else set()
    for p in parents(m):
        if p == "vesicle" or p in seen:
            continue
        seen.add(p)
        sp = own_setpoint(p)
        if sp:
            return p, sp
        found = inherited(p, seen)
        if found:
            return found
    return None


members = sorted(m for m in SRC if m != "vesicle" and descends(m, "vesicle"))
rows = {"declared": [], "inherited": [], "silent": []}
for m in members:
    sp = own_setpoint(m)
    if sp:
        rows["declared"].append((m, f"{sp[0]} ± {sp[1]} {sp[2]}"))
        continue
    inh = inherited(m)
    if inh:
        rows["inherited"].append((m, f"{inh[1][0]} ± {inh[1][1]} {inh[1][2]}, from {inh[0]}"))
    else:
        rows["silent"].append((m, ""))

print(f"{len(members)} module(s) refine `vesicle`, directly or through a class")
for kind in ("declared", "inherited", "silent"):
    print(f"\n{kind.upper()} ({len(rows[kind])})")
    for m, note in rows[kind]:
        print(f"  {m}" + (f"  {note}" if note else ""))
print(
    "\nSilent means undeclared, not zero. Nothing here is a failure: this report "
    "exits 0 so a gap is visible without blocking anyone."
)
