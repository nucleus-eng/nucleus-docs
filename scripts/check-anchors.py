#!/usr/bin/env python3
"""check-anchors.py — flag `#anchor` links that MyST will bind to the wrong page.

MyST resolves a link fragment by *global identifier* and ignores the file path.
Every module spec has headings called Overview, Requirements, Expected Behavior,
so those slugs collide across pages, and MyST binds each to whichever page won.
The reader lands somewhere else entirely — `../reporter-xyle/spec.md#expected-behavior`
went to the POPC/Chol membrane spec, and one page's own `[Overview](#overview)`
left `docs/` for a getting-started page.

`check-links.py` cannot see this: the named file exists and does own that heading,
so the link passes. Only the collision makes it wrong. That is what this checks.

The fix is a unique label above the target heading:

    (reporter-lacz-requirements)=
    # Requirements

and link to `../reporter-lacz/spec.md#reporter-lacz-requirements`. A link with no
fragment at all is also safe — it builds as a plain link and resolves by path.

Reads sources only, so it runs in well under a second and needs no myst build.

Usage:
    python3 scripts/check-anchors.py            # every page in the myst.yml TOC
    python3 scripts/check-anchors.py <file.md>  # links written in these files only

Exit codes: 0 nothing blocking, 1 mis-binding anchors found, 2 could not run.
"""
import importlib.util
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
MYST_YML = REPO / "myst.yml"

# `[text](target#fragment)` — captures the path part (may be empty) and fragment.
LINK = re.compile(r"\]\(([^)#\s]*)#([^)\s]+)\)")


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, REPO / "scripts" / filename)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def toc_pages() -> list[pathlib.Path]:
    """Every source file myst.yml publishes as a page."""
    try:
        import yaml
    except ImportError:
        print("error: pyyaml is required. Run: pip install pyyaml", file=sys.stderr)
        raise SystemExit(2)
    check_toc = _load("check_toc", "check-toc.py")
    data = yaml.safe_load(MYST_YML.read_text(encoding="utf-8"))
    toc = (data or {}).get("project", {}).get("toc") or (data or {}).get("toc")
    if not toc:
        print(f"error: no toc: in {MYST_YML}", file=sys.stderr)
        raise SystemExit(2)
    pages = []
    for _, resolved in check_toc.collect_toc_files(toc, MYST_YML.parent):
        for cand in (resolved, resolved.with_suffix(".md"), resolved.with_suffix(".ipynb")):
            if cand.is_file():
                pages.append(cand)
                break
    return pages


def main() -> int:
    links = _load("check_links", "check-links.py")
    pages = toc_pages()
    if not pages:
        print("error: resolved no pages from the TOC", file=sys.stderr)
        return 2

    # identifier -> pages that define it
    owners: dict[str, list[pathlib.Path]] = {}
    for page in pages:
        for anchor in links.myst_anchors(str(page)):
            owners.setdefault(anchor, []).append(page)

    if len(sys.argv) > 1:
        targets = [pathlib.Path(a).resolve() for a in sys.argv[1:]]
    else:
        targets = pages

    findings = []
    for page in targets:
        try:
            text = page.read_text(encoding="utf-8")
        except OSError:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for path_part, frag in LINK.findall(line):
                frag = frag.split("#")[0]
                defs = owners.get(links.myst_html_id(frag), [])
                if len(defs) > 1:
                    named = (page.parent / path_part).resolve() if path_part else page
                    findings.append((page, lineno, path_part, frag, named, defs))

    rel = lambda p: str(p.relative_to(REPO)) if p.is_relative_to(REPO) else str(p)

    if not findings:
        print(f"✅ no ambiguous anchors. {len(targets)} page(s) checked, "
              f"{len(owners)} identifier(s) collected.")
        return 0

    print(f"❌ {len(findings)} anchor(s) MyST will bind to the wrong page:\n")
    for page, lineno, path_part, frag, named, defs in findings:
        where = f"{path_part}#{frag}" if path_part else f"#{frag}"
        print(f"  {rel(page)}:{lineno}")
        print(f"      wrote:      {where}")
        print(f"      meant:      {rel(named)}")
        print(f"      but #{frag} is defined on {len(defs)} pages, so MyST picks one:")
        for d in defs[:4]:
            print(f"                    {rel(d)}")
        if len(defs) > 4:
            print(f"                    ... and {len(defs) - 4} more")
        print()
    print("Fix: give the target heading a unique label and link to that.\n"
          "     (reporter-lacz-requirements)=\n"
          "     # Requirements\n"
          "Name labels <module-directory>-<section-slug>. A link with no fragment is\n"
          "also safe. See style-guide/conventions.md § Cross-references.")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 — tooling breakage is exit 2, not a finding
        print(f"error: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(2)
