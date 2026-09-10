#!/usr/bin/env python3
"""Check each module's `# Constituent Modules` prose against its composition.yml.

Jon ruled on 2026-09-09 that the prose section stays for humans while the yml
is the contract for tooling (#248). Two sources for one fact drift, and this one
already did: `london-cascade` listed `Substrate: CPRG` where its own source said
`GUV: CPRG`, within an hour of both existing. Nothing caught it, because every
other check in this repo validates one file against itself.

Two findings, and they are not the same severity.

  MISSING   a module the prose lists that the source never mentions.
            Blocking. The prose is asserting a constituent the build does not
            have, which is what went wrong on london-cascade.

  UNLISTED  an operand of the final step, with a page, that the prose omits.
            Reported, not blocking. The final step's operands are the direct
            constituents, so the prose should usually name them — but a page
            may legitimately describe its constituents at a different grain.
            `chicago-cascade` names two Cascades where the source names the two
            gel pieces they end as, and neither is wrong.

Exit 0 nothing blocking, 1 a MISSING, 2 the check could not run.

    python3 scripts/check-composition.py
    python3 scripts/check-composition.py docs/modules/london-cascade
"""
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML not installed — cannot run (exit 2)")


def repo_root() -> Path:
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True)
    if out.returncode:
        sys.exit("not inside a git repository (exit 2)")
    return Path(out.stdout.strip())


def slug_of(page: str | None) -> str | None:
    """`../guv-cprg/spec.md` -> `guv-cprg`. Only module pages have a slug."""
    if not page:
        return None
    m = re.search(r"\.\./([A-Za-z0-9._-]+)/spec\.md$", page)
    return m.group(1) if m else None


def prose_constituents(text: str) -> list[str]:
    """Slugs bullet-linked under `# Constituent Modules`, in order.

    Only bullets count. A link in the surrounding prose is a mention, not a
    declaration — the same rule gen-module-diagrams.py uses.
    """
    m = re.search(r"^#+\s*Constituent Modules\s*$(.*?)(?=^#|\Z)", text, re.M | re.S)
    if not m:
        return []
    out = []
    for line in m.group(1).splitlines():
        if not line.lstrip().startswith(("-", "*")):
            continue
        link = re.search(r"\]\(\.\./([A-Za-z0-9._-]+)/spec\.md", line)
        if link and link.group(1) not in out:
            out.append(link.group(1))
    return out


def source_slugs(doc: dict) -> tuple[set[str], set[str]]:
    """(every module the source names, the final step's operands with pages)."""
    named, pages = set(), {}
    for key, v in (doc.get("inputs") or {}).items():
        if (s := slug_of(v.get("page"))):
            named.add(s)
            pages[key] = s
    for step in doc.get("steps") or []:
        out = step["produces"]
        if (s := slug_of(out.get("page"))):
            named.add(s)
            pages[out["id"]] = s
    steps = doc.get("steps") or []
    direct = {pages[o] for o in steps[-1]["operands"] if o in pages} if steps else set()
    return named, direct


def check(spec: Path, src: Path) -> tuple[list[str], list[str]]:
    doc = yaml.safe_load(src.read_text(encoding="utf-8"))
    named, direct = source_slugs(doc)
    listed = prose_constituents(spec.read_text(encoding="utf-8"))
    missing = [s for s in listed if s not in named]
    unlisted = sorted(s for s in direct if s not in listed)
    return missing, unlisted


def main() -> int:
    root = repo_root()
    targets = [Path(a) for a in sys.argv[1:] if not a.startswith("-")]
    roots = targets or [root / "docs" / "modules"]
    sources = sorted({p for r in roots for p in Path(r).rglob("composition.yml")})
    if not sources:
        print(f"no composition.yml under {', '.join(str(r) for r in roots)}")
        return 0

    blocking, reported = 0, 0
    for src in sources:
        spec = src.parent / "spec.md"
        if not spec.is_file():
            print(f"⛔️ {src.parent.name}: composition.yml with no spec.md")
            blocking += 1
            continue
        missing, unlisted = check(spec, src)
        for s in missing:
            print(f"⛔️ {spec}: '# Constituent Modules' lists {s}, "
                  f"which composition.yml never names")
            blocking += 1
        for s in unlisted:
            print(f"⚠️  {spec}: {s} is an operand of the final step "
                  f"but is not in '# Constituent Modules'")
            reported += 1

    n = len(sources)
    if blocking:
        print(f"\n⛔️ {blocking} blocking, {reported} reported, {n} source(s) checked")
        return 1
    print(f"\n✅ prose agrees with source. {reported} reported, {n} source(s) checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
