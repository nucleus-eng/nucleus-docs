---
title: "Reporter: LacZ Enzyme"
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

The LacZ Enzyme Reporter is purified β-galactosidase (LacZ) added to the outer solution in a basic buffer. It converts the yellow substrate chlorophenol red-β-D-galactopyranoside (CPRG) into the purple chlorophenol red (CPR). It reads out CPRG that was released from liposomes, such as [Substrate LUV: CPRG](../substrate-cprg-luv/spec.md) and [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md). It is the reporter of the [pH Cascade](../ph-cascade/spec.md). The basic buffer raises the pH of the assay so that β-galactosidase can act.

:::{attention}
@Developer: The DevNote calls the color of CPR purple in its overview and pink in its figure captions. Give the color name to use.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} Enzyme Solution

:::{table} Enzyme solution, a 3× solution made from the 1000 U/mL stock in the basic buffer of the next tab. Adding 30 µL of it to 60 µL of assay gives 1.2 U/mL.
:label: comp-reporter-lacz-enzyme-solution

| Component | Stock concentration | 3× concentration | Final concentration |
| --- | --- | --- | --- |
| β-galactosidase | 1000 U/mL | 3.6 U/mL | 1.2 U/mL |
:::
::::

::::{tab-item} Basic Buffer

:::{table} Basic buffer that carries the enzyme. Its pH is 9.9, and its osmolarity is 1165 mOsm/kg, measured.
:label: comp-reporter-lacz-enzyme-buffer

| Component | Amount |
| --- | --- |
| Tris base, 1 M | 1 mL |
| HCl, 37 % | 2.5 µL |
:::

:::{attention}
@Developer: State whether the color of CPR depends on pH.
:::
::::

:::::

# Expected Behavior

## Solution

The LacZ Enzyme Reporter is expected to turn released CPRG from yellow to purple in solution. At 1.2 U/mL the color was visible by eye after 5.5 h at 37 °C. Data are in the [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md), read by [Colorimetric Readout](../../processes/colorimetric-readout/main.md).

## Gels

The LacZ Enzyme Reporter is expected to do the same in 3.5 mg/mL low-gelling agarose, where 1.2 U/mL gave a visible color after 5.5 h at 37 °C. In 7 mg/mL low-gelling agarose, 2 U/mL gave a visible color after 2 h in all wells, including the control without pH Sensing Cells. The leakage is described on [Substrate LUV: CPRG](../substrate-cprg-luv/spec.md). Data are in the [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md).

# Requirements

Requires CPRG in the outer solution (e.g. CPRG released from [Substrate LUV: CPRG](../substrate-cprg-luv/spec.md) or [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md)).

# Implementations

- [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md)

# Processes

- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) adds the enzyme after the substrate is released, and reads the color.

# Materials

:::{attention}
@Developer: Give the source organism, manufacturer and part number of the β-galactosidase, and the manufacturer and part number of the Tris base.
:::

# Credits

Developed by [Sung-Won Hwang](https://orcid.org/0000-0003-1686-7090), [Samuel Chen](https://orcid.org/0000-0001-8501-7175) and [Allen P. Liu](https://orcid.org/0000-0002-0309-7018) (University of Michigan).

:::{attention}
@Editor: Add the Node and Lab to this credit.
:::

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this specification include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Two Vesicle Colorimetric pH Sensor System
:link: https://devnotes.nucleus.engineering/articles/01a0ea82-2101-7fed-82f9-1d8ef9258009
:footer: Sung-Won Hwang, Samuel Chen, Allen P. Liu · DevStudio 2026

![](https://pub.curvenote.com/01a1659e-fe19-7cd1-8542-37ff98753726/public/overview-schematic-a686967b8ee4691359ab0bc0bd9be620.webp)
:::

::::
