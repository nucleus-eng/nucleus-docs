---
title: Materials Reference
---

# Overview

This page is a single, distribution-wide index of every material catalogued in a process Bill of Materials anywhere in the Distribution — its product, vendor, part number, price, storage conditions, and the processes that use it. Use it when authoring or reviewing a contribution to reuse an existing part number and vendor rather than introducing a near-duplicate, and to check pricing and storage at a glance across processes.

The table below is **generated** from the `bom-<process>` tables on the process pages by `scripts/build-materials-reference.py`; it is rebuilt at every deploy and is never committed, so it cannot drift from the source pages (the same single-source-of-truth model as the lab-ready protocol PDFs — see the lab-ready pipeline notes in `CLAUDE.md`). To regenerate it locally, run `python3 scripts/build-materials-reference.py` before `jupyter book start` or `myst build`. To add or correct an entry, edit the material's row on its process page, not this page.

<!-- The included file lives in the gitignored guides/generated/ dir and is
     produced by scripts/build-materials-reference.py. Run that script before
     building locally, or the include below will be missing. -->

:::{include} ./generated/materials-reference-table.md
:::
