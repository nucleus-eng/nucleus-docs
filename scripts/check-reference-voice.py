#!/usr/bin/env python3
"""
check-reference-voice.py — flag text on docs pages that describes our work on a
Module instead of the Module.

Docs pages are reference documentation. style-guide/principles.md asks one
question of every prose block: does this describe the Module, or our work on
it? style-guide/conventions.md lists what the second kind looks like. This
script finds the commonest markers of it. It is a net, not the rule: a page can
pass this check and still read as a decision log, and only reading finds that.

Tier 1 — errors, exit 1:
  person        a contributor's first name without their surname ("Ashford ruled",
                "on Ashford's word"), or "<Name>, <date>". A full name is fine, so
                Credits pass. Names come from about/contributors.md. A line
                citing "(Group Meeting, contributor, date)" or "personal
                communication" passes this rule and the date rule: those
                forms are an Editor's choice, and an agent must not write
                them (see style-guide/principles.md).
  ruling        "ruled" or "ruling". "ruled out" is fine.
  working-notes a pointer into our working notes: compositional-biology-theory,
                "the theory corpus", open.md / rulings.md / glossary.md /
                signature.md. A reader cannot follow them.
  review-tag    an @-tag other than @Editor or @Developer, such as @Claude.

Tier 2 — warnings, exit 0 unless --strict:
  date          an ISO date in prose ("Written 2026-09-24", "until 2026-09-29")
  corpus-talk   "this corpus", "the corpus", "this tranche"
  tooling       a script path, spec.yml, "the composition source", a `function()`
  hash          a commit hash in backticks

Frontmatter, fenced code, HTML comments, link targets and bare URLs are
skipped. The text between <!-- gen:... --> markers is checked, because it
renders.

Usage:
    python3 scripts/check-reference-voice.py               # check docs/
    python3 scripts/check-reference-voice.py docs/modules  # check specific path(s)
    python3 scripts/check-reference-voice.py --strict      # warnings fail too

Exit codes: 0 clean (warnings allowed), 1 findings, 2 nothing was checked: no
contributor names read, a path that does not exist, or no markdown file found.
"""

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
CONTRIBUTORS = REPO / "about" / "contributors.md"

# "- Robin Ashford — b.next" -> ("Robin", "Ashford")
_CONTRIBUTOR_RE = re.compile(r"^-\s+(\S+)\s+(.+?)\s+—\s")

_ISO_DATE = r"20\d\d-\d\d-\d\d"

# Link targets and bare URLs are addresses, not prose. A dated URL or a link to a
# page named glossary.md is not a finding; the link text around it still is.
_LINK_TARGET = re.compile(r"\]\([^)]*\)")
_URL = re.compile(r"\bhttps?://\S+")

TIER1 = {
    "ruling": (
        # `(?!\.md)` keeps the filename `rulings.md` out of this rule. A filename is
        # an address, the same reason `_LINK_TARGET` is blanked out, and the pointer
        # itself is already what `working-notes` is for. It fired on
        # effector-pla1/spec.yml, which cites `rulings.md#D35` for associativity.
        re.compile(r"\b[Rr]ul(?:ed|ings?)\b(?! out)(?!\.md)"),
        "records a ruling. State the result; the commit message records who decided.",
    ),
    "working-notes": (
        re.compile(
            r"compositional-biology-theory"
            r"|\b[Tt]heory corpus\b"
            r"|\b(?:open|rulings|glossary|signature)\.md\b"
        ),
        "points into our working notes, which a reader cannot follow. State the content, or leave it out.",
    ),
    "review-tag": (
        re.compile(r"(?<![\w.])@(?!Editor\b|Developer\b)[A-Z][A-Za-z]+"),
        "is a review tag. Resolve it before the page ships.",
    ),
}

TIER2 = {
    "date": (
        re.compile(rf"\b{_ISO_DATE}\b"),
        "dates the text. Check it describes the Module, not our work on it.",
    ),
    "corpus-talk": (
        re.compile(r"\b(?:[Tt]his|[Tt]he) corpus\b|\b[Tt]his tranche\b"),
        "talks about the corpus, not the Module.",
    ),
    "tooling": (
        re.compile(r"scripts/[\w-]+\.py|\bspec\.yml\b|\bcomposition source\b|`[a-z_]+\(\)`"),
        "makes our tooling the subject. Tooling keeps the pages right; it is not what a page describes.",
    ),
    "hash": (
        re.compile(r"`(?=[0-9a-f]*[a-f])(?=[0-9a-f]*\d)[0-9a-f]{7,40}`"),
        "cites a commit. Git records it; the reader cannot use it.",
    ),
}

# The two citation forms an Editor may choose for a fact with no document behind it.
EDITOR_CITATION = re.compile(r"\(Group Meeting,|personal communication")

PERSON_MESSAGE = "says who decided or who said so. State the result; the commit message records who decided."


def read_contributors(path: Path) -> list[tuple[str, str]]:
    """Return (first name, rest of name) for each contributor listed in path."""
    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError:
        return []
    names = []
    for line in lines:
        m = _CONTRIBUTOR_RE.match(line.strip())
        if m:
            names.append((m.group(1), m.group(2)))
    return names


# NOUNS THAT ARE NOT PEOPLE, for the "<Name>, <date>" catch-all below. An
# institution confirming something is evidence, not a person deciding it, and
# the sweep of 2026-10-03 kept those sources for that reason — vendor datasheets,
# catalog numbers, and a Node's confirmation of a construct's structure. The
# catch-all cannot tell "Node, 2026-09-09" from a surname and a date.
NOT_A_PERSON = ("Node", "Meeting")


def person_pattern(names: list[tuple[str, str]]) -> re.Pattern:
    """A first name not followed by that contributor's surname, or "<Name>, <date>"."""
    by_first: dict[str, list[str]] = {}
    for first, rest in names:
        by_first.setdefault(first, []).append(rest)
    alternatives = []
    for first, rests in sorted(by_first.items()):
        surnames = "|".join(re.escape(r) for r in rests)
        alternatives.append(rf"\b{re.escape(first)}\b(?!\s+(?:{surnames})\b)")
    not_person = "|".join(NOT_A_PERSON)
    alternatives.append(rf"\b(?!(?:{not_person})\b)[A-Z][a-z]+, {_ISO_DATE}\b")
    return re.compile("|".join(alternatives))


def visible_lines(text: str) -> list[tuple[int, str]]:
    """Return (lineno, line) for lines that render, with comments blanked out."""
    out = []
    lines = text.splitlines()
    in_frontmatter = bool(lines) and lines[0].strip() == "---"
    fence = None
    in_comment = False
    for i, raw in enumerate(lines, start=1):
        stripped = raw.strip()
        if in_frontmatter:
            if i > 1 and stripped == "---":
                in_frontmatter = False
            continue
        if fence:
            if stripped.startswith(fence):
                fence = None
            continue
        m = re.match(r"^(`{3,}|~{3,})", stripped)
        if m and not in_comment:
            fence = m.group(1)
            continue
        # Blank out HTML comments, which may open and close on different lines.
        line = ""
        rest = raw
        while rest:
            if in_comment:
                end = rest.find("-->")
                if end == -1:
                    rest = ""
                else:
                    in_comment = False
                    rest = rest[end + 3:]
            else:
                start = rest.find("<!--")
                if start == -1:
                    line += rest
                    rest = ""
                else:
                    line += rest[:start]
                    in_comment = True
                    rest = rest[start + 4:]
        if line.strip():
            out.append((i, line))
    return out


# TWO RULES ARE EXEMPT IN A `spec.yml`, FOR DIFFERENT REASONS.
#
# `tooling` complains that our tooling has become the subject of a page. Almost
# every hit in a source file is the word `spec.yml` written inside a `spec.yml`,
# where the file IS the tooling and naming it is the only way to say anything.
# Keeping it would mean 114 findings nobody can act on, which is how a check
# stops being read.
#
# `working-notes` is right and is not ready. A pointer to `rulings.md#D35` is as
# unfollowable for a source reader as for a page reader, so the rule belongs
# here eventually. But it is 85 findings, which is a sweep of its own, and
# turning it on before that sweep would block every `spec.yml` change.
EXEMPT_IN_SOURCE = {"tooling", "working-notes"}


def check_file(path: Path, person: re.Pattern) -> list[tuple[int, str, str, str, str]]:
    """Return (lineno, level, rule, match, message) for each finding in path."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return []
    findings = []
    tier1 = {"person": (person, PERSON_MESSAGE), **TIER1}
    source = path.suffix == ".yml"
    for lineno, line in visible_lines(text):
        line = _URL.sub(" ", _LINK_TARGET.sub("]()", line))
        for level, rules in (("error", tier1), ("warning", TIER2)):
            for rule, (pattern, message) in rules.items():
                if source and rule in EXEMPT_IN_SOURCE:
                    continue
                if rule in ("person", "date") and EDITOR_CITATION.search(line):
                    continue
                for m in pattern.finditer(line):
                    findings.append((lineno, level, rule, m.group(0), message))
    return findings


# A `spec.yml` IS A DOCS PAGE'S OTHER HALF, and this check read neither it nor
# its `#` headers until 2026-10-04. The `.md` layer went 139 findings to 0 while
# the source file beside it was never counted: 193 findings on 62 of 76 sources,
# the same who-decided text in `question:`, `notes:` and `why:` values that the
# schema defines and `check-spec-schema.py` validates. Content, not a note to the
# next editor.
SUFFIXES = (".md", ".yml")


def iter_pages(paths: list[Path]):
    for p in paths:
        if p.is_file() and p.suffix in SUFFIXES:
            yield p
        elif p.is_dir():
            yield from sorted(q for q in p.rglob("*") if q.suffix in SUFFIXES)


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("paths", nargs="*", type=Path, help="files or directories (default: docs/)")
    parser.add_argument("--strict", action="store_true", help="exit 1 on warnings as well as errors")
    parser.add_argument("--contributors", type=Path, default=CONTRIBUTORS, help=argparse.SUPPRESS)
    args = parser.parse_args(argv)

    names = read_contributors(args.contributors)
    if not names:
        # With no names the person rule can never fire, and a clean run would mean nothing.
        print(f"check-reference-voice: no contributor names read from {args.contributors}", file=sys.stderr)
        return 2
    person = person_pattern(names)

    paths = args.paths or [REPO / "docs"]
    missing = [p for p in paths if not p.exists()]
    if missing:
        # A path that is not there checks nothing, and a clean run over nothing is not a pass.
        for p in missing:
            print(f"check-reference-voice: no such file or directory: {p}", file=sys.stderr)
        return 2
    errors = warnings = checked = 0
    for path in iter_pages(paths):
        checked += 1
        for lineno, level, rule, match, message in check_file(path, person):
            try:
                shown = path.resolve().relative_to(REPO)
            except ValueError:
                shown = path
            print(f"{shown}:{lineno}: {level} [{rule}] '{match}' {message}")
            if level == "error":
                errors += 1
            else:
                warnings += 1

    if not checked:
        print("check-reference-voice: no markdown files found in the given paths", file=sys.stderr)
        return 2
    print(f"check-reference-voice: {errors} error(s), {warnings} warning(s) in {checked} file(s)", file=sys.stderr)
    if errors or (args.strict and warnings):
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
