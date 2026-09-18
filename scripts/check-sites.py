#!/usr/bin/env python3
"""Check every `| File | Line | Current | Proposed |` row in tmp/staging/STAGED-*.md against
the working tree. Reports drift. Applies nothing.

  anchored  Current text found at the cited line          -> row is live
  drifted   found, but elsewhere -> line number is stale, text is good
  gone      not found anywhere   -> row is stale; go look
  described Current is prose about the site, not a quote  -> unanchorable by design
  malformed Current has no text left after normalizing    -> the row cannot be checked

An empty probe matches every window, so without the malformed guard a row whose Current
cell is only markup reports `anchored` against any line number, including one that does
not exist.

Adapted 2026-09-17 from `compositional-biology-theory` `tmp/tools/check-sites.py`, written by
that session 2026-09-14. Two changes: staging lives in `tmp/staging/` here, and this sits in
`scripts/` because staging proposals are untracked and the thing that checks them is
infrastructure.

Two ways to get a clean run that means nothing, both found in practice:

  * **The header must read exactly `| File | Line | Current | Proposed |`.** Any other column
    names and the table is skipped in silence, which reads like no drift.
  * **Keep the `Current` cell to the quoted text alone.** Commentary beside the quote reports
    a false GONE, and a checker that cries wolf gets ignored.
"""
import re, os, glob, collections

os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
HDR  = re.compile(r'^\|\s*File\s*\|\s*Line\s*\|\s*Current\s*\|\s*Proposed\s*\|', re.I)
NORM = lambda t: re.sub(r'\s+', ' ', re.sub(r'[>*`_]', '', t.replace('\\|', '|'))).strip()

def unquote(s):
    s = s.strip()
    while len(s) > 1 and s[0] in '`"“*' and s[-1] in '`"”*':
        s = s[1:-1].strip()
    return s

tally = collections.Counter()
for sf in sorted(glob.glob('tmp/staging/STAGED-*.md')):
    out, intable = [], False
    for raw in open(sf, encoding='utf-8'):
        if HDR.match(raw): intable = True; continue
        if not intable: continue
        if not raw.startswith('|'): intable = False; continue
        if set(raw.strip()) <= set('|- :'): continue
        c = [x.strip() for x in re.split(r'(?<!\\)\|', raw.strip().strip('|'))]
        if len(c) < 4: continue
        path = re.sub(r'^\[|\]\(.*$', '', unquote(c[0])).strip('`* ')
        if not path.endswith('.md'): continue
        m, cur = re.match(r'^\**:?(\d+)', c[1].strip()), unquote(c[2])
        if not os.path.exists(path):
            out.append(f'  NO FILE   {path}:{c[1].strip()}'); tally['nofile'] += 1; continue
        if not m or not cur or cur in ('—', '-'):
            tally['skip'] += 1; continue
        n, lines = int(m.group(1)), open(path, encoding='utf-8').read().split('\n')
        probe = NORM(cur)[:60]
        win   = lambda a, b: NORM(' '.join(lines[max(0, a):b]))
        if not probe:
            out.append(f'  MALFORMED {path}:{n}  "{cur[:44]}"'); tally['malformed'] += 1; continue
        if probe in win(n - 4, n + 4):
            tally['anchored'] += 1; continue
        where = [i + 1 for i in range(len(lines)) if probe in win(i - 1, i + 3)]
        if where:
            out.append(f'  DRIFTED   {path}:{n} -> {where[:3]}  "{cur[:44]}"'); tally['drifted'] += 1
        elif re.match(r'^(the|its)\s', cur, re.I):
            out.append(f'  DESCRIBED {path}:{n}  "{cur[:44]}"'); tally['described'] += 1
        else:
            out.append(f'  GONE      {path}:{n}  "{cur[:44]}"'); tally['gone'] += 1
    if out:
        print(os.path.basename(sf)); [print(o) for o in out]; print()

print(' | '.join(f'{k} {tally[k]}' for k in
      ('anchored','drifted','gone','described','malformed','nofile','skip') if tally[k]))
