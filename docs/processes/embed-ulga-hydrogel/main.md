---
title: "ULGA Hydrogel Embedding"
subtitle: "Process"
status: draft
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

ULGA Hydrogel Embedding immobilizes synthetic-cell-encapsulated London Sensing Cells in a gel matrix made from ultra-low-gelling-temperature agarose (ULGA), so that a downstream colorimetric or fluorescent readout can be measured in place rather than in free solution. In the London quorum-sensing demo, POPC synthetic cells carrying the AHL Sensing Module (S30 Lysate plus the `LuxR-deGFP` sensor plasmid) are dispersed into a ULGA solution before it gels, holding the sensing synthetic cells fixed while AHL from an external bacterial source diffuses in through the gel and triggers a response.

In the process-dependency diagram, ULGA Hydrogel Embedding is fed only by [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) and feeds only into [Colorimetric Readout](../colorimetric-readout/main.md). This differs from [Alginate Hydrogel Embedding](../embed-alginate-hydrogel/main.md), which is fed by both phase transfer and [SUV Encapsulation](../encapsulate-suv/main.md) — this process uses synthetic cells alone, with no SUV input.

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Notes
:class: dropdown
:icon: false

- ULGA gels at (8-17)°C, well below the gelling temperature of standard agarose. The exact dissolution and cooling temperatures for this protocol are not established; the dissolving and cooling steps below follow standard low-melting-agarose handling as a general technique, not values confirmed for this specific preparation.
- Two ULGA concentrations are documented for this process, from two distinct experiments: 1% ULGA for the GFP-readout demonstration (confirmed by Z-stack imaging), and 1.5% ULGA for the PLA1/CPRG colorimetric two-liposome demonstration. Both use the same S30 Lysate-compatible outer solution base. Pick the concentration that matches the readout you are running; do not assume they are interchangeable without re-validation.
- This protocol has so far been tested with liquid bacterial culture and supernatant; testing with solid agar bacterial media has not yet been completed.

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

**Hot ULGA solution** - Dissolving agarose requires heating near boiling. Handle hot glass vessels and solution with appropriate heat-resistant gloves; allow to cool before combining with heat-sensitive synthetic cells or lysate.

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::::{tab-set}

::::{tab-item} 1% ULGA (GFP readout)

:::{table} Outer solution used to embed AHL Sensing Cell synthetic cells for the GFP readout, ULGA at 1% final concentration.
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

:::{table} Outer solution used for the S30 Lysate-encapsulated, PLA1/CPRG colorimetric two-liposome demonstration, ULGA at 1.5% final concentration.
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

This variant feeds the Colorimetric Readout process; see the [AHL Sensing Cell](../../modules/ahl-sensing-cell/spec.md) spec for the sensing synthetic cell composition and the [PLA1 Lysis Module](../../modules/effector-pla1/spec.md) and [LacZ Reporter](../../modules/reporter-lacz/spec.md) specs for the downstream lysis and colorimetric chemistry — this process page covers embedding only, not the readout itself.

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
No manufacturer, part number, price or storage data is established for glucose, potassium L-glutamate or HEPES on this page. Nucleus buys all three elsewhere in this documentation — [D-(+)-Glucose, 99%](https://www.thermofisher.com/order/catalog/product/A16828.36) (Thermo Scientific A16828-36), [L-glutamic acid potassium monohydrate](https://www.sigmaaldrich.com/US/en/product/sigma/g1501) (Sigma-Aldrich G1501-100G) and [HEPES, crystalline powder, ≥99.5%](https://www.sigmaaldrich.com/US/en/product/sigma/h3375) (Sigma-Aldrich H3375-500G).

@Editor(london): confirm whether London uses these same three products before the rows above are filled in from them.
:::

# Protocol

## Prepare ULGA Outer Solution

- [ ] Prepare the base outer solution: (578 mM) potassium L-glutamate, (72 mM) HEPES, (300 mM) glucose in water.
- [ ] Dissolve ULGA into the base outer solution to a final concentration of 1% (w/v) for a GFP readout, or 1.5% (w/v) for a PLA1/CPRG colorimetric readout, by heating near boiling with stirring until fully dissolved.

:::{hint} Note
:class: simple
:icon: false
No exact dissolution temperature or hold time is established for this step. Standard low-melting-agarose technique is to heat until the solution runs clear, then hold above the gel point (above ~17 °C for ULGA) until combined with the synthetic cell suspension, and only then cool below the gel point to set.
:::

- [ ] Cool the dissolved ULGA solution to a temperature that keeps it liquid (above its (8-17)°C gel point) but is safe to mix with synthetic cells without damaging them, before proceeding.

## Form Hydrogel-Embedded synthetic cells

- [ ] Combine the cooled, still-liquid ULGA solution with phase-transfer synthetic cells (e.g., AHL Sensing Cell POPC synthetic cells carrying `LuxR-deGFP` in S30 Lysate) to a total volume of 100 µL per reaction.
- [ ] Dispense the synthetic cell/ULGA mixture into wells or onto a plate and allow the gel to set by cooling below the ULGA gel point.

## Add Bacterial Input

- [ ] Add 10 µL of one of the following on top of the set gel, per condition:
    - [ ] Overnight bacterial culture (AHL-producing).
    - [ ] Bacterial culture supernatant (AHL-producing, cell-free).
    - [ ] LB medium only (negative control).
- [ ] Include a positive control gel using a constitutively expressed GFP construct (not the AHL-gated sensor) to confirm the encapsulated lysate is expressing independent of AHL exposure.
- [ ] Incubate 2.5 h.

# Quality Control

Confirm embedding succeeded before scoring a readout:

- **GFP signal association**: image the gel by fluorescence microscopy, collecting a Z-stack to confirm GFP signal is associated with intact, embedded synthetic cells rather than background.
- **Negative control comparison**: compare against the LB-only negative control at matched optical and contrast settings.

:::{attention} Primary data not located
@Editor(london): GFP signal is reported in both the overnight-culture and supernatant conditions after 2.5 h, with no signal in the LB-only control at matched settings, confirmed by Z-stack imaging — but the underlying Z-stack image files are not available on this page and this result has not been independently re-verified.
:::

# Credits

Developed by Julia Purrinos De Oliveira (London Node), with the PLA1 colorimetric variant by Jonah McDonald and Charlie Newell.

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

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
