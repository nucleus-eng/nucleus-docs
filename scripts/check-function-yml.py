#!/usr/bin/env python3
"""Check each docs/functions/<page>/function.yml against the signature it pins.

Local only, like check-functions.py: it reads compositional-biology-theory at a commit, and
a commit there must not be able to turn a PR here red.

WHAT IS CHECKED, AND WHAT IS NOT. A function.yml holds the docs' own words and a few fields
that the signature can confirm. Only the second kind is compared.
  process          must be a declared process (or refinement) in the Interface block
  routes[].key     must be declared there too, and `refines` must be the relation the
                   signature states ("refines X" in the profile) or the stem implies
                   (degrade[ssrA] has the stem degrade)
  species          must equal the signature's change lines for that name, per denominator
                   (per_residue, per_chain, per_cargo, per_event), species by species
  realized_by      every id must be a Module here, which is the one thing checkable
                   without the signature
NOT CHECKED: `match_name` (the shared provider/requirer spelling, which the signature may use
only in prose) and `docs_group` (a grouping the signature does not state). Both are listed
so a reader sees what the run took on trust.

A function with no `species:` has no declared change. That is reported as unknown. It is
never read as zero, because a reading of zero from an absence is the mistake this block
exists to prevent: an argument from what is not declared is only as good as the declaration
set being complete.

    python3 scripts/check-function-yml.py --theory PATH --ref a7c7a7a

Exit 0 when clean, 1 on a failing finding, 2 when it could not run.
"""
import argparse
import importlib.util
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
FUNCTIONS = REPO / "docs" / "functions"
MODULES = REPO / "docs" / "modules"

_spec = importlib.util.spec_from_file_location("check_functions", Path(__file__).with_name("check-functions.py"))
cf = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cf)

DENOM = re.compile(r"per\s+(\w+)\s*:\s*(.+)")
ITEM = re.compile(r"^(?P<name>[^\s]+)\s+(?P<sign>[+−-])(?P<n>\d+)$")
GAP = re.compile(r"\s{2,}")


def spans(block):
    """{declared name: its lines, the declaration and everything indented under it}."""
    lines = block.split("\n")
    heads = [(i, cf.DECL.match(l).group(1)) for i, l in enumerate(lines)
             if l and not l[0].isspace() and cf.DECL.match(l)]
    out = {}
    for k, (i, name) in enumerate(heads):
        j = heads[k + 1][0] if k + 1 < len(heads) else len(lines)
        out[name] = lines[i:j]
    return out


def change_lines(span):
    """{denominator: {species: signed int}} from a declaration's `per X : ...` lines."""
    out = {}
    for line in span:
        m = DENOM.search(line)
        if not m:
            continue
        items = GAP.split(m.group(2).strip())[0]
        sp = {}
        for it in (x.strip() for x in items.split(",")):
            mm = ITEM.match(it)
            if not mm:
                sp = None
                break
            sp[mm["name"]] = (-1 if mm["sign"] in "−-" else 1) * int(mm["n"])
        if sp is not None:
            out[m.group(1)] = sp
    return out


NET = re.compile(r"Δν\([^)]*\)\s+per\s+(\w+)\s*:\s*([+−-]?\d+)(?=\s|$)")


def net_of(span):
    """{denominator: net particle change} from a `Δν(X) per event : N` line, which gives no species."""
    out = {}
    for line in span:
        m = NET.search(line)
        if m:
            n = int(m.group(2).replace("−", "-"))
            out[m.group(1)] = n
    return out


def states_refines(span, parent):
    text = " ".join(span).replace("`", "")
    return f"refines {parent}" in text


def check_entry(entry, valid, sp, modules, where):
    """Findings for one process or route. `entry` has `key` or `process`."""
    out = []
    name = entry.get("key") or entry.get("process")
    if name is None:
        return [("⛔️", f"{where}: no `key` or `process`")]
    if name not in valid:
        out.append(("⛔️", f"{where}: `{name}` is not a declared process in the signature"))
        return out
    parent = entry.get("refines")
    if parent:
        stem = name.split("[")[0]
        if parent not in valid:
            out.append(("⛔️", f"{where}: `refines: {parent}` names nothing declared"))
        elif parent not in {stem, *stem.split("_")} and not states_refines(sp.get(name, []), parent):
            out.append(("⛔️", f"{where}: `{name}` refines `{parent}` here, and the signature "
                              f"neither states it nor implies it by the stem"))
    declared_change = change_lines(sp.get(name, []))
    own_net = net_of(sp.get(name, []))
    inherited_net = net_of(sp.get(parent, [])) if parent else {}
    net = own_net or inherited_net
    claimed_net = entry.get("net")
    if claimed_net is not None:
        mine_net = {k.removeprefix("per_"): v for k, v in claimed_net.items()}
        if not own_net:
            out.append(("⛔️", f"{where}: states a net change and the signature has no net line "
                              f"for `{name}`"))
        elif mine_net != own_net:
            out.append(("⛔️", f"{where}: net change differs from the signature. here {mine_net}, "
                              f"signature {own_net}"))
    mine = entry.get("species")
    if mine is None:
        if declared_change:
            out.append(("ℹ️ ", f"{where}: the signature states a change for `{name}` and this "
                              f"file states none"))
        elif net or claimed_net is not None:
            out.append(("ℹ️ ", f"{where}: a net change is declared and no species at this level"))
        else:
            out.append(("ℹ️ ", f"{where}: no declared change, so UNKNOWN, not zero"))
    else:
        norm = {k.removeprefix("per_"): v for k, v in mine.items()}
        if not declared_change and net:
            # no species to compare, only a net count: the species must sum to it
            for den, total in net.items():
                have = norm.get(den)
                if have is None:
                    out.append(("⛔️", f"{where}: the signature gives a net for per {den} and this "
                                      f"file states no species for it"))
                elif sum(have.values()) != total:
                    out.append(("⛔️", f"{where}: species per {den} sum to {sum(have.values())} "
                                      f"and the signature's net is {total}"))
        elif not declared_change:
            out.append(("⛔️", f"{where}: states a change for `{name}` and the signature has no "
                              f"change line for it"))
        elif norm != declared_change:
            out.append(("⛔️", f"{where}: change differs from the signature. here {norm}, "
                              f"signature {declared_change}"))
    for mod in entry.get("realized_by") or []:
        if not (modules / mod / "spec.md").is_file():
            out.append(("⛔️", f"{where}: realized_by `{mod}` is not a Module here"))
    return out


def check_file(path, valid, sp, modules):
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    out, untaken = [], []
    for op in data.get("processes") or []:
        out += check_entry(op, valid, sp, modules, f"{path.parent.name} {op.get('process')}")
        for r in op.get("routes") or []:
            where = f"{path.parent.name} {op.get('process')} route {r.get('id')}"
            if "key" in r:
                out += check_entry(r, valid, sp, modules, where)
            else:
                if r.get("match_name"):
                    untaken.append(f"{where}: match_name `{r['match_name']}` not checked")
                for mod in r.get("realized_by") or []:
                    if not (modules / mod / "spec.md").is_file():
                        out.append(("⛔️", f"{where}: realized_by `{mod}` is not a Module here"))
            if r.get("docs_group"):
                untaken.append(f"{where}: docs_group `{r['docs_group']}` not checked")
    return out, untaken


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--theory", help="a checkout of compositional-biology-theory")
    ap.add_argument("--ref", default="HEAD")
    a = ap.parse_args()
    files = sorted(FUNCTIONS.glob("*/function.yml"))
    if not files:
        print("ℹ️  no function.yml files; nothing to check")
        return 0
    path, text, h = cf.find_theory(a.theory, a.ref)
    if path is None:
        print("ℹ️  skipped: no checkout of compositional-biology-theory found. A skip is not a pass.")
        return 2 if a.theory else 0
    block = cf.interface_block(text)
    if block is None:
        print(f"⛔️ no Interface block in signature.md at {h}")
        return 2
    counted, excluded = cf.declared(block)
    valid = set(counted) | {n for n, why in excluded.items() if why.startswith("refines")}
    sp = spans(block)
    fails = 0
    for f in files:
        pin = (yaml.safe_load(f.read_text(encoding="utf-8")) or {}).get("signature_pin")
        if pin and not h.startswith(str(pin)[:7]) and not str(pin).startswith(h[:7]):
            print(f"ℹ️  {f.parent.name}: pinned at {pin}, checked at {h}")
    for f in files:
        out, untaken = check_file(f, valid, sp, MODULES)
        for mark, msg in out:
            print(f"{mark} {msg}")
        for msg in untaken:
            print(f"ℹ️  {msg}")
        fails += sum(1 for m, _ in out if m == "⛔️")
    print(f"{'✅' if not fails else '⛔️'} {len(files)} function.yml file(s) against signature.md at {h}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
