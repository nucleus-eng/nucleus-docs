---
title: Documentation Graph
site:
    hide-toc: true
---

# Documentation Graph

An interactive map of how modules, processes, and implementations relate to one another in the Distribution. Nodes are colored by type: **modules** (blue), **processes** (green), **implementations** (orange). Edges follow the direction of cross-links in the source pages.

**Click a node** to highlight its immediate connections. **Click the background** to reset. **Click a legend label** to show or hide that node type.

To regenerate after adding or editing pages: `python3 scripts/build-graph.py`

:::{raw} html
<iframe src="graph-data.html"
        style="width:100%; height:78vh; border:none; border-radius:4px; display:block;"
        title="Nucleus Distribution documentation relationship graph">
</iframe>
:::
