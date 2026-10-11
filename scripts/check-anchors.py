#!/usr/bin/env python3
"""check-anchors.py — flag anchors MyST will bind to the wrong page.

MyST resolves a link fragment by *global identifier* and ignores the file path.
Every module spec has headings called Overview, Requirements, Expected Behavior,
so those slugs collide across pages, and MyST binds each to whichever page won.
The reader lands somewhere else entirely — `../reporter-xyle/spec.md#expected-behavior`
went to the POPC/Chol membrane spec, and one page's own `[Overview](#overview)`
left `docs/` for a getting-started page.

`check-links.py` cannot see this: the named file exists and does own that heading,
so the link passes. Only the collision makes it wrong. That is what this checks.

This script reports two different things, and the difference matters:

  AMBIGUOUS LINK (present defect) — a link is written to a fragment that more
  than one page defines. A reader clicking it lands on the wrong page today.

  DUPLICATE DEFINITION (latent defect) — one explicit label is defined at more
  than one site. Nothing need link to it. Nothing is wrong on the rendered site
  until someone writes the link, and then it is wrong silently. Reporting only
  the first kind means the collision is found only after it has been armed.

Heading slugs are deliberately excluded from the duplicate-definition pass.
Repeated headings are normal and expected here (52 of them across the TOC), and
the remedy for a repeated heading is a unique label *at the point you link to
it* — which is what the ambiguous-link pass already enforces. An explicit label
is different: writing `:name: os-prep` is an author deliberately claiming a
name, and two authors claiming the same one is always a mistake.

The fix for either is a unique label above the target:

    (reporter-lacz-requirements)=
    # Requirements

and link to `../reporter-lacz/spec.md#reporter-lacz-requirements`. A link with no
fragment at all is also safe — it builds as a plain link and resolves by path.

Scope note. The ambiguous-link pass reads the myst.yml TOC, because only a page
in the TOC can be linked to. The duplicate-definition pass reads every content
file under CONTENT_ROOTS, TOC or not. A page outside the TOC is not in the built
site's cross-reference index, so its labels collide with nothing *today* — but it
is one TOC entry away from colliding, and that is exactly the latent case worth
reporting. `templates/` is excluded: starter files repeat placeholder labels like
`fig-schematic` on purpose.

Reads sources only, so it runs in well under a second and needs no myst build.

Usage:
    python3 scripts/check-anchors.py            # whole repo
    python3 scripts/check-anchors.py <file.md>  # findings touching these files only

Exit codes: 0 nothing blocking, 1 findings, 2 could not run.
"""
import importlib.util
import pathlib
import re
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
MYST_YML = REPO / "myst.yml"

# Content directories whose pages share one MyST identifier namespace.
# `templates/` is excluded on purpose — see the module docstring.
CONTENT_ROOTS = ("docs", "guides", "about", "start", "cdk")

# `[text](target#fragment)` — captures the path part (may be empty) and fragment.
LINK = re.compile(r"\]\(([^)#\s]*)#([^)\s]+)\)")

# An explicit identifier: a directive option, or a `(target)=` block.
OPTION = re.compile(r"^:(?:label|name):\s+(\S+)\s*$")
TARGET = re.compile(r"^\(([^)]+)\)=\s*$")

# A fence opener. ```{note} is a MyST directive and its body is live content;
# a bare ``` is a literal block and everything inside it is only an example.
FENCE = re.compile(r"^\s*(?P<fence>`{3,}|~{3,})(?P<info>.*)$")


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


def content_pages() -> list[pathlib.Path]:
    """Every markdown source under CONTENT_ROOTS, whether or not it is in the TOC."""
    found = set()
    for root in CONTENT_ROOTS:
        found.update((REPO / root).rglob("*.md"))
    return sorted(p for p in found if p.is_file())


def explicit_definitions(path: pathlib.Path) -> list[tuple[str, int]]:
    """Every explicit identifier a file defines, as (identifier, line number).

    Skips literal code fences. A page that teaches MyST syntax shows the same
    `:label:` twice — once in a ``` block as the source, once rendered below it
    as "will appear as..." — and only the rendered one is a real definition.
    Counting both reports a duplicate on every syntax guide in the repo.

    Returns a list, not a set: two definitions of one identifier on the *same*
    page is a finding too, and a set would hide it.
    """
    links = _load("check_links", "check-links.py")
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return []

    found: list[tuple[str, int]] = []
    fence = None  # the literal fence we are inside, as its opening token
    for lineno, line in enumerate(text.splitlines(), 1):
        opener = FENCE.match(line)
        if opener:
            token = opener.group("fence")
            if fence is None:
                # ```{directive} is live content; a bare ``` is a literal block.
                if not opener.group("info").strip().startswith("{"):
                    fence = token
            elif line.strip().startswith(fence[0] * len(fence)):
                fence = None
            continue
        if fence is not None:
            continue
        stripped = line.strip()
        match = OPTION.match(stripped) or TARGET.match(stripped)
        if match:
            found.append((links.myst_html_id(match.group(1)), lineno))
    return found


def main() -> int:
    links = _load("check_links", "check-links.py")
    pages = toc_pages()
    if not pages:
        print("error: resolved no pages from the TOC", file=sys.stderr)
        return 2

    # --- identifier -> TOC pages that define it (headings included) ----------
    owners: dict[str, list[pathlib.Path]] = {}
    for page in pages:
        for anchor in links.myst_anchors(str(page)):
            owners.setdefault(anchor, []).append(page)

    # --- explicit identifier -> every site that defines it ------------------
    # Content roots, plus every TOC page wherever it sits. `intro.md` is the site
    # root and lives at the repo root, outside CONTENT_ROOTS — anything MyST
    # builds is in the identifier namespace, so anything MyST builds gets read.
    sources = sorted(set(content_pages()) | set(pages))
    if not sources:
        print("error: resolved no content files", file=sys.stderr)
        return 2
    defined: dict[str, list[tuple[pathlib.Path, int]]] = {}
    for page in sources:
        for ident, lineno in explicit_definitions(page):
            defined.setdefault(ident, []).append((page, lineno))

    if len(sys.argv) > 1:
        targets = [pathlib.Path(a).resolve() for a in sys.argv[1:]]
    else:
        targets = pages

    # --- pass 1: links that bind to the wrong page --------------------------
    ambiguous = []
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
                    ambiguous.append((page, lineno, path_part, frag, named, defs))

    # --- pass 2: identifiers defined more than once -------------------------
    selected = {p.resolve() for p in targets} if len(sys.argv) > 1 else None
    duplicates = []
    for ident, sites in sorted(defined.items()):
        if len(sites) < 2:
            continue
        if selected is not None and not any(p.resolve() in selected for p, _ in sites):
            continue
        duplicates.append((ident, sites))

    toc_set = {p.resolve() for p in pages}
    rel = lambda p: str(p.relative_to(REPO)) if p.is_relative_to(REPO) else str(p)

    # Say what was READ, not just how much. A count tells a reader how much of a
    # set was scanned and never which set it was — and the whole reason this
    # script grew a second pass is that its green line looked thorough while
    # reading none of the files holding the defect.
    roots = "".join(f"{r}/, " for r in CONTENT_ROOTS)
    domain = (
        f"   links read:       {len(targets)} page(s) from the myst.yml TOC\n"
        f"                     ({len(owners)} identifier(s) collected, headings included)\n"
        f"   definitions read: {len(sources)} file(s) under {roots}plus every TOC page\n"
        f"                     ({len(defined)} explicit label(s); templates/ excluded, "
        f"literal code fences skipped)"
    )

    if not ambiguous and not duplicates:
        print("✅ no ambiguous anchors, no duplicate definitions.")
        print(domain)
        return 0

    if ambiguous:
        print(f"❌ {len(ambiguous)} anchor(s) MyST will bind to the wrong page "
              f"(present defect — the link is wrong today):\n")
        for page, lineno, path_part, frag, named, defs in ambiguous:
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

    if duplicates:
        print(f"❌ {len(duplicates)} identifier(s) defined more than once "
              f"(latent defect — nothing links here yet, so nothing looks wrong):\n")
        for ident, sites in duplicates:
            in_toc = sum(1 for p, _ in sites if p.resolve() in toc_set)
            if in_toc > 1:
                note = f"{in_toc} of these are TOC pages — they collide in the built site now"
            else:
                note = ("only one is a TOC page, so the built site has no collision yet; "
                        "adding another to the TOC creates one")
            print(f"  {ident} — defined at {len(sites)} sites")
            print(f"      {note}")
            for p, lineno in sites:
                tag = "TOC" if p.resolve() in toc_set else "not in TOC"
                print(f"                    {rel(p)}:{lineno}  [{tag}]")
            print()

    print(domain)
    print()
    print("Fix: give each one a unique label derived from its own page, and link to that.\n"
          "     (reporter-degfp-cells-rxn-setup)=\n"
          "     # Reaction Setup\n"
          "Name labels <page-directory>-<page>-<section-slug>. The module directory\n"
          "alone is not enough when one directory holds two pages. A link with no\n"
          "fragment is also safe. See style-guide/conventions.md § Cross-references.")
    return 1


if __name__ == "__main__":
    try:
        sys.exit(main())
    except SystemExit:
        raise
    except Exception as exc:  # noqa: BLE001 — tooling breakage is exit 2, not a finding
        print(f"error: {type(exc).__name__}: {exc}", file=sys.stderr)
        sys.exit(2)
