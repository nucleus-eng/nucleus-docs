#!/usr/bin/env python3
"""
assemble-module-graph-artifact.py — Layer 4b: substitute freshly rendered
Mermaid blocks into the artifact's HTML shell.

Runs render-module-graph.py, then drops each of the six diagrams into its
`{{MERMAID:<key>}}` placeholder in module-graph-template.html. The shell
itself (design, CSS, pan/zoom script, and the surrounding curated prose in
"Reading the edges") is not regenerated -- only the six diagrams are data-
driven. The prose is its own kind of Layer 3: synthesis a human writes, not
structure a script emits, and it doesn't go stale the way a diagram does
every time a module's composition changes.

Usage:
    python3 scripts/assemble-module-graph-artifact.py --out module-graph.html
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
TEMPLATE = HERE / "module-graph-template.html"

PLACEHOLDER_RE = re.compile(r"\{\{MERMAID:(\w+)\}\}")


def render_blocks(out_dir: Path) -> dict:
    out = subprocess.run(
        [sys.executable, str(HERE / "render-module-graph.py"), "--out-dir", str(out_dir)],
        capture_output=True,
        text=True,
    )
    if out.returncode != 0:
        sys.exit(f"render-module-graph.py failed:\n{out.stderr}")
    print(out.stdout)

    blocks = {}
    for path in out_dir.glob("*.md"):
        key = path.stem.replace("-", "_")
        text = path.read_text().strip()
        # Strip the ```mermaid / ``` fence -- the HTML shell's own
        # <pre class="mermaid"> tag is the fence equivalent here.
        lines = text.splitlines()
        if lines[0].strip() == "```mermaid" and lines[-1].strip() == "```":
            lines = lines[1:-1]
        blocks[key] = "\n".join(lines)
    return blocks


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--blocks-dir", type=Path, default=Path("tmp/mermaid-blocks"))
    args = ap.parse_args()

    blocks = render_blocks(args.blocks_dir)
    html = TEMPLATE.read_text()

    missing = []

    def replace(m):
        key = m.group(1)
        if key not in blocks:
            missing.append(key)
            return m.group(0)
        return blocks[key]

    html = PLACEHOLDER_RE.sub(replace, html)
    if missing:
        sys.exit(f"no rendered block for placeholder(s): {missing}")

    args.out.write_text(html)
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()
