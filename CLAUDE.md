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
python3 scripts/check-dropdowns.py      # (CI) flag placeholder-only lists
python3 scripts/check-file-placement.py # (CI) flag content files outside allowed dirs
python3 scripts/check-toc.py            # (CI) validate myst.yml TOC entries
python3 scripts/check-composition.py    # (CI) if you touched a spec.yml or a Constituent Modules list
python3 scripts/check-spec-schema.py    # (local) validate spec.yml against scripts/spec-yml-schema.yml
python3 scripts/check-anchors.py        # (local) flag #anchors MyST binds to the wrong page
python3 scripts/check-dna-refs.py       # (local) if you touched a Designs table: verify construct/bp claims against nucleus-eng/DNA
```

**The four marked `(CI)` run automatically on PRs** via `.github/workflows/qa.yml`, which
also runs Vale and `check-composition-tabs.py`. **The three marked `(local)` run in no
workflow** — `check-dna-refs.py` deliberately, because a commit in `nucleus-eng/DNA` could
turn it red with no change here (see the DNA section below); `check-anchors.py` because it
is not wired up yet; `check-spec-schema.py` deliberately, per the ruling that the composition
tooling is built before it is enforced — wiring it up needs `jsonschema` beside `pyyaml` in
`qa.yml`. Run both by hand before opening a PR. Install pre-commit hooks to catch violations before pushing:
```bash
pre-commit install        # installs hooks (done automatically by setup.sh)
pre-commit run --all-files  # run all hooks manually
```

## Staged edits

**Do not edit committed files directly when resolving a conflict or applying a ruling.** Invoke the `staging` skill. It holds the whole practice — when it applies, where the document goes, the four things it records, why a ruling is not approval to apply, that the commit is the fold-in, and the provenance rules for hashes, line numbers and cross-repo pins.

**Scope in this repo:** every committed file — `docs/`, `CLAUDE.md`, `STYLE-GUIDE.md`, `myst.yml`, `scripts/`. Files under `tmp/` are gitignored and may be edited directly. **This repo's staging location is declared in [`tmp/README.md`](tmp/README.md).**

**Name a staging file's dependencies.** One review pass can produce edits that land in several files, and applying them in the wrong order can make a correct proposal wrong — line numbers in particular are only valid against an unchanged file. This one is not in the skill.

**Open questions go at the top of the file**, ahead of the drafted edits, each with space for a ruling written inline beside it. A reviewer reads a staging file once, top to bottom; with the questions last, they read every proposed edit before reaching the one thing the drafter needs from them, and a long file buries the ask. The block is a running ledger of decided versus open, updated as rulings arrive — and a ruling written beside its question is the record. See `nucleus-eng/nucleus-skills#24`.

## Architecture

### Companion DNA repository

Sequence files for every plasmid and construct referenced in these docs live in a separate repository: **[nucleus-eng/DNA](https://github.com/nucleus-eng/DNA)** (local path: `~/src/bnext/nucleus-eng/DNA`). Never create or store `.gb` files here, and never link a construct into the legacy `bnext-bio/nucleus` repo.

**Naming a construct, or adding a Designs-table row?** Invoke the `verify-dna-constructs` skill first. A Designs-table row is an identity claim, not a name match — the skill has the repo layout, the verification steps, the Nucleus-equivalent attention block, and `scripts/check-dna-refs.py`.

### Terminology

These definitions ground the content model below — all three hierarchies: `docs/modules/`, `docs/implementations/` and `docs/processes/`, and their `spec.md` and `main.md` files:

- Composition (n): the specified make up of a system; typically concentration and spatial organization. Composition is the design, not a completed run — see [sections.md](style-guide/sections.md#reference-composition).
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

**Adding a module spec requires two table-of-contents updates, not one.** In addition to the `myst.yml` TOC entry, add a row to the table in `docs/modules/modules-main.md`. The table columns are `Module Class | Specification | Validation` — fill in the class name (e.g. `Detector`), a relative link to the spec (e.g. `[LacI-IPTG](./detector-laci-iptg/spec.md)`), and the validation star rating (use ★ to ★★★ following the validation key at the top of `modules-main.md`: ★ = preliminary/DevNote only, ★★ = validated in cells or in vitro, ★★★ = frequently used). Missing this step leaves the module off the main module index page.

Note that `hidden: true` is used pervasively for *every* non-sidebar child page — it is a navigation setting, **not** a maturity signal. Page maturity is tracked separately via the `status:` frontmatter field, which the `author-myst-content` skill documents.

### Templates

`templates/` contains Cookiecutter-style starter files:
- `process-template/process-make_template.md` — full example of a process page including admonition blocks, protocol steps with checkboxes, and a Downloads section
- `module-template/spec-formulation.md` — for a module you **mix**: cytosols, membranes, chassis, cells. Sections: Overview / Reference Composition / Expected Behavior / Process / Materials / Credits
- `module-template/spec-functional.md` — for a module you **add to someone else's recipe**: detectors, reporters, effectors, emitters, controls, pores, energy. Sections: Overview / Reference Composition / Expected Behavior (with per-context subsections) / Requirements / Implementations / Materials / Downloads / Credits

  Pick by what the page documents, not by where the module sits in the composition tree — Base Cell is a composed module but reads as a recipe, and a membrane pore is a membrane but reads as a function. Omit a section rather than stubbing it empty.
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

### Composition sources

A module may carry a `spec.yml` beside its `spec.md`: the machine-readable
composition (#248), naming the process that performs each combination step and the operator it applies. `scripts/render-composition.py` draws the diagram from it and writes it into the `gen:composition-diagram` markers on that page.

```bash
python3 scripts/render-composition.py docs/modules/<module>/spec.yml            # print the mermaid
python3 scripts/render-composition.py docs/modules/<module>/spec.yml --embed    # write it into spec.md
python3 scripts/render-composition.py docs/modules/<module>/spec.yml --depth 2  # expand the leaves too
```

**Diagrams on module pages render at depth 1.** Anything you can obtain is a leaf; only what the module builds on the way to its own result is expanded. Base Cytosol is a leaf for the same reason S30 Lysate is — it is a thing you can have, and its own page says how. Having a page is *not* the test: `aTc Sensor Cytosol` has a page and is still expanded on the cascade that builds it. Deeper renders are for review material, never for a docs page. A module whose composition is a single box gets no diagram at all.

**The composition steps are `process_steps:`** (Jon, 2026-09-15). Each entry applies one Process
to named operands and yields a named product — *"`step` isn't the right language. These are
Processes, are they not?"* Two entries may name the same Process, so an entry is an application of
one, not the Process itself.

**An input or a step may be `optional: true`,** and an input may carry a `range:` where one figure
would be wrong. **Skipping an optional step rewires rather than removes**: whatever consumed its
product consumes its operands instead. `check-composition.py` reports where that cannot work — a
`packing` consumer expected one bounded thing and would get several loose ones. It reports rather
than blocks, because no source marks a step optional yet and a rule with no corpus behind it is a
rule nobody has tested.

**The schema is [`scripts/spec-yml-schema.yml`](scripts/spec-yml-schema.yml)**, with
`python3 scripts/check-spec-schema.py` to validate against it. A key the schema does not allow is
rejected, rather than merely being absent from a list — the key table this replaces was wrong
about four things within four days of being written, and did not carry `abstract:` or
`composed_of:` at all. The validator also checks what a schema cannot express: an operand naming
nothing, a duplicated product id, an `abstract:` naming no process, and a `page:` that does not
resolve.

**A number belongs in `spec.yml` when it states a fact no single constituent page can
state** (Jon, 2026-09-11). `headroom.provides` is a property of the Module that provides
the slot, not of the process that filled it, and not of any additive. A combining `ratio`
is a property of the step. An osmolarity that has to match across a membrane is a relation.
Those belong here.

**The test for a `parameters:` value, made operational 2026-09-15.** Delete it when the step names
an operand that **has a page of its own**, and that page states the figure. Keep it otherwise. The
audit that produced this rule removed three of thirteen values — `ulga` and `ulga_final`, both on
[`gel-ulga`](docs/modules/gel-ulga/spec.md), and `riboswitch`, on
[`detector-theophylline`](docs/modules/detector-theophylline/spec.md).

**The ten that stayed, stayed for two reasons, and neither is laziness.** Four are `osmolarity`, a
relation by the rule above. Six name an operand with **no page at all** — `agarose`, `hpts`,
`tris-hepes-stock` — so no constituent page can state them, and deleting would lose the figure.
**That `agarose` and HPTS have no module page is the finding**, not the duplication. `tris-hepes`
is the one to watch: `processes/assemble-outer-solution/main.md` states it, but a process page is
not a constituent page, so the rule leaves it in place.

**Read the comment before deleting the key it sits on.** `ulga_final` carried
`# in the set gel; 0.2-0.5% works` — a working range, not a restatement. It was safe to delete
only because `gel-ulga`'s own page says *"Works from 0.2% to 0.5% in the set gel"*. A first search
for that range missed it, because the page writes `0.2% to 0.5%` and the pattern allowed no `%`
between. **A search that finds nothing is not evidence; widen it before you act on it.**

**`# Constituent Modules` stays as prose and the yml is the contract for tooling** (Jon, 2026-09-09). Nothing makes the two agree, so `python3 scripts/check-composition.py` checks that they do not disagree. It blocks when the prose lists a module the source never names — the live failure was `london-cascade` claiming `Substrate: CPRG` where its source said `GUV: CPRG`, an hour after both existed — and reports without blocking when the final step has an operand the prose omits, which is a grain difference rather than an error.

Two generators currently read two different sources into the same markers; see issue #250 before running the other one.

### DNA reference checking

**Run `python3 scripts/check-dna-refs.py` before opening a PR if you added or edited a Designs table** (any table with a `Length (bp)` / construct-name row linking into `nucleus-eng/DNA`). This is a different failure mode than link checking: a link can 404-free and still assert the wrong sequence — the motivating case was `reporter-degfp/spec.md` claiming 2789 bp for a construct that is actually 2812 bp after a correction in the DNA repo. `check-links.py` cannot see that; this script diffs the docs' bp claim against the target file's GenBank `LOCUS` line.

```bash
python3 scripts/check-dna-refs.py                       # all of docs/
python3 scripts/check-dna-refs.py docs/modules/<module>/ # one module
```

Local-only — not run in CI, since CI has no DNA-repo checkout. Three levels: **blocking** (wrong bp, missing file, or a link into the legacy `bnext-bio/nucleus` repo — real errors), **warn** (construct name doesn't obviously relate to the target's `LOCUS` name or filename — often a benign alias, but exactly the shape of a greedy link, so confirm it's intentional before dismissing), **info** (nothing to verify — a `.dna` SnapGene file with no parseable length, or a row with no bp cell). It checks length, not sequence — a same-length, different-sequence swap is not detectable by this tool, and that blind spot is live: PLA1 is realized as two 963 bp coding sequences that differ at 77.6% nucleotide identity and encode the same protein.

**It also flags stale absence claims — a page asserting a construct is *not* in `nucleus-eng/DNA` when a file of that name now is.** This is a second failure mode with the same cause as the first: the DNA repo moves independently, and nothing here watches it. Every other check in this script validates rows that *cite* a file, so a hook claiming absence was invisible to all of them — six such claims sat wrong for twelve days after `nucleus-eng/DNA` landed the constructs they said were missing.

**It reports a finding, never a fix.** The message is *"a file of that name exists — verify it is the same construct"*, and it must stay that way. A filename match is not an identity claim: `LuxR-PLA1-linear.gb` (2237 bp) and `pOpen-LuxR-PLA1.gb` (4175 bp) share a cassette, differ by a whole backbone, and are not interchangeable — the linear form is for Base Cytosol, the circular one for S30, which degrades linear DNA. A check that said "closeable" here would automate the exact greedy-linking mistake it exists to catch. `tests/test_stale_absence_claims.py` pins that wording.

It finds the DNA repo at `$NUCLEUS_DNA_REPO`, else beside this repo, else `~/src/nucleus-eng/DNA`, and accepts a candidate only if it actually contains sequence files — an empty directory named `DNA` would otherwise satisfy the search and produce a clean run over an index of nothing. It exits 2 and lists what it searched when it finds none, so a missing checkout never reads as a pass.

### Pull request workflow

When merging a PR via `gh pr merge`, never use `--admin` to bypass branch protection rules. If a merge fails due to branch policy, stop and ask the developer how to proceed — options are leaving the PR open for a reviewer, asking the developer to approve it themselves, or using `--auto` to merge once requirements are met.
