#!/usr/bin/env python3
"""
check-file-placement.py — flag content files committed outside allowed directories.

Content file extensions: .md, .csv, .pdf, .png, .jpg, .jpeg, .gif, .svg, .webp, .ico

Allowed top-level directories: docs/, guides/, about/, start/, templates/, styles/, assets/
Allowed root-level files: intro.md, README.md, CLAUDE.md (and other non-content root files
like myst.yml, site.yml, environment.yml, requirements.txt, setup.sh, .vale.ini, etc. are
not content files and are not checked).

Any content-extension file whose path is not inside an allowed root (or is not an
explicitly allowed root-level file) is flagged as a placement violation.

Usage:
    python3 scripts/check-file-placement.py
"""

import subprocess
import sys
from pathlib import Path

CONTENT_EXTENSIONS = {".md", ".csv", ".pdf", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".ico"}

ALLOWED_ROOTS = {
    "docs", "guides", "about", "start", "templates", "styles", "assets",
}

ALLOWED_ROOT_FILES = {
    "intro.md", "readme.md", "claude.md",
    "contributors.md", "license.md", "fixme.md",
    "favicon.ico",
}

IGNORED_DIRS = {"_build", ".github", ".claude", ".obsidian", "scripts", "generated"}


def get_tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files"],
        capture_output=True, text=True, check=True,
    )
    return [Path(p) for p in result.stdout.splitlines() if p]


def is_violation(path: Path) -> bool:
    if path.suffix.lower() not in CONTENT_EXTENSIONS:
        return False
    parts = path.parts
    if not parts:
        return False
    top = parts[0]
    # Single-level root file
    if len(parts) == 1:
        return path.name.lower() not in ALLOWED_ROOT_FILES
    # Inside an ignored or allowed directory
    if top in IGNORED_DIRS or top.startswith("."):
        return False
    return top not in ALLOWED_ROOTS


def main() -> int:
    try:
        files = get_tracked_files()
    except subprocess.CalledProcessError as e:
        print(f"error: git ls-files failed: {e}", file=sys.stderr)
        return 1

    violations = [f for f in files if is_violation(f)]
    if violations:
        for f in sorted(violations):
            print(f"{f}  content file outside allowed directory")
        print(
            f"\n{len(violations)} misplaced file(s). Move to docs/, guides/, about/, "
            "start/, templates/, styles/, or assets/."
        )
        return 1
    print(f"✅ All {len([f for f in files if f.suffix.lower() in CONTENT_EXTENSIONS])} "
          f"content file(s) are correctly placed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
