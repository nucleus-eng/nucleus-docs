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

**Three of these citations pointed at the wrong line and were repointed 2026-09-21,
against compositional-biology-theory `main` at `ada4ea5`.** `the-tensor-problem.md:5`
was the code fence above the claim, off by one. `signature.md:124` was cited twice for
*"LacZ in the outer phase"* and names a sentence about `Cell (Base)`; the claim is at
`:149`. **The discipline here was to cite, and nothing ever checked a citation.** That
is the same shape as the rule these rows enforce: an independent claim was demanded and
the pointer to it was not read back.

**A LINE NUMBER INTO ANOTHER REPO IS NOT A CITATION ON ITS OWN**, which is why the pins
below are new. That file moves under every commit, and a reader following a bare
`file.md:NN` a week later lands wherever the line drifted to. Session `c9d6a5` measured
the same class in its own tree on the same day and found 5 of 16 wrong, 31 percent;
this file was 3 of 9. Repoint against a stated commit or the number is decoration.

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
  frozenset({'cytosol', 'effector'}):  (MIX,  '2026-08-25-chicago-cross-lysis.md:227 "aTcCell = M<BaseCytosol (+) Det_aTc (+) PLA1_teto"', False),
  frozenset({'cytosol', 'reporter'}):  (MIX,  '2026-08-25-chicago-cross-lysis.md:227, same interior', False),
  frozenset({'detector', 'effector'}): (MIX,  '2026-08-25-chicago-cross-lysis.md:227, same interior', False),
  frozenset({'detector', 'reporter'}): (MIX,  '2026-08-25-chicago-cross-lysis.md:227, same interior', False),
  frozenset({'effector', 'reporter'}): (MIX,  '2026-08-25-chicago-cross-lysis.md:227, same interior', False),
  frozenset({'cytosol', 'membrane'}):  (PACK, 'the-tensor-problem.md:6 "Cytosol (x) Membrane -> a real tensor: separated by a membrane"', False),
  frozenset({'polymer', 'solution'}):  (MIX,  'codimension-is-a-coordinate.md:32 "Gel = OuterSolution (+) polymer, same compartment, no membrane between them"', False),
  # O8-dependent: whether a payload pre-added to a forming gel is a constituent or
  # is *held* is exactly open question O8. An independent claim exists either way,
  # so this is reported BLOCKED rather than scored.
  frozenset({'reporter', 'solution'}): (MIX,  'signature.md:149 "LacZ (+) in the outer phase" -- but see O8', True),
  frozenset({'polymer', 'reporter'}):  (MIX,  'signature.md:149, same claim against the polymer -- but see O8', True),
}
# Deliberately NOT seeded: Alginate with PEGDA. review-poset-draft.md calls the
# neighbouring term "a notation choice I am making, not one the corpus has".

# Every line number above was read back at this commit on 2026-09-21. It is one pin for
# the table rather than ten copies of a hash, because all ten rows cite the same repo.
SEED_PIN = 'ada4ea5'


def verify_citations(theory_repo):
    """Read each seed row's quoted fragment back off the line it names.

    NOT IN CI, and the reason is not cost. This needs a clone of
    compositional-biology-theory, CI has none, and a check that cannot run must not
    print something a reader mistakes for a pass. It is a flag so that a human with
    both repos can run it, and so the silence in CI is stated rather than implied.

    It compares against the repo's CURRENT main, not against SEED_PIN. Checking a
    pinned commit would always agree: the pin records where the line was read, and the
    question this answers is whether it is still there.
    """
    import subprocess, re

    # Word-set containment, not substring. The quoted fragments are transliterations
    # -- (x) for a tensor, -> for an arrow -- and the lines they name carry column
    # padding and an extra clause. A substring test called all four wrong on the first
    # run, which is this repo's own "a checker that cries wolf gets ignored" arriving
    # inside the checker written to stop that.
    STOP = {'a', 'an', 'the', 'in', 'is', 'of', 'by', 'not', 'no', 'and', 'or', 'to',
            'it', 'on', 'one', 'two', 'same', 'see', 'but'}
    words = lambda t: {w for w in re.findall(r'[A-Za-z]{2,}', t.lower())} - STOP
    cache, bad, checked, skipped = {}, [], 0, []
    for cite in sorted({c for _, (_, c, _) in SEED.items()}):
        m = re.match(r'([A-Za-z0-9_.\-]+\.md):(\d+)(.*)', cite)
        if not m:
            skipped.append(cite); continue
        fname, line, tail = m.group(1), int(m.group(2)), m.group(3)
        q = re.search(r'"([^"]+)"', tail)
        if not q:
            skipped.append(cite); continue       # "same interior", "same claim"
        if fname not in cache:
            r = subprocess.run(['git', '-C', theory_repo, 'show', f'origin/main:{fname}'],
                               capture_output=True, text=True)
            cache[fname] = r.stdout.split('\n') if r.returncode == 0 else None
        lines = cache[fname]
        if lines is None:
            bad.append((cite, 'no such file at origin/main')); continue
        if line > len(lines):
            bad.append((cite, f'past EOF, file has {len(lines)} lines')); continue
        body = lines[line - 1]
        checked += 1
        missing = words(q.group(1)) - words(body)
        if missing:
            bad.append((cite, f'line reads {body.strip()[:64]!r}; '
                              f'missing {sorted(missing)}'))
    return checked, bad, skipped

rows, tally = [], collections.Counter()
for f in sorted(glob.glob('docs/**/spec.yml', recursive=True)):
    d = yaml.safe_load(open(f)) or {}
    key = 'process_steps' if 'process_steps' in d else 'steps'
    for s in (d.get(key) or []):
        label = s.get('operator')
        # A step may override its label for named pairs. The label stays the
        # default and operator_pairs lists only the exceptions, so a pair's
        # operator is the exception where one exists and the label otherwise.
        overrides = {}
        for ov in (s.get('operator_pairs') or []):
            pair = ov.get('operands') or []
            if len(pair) == 2:
                overrides[frozenset(pair)] = ov.get('operator')
        ops = [o if isinstance(o, str) else (o.get('module') or o)
               for o in (s.get('operands') or [])]
        for a, b in itertools.combinations(sorted(set(ops)), 2):
            label = overrides.get(frozenset({a, b}), s.get('operator'))
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
if '--verify-citations' in sys.argv:
    repo = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '..', '..', '..', '..', 'compositional-biology-theory')
    repo = os.path.abspath(repo)
    print()
    if not os.path.isdir(os.path.join(repo, '.git')):
        print(f"CANNOT RUN: no compositional-biology-theory clone at {repo}.")
        print("That is not a pass. Clone it beside nucleus-eng and run this again.")
        sys.exit(2)
    checked, bad, skipped = verify_citations(repo)
    for cite, why in bad:
        print(f"WRONG CITATION  {cite}\n                {why}")
    print(f"{checked} quoted citation(s) read back at origin/main, {len(bad)} wrong, "
          f"{len(skipped)} carry no quote to check")
    print(f"seed pin: {SEED_PIN}. A row with no quoted fragment cannot be verified "
          f"mechanically and is not counted as passing.")
    sys.exit(1 if bad else 0)

if '--strict' in sys.argv:
    sys.exit(1 if tally['violation'] else 0)
if tally['violation']:
    print(f"advisory: {tally['violation']} violation(s); pass --strict to fail on them.")
sys.exit(0)
