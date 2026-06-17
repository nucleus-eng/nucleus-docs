#!/usr/bin/env python3
"""
check-formatting.py — detect hard-wrapped prose paragraphs in Markdown files.

CLAUDE.md requires prose paragraphs to be written as a single line regardless
of length. This script flags consecutive non-blank prose lines in the same
paragraph, which indicate a hard line-wrap.

This check is WARNING-ONLY by default (exits 0 even with findings). Pass
--strict to exit 1 when findings are present, for local enforcement.

Usage:
    python3 scripts/check-formatting.py              # check docs/ and templates/
    python3 scripts/check-formatting.py docs/        # check specific path(s)
    python3 scripts/check-formatting.py --strict     # exit 1 if findings found
"""

import re
import subprocess
import sys
from pathlib import Path

# Lines matching these patterns are not prose and don't form hard-wrap pairs.
# Order matters: checked top to bottom; first match wins.
_SKIP_PATTERNS = [
    re.compile(r"^---"),                          # frontmatter fence / thematic break
    re.compile(r"^```"),                          # fenced code block
    re.compile(r"^:{2,}"),                        # MyST directive fence (:::, ::::, etc.)
    re.compile(r"^\s*\|"),                        # table row
    re.compile(r"^\s*[-*+] "),                    # unordered list item
    re.compile(r"^\s*\d+\. "),                    # ordered list item
    re.compile(r"^\s*- \["),                      # checkbox list item
    re.compile(r"^\s*>"),                         # blockquote
    re.compile(r"^#{1,6} "),                      # heading
    re.compile(r"^\s*<!--"),                      # HTML comment (opening or self-closing)
    re.compile(r"^\s*<[a-zA-Z/]"),               # HTML tag (e.g. <br>, </div>)
    re.compile(r"^\s*\{[%{]"),                    # Jinja / MyST template tag
    re.compile(r"^\s*:[a-z_-]+:"),               # MyST role or directive option
]


def _is_skip_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return True  # blank line
    for pat in _SKIP_PATTERNS:
        if pat.match(line) or pat.match(stripped):
            return True
    return False


def check_file(path: Path) -> list[tuple[int, str]]:
    """Return (lineno, message) for each hard-wrapped prose line."""
    findings = []
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return findings

    lines = text.splitlines()
    in_frontmatter = False
    in_code_fence = False
    directive_fence_stack: list[int] = []
    in_html_comment = False
    prev_was_prose = False

    for i, raw in enumerate(lines, start=1):
        stripped = raw.strip()

        # Track frontmatter block (leading --- ... ---)
        if i == 1 and stripped == "---":
            in_frontmatter = True
            prev_was_prose = False
            continue
        if in_frontmatter:
            if stripped == "---":
                in_frontmatter = False
            prev_was_prose = False
            continue

        # Track multi-line HTML comments (<!-- ... -->)
        if in_html_comment:
            if "-->" in raw:
                in_html_comment = False
            prev_was_prose = False
            continue
        if stripped.startswith("<!--") and "-->" not in raw:
            in_html_comment = True
            prev_was_prose = False
            continue

        # Track fenced code blocks (``` ... ```)
        if re.match(r"^```", raw):
            in_code_fence = not in_code_fence
            prev_was_prose = False
            continue
        if in_code_fence:
            prev_was_prose = False
            continue

        # Track MyST directive fences (:::+ ... :::+) using a depth stack so
        # nested fences (e.g. ::::{tab-item} inside ::::::{tab-set}) don't
        # cause a premature close of the outer block.
        directive_match = re.match(r"^(:{3,})", raw)
        if directive_match:
            depth = len(directive_match.group(1))
            if directive_fence_stack and depth <= directive_fence_stack[-1]:
                directive_fence_stack.pop()
            else:
                directive_fence_stack.append(depth)
            prev_was_prose = False
            continue
        if directive_fence_stack:
            prev_was_prose = False
            continue

        # Classify this line
        is_skip = _is_skip_line(raw)

        if is_skip:
            prev_was_prose = False
        else:
            if prev_was_prose:
                findings.append((i, "hard-wrapped prose line"))
            prev_was_prose = True

    return findings


def get_md_files(roots: list[str]) -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "--", *[f"{r}/**/*.md" for r in roots], *[f"{r}/*.md" for r in roots]],
        capture_output=True, text=True,
    )
    if result.returncode != 0:
        # Fall back to filesystem walk if not in a git repo
        paths = []
        for root in roots:
            paths.extend(Path(root).rglob("*.md"))
        return sorted(set(paths))
    seen = set()
    paths = []
    for p in result.stdout.splitlines():
        resolved = Path(p)
        if resolved not in seen:
            seen.add(resolved)
            paths.append(resolved)
    return paths


def main() -> int:
    args = sys.argv[1:]
    strict = "--strict" in args
    roots = [a for a in args if not a.startswith("--")] or ["docs", "templates"]

    files = get_md_files(roots)
    all_findings: list[tuple[Path, int, str]] = []

    for path in files:
        for lineno, msg in check_file(path):
            all_findings.append((path, lineno, msg))

    if all_findings:
        for path, lineno, msg in all_findings:
            print(f"{path}:{lineno}  {msg}")
        print(f"\n⚠️  {len(all_findings)} hard-wrapped prose line(s) found.")
        print("    Prose paragraphs should be a single line (see CLAUDE.md).")
        return 1 if strict else 0

    content_count = len(files)
    print(f"✅ No hard-wrapped prose lines found in {content_count} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
