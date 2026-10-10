#!/usr/bin/env python3
"""Report, for each Module, which provided operations have a declared change in particle count.

A Module's `provides:` names the operations it performs. A Function page's
`function.yml` declares what each operation consumes and produces, per residue, per chain
or per event. This joins the two and says where the join is complete.

It does NOT add anything up. The multiplier is not in any file: chain length, the rate and
the pool sizes are inputs. What it reports is whether every provided operation has a
declared change, because a sum over a gap is a sum that reads as smaller than it is.

AN OPERATION WITH NO DECLARED CHANGE IS REPORTED AS UNKNOWN, NEVER AS ZERO. A route with no
`species:` inherits its operation's, and an operation with none has none.

REPORT ONLY. It always exits 0 and is in no workflow.

    python3 scripts/report-particle-count.py
    python3 scripts/report-particle-count.py --functions path/to/functions
"""
import argparse
import glob
import os

import yaml

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

ap = argparse.ArgumentParser()
ap.add_argument("--functions", default="docs/functions", help="directory holding <operation>/function.yml")
args = ap.parse_args()

# id -> (species or None, where it came from)
INDEX = {}
files = sorted(glob.glob(os.path.join(args.functions, "*", "function.yml")))
for f in files:
    for op in (yaml.safe_load(open(f)) or {}).get("operations") or []:
        name = op.get("operation")
        op_species = op.get("species")
        INDEX.setdefault(name, (op_species, f"{name} (operation)"))
        for r in op.get("routes") or []:
            key = r.get("key") or r.get("match_name")
            if key:
                INDEX[key] = (r.get("species") or op_species, f"{key} (route of {name})")

SRC = {}
for f in sorted(glob.glob("docs/modules/*/spec.yml")):
    SRC[f.split("/")[2]] = yaml.safe_load(open(f)) or {}


def lookup(op_id):
    """The declared change for a provided id, matched by the route's key or shared name."""
    return INDEX.get(op_id)


def fmt(species):
    return "; ".join(f"{d.replace('_', ' ')} {{{', '.join(f'{k} {v:+d}' for k, v in s.items())}}}" for d, s in species.items())


print(f"{len(files)} function.yml file(s) read from {args.functions}")
mods = {m: s for m, s in SRC.items() if s.get("provides")}
unknown_total = 0
total = 0
for m, s in mods.items():
    print(f"\n{m}")
    gaps = 0
    for p in s["provides"]:
        total += 1
        basis = p.get("basis") or "undeclared"
        hit = lookup(p["id"])
        if hit and hit[1] and hit[0]:
            print(f"  {p['id']:<22} [{basis}]  {fmt(hit[0])}")
        else:
            gaps += 1
            unknown_total += 1
            why = "no function.yml names it" if not hit else f"{hit[1]} declares no species"
            print(f"  {p['id']:<22} [{basis}]  UNKNOWN: {why}")
    verdict = "complete" if not gaps else f"cannot compute: {gaps} of {len(s['provides'])} provided operation(s) have no declared change"
    print(f"  -> {verdict}")

print(
    f"\n{len(mods)} module(s) declare `provides:`; {unknown_total} of {total} provided operation(s) have no declared change."
    "\nNo sum is produced. Chain length, rate and pool sizes are inputs and live in no file."
    "\nUNKNOWN is not zero."
)
