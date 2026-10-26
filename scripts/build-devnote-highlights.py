#!/usr/bin/env python3
"""
build-devnote-highlights.py — write the "Documentation comes from DevNotes"
section on the homepage (intro.md), showing the 5 most recently published
DevNotes.

Queries the same Curvenote SCMS API as build-devnote-cards.py and
build-devnote-counts.py (see those for the request shape), sorts by
``date_published`` (falling back to ``date``), and renders the top 5 in
the same compact thumbnail-list style as that script's own
``render_cards()`` (the ``devnote-cards`` CSS class already used by every
page's "# Supported by" section) rather than a multi-column card grid,
since each DevNote here is one item with its own link, not a bundle.

Not wired into CI: this repo does not make outbound network calls during the
build (see build-devnote-cards.py's docstring), so this is a one-off local
script you run and commit the output of, re-run occasionally to refresh the
list.

Usage:
    python3 scripts/build-devnote-highlights.py
    python3 scripts/build-devnote-highlights.py --dry-run
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

CURVENOTE_API = "https://scms.curvenote.com/v1/sites/bnext-devnotes/works"
FETCH_LIMIT = 200
TIMEOUT = 20
COUNT = 5

REPO_ROOT = Path(__file__).parent.parent.resolve()
INTRO_MD = REPO_ROOT / "intro.md"

START_MARKER = "<!-- devnote-highlights:start -->"
END_MARKER = "<!-- devnote-highlights:end -->"


def get_json(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read())


def fetch_thumbnail(work: dict) -> str | None:
    """A work's optimized thumbnail URL from its CDN config, or None — same
    lookup as build-devnote-cards.py's fetch_all_notes()."""
    cdn, cdn_key = work.get("cdn"), work.get("cdn_key")
    if not cdn or not cdn_key:
        return None
    try:
        config = get_json(f"{cdn}{cdn_key}/config.json")
    except (urllib.error.URLError, urllib.error.HTTPError, ValueError, OSError):
        return None
    project = (config.get("projects") or [{}])[0]
    thumb_path = project.get("thumbnailOptimized") or project.get("thumbnail")
    return f"{cdn}{cdn_key}/public{quote(thumb_path, safe='/')}" if thumb_path else None


def fetch_recent(n: int = COUNT) -> list[dict]:
    try:
        payload = get_json(f"{CURVENOTE_API}?limit={FETCH_LIMIT}")
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        print(f"error: could not query the Curvenote API ({exc})", file=sys.stderr)
        sys.exit(1)

    items = payload.get("items", [])
    if len(items) == FETCH_LIMIT:
        print(f"warning: Curvenote API returned exactly {FETCH_LIMIT} items — "
              "results may be truncated; this script does not paginate", file=sys.stderr)

    def sort_key(work: dict) -> str:
        return work.get("date_published") or work.get("date") or ""

    items = [w for w in items if sort_key(w)]
    items.sort(key=sort_key, reverse=True)
    return items[:n]


def format_date(iso_date: str) -> str:
    try:
        return datetime.strptime(iso_date, "%Y-%m-%d").strftime("%B %-d, %Y")
    except ValueError:
        return iso_date


def render_cards(works: list[dict]) -> str:
    lines = ["::::{grid} 1 1 1 1", ":class: devnote-cards", ""]
    for work in works:
        title = work.get("title", "Untitled")
        authors = ", ".join(a.get("name") for a in (work.get("authors") or []) if a.get("name")) or "Unknown author"
        date = format_date(work.get("date_published") or work.get("date") or "")
        byline = f"{authors} · {date}" if date else authors
        url = (work.get("links") or {}).get("html", "")
        thumbnail = fetch_thumbnail(work)

        lines.append(f":::{{card}} {title}")
        lines.append(f":link: {url}")
        lines.append(f":footer: {byline}")
        lines.append("")
        if thumbnail:
            lines.append(f"![]({thumbnail})")
        lines.append(":::")
        lines.append("")
    lines.append("::::")
    return "\n".join(lines)


def update_intro(dry_run: bool) -> None:
    text = INTRO_MD.read_text(encoding="utf-8")
    start = text.find(START_MARKER)
    end = text.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        print(f"error: {START_MARKER!r}/{END_MARKER!r} markers not found in intro.md", file=sys.stderr)
        sys.exit(1)

    works = fetch_recent(COUNT)
    if not works:
        print("error: no published DevNotes with a date were found", file=sys.stderr)
        sys.exit(1)

    grid = render_cards(works)
    new_text = text[: start + len(START_MARKER)] + "\n\n" + grid + "\n\n" + text[end:]

    if dry_run:
        print(grid)
        return

    INTRO_MD.write_text(new_text, encoding="utf-8")
    print(f"wrote {len(works)} DevNote(s) to {INTRO_MD.relative_to(REPO_ROOT)}")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="print the generated grid without writing intro.md")
    args = parser.parse_args()
    update_intro(dry_run=args.dry_run)
    return 0


if __name__ == "__main__":
    sys.exit(main())
