#!/usr/bin/env python3
"""
check-template-compliance.py — a page's sections against the template it was
written from.

Four failures, and the third is the one a hand sweep misses.

  SHAPE: a page carries the template's sections out of the template's order.
  Order is the template's claim about how a reader moves through the page, so a
  Credits section above Materials is a finding even though both are present.

  LEVEL: a page's top-level sections are `##` where the template puts `#`.
  `docs/implementations/emitter-ivhsl/main.md` is the live case. Anything that
  counts `#` headings sees no sections there at all and reports the page clean,
  which is how a corpus number gets published containing the very thing the
  count was taken to find. So the level a page actually uses is measured first,
  the sections are read at that level, and the mismatch is its own finding.

  ORPHAN: a top-level heading that is in no template and on no allowlist. The
  allowlist is ALLOWED_EXTRA below and it is short on purpose — an undocumented
  heading is a finding against the guide, not against the page, and the fix may
  well be to add it here rather than to rename the heading.

  MISSING: Overview and Credits on a Module page, Credits on a Process page.
  Only those. "Omit a section rather than stubbing it empty" (style-guide/
  sections.md) means absence is normally correct, so a completeness check that
  demanded every template section would report noise rather than findings.

Sub-headings are not checked. Protocol step names, Expected Behavior contexts
and population tabs are all free text, and style-guide/sections.md says of the
context list: "That list is a template convention, not an ontology ... Do not
write a rule that depends on the set being closed."

Local-only. Not wired into .github/ — composition and shape tooling is built
before it is enforced.

Usage:
    python3 scripts/check-template-compliance.py
    python3 scripts/check-template-compliance.py docs/modules
    python3 scripts/check-template-compliance.py docs/modules/base-cell/spec.md
"""

import re
import sys
from pathlib import Path

# --- the templates ---------------------------------------------------------
#
# Each tuple is the literal top-level heading order of the file named beside
# it. These are read off the templates, which are the authority. They are NOT
# read off style-guide/sections.md, whose order line is stale: it reads
# "Overview, Reference Composition, Expected Behavior, Requirements,
# Implementations, Processes, Materials, Downloads, Credits" and omits
# `Constituent Modules`, a section the same file's body treats as real (it is
# one of two strings the diagram generator matches with hardcoded text) and
# which both Module templates place immediately before Credits, calling it
# "the last section before Credits". Follow the templates and the body; the
# order line needs an edit.

MODULE_FUNCTIONAL = (
    "Overview",
    "Reference Composition",
    "Expected Behavior",
    "Requirements",
    "Implementations",
    "Processes",
    "Materials",
    "Downloads",
    "Constituent Modules",
    "Credits",
)

MODULE_FORMULATION = (
    "Overview",
    "Reference Composition",
    "Expected Behavior",
    "Requirements",
    "Implementations",
    "Processes",
    "Materials",
    "Constituent Modules",
    "Credits",
)

PROCESS = (
    "Overview",
    "Materials and Equipment",
    "Protocol",
    "Quality Control",
    "Credits",
    "Downloads",
)

IMPLEMENTATION = (
    "Overview",
    "Modules",
    "Processes",
    "Protocol as run",
    "Observed Performance",
    "Credits",
)

TEMPLATE_FILE = {
    MODULE_FUNCTIONAL: "templates/module-template/spec-functional.md",
    MODULE_FORMULATION: "templates/module-template/spec-formulation.md",
    PROCESS: "templates/process-template/process-make_template.md",
    IMPLEMENTATION: "templates/implementation-template/implementation-template.md",
}

# The two Module templates agree on every section except `Downloads`, which the
# functional one carries and the formulation one does not — and `Downloads` is
# allowlisted below in any case. So picking the wrong one of the two changes
# which filename a finding names and nothing else. That will stop being true
# when spec-class.md lands, which is a third shape rather than a variant.
MODULE_UNION = MODULE_FUNCTIONAL

# --- the allowlist ---------------------------------------------------------
#
# A top-level heading that is legitimate on a page whose own template does not
# list it. Two entries, both ruled:
#
#   Materials — a Module page may carry purchased reagents whatever else it
#   carries, and the functional template, the formulation template and the
#   process template each have a form of it. A page that acquires one is not
#   deviating from its template.
#
#   Downloads — generated protocol and BOM artifacts. The functional Module
#   template and the process template carry it; the formulation template does
#   not, and a formulation that gains a BOM should not have to change template
#   to say so.
#
# Nothing else, and `Open` in particular is absent because it is not yet
# decided — it belongs here or it does not, and until that is settled a page
# carrying it should say so out loud. `Acknowledgments`, `Process` (singular)
# and `Expected Performance` are findings: the corpus settled on `Credits`,
# `Processes` and `Observed Performance`, and a page using the other word is
# drifting from the guide. Add an entry here only with a line saying why it is
# legitimate — the point of a written allowlist is that an undocumented
# heading becomes a finding against this file rather than a silent pass.
ALLOWED_EXTRA = frozenset({"Materials", "Downloads"})

# Required regardless of what else the page omits, per the ruled scope.
REQUIRED = {
    "module": ("Overview", "Credits"),
    "process": ("Credits",),
    "implementation": (),
}


def canonical(title: str, template: tuple[str, ...]) -> str | None:
    """The template section `title` names, ignoring case, else None.

    Case-insensitive on purpose. `make-ribosomes` writes `## Quality Control`
    and `make-trna` writes `## Quality control`, and both are the template's
    `# Quality Control` sitting a level too deep. Matching exactly would report
    one and not the other, which reads as a rule about capital letters.
    Casing itself is not reported — that is Vale's job, not this one's.
    """
    lowered = title.casefold()
    for section in template:
        if section.casefold() == lowered:
            return section
    return None

# --- heading parsing -------------------------------------------------------
#
# Fence-aware. A `#` inside a fenced code block, inside a `:::{directive}`
# block or inside an HTML comment is not a heading — the templates are full of
# all three, and a parser that counted them would read `# Title format:` out of
# a frontmatter comment as a section. Directive fences nest by colon count
# (`:::::{tab-set}` holds `::::{tab-item}` holds `:::{table}`), so they need a
# stack and not a boolean.

_DIRECTIVE_OPEN = re.compile(r"^(:{3,})\s*\{")
_DIRECTIVE_CLOSE = re.compile(r"^(:{3,})\s*$")
_CODE_FENCE = re.compile(r"^(`{3,}|~{3,})(.*)$")
_HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*$")
_TITLE = re.compile(r"^title:\s*(.*?)\s*$")


def headings(text: str) -> list[tuple[int, int, str]]:
    """Every real heading in the page, as (line number, level, text)."""
    found: list[tuple[int, int, str]] = []
    in_frontmatter = False
    in_comment = False
    code_fence: tuple[str, int] | None = None
    directives: list[int] = []

    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()

        if lineno == 1 and stripped == "---":
            in_frontmatter = True
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            continue

        # A code fence swallows everything, comments and directives included,
        # until a fence of the same character and at least the same length.
        if code_fence is not None:
            match = _CODE_FENCE.match(stripped)
            if (
                match
                and match.group(1)[0] == code_fence[0]
                and len(match.group(1)) >= code_fence[1]
                and not match.group(2).strip()
            ):
                code_fence = None
            continue
        match = _CODE_FENCE.match(stripped)
        if match:
            code_fence = (match.group(1)[0], len(match.group(1)))
            continue

        if in_comment:
            if "-->" in line:
                in_comment = False
            continue
        if stripped.startswith("<!--"):
            if "-->" not in line:
                in_comment = True
            continue

        match = _DIRECTIVE_CLOSE.match(stripped)
        if match and directives:
            depth = len(match.group(1))
            for i in range(len(directives) - 1, -1, -1):
                if directives[i] == depth:
                    del directives[i:]
                    break
            else:
                # Unbalanced. Close the innermost rather than leaving the rest
                # of the page swallowed.
                directives.pop()
            continue
        match = _DIRECTIVE_OPEN.match(stripped)
        if match:
            directives.append(len(match.group(1)))
            continue
        if directives:
            continue

        match = _HEADING.match(line)
        if match:
            found.append((lineno, len(match.group(1)), match.group(2)))

    return found


def frontmatter_title(text: str) -> str:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return ""
    for line in lines[1:]:
        if line.strip() == "---":
            break
        match = _TITLE.match(line)
        if match:
            return match.group(1).strip().strip("\"'")
    return ""


# --- genre -----------------------------------------------------------------
#
# Which Module template a page was written from is not recorded anywhere on the
# page, so it is inferred from the words in its title and directory name. The
# two word lists are the ones the templates give for themselves: the functional
# template is "a part you add to someone else's recipe: detectors, reporters,
# effectors, emitters, controls, membrane pores, energy", the formulation
# template is "something you mix: cytosols, membranes, chassis, cells, dye
# liposomes".
#
# Functional wins a tie, because every tie in the corpus is a functional module
# named after what it sits in — a Membrane Pore is a pore, not a membrane.

_FUNCTIONAL_WORDS = frozenset(
    {"detector", "reporter", "effector", "emitter", "control", "pore", "energy"}
)
_FORMULATION_WORDS = frozenset(
    {"cytosol", "membrane", "chassis", "cell", "liposome"}
)


def _words(*parts: str) -> set[str]:
    out = set()
    for part in parts:
        for token in re.split(r"[^a-z]+", part.lower()):
            if token:
                out.add(token)
                out.add(token.rstrip("s"))
    return out


def module_template(path: Path, text: str):
    """The Module template this page was written from, or None if unclear."""
    found = _words(frontmatter_title(text), path.parent.name)
    if found & _FUNCTIONAL_WORDS:
        return MODULE_FUNCTIONAL
    if found & _FORMULATION_WORDS:
        return MODULE_FORMULATION
    return None


def is_class_page(path: Path, text: str, levels: list[tuple[int, int, str]]) -> bool:
    """A class page: an abstract Module that other Modules refine.

    Two signals, because the corpus is mid-move. A `spec.yml` beside the page
    declaring `abstract:` is the machine-readable one. A `# Members` heading is
    the readable one — the class template's second section is "Reference
    Composition or Members", and no other template has Members at all.
    """
    spec_yml = path.parent / "spec.yml"
    if spec_yml.is_file():
        try:
            if re.search(r"^abstract:", spec_yml.read_text(encoding="utf-8"), re.M):
                return True
        except OSError:
            pass
    top = min((level for _, level, _ in levels), default=0)
    return any(
        level == top and title.casefold() == "members" for _, level, title in levels
    )


# --- the checks ------------------------------------------------------------


def check_page(path: Path, text: str, kind: str) -> tuple[list[str], str | None]:
    """Findings for one page, plus a note where the page could not be checked.

    Returns (findings, note). A note means the page was skipped and says why;
    skips are printed, never silent, because a skip the reader cannot see is
    indistinguishable from a pass.
    """
    rel = path.as_posix()
    heads = headings(text)

    if not heads:
        return ([f"{rel}  no headings — the page has no sections to check"], None)

    if kind == "module":
        if is_class_page(path, text, heads):
            return (
                [],
                f"{rel}  skipped: class page, and "
                "templates/module-template/spec-class.md is not in this tree",
            )
        template = module_template(path, text)
        note = None
        if template is None:
            template = MODULE_UNION
            note = (
                f"{rel}  genre not inferable from the title — checked against "
                "the union of the two Module templates"
            )
    elif kind == "process":
        if path.name != "main.md":
            return (
                [],
                f"{rel}  skipped: parent page (`*-main.md`), and no template "
                "describes one",
            )
        template, note = PROCESS, None
    else:
        template, note = IMPLEMENTATION, None

    findings: list[str] = []
    template_file = TEMPLATE_FILE[template]

    # LEVEL. Measure the level the page actually uses before reading sections
    # off it, so a page written entirely at `##` is still read rather than
    # coming back empty.
    top = min(level for _, level, _ in heads)
    if top != 1:
        line = next(n for n, level, _ in heads if level == top)
        findings.append(
            f"{rel}:{line}  top-level sections are H{top}; {template_file} puts "
            f"them at H1 — promote every section heading one level"
        )

    sections = [(n, title) for n, level, title in heads if level == top]
    seen = {canonical(title, template) for _, title in sections}

    for line, level, title in heads:
        if level > top and canonical(title, template):
            findings.append(
                f"{rel}:{line}  '{title}' is a top-level section of "
                f"{template_file} but sits at H{level} — promote it, or rename "
                "it if it is a sub-heading that happens to share the name"
            )

    # ORPHAN.
    allowed = {a.casefold() for a in ALLOWED_EXTRA}
    for line, title in sections:
        if not canonical(title, template) and title.casefold() not in allowed:
            findings.append(
                f"{rel}:{line}  orphan section '{title}' — not in "
                f"{template_file} and not in ALLOWED_EXTRA"
            )

    # SHAPE. Only sections the template names take part; an orphan has no
    # position to be out of.
    furthest, previous = -1, None
    for line, title in sections:
        name = canonical(title, template)
        if name is None:
            continue
        position = template.index(name)
        if position < furthest:
            findings.append(
                f"{rel}:{line}  '{title}' comes after '{previous}'; "
                f"{template_file} puts it before"
            )
        else:
            furthest, previous = position, title

    # MISSING.
    for title in REQUIRED[kind]:
        if title not in seen:
            index = template.index(title)
            where = (
                f"after '{template[index - 1]}'" if index else "at the top of the page"
            )
            findings.append(
                f"{rel}  missing required section '{title}' — add it {where}, "
                f"per {template_file}"
            )

    return findings, note


# --- discovery -------------------------------------------------------------


def collect(docs: Path) -> list[tuple[Path, str]]:
    """Every page the three hierarchies hold, with the kind it is.

    A Module is its directory's `spec.md`; its other pages (protocol-cells.md,
    bom-cytosol.md) are not specs and have no template. A Process is a
    `main.md` or, for a parent, a `<dir>-main.md`, at any depth, since
    sub-protocols nest. A page sitting directly in `docs/<hierarchy>/` is that
    hierarchy's index, not a page in it.
    """
    pages: list[tuple[Path, str]] = []

    for spec in sorted((docs / "modules").glob("*/spec.md")):
        pages.append((spec, "module"))

    for page in sorted((docs / "processes").rglob("*.md")):
        if page.parent == docs / "processes":
            continue
        if page.name == "main.md" or page.name.endswith("-main.md"):
            pages.append((page, "process"))

    for page in sorted((docs / "implementations").glob("*/main.md")):
        pages.append((page, "implementation"))

    return pages


def run(docs: Path, only: list[Path] | None = None):
    findings: list[str] = []
    notes: list[str] = []
    checked = 0
    for path, kind in collect(docs):
        if only and not any(
            path == p or p in path.parents for p in only
        ):
            continue
        checked += 1
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:  # pragma: no cover
            findings.append(f"{path.as_posix()}  unreadable: {exc}")
            continue
        page_findings, note = check_page(path, text, kind)
        findings.extend(page_findings)
        if note:
            notes.append(note)
    return findings, notes, checked


def main(argv: list[str] | None = None) -> int:
    args = [a for a in (argv if argv is not None else sys.argv[1:]) if not a.startswith("-")]
    only = [Path(a) for a in args] or None

    findings, notes, checked = run(Path("docs"), only)

    for note in notes:
        print(note)
    if notes:
        print()

    if findings:
        for finding in findings:
            print(finding)
        print(f"\n{len(findings)} finding(s) across {checked} page(s) checked.")
        print(
            "    Fix a page by giving it the shape of its template in templates/. "
            "Fix the\n    guide instead by adding the heading to ALLOWED_EXTRA in "
            "this script, with a\n    line saying why it is legitimate."
        )
        return 1

    print(f"✅ {checked} page(s) match their templates.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
