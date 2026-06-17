#!/usr/bin/env python3
"""
build-protocols.py — generate lab-ready protocol PDFs, BOM PDFs, and materials
CSVs from process pages.

For each process page (a ``main.md`` / ``*-main.md`` under ``docs/processes/``
that contains a ``# Protocol`` heading), this script produces, in the page's
``generated/`` directory:

  - ``<slug>-protocol.pdf``  — a pure bench checklist: title + step headings +
    ``- [ ]`` items + a brief hazard note (if the page has one). All narrative
    prose, admonitions, tables, and figures are stripped.
  - ``<slug>-bom.pdf`` + ``<slug>-materials.csv`` — generated from the page's
    table labeled ``bom-<slug>`` (only if that table exists).

``<slug>`` is the process's containing directory name. Generated artifacts are
never committed (``generated/`` is gitignored); they are rebuilt on every deploy
so they cannot drift from the source page. See issue #10 for the full design.

PDF rendering requires ``myst`` and ``typst`` on PATH. When they are absent the
script still performs extraction and writes the intermediate markdown + CSV, and
reports the skipped renders — useful for local testing of the extraction layer.

Usage:
    python3 scripts/build-protocols.py [docs/processes/...]
    python3 scripts/build-protocols.py                 # all processes
    python3 scripts/build-protocols.py --extract-only   # skip PDF rendering
"""

import csv
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import List, Optional, Tuple

# Shared BOM helpers (parse/normalize/index) — one definition across the
# generator, the label checker, the enricher, and the materials reference.
from bom_common import (  # noqa: E402  (sibling module, resolved via sys.path[0])
    TABLE_ROW_RE,
    csv_to_table_rows,
    extract_bom_table,
    table_to_csv,
)

# Branded in-repo typst template (owned + version-pinned; see its README). The
# absolute path is written into each intermediate's `exports.template` so MyST
# resolves it regardless of the intermediate's location.
TYPST_TEMPLATE_DIR = Path("templates/typst/nucleus-protocols")

PROCESSES_ROOT = Path("docs/processes")

# A checklist item: optional leading indentation, "- [ ]" or "- [x]".
CHECKLIST_RE = re.compile(r"^\s*- \[[ xX]\]")
# Any ATX heading.
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*)$")
# Any directive fence (run of 3+ colons), possibly indented.
FENCE_RE = re.compile(r"^\s*(:{3,})")
# A directive open fence: (colon run, directive name, trailing title text).
ADMONITION_OPEN_RE = re.compile(r"^\s*(:{3,})\{([^}]+)\}\s*(.*?)\s*$")
# A standalone directive option line (e.g. ":class: dropdown", ":label: ...").
DIRECTIVE_OPTION_RE = re.compile(r"^\s*:[A-Za-z_][A-Za-z0-9_-]*:")
# (TABLE_ROW_RE / TABLE_SEP_RE imported from bom_common.)


def slug_from_page(path: Path) -> str:
    """The slug is the process's containing directory name (e.g. 'make-36pot')."""
    return path.parent.name


def split_frontmatter(text: str) -> Tuple[dict, str]:
    """Return (frontmatter dict, body). Only the fields we need are parsed."""
    fm: dict = {}
    if not text.startswith("---"):
        return fm, text
    end = text.find("\n---", 3)
    if end == -1:
        return fm, text
    block = text[3:end]
    body = text[end + 4:]
    for line in block.splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fm[key.strip()] = value.strip()
    return fm, body.lstrip("\n")


def page_title(fm: dict, fallback_slug: str) -> str:
    title = fm.get("title", "").strip().strip('"').strip("'")
    return title or fallback_slug


def has_protocol_section(body: str) -> bool:
    return any(
        HEADING_RE.match(line) and HEADING_RE.match(line).group(1) == "#"
        and HEADING_RE.match(line).group(2).strip().lower() == "protocol"
        for line in body.splitlines()
    )


def extract_section(body: str, heading_text: str) -> Optional[List[str]]:
    """Return the lines of the H1 section named `heading_text` (excluding the
    heading line itself), stopping at the next H1 or end of file. None if the
    section is absent."""
    lines = body.splitlines()
    start = None
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line)
        if m and m.group(1) == "#" and m.group(2).strip().lower() == heading_text.lower():
            start = i + 1
            break
    if start is None:
        return None
    out = []
    for line in lines[start:]:
        m = HEADING_RE.match(line)
        if m and m.group(1) == "#":  # next H1 ends the section
            break
        out.append(line)
    return out


def strip_protocol_content(section_lines: List[str]) -> List[str]:
    """Keep sub-headings (##+), checklist items, and tables — these carry the
    procedure. Drop prose, directive options, and everything inside any :::{...}
    admonition (hints, figures, notes). Blank lines are preserved then
    normalized so kept tables stay attached to their steps."""
    out: List[str] = []
    admonition_stack: List[int] = []  # colon-run lengths of open admonitions

    for line in section_lines:
        stripped = line.rstrip("\n")

        # Track directive nesting (indent-tolerant) and drop their contents —
        # EXCEPT {table} directives, which we treat as transparent so their rows
        # are kept (tables are part of the procedure). {figure} and all other
        # admonitions (note/hint/danger/...) are stripped.
        fence = FENCE_RE.match(stripped)
        if fence:
            run = len(fence.group(1))
            m = ADMONITION_OPEN_RE.match(stripped)
            if m:
                directive = m.group(2).split()[0].lower()
                # A {table} at top level stays transparent (don't strip its rows);
                # one nested inside an already-stripped block is still dropped.
                if not (directive == "table" and not admonition_stack):
                    admonition_stack.append(run)
            elif admonition_stack and run == admonition_stack[-1]:
                admonition_stack.pop()
            # Fence lines themselves are never emitted.
            continue
        if admonition_stack:
            continue

        m = HEADING_RE.match(stripped)
        if m and m.group(1) != "#":  # keep step sub-headings, never another H1
            out.append(stripped)
            continue
        if CHECKLIST_RE.match(stripped) or TABLE_ROW_RE.match(stripped):
            out.append(stripped)
            continue
        if stripped.strip() == "":  # keep blanks for now; normalized below
            out.append("")
            continue
        # Drop everything else: prose, directive option lines.

    return _normalize_blanks(out)


def _normalize_blanks(lines: List[str]) -> List[str]:
    """Trim leading/trailing blanks, collapse blank runs to one, and guarantee a
    blank line before each heading and after each table block so Markdown parses
    the kept tables and lists correctly."""
    out: List[str] = []
    for line in lines:
        if line == "":
            if not out or out[-1] == "":
                continue
            out.append("")
            continue
        # Separate a table from whatever non-table content follows it.
        prev_is_table = bool(out) and bool(TABLE_ROW_RE.match(out[-1]))
        this_is_table = bool(TABLE_ROW_RE.match(line))
        needs_break = HEADING_RE.match(line) or (prev_is_table and not this_is_table)
        if needs_break and out and out[-1] != "":
            out.append("")
        out.append(line)
    while out and out[-1] == "":
        out.pop()
    return out


def extract_hazard_note(body: str) -> Optional[List[str]]:
    """Return the body lines of the admonition titled 'Hazardous Materials',
    or None if absent. Directive option lines (:class:, :icon:) are dropped."""
    lines = body.splitlines()
    for i, line in enumerate(lines):
        m = ADMONITION_OPEN_RE.match(line)
        if m and m.group(3).strip().lower() == "hazardous materials":
            run = len(m.group(1))
            out = []
            for line2 in lines[i + 1:]:
                fence = re.match(r"^(:{3,})\s*$", line2)
                if fence and len(fence.group(1)) == run:
                    break
                if DIRECTIVE_OPTION_RE.match(line2):
                    continue
                out.append(line2.rstrip("\n"))
            # Trim surrounding blanks.
            while out and out[0] == "":
                out.pop(0)
            while out and out[-1] == "":
                out.pop()
            return out
    return None


def strip_cross_references(text: str) -> str:
    """Neutralize MyST cross-reference roles ({ref}`x`, {numref}`x`, {eq}`x`)
    to a plain readable noun. Protocol steps often reference labels defined in
    stripped page sections (e.g. {ref}`comp-cytosol` -> the Composition table);
    standalone, those labels don't exist and typst errors. A lab-ready sheet
    doesn't need clickable cross-refs, so render the target's type as a word."""
    def repl(m):
        label = m.group(2).lower()
        if label.startswith("fig"):
            return "figure"
        if label.startswith(("tbl", "tab", "comp", "bom")):
            return "table"
        return "section"
    return re.sub(r"\{(?:ref|numref|eq)\}`([^`<]*?<)?([^`>]+)>?`", repl, text)


def build_protocol_markdown(title: str, hazard: Optional[List[str]],
                            checklist: List[str], slug: str) -> str:
    """Assemble the intermediate markdown that MyST renders to the protocol PDF."""
    fm = (
        "---\n"
        f"title: {title}\n"
        "exports:\n"
        "  - format: typst\n"
        f"    template: {TYPST_TEMPLATE_DIR.resolve()}\n"
        f"    output: {slug}-protocol.pdf\n"
        "---\n\n"
    )
    parts = [fm]
    if hazard:
        parts.append(":::{danger} Hazardous Materials\n")
        parts.append(strip_cross_references("\n".join(hazard)) + "\n")
        parts.append(":::\n\n")
    parts.append(strip_cross_references("\n".join(checklist)) + "\n")
    return "".join(parts)


def build_bom_markdown(title: str, bom_rows: List[str], slug: str) -> str:
    """Assemble the intermediate markdown that MyST renders to the BOM PDF."""
    fm = (
        "---\n"
        f"title: {title} — Bill of Materials\n"
        "exports:\n"
        "  - format: typst\n"
        f"    template: {TYPST_TEMPLATE_DIR.resolve()}\n"
        f"    output: {slug}-bom.pdf\n"
        "---\n\n"
    )
    return fm + "\n".join(bom_rows) + "\n"


def resolve_bom_source(page: Path, body: str, slug: str) -> Tuple[Optional[List[str]], str]:
    """Resolve a process page's BOM from either of two accepted inputs (#108):

      - an inline table labeled ``bom-<slug>`` on the page, or
      - an uploaded ``resources/<slug>-bom.csv`` beside the page.

    Returns ``(table_rows, source)`` where source is ``"inline"``, ``"csv"``, or
    ``"none"``. If both inputs exist the inline table wins for rendering (it's
    what readers see on the page); enforcing that the two agree is the label
    checker's job, not the generator's. A malformed/empty CSV warns on stderr
    and yields no BOM rather than crashing the build."""
    inline = extract_bom_table(body, slug)
    csv_path = page.parent / "resources" / f"{slug}-bom.csv"
    if inline is not None:
        return inline, "inline"
    if csv_path.is_file():
        try:
            rows = csv_to_table_rows(csv_path.read_text(encoding="utf-8"))
        except (OSError, UnicodeDecodeError, csv.Error) as exc:
            print(f"  ⚠️  {csv_path}: could not read BOM CSV ({exc}); skipping BOM.",
                  file=sys.stderr)
            return None, "none"
        if not rows:
            print(f"  ⚠️  {csv_path}: BOM CSV is empty; skipping BOM.",
                  file=sys.stderr)
            return None, "none"
        return rows, "csv"
    return None, "none"


def find_process_pages(args: List[str]) -> List[Path]:
    targets = [Path(a) for a in args] if args else [PROCESSES_ROOT]
    pages: List[Path] = []
    for target in targets:
        if target.is_file() and target.suffix == ".md":
            pages.append(target)
            continue
        for pattern in ("**/main.md", "**/*-main.md"):
            pages.extend(target.glob(pattern))
    # Dedupe, keep only those with a Protocol section.
    seen = set()
    result = []
    for p in sorted(pages):
        if p in seen:
            continue
        seen.add(p)
        if has_protocol_section(split_frontmatter(p.read_text(encoding="utf-8"))[1]):
            result.append(p)
    return result


def render_pdf(intermediate_md: Path, attempts: int = 3) -> Tuple[bool, str]:
    """Render a PDF from an intermediate markdown file via MyST + typst.

    The first `myst build --pdf` in a cold checkout occasionally produces no PDF
    (intermittent, observed in CI — see issue #132), so retry up to `attempts`
    times. On final failure, surface myst/typst's exit code and stderr tail —
    the old code only checked `pdf.exists()` and discarded the captured output,
    leaving failures undiagnosable in CI."""
    pdf = intermediate_md.with_suffix(".pdf")
    last = "unknown error"
    for attempt in range(1, attempts + 1):
        if pdf.exists():
            pdf.unlink()
        try:
            proc = subprocess.run(
                ["myst", "build", intermediate_md.name, "--pdf"],
                cwd=intermediate_md.parent,
                capture_output=True, text=True, timeout=180,
            )
        except subprocess.TimeoutExpired:
            last = f"timeout after 180s (attempt {attempt}/{attempts})"
            continue
        if pdf.exists():
            return True, f"rendered {pdf.name}"
        tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-15:]
        last = "\n".join(
            [f"exit {proc.returncode}, no PDF (attempt {attempt}/{attempts})"]
            + [f"      {line}" for line in tail]
        )
    return False, f"render produced no PDF for {intermediate_md.name}: {last}"


def main() -> int:
    argv = sys.argv[1:]
    extract_only = "--extract-only" in argv
    args = [a for a in argv if not a.startswith("--")]

    if not PROCESSES_ROOT.exists():
        print(f"ERROR: '{PROCESSES_ROOT}' not found — run from the repo root.")
        return 1

    render_available = bool(shutil.which("myst") and shutil.which("typst"))
    if not render_available and not extract_only:
        print("ℹ️  myst/typst not on PATH — extracting only, skipping PDF renders.")

    pages = find_process_pages(args)
    if not pages:
        print("No process pages with a '# Protocol' section found.")
        return 0

    render_failures = 0
    for page in pages:
        slug = slug_from_page(page)
        text = page.read_text(encoding="utf-8")
        fm, body = split_frontmatter(text)
        title = page_title(fm, slug)

        section = extract_section(body, "Protocol")
        checklist = strip_protocol_content(section or [])

        # Skip stubs / under-construction pages: a Protocol section with no
        # checklist items would only yield an empty PDF.
        if not any(CHECKLIST_RE.match(line) for line in checklist):
            print(f"– {page}  (skipped: no protocol steps)")
            continue

        hazard = extract_hazard_note(body)
        bom_rows, bom_source = resolve_bom_source(page, body, slug)

        gen_dir = page.parent / "generated"
        gen_dir.mkdir(exist_ok=True)

        to_render = []  # intermediate .md files to render to PDF

        protocol_md = gen_dir / f"{slug}-protocol.md"
        protocol_md.write_text(
            build_protocol_markdown(title, hazard, checklist, slug),
            encoding="utf-8",
        )
        to_render.append(protocol_md)

        bom_note = ""
        if bom_rows:
            (gen_dir / f"{slug}-materials.csv").write_text(
                table_to_csv(bom_rows), encoding="utf-8"
            )
            bom_md = gen_dir / f"{slug}-bom.md"
            bom_md.write_text(
                build_bom_markdown(title, bom_rows, slug), encoding="utf-8"
            )
            to_render.append(bom_md)
            bom_note = f" + BOM/CSV (from {bom_source})"

        haz = " + hazard note" if hazard else ""
        print(f"✓ {page}  →  {slug}-protocol.md ({len(checklist)} lines){haz}{bom_note}")

        if render_available and not extract_only:
            for md in to_render:
                ok, msg = render_pdf(md)
                print(f"    {'✓' if ok else '✗'} {msg}")
                if not ok:
                    render_failures += 1

    print(f"\nProcessed {len(pages)} process page(s).")
    if render_failures:
        print(f"❌ {render_failures} PDF render(s) failed.")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
