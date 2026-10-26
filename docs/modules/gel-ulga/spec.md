---
title: "Gel: ULGA"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Gel: ULGA is a physical hydrogel of ultra-low gelling agarose (ULGA) in an outer solution. The network sets on cooling, at about 8 °C to 15 °C. It is set by [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    ULGA_POWDER["Ultra-low gelling agarose"]
    OUTER_SOLUTION["Outer solution"]

    P1_SET_THERMAL_0(["Embedding: Thermal Setting (mixing)"])
    GEL_ULGA["Gel: ULGA"]

    ULGA_POWDER --> P1_SET_THERMAL_0
    OUTER_SOLUTION --> P1_SET_THERMAL_0
    P1_SET_THERMAL_0 -->|"1:1 with the sample, halving the ULGA to its final figure"| GEL_ULGA


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class ULGA_POWDER,OUTER_SOLUTION leaf;
    class GEL_ULGA composed;
    class P1_SET_THERMAL_0 process;

    click P1_SET_THERMAL_0 "/docs/processes/embed-thermal-setting/main"
    click GEL_ULGA "/docs/modules/gel-ulga/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Outer Solution

:::{table} Outer solution of Gel: ULGA.
| Component | Type |
| --- | --- |
| Outer solution | Solution |
:::

::::

::::{tab-item} Polymer

:::{table} Polymer of Gel: ULGA.
| Component | Stock concentration | Final concentration |
| --- | --- | --- |
| Ultra-low gelling agarose | 10 mg/mL | 5 mg/mL |
:::

The final concentration is for a stock mixed 1:1 with the sample.

::::

:::::

# Expected Behavior

Gel: ULGA has a gel point of about 8 °C to 15 °C. The mixture sets at this temperature. The stock is easy to pipette. The ULGA stock is held at 55 °C until use.

:::{attention} Mixing temperature is not confirmed
@Editor: state the temperature at which the sample is mixed with the ULGA stock. The stock is held at 55 °C. Confirm whether the sample is also mixed in at 55 °C, or state the correct temperature. State how the mixture then cools to its gel point.
:::

# Requirements

Requires an outer solution to dissolve into. For liposomes, use the outer solution used to prepare the liposomes.

Requires that a sample tolerate the temperature at which it is mixed with the stock.

# Processes

[Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) prepares the stock and sets the gel.

# Materials

:::{table} Materials of Gel: ULGA.
:label: materials-gel-ulga

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Ultra-low gelling agarose | Polymer | Ultra-low gelling agarose | Sigma-Aldrich | A5030 | — | Room temperature | [Sigma-Aldrich A5030](https://www.sigmaaldrich.com/US/en/product/sial/a5030) |
:::

# Constituent Modules

- Outer solution — the solution the polymer dissolves into
- Ultra-low gelling agarose — the polymer

# Credits

Developed by Ojaswita Pant (Northwestern University, DevCells Chicago Node, Truby Lab) and Manuel Bibrowski (Imperial College London, DevCells London Node, Elani Lab).

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this specification include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Bacterial Sensing in Hydrogel Embedded Synthetic Cells using LuxR Dependent Transcriptional Regulation
:link: https://devnotes.nucleus.engineering/articles/01a1121a-7513-7ec7-8378-0326c6b3630b#guv-embedding-in-gels-for-synthetic-ahl-experiment
:footer: Julia Purrinos de Oliveira, Niall McIntyre, Manuel Bibrowski, Charlie Newell, Jonah McDonald · DevStudio 2026

![](https://pub.curvenote.com/01a1659f-0760-755b-84e0-9a6fab2b60e4/public/overview-fac6c68e96a967785c623ca3bb266c61.png)
:::

:::{card} Understanding Liposome Behaviour in Hydrogel Matrices
:link: https://devnotes.nucleus.engineering/articles/01a10dfe-c1df-7c2d-ba5a-035280a349f7#hydrogel-preparation
:footer: Ojaswita Pant, Manuel Bibrowski · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-f2a7-7372-93d6-8ea9f387f61d/public/schematic-hydrogel-o-d7d3affce66c5490e22c9a76d4696445.webp)
:::

::::
