#!/usr/bin/env python3
"""
check-dna-refs.py — verifies that a docs page's claims about a DNA construct
match the actual file in nucleus-eng/DNA, rather than just checking that the
link resolves.

check-links.py already confirms a `github.com/nucleus-eng/DNA/blob/...` URL
returns 200. That says nothing about whether the construct named next to the
link is *the same sequence* as the file it points at — a link can be perfectly
alive and still assert a false identity (issue #120's motivating failure mode:
"greedy linking", where a name-similarity match gets claimed as a sequence
match). This script checks the identity claim itself.

For every Designs-table row containing a DNA-repo link, it compares:

  * the construct name (backtick-quoted, e.g. `pOpen-lacI`) against the
    target file's GenBank LOCUS name and filename
  * the docs' stated length in bp against the target file's LOCUS length
  * the link text's filename against the target file's actual filename
  * the link's repo against the canonical nucleus-eng/DNA (not the legacy
    bnext-bio/nucleus)

Severity:

  BLOCKING  the claim is verifiably wrong — missing file/dir, wrong bp, or a
            link into the legacy repo. These are real errors, not judgment
            calls.
  WARN      the construct name doesn't obviously relate to the target's LOCUS
            name or filename. Often a benign alias (LOCUS names are frequently
            truncated internal labels, not the full construct name used in
            prose) — but exactly the shape of a greedy-link mistake, so it is
            surfaced for a human decision rather than silently passed or
            silently blocked.
  INFO      the claim could not be verified at all — the target is a
            SnapGene `.dna` file (no parseable LOCUS length), or the row has
            no bp cell to check.

This is a *local, author-time* check, not a CI gate: nucleus-docs CI has no
checkout of the DNA repo, and a committed manifest of construct names would
drift from the source repo the moment either side changed. It reads the DNA
repo directly, defaulting to ~/src/nucleus-eng/DNA (override with
NUCLEUS_DNA_REPO).

It verifies *length*, not *sequence*. Two constructs of identical length but
different content are indistinguishable to this check — same blind spot
check-links.py documents for its own tolerated-failure list.

Usage:
    python3 scripts/check-dna-refs.py                 # all of docs/
    python3 scripts/check-dna-refs.py docs/modules/    # one subtree
    python3 scripts/check-dna-refs.py <file.md>        # one file
    NUCLEUS_DNA_REPO=/path/to/DNA python3 scripts/check-dna-refs.py

Exit codes:
    0  no blocking findings (warnings/info may be listed)
    1  blocking findings found
    2  the check could not run (DNA repo not found)
"""

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path

EXIT_OK = 0
EXIT_FINDINGS = 1
EXIT_CANNOT_RUN = 2

BLOCKING = "BLOCKING"
WARN = "WARN"
INFO = "INFO"

CANONICAL_REPO = "nucleus-eng/DNA"
LEGACY_REPO = "bnext-bio/nucleus"

SEQ_EXTENSIONS = {".gb", ".gbk", ".dna"}

# Backbone prefixes stripped before comparing construct names — these describe
# the vector/promoter context, not the identity of the insert, and differ
# routinely between a docs construct name and a DNA-repo filename/LOCUS name.
PREFIX_STRIP = ("pOpen-", "pET28a-")

LINK_RE = re.compile(
    r"\[([^\]]*)\]\(https://github\.com/(nucleus-eng/DNA|bnext-bio/nucleus)"
    r"/(blob|tree)/([^/]+)/([^)\s]+)\)"
)
BACKTICK_RE = re.compile(r"`([^`]+)`")
BP_SUFFIX_RE = re.compile(r"^(\d[\d,]*)\s*bp$", re.IGNORECASE)
FILENAME_RE = re.compile(r"^([\w.\-]+\.(?:gb|gbk|dna|fasta|fa))$", re.IGNORECASE)
LOCUS_RE = re.compile(r"^LOCUS\s+(\S+)\s+(\d+)\s+bp", re.IGNORECASE)
SEP_ROW_RE = re.compile(r"^[\s|:-]+$")


@dataclass
class Finding:
    level: str
    file: str
    line: int
    message: str

    def __str__(self):
        return f"{self.file}:{self.line} — {self.message}"


@dataclass
class ConstructFile:
    rel_path: str
    locus_name: str | None
    length_bp: int | None


@dataclass
class Claim:
    file: str
    line: int
    repo: str
    kind: str  # "blob" or "tree"
    path: str
    link_text: str
    bp: int | None
    name: str | None


# --------------------------------------------------------------------------- #
# DNA repo indexing
# --------------------------------------------------------------------------- #


def find_dna_repo() -> Path | None:
    env = os.environ.get("NUCLEUS_DNA_REPO")
    candidate = Path(env) if env else Path.home() / "src" / "nucleus-eng" / "DNA"
    return candidate if candidate.is_dir() else None


def _parse_locus(path: Path) -> tuple[str | None, int | None]:
    if path.suffix.lower() == ".dna":
        return None, None
    try:
        with path.open("r", errors="ignore") as f:
            first_line = f.readline()
    except OSError:
        return None, None
    m = LOCUS_RE.match(first_line)
    if not m:
        return None, None
    return m.group(1), int(m.group(2))


def index_dna_repo(repo_root: Path) -> dict[str, ConstructFile]:
    index = {}
    for path in repo_root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in SEQ_EXTENSIONS:
            continue
        rel = path.relative_to(repo_root).as_posix()
        locus_name, length_bp = _parse_locus(path)
        index[rel] = ConstructFile(rel, locus_name, length_bp)
    return index


# --------------------------------------------------------------------------- #
# Markdown table parsing
# --------------------------------------------------------------------------- #


def _split_row(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]


def find_tables(text: str):
    """Yield (header_cells, [(line_no, cells), ...]) for each markdown table."""
    lines = text.splitlines()
    i, n = 0, len(lines)
    while i < n:
        if lines[i].lstrip().startswith("|"):
            block = []
            while i < n and lines[i].lstrip().startswith("|"):
                block.append((i + 1, lines[i]))
                i += 1
            if len(block) >= 2:
                header_cells = _split_row(block[0][1])
                data_block = block[2:] if SEP_ROW_RE.match(block[1][1].strip()) else block[1:]
                data_rows = [(ln, _split_row(l)) for ln, l in data_block]
                yield header_cells, data_rows
        else:
            i += 1


def _bp_column_index(header_cells: list[str]) -> int | None:
    for idx, h in enumerate(header_cells):
        if "bp" in h.lower():
            return idx
    return None


def _parse_bp_cell(cell: str) -> int | None:
    cell = cell.strip().strip("*")
    m = BP_SUFFIX_RE.match(cell)
    if m:
        return int(m.group(1).replace(",", ""))
    try:
        return int(cell.replace(",", ""))
    except ValueError:
        return None


def extract_claims(header_cells: list[str], rows, filename: str) -> list[Claim]:
    bp_col = _bp_column_index(header_cells)
    claims = []
    for line_no, cells in rows:
        name = None
        for c in cells:
            m = BACKTICK_RE.search(c)
            if m:
                name = m.group(1)
                break

        bp_value = None
        if bp_col is not None and bp_col < len(cells):
            bp_value = _parse_bp_cell(cells[bp_col])
        if bp_value is None:
            for c in cells:
                m = BP_SUFFIX_RE.match(c.strip().strip("*"))
                if m:
                    bp_value = int(m.group(1).replace(",", ""))
                    break

        for cell in cells:
            for link_text, repo, kind, ref, path in LINK_RE.findall(cell):
                claims.append(
                    Claim(
                        file=filename,
                        line=line_no,
                        repo=repo,
                        kind=kind,
                        path=path,
                        link_text=link_text,
                        bp=bp_value,
                        name=name,
                    )
                )
    return claims


# --------------------------------------------------------------------------- #
# Validation
# --------------------------------------------------------------------------- #


def _normalize(name: str) -> str:
    n = name.strip().strip("`").lower()
    for prefix in PREFIX_STRIP:
        if n.startswith(prefix.lower()):
            n = n[len(prefix) :]
    return n


def _names_related(claim_name: str, locus_name: str | None, filename: str) -> bool:
    """A claim name is related to a target identifier if it is the identifier
    itself, optionally with a prefix decoration (promoter/vector context, e.g.
    `pT7-lacI` for target `lacI`). A *suffix* difference — the claim naming an
    extra downstream element the target doesn't confirm (`pT7-lacO-plamGFP`
    for target `pT7-lacO`; `pOpen-PPK` for target `pOpen-PPK-CHis`) — is not
    considered related: that shape is exactly how a greedy link drops or
    invents a genetic element, so it is left for a human to confirm rather
    than passed automatically."""
    a = _normalize(claim_name)
    if not a:
        return True
    candidates = []
    if locus_name:
        candidates.append(_normalize(locus_name))
    candidates.append(_normalize(Path(filename).stem))
    for c in candidates:
        if not c or len(c) < 3:
            continue
        if a == c or a.endswith("-" + c):
            return True
    return False


def _filename_from_text(text: str) -> str | None:
    m = FILENAME_RE.match(text.strip().strip("`"))
    return m.group(1) if m else None


def validate_claim(claim: Claim, dna_index: dict, dna_repo_root: Path) -> list[Finding]:
    findings = []

    if claim.repo == LEGACY_REPO:
        findings.append(
            Finding(
                BLOCKING,
                claim.file,
                claim.line,
                f"link points at legacy {LEGACY_REPO}, not {CANONICAL_REPO}: {claim.link_text!r}",
            )
        )
        return findings

    if claim.kind == "tree":
        if not (dna_repo_root / claim.path).is_dir():
            findings.append(
                Finding(BLOCKING, claim.file, claim.line, f"directory not found in DNA repo: {claim.path}")
            )
        return findings

    entry = dna_index.get(claim.path)
    if entry is None:
        findings.append(Finding(BLOCKING, claim.file, claim.line, f"file not found in DNA repo: {claim.path}"))
        return findings

    actual_basename = Path(claim.path).name
    link_basename = _filename_from_text(claim.link_text)
    if link_basename and link_basename != actual_basename:
        findings.append(
            Finding(
                WARN,
                claim.file,
                claim.line,
                f"link text names `{link_basename}` but target file is `{actual_basename}`",
            )
        )

    if claim.bp is None:
        findings.append(Finding(INFO, claim.file, claim.line, f"no length (bp) claim to verify for {actual_basename}"))
    elif entry.length_bp is None:
        findings.append(
            Finding(INFO, claim.file, claim.line, f"cannot verify length — {actual_basename} has no parseable LOCUS length")
        )
    elif claim.bp != entry.length_bp:
        findings.append(
            Finding(
                BLOCKING,
                claim.file,
                claim.line,
                f"docs claims {claim.bp} bp but {actual_basename} LOCUS reports {entry.length_bp} bp",
            )
        )

    if claim.name and not _names_related(claim.name, entry.locus_name, actual_basename):
        findings.append(
            Finding(
                WARN,
                claim.file,
                claim.line,
                f"construct name `{claim.name}` does not obviously match LOCUS "
                f"`{entry.locus_name}` or filename `{actual_basename}` — confirm this is an "
                "intentional alias, not a name-similarity guess",
            )
        )

    return findings


# --------------------------------------------------------------------------- #
# Driver
# --------------------------------------------------------------------------- #


def collect_markdown_files(paths: list[str]) -> list[Path]:
    files = []
    for raw in paths:
        p = Path(raw)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
        elif p.is_file():
            files.append(p)
    return files


def check(paths: list[str], dna_repo: Path) -> list[Finding]:
    dna_index = index_dna_repo(dna_repo)
    findings: list[Finding] = []
    for md_file in collect_markdown_files(paths):
        text = md_file.read_text(errors="ignore")
        for header_cells, rows in find_tables(text):
            for claim in extract_claims(header_cells, rows, str(md_file)):
                findings.extend(validate_claim(claim, dna_index, dna_repo))
    return findings


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", default=["docs/"])
    args = parser.parse_args(argv)

    dna_repo = find_dna_repo()
    if dna_repo is None:
        print(
            "ERROR: could not find the nucleus-eng/DNA repo. Clone it to "
            "~/src/nucleus-eng/DNA, or set NUCLEUS_DNA_REPO to its path.",
            file=sys.stderr,
        )
        return EXIT_CANNOT_RUN

    findings = check(args.paths, dna_repo)
    blocking = [f for f in findings if f.level == BLOCKING]
    warn = [f for f in findings if f.level == WARN]
    info = [f for f in findings if f.level == INFO]

    for level_name, group in ((BLOCKING, blocking), (WARN, warn), (INFO, info)):
        if not group:
            continue
        print(f"\n{level_name} ({len(group)}):")
        for f in group:
            print(f"  {f}")

    if blocking:
        print(f"\n❌ {len(blocking)} blocking DNA-reference issue(s) found")
        return EXIT_FINDINGS

    print(f"\n✅ no blocking DNA-reference issues ({len(warn)} warning(s), {len(info)} info)")
    return EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
