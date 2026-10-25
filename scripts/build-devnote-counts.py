#!/usr/bin/env python3
"""
build-devnote-counts.py — count the DevNotes that support each Module, and
write that count into a "DevNotes" column in docs/modules/modules-main.md,
replacing the old star-based Validation column.

The count for a Module is the union of two sources:

1. scripts/devnote-associations.yml — a human-reviewed mapping, built with
   the "Module x DevNote Map" tool, of DevNote -> Module/Process/Implementation.
   This is authoritative wherever it has an entry.
2. A DOI citation on the Module's spec.md page (a https://doi.org/10.63765/...
   link) for any DevNote NOT YET represented in that mapping — the same join
   key scripts/build-graph.py uses for its DevNote ghost nodes. This is a
   fallback for a DevNote published after the last manual review pass.

Usage:
    python3 scripts/build-devnote-counts.py
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: pyyaml required — pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent.resolve()
DOCS_ROOT = REPO_ROOT / "docs"
MODULES_INDEX = DOCS_ROOT / "modules" / "modules-main.md"
ASSOCIATIONS_FILE = Path(__file__).parent / "devnote-associations.yml"

CURVENOTE_API = "https://scms.curvenote.com/v1/sites/bnext-devnotes/works"
CURVENOTE_COLLECTIONS = {"nucleus-core"}
FETCH_LIMIT = 200

DEVNOTE_DOI_RE = re.compile(r"https://doi\.org/(10\.63765/[A-Za-z0-9]+)")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)]+)\)")
NEW_COLUMN = "DevNotes"
OLD_COLUMN = "Validation"


def load_associations() -> dict:
    """Every DevNote entry (keyed by its Curvenote slug/id), excluding the
    file's own `exclude:` key — see build-devnote-cards.py, which is what
    reads that one."""
    if not ASSOCIATIONS_FILE.exists():
        return {}
    data = yaml.safe_load(ASSOCIATIONS_FILE.read_text(encoding="utf-8")) or {}
    return {k: v for k, v in data.items() if k != "exclude"}


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


def module_tags_from_associations(associations: dict) -> dict[str, set[str]]:
    """Map each module slug (docs/modules/<slug>) to the set of DevNote keys
    (the yaml's own keys — stable Curvenote slugs/ids) manually tagged to it."""
    by_module: dict[str, set[str]] = {}
    for devnote_key, entry in associations.items():
        for module_slug in (entry or {}).get("modules") or []:
            by_module.setdefault(module_slug, set()).add(devnote_key)
    return by_module


def known_dois(associations: dict) -> set[str]:
    """Every DOI already represented by some entry in the manual mapping,
    whatever module (or none) it's tagged to — used to avoid double-counting
    a DOI-cited DevNote the manual pass has already reviewed."""
    return {entry["doi"] for entry in associations.values() if entry and entry.get("doi")}


def count_devnotes_per_module(
    nucleus_core_dois: set[str], associations: dict
) -> dict[Path, tuple[int, set[str], set[str]]]:
    """Map each module's spec.md path to (count, manual DevNote keys, fallback DOIs)."""
    by_module = module_tags_from_associations(associations)
    already_known = known_dois(associations)
    counts: dict[Path, tuple[int, set[str], set[str]]] = {}
    modules_dir = DOCS_ROOT / "modules"
    for spec_md in sorted(modules_dir.glob("*/spec.md")):
        module_slug = spec_md.parent.name
        manual = by_module.get(module_slug, set())
        # A cited DOI not yet reviewed in the mapping is a fallback signal;
        # one already reviewed there is counted through `manual` instead,
        # whether or not that review kept it tagged to this module.
        fallback = (cited_dois(spec_md) & nucleus_core_dois) - already_known
        counts[spec_md.resolve()] = (len(manual) + len(fallback), manual, fallback)
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


def update_table_block(lines: list[str], counts: dict[Path, tuple[int, set[str], set[str]]]) -> list[str]:
    header_idx = None
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and (OLD_COLUMN in line or NEW_COLUMN in line):
            header_idx = i
            break
    if header_idx is None:
        return lines

    header_cells = split_row(lines[header_idx])
    validation_idx = header_cells.index(OLD_COLUMN) if OLD_COLUMN in header_cells else None
    devnotes_idx = header_cells.index(NEW_COLUMN) if NEW_COLUMN in header_cells else None

    if devnotes_idx is None:
        # First run against this table: repurpose the Validation column's
        # own slot, so DevNotes reads where the star rating used to.
        header_cells[validation_idx] = NEW_COLUMN
        devnotes_idx = validation_idx
        drop_idx = None
    elif validation_idx is not None:
        # A prior run already added a separate DevNotes column alongside
        # Validation; drop Validation now that DevNotes replaces it.
        drop_idx = validation_idx
    else:
        drop_idx = None

    spec_col = next((i for i, c in enumerate(header_cells) if c == "Specification"), None)
    if spec_col is None:
        print("warning: no Specification column found — skipping this table", file=sys.stderr)
        return lines

    sep_idx = header_idx + 1
    rows = [header_cells, split_row(lines[sep_idx])]

    end_idx = sep_idx + 1
    while end_idx < len(lines) and lines[end_idx].strip().startswith("|"):
        cells = split_row(lines[end_idx])
        while len(cells) <= max(spec_col, devnotes_idx, drop_idx or 0):
            cells.append("")
        spec_link = LINK_RE.search(lines[end_idx].split("|")[spec_col + 1])
        count = 0
        if spec_link:
            target = spec_path_from_link(spec_link.group(2))
            if target in counts:
                count, _manual, _fallback = counts[target]
        cells[devnotes_idx] = str(count)
        rows.append(cells)
        end_idx += 1

    if drop_idx is not None:
        for row in rows:
            del row[drop_idx]

    rendered = render_table(rows)
    return lines[:header_idx] + rendered + lines[end_idx:]


def update_modules_index(counts: dict[Path, tuple[int, set[str], set[str]]]) -> None:
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
    associations = load_associations()
    nucleus_core_dois = fetch_nucleus_core_dois()
    counts = count_devnotes_per_module(nucleus_core_dois, associations)

    print(f"{len(associations)} entries in {ASSOCIATIONS_FILE.name}, "
          f"{len(nucleus_core_dois)} published nucleus-core DevNote DOIs found\n")
    for spec_md, (count, manual, fallback) in sorted(counts.items()):
        module = spec_md.parent.name
        detail = []
        if manual:
            detail.append(f"manual: {sorted(manual)}")
        if fallback:
            detail.append(f"fallback DOI: {sorted(fallback)}")
        print(f"{module:28s} {count} DevNote(s)" + ("  " + "; ".join(detail) if detail else ""))

    update_modules_index(counts)
    print(f"\nwrote DevNotes column to {MODULES_INDEX.relative_to(REPO_ROOT)}, replacing Validation")


if __name__ == "__main__":
    main()
