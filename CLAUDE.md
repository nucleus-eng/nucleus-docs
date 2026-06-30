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

### Templates

`templates/` contains Cookiecutter-style starter files:
- `process-template/process-make_template.md` — full example of a process page including admonition blocks, protocol steps with checkboxes, and a Downloads section
- `module-template/spec.md` — module spec structure with schematic, designs table, compatible processes, and usage references
- `implementation-template/implementation-template.md` — combined implementation format
- `typst/nucleus-protocols/` — the branded typst template used to render lab-ready protocol/BOM PDFs (vendored in-repo; pubmatter pinned to 0.2.2 — see its README)

**When migrating content into a pre-created stub directory**, scan for and delete any template placeholder files before committing. Stub directories are often created with placeholder images (e.g. `behavior/ppk-kinetics.png`, `behavior/ppk-endpoint.png`) that have no real data and were copied from the implementation template. Run `git ls-files docs/modules/<module>/` to see what's tracked, and `git rm` any placeholders that have not been replaced by real figures.

### Lab-ready protocol pipeline

**Working on BOMs or the protocol pipeline** (`build-protocols.py`, `check-bom-labels.py`, `bom-<slug>` tables, download buttons)? Invoke the `build-boms` skill for the full pipeline spec and rules. One always-on rule: `generated/` is gitignored (`**/generated/`) — never commit PDFs or CSVs.

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

**Internal links in inline HTML must use `.md` extensions, not `.html`.** MyST resolves internal links via the source `.md` paths. Using `.html` in an `<a href="...">` tag produces a 404 on the deployed site. This applies to all inline HTML links (e.g. version badges, quick-link pills) — always write `href="./path/to/page.md"`, never `href="./path/to/page.html"`.

**Tab-set fence depth.** Tab-sets require a consistent three-level nesting: the outer `{tab-set}` uses `:::::`(5 colons), each `{tab-item}` inside uses `::::` (4 colons), and figures or admonitions inside a tab-item use `:::` (3 colons). Mismatched colon counts are a common source of rendering failures.

**Secondary figures.** Within a section that has a primary figure (e.g. a performance plot), de-emphasize supplementary or supporting figures by wrapping them in a `::::{hint} <descriptive title>` block with `:class: dropdown`. The dropdown title should describe the finding, not just label the figure (e.g. `::::{hint} The Emitter Cell causes E. coli to express GFP in response to IV-HSL`). This keeps the primary figure prominent while keeping supporting context one click away. When there are multiple parallel secondary figures (e.g. the same experiment across several conditions), use a hybrid: a single dropdown wrapping a tab-set, so readers open one drawer and switch between conditions with tabs. The outer hint uses 7 colons, the `{tab-set}` inside uses 6, each `{tab-item}` uses 5, and figures inside use 3 — consistent with the tab-set nesting rules above.

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

### Content migration

**Migrating Notion or DevNote content?** Invoke the `migrate-content` skill — it has the full checklist: table indentation, aside/toggle conversion, DOI citation format, data-discrepancy flagging, scope boundary (spec vs. process), and more.

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

### Prose linting

**Before opening a PR or committing content**, run Vale + codespell (and the link checker if you touched any URLs). Invoke the `lint-docs` skill for exact commands and how to interpret each tool's output — including which Vale errors are real vs. false positives.

### Pull request workflow

When merging a PR via `gh pr merge`, never use `--admin` to bypass branch protection rules. If a merge fails due to branch policy, stop and ask the developer how to proceed — options are leaving the PR open for a reviewer, asking the developer to approve it themselves, or using `--auto` to merge once requirements are met.
