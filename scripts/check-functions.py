#!/usr/bin/env python3
"""Check the Function pages: the hub's rows, each page's members, and the signature's count.

Three passes. The first two read only this repo and are safe in CI. The third reads the
theory repo's signature, so it runs only where a checkout is found, and says so when it
is not.

  HUB       Every row of the table in docs/functions/functions-main.md is in one of
            three states: a link to a page that exists, a reason it has none (a cell
            that starts "No page" or "No Function page"), or "To be written". The three
            are counted and printed. A row in none of them, or a link that does not
            resolve, fails the run. "To be written" is a backlog, not a failure.
  MEMBERS   For each Function page named in scripts/function-members.yml, the Modules its
            `# Routes` section links are compared with the members of the class that
            performs it: every Module that refines that class, directly or through a
            subclass, and is not itself refined. A member the page leaves out on purpose
            is listed in that file with its reason. Reported and never failed, because a
            member list is prose and the author decides which side is wrong.
  COVERAGE  The declared operations in the signature's Interface block are counted and
            compared with the hub's rows. A mismatch fails. Local only: CI has no
            checkout of compositional-biology-theory, and a commit there must not be
            able to turn a PR here red.

HOW THE COVERAGE PASS COUNTS. Every rule prints what it left out.
  - A declaration starts at column 0 inside the block's code fence. It is either
    `name : profile` on one line, or `name` alone with `: profile` indented on the
    next line. hydrolyse[PPi] and hydrolyse[ATP] use the second form, so a parser
    that reads only the first undercounts by exactly those two.
  - `name = ...` is a composite and is not counted: express.
  - A declaration marked "— undeclared" is not counted: translocate. The marker is
    prose, so the next edit to that line can drop it, and a test pins the rule.
  - A name whose stem is another declared name is a refinement and is not counted:
    report_color and passive_transport by their parts, degrade[ssrA] by its bracket.
    hydrolyse[PPi] is counted, because no bare `hydrolyse` is declared.
  IT COMPARES COUNTS, NOT NAMES. The hub names each function in this site's own words
  and does not quote the signature, so there is nothing to match a name against. One
  function dropped and another added in the same edit would pass. That gap is known.

The signature is read from a commit, never from the working tree: `git show REF:`, with
REF defaulting to HEAD. Uncommitted edits in that checkout are not what anyone else can
read.

    python3 scripts/check-functions.py                       # all three; coverage if found
    python3 scripts/check-functions.py --theory PATH --ref main

Exit 0 when clean, 1 on a failing finding, 2 when it could not run.
"""
import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
HUB = REPO / "docs" / "functions" / "functions-main.md"
MEMBERS_FILE = REPO / "scripts" / "function-members.yml"
MODULES = REPO / "docs" / "modules"

LINK = re.compile(r"\]\((\.[^)#\s]*?\.md)(?:#[^)]*)?\)")
MODULE_LINK = re.compile(r"\.\./\.\./modules/([A-Za-z0-9._-]+)/spec\.md")
DECL = re.compile(r"^(::|[^\s:=]+)(.*)$")
REASON = ("No page", "No Function page")
TO_WRITE = "To be written"


# ---- HUB -------------------------------------------------------------------------

def hub_rows(text):
    """(function, page cell) for each row of the table under `# Functions`."""
    m = re.search(r"^# Functions[ \t]*$(.*?)(?=^# |\Z)", text, re.M | re.S)
    rows = []
    for line in (m.group(1) if m else "").splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells[0] == "Function" or set(cells[0]) <= set("-: "):
            continue
        rows.append((cells[0], cells[-1]))
    return rows


def row_state(cell, base):
    """The row's state, or None, and any link in the cell that does not resolve."""
    broken = [t for t in LINK.findall(cell) if not (base / t).is_file()]
    if cell.startswith(REASON):
        return "reason", broken
    if cell == TO_WRITE:
        return "to-write", broken
    if LINK.search(cell):
        return "page", broken
    return None, broken


def check_hub(hub):
    """(rows, counts by state, failing messages)."""
    rows = hub_rows(hub.read_text(encoding="utf-8"))
    counts = {"page": 0, "reason": 0, "to-write": 0}
    fails = []
    for name, cell in rows:
        state, broken = row_state(cell, hub.parent)
        if state is None:
            fails.append(f"{name}: no page, no reason and not '{TO_WRITE}' — {cell!r}")
        else:
            counts[state] += 1
        for t in broken:
            fails.append(f"{name}: links {t}, which does not exist")
    return rows, counts, fails


# ---- MEMBERS ---------------------------------------------------------------------

def load_sources(modules):
    out = {}
    for p in sorted(Path(modules).glob("*/spec.yml")):
        d = yaml.safe_load(p.read_text(encoding="utf-8")) or {}
        if isinstance(d, dict) and d.get("module"):
            out[d["module"]] = d
    return out


def _parents(d):
    r = d.get("refines")
    return [] if not r else ([r] if isinstance(r, str) else list(r))


def class_members(cls, sources):
    """Every Module under `cls` through `refines:` that nothing refines in turn."""
    children = {}
    for m, d in sources.items():
        for p in _parents(d):
            children.setdefault(p, set()).add(m)
    seen, stack = set(), [cls]
    while stack:
        for c in children.get(stack.pop(), ()):
            if c not in seen:
                seen.add(c)
                stack.append(c)
    return {m for m in seen if m not in children}


def page_members(text):
    """The Modules linked in a Function page's `# Routes` section."""
    m = re.search(r"^# Routes[ \t]*$(.*?)(?=^# |\Z)", text, re.M | re.S)
    return set(MODULE_LINK.findall(m.group(1) if m else ""))


def check_members(slug, page_text, cls, not_members, sources):
    """Report lines for one page. Never failing."""
    walk = class_members(cls, sources)
    listed = page_members(page_text)
    out = []
    if not walk:
        out.append(f"{slug}: class {cls!r} has no members, so nothing was compared")
    for m in sorted(walk - listed - set(not_members)):
        out.append(f"{slug}: {m} refines {cls} and the page does not list it")
    for m in sorted(listed - walk):
        out.append(f"{slug}: lists {m}, which does not refine {cls}")
    for m in sorted(set(not_members) & listed):
        out.append(f"{slug}: {m} is excluded in {MEMBERS_FILE.name} but the page lists it")
    for m in sorted(set(not_members) - walk):
        out.append(f"{slug}: {m} is excluded but is not a member of {cls}")
    return walk, listed, out


# ---- COVERAGE --------------------------------------------------------------------

def interface_block(text):
    m = re.search(r"^### Interface\b[^\n]*\n+```[^\n]*\n(.*?)\n```", text, re.M | re.S)
    return m.group(1) if m else None


def declared(block):
    """(counted names, {excluded name: why}), in the order the block declares them."""
    lines = block.split("\n")
    found = []
    for i, line in enumerate(lines):
        if not line or line[0].isspace():
            continue
        m = DECL.match(line)
        if not m:
            continue
        name, rest = m.group(1), m.group(2).strip()
        if rest.startswith("="):
            found.append((name, "composite"))
        elif rest.startswith(":"):
            found.append((name, "undeclared" if "— undeclared" in rest else None))
        else:
            nxt = next((x for x in lines[i + 1:] if x.strip()), "")
            if nxt[:1].isspace() and nxt.strip().startswith(":"):
                found.append((name, "undeclared" if "— undeclared" in nxt else None))
    names = {n for n, _ in found}
    counted, excluded = [], {}
    for name, why in found:
        if why:
            excluded[name] = why
            continue
        stem = name.split("[")[0]
        base = sorted(p for p in {stem, *stem.split("_")} if p != name and p in names)
        if base:
            excluded[name] = f"refines {base[0]}"
        else:
            counted.append(name)
    return counted, excluded


def find_theory(explicit, ref):
    """(path, signature text, short hash), or (None, None, searched list)."""
    cands = [Path(explicit)] if explicit else [
        Path(p) for p in (os.environ.get("NUCLEUS_THEORY_REPO"),) if p] + [
        REPO.parent / "compositional-biology-theory",
        REPO.parent.parent / "compositional-biology-theory",
        Path.home() / "src" / "compositional-biology-theory"]
    for c in cands:
        show = subprocess.run(["git", "-C", str(c), "show", f"{ref}:signature.md"],
                              capture_output=True, text=True)
        if show.returncode == 0 and show.stdout:
            h = subprocess.run(["git", "-C", str(c), "rev-parse", "--short", ref],
                               capture_output=True, text=True).stdout.strip()
            return c, show.stdout, h
    return None, None, [str(c) for c in cands]


def ref_warning(repo_root, ref: str) -> str:
    """Empty, or a warning that `ref` is not what a reader would resolve.

    **The default `ref` is HEAD, and HEAD is whatever branch that checkout sits on.**
    Measured 2026-10-08: the only theory checkout on this machine was on a feature
    branch 15 commits behind `origin/main`, so every count taken that day was against
    a tree no reader shares. The count came out right by luck — the branch had not
    touched the Interface block.

    This is `check-dna-refs.py`'s defect in a second script. There the fix was to say
    which tree was read; the same applies here, and for the same reason: there is no
    ref that is right for every run, because a count against an unpushed branch is
    exactly what you want when checking your own edit before pushing it.
    """
    def _git(*a):
        r = subprocess.run(["git", "-C", str(repo_root), *a], capture_output=True, text=True)
        return r.stdout.strip() if r.returncode == 0 else None

    resolved = _git("rev-parse", ref)
    main = _git("rev-parse", "origin/main")
    if resolved is None or main is None or resolved == main:
        return ""
    behind = _git("rev-list", "--count", f"{ref}..origin/main")
    branch = _git("rev-parse", "--abbrev-ref", "HEAD") if ref == "HEAD" else ref
    extra = f", {behind} commit(s) behind it" if behind and behind != "0" else ""
    return (f"\n⚠️  COVERAGE read `{branch}`, which is NOT `origin/main`{extra}.\n"
            "    The count below is against a tree other readers may not have. Pass\n"
            "    `--ref origin/main` for the count a reader would get.")


# ---- main ------------------------------------------------------------------------

def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--theory", help="a checkout of compositional-biology-theory")
    ap.add_argument("--ref", default="HEAD", help="the commit to read signature.md at")
    a = ap.parse_args()

    if not HUB.is_file():
        print(f"⛔️ no hub at {HUB.relative_to(REPO)}; nothing to check")
        return 2
    fails = 0

    rows, counts, hub_fails = check_hub(HUB)
    for f in hub_fails:
        print(f"⛔️ HUB {f}")
    fails += len(hub_fails)
    print(f"{'✅' if not hub_fails else '⛔️'} HUB {len(rows)} row(s): {counts['page']} with a "
          f"page, {counts['reason']} with a reason, {counts['to-write']} to be written")

    spec = yaml.safe_load(MEMBERS_FILE.read_text(encoding="utf-8")) if MEMBERS_FILE.is_file() else {}
    sources = load_sources(MODULES)
    for slug, entry in (spec or {}).items():
        page = HUB.parent / slug / "main.md"
        if not page.is_file():
            print(f"⚠️  MEMBERS {slug}: named in {MEMBERS_FILE.name} and has no page")
            continue
        walk, listed, out = check_members(slug, page.read_text(encoding="utf-8"),
                                          entry["class"], entry.get("not_members") or {},
                                          sources)
        for line in out:
            print(f"⚠️  MEMBERS {line}")
        print(f"{'✅' if not out else 'ℹ️ '} MEMBERS {slug}: {len(walk)} member(s) of "
              f"{entry['class']}, {len(listed)} listed, "
              f"{len(entry.get('not_members') or {})} excluded with a reason")

    path, text, h = find_theory(a.theory, a.ref)
    if path is None:
        if a.theory:
            print(f"⛔️ COVERAGE cannot read signature.md at {a.ref} in {a.theory}")
            return 2
        print("ℹ️  COVERAGE skipped: no checkout of compositional-biology-theory found. "
              "A skip is not a pass. Searched: " + ", ".join(h))
    else:
        block = interface_block(text)
        if block is None:
            print(f"⛔️ COVERAGE no Interface block in signature.md at {h}")
            return 2
        warn = ref_warning(path, a.ref)
        if warn:
            print(warn)
        counted, excluded = declared(block)
        for name, why in excluded.items():
            print(f"ℹ️  COVERAGE not counted: {name} ({why})")
        ok = len(counted) == len(rows)
        fails += not ok
        print(f"{'✅' if ok else '⛔️'} COVERAGE {len(counted)} declared operation(s) in "
              f"signature.md at {h} ({a.ref}), {len(rows)} row(s) in the hub"
              + ("" if ok else " — they must match; counts are compared, not names"))

    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
