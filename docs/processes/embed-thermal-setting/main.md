---
title: "Embedding: Thermal Setting"
subtitle: "Process"
status: draft
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

Embedding: Thermal Setting holds synthetic cells in an agarose gel that sets on cooling, so a downstream colorimetric or fluorescent readout can be measured in place rather than in free solution. Two grades are in use, and the grade sets two temperatures: the hold temperature, above the grade's gel-point range, keeps the agarose liquid while the synthetic cells go in; the set temperature, below that range, forms the gel. The London quorum-sensing demo uses ultra-low-gelling agarose (ULGA): POPC synthetic cells carrying the 3OC6-HSL Sensing Module (S30 Lysate plus the `LuxR-deGFP` sensor plasmid) are dispersed into it before it gels, and 3OC6-HSL from an external bacterial source diffuses in through the gel. The pH path uses low-gelling agarose (LGA).

:::{table} The two grades.
| Grade | Gel point | Melting point | Used in |
| --- | --- | --- | --- |
| [ULGA](../../modules/gel-ulga/spec.md) | (8–17) °C | ≤ 50 °C | [London Cascade](../../modules/london-cascade/spec.md) |
| [LGA](../../modules/gel-lga/spec.md) | (26–30) °C | ≤ 65 °C | [pH Cascade](../../modules/ph-cascade/spec.md) |
:::

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Notes
:class: dropdown
:icon: false

- Both grades gel well below standard agarose. The exact dissolution and cooling temperatures are not established for either; the steps below follow standard low-melting-agarose handling, not values confirmed for these preparations.
- Dissolve ULGA to 1% (w/v) in the prepared outer solution. Combined 1:1 with the synthetic cell suspension, that gives 0.5% (w/v) in the set gel, which is the top of the 0.2% to 0.5% working range. Lower concentrations gel more slowly and give faster kinetics. Both readouts on this page use the same concentration.
- The colorimetric demonstration ran at 1.5% (w/v), which gives 0.75% (w/v) in the set gel under the 1:1:2 combining ratio, above the working range. Use 1% for new work. The result measured at 1.5% is kept on the [Gel: ULGA](../../modules/gel-ulga/spec.md) spec, because it records the condition the experiment ran at.
- This protocol has so far been tested with liquid bacterial culture and supernatant; testing with solid agar bacterial media has not yet been completed.

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

**Hot agarose solution** - Dissolving agarose requires heating near boiling. Handle hot glass vessels and solution with appropriate heat-resistant gloves; allow to cool before combining with heat-sensitive synthetic cells or lysate.

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::::{tab-set}

::::{tab-item} GFP readout

:::{table} Outer solution used to embed SensorCell[3OC6-HSL ⟶ PLA1] synthetic cells for the GFP readout. ULGA at 1% (w/v) in the prepared solution.
:label: comp-ulga-gfp

| Component | Concentration |
| --- | --- |
| Potassium L-glutamate | 578 mM |
| HEPES | 72 mM |
| Glucose | 300 mM |
| ULGA | 1% (w/v) |

:::

::::

::::{tab-item} Colorimetric readout

:::{table} Outer solution used for the S30 Lysate-encapsulated, PLA1/CPRG colorimetric two-liposome demonstration. ULGA at 1% (w/v) in the prepared solution.
:label: comp-ulga-colorimetric

| Component | Concentration |
| --- | --- |
| Potassium L-glutamate | 578 mM |
| HEPES (pH 7.4) | 72 mM |
| Glucose | 300 mM |
| 3OC6-HSL (+ condition only) | (5-10) µM |
| 3OC6-HSL-producing bacteria supernatant | 10:1 dilution (20 µL per 200 µL hydrogel) |
| ULGA | 1% (w/v) |

:::

This variant feeds the Colorimetric Readout process; see the [SensorCell[3OC6-HSL ⟶ PLA1]](../../modules/ahsl-sensing-cell/spec.md) spec for the sensing synthetic cell composition and the [PLA1 Lysis Module](../../modules/effector-pla1/spec.md) and [LacZ Reporter](../../modules/reporter-lacz/spec.md) specs for the downstream lysis and colorimetric chemistry — this process page covers embedding only, not the readout itself.

::::

::::{tab-item} pH path

:::{table} Gel used to embed the pH-path populations. LGA at 0.7% (w/v) in the set gel.
| Component | Concentration |
| --- | --- |
| LGA | 0.7% (w/v) |
| [Outer Solution](../../modules/outer-solution/spec.md) | 1× |
:::

::::

:::::

::::::

:::::::

# Materials and Equipment

:::{table}
:label: bom-embed-thermal-setting
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ULGA | Reagent | Ultra low gelling temperature agarose | Sigma-Aldrich | A5030 | £52.00 | RT | [link](https://www.sigmaaldrich.com/GB/en/product/sial/a5030) |
| LGA | Reagent | Low gelling temperature agarose | — | — | — | RT | — |
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

Two part numbers are recorded for the ULGA: Sigma-Aldrich A5030 and A2576, "Agarose, Type IX-A, ultra low gelling temperature". They are interchangeable. @Editor(london): cite the source for treating A5030 and A2576 as interchangeable.

# Protocol

## Prepare the Agarose Solution

- [ ] Prepare the base outer solution: (578 mM) potassium L-glutamate, (72 mM) HEPES, (300 mM) glucose in water.
- [ ] Dissolve the agarose into the outer solution by heating near boiling with stirring until fully dissolved: ULGA to 1% (w/v), which gives 0.5% (w/v) in the set gel after the 1:1 combination below; LGA to its set-gel concentration (0.7% (w/v) in the pH path).

:::{hint} Note
:class: simple
:icon: false
No exact dissolution temperature or hold time is established for either grade. Standard low-melting-agarose technique is to heat until the solution runs clear, then hold above the top of the grade's gel-point range until combined with the synthetic cell suspension, and only then cool below the bottom of that range to set.
:::

- [ ] Cool the dissolved agarose to a temperature that keeps it liquid (above the top of its gel-point range, in the table above) but is safe to mix with synthetic cells, before proceeding.

## Form Hydrogel-Embedded synthetic cells

- [ ] Combine the cooled, still-liquid agarose with the synthetic cells (e.g., SensorCell[3OC6-HSL ⟶ PLA1] POPC synthetic cells carrying `LuxR-deGFP` in S30 Lysate) to a total volume of 100 µL per reaction.
- [ ] Dispense the mixture into wells or onto a plate, and set the gel by cooling below the bottom of the grade's gel-point range.

## Add Bacterial Input

Where a component is sensitive to anything the formation step imposes (e.g., temperature), add at this step — noting that it is applied on top of the set gel and reaches the interior only by diffusion, so this suits an analyte rather than a component that must sit with the cells.

- [ ] Add 10 µL of one of the following on top of the set gel, per condition:
    - [ ] Overnight bacterial culture (3OC6-HSL-producing).
    - [ ] Bacterial culture supernatant (3OC6-HSL-producing, cell-free).
    - [ ] LB medium only (negative control).
- [ ] Include a positive control gel using a constitutively expressed GFP construct (not the 3OC6-HSL-gated sensor) to confirm the encapsulated lysate is expressing independent of 3OC6-HSL exposure.
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

{button}`download <generated/embed-thermal-setting-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/embed-thermal-setting-bom.pdf>`
:::

::::

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
