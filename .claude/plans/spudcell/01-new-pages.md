# Plan 1 — New pages (migrate technical, you write humanistic)

**Goal.** Resolve the SpudCell-spec TODOs that are really "a page that doesn't exist yet." For each, we build a shared template that separates **technical slots** (I migrate from your notes + protobiology.org) from **humanistic slots** (you write). This plan covers the *page inventory*, the *template*, the *migration workflow*, and the *wiring* (TOC + index).

Source of the split: your own `Jon's Notes on Module Specs.md` — a spec captures **Technical Details** (composition, conditions, part numbers, expected behavior) *and* **Humanistic Information** (contextual, operational, empathetic). I fill the former; you own the latter.

---

## A. Page inventory

Every "(TODO link)" in `spudcell-spec.md` points at one of these. Classified as **process** (step-by-step protocol, `docs/processes/<slug>/main.md`) or **module** (spec, `docs/modules/<slug>/spec.md`).

| # | Page | Type | Resolves spec TODO(s) | Primary source(s) |
| --- | --- | --- | --- | --- |
| P1 | **Encapsulation: Mechanical Extrusion** | process | L164 "Assembly and encapsulation… (TODO link)" | Notes-SpudCell §"Liposome Size Control (Extrusion Parameters)" (2 µm cell / 0.8 µm DLS / 0.4 µm feeder); protobiology "Encapsulation method" |
| P2 | **Synthetic Cell Cycle: Growth & Division** | process | L14 process link; L12 "growth module (TODO)" + "cell division module (TODO)"; L150 "Feeding (TODO link)"; L165 dangling "see " | Notes-SpudCell §"Growth and division system", §"Feeding", §(4); protobiology "Synthetic Cell Cycle with Feeder Liposome Growth and Mechanical Division" |
| P3 | **Feeder Liposome Prep & Fusion / FRET assay** | process | L150 feeding link (shared with P2); L63 azido/immobilization ("Methods §20") | Notes-SpudCell §"Feeding", §"Liposome Fusion Experiments", §"FRET…"; feeder-cell-spec.md already exists as the *module* side |
| P4 | **(decision) Growth module + Division module as specs?** | module ×2 | L12 the two "module (TODO)" parentheticals — *if* you want them as first-class modules rather than sections of P2 | Notes-SpudCell §(3),(4); membrane-pore-ahly/spec.md is the reusable aHL base to extend |

### Open decisions (yours — I'll build to whichever you pick)
1. **Do "growth module" and "division module" become module specs (P4), or just anchor into the P2 process page?** Your Module-Specs notes lean toward modules-as-first-class (`Encapsulation: Mechanical Extrusion :> Encapsulation`), which argues for P4. But feeding/division may read better as one process. **Recommend:** P2 as the process + the growth/division *mechanisms* documented in `spudcell-spec.md`'s existing Expected Behavior section; only spin out P4 module specs if another cell will reuse them. Defer.
2. **Is P3 separate from P2, or one big "cell cycle" process with sub-protocols?** Adamala's site splits them (Feeder Prep, Fusion, FRET, Cell Cycle are distinct protocols). **Recommend:** mirror that — P3 (+ FRET as a sub-page) feeds into P2. Defer.
3. **`Encapsulation: Mechanical Extrusion` vs `: Phase Transfer`** — your notes flag both (mechanical extrusion for SpudCell; emulsion phase transfer / inverted emulsion is the other lineage). P1 is only the extrusion one; note the sibling exists but is out of scope here.

---

## B. The template (build together, once)

One annotated skeleton per type, extending the existing `templates/process-template/` and `templates/module-template/`. Each section tagged:

- **`[TECH]`** — I migrate verbatim-faithful technical content from notes/protobiology/manuscript. Tables, concentrations, catalog numbers, extrusion sizes, reaction conditions, construct refs, quantitative expected behavior.
- **`[HUMAN]`** — you write. Overview framing, *why this matters*, design rationale, operational gotchas ("eater liposomes are limiting → every hungry mouth gets fed"), narrative, credits.
- **`[BOTH]`** — I draft the skeleton/data, you add the judgment.

Proposed process-page section map:
```
title (frontmatter)                      [TECH]
# Overview                               [HUMAN]  ← the contextual/empathetic layer
  :::{card} Important Information         [BOTH]
    Notes / Prereqs / Hazards /          [HUMAN notes, TECH materials]
    Critical Materials / GECs /
    Composition / References
# Protocol (## steps, - [ ] checkboxes)  [TECH]   ← operational, migrated from protobiology
  :::{hint} extended notes               [HUMAN]
# Downloads (PDF + BOM cards)            [TECH]
```

**Deliverable of step B:** `templates/spudcell-migration/process.md` + `.../module.md` (annotated). *Question for you:* keep these throwaway (delete after migration) or contribute them as reusable annotated templates? Leaning throwaway → put them under `.claude/plans/spudcell/templates/` so they don't ship.

---

## C. Migration workflow (per page)

For each page P1–P3, in order:

1. **Assemble sources.** Pull the matching section from `Jon's Notes on SpudCell.md` + fetch the corresponding protobiology.org/spudcell.php protocol (WebFetch). Note which numbers are still missing → hand to **Plan 2** (manuscript).
2. **I draft `[TECH]` slots.** Materials tables as inline `bom-<slug>` tables (per `build-boms` skill + migrate-content rules: 0-indent tables, `MW (g/mol)` paren units, DOI citations as full links, discrepancy `:::{warning}` blocks).
3. **Cross-repo DNA check.** Use **Plan 2, section D** (the construct-by-construct verification table) as the source of truth for which constructs are in `nucleus-eng/DNA` and which need an `:::{attention}` gap block — don't re-derive this per page.
4. **You fill `[HUMAN]` slots.** I leave `<!-- HUMAN: ... -->` prompts at each.
5. **Wire it in** (see D).
6. **QA** — Plan 3's gauntlet, scoped to the new file.

**Dependency:** P2/P3 feeding & genome numbers partly blocked on **Plan 2**. P1 (extrusion) is fully covered by notes → do P1 first as the template shakedown.

---

## D. Wiring each new page (don't forget)

Per CLAUDE.md, a new page is never just the file:

- **Process page:** add to `myst.yml` under `docs/processes/…` (`hidden: true` if a child); it appears via `processes-main.md`.
- **Module spec (if P4):** *two* TOC updates — `myst.yml` entry **and** a row in `docs/modules/modules-main.md` (`Class | Spec | Validation ★`). SpudCell modules would be ★ (preliminary / preprint-only).
- **Back-links:** replace the `(TODO link)` in `spudcell-spec.md` with the real relative `.md` link (never `.html`).
- **File placement:** all under `docs/processes/<slug>/` or `docs/modules/<slug>/`; BOMs/images in `resources/`.

---

## E. Suggested order

1. Build template (B) — quick, unblocks everything.
2. **P1 Encapsulation: Mechanical Extrusion** — fully sourced from notes; proves the workflow end-to-end.
3. **P3 Feeder prep / fusion / FRET** — mostly in notes; a few numbers → Plan 2.
4. **P2 Synthetic Cell Cycle** — composes P1+P3; needs Plan 2 for genome/retention data.
5. Revisit decision on **P4** modules once P2 exists.
