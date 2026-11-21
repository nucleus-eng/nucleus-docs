---
title: "Reporter: Color Change"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Overview

Reporter: Color Change outputs a visible color change in response to a signal. As designed, Phospholipase A1 (PLA1) is expressed in the presence of a signal, which then lyses a membrane holding chlorophenol red-β-D-galactopyranoside (CPRG, yellow), which is then catalyzed by β-galactosidase (LacZ) and converted to chlorophenol red (CPR, purple). Where each component is localized (e.g., "one vessicle" has dye OR enzyme in the synthetic cell and the other component in outer solution, "two vessicle" has dye in one liposome and enzyme in another") depends on the implementation. See the [pH Cascade](../ph-cascade/spec.md), with PLA1 expressed in a [pH Sensing Cell](../ph-sensing-cell/spec.md), CPRG in separate liposomes, and the enzyme in the outer solution, for a concrete implementation.

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    GATED_PLA1_DNA["PLA1 template"]
    SUBSTRATE_CPRG["Substrate: CPRG"]
    MEMBRANE["Base Membrane: POPC/Chol"]
    REPORTER_LACZ_ENZYME["Reporter: LacZ Enzyme"]

    P1_REPORT_COLOR_0(["Colorimetric Readout (mixing)"])
    COLOR["Color: CPR"]

    REPORTER_LACZ_ENZYME --> P1_REPORT_COLOR_0
    SUBSTRATE_CPRG --> P1_REPORT_COLOR_0
    MEMBRANE --> P1_REPORT_COLOR_0
    GATED_PLA1_DNA --> P1_REPORT_COLOR_0
    P1_REPORT_COLOR_0 --> COLOR


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class GATED_PLA1_DNA,SUBSTRATE_CPRG,MEMBRANE,REPORTER_LACZ_ENZYME leaf;
    class COLOR composed;
    class P1_REPORT_COLOR_0 process;

    click MEMBRANE "/docs/modules/membrane-popc-chol/spec"
    click REPORTER_LACZ_ENZYME "/docs/modules/reporter-lacz-enzyme/spec"
    click P1_REPORT_COLOR_0 "/docs/processes/colorimetric-readout/main"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Substrate

:::{table} Where the substrate is held until lysis.
:label: comp-color-change-substrate

| Substrate | Held in | Module |
| --- | --- | --- |
| CPRG | Inner solution of the LUV | [Substrate LUV: CPRG](../substrate-cprg-luv/spec.md) |
| CPRG | Inner solution of the SUV | [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md) |
:::
::::

::::{tab-item} Membrane

:::{table} The membrane that PLA1 lyses.
:label: comp-color-change-membrane

| Membrane | Holds | Module |
| --- | --- | --- |
| POPC/cholesterol bilayer | CPRG, until PLA1 lyses it | [Base Membrane: POPC/Chol](../membrane-popc-chol/spec.md) |
:::
::::

::::{tab-item} DNA

Constructs that express PLA1 under each signal gate. The gate is the regulatory DNA that the construct carries.

:::{table} DNA constructs that express PLA1, by signal gate.
:label: comp-color-change-dna

| Name | Length | Gate | Format | File |
| --- | --- | --- | --- | --- |
| `pT7-toehold9-PLA1-linear` | 1203 bp | pH (toehold9) | Linear template, added to the cytosol at 2 nM in the pH implementation | [pT7-toehold9-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/bf3d5aeea79c652b3f7af08f32409dbc7b3431b0/effectors/detector-ph/pT7-toehold9-PLA1-linear.gb) |
| `pT7-tetO-PLA1-linear` | 1202 bp | aTc, through TetR | Linear template | [pT7-tetO-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/bd9574151d1e2c15878ce30fb05b320a8a0a5936/effectors/detector-tetr-atc/pT7-tetO-PLA1-linear.gb) |
| `pOpen-T7-tetO-PLA1` | 3140 bp | aTc, through TetR | Circular plasmid (pOpen) | [pOpen-T7-tetO-PLA1.gb](https://github.com/nucleus-eng/DNA/blob/f06e12cbc43da77dbb3c9d2d9a4ecc790fdd75b9/effectors/detector-tetr-atc/pOpen-T7-tetO-PLA1.gb) |
| `LuxR-PLA1-linear` | 2237 bp | 3OC6-HSL, through LuxR | Linear template | [LuxR-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/bd9574151d1e2c15878ce30fb05b320a8a0a5936/effectors/detector-3oc6-hsl/LuxR-PLA1-linear.gb) |
| `pOpen-LuxR-PLA1` | 4175 bp | 3OC6-HSL, through LuxR | Circular plasmid (pOpen) | [pOpen-LuxR-PLA1.gb](https://github.com/nucleus-eng/DNA/blob/f06e12cbc43da77dbb3c9d2d9a4ecc790fdd75b9/effectors/detector-3oc6-hsl/pOpen-LuxR-PLA1.gb) |
:::

::::

:::::

# Expected Behavior

## Cells

In the [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md), color is expected to stay yellow when the gating signal is absent (pH 7.6) and to turn purple when it is present (pH 6.3), after β-galactosidase is added during [color development](../../processes/colorimetric-readout/main.md)

# Requirements

Requires pT7 transcription and translation to express PLA1 (e.g. [Base Cytosol](../base-cytosol/spec.md)).

Requires a signal that gates PLA1 expression (e.g. [Detector: pH-Sensing](../detector-ph/spec.md)) with a low noise floor. 

Requires a membrane (e.g., [Base Membrane](../membrane-popc-chol/spec.md)) with low leakiness.

# Implementations

- [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md)

# Constituent Modules

- [Reporter: LacZ Enzyme](../reporter-lacz-enzyme/spec.md) — converts released CPRG from yellow to purple
- [Substrate LUV: CPRG](../substrate-cprg-luv/spec.md) — holds CPRG until lysis
- [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md) — alternative substrate population, used in place of the LUV

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this specification include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Co-Encapsulated Cell-Free PLA1 Expression in beta-Galactosidase GUVs
:link: https://devnotes.nucleus.engineering/articles/01a12e24-46dc-761d-b020-f1f77cce78ba
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659c-0b14-7107-9490-170bb5b0dc82/public/fig8-endpoint-abs-15-fa8ff33abe1e637358abcbe415f6130e.webp)
:::

:::{card} Implementing of a bulk color change module into bacterial quorum sensing
:link: https://devnotes.nucleus.engineering/articles/01a12e6c-b511-7d30-aa95-002d386f751e
:footer: Manuel Bibrowski, Charlie Newell, Jonah McDonald, Niall McIntyre, Julia Purrinos de Oliveira · DevStudio 2026

![](https://pub.curvenote.com/01a1650a-90b4-729f-875b-e4f1ddce3bec/public/colorchange-overnigh-520d47ff723d53997b42c0e1c8c68cdc.webp)
:::

:::{card} TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning
:link: https://devnotes.nucleus.engineering/articles/01a1304b-1c56-7352-a082-ba84a2684f82
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-ebfe-71b5-b20a-66b33af95dfb/public/fig7-patterned-gel-5fc6273fa124c69e6d78ac4caafe3ce4.webp)
:::

:::{card} Triggered Lysis of beta-Galactosidase-Loaded GUVs by Cell-Free Expressed Phospholipase A1
:link: https://devnotes.nucleus.engineering/articles/01a12d42-ca2e-70e7-b78b-66fcf11c400a
:footer: Mary Kelly · DevStudio 2026

![](https://pub.curvenote.com/01a1659c-0cd1-7f71-b8ee-df80a98ce1f8/public/fig1-pla1-guv-lysis--b9cba8b401d09e1f3b6124e89a713123.webp)
:::

:::{card} Two Vesicle Colorimetric pH Sensor System
:link: https://devnotes.nucleus.engineering/articles/01a0ea82-2101-7fed-82f9-1d8ef9258009
:footer: Sung-Won Hwang, Samuel Chen, Allen P. Liu · DevStudio 2026

![](https://pub.curvenote.com/01a1659e-fe19-7cd1-8542-37ff98753726/public/overview-schematic-a686967b8ee4691359ab0bc0bd9be620.webp)
:::

:::{card} Understanding Liposome Behaviour in Hydrogel Matrices
:link: https://devnotes.nucleus.engineering/articles/01a10dfe-c1df-7c2d-ba5a-035280a349f7
:footer: Ojaswita Pant, Manuel Bibrowski · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-f2a7-7372-93d6-8ea9f387f61d/public/schematic-hydrogel-o-d7d3affce66c5490e22c9a76d4696445.webp)
:::

::::
