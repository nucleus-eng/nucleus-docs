# Plan 3 — Formatting & structural cleanup of `spudcell-spec.md`

**Goal.** Fix the *structural* defects on the page — broken fences, dead cross-refs, unit/style violations — that are independent of the content TODOs. These I can do without new pages or manuscript data (a few are gated on Plans 1–2 and are marked). Line numbers reference the `spudcell` branch version.

---

## A. Broken MyST / rendering (fix first — these break the build or render wrong)

| # | Line | Defect | Fix |
| --- | --- | --- | --- |
| F1 | 147 | Attention block closes with `::` instead of `:::` | Change `::` → `:::` |
| F2 | 145–146 | Text says "**five** of seven" then lists **six** names (`pLD1, pLD2, pLD3, pREP, aHL-6xHis, aHL-FLAG`) — and the two "matching" (`FP`, `T7RNAP`) make 8 total vs "seven plasmids" | Recount vs Plan 2 M1/M2; fix the count + list (content-adjacent — confirm the real plasmid set) |
| F3 | 67 | Two broken links: `[Synthetic Cell Media]` (reference-style link with no definition → renders literally) and `[SpudCell Cytosol](#Cytosol Competition)` (anchor has a space **and** wrong name — section is "Cytosol Composition", not "Competition"). Sentence also missing terminal period | Point first link to `./synthetic-cell-media-spec.md`; fix anchor to the real heading slug (`#cytosol-composition`); add period |
| F4 | 50–51 | `See {ref}…` caption line sits *inside* the table fence after the rows — verify it renders as caption vs. leaks into the table | Move below `:::` or confirm intended |

## B. Unit / style (Vale + codespell will flag)

| # | Line | Defect | Fix |
| --- | --- | --- | --- |
| F5 | 73 | Table title "per 30 uL prep" — ASCII `u` | `µL` (nucleus.micro-symbol) |
| F6 | 64 | "Fluorescent **labelled** lipids" — British | `labeled` (codespell en-GB→en-US) |
| F7 | 132–139 | **Unit inconsistency** in genome table: lengths in **kb** (30.1) but `FP` row shows `2,500` (bp) | Normalize — either kb throughout (`2.5`) or add a unit column. Coordinate w/ Plan 2 M1 |
| F8 | 12 | Double space: "90.3 kb,  seven" | single space |
| F9 | 15–16 | Double blank line | single |

> Run Vale/codespell to catch the rest — spot-checks only above. Watch for other `um`/`uL`/`uM` (notes use ASCII `u` heavily; some may have been pasted in), and ion/chemical notation if any crept in.

## C. Empty-column / table-shape decisions (yours)

| # | Line | Issue | Decision needed |
| --- | --- | --- | --- |
| F10 | 44 | Base-bilayer table has empty `TODO: links` column (all rows blank) | Fill catalog links or **drop the column**? |
| F11 | 93 | Cytosol table has **two** TODO header cells (`Notes TODO…`, `TODO: part numbers…`) with fully empty columns | Part-# column is Plan 2 (M5); the *Notes* column already has content mid-table — clean the header. Decide final column set |

## D. Gated on other plans (don't fix in isolation)

- **L162–165 "Protocols" section** — L165 dangling "see " and L164 "(TODO link)". Structural fix = insert the real links, but the *targets don't exist yet* → resolved by **Plan 1** (P1/P2). Leave a single `<!-- TODO: link after Plan 1 -->` for now rather than a half-sentence.
- **L25 / L154 figure placeholders** — **Plan 2** M9 (sourcing/license) + possible BioRender build. Per CLAUDE.md, mechanism schematic belongs in Overview (✓ L25), system-in-context figure belongs in a `## Cells` section (none exists yet — flag if we add one).

## E. QA gauntlet (run before PR; scope to this file where possible)

```bash
conda run -n nucleus-docs myst build --html          # confirm ONE bibliography block renders
python3 scripts/check-dropdowns.py                    # placeholder-only lists (spec TODOs are inline/table, likely OK — confirm)
python3 scripts/check-formatting.py docs/modules/spudcell/spudcell-spec.md
python3 scripts/check-toc.py
vale docs/modules/spudcell/spudcell-spec.md
codespell docs/modules/spudcell/spudcell-spec.md
python3 scripts/check-links.py docs/modules/spudcell/spudcell-spec.md   # after F3 link fixes
```

**Order:** A (rendering) → B (units) → C (decide w/ you) → E (verify) → D last (unblocked by Plans 1–2).
