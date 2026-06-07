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

**Generate lab-ready protocol PDFs / BOMs** (requires `myst` + `typst` on PATH):
```bash
python3 scripts/build-protocols.py            # all processes
python3 scripts/build-protocols.py <dir>      # one process
python3 scripts/build-protocols.py --extract-only   # skip PDF rendering
```

CI runs on pushes to `main` via `.github/workflows/deploy.yml`, installing `mystmd` via npm and deploying to GitHub Pages.

**QA checks** (run locally before opening a PR):
```bash
python3 scripts/check-dropdowns.py      # flag placeholder-only lists
python3 scripts/check-file-placement.py # flag content files outside allowed dirs
python3 scripts/check-toc.py            # validate myst.yml TOC entries
```

These run automatically on PRs via `.github/workflows/qa.yml` (which also runs Vale). Install pre-commit hooks to catch violations before pushing:
```bash
pre-commit install        # installs hooks (done automatically by setup.sh)
pre-commit run --all-files  # run all hooks manually
```

## Architecture

### Companion DNA repository

Sequence files for every plasmid and construct referenced in these docs are maintained in a separate repository: **[nucleus-eng/DNA](https://github.com/nucleus-eng/DNA)** (local path: `~/src/nucleus-eng/DNA`). That repo stores GenBank (`.gb`) files organized by part type:

```
DNA/
├── PURE/
│   ├── cloning/      # pOpen entry vectors for all PURE system proteins
│   └── expression/   # pET28a expression vectors for PURE system proteins
├── assembly/         # MoClo backbone (pOpen-pOpenv3-MCL0)
├── RBS/              # Ribosome binding site and UTR parts
├── promoters/        # Level-matched T7 promoter library (PURET7-1 through -10)
├── reporters/        # Fluorescent protein and chromoprotein reporters
├── terminators/      # T7 terminator variants
└── detectors/        # LacI/TetR circuits and quorum sensing components
```

**Checking the DNA repo's current state.** The DNA repo evolves independently — always verify its current state before writing or editing content that references specific constructs. Use a tiered approach:

1. **Session start** — when beginning any work that involves DNA construct references, check recent activity in the DNA repo:
   ```bash
   git -C ~/src/nucleus-eng/DNA log --oneline -5
   ```
   Commit messages will tell you if the structure or contents have changed since you last worked with it.

2. **Before naming a specific construct** — before writing a protocol step that references a construct by filename (e.g., `pOpen-PURET7-3`), confirm the file exists:
   ```bash
   ls ~/src/nucleus-eng/DNA/promoters/pOpen-PURET7-3.gb
   ```
   If the file is missing, flag it to the developer — do not invent construct names or create placeholder references.

3. **If folder structure is uncertain** — if you are unsure which subdirectory a part type lives in, read the DNA repo's README:
   ```bash
   # or: Read ~/src/nucleus-eng/DNA/README.md
   ```
   The README is maintained as the canonical description of the repo structure.

**Key rules when working across both repos:**

- **Do not create or store `.gb` sequence files in nucleus-docs.** All DNA sequences belong in the DNA repo.
- **Construct names in protocol pages must match actual filenames** in the DNA repo (e.g., a step that says "use `pOpen-PURET7-3`" corresponds to `promoters/pOpen-PURET7-3.gb`). Verify before writing.
- **Cross-repo links** in doc pages should point to the GitHub URL of the `.gb` file in `nucleus-eng/DNA`, not to a local path.
- **Changes to the DNA repo are out of scope for nucleus-docs PRs.** If a protocol requires a new construct that doesn't exist in the DNA repo yet, flag that to the developer rather than creating a placeholder.

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
- `typst/nucleus-protocols/` — the branded typst template used to render lab-ready protocol/BOM PDFs (vendored in-repo; pubmatter pinned to 0.2.2 — see its README)

### Lab-ready protocol pipeline (issue #10)

`scripts/build-protocols.py` generates downloadable artifacts from process pages — **derived files are never committed; they are rebuilt at deploy so they cannot drift from the source page.** For each `docs/processes/**/main.md` (or `*-main.md`) that has a `# Protocol` heading, it writes to a gitignored `generated/` dir beside the page:

- `<slug>-protocol.pdf` — a pure bench checklist: page title + step headings + `- [ ]` items + a brief hazard note (if present). All prose, admonitions, and figures are stripped; **tables are kept** (recipes/reaction setups are part of the procedure). `<slug>` is the process's directory name.
- `<slug>-bom.pdf` + `<slug>-materials.csv` — generated from the page's Bill of Materials, supplied as **either** an inline table labeled `bom-<slug>` **or** an uploaded `resources/<slug>-bom.csv` beside the page (whichever exists; see `resolve_bom_source` in `build-protocols.py`). Generated only if one of those exists.

Markers the generator keys off: `# Protocol` heading (pages without one are skipped, as are stubs with no checklist items); frontmatter `title:`; an admonition titled `Hazardous Materials` for the hazard note; a `bom-<slug>` table **or** a `resources/<slug>-bom.csv` for the BOM/CSV. Cross-reference roles (`{ref}`, `{numref}`) in protocol steps are neutralized to a plain noun, since they often point at stripped sections.

**Rules:**
- `generated/` is gitignored (`**/generated/`) — never commit PDFs/CSVs. Treat `resources/` as source assets, `generated/` as derived.
- Download buttons point at the relative generated path, e.g. `` {button}`download <generated/<slug>-protocol.pdf>` ``. MyST resolves these at build time, so **generation must run before `myst build`** (the deploy/CI ordering). Only include a BOM button if the page has a BOM source (`bom-<slug>` table or `resources/<slug>-bom.csv`).
- A page's BOM may be an inline table labeled `bom-<slug>` (the slug must match the directory name) **or** an uploaded `resources/<slug>-bom.csv`. **If both exist they must agree** — `check-bom-labels.py` fails on any row-for-row difference after normalization (the inline table is what renders; the CSV is treated as a redundant copy that must not drift). Use the standard 8-column schema: `Name | Category | Product | Manufacturer | Part # | Price | Storage | Link`.
- `scripts/check-bom-labels.py` (runs on PRs via `.github/workflows/protocols.yml`) enforces: bom label matches directory; a BOM download button points at the canonical `generated/<slug>-bom.pdf` (a misnamed BOM PDF is caught too) and has a backing source; protocol download buttons point at `generated/<slug>-protocol.pdf`; inline/CSV agreement; and flags orphan standalone `bom-*.md` pages, misnamed `resources/*bom*.csv`, and a BOM source on a page with no `# Protocol`.
- `scripts/enrich-bom.py <page>` is an author-time aid (not in CI): it fills the **empty** cells of a page's `bom-<slug>` table from other pages' BOM tables by exact `(manufacturer, part #)` match, and reports near matches (same name, different part #) for manual review. Dry-run by default; `--write` applies.
- `scripts/build-materials-reference.py` aggregates every BOM table across `docs/` into one distribution-wide reference, written to a gitignored `guides/generated/` partial that `guides/materials-reference.md` includes (derived, rebuilt at deploy — same model as the PDFs; wired into `deploy.yml` before `myst build`). It also prints a near-duplicate/conflict QA report. Point contributors at the rendered **Materials Reference** page to reuse existing part numbers and vendors rather than introducing near-duplicates.
- Shared parse/normalize/index logic lives in `scripts/bom_common.py` (imported by the generator, the checker, the enricher, and the reference) — change the definition of "a BOM table" or "equal" there, once.

### Prose formatting

**Do not hard-wrap paragraph text.** Write prose paragraphs as a single line, regardless of length. Do not insert line breaks in the middle of a sentence or at an arbitrary column width. Hard wraps in `.md` files render as spaces in most contexts but create messy diffs and make future editing harder. This applies to instructional text in templates, overview sections, figure captions, and all other prose. The only intentional line breaks in paragraph content are blank lines between paragraphs.

### MyST syntax conventions

Pages use MyST admonition nesting with `:::` fences. Process pages follow a consistent structure:
1. Frontmatter (`title:`)
2. `# Overview` with an `:::::::{card}` block containing nested dropdowns for Notes, Prerequisites, Hazardous Materials, Critical Materials, Genetically Encoded Components, Composition, and References
3. `# Protocol` with `##` subsections and checklist steps (`- [ ]`)
4. `# Downloads` grid with cards linking to PDF lab protocol and Bill of Materials

Protocol steps use `- [ ]` checkboxes and `:::{hint}` dropdowns for extended notes. Cross-references use MyST `{ref}` syntax for same-page targets and standard markdown links for cross-page references.

### Overview card dropdowns — empty dropdown policy

The template includes all possible dropdown sections as a starting point. **When authoring or reviewing a process page, only keep dropdowns that have real content.** Delete any dropdown whose only content is a placeholder (e.g. `- TODO`).

The process template uses `- TODO` as the scaffold placeholder — this is intentional so contributors know which sections need to be filled in. **`check-dropdowns.py` (and CI) will fail if any `- TODO`, `- None`, `- N/A`, or `- TBD` placeholder-only list survives outside `templates/`.** Before opening a PR, run:
```bash
python3 scripts/check-dropdowns.py
```

**When editing or reviewing a process page**, scan for empty dropdowns matching this pattern and flag them:

```
::::::{<type>} <Section Title>
:class: dropdown
:icon: false

- TODO

::::::
```

If you find one, flag it and ask the developer: **"The `<Section Title>` dropdown is empty — should it be deleted, or does it need content?"** Wait for confirmation before making any changes. Do not silently leave placeholder content in committed files, but also do not silently delete them. The template file (`templates/process-template/process-make_template.md`) is the only file exempt from this rule.

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
- **Materials/consumables lists**: For a BOM rendered on the page, keep it as an inline markdown table labeled `bom-<slug>` (mystmd does not support the `{csv-table}` `:file:` option for rendering external CSVs — the table must be inlined); the lab-ready pipeline generates `<slug>-materials.csv` from it. A contributor may alternatively upload the BOM as `resources/<slug>-bom.csv` (the pipeline ingests it the same way) — but do **not** hand-maintain a generic `resources/materials.csv` copy alongside an inline table, and if both a `bom-<slug>` table and `resources/<slug>-bom.csv` exist they must agree (CI enforces it). See the lab-ready protocol pipeline section below.
- **Notion `<aside>` blocks**: Convert to the appropriate MyST admonition or section header depending on context (e.g., "Getting Started" asides → Overview prose, "Step X" asides → `##` section headers, "Resources" asides → `# References`).
- **Notion toggles**: Convert to `:::{hint} Note: <title>` with `:class: dropdown`.
- **Units in table column headers**: Use parentheses, not brackets (e.g., `MW (g/mol)` not `MW [g/mol]`).

### External references

`myst.yml` maintains a `references:` map of named keys (e.g., `devnote-01:`) pointing to external DevNote URLs. These can be cited throughout the docs without repeating URLs.

### Prose linting (Vale)

**Run `vale docs/` before opening a PR or committing a content migration.** Vale lints both `.md` and `.csv` files under `docs/`. Vale runs as part of the `qa` CI workflow (`.github/workflows/qa.yml`).

```bash
vale docs/          # lint all docs
vale <file.md>      # lint a single file
```

Vale rules live in `styles/nucleus/`. Current rules enforce temperature unit formatting (`°C`), micro symbol usage (`µ`), and ion notation (`Mg2+`).

**Interpreting `nucleus.degrees-symbol` errors.** This rule flags patterns like `37C` or `4 C` that are missing the degree symbol. However, it cannot distinguish temperatures from alphanumeric labels, so it produces false positives. When Vale flags a `nucleus.degrees-symbol` error, check the surrounding context:

- **Real error** — the token is a temperature value. Fix it by adding the degree symbol (e.g., `37C` → `37°C`, `4 C` → `4°C`).
  - Signals: preceded by "at", "to", "of", or a verb like "incubate", "store", "heat"; followed by "for X minutes/hours"; in a reaction table or thermocycler step.
  - **Table cells**: a bare value (e.g., `37C`) in a table column whose header indicates temperature (e.g., "Temperature", "Incubation temp", "Storage") is always a real error, even without surrounding signal words.
- **False positive** — the token is a label, not a temperature. Leave it alone.
  - Signals: preceded by "Figure", "Fig.", "Step", "Lane", "Panel", "Tube", "Option", or a similar structural label word.

**Interpreting `nucleus.ion-notation` errors.** This rule flags `Mg++` and should always be treated as a real error — replace with `Mg2+`. There are no known false positives.

**Interpreting `nucleus.micro-symbol` errors.** This rule flags patterns like `10 uL`, `500 uM`, or `2 um` that use an ASCII `u` instead of the micro symbol `µ`. Always a real error — replace with `µL`, `µM`, or `µm` respectively.

**Vale `TokenIgnores` limitation on CSV files.** Vale's `TokenIgnores` setting (used to suppress URL matches) works for `.md` files but is silently ignored for `.csv` files. This means URL-encoded sequences like `%2C` in CSV cells can trigger rules even when URLs are listed in `TokenIgnores`. The workaround is to bake URL safety directly into the rule pattern (e.g., `(?<!%)\d+\s*C\b` instead of `\d+\s*C\b`).

**Applying fixes programmatically.** When using a script (e.g., perl/sed) to bulk-apply degrees-symbol fixes, always use a negative lookbehind for `%` to avoid corrupting URL-encoded sequences like `%2C` (comma):

```perl
# Safe — won't corrupt %2C, %3C, etc. in URLs
s/(?<!%)(\d+)C\b/$1°C/g

# Unsafe — will corrupt URL-encoded sequences
s/(\d+)C\b/$1°C/g
```

Do not add Vale inline suppression comments (`<!-- vale off -->`) without confirming with the developer first.

### Link checking (lychee)

**Run `python3 scripts/check-links.py docs/` before opening a PR if you have added, edited, or removed any links or URLs.** This is slower than Vale and doesn't need to run on every commit — focus on PRs that touch links.

```bash
python3 scripts/check-links.py docs/       # check all docs
python3 scripts/check-links.py <file.md>   # check a single file
```

The script wraps `lychee` and filters known false positives before reporting. **What it catches:** dead internal links, 404 external links, empty URLs. **What it does not catch:** product catalog changes on vendor sites (e.g. Sigma-Aldrich discontinuing a part number) — those require manual review.

**Interpreting output.** The script will note how many HTTP/2 false positives were filtered from `sigmaaldrich.com` — these are valid URLs on a server that blocks automated crawlers at the protocol level and can be ignored. Any remaining errors are genuine and should be fixed before opening a PR.

### Pull request workflow

When merging a PR via `gh pr merge`, never use `--admin` to bypass branch protection rules. If a merge fails due to branch policy, stop and ask the developer how to proceed — options are leaving the PR open for a reviewer, asking the developer to approve it themselves, or using `--auto` to merge once requirements are met.
