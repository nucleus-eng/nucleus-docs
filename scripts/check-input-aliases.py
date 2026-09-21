#!/usr/bin/env python3
"""Report input keys that name one module under more than one name.

An `inputs` key is an identity: operands reference it, `operator_pairs` name it,
and a diagram draws one node per key. Two keys resolving to the same `page:` are
one material wearing two names, and nothing compared them until 2026-09-21.

WHAT IT MISSED, which is why it exists. ULGA powder was `ulga` in gel-ulga,
`ulga-powder` in london-cascade and `agarose` in the two Chicago cascades. The
third name was invisible while it carried `page: null`, because an unidentified
material cannot collide with anything. Jon identifying the agarose as ULGA is
what turned a gap into a duplicate, so the corpus got WORSE by getting more
correct, and no check noticed either event.

A key with `page: null` is reported separately and is not a finding. It cannot
collide yet, and saying so is the honest state rather than a pass.
"""
import collections
import glob
import os
import sys

import yaml

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

by_page = collections.defaultdict(set)
key_uses = collections.Counter()
unpaged = collections.Counter()
keys = 0

for f in sorted(glob.glob("docs/modules/*/spec.yml")):
    d = yaml.safe_load(open(f)) or {}
    here = os.path.dirname(f)
    for key, v in (d.get("inputs") or {}).items():
        keys += 1
        page = (v or {}).get("page")
        if not page:
            unpaged[key] += 1
            continue
        target = os.path.normpath(os.path.join(here, page))
        by_page[target].add(key)
        key_uses[(target, key)] += 1

rows = {p: ks for p, ks in by_page.items() if len(ks) > 1}
for page, ks in sorted(rows.items()):
    # HOW LOPSIDED, not just how many. Two keys says there is a rename to do; the
    # per-key counts say which way it runs, and the two cases so far run opposite
    # ways. The ULGA powder had `agarose` as the odd one out in two files. The
    # Chicago membrane has the LONG id as the odd one out in one file against the
    # short id in seven, so renaming toward the long name would touch seven files
    # to fix one. A checker that prints only the key count hands that decision to
    # whoever reads it, with the evidence left in the tree.
    counts = sorted(((key_uses[(page, k)], k) for k in ks), reverse=True)
    print(f"ALIASES  {page}")
    print(f"         named by {len(ks)} keys: "
          + ", ".join(f"{k} ({n} source{'s' if n != 1 else ''})" for n, k in counts))
    print()

print(f"{keys} input key(s) over {len(glob.glob('docs/modules/*/spec.yml'))} sources")
print(f"{len(by_page)} distinct module page(s) referenced, {len(rows)} with more than one name")
print(f"{sum(unpaged.values())} key(s) carry page: null and cannot collide yet")
print("\nAn unpaged key is not a pass. It is a material nothing has identified,\n"
      "and identifying one is exactly what created the alias this check exists for.")

if "--strict" in sys.argv:
    sys.exit(1 if rows else 0)
if rows:
    print(f"\nadvisory: {len(rows)} aliased page(s); pass --strict to fail on them.")
sys.exit(0)
