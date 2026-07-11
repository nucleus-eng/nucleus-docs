# Plan 2 — Manuscript deep dive (fill the numbers the notes don't have)

**Goal.** Close the *quantitative* TODOs in `spudcell-spec.md` that are not answerable from your notes and require the actual preprint + Methods + SI. Output is a **structured extraction table** you review — per the collaboration model, domain values are a hard-gate: I extract + cite, you confirm before they land.

**Primary sources**
- Preprint DOI `10.64898/2026.07.01.735724` (SpudCell / Adamala + Engelhart).
- Protocols: `protobiology.org/spudcell.php` (protocol PDFs — the notes say the FRET assay and media are "fully expounded" here vs. terse in the paper).
- Your notes already resolve a *surprising* amount — cross-check, don't re-derive.

---

## A. Extraction targets (mapped to spec location)

| # | Spec location | What's missing | Where in paper | In notes already? |
| --- | --- | --- | --- | --- |
| M1 | Genome L120, table L132–139 | Total genome kb (confirm 90.3); **7 plasmid lengths** (only pLD1 = 30.1 kb, FP ≈ 2.5 kb known) | SI genome maps / plasmid table | pLD1 = 30.1 kb (~11 genes); FP = 2.5 kb (1 gene). Rest **TODO** |
| M2 | Genome table L132–134 "which" | **Which PURE genes on pLD1 / pLD2 / pLD3** (30 of 36 split across three) | SI construct maps | "pLD1–pLD3 encode 30 of 36; T7RNAP separate; missing = AK, CK, NDK, PPiase". Per-plasmid split **TODO** |
| M3 | Expected Behavior L154 / retention | Per-plasmid retention values | Fig 3o (30% retain all 7), Fig 3p (50% pLD1 → 70% aHL) | **Yes** — in notes; just needs transcription + fig citation |
| M4 | Membrane table L49, functional L63 | **Azido lipid catalog/vendor** + stock conc + per-rxn volume | Methods §20 | "1 mol%, Methods §20" — **no catalog**. Biotin-NTA = VWR 90074 known |
| M5 | Cytosol table L93 (empty part-# column) | Part numbers for HEPES, K-glutamate, Mg-glutamate, spermidine, creatine-P, folinic acid, AAs, rNTPs, dNTPs, DTT, PMix, tRNA, ribosomes | Methods §2 / reagents table | Phi29 = **Lucigen 30221-2** (known); NEB Sol B 60% v/v noted. Rest **TODO** |
| M6 | Functional membrane L61–62 | aHL-6xHis / aHL-FLAG expression details; DNA vs protein; confirm 10 nM template | Methods (fusion tags) | aHL-FLAG 10 nM confirmed; sequences flagged as your own "JON TODO" |
| M7 | Gen counter L116 | Top-strand (parent) / bottom-strand (feeder) delivery **method**; ligation chemistry | Methods §12 | Substantial: dsRNA oligos, T4 RNA/DNA ligase, 1 nM each, gen ≥ 3 readout, full energy-mix recipe. Confirm §12 details |
| M8 | Cytosol "estimated" caveat L18, table L90 | Validate the **estimated** pREP concentrations vs. Methods §2 (remove "estimated" where confirmed) | Methods §2 + §13 media | Full estimated table in notes w/ the "Sol A = SMix" caveat (folinic acid †, DTT-for-TCEP). Needs paper confirmation |
| M9 | Overview L25 + Behavior L154 | **Figures** — mechanism schematic (may build in BioRender) + a behavior/result figure | Figs 2, 3, 6 | none — need figure sourcing + **license check** |

---

## B. Method

1. **Fetch** the preprint (WebFetch on the DOI landing page → PDF) and the protobiology protocol index. If the PDF isn't machine-readable, note it and fall back to the protocol pages, which your notes say are more complete anyway.
2. **Extract into one table** keyed by the M# above: `value | unit | source (fig/§) | confidence | conflicts-with-notes?`.
3. **Discrepancy flag** (migrate-content rule): where the paper disagrees with your notes or the current spec (e.g. "31 of 36" vs "30 of 36 + T7RNAP" vs spec's "pLD1–pLD3 encode 30 of 36"; genome "90 kb" vs "90.3 kb"; SpudCell.md's "34/38 genes" — a *third* number), surface all values side by side, don't silently pick one.
4. **License gate for figures (M9).** Before reusing any paper figure, confirm the preprint license (CC-BY?). If not reusable, plan an original BioRender schematic instead (the mechanism schematic at L25 is ours to draw regardless). Do not commit vendor/paper PDFs (CLAUDE.md).
5. **Hand back** the table for your confirmation; only then do I write values into the spec / new pages.

---

## C. Known conflicts to resolve first (don't paper over)

- **Gene count:** spec "seven plasmids / 30 of 36" · Notes "31 of 36 (−EF-Tu −metabolism)" · SpudCell.md "34/38 genes" · outline "30 of 36 PURE + T7RNAP." Pin the exact denominator (36 vs 38) and numerator against the SI.
- **Genome size:** 90 kb vs 90.3 kb — trivial but pick the cited one.
- **aHL division linker:** Notes §(4) prose says "aHL-6xHis → Ni-NTA-biotin → streptavidin" in one place but the growth+division demo uses "aHL-FLAG → biotin-antiFLAG → streptavidin." Spec uses aHL-FLAG. Confirm which pore carries which linker in the division regime (this is a real mechanism ambiguity, not just wording).
- **"estimated" cytosol:** decide per-row whether the paper confirms it (drop "est.") or not (keep + caveat).

---

## D. Deliverable

`.claude/plans/spudcell/extraction.md` — the filled table + citations + flagged conflicts, ready for your sign-off. Feeds Plan 1 (P2/P3 numbers) and Plan 3 (genome-table unit normalization).
