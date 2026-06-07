---
title: Materials Reference
---

# Overview

This page is a single, distribution-wide index of all materials referenced in this Distribution. Use it when authoring or reviewing a contribution to reuse an existing part number and vendor rather than introducing a near-duplicate.

::::::{note} Note: this table is automatically generated.
:class: dropdown
:icon: false

The table below is generated from `bom-<process>` tables on the Process pages by `scripts/build-materials-reference.py`. It is rebuilt at every deploy and is never committed, so it cannot drift from the source pages (the same single-source-of-truth model as the lab-ready protocol PDFs — see the lab-ready pipeline notes in `CLAUDE.md`). To regenerate it locally, run `python3 scripts/build-materials-reference.py` before `jupyter book start` or `myst build`. To add or correct an entry, edit the Materials in the appropriate Process page, not this page.
::::::

<!-- The included file lives in the gitignored guides/generated/ dir and is
     produced by scripts/build-materials-reference.py. Run that script before
     building locally, or the include below will be missing. -->

:::{include} ./generated/materials-reference-table.md
:::
