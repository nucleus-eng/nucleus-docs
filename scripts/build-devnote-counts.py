#!/usr/bin/env python3
"""
build-devnote-counts.py — count the DevNotes that support each Module, and
write that count into a "DevNotes" column in docs/modules/modules-main.md.

A DevNote "supports" a Module when the Module's spec.md cites that DevNote's
DOI inline (a https://doi.org/10.63765/... link) and the DevNote is published
to the bnext-devnotes Curvenote site under the nucleus-core collection — the
same scope and join key scripts/build-graph.py already uses for its DevNote
ghost nodes.

This undercounts: most published DevNotes have no DOI yet (Curvenote mints
one lazily), so a Module can be supported by a DevNote this script cannot
see. Until there is a maintained Module -> DevNote mapping, DOI citation is
the only automatic signal available.

Usage:
    python3 scripts/build-devnote-counts.py
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()
DOCS_ROOT = REPO_ROOT / "docs"
MODULES_INDEX = DOCS_ROOT / "modules" / "modules-main.md"

CURVENOTE_API = "https://scms.curvenote.com/v1/sites/bnext-devnotes/works"
CURVENOTE_COLLECTIONS = {"nucleus-core"}
FETCH_LIMIT = 200

DEVNOTE_DOI_RE = re.compile(r"https://doi\.org/(10\.63765/[A-Za-z0-9]+)")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
NEW_COLUMN = "DevNotes"


def fetch_nucleus_core_dois() -> set[str]:
    """Bare DOIs (10.63765/...) of DevNotes published under nucleus-core."""
    try:
        with urllib.request.urlopen(f"{CURVENOTE_API}?limit={FETCH_LIMIT}", timeout=20) as resp:
            payload = json.loads(resp.read().decode("utf-8"))
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        print(f"error: could not query the Curvenote API ({exc})", file=sys.stderr)
        sys.exit(1)

    items = payload.get("items", [])
    if len(items) == FETCH_LIMIT:
        print(f"warning: Curvenote API returned exactly {FETCH_LIMIT} items — "
              "results may be truncated; this script does not paginate", file=sys.stderr)

    dois = set()
    for work in items:
        if work.get("collection", {}).get("slug") not in CURVENOTE_COLLECTIONS:
            continue
        doi = work.get("doi")
        if doi:
            dois.add(doi)
    return dois


def cited_dois(spec_md: Path) -> set[str]:
    try:
        text = spec_md.read_text(encoding="utf-8")
    except OSError:
        return set()
    return set(DEVNOTE_DOI_RE.findall(text))


def count_devnotes_per_module(nucleus_core_dois: set[str]) -> dict[Path, tuple[int, set[str]]]:
    """Map each module's spec.md path to (count, matched DOIs)."""
    counts: dict[Path, tuple[int, set[str]]] = {}
    modules_dir = DOCS_ROOT / "modules"
    for spec_md in sorted(modules_dir.glob("*/spec.md")):
        matched = cited_dois(spec_md) & nucleus_core_dois
        counts[spec_md.resolve()] = (len(matched), matched)
    return counts


# --------------------------------------------------------------------------- #
# modules-main.md table rewriting
# --------------------------------------------------------------------------- #

def split_row(line: str) -> list[str]:
    """Split a markdown table row into its cell contents, stripped."""
    inner = line.strip()
    if inner.startswith("|"):
        inner = inner[1:]
    if inner.endswith("|"):
        inner = inner[:-1]
    return [cell.strip() for cell in inner.split("|")]


def is_separator_row(cells: list[str]) -> bool:
    return all(re.fullmatch(r":?-+:?", cell) for cell in cells)


def render_table(rows: list[list[str]]) -> list[str]:
    """Render cell rows (header, separator placeholder ignored, data...) as a
    padded, pipe-aligned markdown table. rows[1] is rebuilt as the dash row."""
    ncols = len(rows[0])
    widths = [3] * ncols
    for i, row in enumerate(rows):
        if i == 1:
            continue
        for c, cell in enumerate(row):
            widths[c] = max(widths[c], len(cell))

    out = []
    for i, row in enumerate(rows):
        if i == 1:
            cells = ["-" * widths[c] for c in range(ncols)]
        else:
            cells = [row[c].ljust(widths[c]) for c in range(ncols)]
        out.append("| " + " | ".join(cells) + " |")
    return out


def spec_path_from_link(href: str) -> Path | None:
    href = href.split("#")[0].strip()
    if not href.endswith(".md"):
        return None
    if re.match(r"^https?://|^mailto:", href):
        return None
    base = MODULES_INDEX.parent if not href.startswith("/") else REPO_ROOT
    return (base / href.lstrip("/")).resolve()


def update_table_block(lines: list[str], counts: dict[Path, tuple[int, set[str]]]) -> list[str]:
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "Validation" in line:
            header_idx = i
            break
    if header_idx is None:
        return lines

    header_cells = split_row(lines[header_idx])
    if NEW_COLUMN in header_cells:
        print("DevNotes column already present — recomputing values only", file=sys.stderr)
        devnotes_idx = header_cells.index(NEW_COLUMN)
    else:
        header_cells.append(NEW_COLUMN)
        devnotes_idx = len(header_cells) - 1

    spec_col = next((i for i, c in enumerate(header_cells) if c == "Specification"), None)
    if spec_col is None:
        print("warning: no Specification column found — skipping this table", file=sys.stderr)
        return lines

    sep_idx = header_idx + 1
    rows = [header_cells, split_row(lines[sep_idx])]

    end_idx = sep_idx + 1
    while end_idx < len(lines) and lines[end_idx].strip().startswith("|"):
        cells = split_row(lines[end_idx])
        while len(cells) < devnotes_idx:
            cells.append("")
        spec_link = LINK_RE.search(lines[end_idx].split("|")[spec_col + 1]) if spec_col < len(cells) else None
        count = 0
        if spec_link:
            target = spec_path_from_link(spec_link.group(2))
            if target in counts:
                count, _matched = counts[target]
        if len(cells) <= devnotes_idx:
            cells.append(str(count))
        else:
            cells[devnotes_idx] = str(count)
        rows.append(cells)
        end_idx += 1

    rendered = render_table(rows)
    return lines[:header_idx] + rendered + lines[end_idx:]


def update_modules_index(counts: dict[Path, tuple[int, set[str]]]) -> None:
    text = MODULES_INDEX.read_text(encoding="utf-8")
    lines = text.split("\n")

    out: list[str] = []
    i = 0
    while i < len(lines):
        out.append(lines[i])
        if lines[i].strip() == ":::{table}":
            # find the matching closing ':::' for this fence
            j = i + 1
            while j < len(lines) and lines[j].strip() != ":::":
                j += 1
            block = lines[i + 1:j]
            block = update_table_block(block, counts)
            out.extend(block)
            i = j
            continue
        i += 1

    MODULES_INDEX.write_text("\n".join(out), encoding="utf-8")


def main():
    nucleus_core_dois = fetch_nucleus_core_dois()
    counts = count_devnotes_per_module(nucleus_core_dois)

    print(f"{len(nucleus_core_dois)} published nucleus-core DevNote DOIs found\n")
    for spec_md, (count, matched) in sorted(counts.items()):
        module = spec_md.parent.name
        print(f"{module:28s} {count} DevNote(s)" + (f"  {sorted(matched)}" if matched else ""))

    update_modules_index(counts)
    print(f"\nwrote DevNotes column to {MODULES_INDEX.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
