#!/usr/bin/env python3
"""
check-toc.py — validate myst.yml TOC against the docs/ file tree.

Two checks:

  STRICT (error, exit 1): every file: entry in myst.yml must resolve to an
  existing file. Broken TOC references are always wrong — zero false positives.

  ADVISORY (warning, exit 0): every .md file under docs/ should appear in the
  TOC. Files excluded by naming convention (protocol-*.md, bom-*.md) or by an
  inline allowlist of known intentional non-sidebar pages are skipped.

hidden: true entries ARE real TOC entries — their files must exist.
title:-only nodes (no file: key) are skipped.

Usage:
    python3 scripts/check-toc.py
    python3 scripts/check-toc.py myst.yml
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: pyyaml is required. Run: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

MYST_YML = Path("myst.yml")
DOCS_ROOT = Path("docs")

# Files intentionally not in the sidebar (known stragglers).
# Paths relative to repo root.
ADVISORY_ALLOWLIST = {
    "docs/processes/make-36pot/assemble-pmix/main.md",
    "docs/modules/reporter-degfp/bom-cells.md",
    "docs/modules/reporter-degfp/bom-cytosol.md",
    "docs/modules/reporter-degfp/protocol-cells.md",
    "docs/modules/reporter-degfp/protocol-cytosol.md",
}

# Naming-convention exclusions (basename patterns).
ADVISORY_EXCLUDE_PREFIXES = ("protocol-", "bom-")
ADVISORY_EXCLUDE_SUFFIXES = ("-main.md",)  # index pages that are TOC roots themselves


def collect_toc_files(node, base: Path) -> list[tuple[str, Path]]:
    """Recursively collect (raw_ref, resolved_path) from a TOC node or list."""
    results = []
    if isinstance(node, list):
        for item in node:
            results.extend(collect_toc_files(item, base))
    elif isinstance(node, dict):
        if "file" in node:
            raw = node["file"]
            resolved = (base / raw).resolve()
            results.append((raw, resolved))
        for key in ("children",):
            if key in node:
                results.extend(collect_toc_files(node[key], base))
    return results


def advisory_excluded(path: Path) -> bool:
    name = path.name.lower()
    if any(name.startswith(p) for p in ADVISORY_EXCLUDE_PREFIXES):
        return True
    if any(name.endswith(s) for s in ADVISORY_EXCLUDE_SUFFIXES):
        return True
    rel = str(path).replace("\\", "/")
    if rel in ADVISORY_ALLOWLIST:
        return True
    return False


def main() -> int:
    myst_path = Path(sys.argv[1]) if len(sys.argv) > 1 else MYST_YML
    if not myst_path.exists():
        print(f"error: {myst_path} not found", file=sys.stderr)
        return 1

    config = yaml.safe_load(myst_path.read_text(encoding="utf-8"))
    toc = config.get("project", {}).get("toc") or config.get("toc", [])
    base = myst_path.parent

    toc_entries = collect_toc_files(toc, base)
    toc_resolved = {p for _, p in toc_entries}

    # --- STRICT: every TOC entry must resolve ---
    strict_errors = 0
    for raw, resolved in toc_entries:
        if not resolved.exists():
            # Report relative to repo root
            try:
                rel = resolved.relative_to(base.resolve())
            except ValueError:
                rel = resolved
            print(f"{myst_path}:  broken TOC reference: {raw!r} → {rel} does not exist")
            strict_errors += 1

    if strict_errors:
        print(f"\n{strict_errors} broken TOC reference(s). Fix myst.yml.")
        return 1

    # --- ADVISORY: every docs/ .md should appear in the TOC ---
    advisory_warnings = 0
    all_docs_md = sorted(DOCS_ROOT.rglob("*.md")) if DOCS_ROOT.exists() else []
    for md in all_docs_md:
        if "generated" in md.parts:
            continue
        if advisory_excluded(md):
            continue
        resolved = md.resolve()
        if resolved not in toc_resolved:
            print(f"warning: {md}  not in myst.yml TOC (advisory)")
            advisory_warnings += 1

    if advisory_warnings:
        print(f"\n{advisory_warnings} advisory: file(s) not in TOC. Add to myst.yml or allowlist.")
    else:
        print(f"✅ TOC valid. {len(toc_entries)} entries checked, {len(all_docs_md)} docs/ files scanned.")

    return 0  # Advisory warnings do not fail CI


if __name__ == "__main__":
    sys.exit(main())
