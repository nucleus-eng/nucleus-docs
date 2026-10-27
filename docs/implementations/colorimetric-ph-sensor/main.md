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

# Overview

The Colorimetric pH Sensor Implementation combines the [pH Cascade](../../modules/ph-cascade/spec.md), which is made of [pH Sensing Cells](../../modules/ph-sensing-cell/spec.md), substrate liposomes ([Substrate LUV: CPRG](../../modules/substrate-cprg-luv/spec.md) and [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md)) and the [LacZ enzyme](../../modules/reporter-lacz-enzyme/spec.md), with [Colorimetric Readout](../../processes/colorimetric-readout/main.md). It produces a visible color change at pH 6.3 and none at pH 7.6, in solution and in 3.5 mg/mL low-gelling agarose. Acidic pH makes the cells express phospholipase A1 (PLA1). PLA1 lyses the CPRG liposomes, and β-galactosidase converts the released CPRG from yellow to purple. Wells hold 60 µL and are incubated at 37 °C.

The data are from the DevNote [Two Vesicle Colorimetric pH Sensor System](https://devnotes.nucleus.engineering/articles/01a0ea82-2101-7fed-82f9-1d8ef9258009) by Sung-Won Hwang, Samuel Chen and Allen P. Liu.

# Protocol

## Solution Assay

The solution assay runs in a 384-well square plate with 60 µL per well. The pH 7.6 arm is plate column 4, and the pH 6.3 arm is plate column 5. The pH 6.3 arm replaces the Tris1M-HEPES1.15M buffer stock with a buffer mix for pH 6.3. The composition of the buffer mix is in the Outer Solution tab of the [pH Cascade](../../modules/ph-cascade/spec.md).

:::{table} Assembly of a 60 µL well in the solution assay.
:label: tbl-colorimetric-ph-sensor-well
:align: center

| Component | pH 7.6 arm (µL) | pH 6.3 arm (µL) |
| --- | --- | --- |
| Energy solution (2×) | 30 | 30 |
| Ultrapure water | 15.6 | 15.6 |
| Tris1M-HEPES1.15M buffer stock | 7.2 | |
| Buffer mix for pH 6.3 | | 7.2 |
| pH Sensing Cells, CPRG liposomes and suspension buffer | 7.2 | 7.2 |
| Total | 60 | 60 |
:::

The last row of the table above is a 7.2 µL slot that holds the cells, the liposomes and suspension buffer. The table below gives its split for the four wells that were imaged.

:::{table} Conditions of the four imaged wells. The suspension buffer is 466.7 mL/L Tris1M-HEPES1.15M.
:label: tbl-colorimetric-ph-sensor-conditions
:align: center

| Well | Name | Type | pH | pH Sensing Cells (µL) | CPRG liposomes (µL) | Suspension buffer (µL) |
| --- | --- | --- | --- | --- | --- | --- |
| D4 | pH 7.6, cells only | Control | 7.6 | 1 | 0 | 6.2 |
| D5 | pH 6.3, cells only | Control | 6.3 | 1 | 0 | 6.2 |
| E4 | pH 7.6, cells and liposomes | Sample | 7.6 | 3 | 2.1 | 2.1 |
| E5 | pH 6.3, cells and liposomes | Sample | 6.3 | 3 | 2.1 | 2.1 |
:::

The cells-only wells take 1 µL of cells, and the sample wells take 3 µL, so the two differ in cell dose as well as in liposomes. The four wells are imaged by fluorescence microscopy after 13 h at 37 °C.

## Gel Assay

The gel assay uses 60 µL of low-gelling agarose gel per well, set by [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md). It is the solution well with the 15.6 µL of ultrapure water replaced by 15.6 µL of a 27 mg/mL low-gelling agarose stock, which gives a final agarose concentration of 7 mg/mL. The pH 6.3 arm takes the same buffer mix as in the solution assay.

:::{table} Assembly of a 60 µL well in the gel assay, at 7 mg/mL agarose.
:label: tbl-colorimetric-ph-sensor-gel-well
:align: center

| Component | pH 7.6 arm (µL) | pH 6.3 arm (µL) |
| --- | --- | --- |
| Energy solution (2×) | 30 | 30 |
| 27 mg/mL agarose stock in ultrapure water | 15.6 | 15.6 |
| Tris1M-HEPES1.15M buffer stock | 7.2 | |
| Buffer mix for pH 6.3 | | 7.2 |
| pH Sensing Cells, CPRG liposomes and suspension buffer | 7.2 | 7.2 |
| Total | 60 | 60 |
:::

The agarose stock is 40.5 mg of low-gelling agarose (Sigma-Aldrich A9414-5G) in 1500 µL of ultrapure water. It is dissolved in a heat block at 85 °C to 95 °C with occasional vortexing, then cooled to 65 °C. The stock is mixed with the energy solution and the buffer, the mixture is cooled to 45 °C, and the cells and liposomes are added last. For 3.5 mg/mL agarose, half of the stock is replaced with ultrapure water: 7.8 µL of stock and 7.8 µL of water in place of the 15.6 µL.

The 7.2 µL slot holds 3 µL of pH Sensing Cells, 3 µL of CPRG liposomes and 1.2 µL of suspension buffer. The suspension buffer is at 1175 mOsm/kg and pH 8.

:::{attention}
@Developer: Give the steps that dispense the gel into the well and set it, with the time and temperature.
:::

## Readout

Color is developed with [Colorimetric Readout](../../processes/colorimetric-readout/main.md), which adds 30 µL of a 3× β-galactosidase solution to 60 µL of gel or solution. The 30 µL of 3× solution gives 1.2 U/mL, as in the run in 3.5 mg/mL agarose. The first gel run used 2 U/mL, and its preparation is not given.

# Performance

## Validation in Solution

In solution, acidic pH gave a visible color change.

:::{figure} solution-color-change.png
:align: center
:width: 60%

Photograph of the two-liposome system in solution at pH 7.6 (left) and pH 6.3 (right).
:::

:::{attention}
@Developer: Give the wells, the plate, the date and the time of this photograph.
:::

::::{hint} Color developed with PLA1-expressing cells and at pH 6.5, but not without them or at pH 7.4
:class: dropdown

:::{figure} initial-color-change.png
:align: center
:width: 100%

Photographs of the colorimetric response without (−) and with (+) PLA1-expressing cells (left), and at pH 7.4 and pH 6.5 (right).
:::

:::{attention}
@Developer: Give the conditions of this experiment, and say why its pH values differ from the 7.6 and 6.3 of the other results.
:::
::::

Fluorescence microscopy shows the cells in four wells after 13 h at 37 °C. Rhodamine, the membrane label, is yellow. Alexa Fluor 647 is red, and the Cy5 signal is read in it. Both populations carry Rhodamine in the membrane, so only Cy5 marks the pH Sensing Cells. Each panel is a 502 µm square at 0.465 µm per pixel, taken at the same stage coordinates in every well. The four panels share one contrast stretch per channel, so their brightness is comparable: Rhodamine from 2410 to 50690, and Alexa Fluor 647 from 1904 to 30863. The cells-only wells (D4 and D5) hold a third of the cells of the sample wells (E4 and E5), so the Cy5 outcomes of the two pairs at the same pH are not directly comparable.

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

:::{attention}
@Developer: Name the microscope, and give the objective, exposure, gain and laser power. The common contrast stretch assumes that these settings were the same for the four wells.
:::

:::{attention}
@Developer: The comparison of E5 with E4 is read from one field of view per well and is not counted. Give the number of cells with and without Cy5 in each of the four wells, or the analysis that supports a difference in the fraction.
:::

## Gel, LUVs in 7 mg/mL Agarose

The first gel run used CPRG LUVs in 7 mg/mL low-gelling agarose. A color change was visible at pH 6.3, but the control without pH Sensing Cells also developed color, so the difference was not clear. The only difference from the solution assay was the gel. Gel embedding seems to cause CPRG leakage from the LUVs, even without PLA1.

:::{figure} gel-luv-agarose-0.7pct.png
:align: center
:width: 80%

Photograph of color development after 2 h at 37 °C with 2 U/mL β-galactosidase. Two gel replicates (Gel-1 and Gel-2) each show the control without pH Sensing Cells (− PLA1 ves.) and both pH arms. All six wells develop a similar pink color.
:::

## Gel, SUVs in 7 mg/mL Agarose

To lower the CPRG leakage, the LUVs were extruded through 400 nm membranes to make SUVs, because smaller liposomes are expected to be more stable. The background was slightly lower than in the LUV run, but the difference was still not visible by eye. The yields of SUVs and of pH Sensing Cells were lower than before, so the signal was low.

## Gel and Solution, SUVs in 3.5 mg/mL Agarose

Three changes were made. The starting volume of the SUV preparation was raised to increase the yield. More washes were done to lower the background. The agarose was lowered from 7 mg/mL to 3.5 mg/mL to reduce the stress of gel embedding. A solution assay ran in parallel, to test whether the gel caused the problem. A visible color difference appeared in the gel and in solution.

:::{figure} gel-and-solution-suv-agarose-0.35pct.png
:align: center
:width: 80%

Photograph of color development after 5.5 h at 37 °C with 1.2 U/mL β-galactosidase, in solution and in gel. The control without pH Sensing Cells and the pH 7.6 arm stay yellow in both rows. The pH 6.3 arm turns pink in both rows.
:::

:::{attention}
@Developer: Give the new starting volume of the SUV preparation and the number of washes. The caption of this photograph calls the control "GUV-only", and the figure labels it "− PLA1 ves". Confirm that the control holds CPRG liposomes and β-galactosidase and no pH Sensing Cells.
:::

## Patterned Gel

The two-liposome system was also tested in a patterned hydrogel, to explore an output that a smartphone can read. A smartphone app, Hydrogel Sensor, was to read the pattern and report whether the sensor was ON or OFF. A visible color change appeared at pH 6.3, but the color developed outside the patterned region, likely because CPRG or CPR diffused over time. The app could not detect the pattern. The yellow CPRG stayed relatively inside the pattern, possibly because CPRG in SUVs diffuses less. Detecting the color change in the outer gel region, or using a less diffusive substrate such as X-gal, may improve the result.

:::{figure} patterned-gel.png
:align: center
:width: 100%

Photographs and schematic of the patterned hydrogel test. **(A)** The patterned hydrogel at 0 h, 15 h and 19 h with no PLA1 cells, at pH 7.6, and at pH 6.3. A purple or pink color appeared only at pH 6.3, after β-galactosidase was added. **(B)** Schematic of the patterned hydrogel design and of the color mechanism: PLA1 releases CPRG, and β-galactosidase converts it to CPR.
:::

:::{attention}
@Developer: The text describes a QR-code pattern, and the figure shows a cross. Confirm the pattern.
:::

## Gramicidin A

The colorimetric runs contain no gramicidin A, which the [earlier description of this pH sensor](https://doi.org/10.1101/2025.11.16.688650) uses. Gramicidin A ruptured part of the CPRG liposomes early, and this gave color without PLA1. Its absence may reduce the efficiency of pH sensing. PLA1 expression, probably driven by proton entry into a subset of cells with relatively permeable membranes, appeared to be enough to start the lysis cascade.

# Process

- [Anneal pH Trigger Duplex](../../processes/anneal-ph-trigger-duplex/main.md) makes the gate duplex of the pH Sensing Cell.
- [Encapsulation: Freeze-Thaw](../../processes/encapsulate-freeze-thaw/main.md) makes the CPRG liposomes as LUVs, and as SUVs from the second gel run onward.
- [Protocol: Inverted Emulsion](../../processes/assemble-base-cell/protocol-guv.md) makes the pH Sensing Cells.
- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) places the cells and liposomes in a gel.
- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) develops and reads the color.

# Modules

- [pH Cascade](../../modules/ph-cascade/spec.md)
- [pH Sensing Cell](../../modules/ph-sensing-cell/spec.md)
- [Detector: pH-Sensing](../../modules/detector-ph/spec.md)
- [Substrate LUV: CPRG](../../modules/substrate-cprg-luv/spec.md)
- [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md)
- [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md)
- [Color Change](../../modules/color-change/spec.md)

# Credits

Developed by [Sung-Won Hwang](https://orcid.org/0000-0003-1686-7090), [Samuel Chen](https://orcid.org/0000-0001-8501-7175) and [Allen P. Liu](https://orcid.org/0000-0002-0309-7018) (University of Michigan).

:::{attention}
@Editor: Add the Node and Lab to this credit.
:::

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
