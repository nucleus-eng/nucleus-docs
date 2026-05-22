# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## About this repository

Documentation for the [Nucleus Distribution](https://docs.nucleus.engineering) — a knowledge base of validated protocols and modular components for developing synthetic cells. Built with [MyST MD](https://mystmd.org/) (Jupyter Book).

## Development commands

**Setup (first time):**
```bash
./setup.sh               # Creates the nucleus-docs conda environment
conda activate nucleus-docs
```

**Local dev server** (live reload on `.md` and `.ipynb` changes):
```bash
jupyter book start
```

**Build HTML** (mirrors what CI does):
```bash
myst build --html
```

CI runs on pushes to `main` via `.github/workflows/deploy.yml`, installing `mystmd` via npm and deploying to GitHub Pages.

## Architecture

### Content model

The documentation organizes content into three parallel hierarchies under `docs/`:

- **`docs/processes/`** — Step-by-step lab protocols. Each process lives in its own subdirectory with a `main.md` (or a named `*-main.md` for parent pages). Sub-protocols nest as children.
- **`docs/modules/`** — Modular components that extend base cytosol functionality. Each module has a `spec.md` describing its design, compatible processes, and usage.
- **`docs/implementations/`** — Documented combinations of modules and processes that demonstrate a complete system behavior.

**File placement rules.** All content files — `.md`, images, `.csv` resources — must live inside one of these three subdirectories. Never create content files or directories at the repo root or anywhere outside `docs/`.

| Content type | Correct location |
| --- | --- |
| New module | `docs/modules/<module-name>/` |
| New process | `docs/processes/<process-name>/` |
| New implementation | `docs/implementations/<implementation-name>/` |
| Process sub-resources (BOMs, images) | `docs/processes/<process-name>/resources/` |
| Module images | `docs/modules/<module-name>/` |

**Before creating or moving any file**, verify the target path matches this structure. If a file is about to land outside `docs/`, stop and flag it to the developer before proceeding.

### Table of contents management

The site TOC is defined entirely in `myst.yml`. When adding a new page, you must add it to the `toc:` section. Child pages that should not appear directly in the sidebar use `hidden: true`. The file `site.yml` holds site-wide settings (license, nav links, theme) that `myst.yml` extends.

### Templates

`templates/` contains Cookiecutter-style starter files:
- `process-template/process-make_template.md` — full example of a process page including admonition blocks, protocol steps with checkboxes, and a Downloads section
- `module-template/spec.md` — module spec structure with schematic, designs table, compatible processes, and usage references
- `implementation-template/implementation-template.md` — combined implementation format

### MyST syntax conventions

Pages use MyST admonition nesting with `:::` fences. Process pages follow a consistent structure:
1. Frontmatter (`title:`)
2. `# Overview` with an `:::::::{card}` block containing nested dropdowns for Notes, Prerequisites, Hazardous Materials, Critical Materials, Genetically Encoded Components, Composition, and References
3. `# Protocol` with `##` subsections and checklist steps (`- [ ]`)
4. `# Downloads` grid with cards linking to PDF lab protocol and Bill of Materials

Protocol steps use `- [ ]` checkboxes and `:::{hint}` dropdowns for extended notes. Cross-references use MyST `{ref}` syntax for same-page targets and standard markdown links for cross-page references.

### Overview card dropdowns — empty dropdown policy

The template includes all possible dropdown sections as a starting point. **When authoring or reviewing a process page, only keep dropdowns that have real content.** Delete any dropdown whose only content is `- None`.

**When editing or reviewing a process page**, scan for empty dropdowns matching this pattern and flag them:

```
::::::{<type>} <Section Title>
:class: dropdown
:icon: false

- None

::::::
```

If you find one, flag it and ask the developer: **"The `<Section Title>` dropdown is empty — should it be deleted, or does it need content?"** Wait for confirmation before making any changes. Do not silently leave `- None` placeholders in committed files, but also do not silently delete them. The template file (`templates/process-template/process-make_template.md`) is the only file exempt from this rule.

**If all dropdowns in the Important Information card are removed**, the containing card block should also be removed:

```
:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

:::::::
```

Again, confirm with the developer before deleting the card.

### Notion migration gotchas

When migrating content from Notion markdown exports:

- **Table indentation**: Notion exports often produce tables with inconsistent indentation — the header row at 0 spaces and subsequent rows (including the separator) at 2 spaces, or all rows at 2 spaces. MyST requires all rows to be at the same indentation level. The correct pattern is **0 indentation throughout** (no leading spaces on any row), even when the table follows a `- [ ]` list item. Do not indent tables to nest them under list items — it breaks rendering.
- **Materials/consumables lists**: Large materials tables should be kept as inline markdown tables. A copy can be maintained as `resources/materials.csv` for download purposes, but mystmd does not support the `{csv-table}` `:file:` option for rendering external CSVs — the table must be inlined in the `.md` file.
- **Notion `<aside>` blocks**: Convert to the appropriate MyST admonition or section header depending on context (e.g., "Getting Started" asides → Overview prose, "Step X" asides → `##` section headers, "Resources" asides → `# References`).
- **Notion toggles**: Convert to `:::{hint} Note: <title>` with `:class: dropdown`.
- **Units in table column headers**: Use parentheses, not brackets (e.g., `MW (g/mol)` not `MW [g/mol]`).

### External references

`myst.yml` maintains a `references:` map of named keys (e.g., `devnote-01:`) pointing to external DevNote URLs. These can be cited throughout the docs without repeating URLs.

### Prose linting (Vale)

Run Vale to check docs for style violations:

```bash
vale docs/          # lint all docs
vale <file.md>      # lint a single file
```

Vale rules live in `styles/nucleus/`. Current rules enforce temperature unit formatting (`°C`).

**Interpreting `nucleus.degrees-symbol` errors.** This rule flags patterns like `37C` or `4 C` that are missing the degree symbol. However, it cannot distinguish temperatures from alphanumeric labels, so it produces false positives. When Vale flags a `nucleus.degrees-symbol` error, check the surrounding context:

- **Real error** — the token is a temperature value. Fix it by adding the degree symbol (e.g., `37C` → `37°C`, `4 C` → `4°C`).
  - Signals: preceded by "at", "to", "of", or a verb like "incubate", "store", "heat"; followed by "for X minutes/hours"; in a reaction table or thermocycler step.
  - **Table cells**: a bare value (e.g., `37C`) in a table column whose header indicates temperature (e.g., "Temperature", "Incubation temp", "Storage") is always a real error, even without surrounding signal words.
- **False positive** — the token is a label, not a temperature. Leave it alone.
  - Signals: preceded by "Figure", "Fig.", "Step", "Lane", "Panel", "Tube", "Option", or a similar structural label word.

Do not add Vale inline suppression comments (`<!-- vale off -->`) without confirming with the developer first.

### Pull request workflow

When merging a PR via `gh pr merge`, never use `--admin` to bypass branch protection rules. If a merge fails due to branch policy, stop and ask the developer how to proceed — options are leaving the PR open for a reviewer, asking the developer to approve it themselves, or using `--auto` to merge once requirements are met.
