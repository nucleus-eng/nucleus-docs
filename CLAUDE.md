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
| Module raw assets (Notion/DevNote exports, source files) | `docs/modules/<module-name>/resources/` |

**Before creating or moving any file**, verify the target path matches this structure. If a file is about to land outside `docs/`, stop and flag it to the developer before proceeding.

**Manufacturer PDFs and datasheets must not be committed to this repo.** Reference them via vendor URLs or host them externally. Until a shared hosting convention is established, add a `<!-- TODO: replace with hosted PDF link -->` comment on the download card in the `# Downloads` section rather than committing the file. Do not include vendor PDFs in PRs.

### Table of contents management

The site TOC is defined entirely in `myst.yml`. When adding a new page, you must add it to the `toc:` section. Child pages that should not appear directly in the sidebar use `hidden: true`. The file `site.yml` holds site-wide settings (license, nav links, theme) that `myst.yml` extends.

**Adding a module spec requires two table-of-contents updates, not one.** In addition to the `myst.yml` TOC entry, add a row to the table in `docs/modules/modules-main.md`. The table columns are `Module Class | Specification | Validation` — fill in the class name (e.g. `Detector`), a relative link to the spec (e.g. `[LacI-IPTG](./detector-laci_iptg/spec.md)`), and the validation star rating (use ★ to ★★★ following the validation key at the top of `modules-main.md`: ★ = preliminary/DevNote only, ★★ = validated in cells or in vitro, ★★★ = frequently used). Missing this step leaves the module off the main module index page.

Note that `hidden: true` is used pervasively for *every* non-sidebar child page — it is a navigation setting, **not** a maturity signal. Page maturity is tracked separately via the `status:` frontmatter field (see below).

### Page status (draft / published)

Every content page has a maturity `status`, declared as a frontmatter field. This keeps stub or unvalidated pages from misrepresenting themselves on the public site without a heavyweight build-exclusion mechanism (issue #74; #57 may later add build-time exclusion keyed off this same field).

| `status:` value | meaning | TOC | banner |
| --- | --- | --- | --- |
| `draft` | incomplete; not ready for public consumption | must be `hidden: true` (keep out of the sidebar) | **Draft** banner (below) |
| `unvalidated-published` | complete and publicly visible, but not yet validated in the current Nucleus Cytosol | normal | **Not yet validated** banner (below) |
| `validated-published` | complete and validated; ready | normal | none |

- **Absent `status:` is treated as `validated-published`** — do not churn the ~50 ready pages. Only `draft` and `unvalidated-published` pages need an explicit field.
- **Templates ship with `status: draft`** so a new page can't accidentally appear validated; the author changes it to `unvalidated-published` or `validated-published` when ready.
- The `status:` field does **not** auto-render anything — add the matching banner by hand when you set `draft` or `unvalidated-published`. The two standard banners:

```
:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::
```

```
:::{attention} Not yet validated
This page has not been validated in Nucleus Cytosol. <optional specifics, e.g. "Expected performance data below is from PURExpress cells.">
:::
```

A page may also carry an unrelated content caveat (e.g. aHly's "not actively supported" BSL-2 note) — that is independent of `status:` and stays as its own admonition.

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

`scripts/check-formatting.py` detects hard-wrapped prose and runs as a **warning-only** CI check (never blocks a PR). Run it locally to surface violations before review:

```bash
python3 scripts/check-formatting.py          # check docs/ and templates/ (exits 0 always)
python3 scripts/check-formatting.py --strict # exit 1 if findings found (for local enforcement)
python3 scripts/check-formatting.py docs/    # check a specific directory
```

### MyST syntax conventions

Pages use MyST admonition nesting with `:::` fences. Process pages follow a consistent structure:
1. Frontmatter (`title:`)
2. `# Overview` with an `:::::::{card}` block containing nested dropdowns for Notes, Prerequisites, Hazardous Materials, Critical Materials, Genetically Encoded Components, Composition, and References
3. `# Protocol` with `##` subsections and checklist steps (`- [ ]`)
4. `# Downloads` grid with cards linking to PDF lab protocol and Bill of Materials

Protocol steps use `- [ ]` checkboxes and `:::{hint}` dropdowns for extended notes. Cross-references use MyST `{ref}` syntax for same-page targets and standard markdown links for cross-page references.

**Tab-set fence depth.** Tab-sets require a consistent three-level nesting: the outer `{tab-set}` uses `:::::`(5 colons), each `{tab-item}` inside uses `::::` (4 colons), and figures or admonitions inside a tab-item use `:::` (3 colons). Mismatched colon counts are a common source of rendering failures.

**Secondary figures.** Within a section that has a primary figure (e.g. a performance plot), de-emphasize supplementary or supporting figures by wrapping them in a `::::{hint} <descriptive title>` block with `:class: dropdown`. The dropdown title should describe the finding, not just label the figure (e.g. `::::{hint} The Emitter Cell causes E. coli to express GFP in response to IV-HSL`). This keeps the primary figure prominent while keeping supporting context one click away.

**System-context figure placement (module specs).** A figure showing the module in the context of the Base Cell or Developer Cell belongs in the `## Cells` section, not `# Overview`. The Overview section should carry mechanism and schematic figures only.

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
- **Data discrepancies (including concentrations)**: Source content sometimes carries internally inconsistent or unverified values — a value in the body text that conflicts with a figure caption, or a stock concentration that does not match the stated final concentration. Do not silently correct or copy these — add a `:::{warning}` block adjacent to the affected content that names the specific discrepancy, shows the conflicting values, states the most likely interpretation, and instructs the reviewer to verify before bench use. For reaction tables specifically, verify that `stock concentration × volume / total volume = stated final concentration` for every reagent row, and flag any row that fails.
- **Scope boundary — spec vs. process**: Protocol steps, materials tables, and imaging conditions from a DevNote belong in a future Process page, not the module spec. The spec covers what the module is, its genetic designs, and expected performance. If protocol-level content appears in the DevNote, note it with a `<!-- TODO: move to process page -->` comment rather than migrating it into the spec.
- **DevNote figures — use static PNGs with `:name:` labels**: Computed figures (e.g. from Jupyter notebook outputs or `lorem.mjs`) cannot be copied as static images and cannot be cross-referenced from nucleus-docs. Key result figures in a module spec should be static PNG files with explicit `:name: fig:something` labels in `main.md`. Only figures with `:name:` labels are reachable via `xref:<devnote-key>#fig:something` in spec pages.
- **Bare DOI citations from Curvenote**: Curvenote DevNotes use `[](10.xxxx/xxxxx)` as a shorthand DOI citation. This resolves as a local file path in the nucleus-docs MyST build and causes a link-checker error. Always replace with a full markdown link on migration: `[Author et al., year](https://doi.org/10.xxxx/xxxxx)`. Check for bare `[](` patterns with `grep -n '\[\](' <file>` before committing a migrated spec.

### DevNote migration

**Read `curvenote.yml` first.** `curvenote.yml` is the single best starting point for a DevNote migration. It contains the DOI, project ID, author list (with ORCIDs and affiliations), figure sources, and download files. Read it before `main.md` to orient to the content.

### External references

`myst.yml` maintains a `references:` map of named keys (e.g., `devnote-01:`) pointing to external DevNote URLs. These can be cited throughout the docs without repeating URLs.

### Citations and references

**Do not hand-write a `# References` section (or a References dropdown).** MyST's implicit-DOI feature auto-generates a single references section at the bottom of every page from the `https://doi.org/…` links it finds in the page content. A page that also hand-maintains a References list **double-renders** (the manual list *plus* the autogen block) — and because the DOI links often live only inside that manual list, deleting it would remove the references entirely. This was issue #101.

The convention:

- **Cite each source inline** where it is discussed, using a DOI link. Both styles are fine — pick whichever reads naturally:
  - Parenthetical: `…permits passage of small molecules ([Song et al., 1996](https://doi.org/10.1126/science.274.5294.1859)).`
  - Narrative: `As shown in [Bhatt et al., 2023](https://doi.org/10.1021/jacs.2c12491), the module functions in…`
- The inline link text (`Author, YYYY`) is just the in-prose anchor; the bottom references entry is built from the DOI's live metadata, so it is authoritative. **This surfaces stale citations** — if the inline text disagrees with the rendered entry (wrong author/year/DOI), fix it.
- **DevNotes with a `10.63765/…` DOI** must be cited via their `doi.org` link so they autogenerate like any other reference (a bare `doi:10.63765/…` text string does **not** trigger autogen).
- **Non-DOI sources** (DevNotes/articles with no DOI) stay as plain inline links for now; they will not appear in the auto-generated list until the `.bib` + `{cite}` work lands (issue #138).
- After editing references, run `myst build --html` and confirm the page renders exactly **one** `myst-bibliography` block with every cited source present.

### Prose linting (Vale)

**Run `git ls-files docs/ | grep -E '\.(md|csv)$' | xargs vale` before opening a PR or committing a content migration.** This command lints only committed source files (skipping gitignored `generated/` artifacts). Vale lints both `.md` and `.csv` files and runs as part of the `qa` CI workflow (`.github/workflows/qa.yml`).

```bash
git ls-files docs/ | grep -E '\.(md|csv)$' | xargs vale   # lint all committed docs
vale <file.md>                                              # lint a single file
```

Vale rules live in `styles/nucleus/`. Current rules enforce temperature unit formatting (`°C`), micro symbol usage (`µ`), chemical notation (subscripts and ion superscripts), and unit spacing.

**Interpreting `nucleus.degrees-symbol` errors.** This rule flags patterns like `37C` or `4 C` that are missing the degree symbol. However, it cannot distinguish temperatures from alphanumeric labels, so it produces false positives. When Vale flags a `nucleus.degrees-symbol` error, check the surrounding context:

- **Real error** — the token is a temperature value. Fix it by adding the degree symbol (e.g., `37C` → `37°C`, `4 C` → `4°C`).
  - Signals: preceded by "at", "to", "of", or a verb like "incubate", "store", "heat"; followed by "for X minutes/hours"; in a reaction table or thermocycler step.
  - **Table cells**: a bare value (e.g., `37C`) in a table column whose header indicates temperature (e.g., "Temperature", "Incubation temp", "Storage") is always a real error, even without surrounding signal words.
- **False positive** — the token is a label, not a temperature. Leave it alone.
  - Signals: preceded by "Figure", "Fig.", "Step", "Lane", "Panel", "Tube", "Option", or a similar structural label word.

**Interpreting `nucleus.chemical-notation` errors.** This rule flags molecular formulae and wavelength labels written with bare ASCII digits and suggests the correct Unicode subscript form. Always a real error — replace `OD600` → `OD₆₀₀`, `A260` → `A₂₆₀`, `H2O` → `H₂O`, `ddH2O` → `ddH₂O`, `MgSO4` → `MgSO₄`, etc. The rule is a substitution rule — the error message shows the exact correct form to use. There are no known false positives (the rule uses an explicit curated list of formulae rather than a generic pattern, so construct names like `pET28a` and labels like `A19` are unaffected).

**Interpreting `nucleus.ion-charges` errors.** This rule flags ion charges written with inline numbers rather than Unicode superscripts. Always a real error — replace `Mg2+` → `Mg²⁺`, `Ni2+` → `Ni²⁺`, `Na+` → `Na⁺`, `K+` → `K⁺`, `Mg++` → `Mg²⁺`, etc. Superscript characters: ⁺ (U+207A), ² (U+00B2), ³ (U+00B3).

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

### Spell checking (codespell)

**Run `codespell docs/` before opening a PR or committing content.** codespell catches real typos and enforces American English spelling.

```bash
codespell docs/          # check all docs
codespell <file.md>      # check a single file
```

Configuration lives in `.codespellrc` at the repo root. It uses the `en-GB_to_en-US` builtin dictionary, which flags British spellings as errors (`labelled` → `labeled`, `grey` → `gray`, `Acknowledgements` → `Acknowledgments`, `homogenous` → `homogeneous`). The `ignore-words = .codespell-ignore` option suppresses known false positives — add a **lowercased** word on its own line to suppress it (e.g., `ser` suppresses the amino acid abbreviation Ser which codespell misreads as a typo for "set").

codespell only flags words in its curated misspelling dictionary, so niche technical terms (`PURExpress`, `plamGFP`, `PURET7`) are not flagged.

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
