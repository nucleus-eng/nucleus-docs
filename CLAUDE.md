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

4. **If `~/src/nucleus-eng/DNA` is not on this machine** — use the GitHub API as a fallback to browse the repo or inspect construct files without cloning:
   ```bash
   # Browse a directory (e.g. detectors/)
   gh api "repos/nucleus-eng/DNA/contents/detectors" --jq '.[].name'
   # Decode a GenBank file and read the LOCUS line for construct length
   gh api "repos/nucleus-eng/DNA/contents/detectors/pOpen-LacI-IPTG.gb" --jq '.content' | base64 -d | grep "^LOCUS"
   ```

**Key rules when working across both repos:**

- **Do not create or store `.gb` sequence files in nucleus-docs.** All DNA sequences belong in the DNA repo.
- **Construct names in protocol pages must match actual filenames** in the DNA repo (e.g., a step that says "use `pOpen-PURET7-3`" corresponds to `promoters/pOpen-PURET7-3.gb`). Verify before writing.
- **Cross-repo links** in doc pages should point to the GitHub URL of the `.gb` file in `nucleus-eng/DNA`, not to a local path.
- **Changes to the DNA repo are out of scope for nucleus-docs PRs.** If a construct referenced in a source page is not found in `nucleus-eng/DNA`, add an `:::{attention}` block in the spec noting the gap, e.g.: "Construct `pOpen-pT7-Cx43` is not yet in `nucleus-eng/DNA` (originated in `bnext-bio/nucleus`). Do not link to the legacy repo — flag for follow-up so the construct can be submitted to `nucleus-eng/DNA` before this page is used at the bench." DNA constructs referenced in a DevNote SHOULD be submitted to `nucleus-eng/DNA` before or alongside migration; if they are not present at migration time, apply the attention block and flag.

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

**Manufacturer PDFs and datasheets must not be committed to this repo.** Reference them via vendor URLs or host them externally. Until a shared hosting convention is established, add a `<!-- TODO: replace with hosted PDF link -->` comment on the download card in the `# Downloads` section rather than committing the file. Do not include vendor PDFs in PRs.

### Table of contents management

The site TOC is defined entirely in `myst.yml`. When adding a new page, you must add it to the `toc:` section. Child pages that should not appear directly in the sidebar use `hidden: true`. The file `site.yml` holds site-wide settings (license, nav links, theme) that `myst.yml` extends.

**Adding a module spec requires two table-of-contents updates, not one.** In addition to the `myst.yml` TOC entry, add a row to the table in `docs/modules/modules-main.md`. The table columns are `Module Class | Specification | Validation` — fill in the class name (e.g. `Detector`), a relative link to the spec (e.g. `[LacI-IPTG](./detector-laci_iptg/spec.md)`), and the validation star rating (use `★` for validated, `☆` for unvalidated, following the existing rows as a guide). Missing this step leaves the module off the main module index page.

### Templates

`templates/` contains Cookiecutter-style starter files:
- `process-template/process-make_template.md` — full example of a process page including admonition blocks, protocol steps with checkboxes, and a Downloads section
- `module-template/spec.md` — module spec structure with schematic, designs table, compatible processes, and usage references
- `implementation-template/implementation-template.md` — combined implementation format
- `typst/nucleus-protocols/` — the branded typst template used to render lab-ready protocol/BOM PDFs (vendored in-repo; pubmatter pinned to 0.2.2 — see its README)

**When migrating content into a pre-created stub directory**, scan for and delete any template placeholder files before committing. Stub directories are often created with placeholder images (e.g. `behavior/ppk-kinetics.png`, `behavior/ppk-endpoint.png`) that have no real data and were copied from the implementation template. Run `git ls-files docs/modules/<module>/` to see what's tracked, and `git rm` any placeholders that have not been replaced by real figures.

### Lab-ready protocol pipeline (issue #10)

`scripts/build-protocols.py` generates downloadable artifacts from process pages — **derived files are never committed; they are rebuilt at deploy so they cannot drift from the source page.** For each `docs/processes/**/main.md` (or `*-main.md`) that has a `# Protocol` heading, it writes to a gitignored `generated/` dir beside the page:

- `<slug>-protocol.pdf` — a pure bench checklist: page title + step headings + `- [ ]` items + a brief hazard note (if present). All prose, admonitions, and figures are stripped; **tables are kept** (recipes/reaction setups are part of the procedure). `<slug>` is the process's directory name.
- `<slug>-bom.pdf` + `<slug>-materials.csv` — generated **only if** the page has a table labeled `bom-<slug>`.

Markers the generator keys off: `# Protocol` heading (pages without one are skipped, as are stubs with no checklist items); frontmatter `title:`; an admonition titled `Hazardous Materials` for the hazard note; a `bom-<slug>` labeled table for the BOM/CSV. Cross-reference roles (`{ref}`, `{numref}`) in protocol steps are neutralized to a plain noun, since they often point at stripped sections.

**Rules:**
- `generated/` is gitignored (`**/generated/`) — never commit PDFs/CSVs. Treat `resources/` as source assets, `generated/` as derived.
- Download buttons point at the relative generated path, e.g. `` {button}`download <generated/<slug>-protocol.pdf>` ``. MyST resolves these at build time, so **generation must run before `myst build`** (the deploy/CI ordering). Only include a BOM button if the page has a `bom-<slug>` table.
- A page's materials/BOM table must be labeled `bom-<slug>` to be picked up (the slug must match the directory name). `scripts/check-bom-labels.py` enforces the download/label conventions (bom label matches directory; BOM download buttons have a backing table; protocol download buttons point at `generated/<slug>-protocol.pdf`, not a placeholder or another page's PDF) and runs on PRs via `.github/workflows/protocols.yml`.

### Prose formatting

**Do not hard-wrap paragraph text.** Write prose paragraphs as a single line, regardless of length. Do not insert line breaks in the middle of a sentence or at an arbitrary column width. Hard wraps in `.md` files render as spaces in most contexts but create messy diffs and make future editing harder. This applies to instructional text in templates, overview sections, figure captions, and all other prose. The only intentional line breaks in paragraph content are blank lines between paragraphs.

### MyST syntax conventions

Pages use MyST admonition nesting with `:::` fences. Process pages follow a consistent structure:
1. Frontmatter (`title:`)
2. `# Overview` with an `:::::::{card}` block containing nested dropdowns for Notes, Prerequisites, Hazardous Materials, Critical Materials, Genetically Encoded Components, Composition, and References
3. `# Protocol` with `##` subsections and checklist steps (`- [ ]`)
4. `# Downloads` grid with cards linking to PDF lab protocol and Bill of Materials

Protocol steps use `- [ ]` checkboxes and `:::{hint}` dropdowns for extended notes. Cross-references use MyST `{ref}` syntax for same-page targets and standard markdown links for cross-page references.

**Tab-set fence depth.** Tab-sets require a consistent three-level nesting: the outer `{tab-set}` uses `:::::`(5 colons), each `{tab-item}` inside uses `::::` (4 colons), and figures or admonitions inside a tab-item use `:::` (3 colons). Mismatched colon counts are a common source of rendering failures.

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
- **Materials/consumables lists**: Large materials tables should be kept as inline markdown tables (mystmd does not support the `{csv-table}` `:file:` option for rendering external CSVs — the table must be inlined). Do **not** hand-maintain a `resources/materials.csv` copy: the lab-ready pipeline generates `<slug>-materials.csv` from the page's `bom-<slug>` labeled table. See the lab-ready protocol pipeline section below.
- **Notion `<aside>` blocks**: Convert to the appropriate MyST admonition or section header depending on context (e.g., "Getting Started" asides → Overview prose, "Step X" asides → `##` section headers, "Resources" asides → `# References`).
- **Notion toggles**: Convert to `:::{hint} Note: <title>` with `:class: dropdown`.
- **Units in table column headers**: Use parentheses, not brackets (e.g., `MW (g/mol)` not `MW [g/mol]`).
- **Concentration discrepancies**: Reaction tables in Notion sources sometimes list a stock concentration that does not match the stated final concentration. Before migrating a table, verify that `stock concentration × volume / total volume = stated final concentration` for every reagent row. If a discrepancy is found, do not silently copy the values — add a `:::{warning}` block flagging the specific row(s) for author review before the page is used at the bench.
- **Scope boundary — spec vs. process**: Protocol steps, materials tables, and imaging conditions from a DevNote belong in a future Process page, not the module spec. The spec covers what the module is, its genetic designs, and expected performance. If protocol-level content appears in the DevNote, note it with a `<!-- TODO: move to process page -->` comment rather than migrating it into the spec.
- **DevNote migration start — read `curvenote.yml` first**: `curvenote.yml` is the single best starting point for a DevNote migration. It contains the DOI, project ID, author list (with ORCIDs and affiliations), figure sources, and download files. Read it before `main.md` to orient to the content.
- **DevNote figures — use static PNGs with `:name:` labels**: Computed figures (e.g. from Jupyter notebook outputs or `lorem.mjs`) cannot be copied as static images and cannot be cross-referenced from nucleus-docs. Key result figures in a module spec should be static PNG files with explicit `:name: fig:something` labels in `main.md`. Only figures with `:name:` labels are reachable via `xref:<devnote-key>#fig:something` in spec pages.
- **Bare DOI citations from Curvenote**: Curvenote DevNotes use `[](10.xxxx/xxxxx)` as a shorthand DOI citation. This resolves as a local file path in the nucleus-docs MyST build and causes a link-checker error. Always replace with a full markdown link on migration: `[Author et al., year](https://doi.org/10.xxxx/xxxxx)`. Check for bare `[](` patterns with `grep -n '\[\](' <file>` before committing a migrated spec.

### External references

`myst.yml` maintains a `references:` map of named keys (e.g., `devnote-01:`) pointing to external DevNote URLs. These can be cited throughout the docs without repeating URLs.

### Prose linting (Vale)

**Run `vale docs/` before opening a PR or committing a content migration.** Vale lints both `.md` and `.csv` files under `docs/`.

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
