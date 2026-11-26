---
title: "Colorimetric pH Sensor"
subtitle: Implementation
status: draft
site:
    hide-toc: true
---

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

(colorimetric-ph-sensor-overview)=
# Overview

The Colorimetric pH Sensor is an Implementation that combines [pH Sensing Cells](../../modules/ph-sensing-cell/spec.md) with [liposomes containing a substrate](../../modules/substrate-cprg-suv/spec.md) and [LacZ enzyme](../../modules/reporter-lacz-enzyme/spec.md). The Sensor detects acidic conditions (pH 6.3) and produces a visible color change. This signaling cascade is demonstrated in solution and in 3.5 mg/mL [low-gelling agarose](../../modules/gel-lga/spec.md) upon [color development](../../processes/color-change-neutralization/main.md). Acidic pH triggers expression of phospholipase A1 (PLA1), which lyses the CPRG liposomes, allowing β-galactosidase to convert released CPRG from yellow to purple. Wells hold 60 µL of sample and are incubated at 37 °C.

(colorimetric-ph-sensor-protocol)=
# Protocol

(colorimetric-ph-sensor-solution-assay)=
## Solution Assay

The solution assay runs in a 384-well square plate with 60 µL per well. The pH 6.3 condition replaces the Tris 1M, HEPES 1.15M buffer stock with a buffer mix for pH 6.3, the composition of which can be found in the Outer Solution tab of the [pH Cascade](../../modules/ph-cascade/spec.md).

:::{table} Assembly of a 60 µL well in the solution assay.
:label: tbl-colorimetric-ph-sensor-well
:align: center

| Component | pH 7.6 arm (µL) | pH 6.3 arm (µL) |
| --- | --- | --- |
| Energy solution (2×) | 30 | 30 |
| Ultrapure water | 15.6 | 15.6 |
| Tris 1 M, HEPES 1.15 M buffer stock | 7.2 | |
| Buffer mix for pH 6.3 | | 7.2 |
| pH Sensing Cells, CPRG liposomes and suspension buffer | 7.2 | 7.2 |
| Total | 60 | 60 |
:::

The last row of the table above is a 7.2 µL slot that holds the liposomes and suspension buffer. 

:::{table} Conditions of the four imaged wells. The suspension buffer is 466.7 mL/L Tris 1 M, HEPES 1.15 M.
:label: tbl-colorimetric-ph-sensor-conditions
:align: center
@Claude: this table is better served by the data that it represents in the Performance / Results section

@Claude: on nomenclature, the cells are liposomes too. make the distinction between pH Sensing Cells and CPRG liposomes in the "Name" column
| Well | Name | Type | pH | pH Sensing Cells (µL) | CPRG liposomes (µL) | Suspension buffer (µL) |
| --- | --- | --- | --- | --- | --- | --- |
| D4 | pH 7.6, cells only | Control | 7.6 | 1 | 0 | 6.2 |
| D5 | pH 6.3, cells only | Control | 6.3 | 1 | 0 | 6.2 |
| E4 | pH 7.6, cells and liposomes | Sample | 7.6 | 3 | 2.1 | 2.1 |
| E5 | pH 6.3, cells and liposomes | Sample | 6.3 | 3 | 2.1 | 2.1 |
:::

@Claude: copy edit this line too given what I said above: The cells-only wells take 1 µL of cells, and the sample wells take 3 µL, so the two differ in cell dose as well as in liposomes. The four wells are imaged by fluorescence microscopy after 13 h at 37 °C.

(colorimetric-ph-sensor-gel-assay)=
## Gel Assay

The gel assay uses 60 µL of low-gelling agarose gel per well, set by [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md). It is the solution well with the 15.6 µL of ultrapure water replaced by 15.6 µL of a 27 mg/mL low-gelling agarose stock, which gives a final agarose concentration of 7 mg/mL. The pH 6.3 arm takes the same buffer mix as in the solution assay.

:::{table} Assembly of a 60 µL well in the gel assay, at 7 mg/mL agarose.
:label: tbl-colorimetric-ph-sensor-gel-well
:align: center

| Component | OFF (pH 7.6, µL) | ON (pH 6.3, µL) |
| --- | --- | --- |
| Energy solution (2×) | 30 | 30 |
| 27 mg/mL agarose stock in ultrapure water | 15.6 | 15.6 |
| Tris 1 M, HEPES 1.15 M buffer stock | 7.2 | - | | Buffer mix for pH 6.3 | - | 7.2 |
| pH Sensing Cells, CPRG liposomes and suspension buffer | 7.2 | 7.2 |
| Total | 60 | 60 |

@Claude: pull the Energy solution (2x) table in here too
:::

The agarose stock is 40.5 mg of low-gelling agarose (Sigma-Aldrich A9414-5G) in 1500 µL of ultrapure water. It is dissolved in a heat block at 85 °C to 95 °C with occasional vortexing, then cooled to 65 °C. The stock is mixed with the Energy Solution and the buffer (either Tris 1 M, HEPES 1.5 M; or Buffer mix), then cooled to 45 °C before adding liposomes. For 3.5 mg/mL agarose, half of the stock is replaced with ultrapure water: 7.8 µL of stock and 7.8 µL of water in place of the 15.6 µL gel stock.

The 7.2 µL slot holds 3 µL of pH Sensing Cells, 3 µL of CPRG liposomes and 1.2 µL of suspension buffer. The suspension buffer is at 1175 mOsm/kg and pH 8. @Claude: what is the "7.2 slot"? use the name in the line in the appropriate table instead, be explicit

(colorimetric-ph-sensor-readout)=
## Readout

Color is developed with [@Claude: rename this appropriately](../../processes/color-change-neutralization/main.md), which adds 30 µL of a 3× β-galactosidase solution to 60 µL of gel or solution. The 30 µL of 3× solution gives 1.2 U/mL, as in the run in 3.5 mg/mL agarose. 

(colorimetric-ph-sensor-performance)=
# Performance

(colorimetric-ph-sensor-validation-in-solution)=
## Validation in Solution

In solution, acidic pH gave a visible color change.

:::{figure} solution-color-change.png
:align: center
:width: 60%

Photograph of the two-liposome system in solution at pH 7.6 (left) and pH 6.3 (right).
:::

Fluorescence microscopy shows the cells in four wells after 13 h at 37 °C. Note: The wells lacking CPRG liposomes (D4 and D5) hold approximately 30% of the number of cells in the sample wells (E4 and E5), so brightness of samples at the same pH are not directly comparable.

:::::{tab-set}

::::{tab-item} Cells at pH 7.6 (D4)
:::{figure} microscopy-d4.png
:align: center
:width: 100%

Fluorescence micrograph of pH Sensing Cells at pH 7.6 after 13 h at 37 °C. Cy5 signal stays inside the cells, which indicates that the membranes stayed intact.
:::
::::

::::{tab-item} Cells at pH 6.3 (D5)
:::{figure} microscopy-d5.png
:align: center
:width: 100%

Fluorescence micrograph of pH Sensing Cells at pH 6.3 after 13 h at 37 °C. Cy5 signal is absent, which indicates that acidic conditions triggered PLA1 expression, which disrupted the membrane and released the dye.
:::
::::

::::{tab-item} Cells and liposomes at pH 7.6 (E4)
:::{figure} microscopy-e4.png
:align: center
:width: 100%

Fluorescence micrograph of CPRG liposomes with pH Sensing Cells at pH 7.6 after 13 h at 37 °C. Cy5 signal is detected only in the cells.
:::
::::

::::{tab-item} Cells and liposomes at pH 6.3 (E5)
:::{figure} microscopy-e5.png
:align: center
:width: 100%

Fluorescence micrograph of CPRG liposomes with pH Sensing Cells at pH 6.3 after 13 h at 37 °C. Cy5 signal is detected only in the cells. In the field shown, fewer cells keep Cy5 than in E4, which indicates PLA1-mediated Cy5 release.
:::
::::

:::::

(colorimetric-ph-sensor-validation-in-gels)=
## Validation in Gels

CPRG LUVs in 7 mg/mL [low-gelling agarose](../../modules/gel-lga/spec.md) showed a visible color change at pH 6.3 that was barely distinguishable from the negative control lacking pH Sensing Cells. The only difference from the solution assay was the gel, implying that embedding caused CPRG to leak from the Substrate Liposomes, even without PLA1.

To lower the CPRG leakage, SUVs were used instead because smaller liposomes are expected to be more stable. Background color change was slightly lower than with LUVs, but the difference between on and off states was still not easily distinguishable by eye. 

:::::{tab-set}

::::{tab-item} CPRG LUVs in 7 mg/mL Agarose
:::{figure} gel-luv-agarose-0.7pct.png
:align: center
:width: 80%

Photograph of color development after 2 h at 37 °C with 2 U/mL β-galactosidase. Two gel replicates (Gel-1 and Gel-2) each show the control without pH Sensing Cells (− PLA1 ves) and both pH arms.
:::
::::

::::{tab-item} CPRG SUVs in 3.5 mg/mL Agarose and in Solution
:::{figure} gel-and-solution-suv-agarose-0.35pct.png
:align: center
:width: 80%

Photograph of color development after 5.5 h at 37 °C with 1.2 U/mL β-galactosidase, in solution and in gel. The control without pH Sensing Cells and the pH 7.6 arm stay yellow in both rows. The pH 6.3 arm turns pink in both rows.
:::


::::

:::::

The starting volume of the SUV preparation was raised to increase the yield. More washes were done to lower the background color change. The agarose concentration was lowered from 7 mg/mL to 3.5 mg/mL to reduce liposome lysis during gel embedding. A solution assay was run in parallel as a control. Color change was distinct between ON and OFF states in both gel and in solution.

(colorimetric-ph-sensor-process)=
# Process

- [Anneal pH Trigger Duplex](../../processes/anneal-ph-trigger-duplex/main.md) makes the gate duplex of the pH Sensing Cell.
- [Encapsulation: Freeze-Thaw](../../processes/encapsulate-freeze-thaw/main.md) makes the CPRG liposomes as LUVs, and as SUVs from the second gel run onward.
- [Protocol: Inverted Emulsion](../../processes/assemble-base-cell/protocol-guv.md) makes the pH Sensing Cells.
- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) places the cells and liposomes in a gel.
- [Color Change: Neutralization](../../processes/color-change-neutralization/main.md) develops and reads the color. @Claude: this may be stale now

(colorimetric-ph-sensor-modules)=
# Modules

- [pH Cascade](../../modules/ph-cascade/spec.md)
- [pH Sensing Cell](../../modules/ph-sensing-cell/spec.md)
- [Detector: pH-Sensing](../../modules/detector-ph/spec.md)
- [Substrate LUV: CPRG](../../modules/substrate-cprg-luv/spec.md)
- [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md)
- [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md)
- [Color Change](../../modules/color-change/spec.md)

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this page include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Two Vesicle Colorimetric pH Sensor System
:link: https://devnotes.nucleus.engineering/articles/01a0ea82-2101-7fed-82f9-1d8ef9258009
:footer: Sung-Won Hwang, Samuel Chen, Allen P. Liu · DevStudio 2026

![](https://pub.curvenote.com/01a1659e-fe19-7cd1-8542-37ff98753726/public/overview-schematic-a686967b8ee4691359ab0bc0bd9be620.webp)
:::

::::
