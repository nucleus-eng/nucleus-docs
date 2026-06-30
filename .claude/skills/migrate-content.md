---
description: Convention checklist for migrating content into nucleus-docs from Notion markdown exports or Curvenote DevNotes.
---

### Notion migration gotchas

When migrating content from Notion markdown exports:

- **Table indentation**: Notion exports often produce tables with inconsistent indentation — the header row at 0 spaces and subsequent rows (including the separator) at 2 spaces, or all rows at 2 spaces. MyST requires all rows to be at the same indentation level. The correct pattern is **0 indentation throughout** (no leading spaces on any row), even when the table follows a `- [ ]` list item. Do not indent tables to nest them under list items — it breaks rendering.
- **Materials/consumables lists**: For a BOM rendered on the page, keep it as an inline markdown table labeled `bom-<slug>` (mystmd does not support the `{csv-table}` `:file:` option for rendering external CSVs — the table must be inlined); the lab-ready pipeline generates `<slug>-materials.csv` from it. A contributor may alternatively upload the BOM as `resources/<slug>-bom.csv` (the pipeline ingests it the same way) — but do **not** hand-maintain a generic `resources/materials.csv` copy alongside an inline table, and if both a `bom-<slug>` table and `resources/<slug>-bom.csv` exist they must agree (CI enforces it). See the lab-ready protocol pipeline section below.
- **Notion `<aside>` blocks**: Convert to the appropriate MyST admonition or section header depending on context (e.g., "Getting Started" asides → Overview prose, "Step X" asides → `##` section headers, "Resources" asides → `# References`).
- **Notion toggles**: Convert to `:::{hint} Note: <title>` with `:class: dropdown`.
- **Units in table column headers**: Use parentheses, not brackets (e.g., `MW (g/mol)` not `MW [g/mol]`).
- **Data discrepancies (including concentrations)**: Source content sometimes carries internally inconsistent or unverified values — a value in the body text that conflicts with a figure caption, or a stock concentration that does not match the stated final concentration. Do not silently correct or copy these — add a `:::{warning}` block adjacent to the affected content that names the specific discrepancy, shows the conflicting values, states the most likely interpretation, and instructs the reviewer to verify before bench use. For reaction tables specifically, verify that `stock concentration × volume / total volume = stated final concentration` for every reagent row, and flag any row that fails.
- **Scope boundary — spec vs. process**: Protocol steps, materials tables, and imaging conditions from a DevNote belong in a future Process page, not the module spec. The spec covers what the module is, its genetic designs, and expected performance. If protocol-level content appears in the DevNote, note it with a `<!-- TODO: move to process page -->` comment rather than migrating it into the spec.
- **DevNote figures — use static PNGs with `:name:` labels**: Computed figures (e.g. from Jupyter notebook outputs or `lorem.mjs`) cannot be copied as static images and cannot be cross-referenced from nucleus-docs. Key result figures in a module spec should be static PNG files with explicit `:name: fig:something` labels in `main.md`. Only figures with `:name:` labels are reachable via `xref:<devnote-key>#fig:something` in spec pages.
- **Bare DOI citations from Curvenote**: Curvenote DevNotes use `[](10.xxxx/xxxxx)` as a shorthand DOI citation. This resolves as a local file path in the nucleus-docs MyST build and causes a link-checker error. Always replace with a full markdown link on migration: `[Author et al., year](https://doi.org/10.xxxx/xxxxx)`. Check for bare `[](` patterns with `grep -n '\[\](' <file>` before committing a migrated spec.

### DevNote migration

**Read `curvenote.yml` first.** `curvenote.yml` is the single best starting point for a DevNote migration. It contains the DOI, project ID, author list (with ORCIDs and affiliations), figure sources, and download files. Read it before `main.md` to orient to the content.
