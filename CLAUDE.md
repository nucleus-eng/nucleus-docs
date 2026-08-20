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

**Check for myst build errors** (what the `build-protocols` CI job gates on — see issue #176):
```bash
python3 scripts/build-protocols.py
python3 scripts/build-materials-reference.py
python3 scripts/check-myst-build.py
```
`scripts/check-myst-build.py` runs `myst build --html --strict` and fails only on ⛔️ errors (broken links, missing images, malformed directives) — ⚠️ warnings are summarized but never fail the build. Run the two generator scripts first: `guides/materials-reference.md` and every process page's Downloads cards reference gitignored `generated/` artifacts, and a build run without them reports those as real missing-file errors. Known false positives (currently: a figure sourced from a remote DevNote via `xref:`, which myst still checks for on local disk) are declared in `scripts/myst-build-false-positives.toml` — myst's own `error_rules` config can't scope this to a single file, since some rules carry no per-file key, so a `myst.yml`-level suppression would silently blind the check to a genuinely missing file anywhere else in the docs.

**Generate lab-ready protocol PDFs / BOMs** (requires `myst` + `typst` on PATH):
```bash
python3 scripts/build-protocols.py            # all processes
python3 scripts/build-protocols.py <dir>      # one process
python3 scripts/build-protocols.py --extract-only   # skip PDF rendering
```

**When verifying changes before a commit, only regenerate the process directories you actually touched** — pass the specific `docs/processes/<dir>` path(s) to `build-protocols.py`, not the bare command. Rendering PDFs for the whole site via `myst` + `typst` is the slowest step in local verification, and CI regenerates everything from scratch at deploy time regardless, so a full-site run adds no safety over a scoped one.

CI runs on pushes to `main` via `.github/workflows/deploy.yml`, installing `mystmd` via npm and deploying to GitHub Pages.

**QA checks** (run locally before opening a PR):
```bash
python3 scripts/check-dropdowns.py      # flag placeholder-only lists
python3 scripts/check-file-placement.py # flag content files outside allowed dirs
python3 scripts/check-toc.py            # validate myst.yml TOC entries
python3 scripts/check-dna-refs.py       # if you touched a Designs table: verify construct/bp claims against nucleus-eng/DNA
```

These run automatically on PRs via `.github/workflows/qa.yml` (which also runs Vale). Install pre-commit hooks to catch violations before pushing:
```bash
pre-commit install        # installs hooks (done automatically by setup.sh)
pre-commit run --all-files  # run all hooks manually
```

## Architecture

### Companion DNA repository

Sequence files for every plasmid and construct referenced in these docs live in a separate repository: **[nucleus-eng/DNA](https://github.com/nucleus-eng/DNA)** (local path: `~/src/bnext/nucleus-eng/DNA`). Never create or store `.gb` files here, and never link a construct into the legacy `bnext-bio/nucleus` repo.

**Naming a construct, or adding a Designs-table row?** Invoke the `verify-dna-constructs` skill first. A Designs-table row is an identity claim, not a name match — the skill has the repo layout, the verification steps, the Nucleus-equivalent attention block, and `scripts/check-dna-refs.py`.

### Terminology

These definitions ground the module/implementation content model below (`docs/modules/`, `docs/implementations/`, and their `spec.md` files):

- Composition (n): the physical make up of a system; typically concentration and spatial organization
- Composing (v): the act of combining two or more systems and their associated functions
- Component: an element (abstract or concrete) of Composition; a single part or piece of a larger whole. May be defined as having subcomponents.
- Function: a designed behavior; defined by and emergent from Composition
- Requirements: Functional or Compositional elements whose presence (or often absence) are required (and in specified amounts) in order for a system of a given Composition to demonstrate a designed Function
- Module: a component with specified Composition and Function (given certain Requirements).
- Specification: a concrete description of the Composition and Function of a system, as well as any Requirements on that system to Function as described
- Integration: the engineering work required to modify the Composition of two or more Modules such as to retain their Functions when composed.

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

Note that `hidden: true` is used pervasively for *every* non-sidebar child page — it is a navigation setting, **not** a maturity signal. Page maturity is tracked separately via the `status:` frontmatter field, which the `author-myst-content` skill documents.

### Templates

`templates/` contains Cookiecutter-style starter files:
- `process-template/process-make_template.md` — full example of a process page including admonition blocks, protocol steps with checkboxes, and a Downloads section
- `module-template/spec.md` — module spec structure with schematic, designs table, compatible processes, and usage references
- `implementation-template/implementation-template.md` — combined implementation format
- `typst/nucleus-protocols/` — the branded typst template used to render lab-ready protocol/BOM PDFs (vendored in-repo; pubmatter pinned to 0.2.2 — see its README)

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

### Authoring pages in MyST

**Writing or editing a page under `docs/`?** Invoke the `author-myst-content` skill. It covers fence and tab-set nesting depth, `.md`-not-`.html` internal links, secondary-figure dropdowns, system-context figure placement, composition-table depth, the `status:` frontmatter values and their banners, and the empty-dropdown policy that `scripts/check-dropdowns.py` enforces.

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

### Checking your work

**Before opening a PR or committing content**, run Vale + codespell, and the link checker if you touched any URLs. Invoke the `lint-docs` skill for the exact commands and how to read each tool's output — including which Vale errors are real and which are false positives. It also covers `scripts/check-myst-build.py`, the strict MyST build that the `build-protocols` CI job gates on.

### Pull request workflow

When merging a PR via `gh pr merge`, never use `--admin` to bypass branch protection rules. If a merge fails due to branch policy, stop and ask the developer how to proceed — options are leaving the PR open for a reviewer, asking the developer to approve it themselves, or using `--auto` to merge once requirements are met.
