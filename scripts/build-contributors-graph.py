#!/usr/bin/env python3
"""
build-contributors-graph.py — generate about/contributors-graph-data.html, an
interactive Cytoscape.js graph of contributor -> DevNote -> Module/Process/
Implementation relationships.

The graph's spine is DevNote authorship, the one hard data link between a
name on about/contributors.md and a DevNote on the Curvenote SCMS API (see
build-devnote-cards.py and build-devnote-counts.py, which query the same
API for the same kind of data). A contributor node appears only if their
name matches a DevNote author's name exactly (case-insensitive, whole
string) — no fuzzy matching, to avoid drawing a false edge on a public
page. This means someone listed in contributors.md for other kinds of
contribution (review, lab work not yet written up as a DevNote, tooling)
will not appear here; the graph is a view of DevNote-linked contribution,
not a replacement for the full list above it.

A DevNote's edges onward to the Module/Process/Implementation pages it
supports reuse scripts/devnote-associations.yml — the same manually
reviewed mapping build-devnote-cards.py renders as each page's
"# Supported by" section. Only DevNotes matched to a contributor get this
second hop, so the graph stays a connected contributor -> output picture
rather than the full module/process/implementation map (that's
docs/graph.md's job, on the unmerged feat/graph-devnotes branch).

Not wired into CI (this repo does not make outbound network calls during
the build — see build-devnote-cards.py's docstring): run locally and
commit the result, same as that script and build-devnote-highlights.py.

Usage:
    python3 scripts/build-contributors-graph.py
"""

import json
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: pyyaml required — pip install pyyaml", file=sys.stderr)
    sys.exit(1)

SCMS_BASE = "https://scms.curvenote.com/v1/sites/bnext-devnotes"
FETCH_LIMIT = 500
TIMEOUT = 20

REPO_ROOT = Path(__file__).parent.parent.resolve()
DOCS_ROOT = REPO_ROOT / "docs"
CONTRIBUTORS_MD = REPO_ROOT / "about" / "contributors.md"
ASSOCIATIONS_FILE = Path(__file__).parent / "devnote-associations.yml"
OUTPUT = REPO_ROOT / "about" / "contributors-graph-data.html"

CONTENT_TYPES = {"modules": "modules", "processes": "processes", "implementations": "implementations"}
PAGE_CANDIDATES = {"modules": ["spec.md"], "processes": ["main.md"], "implementations": ["main.md"]}

# Nucleus Graph Style Guide palette (surface tokens + categorical palette),
# assigned to our 5 fixed node types rather than hashed, since the type set
# is small and fixed. Accent green goes to "contributor" (the guide uses it
# for a person/core node); the rest are distinct categorical-palette hues.
COLORS = {
    "contributor": "#006837",
    "devnote": "#6a3d9a",
    "modules": "#1f78b4",
    "processes": "#b15928",
    "implementations": "#ff7f00",
}
SURFACE = {
    "bg": "#ffffff",
    "panel": "#f2f6f1",
    "ink": "#11271c",
    "accent": "#006837",
    "text": "#26302a",
    "muted": "#4b564e",
    "faint": "#6e7a71",
    "divider": "#c9d3c9",
}

CONTRIBUTOR_LINE_RE = re.compile(r"^-\s+([^—]+?)\s+—")
WORD_RE = re.compile(r"[A-Za-z]+")


def initials(label: str, node_type: str) -> str:
    if node_type == "contributor":
        parts = label.split()
        if len(parts) >= 2:
            return (parts[0][0] + parts[-1][0]).upper()
        return (parts[0][:2] if parts else "?").upper()
    words = WORD_RE.findall(label)
    if len(words) >= 2:
        return (words[0][0] + words[1][0]).upper()
    return (words[0][:2] if words else "?").upper()


def get_json(url: str):
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
        return json.loads(resp.read())


def load_contributors() -> dict[str, str]:
    """lowercased full name -> canonical-cased full name, from the bullet
    list in about/contributors.md."""
    names: dict[str, str] = {}
    for line in CONTRIBUTORS_MD.read_text(encoding="utf-8").splitlines():
        m = CONTRIBUTOR_LINE_RE.match(line)
        if m:
            name = m.group(1).strip()
            names[name.lower()] = name
    return names


def sanitize_key(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.~:@+-]", "-", value)


def fetch_works() -> list[dict]:
    try:
        return get_json(f"{SCMS_BASE}/works?limit={FETCH_LIMIT}")["items"]
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
        print(f"error: could not query the Curvenote API ({exc})", file=sys.stderr)
        sys.exit(1)


def load_associations() -> dict:
    if not ASSOCIATIONS_FILE.exists():
        return {}
    data = yaml.safe_load(ASSOCIATIONS_FILE.read_text(encoding="utf-8")) or {}
    return {k: v for k, v in data.items() if k != "exclude"}


def content_title(content_type: str, slug: str) -> str:
    base = DOCS_ROOT / content_type / slug
    for filename in PAGE_CANDIDATES[content_type]:
        page = base / filename
        if page.exists():
            fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n", page.read_text(encoding="utf-8"), re.DOTALL)
            if fm_match:
                try:
                    fm = yaml.safe_load(fm_match.group(1)) or {}
                except yaml.YAMLError:
                    fm = {}
                if fm.get("title"):
                    return str(fm["title"])
    return slug


def build_graph() -> tuple[list[dict], list[dict]]:
    contributors = load_contributors()
    works = fetch_works()
    associations = load_associations()

    nodes: dict[str, dict] = {}
    edges: list[dict] = []
    seen_edges: set[tuple] = set()

    def add_edge(source: str, target: str) -> None:
        key = (source, target)
        if key not in seen_edges:
            seen_edges.add(key)
            edges.append({"source": source, "target": target})

    # work id/sanitized-slug -> work, so an association key (whichever form
    # it used) resolves back to the work it was tagged against.
    work_by_key: dict[str, dict] = {}
    matched_devnote_ids: set[str] = set()

    for work in works:
        work_id = work["id"]
        for key in {work_id, sanitize_key(work.get("slug") or "")}:
            if key:
                work_by_key[key] = work

        author_names = [a.get("name") for a in (work.get("authors") or []) if a.get("name")]
        matched = [contributors[n.lower()] for n in author_names if n.lower() in contributors]
        if not matched:
            continue  # no contributor-page name matches this DevNote's authors

        matched_devnote_ids.add(work_id)
        devnote_node_id = f"devnote/{work_id}"
        devnote_title = work.get("title", "Untitled")
        nodes[devnote_node_id] = {
            "id": devnote_node_id,
            "label": devnote_title,
            "type": "devnote",
            "url": (work.get("links") or {}).get("html"),
            "initials": initials(devnote_title, "devnote"),
        }
        for name in matched:
            contributor_node_id = f"contributor/{sanitize_key(name)}"
            nodes[contributor_node_id] = {
                "id": contributor_node_id, "label": name, "type": "contributor", "url": None,
                "initials": initials(name, "contributor"),
            }
            add_edge(contributor_node_id, devnote_node_id)

    for key, entry in associations.items():
        if not entry:
            continue
        work = work_by_key.get(key)
        if work is None or work["id"] not in matched_devnote_ids:
            continue
        devnote_node_id = f"devnote/{work['id']}"
        for content_type in CONTENT_TYPES:
            for slug in entry.get(content_type) or []:
                content_node_id = f"{content_type}/{slug}"
                title = content_title(content_type, slug)
                nodes[content_node_id] = {
                    "id": content_node_id,
                    "label": title,
                    "type": content_type,
                    "url": None,
                    "initials": initials(title, content_type),
                }
                add_edge(devnote_node_id, content_node_id)

    return list(nodes.values()), edges


def render_html(nodes: list, edges: list) -> str:
    data = json.dumps({"nodes": nodes, "edges": edges}, indent=2)
    colors = json.dumps(COLORS)
    surface = json.dumps(SURFACE)
    labels = json.dumps({
        "contributor": "Contributor", "devnote": "DevNote", "modules": "Module",
        "processes": "Process", "implementations": "Implementation",
    })

    # Tokens and rules ported from the Nucleus Graph Style Guide (surface
    # colors, node/edge geometry, rail/stage/panel layout). The guide's
    # status-traffic-light and metric-gradient modes don't apply here (no
    # tracking state or weighted metric on these nodes), so only the
    # categorical palette and the fixed-case rules carry over.
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Nucleus Docs — Contributors Graph</title>
<style>
  :root {{
    --bg: {SURFACE['bg']}; --panel: {SURFACE['panel']}; --ink: {SURFACE['ink']};
    --accent: {SURFACE['accent']}; --text: {SURFACE['text']}; --muted: {SURFACE['muted']};
    --faint: {SURFACE['faint']}; --divider: {SURFACE['divider']};
    --sans: system-ui, -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  }}
  * {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html, body {{ height: 100%; background: var(--bg); color: var(--text); font-family: var(--sans); }}
  #app {{ display: grid; grid-template-columns: 250px 1fr 0px; height: 100vh; transition: grid-template-columns 150ms; }}
  #app.panel-open {{ grid-template-columns: 250px 1fr 360px; }}

  #rail {{ border-right: 1px solid var(--divider); padding: 1rem; overflow-y: auto; }}
  #rail h1 {{ font-size: 1.05rem; font-weight: 700; color: var(--ink); margin-bottom: .2rem; }}
  #rail .subtitle {{ font-size: .78rem; color: var(--muted); margin-bottom: 1.4rem; }}
  .rail-label {{ font-size: .74rem; text-transform: uppercase; letter-spacing: .035em; color: var(--muted); font-weight: 600; margin: 1.1rem 0 .5rem; }}
  .rail-label:first-of-type {{ margin-top: 0; }}
  .legend-row {{ display: flex; align-items: center; gap: .55rem; padding: .3rem 0; cursor: pointer; user-select: none; font-size: .86rem; }}
  .legend-row.dimmed {{ opacity: .35; }}
  .legend-dot {{ width: 12px; height: 12px; border-radius: 50%; flex: none; }}
  #rail p.help {{ font-size: .8rem; color: var(--muted); line-height: 1.5; }}
  #rail p.regen {{ font-size: .74rem; color: var(--faint); line-height: 1.5; }}
  #rail code {{ font: 500 .78em ui-monospace, SFMono-Regular, Menlo, Consolas, monospace; background: var(--panel); border-radius: 4px; padding: .1em .35em; }}

  #stage {{ position: relative; background: var(--bg); overflow: hidden; }}
  #cy {{ position: absolute; inset: 0; }}
  #label-layer {{ position: absolute; inset: 0; pointer-events: none; overflow: hidden; }}
  .node-name-label {{ position: absolute; transform: translate(-50%, 0); font-size: .76rem; color: var(--text); white-space: nowrap; font-weight: 500; }}
  .node-name-label.hover-label {{ font-weight: 600; }}

  #panel {{ border-left: 1px solid var(--divider); padding: 1rem; overflow-y: auto; position: relative; }}
  #app:not(.panel-open) #panel {{ padding: 0; border-left: none; }}
  #panel .close {{ position: absolute; top: .7rem; right: .8rem; background: none; border: none; color: var(--muted); font-size: 1.1rem; cursor: pointer; line-height: 1; }}
  #panel .kind {{ font-size: .74rem; text-transform: uppercase; letter-spacing: .035em; color: var(--muted); font-weight: 600; }}
  #panel .name {{ font-size: 1rem; font-weight: 700; color: var(--ink); margin: .35rem 0 1rem; line-height: 1.35; }}
  #panel a.open-link {{ display: inline-block; font-size: .86rem; font-weight: 600; color: var(--accent); text-decoration: none; }}
  #panel a.open-link:hover {{ text-decoration: underline; }}

  @media (max-width: 760px) {{
    #app {{ grid-template-columns: 1fr; grid-template-rows: auto 1fr 0px; height: 100vh; }}
    #app.panel-open {{ grid-template-columns: 1fr; grid-template-rows: auto 1fr 260px; }}
    #rail {{ border-right: none; border-bottom: 1px solid var(--divider); max-height: 40vh; }}
    #panel {{ border-left: none; border-top: 1px solid var(--divider); }}
  }}
</style>
</head>
<body>
<div id="app">
  <aside id="rail">
    <h1>Contributors Graph</h1>
    <div class="subtitle">Nucleus Distribution</div>
    <div class="rail-label">Node types</div>
    <div id="legend"></div>
    <div class="rail-label">How to use it</div>
    <p class="help">Click a node for details. Click the background to clear. Click a type below to show or hide it.</p>
    <div class="rail-label">Maintaining</div>
    <p class="regen">Regenerate after new DevNotes are published or <code>devnote-associations.yml</code> changes:<br><code>python3 scripts/build-contributors-graph.py</code></p>
  </aside>
  <main id="stage">
    <div id="cy"></div>
    <div id="label-layer"></div>
  </main>
  <aside id="panel">
    <button class="close" aria-label="Close">&times;</button>
    <div class="kind"></div>
    <div class="name"></div>
    <a class="open-link" target="_blank" rel="noopener" style="display:none;">Open DevNote ↗</a>
  </aside>
</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.30.2/cytoscape.min.js"></script>
<script>
const GRAPH = {data};
const COLORS = {colors};
const LABELS = {labels};
const SURFACE = {surface};
const LABEL_RADIUS_THRESHOLD = 20;

const app = document.getElementById('app');
const legendEl = document.getElementById('legend');
const hiddenTypes = {{}};
Object.keys(LABELS).forEach(type => {{
  const row = document.createElement('div');
  row.className = 'legend-row';
  row.innerHTML = `<div class="legend-dot" style="background:${{COLORS[type]}}"></div>${{LABELS[type]}}`;
  row.addEventListener('click', () => {{
    hiddenTypes[type] = !hiddenTypes[type];
    row.classList.toggle('dimmed', hiddenTypes[type]);
    cy.nodes(`[type="${{type}}"]`).toggleClass('hidden', !!hiddenTypes[type]);
    refreshPersistentLabels();
  }});
  legendEl.appendChild(row);
}});

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
        'shape': 'ellipse',
        'label': 'data(initials)',
        'color': '#ffffff',
        'font-weight': 600,
        'text-valign': 'center',
        'text-halign': 'center',
        'font-size': ele => Math.max(8, radius(ele) * 0.62) + 'px',
        'width': ele => radius(ele) * 2,
        'height': ele => radius(ele) * 2,
        'border-width': 0,
        'transition-property': 'opacity, border-width, border-color',
        'transition-duration': '120ms',
      }},
    }},
    {{ selector: 'node.hidden', style: {{ 'opacity': 0, 'events': 'no' }} }},
    {{ selector: 'node.dimmed', style: {{ 'opacity': 0.35 }} }},
    {{ selector: 'node.hovered', style: {{ 'border-width': 2.5, 'border-color': SURFACE.ink, 'border-opacity': 1 }} }},
    {{ selector: 'node.selected', style: {{ 'border-width': 2.5, 'border-color': SURFACE.accent, 'border-opacity': 1 }} }},
    {{
      selector: 'edge',
      style: {{
        'width': 1.5,
        'line-color': 'rgba(0,0,0,0.15)',
        'curve-style': 'bezier',
        'transition-property': 'line-color, width, opacity',
        'transition-duration': '120ms',
      }},
    }},
    {{ selector: 'edge.dimmed', style: {{ 'line-color': 'rgba(0,0,0,0.05)' }} }},
    {{ selector: 'edge.active', style: {{ 'line-color': SURFACE.accent, 'width': 2.5 }} }},
    {{ selector: '.hidden', style: {{ 'opacity': 0, 'events': 'no' }} }},
  ],
  layout: {{ name: 'cose', animate: false, padding: 40, nodeRepulsion: 9000, idealEdgeLength: 70 }},
  wheelSensitivity: 0.2,
}});

function radius(ele) {{
  return Math.max(10, Math.min(34, Math.sqrt(Math.max(ele.degree(), 1)) * 7));
}}

// ---- persistent name labels (above a size threshold), DOM-overlaid so the
// in-circle initials and the below-circle name can use different styles ----
const labelLayer = document.getElementById('label-layer');
const labelEls = new Map();

function ensureLabel(node) {{
  let div = labelEls.get(node.id());
  if (!div) {{
    div = document.createElement('div');
    div.className = 'node-name-label';
    div.textContent = node.data('label');
    labelLayer.appendChild(div);
    labelEls.set(node.id(), div);
  }}
  return div;
}}
function removeLabel(id) {{
  const div = labelEls.get(id);
  if (div) {{ div.remove(); labelEls.delete(id); }}
}}
function updateLabelPositions() {{
  labelEls.forEach((div, id) => {{
    const n = cy.getElementById(id);
    if (!n || n.empty() || n.hasClass('hidden')) {{ div.style.display = 'none'; return; }}
    div.style.display = '';
    const pos = n.renderedPosition();
    div.style.left = pos.x + 'px';
    div.style.top = (pos.y + n.renderedHeight() / 2 + 4) + 'px';
  }});
}}
function refreshPersistentLabels() {{
  cy.nodes().forEach(n => {{
    if (radius(n) >= LABEL_RADIUS_THRESHOLD && !n.hasClass('hidden')) ensureLabel(n);
    else if (!n.hasClass('hovered')) removeLabel(n.id());
  }});
  updateLabelPositions();
}}
cy.on('layoutstop', refreshPersistentLabels);
cy.on('pan zoom position drag', updateLabelPositions);

// ---- hover: dim everything not touching the hovered node, ink ring ----
cy.on('mouseover', 'node', evt => {{
  const n = evt.target;
  const neighborhood = n.closedNeighborhood();
  cy.elements().difference(neighborhood).addClass('dimmed');
  neighborhood.edges().addClass('active');
  n.addClass('hovered');
  ensureLabel(n).classList.add('hover-label');
  updateLabelPositions();
}});
cy.on('mouseout', 'node', evt => {{
  const n = evt.target;
  cy.elements().removeClass('dimmed active');
  n.removeClass('hovered');
  if (radius(n) < LABEL_RADIUS_THRESHOLD) removeLabel(n.id());
  else {{ const div = labelEls.get(n.id()); if (div) div.classList.remove('hover-label'); }}
}});

// ---- click: select a node, show its detail panel ----
const panelKind = document.querySelector('#panel .kind');
const panelName = document.querySelector('#panel .name');
const panelLink = document.querySelector('#panel a.open-link');

function selectNode(n) {{
  cy.nodes('.selected').removeClass('selected');
  n.addClass('selected');
  panelKind.textContent = LABELS[n.data('type')] || n.data('type');
  panelName.textContent = n.data('label');
  if (n.data('url')) {{
    panelLink.href = n.data('url');
    panelLink.textContent = n.data('type') === 'devnote' ? 'Open DevNote ↗' : 'Open ↗';
    panelLink.style.display = 'inline-block';
  }} else {{
    panelLink.style.display = 'none';
  }}
  app.classList.add('panel-open');
  afterLayoutChange();
}}
function closePanel() {{
  cy.nodes('.selected').removeClass('selected');
  app.classList.remove('panel-open');
  afterLayoutChange();
}}
function afterLayoutChange() {{
  // The rail/stage/panel grid just changed #cy's pixel size; cytoscape
  // only knows its canvas size when told, and CSS transitions it over
  // 150ms, so resize across a few frames rather than once immediately.
  const start = performance.now();
  function tick(now) {{
    cy.resize();
    if (now - start < 200) requestAnimationFrame(tick);
    else updateLabelPositions();
  }}
  requestAnimationFrame(tick);
}}
cy.on('tap', 'node', evt => selectNode(evt.target));
cy.on('tap', evt => {{ if (evt.target === cy) closePanel(); }});
document.querySelector('#panel .close').addEventListener('click', closePanel);
window.addEventListener('resize', () => {{ cy.resize(); updateLabelPositions(); }});
</script>
</body>
</html>
"""


def main() -> int:
    nodes, edges = build_graph()
    contributor_count = sum(1 for n in nodes if n["type"] == "contributor")
    devnote_count = sum(1 for n in nodes if n["type"] == "devnote")
    OUTPUT.write_text(render_html(nodes, edges), encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(REPO_ROOT)}: {contributor_count} contributor(s), "
          f"{devnote_count} DevNote(s), {len(nodes) - contributor_count - devnote_count} content page(s), "
          f"{len(edges)} edge(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
