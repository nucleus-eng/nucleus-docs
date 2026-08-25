#!/usr/bin/env python3
"""
check-composition-tabs.py — a Module's Reference Composition tabs must cover
everything its own dependency graph contains.

The generated `Module Dependencies` diagram already computes the transitive
closure of `# Constituent Modules`. If a membrane is in that closure, the page
composes a membrane, so Reference Composition needs a Membrane tab. A page
missing one reads as "this Module has no membrane", which is a stronger claim
than "we did not write the composition down".

This catches absence, which a prose-quality pass cannot see: a page can score
clean on wording while missing half its composition.

A tab may say the composition is not documented. It may not be absent.

Waivers, for the cases where a node genuinely implies no tab — a reporter
supplied as purified enzyme rather than expressed from DNA, say — go on the
page as an HTML comment naming the tab and the reason:

    <!-- composition-tabs: no-dna (LacZ is added as purified enzyme) -->

Usage:
    python3 scripts/check-composition-tabs.py
    python3 scripts/check-composition-tabs.py docs/modules/ph-cascade/
"""

import re
import sys
from pathlib import Path

MODULES_ROOT = Path("docs/modules")

BEGIN = "<!-- gen:composition-diagram -->"
END = "<!-- /gen:composition-diagram -->"

# A diagram node prefix implies a tab. Keys are matched as prefixes of the
# UPPER_SNAKE node id the generator emits from a module directory name.
#
# Cytosol and Inner Solution are alternatives, not synonyms: Cytosol names what
# fills the compartment, Inner Solution names the compartment. Either satisfies.
IMPLIES = [
    ("MEMBRANE", ("Membrane",), "membrane"),
    ("BASE_CYTOSOL", ("Cytosol", "Inner Solution"), "cytosol"),
    ("S30_LYSATE", ("Cytosol", "Inner Solution"), "cytosol"),
    ("SUBSTRATE", ("Substrate", "Inner Solution"), "substrate"),
    ("DETECTOR", ("DNA",), "dna"),
    ("REPORTER", ("DNA",), "dna"),
    ("EFFECTOR", ("DNA",), "dna"),
    ("EMITTER", ("DNA",), "dna"),
    ("CONTROL", ("DNA",), "dna"),
    ("ENERGY", ("DNA",), "dna"),
]

WAIVER = re.compile(r"<!--\s*composition-tabs:\s*no-([a-z]+)\b", re.I)


HEADING = re.compile(r"^(#{1,6})[ \t]+(.+?)[ \t]*$", re.M)


def section_bodies(text: str, title: str) -> list[str]:
    """Bodies under every heading named `title`, at whatever depth.

    Each body ends at the next heading of the same or shallower depth. Pages
    carry this section at H1, H2 or H3 depending on template, and a page with
    both a Cytosols and a Cells arm carries two of them.
    """
    out = []
    for m in HEADING.finditer(text):
        if m.group(2).strip() != title:
            continue
        depth = len(m.group(1))
        rest = text[m.end():]
        end = len(rest)
        for n in HEADING.finditer(rest):
            if len(n.group(1)) <= depth:
                end = n.start()
                break
        out.append(rest[:end])
    return out


def diagram_nodes(text: str) -> set[str]:
    """Node ids declared inside the generated block."""
    if BEGIN not in text or END not in text:
        return set()
    block = text.split(BEGIN, 1)[1].split(END, 1)[0]
    return set(re.findall(r"^\s+([A-Z][A-Z0-9_]*)\[", block, re.M))


def tab_titles(text: str) -> list[str]:
    return re.findall(r"^:*\{tab-item\}\s*(.+?)\s*$", text, re.M)


def composition_surface(text: str) -> str:
    """Tab titles plus table captions and labels inside Reference Composition.

    A population tab such as `AHL Sensing Cell` satisfies the Membrane
    requirement by carrying a captioned membrane table, so matching tab titles
    alone reports a false gap. This searches the whole section instead.
    """
    sections = section_bodies(text, "Reference Composition")
    if not sections:
        return " | ".join(tab_titles(text))
    parts = []
    for section in sections:
        parts += re.findall(r"^:*\{tab-item\}\s*(.+?)\s*$", section, re.M)
        parts += re.findall(r"^:*\{table\}\s*(.+?)\s*$", section, re.M)
        parts += re.findall(r"^:(?:label|name):\s*(\S+)\s*$", section, re.M)
    return " | ".join(parts)


def check(path: Path) -> tuple[list[str], list[str]]:
    """Return (errors, advisories)."""
    text = path.read_text(encoding="utf-8")
    waived = {m.lower() for m in WAIVER.findall(text)}

    # A composition tab should carry a table. A Module that genuinely takes
    # several hosts is the exception, so this warns rather than fails.
    advisories = []
    if "table" not in waived:
        sec = "\n".join(section_bodies(text, "Reference Composition"))
        for blk in re.split(r"^:*\{tab-item\} ", sec, flags=re.M)[1:]:
            title = blk.split("\n", 1)[0].strip()
            if title in ("Module Dependencies", "Schematic"):
                continue
            if ":::{table" not in blk and not re.search(r"^\|", blk, re.M):
                advisories.append(
                    f"{path}: the '{title}' tab has no table — a composition tab "
                    "carries a table, not a sentence pointing elsewhere"
                )

    nodes = diagram_nodes(text)
    if not nodes:
        return [], advisories

    # A page's own node is not a constituent of itself.
    own = path.parent.name.upper().replace("-", "_")
    nodes.discard(own)

    tabs = composition_surface(text)

    findings = []
    for prefix, accepted, key in IMPLIES:
        matching = sorted(n for n in nodes if n.startswith(prefix))
        if not matching or key in waived:
            continue
        if any(a.lower() in tabs.lower() for a in accepted):
            continue
        findings.append(
            f"{path}: dependency graph contains {', '.join(matching)} "
            f"but there is no {' or '.join(accepted)} tab"
        )
    return findings, advisories


def unreachable_specs(targets: list[Path]) -> list[Path]:
    """Module pages this script cannot see, because they are misnamed.

    `style-guide/page-types.md` puts a Module spec at `docs/modules/<name>/spec.md`.
    A page named `<name>-spec.md` is still a spec to a reader, but it is invisible
    to the glob below — so the run would report success over a corpus it never
    looked at. Silently checking fewer pages than exist is the one failure a
    checker must not have.
    """
    return sorted(
        {
            s
            for t in targets
            if not t.is_file()
            for s in t.rglob("*spec.md")
            if s.name != "spec.md"
        }
    )


def main() -> int:
    targets = [Path(a) for a in sys.argv[1:]] or [MODULES_ROOT]
    specs = sorted(
        {s for t in targets for s in ([t] if t.is_file() else t.rglob("spec.md"))}
    )
    unreachable = unreachable_specs(targets)
    if not specs and not unreachable:
        print("error: no spec.md found in the given path(s)", file=sys.stderr)
        return 2

    findings, advisories = [], []
    for spec in specs:
        e, a = check(spec)
        findings += e
        advisories += a
    checked = sum(1 for s in specs if diagram_nodes(s.read_text(encoding="utf-8")))

    for a in advisories:
        print(f"warning: {a}")

    for u in unreachable:
        print(
            f"error: {u}: a Module spec lives at <name>/spec.md, so nothing "
            "checks this page — rename it or move it into its own directory"
        )

    for f in findings:
        print(f"error: {f}")

    summary = []
    if findings:
        pages = len({f.split(":")[0] for f in findings})
        summary.append(
            f"{len(findings)} missing tab(s) across {pages} page(s) — a tab may "
            "say the composition is not documented; it may not be absent"
        )
    if unreachable:
        summary.append(f"{len(unreachable)} Module page(s) the check cannot reach")

    if summary:
        print("\n" + ". ".join(summary) + ".")
        return 1

    note = f" {len(advisories)} advisory." if advisories else ""
    print(f"✅ Composition tabs cover the dependency graph. {checked} page(s) checked.{note}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
