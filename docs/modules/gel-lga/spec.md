---
title: "Gel: LGA"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Gel: LGA is a physical hydrogel of low gelling agarose (LGA) in an outer solution. The network sets on cooling, at about 24 °C to 28 °C, so the stock is held at 45 °C until it is mixed with a sample. It is set by [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    LGA_POWDER["Low gelling agarose"]
    OUTER_SOLUTION["Outer solution"]

    P1_SET_THERMAL_0(["Embedding: Thermal Setting (mixing)"])
    GEL_LGA["Gel: LGA"]

    LGA_POWDER --> P1_SET_THERMAL_0
    OUTER_SOLUTION --> P1_SET_THERMAL_0
    P1_SET_THERMAL_0 -->|"stock diluted 1:1 with outer solution, then 1:1 with the sample"| GEL_LGA


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class LGA_POWDER,OUTER_SOLUTION leaf;
    class GEL_LGA composed;
    class P1_SET_THERMAL_0 process;

    click P1_SET_THERMAL_0 "/docs/processes/embed-thermal-setting/main"
    click GEL_LGA "/docs/modules/gel-lga/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Outer Solution

:::{table} Outer solution of Gel: LGA.
| Component | Type |
| --- | --- |
| Outer solution | Solution |
:::

::::

::::{tab-item} Polymer

:::{table} Polymer of Gel: LGA.
| Component | Stock concentration | Final concentration |
| --- | --- | --- |
| Low gelling agarose | 2.8% (w/v) | 0.7% (w/v) |
:::

The final concentration is for a stock diluted 1:1 with outer solution and then mixed 1:1 with the sample.

:::{attention} Dilution per well is inferred
@Editor: confirm that the stock is diluted 1:1 with outer solution before it is mixed with the sample. The DevNote gives the final LGA concentration as 0.7% (w/v) with the parenthetical 7.5 µL and 7.5 µL of outer solution, and no step describes the dilution.
:::

::::

:::::

# Expected Behavior

Gel: LGA is expected to set when the mixture cools to its gel point, about 24 °C to 28 °C. It can set at room temperature, so the stock is kept warm until the mixture is dispensed.

# Requirements

Requires an outer solution to dissolve into. For liposomes, use the outer solution used to prepare the liposomes.

Requires that a sample tolerate mixing at 45 °C.

# Processes

[Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) prepares the stock and sets the gel.

# Materials

:::{table} Materials of Gel: LGA.
:label: materials-gel-lga

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Low gelling agarose | Polymer | Low gelling agarose | Sigma-Aldrich | A9414-5G | — | Room temperature | [Sigma-Aldrich A9414](https://www.sigmaaldrich.com/US/en/product/sigma/a9414) |
:::

# Constituent Modules

- Outer solution — the solution the polymer dissolves into
- Low gelling agarose — the polymer

# Credits

Developed by Ojaswita Pant (Northwestern University, DevCells Chicago Node, Truby Lab) and Manuel Bibrowski (Imperial College London, DevCells London Node, Elani Lab).

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this specification include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Understanding Liposome Behaviour in Hydrogel Matrices
:link: https://devnotes.nucleus.engineering/articles/01a10dfe-c1df-7c2d-ba5a-035280a349f7#hydrogel-preparation
:footer: Ojaswita Pant, Manuel Bibrowski · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-f2a7-7372-93d6-8ea9f387f61d/public/schematic-hydrogel-o-d7d3affce66c5490e22c9a76d4696445.webp)
:::

:::{card} Two Vesicle Colorimetric pH Sensor System
:link: https://devnotes.nucleus.engineering/articles/01a0ea82-2101-7fed-82f9-1d8ef9258009
:footer: Sung-Won Hwang, Samuel Chen, Allen P. Liu · DevStudio 2026

![](https://pub.curvenote.com/01a1659e-fe19-7cd1-8542-37ff98753726/public/overview-schematic-a686967b8ee4691359ab0bc0bd9be620.png)
:::

::::
