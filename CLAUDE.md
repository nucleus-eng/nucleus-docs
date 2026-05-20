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

### External references

`myst.yml` maintains a `references:` map of named keys (e.g., `devnote-01:`) pointing to external DevNote URLs. These can be cited throughout the docs without repeating URLs.
