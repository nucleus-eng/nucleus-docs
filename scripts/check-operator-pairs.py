#!/usr/bin/env python3
"""Check each step's single `operator` label against the pairs it actually asserts.

The schema records one operator per step. A step with `n` operands asserts that all
`C(n,2)` pairs carry that operator, and one contrary pair falsifies it. This reports
the contrary pairs. It applies nothing.

  VIOLATION  an independent claim says this pair takes the other operator
  BLOCKED    the pair is a gel-entry pair, which theory question O8 has open
  unknown    no independent claim covers this sort-pair -- NOT a pass

**The seed table must never be extended by reading step labels.** Sort predicts the
recorded operator on all 59 sort-pairs in this corpus, and at least one of those labels
is wrong, so a table fitted to the corpus scores 2 of 2 on the error and reports it as
confirmation. Every row below cites a claim argued independently of any `spec.yml`.
Adding a row without such a citation turns this check into a mirror.

Ruled by Jon 2026-09-17 as option D: derive the pair, check the label, change no schema.
"""
import yaml, glob, itertools, collections, os, sys

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

# --- sorts -------------------------------------------------------------------
# A trailing -suv/-guv is a COMPARTMENT declaration wearing a name suffix: the
# encapsulated form is a container, not a bare substrate. Collapsing them would
# hide the only axis that distinguishes the two forms.
def sort_of(x):
    x = str(x)
    if x.endswith(('-suv', '-guv')) or x.startswith('guv-'): return 'container'
    if x.endswith('-cell'):                                  return 'container'
    if x.startswith('membrane-'):                            return 'membrane'
    if x.endswith('-cytosol') or x == 'base-cytosol':        return 'cytosol'
    for p in ('detector', 'effector', 'reporter', 'substrate'):
        if x.startswith(p):                                  return p
    # LAP is a photoinitiator and not a polymer. The seed cites "Gel = OuterSolution
    # (+) polymer"; stretching 'polymer' to cover a small-molecule initiator would be
    # extending the seed by a sort assignment, which is the same failure as extending
    # it by a label. It gets its own sort, falls outside the table, and reports unknown.
    if x.startswith('lap'):                                  return 'initiator'
    if x.startswith(('agarose', 'ulga', 'peg', 'alginate')): return 'polymer'
    if 'solution' in x or x in ('tris-hepes-stock', 'energy-solution'): return 'solution'
    if 'gel' in x:                                           return 'gelbody'
    return x

# --- seed table --------------------------------------------------------------
# key: frozenset of two sorts -> (operator, citation, o8_dependent)
MIX, PACK = 'mixing', 'packing'
SEED = {
  frozenset({'cytosol', 'detector'}):  (MIX,  'the-tensor-problem.md:7 "Cytosol (+) Detector -> NOT a tensor: one shared cytosol"', False),
  frozenset({'cytosol', 'effector'}):  (MIX,  '2026-08-25-chicago-cross-lysis.md:227 aTcCell = M<BaseCytosol (+) Det_aTc (+) PLA1_teto ...>', False),
  frozenset({'cytosol', 'reporter'}):  (MIX,  '2026-08-25-chicago-cross-lysis.md:227, same interior', False),
  frozenset({'detector', 'effector'}): (MIX,  '2026-08-25-chicago-cross-lysis.md:227, same interior', False),
  frozenset({'detector', 'reporter'}): (MIX,  '2026-08-25-chicago-cross-lysis.md:227, same interior', False),
  frozenset({'effector', 'reporter'}): (MIX,  '2026-08-25-chicago-cross-lysis.md:227, same interior', False),
  frozenset({'cytosol', 'membrane'}):  (PACK, 'the-tensor-problem.md:5 "Cytosol (x) Membrane -> a real tensor: separated by a membrane"', False),
  frozenset({'polymer', 'solution'}):  (MIX,  'codimension-is-a-coordinate.md:32 "Gel = OuterSolution (+) polymer, same compartment, no membrane between them"', False),
  # O8-dependent: whether a payload pre-added to a forming gel is a constituent or
  # is *held* is exactly open question O8. An independent claim exists either way,
  # so this is reported BLOCKED rather than scored.
  frozenset({'reporter', 'solution'}): (MIX,  'signature.md:124 "LacZ (+) in the outer phase" -- but see O8', True),
  frozenset({'polymer', 'reporter'}):  (MIX,  'signature.md:124, same claim against the polymer -- but see O8', True),
}
# Deliberately NOT seeded: Alginate with PEGDA. review-poset-draft.md calls the
# neighbouring term "a notation choice I am making, not one the corpus has".

rows, tally = [], collections.Counter()
for f in sorted(glob.glob('docs/**/spec.yml', recursive=True)):
    d = yaml.safe_load(open(f)) or {}
    key = 'process_steps' if 'process_steps' in d else 'steps'
    for s in (d.get(key) or []):
        label = s.get('operator')
        ops = [o if isinstance(o, str) else (o.get('module') or o)
               for o in (s.get('operands') or [])]
        for a, b in itertools.combinations(sorted(set(ops)), 2):
            k = frozenset({sort_of(a), sort_of(b)})
            if len(k) < 2 or k not in SEED:
                tally['unknown'] += 1; continue
            want, cite, o8 = SEED[k]
            if o8:
                tally['blocked'] += 1
                rows.append(('BLOCKED  ', f, s.get('id'), a, b, label, want, cite))
            elif want != label:
                tally['violation'] += 1
                rows.append(('VIOLATION', f, s.get('id'), a, b, label, want, cite))
            else:
                tally['agrees'] += 1

for kind, f, sid, a, b, label, want, cite in rows:
    if kind.strip() == 'VIOLATION':
        print(f"{kind} {f}  {sid}")
        print(f"          {a} + {b}: step says {label}, claim says {want}")
        print(f"          {cite}\n")
for kind, f, sid, a, b, label, want, cite in rows:
    if kind.strip() == 'BLOCKED':
        print(f"{kind} {f}  {sid}  {a} + {b}  (O8)")

print('\n' + ' | '.join(f'{k} {tally[k]}' for k in
      ('violation', 'blocked', 'agrees', 'unknown') if tally[k]))
print('\nunknown is not a pass: no independent claim covers that sort-pair.')

# Advisory by default, on `check-implementations.py`'s precedent. The violations it
# reports are not editable defects: the step genuinely does two things and no single
# operator value is correct, so failing CI would demand a fix the schema cannot express.
# Pass --strict once the schema question is settled.
if '--strict' in sys.argv:
    sys.exit(1 if tally['violation'] else 0)
if tally['violation']:
    print(f"advisory: {tally['violation']} violation(s); pass --strict to fail on them.")
sys.exit(0)
