---
title: "Colorimetric Readout"
subtitle: "Process"
status: draft
---

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Overview

Colorimetric Readout develops and reads the color of a system that holds a color reporter. The reporter used here is β-galactosidase (LacZ). It converts the yellow substrate chlorophenol red-β-D-galactopyranoside (CPRG) into the purple chlorophenol red (CPR). The enzyme is added to a sample of gel or solution as a 3× solution in a basic buffer at pH 9.9, to a final concentration of 1.2 U/mL. The basic buffer raises the pH of the sample so that β-galactosidase can act. The sample is then incubated at 37 °C, and the color is read by eye and recorded by photograph, so the result is a color and not a number. The system documented here is the [pH Cascade](../../modules/ph-cascade/spec.md), where lysis of substrate liposomes ([Substrate LUV: CPRG](../../modules/substrate-cprg-luv/spec.md) or [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md)) releases CPRG into the outer solution. The enzyme is the [LacZ Enzyme Reporter](../../modules/reporter-lacz-enzyme/spec.md).

# Materials and Equipment

β-galactosidase at 1000 U/mL, 1 M Tris base, and 37 % HCl are required. The sample is a 60 µL gel or a 60 µL solution. The β-galactosidase is from *Escherichia coli* (Sigma-Aldrich G5635, Grade VIII, lyophilized powder, ≥500 units/mg protein).

:::{attention}
@Developer: Give the manufacturer and catalog number of Tris base. None of the DevCell_Materials_Tracker sheet, the Chicago demo-status doc, the distribution's materials reference, or any supporting DevNote names a vendor for it.
:::

# Protocol

## Prepare the Basic Buffer

- [ ] **Mix 1 mL of 1 M Tris base with 2.5 µL of 37 % HCl.** The buffer has a pH of 9.9 and a measured osmolarity of 1165 mOsm/kg. Its job is to raise the pH of the sample when it is added.

## Prepare the 3× β-Galactosidase Solution

- [ ] **Dilute the 1000 U/mL β-galactosidase stock to 3.6 U/mL in the pH 9.9 basic buffer.**

## Develop the Color

- [ ] **Add 30 µL of the 3× solution to 60 µL of gel or solution.** The total volume is 90 µL, and the final concentration is 1.2 U/mL β-galactosidase.
- [ ] **Incubate at 37 °C.** The reported runs read the color after 2 h (at 2 U/mL) and after 5.5 h (at 1.2 U/mL).
- [ ] **Read the color by eye and photograph the wells.** CPRG is yellow, and CPR is purple.

:::{attention}
@Developer: Give the recommended incubation time.
:::

# Credits

Developed by [Sung-Won Hwang](https://orcid.org/0000-0003-1686-7090), [Samuel Chen](https://orcid.org/0000-0001-8501-7175) and [Allen P. Liu](https://orcid.org/0000-0002-0309-7018) (University of Michigan).

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
