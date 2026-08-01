#!/usr/bin/env python3
"""
check-myst-build.py — myst build wrapper that fails only on genuine ⛔️ errors.

`myst build --html` emits ⛔️-prefixed errors for broken links, missing
images, and malformed directives, but exits 0 regardless. `--strict` makes it
exit non-zero on any such error — but mystmd's own `error_rules` config
(myst.yml) cannot scope some rules (e.g. image-exists) to a single file,
because those warnings carry no per-file `key`. A myst.yml suppression for
such a rule would be repo-wide, silently blinding the build check to a
genuinely missing file anywhere else in the docs.

This script runs `myst build --html --strict`, and for any ⛔️ line matches
it against a small allowlist of known false positives (exact file + message
substring). Everything else that doesn't match fails the build. See issue
#176.

Usage:
    python3 scripts/check-myst-build.py

Must run after scripts/build-protocols.py and
scripts/build-materials-reference.py — the Downloads cards and the
guides/materials-reference.md include point at gitignored generated/
artifacts that don't exist until those run, and would otherwise report as
real missing-file errors.
"""

import re
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

_CONFIG_PATH = Path(__file__).with_name("myst-build-false-positives.toml")
_ANSI_RE = re.compile(r"\x1b\[[0-9;]*m")
# addWarningForFile's error format: "⛔️ <file>[:<line>[:<col>]] <message>"
_ERROR_RE = re.compile(r"^⛔️\s+(\S+)\s+(.*)$")


def _load_false_positives() -> list[dict]:
    try:
        with _CONFIG_PATH.open("rb") as f:
            data = tomllib.load(f)
    except FileNotFoundError:
        return []
    return data.get("image_exists", [])


def is_false_positive(file: str, message: str, false_positives: list[dict]) -> bool:
    return any(
        fp["file"] == file and fp["substring"] in message for fp in false_positives
    )


def main():
    if not shutil.which("myst"):
        print("ERROR: myst is not installed. Run ./setup.sh or: npm install -g mystmd")
        sys.exit(1)

    result = subprocess.run(
        ["myst", "build", "--html", "--strict"],
        capture_output=True,
        text=True,
    )

    output = _ANSI_RE.sub("", result.stdout + result.stderr)
    false_positives = _load_false_positives()

    genuine = []
    filtered = 0
    for raw_line in output.splitlines():
        line = raw_line.strip()
        match = _ERROR_RE.match(line)
        if not match:
            continue
        file, message = match.group(1), match.group(2)
        if is_false_positive(file, message, false_positives):
            filtered += 1
        else:
            genuine.append(line)

    if filtered:
        print(f"ℹ️  Filtered {filtered} known false positive(s) — see scripts/myst-build-false-positives.toml")

    if genuine:
        print(f"\n❌ {len(genuine)} genuine myst build error(s):\n")
        for line in genuine:
            print(f"  {line}")
        sys.exit(1)

    print("✅ myst build: no unfiltered ⛔️ errors")
    sys.exit(0)


if __name__ == "__main__":
    main()
