#!/usr/bin/env python3
"""check-outbound-links.py — does every outbound link earn its place?

THE RULE, ruled 2026-10-05: an outbound link from a Module page is justified
only when its target is one of three things to the Module the page specifies:

  * a CONSTITUENT      -- it appears in `inputs[].page`, or as a step operand
  * a REQUIRED PROCESS -- it appears in `process_steps[].process.page`
  * an IMPLEMENTATION  -- it is listed under `# Implementations`
  * a MEMBER           -- it declares `refines:` THIS Module. Added after a first
                          measurement: the five worst pages were all classes, and
                          a class page exists to link its members.

CONSTITUENCY IS TRANSITIVE HERE. A Reference Composition table names the reagents
a Module is built from, which is the closure of `inputs[].page`, not the one step
of it the source declares. Measured: allowing only the direct inputs put 179 of
615 findings in that one section.

Anything else is a page reaching for context it does not own. The motivating
case is the demo gloss: "[Embedding: Ionic Crosslinking](...) - the Chicago
hydrogel format", on a page that does not run that process.

WHAT IS EXEMPT, AND WHY EACH ONE IS.

  * `# Credits` and `# References` -- a credit links a Node or an ORCID, which
    is none of the three, and the rule must not delete attribution.
  * The page's own anchors, and any link into the page's own directory.
  * External URLs and DOIs -- the rule is about the corpus's internal shape.
  * A link to the class this Module `refines:` -- a member naming its parent is
    the refinement order, not context.

IT REPORTS AND DOES NOT BLOCK, and always exits 0 unless it could not run.
A rule this sharp earns its severity by being measured first; the same posture
as check-page-layering.py.

A page with no `spec.yml` CANNOT BE CHECKED and is counted separately rather
than passing. A clean run over pages nothing could be read for is the failure
this script is most likely to produce.

    python3 scripts/check-outbound-links.py
    python3 scripts/check-outbound-links.py --json
"""
import argparse, json, re, sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("error: pyyaml is required; pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
MODULES = ROOT / "docs" / "modules"

LINK = re.compile(r"\[(?P<text>[^\]]*)\]\((?P<href>[^)\s]+)(?:\s+\"[^\"]*\")?\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
EXEMPT_SECTIONS = {"credits", "references", "downloads"}


def sections(text):
    """Yield (line_no, line, current_h1_lowercased)."""
    current = ""
    for i, line in enumerate(text.splitlines(), 1):
        m = HEADING.match(line)
        if m and len(m.group(1)) == 1:
            current = m.group(2).strip().lower()
        yield i, line, current


def direct(doc, mod_dir):
    """The pages this one source names: constituents, processes, parents."""
    out = set()

    def add(p):
        if p and isinstance(p, str):
            out.add((mod_dir / p).resolve())

    for v in (doc.get("inputs") or {}).values():
        add((v or {}).get("page"))
    for s in doc.get("process_steps") or []:
        pr = s.get("process") or {}
        add(pr.get("page"))
        add((s.get("produces") or {}).get("page"))
    r = doc.get("refines")
    for name in ([r] if isinstance(r, str) else (r or [])):
        add(f"../{name}/spec.md")
    return out


def allowed_targets(name, sources, members, direct_by_mod):
    """Direct dependencies, their closure, and this Module's own members."""
    out, seen, stack = set(), {name}, [name]
    while stack:
        cur = stack.pop()
        for t in direct_by_mod.get(cur, ()):
            out.add(t)
            # Walk into a Module page so constituency closes transitively.
            nxt = t.parent.name
            if t.name == "spec.md" and nxt in sources and nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    for m in members.get(name, ()):
        out.add((MODULES / m / "spec.md").resolve())
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if not MODULES.is_dir():
        sys.exit(f"error: no {MODULES}; run from the repo root")

    findings, checked, unreadable, links_total = [], 0, [], 0

    # Read every source first: the closure and the member list both need all of
    # them before any one page can be judged.
    sources, direct_by_mod, members = {}, {}, {}
    for d in sorted(MODULES.iterdir()):
        src = d / "spec.yml"
        if not (d / "spec.md").is_file():
            continue
        if not src.is_file():
            unreadable.append(d.name)
            continue
        try:
            sources[d.name] = yaml.safe_load(src.read_text()) or {}
        except yaml.YAMLError as e:
            unreadable.append(f"{d.name} (unparseable: {e.__class__.__name__})")
    for name, doc in sources.items():
        direct_by_mod[name] = direct(doc, MODULES / name)
        r = doc.get("refines")
        for parent in ([r] if isinstance(r, str) else (r or [])):
            members.setdefault(parent, []).append(name)

    for name in sorted(sources):
        d = MODULES / name
        page, doc = d / "spec.md", sources[name]

        checked += 1
        ok = allowed_targets(name, sources, members, direct_by_mod)
        impl_links = set()
        text = page.read_text()

        # Implementations is a section, so collect its links in a first pass.
        for _, line, sec in sections(text):
            if sec.startswith("implementation"):
                for m in LINK.finditer(line):
                    impl_links.add(m.group("href").split("#")[0])

        for lineno, line, sec in sections(text):
            if sec in EXEMPT_SECTIONS or sec.startswith("implementation"):
                continue
            for m in LINK.finditer(line):
                href = m.group("href")
                if href.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                bare = href.split("#")[0]
                if not bare or not bare.endswith(".md"):
                    continue
                target = (d / bare).resolve()
                if target.parent == d.resolve():
                    continue                      # within its own directory
                links_total += 1
                if target in ok or bare in impl_links:
                    continue
                findings.append({
                    "file": str(page.relative_to(ROOT)),
                    "line": lineno,
                    "section": sec or "(before any heading)",
                    "text": m.group("text")[:60],
                    "href": bare,
                })

    if a.json:
        print(json.dumps({"findings": findings, "checked": checked,
                          "links_checked": links_total,
                          "unreadable": unreadable}, indent=1))
        return 0

    by_file = {}
    for f in findings:
        by_file.setdefault(f["file"], []).append(f)
    for fn in sorted(by_file, key=lambda k: (-len(by_file[k]), k)):
        print(f"\n{fn}  — {len(by_file[fn])}")
        for f in by_file[fn]:
            print(f"  :{f['line']:<4} [{f['section']}]  [{f['text']}]({f['href']})")

    print(f"\n{'=' * 70}")
    print(f"{len(findings)} unjustified of {links_total} outbound links, "
          f"over {checked} Module pages with a readable source.")
    print(f"{len(unreadable)} page(s) HAD NO READABLE spec.yml AND WERE NOT CHECKED"
          + (f": {', '.join(unreadable)}" if unreadable else "."))
    print("Reports only; never blocks.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
