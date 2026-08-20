#!/usr/bin/env python3
"""
build-graph.py — generate docs/graph.html, an interactive Cytoscape.js graph
of module / process / implementation relationships in the Nucleus Distribution.

Usage:
    python3 scripts/build-graph.py

Output: docs/graph.html  (self-contained; commit or gitignore as preferred)
"""

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: pyyaml required — pip install pyyaml", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).parent.parent.resolve()
DOCS_ROOT = REPO_ROOT / "docs"
OUTPUT = DOCS_ROOT / "graph-data.html"

# Map docs/ subdirectory -> node type label
CONTENT_DIRS = {
    "modules": "module",
    "processes": "process",
    "implementations": "implementation",
}

COLORS = {
    "module": "#4e9af1",
    "process": "#50c878",
    "implementation": "#f4a261",
}

# Page filenames that represent the canonical page for a content item
PAGE_FILENAMES = {"spec.md", "main.md"}


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #

def read_frontmatter(text: str) -> dict:
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not m:
        return {}
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return {}


def classify(path: Path):
    """Return (node_id, content_type) for a path under DOCS_ROOT, or None."""
    try:
        rel = path.resolve().relative_to(DOCS_ROOT)
    except ValueError:
        return None
    parts = rel.parts
    if not parts:
        return None
    content_type = CONTENT_DIRS.get(parts[0])
    if content_type is None:
        return None
    node_id = str(rel)
    return node_id, content_type


def resolve_href(src: Path, href: str):
    """Resolve a markdown link href to an absolute Path, or None if external."""
    href = href.split("#")[0].strip()
    if not href or not href.endswith(".md"):
        return None
    if re.match(r"^https?://|^mailto:", href):
        return None
    if href.startswith("/"):
        # Absolute from repo root
        return (REPO_ROOT / href.lstrip("/")).resolve()
    return (src.parent / href).resolve()


def extract_doc_links(src: Path, text: str) -> list[Path]:
    """Return all markdown link targets that resolve to doc pages."""
    results = []
    for m in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", text):
        target = resolve_href(src, m.group(1))
        if target is None:
            continue
        if classify(target) is not None:
            results.append(target)
    return results


# --------------------------------------------------------------------------- #
# Graph builder
# --------------------------------------------------------------------------- #

def find_pages():
    """Yield absolute Paths for canonical content pages under docs/."""
    for subdir in CONTENT_DIRS:
        base = DOCS_ROOT / subdir
        if not base.exists():
            continue
        for md in sorted(base.rglob("*.md")):
            if "generated" in md.parts or "resources" in md.parts:
                continue
            # Skip top-level index pages (e.g. modules-main.md directly in docs/modules/)
            if md.parent == base:
                continue
            if md.name in PAGE_FILENAMES or md.name.endswith("-main.md"):
                yield md


def build_graph():
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    seen_edges: set[tuple] = set()

    for path in find_pages():
        classified = classify(path)
        if classified is None:
            continue
        node_id, content_type = classified

        try:
            text = path.read_text(encoding="utf-8")
        except OSError:
            continue

        fm = read_frontmatter(text)
        title = str(fm.get("title", path.parent.name))

        nodes[node_id] = {
            "id": node_id,
            "label": title,
            "type": content_type,
            "slug": path.parent.name,
        }

        for target in extract_doc_links(path, text):
            result = classify(target)
            if result is None:
                continue
            target_id, _ = result
            if target_id == node_id:
                continue
            key = (node_id, target_id)
            if key not in seen_edges:
                seen_edges.add(key)
                edges.append({"source": node_id, "target": target_id})

    # Only include edges where both endpoints are known nodes
    known = set(nodes)
    edges = [e for e in edges if e["source"] in known and e["target"] in known]

    return list(nodes.values()), edges


# --------------------------------------------------------------------------- #
# HTML renderer
# --------------------------------------------------------------------------- #

def render_html(nodes: list, edges: list) -> str:
    data = json.dumps({"nodes": nodes, "edges": edges}, indent=2)
    colors = json.dumps(COLORS)
    type_labels = json.dumps({v: v for v in CONTENT_DIRS.values()})

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nucleus Docs — Relationship Graph</title>
<style>
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ height: 100%; background: #0f1117; color: #e2e8f0; font-family: system-ui, -apple-system, sans-serif; }}
  #wrap {{ display: flex; flex-direction: column; height: 100vh; }}
  #toolbar {{ flex-shrink: 0; display: flex; align-items: center; gap: 16px; padding: 10px 16px; background: #1a1d2e; border-bottom: 1px solid #252840; }}
  #toolbar h1 {{ font-size: 13px; font-weight: 600; color: #94a3b8; letter-spacing: .06em; text-transform: uppercase; white-space: nowrap; }}
  #legend {{ display: flex; gap: 14px; margin-left: auto; }}
  .leg {{ display: flex; align-items: center; gap: 6px; font-size: 12px; color: #94a3b8; cursor: pointer; user-select: none; }}
  .leg-dot {{ width: 10px; height: 10px; border-radius: 50%; flex-shrink: 0; }}
  .leg.dimmed {{ opacity: 0.35; }}
  #cy {{ flex: 1; }}
  #tip {{ position: fixed; background: #1a1d2e; border: 1px solid #2d3148; border-radius: 6px; padding: 8px 12px; font-size: 12px; pointer-events: none; display: none; z-index: 10; max-width: 240px; }}
  #tip-type {{ color: #64748b; font-size: 10px; text-transform: uppercase; letter-spacing: .07em; }}
  #tip-name {{ color: #f1f5f9; margin-top: 3px; font-weight: 500; line-height: 1.4; }}
  #tip-hint {{ color: #64748b; font-size: 10px; margin-top: 4px; }}
</style>
</head>
<body>
<div id="wrap">
  <div id="toolbar">
    <h1>Nucleus Distribution — Docs Graph</h1>
    <div id="legend"></div>
  </div>
  <div id="cy"></div>
</div>
<div id="tip">
  <div id="tip-type"></div>
  <div id="tip-name"></div>
  <div id="tip-hint"></div>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.30.2/cytoscape.min.js"></script>
<script>
const GRAPH  = {data};
const COLORS = {colors};

// --- legend ---
const legendEl = document.getElementById('legend');
const hidden = {{}};
Object.entries(COLORS).forEach(([type, color]) => {{
  const el = document.createElement('div');
  el.className = 'leg';
  el.dataset.type = type;
  el.innerHTML = `<div class="leg-dot" style="background:${{color}}"></div>${{type}}`;
  el.addEventListener('click', () => {{
    hidden[type] = !hidden[type];
    el.classList.toggle('dimmed', hidden[type]);
    cy.nodes(`[type="${{type}}"]`).toggleClass('hidden', !!hidden[type]);
  }});
  legendEl.appendChild(el);
}});

// --- cytoscape ---
const cy = cytoscape({{
  container: document.getElementById('cy'),
  elements: [
    ...GRAPH.nodes.map(n => ({{ data: n }})),
    ...GRAPH.edges.map(e => ({{ data: e }})),
  ],
  style: [
    {{
      selector: 'node',
      style: {{
        'background-color': ele => COLORS[ele.data('type')] || '#888',
        'label': 'data(label)',
        'color': '#cbd5e1',
        'font-size': ele => Math.max(9, 8 + ele.degree() * 0.6) + 'px',
        'text-valign': 'bottom',
        'text-halign': 'center',
        'text-margin-y': 6,
        'text-outline-width': 2,
        'text-outline-color': '#0f1117',
        'width': ele => Math.max(14, 8 + ele.degree() * 5),
        'height': ele => Math.max(14, 8 + ele.degree() * 5),
        'transition-property': 'opacity',
        'transition-duration': '150ms',
      }},
    }},
    {{
      selector: 'node:selected',
      style: {{ 'border-width': 2.5, 'border-color': '#f8fafc' }},
    }},
    {{
      selector: 'node.hidden',
      style: {{ 'opacity': 0, 'events': 'no' }},
    }},
    {{
      selector: 'edge',
      style: {{
        'width': 1.2,
        'line-color': '#2d3148',
        'target-arrow-color': '#2d3148',
        'target-arrow-shape': 'triangle',
        'curve-style': 'bezier',
        'opacity': 0.65,
        'transition-property': 'opacity, line-color, target-arrow-color',
        'transition-duration': '150ms',
      }},
    }},
    {{
      selector: 'edge.highlighted',
      style: {{
        'line-color': '#94a3b8',
        'target-arrow-color': '#94a3b8',
        'opacity': 1,
      }},
    }},
    {{
      selector: 'edge.faded',
      style: {{ 'opacity': 0.08 }},
    }},
  ],
  layout: {{
    name: 'breadthfirst',
    directed: true,
    padding: 48,
    spacingFactor: 1.8,
    avoidOverlap: true,
  }},
  minZoom: 0.3,
  maxZoom: 3,
}});

// --- tooltip ---
const tip = document.getElementById('tip');
const tipType = document.getElementById('tip-type');
const tipName = document.getElementById('tip-name');
const tipHint = document.getElementById('tip-hint');

cy.on('mouseover', 'node', e => {{
  const n = e.target;
  tipType.textContent = n.data('type');
  tipName.textContent = n.data('label');
  tipHint.textContent = 'click to highlight connections';
  tip.style.display = 'block';
}});
cy.on('mousemove', e => {{
  tip.style.left = (e.originalEvent.clientX + 14) + 'px';
  tip.style.top  = (e.originalEvent.clientY + 14) + 'px';
}});
cy.on('mouseout', 'node', () => {{ tip.style.display = 'none'; }});

// --- click to highlight neighbourhood ---
cy.on('tap', 'node', e => {{
  const n = e.target;
  const hood = n.closedNeighborhood();
  cy.elements().not(hood).addClass('faded').removeClass('highlighted');
  hood.edges().addClass('highlighted').removeClass('faded');
  n.removeClass('faded');
}});
cy.on('tap', e => {{
  if (e.target === cy) {{
    cy.elements().removeClass('faded highlighted');
  }}
}});
</script>
</body>
</html>"""


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main():
    nodes, edges = build_graph()
    if not nodes:
        print("warning: no nodes found — check DOCS_ROOT", file=sys.stderr)
    html = render_html(nodes, edges)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(REPO_ROOT)}  ({len(nodes)} nodes, {len(edges)} edges)")


if __name__ == "__main__":
    main()
