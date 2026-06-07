#!/usr/bin/env python3
"""
check-dropdowns.py — flag markdown lists whose only content is a placeholder token.

A list item is a placeholder if it is one of: None, TODO, TBD, N/A, NA, —, –, -
(case-insensitive). A list is flagged if every non-blank, non-directive item is
a placeholder. This catches unfilled scaffold sections that should be deleted or
filled before merge (per CLAUDE.md empty-dropdown policy).

Scope: .md files under docs/, guides/, about/. Excludes templates/ (placeholders
are intentional there) and generated/ directories.

Usage:
    python3 scripts/check-dropdowns.py
    python3 scripts/check-dropdowns.py docs/
    python3 scripts/check-dropdowns.py docs/ guides/ about/
"""

import re
import subprocess
import sys
from pathlib import Path

PLACEHOLDER = re.compile(
    r"^[-*]\s*(none|todo|tbd|n/?a|—|–|-)\s*$", re.IGNORECASE
)
LIST_ITEM = re.compile(r"^[-*]\s+\S")
DEFAULT_ROOTS = ["docs", "guides", "about"]


def check_file(path: Path) -> list[tuple[int, str]]:
    """Return (line_number, message) for each placeholder-only list block."""
    violations = []
    lines = path.read_text(encoding="utf-8").splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        # Start of a list item that is a placeholder
        if PLACEHOLDER.match(line.strip()):
            block_start = i + 1
            # Collect the whole contiguous list block
            j = i
            block = []
            while j < len(lines) and (
                PLACEHOLDER.match(lines[j].strip())
                or (LIST_ITEM.match(lines[j]) and not PLACEHOLDER.match(lines[j].strip()))
                or lines[j].strip() == ""
            ):
                if lines[j].strip():
                    block.append(lines[j].strip())
                j += 1
            # Flag only if every non-empty item in the block is a placeholder
            if block and all(PLACEHOLDER.match(b) for b in block):
                violations.append(
                    (block_start, f"list contains only placeholder content: {block[0]!r}")
                )
            i = j
        else:
            i += 1
    return violations


def find_files(roots: list[str]) -> list[Path]:
    try:
        result = subprocess.run(
            ["git", "ls-files"] + roots,
            capture_output=True, text=True, check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"error: git ls-files failed: {e}", file=sys.stderr)
        sys.exit(1)
    files = []
    for p in result.stdout.splitlines():
        if not p.endswith(".md"):
            continue
        path = Path(p)
        if "generated" in path.parts or "templates" in path.parts:
            continue
        files.append(path)
    return sorted(files)


def main() -> int:
    roots = [a for a in sys.argv[1:] if not a.startswith("-")] or DEFAULT_ROOTS
    files = find_files(roots)
    errors = 0
    for f in files:
        for lineno, msg in check_file(f):
            print(f"{f}:{lineno}  {msg}")
            errors += 1
    if errors:
        print(f"\n{errors} placeholder-only list(s) found. Delete the empty section or fill it in.")
        return 1
    print(f"✅ No placeholder-only lists found in {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
