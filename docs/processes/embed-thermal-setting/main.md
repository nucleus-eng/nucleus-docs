---
title: "Embedding: Thermal Setting"
subtitle: "Process"
status: draft
---

# Overview

Embedding: Thermal Setting puts a sample in an agarose gel that then sets upon cooling. Agarose powder is mixed in the outer solution then melted and kept warm until the sample is added. This protocol applies to [LGA](../../modules/gel-lga/spec.md) and [ULGA](../../modules/gel-ulga/spec.md), which differ primarily in melting and gelling temperature.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{figure} ./resources/schematic.png
:label: fig-gel-schematic
:width: 100%
:align: center

Schematic representation of unilamellar liposomes held in a hydrogel matrix. Figure from [Understanding Liposome Behaviour in Hydrogel Matrices](https://devnotes.nucleus.engineering/articles/01a10dfe-c1df-7c2d-ba5a-035280a349f7).
:::

:::{table} Process parameters for each gel.
| Parameter | ULGA | LGA |
| --- | --- | --- |
| Melting method | Microwave | 95 °C heat block |
| Temperature hold method | 55 °C bead bath | 45 °C heat block |
| Gel point | 8 °C to 15 °C | 24 °C to 28 °C |
| Agarose final concentration | 5 mg/mL (0.5 % w/v) | 7 mg/mL (0.7 % w/v) |
| Agarose stock concentration | 10 mg/mL (1.0 % w/v) | 28 mg/mL (2.8 % w/v) |
| Agarose stock per well, before sample | 15 µL of stock | 7.5 µL of stock and 7.5 µL of outer solution |
:::

# Materials and Equipment

The agarose is listed under Materials on [LGA](../../modules/gel-lga/spec.md) and [ULGA](../../modules/gel-ulga/spec.md).

:::{table} Reagents.
:label: materials-embed-thermal-setting

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Glucose | Outer solution | D-(+)-Glucose, 99% | Thermo Scientific | A16828-36 | $41.65 | RT | [link](https://www.thermofisher.com/order/catalog/product/A16828.36) |
| HEPES | Outer solution | HEPES, Crystalline Powder, ≥99.5% (titration), Poly bottle | Sigma-Aldrich | H3375-500G | $431 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/h3375) |
| Low gelling agarose | Polymer | Low gelling agarose | Sigma-Aldrich | A9414-5G | — | Room temperature | [Sigma-Aldrich A9414](https://www.sigmaaldrich.com/US/en/product/sigma/a9414) |
| Ultra-low gelling agarose | Polymer | Ultra-low gelling agarose | Sigma-Aldrich | A5030 | — | Room temperature | [Sigma-Aldrich A5030](https://www.sigmaaldrich.com/US/en/product/sial/a5030) |
:::

:::{table} Equipment.
| Item | Used for |
| --- | --- |
| Microwave | Melting ULGA |
| Bead bath | Holding ULGA at temperature |
| Dry bath | Melting LGA, holding LGA at temperature |
| Vortex mixer | Melting LGA |
| 96-well or 384-well plate | Plating |
:::

# Protocol

- [ ] **Prepare the outer solution.** Use the same outer solution that the synthetic cells were prepared in.
- [ ] **Melt the agarose (ULGA).**
    - [ ] Add ULGA powder to 10 mg/mL (1.0 % w/v) in the outer solution.
    - [ ] Microwave in 10 s bursts, 5–7 times, until the ULGA is fully dissolved.
    - [ ] Keep the stock on a bead bath at temperature (55 °C) until use.
- [ ] **Melt the agarose (LGA).**
    - [ ] Add LGA powder to 28 mg/mL (2.8 % w/v) in the outer solution.
    - [ ] Heat the solution in a 95 °C heat block until the LGA is fully incorporated, vortexing occasionally as needed to help it dissolve.
    - [ ] Transfer an aliquot to a microfuge tube and keep it at temperature (45 °C) on a dry bath until use.
    - [ ] Transfer an aliquot of outer solution to a microfuge tube and heat it to the same temperature (45 °C) on the same block.

:::{warning} Keep agarose stocks above gelling temperature.
:class: dropdown
Agarose can set at room temperature. Keeping the stock warm prevents it from setting before it is mixed with the sample.
:::

- [ ] **Mix the sample with the gel precursor.**
    - [ ] For ULGA, combine 15 µL of sample with 15 µL of the ULGA stock.
    - [ ] For LGA, combine 15 µL of sample with 7.5 µL LGA stock and 7.5 µL outer solution.
- [ ] **Plate the mixture.** Dispense 30 µL per well of the combined gel and sample into a 96-well or 384-well plate. Plate the sample in its outer solution, with no gel, as a reference.

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this page include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Understanding Liposome Behaviour in Hydrogel Matrices
:link: https://devnotes.nucleus.engineering/articles/01a10dfe-c1df-7c2d-ba5a-035280a349f7#hydrogel-preparation
:footer: Ojaswita Pant, Manuel Bibrowski · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-f2a7-7372-93d6-8ea9f387f61d/public/schematic-hydrogel-o-d7d3affce66c5490e22c9a76d4696445.webp)
:::

:::{card} Bacterial Sensing in Hydrogel Embedded Synthetic Cells using LuxR Dependent Transcriptional Regulation
:link: https://devnotes.nucleus.engineering/articles/01a1121a-7513-7ec7-8378-0326c6b3630b#guv-embedding-in-gels-for-synthetic-ahl-experiment
:footer: Julia Purrinos de Oliveira, Niall McIntyre, Manuel Bibrowski, Charlie Newell, Jonah McDonald · DevStudio 2026

![](https://pub.curvenote.com/01a1659f-0760-755b-84e0-9a6fab2b60e4/public/overview-fac6c68e96a967785c623ca3bb266c61.png)
:::

:::{card} Two Vesicle Colorimetric pH Sensor System
:link: https://devnotes.nucleus.engineering/articles/01a0ea82-2101-7fed-82f9-1d8ef9258009
:footer: Sung-Won Hwang, Samuel Chen, Allen P. Liu · DevStudio 2026

![](https://pub.curvenote.com/01a1659e-fe19-7cd1-8542-37ff98753726/public/overview-schematic-a686967b8ee4691359ab0bc0bd9be620.png)
:::

::::
