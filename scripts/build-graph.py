#!/usr/bin/env python3
"""
build-graph.py — generate docs/graph-data.html, an interactive Cytoscape.js
graph of module / process / implementation relationships in the Nucleus
Distribution, plus "ghost" nodes for content that is planned but not yet
written (sourced from GitHub issues labeled new-module / new-process).

Usage:
    python3 scripts/build-graph.py
    python3 scripts/build-graph.py --no-ghosts      # skip the GitHub issue lookup

Output: docs/graph-data.html  (self-contained; commit or gitignore as preferred)
"""

import argparse
import json
import re
import subprocess
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
GITHUB_REPO = "nucleus-eng/nucleus-docs"
GHOST_LABELS = {"new-module": "module", "new-process": "process", "new-implementation": "implementation"}

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

DEVNOTE_DOI_RE = re.compile(r"https://doi\.org/(10\.63765/[A-Za-z0-9]+)")
VALIDATION_ROW_RE = re.compile(r"\[([^\]]+)\]\(([^)]+\.md)\)\s*\|\s*(★+)")


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


def extract_devnote(text: str) -> str | None:
    """Return the first DevNote DOI link (doi.org/10.63765/...) found on a page, if any."""
    m = DEVNOTE_DOI_RE.search(text)
    return m.group(0) if m else None


def load_validation_map() -> dict[str, str]:
    """Map a module's docs/modules/<slug>/spec.md path to its star rating,
    read from the tables in docs/modules/modules-main.md."""
    index = DOCS_ROOT / "modules" / "modules-main.md"
    if not index.exists():
        return {}
    out: dict[str, str] = {}
    for m in VALIDATION_ROW_RE.finditer(index.read_text(encoding="utf-8")):
        _label, href, stars = m.groups()
        target = resolve_href(index, href)
        if target is None:
            continue
        classified = classify(target)
        if classified is not None:
            out[classified[0]] = stars
    return out


def fetch_ghost_nodes() -> list[dict]:
    """Build 'planned' nodes for content that doesn't exist in docs/ yet.

    Real source: open GitHub issues labeled new-module / new-process /
    new-implementation. If the repo has no issues under those labels yet
    (true today), fall back to a couple of illustrative examples so the
    rendering can be reviewed — each one is flagged example: true so the
    page can say plainly that it is not live data.
    """
    nodes: list[dict] = []
    try:
        raw = subprocess.run(
            ["gh", "issue", "list", "--repo", GITHUB_REPO, "--state", "open",
             "--label", ",".join(GHOST_LABELS), "--json", "number,title,url,labels,body",
             "--limit", "100"],
            capture_output=True, text=True, timeout=20, check=True,
        ).stdout
        issues = json.loads(raw)
    except (subprocess.SubprocessError, OSError, json.JSONDecodeError, FileNotFoundError) as exc:
        print(f"warning: could not query GitHub issues for ghost nodes ({exc})", file=sys.stderr)
        issues = []

    for issue in issues:
        labels = {l["name"] for l in issue.get("labels", [])}
        content_type = next((GHOST_LABELS[l] for l in labels if l in GHOST_LABELS), "module")
        nodes.append({
            "id": f"ghost/issue-{issue['number']}",
            "label": issue["title"],
            "type": content_type,
            "slug": f"issue-{issue['number']}",
            "planned": True,
            "example": False,
            "devnote": extract_devnote(issue.get("body") or ""),
            "issues": 1,
            "issue_url": issue["url"],
            "validation": None,
        })

    if not nodes:
        print(
            "note: no open issues labeled "
            f"{'/'.join(GHOST_LABELS)} — showing illustrative example ghost nodes instead",
            file=sys.stderr,
        )
        nodes = [
            {
                "id": "ghost/example-atp-regen", "label": "ATP regen", "type": "module",
                "slug": "example-atp-regen", "planned": True, "example": True,
                "devnote": None, "issues": 3, "issue_url": None, "validation": None,
            },
            {
                "id": "ghost/example-new-pore", "label": "New pore", "type": "module",
                "slug": "example-new-pore", "planned": True, "example": True,
                "devnote": None, "issues": 1, "issue_url": None, "validation": None,
            },
        ]
    return nodes


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


def build_graph(include_ghosts: bool = True):
    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    seen_edges: set[tuple] = set()
    validation = load_validation_map()

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
            "planned": False,
            "example": False,
            "devnote": extract_devnote(text),
            "validation": validation.get(node_id),
            "issues": 0,
            "issue_url": None,
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

    if include_ghosts:
        for ghost in fetch_ghost_nodes():
            nodes[ghost["id"]] = ghost

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
  .leg-dot.planned {{ background: transparent; border: 1.5px dashed #94a3b8; }}
  #panel {{ position: fixed; top: 54px; right: 0; bottom: 0; width: 260px; background: #171a2b; border-left: 1px solid #252840; padding: 16px; display: none; overflow-y: auto; z-index: 9; }}
  #panel.open {{ display: block; }}
  #panel .close {{ position: absolute; top: 10px; right: 12px; cursor: pointer; color: #64748b; font-size: 16px; background: none; border: none; }}
  #panel .kind {{ color: #64748b; font-size: 10px; text-transform: uppercase; letter-spacing: .07em; }}
  #panel .name {{ color: #f1f5f9; font-size: 15px; font-weight: 500; margin-top: 4px; }}
  #panel .example-tag {{ display: inline-block; margin-top: 6px; font-size: 10px; color: #0f1117; background: #facc15; padding: 1px 6px; border-radius: 4px; }}
  #panel .rows {{ margin-top: 16px; border-top: 1px solid #252840; padding-top: 12px; }}
  #panel .row {{ display: flex; justify-content: space-between; font-size: 12px; padding: 5px 0; color: #94a3b8; }}
  #panel .row span:last-child {{ color: #e2e8f0; text-align: right; }}
  #panel a {{ color: #7dd3fc; text-decoration: none; }}
  #panel .issue-badge {{ background: #3b2f12; color: #facc15; padding: 1px 7px; border-radius: 10px; font-size: 11px; }}
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
<div id="panel">
  <button class="close" onclick="closePanel()">&times;</button>
  <div class="kind" id="panel-type"></div>
  <div class="name" id="panel-name"></div>
  <div id="panel-example"></div>
  <div class="rows">
    <div class="row"><span>Validation</span><span id="panel-validation"></span></div>
    <div class="row"><span>DevNote</span><span id="panel-devnote"></span></div>
    <div class="row"><span>Open issues</span><span id="panel-issues"></span></div>
  </div>
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
{{
  const el = document.createElement('div');
  el.className = 'leg';
  el.innerHTML = `<div class="leg-dot planned"></div>planned (DevNote)`;
  el.addEventListener('click', () => {{
    hidden['planned'] = !hidden['planned'];
    el.classList.toggle('dimmed', hidden['planned']);
    cy.nodes('[?planned]').toggleClass('hidden', !!hidden['planned']);
  }});
  legendEl.appendChild(el);
}}

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
        'background-opacity': ele => ele.data('planned') ? 0.12 : 1,
        'border-style': ele => ele.data('planned') ? 'dashed' : 'solid',
        'border-width': ele => ele.data('planned') ? 1.5 : 0,
        'border-color': ele => COLORS[ele.data('type')] || '#888',
        'label': ele => ele.data('label') + (ele.data('issues') ? ` (${{ele.data('issues')}})` : ''),
        'color': ele => ele.data('planned') ? '#94a3b8' : '#cbd5e1',
        'font-style': ele => ele.data('planned') ? 'italic' : 'normal',
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

// --- click to highlight neighbourhood + open detail panel ---
const panel = document.getElementById('panel');
function closePanel() {{ panel.classList.remove('open'); }}

cy.on('tap', 'node', e => {{
  const n = e.target;
  const hood = n.closedNeighborhood();
  cy.elements().not(hood).addClass('faded').removeClass('highlighted');
  hood.edges().addClass('highlighted').removeClass('faded');
  n.removeClass('faded');

  document.getElementById('panel-type').textContent = n.data('type') + (n.data('planned') ? ' · planned' : '');
  document.getElementById('panel-name').textContent = n.data('label');
  document.getElementById('panel-example').innerHTML = n.data('example')
    ? '<span class="example-tag">example — no issue label exists yet</span>' : '';
  document.getElementById('panel-validation').textContent = n.data('validation') || '—';
  const devnote = n.data('devnote');
  document.getElementById('panel-devnote').innerHTML = devnote
    ? `<a href="${{devnote}}" target="_blank" rel="noopener">view ↗</a>` : '—';
  const issues = n.data('issues') || 0;
  const issueUrl = n.data('issue_url');
  document.getElementById('panel-issues').innerHTML = issues
    ? (issueUrl ? `<a class="issue-badge" href="${{issueUrl}}" target="_blank" rel="noopener">${{issues}}</a>`
                : `<span class="issue-badge">${{issues}}</span>`)
    : '0';
  panel.classList.add('open');
}});
cy.on('tap', e => {{
  if (e.target === cy) {{
    cy.elements().removeClass('faded highlighted');
    closePanel();
  }}
}});
</script>
</body>
</html>"""


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-ghosts", action="store_true",
                         help="skip the GitHub issue lookup for planned/ghost nodes")
    args = parser.parse_args()

    nodes, edges = build_graph(include_ghosts=not args.no_ghosts)
    if not nodes:
        print("warning: no nodes found — check DOCS_ROOT", file=sys.stderr)
    html = render_html(nodes, edges)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(html, encoding="utf-8")
    ghosts = sum(1 for n in nodes if n.get("planned"))
    print(f"wrote {OUTPUT.relative_to(REPO_ROOT)}  ({len(nodes)} nodes, {ghosts} planned, {len(edges)} edges)")


if __name__ == "__main__":
    main()
