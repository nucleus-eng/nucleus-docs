---
title: "Colorimetric Readout"
subtitle: "Process"
status: draft  # draft | unvalidated-published | validated-published — see CLAUDE.md "Page status"
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

Colorimetric Readout converts a completed sensing/lysis cascade into a visible, measurable color signal. A chromogenic substrate — chlorophenol red-β-D-galactopyranoside (CPRG) or, in an alternate chemistry, catechol — is hydrolyzed by a reporter enzyme (β-galactosidase, LacZ, or catechol 2,3-dioxygenase, XylE/C23DO) that has been released or exposed by upstream lysis. This page covers the readout step itself: the substrate/enzyme chemistry, the absorbance wavelengths used to read it, and the plate-reader and visual-scoring protocols used across the DevCells cascades. It does not repeat each cascade's own sensing mechanism, encapsulation format, or quantitative result — those are documented on the Module pages that feed into this process and are cited below rather than duplicated.

This is the shared downstream step for both the Chicago and London programs: every sensing cascade in `docs/modules/` that produces a visible signal (theophylline, pH, aTc, and AHL sensing) ends at this same LacZ/CPRG (or XylE/catechol) chemistry, regardless of which upstream sensor or hydrogel format feeds it.

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{attention} Upstream hydrogel status is not uniform — read the diagram precisely
:class: dropdown
:icon: false

The process-dependency diagram draws two edges into this process, with different confirmation status, and they should not be treated as equally solid:

- **ULGA Hydrogel Embedding → Colorimetric Readout is solid (confirmed).** The London ULGA-embedded PLA1/CPRG color-change module shows a clear color change observed after 16 h, reproduced across multiple days and repeats.
- **Photopatterning, PEGDA → Colorimetric Readout is dashed (proposed, not yet demonstrated).** Chicago's PEGDA-patterned hydrogel work (Module 4, PHD) has confirmed photopatterning feature-size control and PEGDA-frame/alginate-core structural integrity, but explicitly caveats that "DevCell component volumes are currently too small to produce macroscopically visible QR code changes" — a functional colorimetric readout from a PEGDA-patterned hydrogel has not been shown.

The diagram does **not** draw a direct edge from Alginate Hydrogel Embedding to this process — alginate embedding feeds into PEGDA patterning (Alginate → PEGDA is itself solid/confirmed), not directly into Colorimetric Readout. The unpatterned alginate-embedded readout ([Theophylline Sensing Cell](../../modules/theophylline-sensing-cell/spec.md) + [CPRG-loaded SUV](../encapsulate-suv/main.md) + LacZ in ~1% alginate, ~16 h color change, Chicago Overview) is a real, separately confirmed result, but it is not represented as its own edge into this node in the current diagram.

::::::

::::::{note} PEG-norbornene requires a different loading order
:class: dropdown
:icon: false

CPRG pre-loaded into liposomes photobleaches under the UV exposure used to crosslink PEG-norbornene (PEG4Nb) hydrogels. This does not affect agarose, alginate, or ULGA embedding, where CPRG is pre-loaded into liposomes as usual. For PEG-norbornene, add CPRG as a free dye *after* UV crosslinking, and pre-add LacZ to the gel rather than encapsulating it — see the [LacZ Reporter Module](../../modules/reporter-lacz/spec.md#requirements) Requirements section for the confirmed four-condition comparison behind this workaround. PEG-norbornene has no node yet in the process-dependency diagram; this note is included here because it directly affects how this readout process is run in that hydrogel chemistry.

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

**Catechol** — irritant, toxic if absorbed through skin; handle with gloves and avoid skin contact. Only relevant if using the XylE/C23DO alternate chemistry below.

::::::

:::::::

# Substrate and Reporter Chemistry

## Primary chemistry: LacZ / CPRG

CPRG (chlorophenol red-β-D-galactopyranoside, Roche 10884308001) is a yellow compound that β-galactosidase (LacZ) hydrolyzes into chlorophenol red (CPR), a magenta/purple product. The reaction is read by absorbance near 570 nm to 575 nm, or by eye. This is the chemistry used across all confirmed and in-progress DevCells cascades — see the [LacZ Reporter Module](../../modules/reporter-lacz/spec.md) spec for substrate handling, the [PLA1 Lysis Module](../../modules/effector-pla1/spec.md) spec for how lysis releases CPRG or exposes it to LacZ, and the individual sensing-cascade pages ([Theophylline Sensing Cell](../../modules/theophylline-sensing-cell/spec.md), [pH Sensing Cell](../../modules/ph-sensing-cell/spec.md), [aTc Sensing Cell](../../modules/atc-sensing-cell/spec.md), [London Cascade](../../modules/london-cascade/spec.md)) for each cascade's own quantitative result. This page does not duplicate those data tables.

## Alternate chemistry: XylE / catechol

Catechol 2,3-dioxygenase (C23DO, the *xylE* gene product) oxidizes colorless catechol into 2-hydroxymuconate semialdehyde, a yellow ring-fission product read by absorbance near 375 nm to 385 nm ([Kunz and Chapman, 1981](https://doi.org/10.1128/jb.146.1.179-191.1981)). This is documented as an orthogonal reporter chemistry for the Chicago node, alongside LacZ/CPRG, intended to give a second colorimetric channel for multiplexed sensing. As of this writing it is confirmed only at bulk-cytosol scale — no synthetic cell/liposome-encapsulated or hydrogel-embedded XylE result exists — and it is not the chemistry used in any confirmed cascade result to date (the confirmed aTc Cascade dose-response uses the LacZ leg, not XylE). See the [XylE / C23DO Reporter Module](../../modules/reporter-xyle/spec.md) spec for the bulk-cytosol reaction composition and result; do not read this alternate chemistry as being at the same readiness level as LacZ/CPRG.

# Materials and Equipment

:::{table} Bill of Materials
:label: bom-colorimetric-readout

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| ---- | -------- | ------- | ------------ | ------ | ----- | ------- | ---- |
| CPRG | Reagent | Chlorophenol red-β-D-galactopyranoside | Roche | 10884308001 | $160.00 | -20 °C, in water at 10 mg/mL to 20 mg/mL | [link](https://www.sigmaaldrich.com/US/en/product/roche/10884308001) |
| Catechol | Reagent | Catechol, 99% | TCI America | P0317 | $45.00 | RT, protect from light | [link](https://www.tcichemicals.com/US/en/p/P0317) |
| β-galactosidase (LacZ), exogenous | Reagent | β-Galactosidase from *E. coli* | Sigma-Aldrich | G6008 | $95.00 | -20 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/g6008) |
| 96-well clear-bottom plate | Consumable | Corning 96-well clear flat-bottom polystyrene microplate | Corning | 3585 | $45.00 | RT | [link](https://www.sigmaaldrich.com/US/en/product/corning/cls3585) |
| 384-well glass bottom plate | Consumable | 384 well glass bottom plate, 1.5 cover glass (20/case) | Cellvis | P384-1.5H-N | $423.00 | RT | [link](https://www.cellvis.com/_384-well-glass-bottom-plate-with-high-performance-number-1.5-cover-glass_/product_detail.php?product_id=53) |
| Plate reader | Equipment | Absorbance-capable microplate reader (e.g., BioTek Synergy or equivalent) | — | — | — | RT | — |
:::

# Protocol

## Prepare exogenous LacZ solution (if not co-encapsulated)

Some cascades co-encapsulate LacZ inside the same synthetic cell as the sensing and lysis constructs (e.g., the confirmed aTc Cascade result); others rely on an external LacZ solution that lysed liposomes release their substrate into (e.g., the alginate-embedded theophylline cascade, the London two-liposome cascade). Only run this step for the latter case.

- [ ] Prepare β-galactosidase stock in reaction buffer at the concentration specified by the cascade's Module page.
- [ ] Add the LacZ solution to the exterior (hydrogel matrix or well) alongside or before the sensing/lysis liposomes, per that cascade's own protocol.

## Plate-reader absorbance protocol

- [ ] Load the completed reaction (solution, hydrogel, or embedded format) into a clear-bottom or glass-bottom plate. Use a 96-well plate for bulk/hydrogel-in-well formats or a 384-well glass-bottom plate for imaged liposome/hydrogel preparations.
- [ ] Set the plate reader to read absorbance at 570 nm to 575 nm (LacZ/CPRG) or 375 nm to 385 nm (XylE/catechol), matching the chemistry in use.
- [ ] Incubate at 37 °C and take kinetic reads over the timescale established for that cascade — reported response times across cascades range from about 3 h (constitutive PLA1/CPRG, no sensing gate) to about 16 h (theophylline and ULGA-embedded AHL cascades) and up to several hours for solution-phase pH sensing. Do not assume a single fixed read window applies to every cascade; check the specific Module page.
- [ ] Include the controls specified by that cascade's own protocol (e.g., minus-inducer, minus-DNA, Triton X-100 positive lysis control) in the same plate read.

## Endpoint visual scoring

For formats read by eye rather than by plate reader (e.g., a hydrogel photographed at fixed timepoints):

- [ ] Photograph the reaction at the timepoints specified by the cascade's protocol under consistent, diffuse lighting against a white background.
- [ ] Score color qualitatively: LacZ/CPRG reactions progress from yellow toward pink/magenta/purple; XylE/catechol reactions progress from colorless toward yellow.
- [ ] Where a quantitative comparison is needed, follow up with the plate-reader protocol above rather than relying on visual scoring alone — several cascades (pH sensing, London AHL) report visually subtle ("slight pink," "temperamental") signals that are easier to distinguish by absorbance than by eye.

# Quality Control

A positive color change alone does not confirm specific detection — several cascades that use this readout process report background or leak issues that affect interpretation, and this page's readout chemistry cannot distinguish specific signal from these known confounds on its own:

- The Chicago theophylline cascade shows the same ~16 h color change with or without theophylline present (riboswitch leak) — see the [Theophylline Sensing Cell](../../modules/theophylline-sensing-cell/spec.md) spec.
- The London AHL cascade shows only a slightly discernible, "temperamental" difference between +AHL and −AHL conditions, with inconsistent liposome rupture reported across repeats — see the [London Cascade](../../modules/london-cascade/spec.md) spec.
- The pH-sensing bulk hydrogel result shows a real but modest absorbance gap (Abs₅₇₀ ≈0.31 at pH 7.4 vs. ≈0.39 at pH 6.5, against a ≈0.46 positive control) — see the [pH-Sensing Module](../../modules/detector-ph/spec.md) spec.

Always include the negative/uninduced control specified by the cascade's own Module page alongside the induced condition in the same read, and treat this process's absorbance values as relative to that same-plate control rather than against an absolute threshold.

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/colorimetric-readout-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/colorimetric-readout-bom.pdf>`
:::

::::
