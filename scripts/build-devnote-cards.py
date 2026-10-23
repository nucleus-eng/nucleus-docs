#!/usr/bin/env python3
"""
build-devnote-cards.py — generate a "Supported by" card block of DevNotes
that cite a given docs page.

A DevNote on devnotes.nucleus.engineering can link back to a module spec or
process page here; this script finds those links from the DevNotes side
(there is no record of the relationship on this side) and renders them as a
``grid``/``card`` block — thumbnail, title, authors — in the same style the
"Downloads" cards on process pages already use.

How it works: fetches every work from the DevNotes SCMS API, reads each
one's rendered page content from its CDN, and collects every outbound link
whose host is ``docs.nucleus.engineering``. A DevNote can carry more than one
link to the same page (e.g. a figure caption and a prose reference); each
DevNote is counted once per page regardless.

This is a proof of concept (see issue discussion): run locally and the
output hand-inserted into the target page, not yet wired into the
``generated/`` + CI pattern ``build-protocols.py`` and
``build-materials-reference.py`` use (where the output is gitignored and
rebuilt on every deploy). Doing that is the natural next step once this is
reviewed, but means adding this repo's first outbound network call to the
build — worth its own discussion.

Usage:
    python3 scripts/build-devnote-cards.py docs/modules/detector-tetr-atc/spec
    python3 scripts/build-devnote-cards.py --list-all   # every page with a hit
"""

import argparse
import json
import sys
import urllib.error
import urllib.request
from urllib.parse import urlparse

SCMS_BASE = "https://scms.curvenote.com/v1/sites/bnext-devnotes"
DOCS_HOST = "docs.nucleus.engineering"
TIMEOUT = 20


def get_json(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read())


def mdast_links(node, out: list[str]) -> list[str]:
    """Every ``link`` node's ``url`` in an mdast tree, found recursively."""
    if not isinstance(node, dict):
        return out
    if node.get("type") == "link" and isinstance(node.get("url"), str):
        out.append(node["url"])
    for value in node.values():
        if isinstance(value, list):
            for child in value:
                mdast_links(child, out)
        elif isinstance(value, dict):
            mdast_links(value, out)
    return out


def docs_page_path(url: str) -> str | None:
    """A docs.nucleus.engineering link's path, normalized with a trailing
    slash, or None if the link points elsewhere."""
    try:
        parsed = urlparse(url)
    except ValueError:
        return None
    if parsed.hostname != DOCS_HOST:
        return None
    path = parsed.path if parsed.path.endswith("/") else parsed.path + "/"
    return path


def fetch_citing_notes() -> dict[str, list[dict]]:
    """Every docs page that at least one DevNote links to, each with the
    DevNotes that cite it (deduplicated per page)."""
    works = get_json(f"{SCMS_BASE}/works?limit=500")["items"]
    by_page: dict[str, list[dict]] = {}
    for work in works:
        cdn, cdn_key = work.get("cdn"), work.get("cdn_key")
        if not cdn or not cdn_key:
            continue
        try:
            config = get_json(f"{cdn}{cdn_key}/config.json")
            project = (config.get("projects") or [{}])[0]
            index = project.get("index")
            if not index:
                continue
            content = get_json(f"{cdn}{cdn_key}/content/{index}.json")
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError):
            continue  # one unreachable or malformed note shouldn't break the rest

        pages_cited = {docs_page_path(u) for u in mdast_links(content.get("mdast"), [])}
        pages_cited.discard(None)
        if not pages_cited:
            continue

        # The SCMS /thumbnail endpoint (work.links.thumbnail) serves no
        # Content-Type header, which myst's image fetcher rejects outright
        # (confirmed: the bytes are a real, valid image — curl -I just shows
        # nothing). The CDN-hosted optimized thumbnail always has a real
        # extension and a correct header, so that's the one worth building
        # a static page with; a note with neither gets rendered with no
        # thumbnail rather than a card the build can't actually produce.
        thumb_path = project.get("thumbnailOptimized") or project.get("thumbnail")
        thumbnail = f"{cdn}{cdn_key}/public{thumb_path}" if thumb_path else None

        card = {
            "title": work.get("title", "Untitled"),
            "authors": [a.get("name") for a in (work.get("authors") or []) if a.get("name")],
            "collection": ((work.get("collection") or {}).get("content") or {}).get("title"),
            "thumbnail": thumbnail,
            "url": (work.get("links") or {}).get("html"),
        }
        for page in pages_cited:
            by_page.setdefault(page, []).append(card)
    return by_page


def render_cards(cards: list[dict]) -> str:
    lines = ["::::{grid} 1 1 2 2", ""]
    for card in cards:
        byline = ", ".join(card["authors"]) or "Unknown author"
        if card["collection"]:
            byline += f" · {card['collection']}"
        lines.append(f":::{{card}} {card['title']}")
        lines.append(f":link: {card['url']}")
        lines.append(f":footer: {byline}")
        lines.append("")
        if card["thumbnail"]:
            lines.append(f"![]({card['thumbnail']})")
        lines.append(":::")
        lines.append("")
    lines.append("::::")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "page",
        nargs="?",
        help="a docs/ page path, e.g. docs/modules/detector-tetr-atc/spec",
    )
    parser.add_argument(
        "--list-all",
        action="store_true",
        help="list every docs page with at least one citing DevNote, and how many",
    )
    args = parser.parse_args()

    if not args.page and not args.list_all:
        parser.error("pass a page path, or --list-all")

    by_page = fetch_citing_notes()

    if args.list_all:
        for path, cards in sorted(by_page.items()):
            print(f"{len(cards):>2}  {path}")
        return 0

    target = "/" + args.page.strip("/") + "/"
    cards = by_page.get(target)
    if not cards:
        print(f"No DevNotes link to {target}", file=sys.stderr)
        return 1
    print(render_cards(cards))
    return 0


if __name__ == "__main__":
    sys.exit(main())
