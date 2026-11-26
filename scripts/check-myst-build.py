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

Exit codes:
    0  no unfiltered ⛔️ error
    1  at least one unfiltered ⛔️ error
    2  the build did not run: myst is missing, or it exited non-zero without
       reporting any ⛔️ error. An old myst (the curvenote 0.13.1 shim prints
       an "Upgrade Required" banner and exits 1) never builds anything, and
       a script that read only the ⛔️ lines reported a pass for it.

With --strict, mystmd 1.9.1 exits 1 on a ⛔️ error and 0 on a warning alone. A
non-zero exit whose ⛔️ lines are all known false positives is still a pass.

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


def parse_errors(output: str, false_positives: list[dict]) -> tuple[list[str], int]:
    """Split the ⛔️ lines of a myst run into (genuine errors, filtered count)."""
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
    return genuine, filtered


def verdict(returncode: int, genuine: list[str], filtered: int) -> int:
    """Map one myst run to this script's exit code (0 pass, 1 errors, 2 did not run).

    A non-zero `returncode` with no ⛔️ line at all, filtered or not, means myst
    stopped before it built anything. A non-zero `returncode` whose ⛔️ lines
    were all filtered is what `--strict` does for a known false positive.
    """
    if genuine:
        return 1
    if returncode != 0 and filtered == 0:
        return 2
    return 0


def main():
    if not shutil.which("myst"):
        print("ERROR: myst is not installed. Run ./setup.sh or: npm install -g mystmd")
        sys.exit(2)

    result = subprocess.run(
        ["myst", "build", "--html", "--strict"],
        capture_output=True,
        text=True,
    )

    output = _ANSI_RE.sub("", result.stdout + result.stderr)
    genuine, filtered = parse_errors(output, _load_false_positives())
    code = verdict(result.returncode, genuine, filtered)

    if filtered:
        print(f"ℹ️  Filtered {filtered} known false positive(s) — see scripts/myst-build-false-positives.toml")

    if code == 1:
        print(f"\n❌ {len(genuine)} genuine myst build error(s):\n")
        for line in genuine:
            print(f"  {line}")
    elif code == 2:
        print(f"\n❌ myst exited {result.returncode} and reported no ⛔️ error, so the build did not run.\n")
        print("Last lines of its output:\n")
        tail = [ln for ln in output.splitlines() if ln.strip()][-12:]
        for line in tail:
            print(f"  {line}")
        print("\nCheck `myst --version`. CI pins mystmd@1.9.1; a curvenote 0.13.1 shim cannot build this site.")
    else:
        print("✅ myst build: no unfiltered ⛔️ errors")
    sys.exit(code)


if __name__ == "__main__":
    main()
