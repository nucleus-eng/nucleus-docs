---
title: "ULGA Hydrogel Embedding"
subtitle: "Process"
status: draft  # draft | unvalidated-published | validated-published — see CLAUDE.md "Page status"
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

ULGA Hydrogel Embedding immobilizes GUV-encapsulated London Sensing Cells in a gel matrix made from ultra-low-gelling-temperature agarose (ULGA), so that a downstream colorimetric or fluorescent readout can be measured in place rather than in free solution. In the London quorum-sensing demo, POPC GUVs carrying the AHL Sensing Module (S30 Lysate plus the `pLux-GFP` sensor plasmid) are dispersed into a ULGA solution before it gels, holding the sensing GUVs fixed while AHL from an external bacterial source diffuses in through the gel and triggers a response.

In the process-dependency diagram, ULGA Hydrogel Embedding is fed only by GUV Encapsulation and feeds only into Colorimetric Readout. This differs from Alginate Hydrogel Embedding, which is fed by both GUV Encapsulation and SUV Encapsulation — this process uses GUVs alone, with no SUV input. GUV Encapsulation and Colorimetric Readout are being authored as separate process pages in parallel with this one; this page does not link to them until they exist, and refers to them by name only.

:::{note}
**Source of this page.** Protocol details below are cited from `Demo Status - London.docx`, Module 4 ("ULGA embedding," contributor Julia Purrinos De Oliveira) and Module 6 ("PLA1-based color change module," contributors Jonah McDonald and Charlie Newell). The backing devnote, `devnotes/london-quorum-sensing-polymersome/main.md`, is confirmed still a template stub — milestones and risk framing only, no primary experiments, figures, or data — so it is not cited as a completed source anywhere on this page. Z-stack images referenced in Module 4's key results were not independently located as primary data during authoring; this is flagged again below rather than treated as independently verified.
:::

:::{attention} Acronym expansion
Source material is inconsistent about the acronym: the Module 4 overview text writes "ultra low gelling agarose (ULGA)," while its own Materials table gives the product name as "Ultra low gelling temperature agarose." This page uses **ultra-low-gelling-temperature agarose (ULGA)**, matching the fuller product-name form and the usage already established on the [AHL Sensing Cell](../../modules/ahl-sensing-cell/spec.md) and [London Chassis](../../modules/london-chassis/spec.md) spec pages.
:::

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Notes
:class: dropdown
:icon: false

- ULGA gels at (8-17)°C, well below the gelling temperature of standard agarose. Source material does not specify the exact dissolution or cooling temperatures used in this protocol; dissolving and cooling steps below follow standard low-melting-agarose handling and are flagged as inferred general technique, not values taken directly from the source.
- Two ULGA concentrations are documented for this process, from two distinct experiments: 1% ULGA for the GFP-readout demonstration (Module 4, confirmed by Z-stack imaging), and 1.5% ULGA for the PLA1/CPRG colorimetric two-vesicle demonstration (Module 6). Both use the same S30 Lysate-compatible outer solution base. Pick the concentration that matches the readout you are running; do not assume they are interchangeable without re-validation.
- Module 4 notes the protocol has so far been tested with liquid bacterial culture and supernatant, with a planned move to solid agar bacteria media not yet reported as complete.

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

**Hot ULGA solution** - Dissolving agarose requires heating near boiling. Handle hot glass vessels and solution with appropriate heat-resistant gloves; allow to cool before combining with heat-sensitive GUVs or lysate.

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::::{tab-set}

::::{tab-item} 1% ULGA (GFP readout)

:::{table} Outer solution used to embed AHL Sensing Cell GUVs for the GFP readout, ULGA at 1% final concentration (Module 4).
:label: comp-ulga-1pct

| Component | Concentration |
| --- | --- |
| Potassium L-glutamate | 578 mM |
| HEPES | 72 mM |
| Glucose | 300 mM |
| ULGA | 1% (w/v) |

:::

::::

::::{tab-item} 1.5% ULGA (colorimetric readout)

:::{table} Outer solution used for the S30 Lysate-encapsulated, PLA1/CPRG colorimetric two-vesicle demonstration, ULGA at 1.5% final concentration (Module 6).
:label: comp-ulga-1-5pct

| Component | Concentration |
| --- | --- |
| Potassium L-glutamate | 578 mM |
| HEPES (pH 7.4) | 72 mM |
| Glucose | 300 mM |
| AHL (3OC6-HSL, + condition only) | (5-10) µM |
| AHL-producing bacteria supernatant | 10:1 dilution (20 µL per 200 µL hydrogel) |
| ULGA | 1.5% (w/v) |

:::

This variant feeds the Colorimetric Readout process; see the [AHL Sensing Cell](../../modules/ahl-sensing-cell/spec.md) spec for the sensing GUV composition and the [PLA1 Lysis Module](../../modules/effector-pla1/spec.md) and [LacZ Reporter](../../modules/reporter-lacz/spec.md) specs for the downstream lysis and colorimetric chemistry — this process page covers embedding only, not the readout itself.

::::

:::::

::::::

:::::::

# Materials and Equipment

:::{table}
:label: bom-embed-ulga-hydrogel
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ULGA | Reagent | Ultra low gelling temperature agarose | Sigma-Aldrich | A5030 | £52.00 | RT | [link](https://www.sigmaaldrich.com/GB/en/product/sial/a5030) |
| RNase inhibitor | Reagent | Murine RNase Inhibitor | New England Biolabs | M0314S | £87.00 | -20 °C | [link](https://www.neb.com/en-gb/products/m0314-rnase-inhibitor-murine) |
| Potassium L-glutamate | Chemical | Potassium L-glutamate | — | — | — | RT | — |
| HEPES | Chemical | HEPES, free acid | — | — | — | RT | — |
| Glucose | Chemical | D-(+)-Glucose | — | — | — | RT | — |
| CPRG | Reagent | Chlorophenol red-β-D-galactopyranoside | Roche | 10884308001 | $160.00 | -20 °C, in water at 10 mg/mL | [link](https://www.sigmaaldrich.com/US/en/product/roche/10884308001) |

:::

:::{attention} Incomplete Materials table
Module 4's own Materials table in the source document lists Glucose, Potassium glutamate, and HEPES rows with no manufacturer, part number, price, or storage data filled in (marked only with a placeholder `#`) — this table carries that gap forward rather than inventing catalog details. Flag for follow-up before this page is used at the bench.
:::

# Protocol

## Prepare ULGA Outer Solution

- [ ] Prepare the base outer solution: (578 mM) potassium L-glutamate, (72 mM) HEPES, (300 mM) glucose in water.
- [ ] Dissolve ULGA into the base outer solution to a final concentration of 1% (w/v) for a GFP readout, or 1.5% (w/v) for a PLA1/CPRG colorimetric readout, by heating near boiling with stirring until fully dissolved.

:::{hint} Note
:class: simple
:icon: false
Source material does not specify an exact dissolution temperature or hold time. Standard low-melting-agarose technique is to heat until the solution runs clear, then hold above the gel point (above ~17 °C for ULGA) until combined with the GUV suspension, and only then cool below the gel point to set.
:::

- [ ] Cool the dissolved ULGA solution to a temperature that keeps it liquid (above its (8-17)°C gel point) but is safe to mix with GUVs without damaging them, before proceeding.

## Form Hydrogel-Embedded GUVs

- [ ] Combine the cooled, still-liquid ULGA solution with GUV Encapsulation output (e.g., AHL Sensing Cell POPC GUVs carrying `pLux-GFP` in S30 Lysate) to a total volume of 100 µL per reaction.
- [ ] Dispense the GUV/ULGA mixture into wells or onto a plate and allow the gel to set by cooling below the ULGA gel point.

## Add Bacterial Input

- [ ] Add 10 µL of one of the following on top of the set gel, per condition:
    - [ ] Overnight bacterial culture (AHL-producing).
    - [ ] Bacterial culture supernatant (AHL-producing, cell-free).
    - [ ] LB medium only (negative control).
- [ ] Include a positive control gel using a constitutively expressed GFP construct (not the AHL-gated sensor) to confirm the encapsulated lysate is expressing independent of AHL exposure.
- [ ] Incubate 2.5 h.

## Confirm Embedding

- [ ] Image the gel by fluorescence microscopy, collecting a Z-stack to confirm GFP signal is associated with intact, embedded GUVs rather than background.
- [ ] Compare against the LB-only negative control at matched optical and contrast settings.

:::{attention} Primary data not located
Module 4 reports GFP signal in both the overnight-culture and supernatant conditions after 2.5 h, with no signal in the LB control at matched settings, "confirmed with Z-stack images." The referenced Z-stack image files were not independently located as a primary dataset during authoring of this page — this result is cited from the status-document summary only, not independently re-verified here.
:::

# Downloads

::::{grid} 1 1 1 1

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/embed-ulga-hydrogel-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/embed-ulga-hydrogel-bom.pdf>`
:::

::::
