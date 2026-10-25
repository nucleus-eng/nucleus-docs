#!/usr/bin/env python3
"""
build-devnote-cards.py — write a "# Supported by" card block of DevNotes
onto every module, process, and implementation page it applies to.

A page's supporting DevNotes come from two signals, merged:

1. The manual mapping in ``scripts/devnote-associations.yml`` (see
   ``build-devnote-counts.py``) — a human reviewed every published DevNote
   and tagged which module(s)/process(es)/implementation(s) it supports.
   This catches a DevNote that doesn't link back to the page at all.
2. An outbound link from a DevNote's own rendered content back to
   ``docs.nucleus.engineering`` (detected live from the DevNotes SCMS API) —
   catches a DevNote not yet in the manual mapping.

Fetches every work from the DevNotes SCMS API, reads each one's rendered
page content and config from its CDN (for thumbnails and outbound links),
and writes a ``grid``/``card`` block — thumbnail, title, byline — styled as
a compact list via the ``devnote-cards`` CSS class (see
assets/style-sheet.css), replacing any "# Supported by" section already on
the page or appending a new one at the end (after "# Credits" or
"# Downloads", wherever the page's last section is).

Not wired into the ``generated/`` + CI pattern ``build-protocols.py`` and
``build-materials-reference.py`` use — run locally and commit the result,
same as a manual edit. Doing that is the natural next step once the
network-call-during-build question gets its own discussion.

Usage:
    python3 scripts/build-devnote-cards.py --sync             # every mapped/cited page
    python3 scripts/build-devnote-cards.py --sync --dry-run   # preview, write nothing
    python3 scripts/build-devnote-cards.py docs/modules/detector-tetr-atc/spec
    python3 scripts/build-devnote-cards.py --list-all   # every page with a detected backlink
"""

import argparse
import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

try:
    import yaml
except ImportError:
    print("error: pyyaml required — pip install pyyaml", file=sys.stderr)
    sys.exit(1)

SCMS_BASE = "https://scms.curvenote.com/v1/sites/bnext-devnotes"
DOCS_HOST = "docs.nucleus.engineering"
TIMEOUT = 20

REPO_ROOT = Path(__file__).parent.parent.resolve()
DOCS_ROOT = REPO_ROOT / "docs"
ASSOCIATIONS_FILE = Path(__file__).parent / "devnote-associations.yml"

SECTION_HEADING = "# Supported by"
SECTION_INTRO = "DevNotes that reference this spec, not curated attribution; see Credits for that."
SECTION_INTRO_NO_CREDITS = "DevNotes that reference this page, not curated attribution."

# docs/<content-type> -> the devnote-associations.yml field naming it
CONTENT_TYPES = {"modules": "modules", "processes": "processes", "implementations": "implementations"}
PAGE_FILENAMES = {"spec.md", "main.md"}  # canonical page filenames, plus any *-main.md


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


def sanitize_key(value: str) -> str:
    """Match the key the Module x DevNote Map tool writes: slug-or-id with
    anything outside the db-path charset flattened to '-'."""
    return re.sub(r"[^A-Za-z0-9_.~:@+-]", "-", value)


def fetch_all_notes() -> tuple[dict[str, list[dict]], dict[str, dict]]:
    """Returns (by_page, cards_by_key):
    - by_page: every docs page some DevNote's own content links to, with
      the DevNotes that cite it (the live "backlink" signal).
    - cards_by_key: every work's rendered card data, keyed by both its
      sanitized slug and its raw id, so a `devnote-associations.yml` key
      (whichever form it used) resolves to card data directly.
    """
    works = get_json(f"{SCMS_BASE}/works?limit=500")["items"]
    by_page: dict[str, list[dict]] = {}
    cards_by_key: dict[str, dict] = {}

    for work in works:
        cdn, cdn_key = work.get("cdn"), work.get("cdn_key")
        if not cdn or not cdn_key:
            continue
        try:
            config = get_json(f"{cdn}{cdn_key}/config.json")
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError, OSError):
            continue  # one unreachable or malformed note shouldn't break the rest
        project = (config.get("projects") or [{}])[0]

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
        for key in {sanitize_key(work.get("slug") or ""), sanitize_key(work["id"])}:
            if key:
                cards_by_key[key] = card

        index = project.get("index")
        if not index:
            continue
        try:
            content = get_json(f"{cdn}{cdn_key}/content/{index}.json")
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError, OSError):
            continue
        pages_cited = {docs_page_path(u) for u in mdast_links(content.get("mdast"), [])}
        pages_cited.discard(None)
        for page in pages_cited:
            by_page.setdefault(page, []).append(card)

    return by_page, cards_by_key


def render_cards(cards: list[dict]) -> str:
    lines = ["::::{grid} 1 1 1 1", ":class: devnote-cards", ""]
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


# --------------------------------------------------------------------------- #
# Mapping-driven sync across every module/process/implementation page
# --------------------------------------------------------------------------- #

def load_associations() -> dict:
    if not ASSOCIATIONS_FILE.exists():
        return {}
    return yaml.safe_load(ASSOCIATIONS_FILE.read_text(encoding="utf-8")) or {}


def target_pages() -> dict[Path, str]:
    """Every canonical module/process/implementation page, keyed path ->
    its slug (the directory name, matched against devnote-associations.yml's
    modules/processes/implementations lists)."""
    pages: dict[Path, str] = {}
    for content_type in CONTENT_TYPES:
        base = DOCS_ROOT / content_type
        if not base.exists():
            continue
        for page in sorted(base.rglob("*.md")):
            if "resources" in page.parts or page.parent == base:
                continue
            if page.name in PAGE_FILENAMES or page.name.endswith("-main.md"):
                pages[page.resolve()] = page.parent.name
    return pages


def devnote_keys_for(slug: str, field: str, associations: dict) -> set[str]:
    return {
        key for key, entry in associations.items()
        if entry and slug in (entry.get(field) or [])
    }


def insert_section(text: str, body: str) -> str:
    """Replace an existing "# Supported by" section (it's always last) or
    append a new one, preserving a single trailing newline."""
    text = text.rstrip("\n")
    heading_re = re.compile(rf"^{re.escape(SECTION_HEADING)}\s*$", re.MULTILINE)
    m = heading_re.search(text)
    if m:
        text = text[: m.start()].rstrip("\n")
    has_credits = re.search(r"^# Credits\s*$", text, re.MULTILINE) is not None
    intro = SECTION_INTRO if has_credits else SECTION_INTRO_NO_CREDITS
    new_section = f"{SECTION_HEADING}\n\n{intro}\n\n{body}"
    return text + "\n\n" + new_section + "\n"


def sync_all(dry_run: bool) -> None:
    associations = load_associations()
    by_page_backlinks, cards_by_key = fetch_all_notes()

    # The live backlink crawl's keys are URL paths (e.g. "/docs/modules/x/");
    # map each target page's own path the same way for lookup.
    def as_docs_path(md_path: Path) -> str:
        rel = md_path.relative_to(REPO_ROOT).with_suffix("")
        return "/" + str(rel) + "/"

    updated = 0
    for md_path, slug in sorted(target_pages().items()):
        content_type = md_path.relative_to(DOCS_ROOT).parts[0]
        field = CONTENT_TYPES[content_type]
        manual_keys = devnote_keys_for(slug, field, associations)
        backlink_cards = by_page_backlinks.get(as_docs_path(md_path), [])

        cards_by_title: dict[str, dict] = {c["title"]: c for c in backlink_cards}
        missing = []
        for key in manual_keys:
            card = cards_by_key.get(key)
            if card is None:
                missing.append(key)
                continue
            cards_by_title.setdefault(card["title"], card)

        if missing:
            print(f"warning: {slug}: no card data fetched for {sorted(missing)}", file=sys.stderr)
        if not cards_by_title:
            continue

        cards = sorted(cards_by_title.values(), key=lambda c: c["title"])
        body = render_cards(cards)
        text = md_path.read_text(encoding="utf-8")
        new_text = insert_section(text, body)
        if new_text == text:
            continue
        updated += 1
        print(f"{'(dry run) ' if dry_run else ''}{len(cards)} card(s) -> {md_path.relative_to(REPO_ROOT)}")
        if not dry_run:
            md_path.write_text(new_text, encoding="utf-8")

    print(f"\n{updated} page(s) {'would be ' if dry_run else ''}updated")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        "page",
        nargs="?",
        help="a docs/ page path, e.g. docs/modules/detector-tetr-atc/spec",
    )
    parser.add_argument(
        "--list-all",
        action="store_true",
        help="list every docs page with at least one live-detected backlink, and how many",
    )
    parser.add_argument(
        "--sync",
        action="store_true",
        help="write/refresh the \"# Supported by\" section on every page named in "
             "devnote-associations.yml or linked from a DevNote's own content",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="with --sync, print what would change without writing any file",
    )
    args = parser.parse_args()

    if args.sync:
        sync_all(dry_run=args.dry_run)
        return 0

    if not args.page and not args.list_all:
        parser.error("pass a page path, --list-all, or --sync")

    by_page, _cards_by_key = fetch_all_notes()

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
