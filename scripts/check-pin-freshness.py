#!/usr/bin/env python3
"""Report quotes in staging files that were true when pinned and are not true now.

`check-pins.py` resolves a pinned citation against the tree it names. That can only
ever confirm it: a pin names an immutable tree, so a correctly-pinned claim that has
gone stale is indistinguishable from one that is current. The pin guarantees the quote
*was* true. Nothing checked whether it still describes the world.

This resolves the same quote twice -- at the pin and at the tip -- and reports only
where they differ.

  STALE   present at the pinned hash, absent at the tip   -> the claim has expired
  CASE    present at the tip but cased differently        -> quote it as written
  GONE    absent at both                                  -> the citation is wrong, not stale
  fresh   present at the tip                              -> nothing to do

STALE and GONE take opposite responses. STALE means re-read and rewrite; GONE means
retract. Without a hash the two are indistinguishable, which is why an unpinned quote
is reported as `nopin` rather than guessed at.

Matching is exact after whitespace normalisation, deliberately. A loose matcher turns a
verdict into a proxy, and a proxy is a prompt to go look rather than an answer. The one
softening is CASE, which is reported as its own status instead of being absorbed --
found 2026-09-17 when a quotation's lowercased initial reported identically to a real
miss.

Three stale-but-correct claims on 2026-09-17 are what this is for: two in the theory
corpus and one of ours, all accurate when written, all edited out afterwards.
"""
import re, os, sys, subprocess, glob, collections

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
SIBLINGS = ['.', '../nucleus-skills', '../devnotes-repo',
            '../../../compositional-biology-theory', '../../compositional-biology-theory']

CITE  = re.compile(r'`([a-z0-9][a-z0-9\-/\._]*\.md):(\d+)`')
HASH  = re.compile(r'`([0-9a-f]{7,40})`')
QUOTE = re.compile(r'[*_]*"([^"]{15,220})"[*_]*')
NORM  = lambda t: re.sub(r'\s+', ' ', re.sub(r'[*_`>]', '', t)).strip()

def sh(*a, cwd=None):
    r = subprocess.run(a, capture_output=True, cwd=cwd)
    return r.returncode, r.stdout.decode('utf-8', 'replace')

def owning_repo(path):
    """Which sibling repo tracks this path at its tip, and under what full path.

    Staging prose cites both `gel-ulga/spec.md` and `docs/modules/gel-ulga/spec.md`
    for the same file. A short form that resolves to exactly one tracked path is
    accepted; one that resolves to several is not, because guessing which was meant
    would make the checker's answer depend on directory order.
    """
    for root in SIBLINGS:
        if not os.path.isdir(os.path.join(root, '.git')):
            continue
        rc, _ = sh('git', 'cat-file', '-e', f'HEAD:{path}', cwd=root)
        if rc == 0:
            return root, path
        rc, out = sh('git', 'ls-files', f'*/{path}', cwd=root)
        hits = [h for h in out.split() if h.endswith('/' + path)]
        if len(hits) == 1:
            return root, hits[0]
    return None, None

def text_at(root, ref, path):
    rc, out = sh('git', 'show', f'{ref}:{path}', cwd=root)
    return NORM(out) if rc == 0 else None

tally, rows = collections.Counter(), []

STAGING = sorted(glob.glob('tmp/staging/STAGED-*.md'))
if not STAGING:
    print('NOTHING CHECKED: no tmp/staging/STAGED-*.md found.')
    print('`tmp/` is gitignored, so this tool finds nothing in a fresh clone and')
    print('a green result here would verify nothing. It is a working-copy check,')
    print('never a CI gate. Run it where the staging files actually live.')
    sys.exit(2)

for sf in STAGING:
    lines = open(sf, encoding='utf-8').read().split('\n')
    for n, raw in enumerate(lines, 1):
        cite = CITE.search(raw)
        if not cite:
            continue
        # A table row is prose about sites, not a quotation of one: its cells carry
        # commentary that reads as a quote and reports a false miss.
        if raw.lstrip().startswith('|'):
            continue
        # The quote must sit on the citation's own line or the one after it. A wider
        # window picks up an unrelated quotation -- including one of Jon's spoken
        # rulings, which is in no repo and can never resolve.
        window = ' '.join(lines[n - 1:n + 1])
        q = QUOTE.search(window)
        if not q:
            continue
        # A quote attributed to a person is a spoken ruling, not a quotation of the
        # cited file. It lives in no repo, has no hash, and can never resolve --
        # reporting it as a miss trains the reader to ignore real ones.
        if re.search(r'\b(Jon|Julia|Mary|Anton|Sam|Ojaswita|Charlie|Surendra)\b[^."]{0,40}:\s*[*_]*$',
                     window[:q.start()]):
            tally['spoken'] += 1; continue
        # A retraction has to quote the claim it withdraws, and that quote will never
        # resolve -- that is the point of it. Without an escape the tool alarms forever
        # on exactly the entries that were handled most carefully.
        if re.search(r'does not exist and never did|never did|withdrawn|retracted|'
                     r'quoted my own paraphrase|no longer exists', window, re.I):
            tally['withdrawn'] += 1; continue
        path, quote = cite.group(1), NORM(q.group(1))
        root, path = owning_repo(path)
        if root is None:
            tally['norepo'] += 1
            rows.append(('NOREPO ', sf, n, path, quote[:52], '')); continue
        tip = text_at(root, 'HEAD', path) or ''
        if quote in tip:
            tally['fresh'] += 1; continue
        if quote.lower() in tip.lower():
            tally['case'] += 1
            rows.append(('CASE   ', sf, n, path, quote[:52], 'cased differently at tip')); continue
        # not at tip -- was it ever true? look for a hash near the citation
        h = HASH.search(window) or HASH.search(' '.join(lines[max(0, n - 12):n]))
        if not h:
            tally['nopin'] += 1
            rows.append(('NOPIN  ', sf, n, path, quote[:52], 'absent at tip, no hash to check')); continue
        pinned = text_at(root, h.group(1), path)
        if pinned is None:
            tally['badhash'] += 1
            rows.append(('BADHASH', sf, n, path, quote[:52], h.group(1))); continue
        if quote in pinned:
            tally['stale'] += 1
            rows.append(('STALE  ', sf, n, path, quote[:52], f'true at {h.group(1)[:7]}, gone at tip'))
        else:
            tally['gone'] += 1
            rows.append(('GONE   ', sf, n, path, quote[:52], f'absent at {h.group(1)[:7]} too'))

for kind, sf, n, path, quote, note in rows:
    print(f'{kind} {os.path.basename(sf)}:{n}  {path}')
    print(f'          "{quote}..."  {note}')
print('\n' + ' | '.join(f'{k} {tally[k]}' for k in
      ('stale', 'gone', 'case', 'badhash', 'nopin', 'norepo', 'spoken', 'withdrawn', 'fresh') if tally[k]))
print('\nfresh is the only status that needs nothing. nopin cannot tell stale from wrong.')
sys.exit(1 if tally['stale'] or tally['gone'] else 0)
