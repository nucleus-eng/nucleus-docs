#!/usr/bin/env python3
"""
check-links.py — lychee wrapper that filters known vendor HTTP/2 false positives.

Some vendor sites (e.g. sigmaaldrich.com) terminate HTTP/2 connections at the
protocol level before returning any HTTP status code. This produces a
"Network error: HTTP/2 protocol error" in lychee's output that cannot be
distinguished from a real error via lychee config alone.

This script runs lychee with JSON output, filters out errors that match the
known HTTP/2 false-positive pattern for excluded domains, and exits non-zero
only if genuine errors remain.

Usage:
    python3 scripts/check-links.py [lychee args...]
    python3 scripts/check-links.py docs/
    python3 scripts/check-links.py --no-progress docs/
"""

import json
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path

HTTP2_ERROR_SUBSTRING = "HTTP/2 protocol error"

_CONFIG_PATH = Path(__file__).with_name("link-false-positives.toml")

def _load_false_positive_domains() -> list[str]:
    try:
        with _CONFIG_PATH.open("rb") as f:
            data = tomllib.load(f)
    except FileNotFoundError:
        return []
    return data.get("http2_false_positives", {}).get("domains", [])


HTTP2_FALSE_POSITIVE_DOMAINS = _load_false_positive_domains()


def is_http2_false_positive(url: str, error_text: str) -> bool:
    return (
        any(domain in url for domain in HTTP2_FALSE_POSITIVE_DOMAINS)
        and HTTP2_ERROR_SUBSTRING in error_text
    )


def main():
    if not shutil.which("lychee"):
        print("ERROR: lychee is not installed. Run ./setup.sh or: brew install lychee")
        sys.exit(1)

    args = sys.argv[1:] or ["docs/"]

    result = subprocess.run(
        ["lychee", "--config", ".lychee.toml", "--format", "json", "--no-progress", *args],
        capture_output=True,
        text=True,
    )

    # lychee emits a trailing "Hint:" line after the JSON — strip it
    json_text = result.stdout.split("\nHint:")[0].strip()

    try:
        report = json.loads(json_text)
    except json.JSONDecodeError:
        print("ERROR: could not parse lychee JSON output:")
        print(result.stdout)
        sys.exit(1)

    # Filter error_map: remove known HTTP/2 false positives
    genuine_errors = {}
    filtered_count = 0

    for filepath, entries in report.get("error_map", {}).items():
        real = []
        for entry in entries:
            url = entry.get("url", "")
            text = entry.get("status", {}).get("text", "")
            if is_http2_false_positive(url, text):
                filtered_count += 1
            else:
                real.append(entry)
        if real:
            genuine_errors[filepath] = real

    # Print summary
    total_errors = sum(len(v) for v in genuine_errors.values())
    excludes = report.get("excludes", 0)
    successful = report.get("successful", 0)
    total = report.get("total", 0)

    if filtered_count:
        print(f"ℹ️  Filtered {filtered_count} HTTP/2 false positive(s) from {', '.join(HTTP2_FALSE_POSITIVE_DOMAINS)}")

    if genuine_errors:
        print(f"\n❌ {total_errors} genuine error(s) found:\n")
        for filepath, entries in genuine_errors.items():
            print(f"  {filepath}")
            for entry in entries:
                url = entry.get("url", "")
                status = entry.get("status", {})
                details = status.get("details", "") or status.get("text", "")
                line = entry.get("span", {}).get("line", "?")
                print(f"    [{line}] {url} — {details}")
        sys.exit(1)
    else:
        print(f"✅ {successful}/{total} links OK ({excludes} excluded)")
        sys.exit(0)


if __name__ == "__main__":
    main()