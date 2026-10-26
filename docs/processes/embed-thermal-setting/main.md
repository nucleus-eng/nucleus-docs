---
title: "Embedding: Thermal Setting"
subtitle: "Process"
status: draft
---

# Overview

Embedding: Thermal Setting holds a sample in an agarose gel that sets on cooling. The agarose is dissolved hot in the outer solution and kept warm until the sample is mixed in. This page covers [Gel: ULGA](../../modules/gel-ulga/spec.md) and [Gel: LGA](../../modules/gel-lga/spec.md), which share the steps and differ in the parameters below.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{figure} ./resources/schematic.png
:label: fig-gel-schematic
:width: 100%
:align: center

Schematic representation of unilamellar liposomes held in a hydrogel matrix. Figure from [Understanding Liposome Behaviour in Hydrogel Matrices](https://devnotes.nucleus.engineering/articles/01a10dfe-c1df-7c2d-ba5a-035280a349f7).
:::

:::{table} Parameters of each gel.
| Parameter | Gel: ULGA | Gel: LGA |
| --- | --- | --- |
| Stock concentration | 10 mg/mL | 28 mg/mL |
| Dissolve | Microwave | 95 °C heat block |
| Hold until use | 55 °C bead bath | 45 °C dry bath |
| Stock per well, before mixing | 15 µL of stock | 7.5 µL of stock and 7.5 µL of outer solution |
| Final concentration | 5 mg/mL | 7 mg/mL |
| Gel point | About 8 °C to 15 °C | About 24 °C to 28 °C |
:::

# Materials and Equipment

The agarose is listed under Materials on [Gel: ULGA](../../modules/gel-ulga/spec.md) and [Gel: LGA](../../modules/gel-lga/spec.md).

:::{table} Reagents.
:label: materials-embed-thermal-setting

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Glucose | Outer solution | D-(+)-Glucose, 99% | Thermo Scientific | A16828-36 | $41.65 | RT | [link](https://www.thermofisher.com/order/catalog/product/A16828.36) |
| HEPES | Outer solution | HEPES, Crystalline Powder, ≥99.5% (titration), Poly bottle | Sigma-Aldrich | H3375-500G | $431 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/h3375) |
:::

:::{table} Equipment.
| Item | Used for |
| --- | --- |
| Microwave | Dissolving ULGA |
| 95 °C heat block | Dissolving LGA |
| 55 °C bead bath | Holding ULGA |
| Dry bath | Holding LGA at 45 °C |
| Vortex mixer | Dissolving LGA |
| 96-well or 384-well plate | Plating |
:::

# Protocol

## Prepare the Outer Solution

- [ ] **Prepare the outer solution.**
    - [ ] Use the outer solution the sample was prepared in. Its composition is flexible: match its osmolarity to the cells being embedded, rather than following one fixed recipe. The supporting DevNotes used glucose and 50 mM HEPES, at a final osmolarity of about 1200 mOsm, as their reference outer solution.

:::{attention} The DevNote's own figures disagree with the figures stated here
@Editor: the DevNote's supplement gives the ULGA outer solution as 1057 Osm of glucose. That is against the about 1200 mOsm stated here. It gives the LGA stock as 2.70 % in ultrapure water, 40.5 mg in 1500 µL, which is 27 mg/mL. That is against the 28 mg/mL stated here. Confirm which figures are right. Also link this step to `assemble-solution` (Layer 1), with the outer solution's components as its inputs, once it is on `main`.
:::

## Prepare the ULGA Stock

- [ ] **Dissolve the ULGA.**
    - [ ] Prepare ULGA at 10 mg/mL in the outer solution.
    - [ ] Microwave in 10 s bursts, 5–7 times, until the ULGA is fully dissolved.
- [ ] **Hold the stock.**
    - [ ] Keep the stock on a 55 °C bead bath until use.

## Prepare the LGA Stock

- [ ] **Dissolve the LGA.**
    - [ ] Dissolve LGA at 28 mg/mL in the outer solution, adjusting to a final osmolarity of about 1200 mOsm.
    - [ ] Heat the solution in a 95 °C heat block until the LGA is fully dissolved. Vortex occasionally to help it dissolve.
- [ ] **Hold the stock.**
    - [ ] Transfer an aliquot to a tube and keep it on a 45 °C dry bath until use.

:::{hint} LGA can set at room temperature
:class: dropdown
Keeping the stock warm prevents it from setting before it is mixed with the sample.
:::

- [ ] **Dilute the stock for each well.**
    - [ ] Combine 7.5 µL of the LGA stock with 7.5 µL of the outer solution.

:::{attention} Dilution per well is inferred
@Editor: confirm that the 15 µL of gel stock per well is 7.5 µL of LGA stock and 7.5 µL of outer solution. The DevNote gives the final LGA concentration as 7 mg/mL with the parenthetical 7.5 µL and 7.5 µL of outer solution.
:::

## Mix with the Sample and Plate

- [ ] **Mix the sample with the gel precursor.**
    - [ ] For ULGA, combine 15 µL of sample with 15 µL of the ULGA stock.
    - [ ] For LGA, combine 15 µL of sample with the 15 µL of diluted LGA stock at 45 °C.
- [ ] **Plate the mixture.**
    - [ ] Dispense 30 µL per well into a 96-well or 384-well plate. Plate each sample in duplicate.
    - [ ] Plate the sample in its outer solution, with no gel, as a reference.

:::{attention} Mixing and setting are not described for ULGA
@Editor: state the temperature at which the ULGA stock is mixed with the sample, and how and where each plated mixture is cooled to its gel point.
:::

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
