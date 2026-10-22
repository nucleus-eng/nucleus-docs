---
title: Documentation Graph
site:
    hide-toc: true
---

# Documentation Graph

An interactive map of how modules, processes, and implementations relate to one another in the Distribution. Nodes are colored by type: **modules** (blue), **processes** (green), **implementations** (orange). A dashed node marks content that is planned but not yet written, sourced from open GitHub issues.

**Click a node** to highlight its immediate connections and open its detail panel. **Click the background** to reset. **Click a legend label** to show or hide that node type.

To regenerate after adding or editing pages: `python3 scripts/build-graph.py`

[Open the interactive graph ↗](graph-data.html)
