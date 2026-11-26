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

(reporter-lacz-enzyme-overview)=
# Overview

The LacZ Enzyme Reporter uses β-galactosidase (LacZ) to convert the substrate chlorophenol red-β-D-galactopyranoside (CPRG, yellow) into chlorophenol red (CPR, purple). It can be used to read out either expression level (by expressing LacZ) or presence of CPRG (e.g., as released from lysed liposomes such as [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md)). 

(reporter-lacz-enzyme-reference-composition)=
# Reference Composition

:::{table} Reaction composition. The final concentration is the concentration after the enzyme is added to a 60 µL sample, which gives 90 µL.
:label: comp-reporter-lacz-enzyme-reaction

| Component | Final concentration |
| --- | --- |
| β-galactosidase | 1.2 U/mL |
| CPRG | at most 0.33 mg/mL |
:::

CPRG enters the reaction inside liposomes, so its concentration depends on how many liposomes lyse. The 0.33 mg/mL is the ceiling when every liposome lyses. [Substrate LUV: CPRG](../substrate-cprg-luv/spec.md) holds 14.25 mg/mL CPRG, a 60 µL solution assay takes 2.1 µL of the liposomes, and the enzyme dilutes the sample to 90 µL. [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md) is taken to hold the same 14.25 mg/mL.

(reporter-lacz-enzyme-expected-behavior)=
# Expected Behavior

(reporter-lacz-enzyme-solution)=
## Solution

The LacZ Enzyme Reporter is expected to convert yellow CPRG to purple CPR in solution. At 1.2 U/mL β-galactosidase, with CPRG released from [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md), the color was visible by eye after 5.5 h at 37 °C. The CPRG concentration in that run was at most 0.33 mg/mL. Data are in the [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md).

(reporter-lacz-enzyme-gels)=
## Gels

The LacZ Enzyme Reporter is expected to show a visible color change in 3.5 mg/mL [low-gelling agarose](../../modules/gel-lga/spec.md). 1.2 U/mL β-galactosidase gave a visible color change after 5.5 h at 37 °C. In 7 mg/mL low-gelling agarose, 2 U/mL gave a visible color after 2 h in all wells, including the negative control. The leakage is described on [Substrate LUV: CPRG](../substrate-cprg-luv/spec.md). Data are in the [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md).

(reporter-lacz-enzyme-requirements)=
# Requirements

Requires CPRG in the outer solution, for example free CPRG, or released from substrate [LUVs](../substrate-cprg-luv/spec.md) or [SUVs](../substrate-cprg-suv/spec.md).

Requires the outer solution to be neutral or basic (> pH 7.0) in order for β-galactosidase to catalyze its reaction.

(reporter-lacz-enzyme-implementations)=
# Implementations

- [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md)

(reporter-lacz-enzyme-processes)=
# Processes

- [Color Change: Neutralization](../../processes/color-change-neutralization/main.md) for acidic reactions, neutralizes outer solution adds the enzyme after the substrate is released, and reads the color.

(reporter-lacz-enzyme-materials)=
# Materials

:::{table}
:label: bom-reporter-lacz-enzyme
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| ---- | -------- | ------- | ------------ | ------ | ----- | ------- | ---- |
| β-galactosidase | Reagent | β-Galactosidase from Escherichia coli, Grade VIII, lyophilized powder, ≥500 units/mg protein | Sigma-Aldrich | G5635 | | −20 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/g5635) |
:::

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this specification include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Co-Encapsulated Cell-Free PLA1 Expression in beta-Galactosidase GUVs
:link: https://devnotes.nucleus.engineering/articles/01a12e24-46dc-761d-b020-f1f77cce78ba
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659c-0b14-7107-9490-170bb5b0dc82/public/fig8-endpoint-abs-15-fa8ff33abe1e637358abcbe415f6130e.webp)
:::

:::{card} Double Vesicle Lysis System Leveraging deGFP CFPE
:link: https://devnotes.nucleus.engineering/articles/01a16026-42c1-71ad-842a-463d52fae7d8
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-f37b-7cd9-ac05-7f491b920d6e/public/fig1-two-vesicle-kin-b2f2e21461dd910150fd25955247d4e8.webp)
:::

:::{card} Implementing of a bulk color change module into bacterial quorum sensing
:link: https://devnotes.nucleus.engineering/articles/01a12e6c-b511-7d30-aa95-002d386f751e
:footer: Manuel Bibrowski, Charlie Newell, Jonah McDonald, Niall McIntyre, Julia Purrinos de Oliveira · DevStudio 2026

![](https://pub.curvenote.com/01a1f78f-6527-7c06-80eb-b0485a63f76a/public/colorchange-overnigh-125e6d1330fca3c802037638204f8e8d.webp)
:::

:::{card} TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning
:link: https://devnotes.nucleus.engineering/articles/01a1304b-1c56-7352-a082-ba84a2684f82
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-ebfe-71b5-b20a-66b33af95dfb/public/fig7-patterned-gel-5fc6273fa124c69e6d78ac4caafe3ce4.webp)
:::

:::{card} Theophylline-LacZ sensor validation in Nucleus Cytosol
:link: https://devnotes.nucleus.engineering/articles/019e0431-5045-7f14-a4f9-d3795e22bcdd
:footer: Maram Naji · Node: Chicago

![](https://pub.curvenote.com/01a08cd1-07b4-7981-8cf4-f888604c5608/public/pT7_theo_lacZ-7c737c9e5acb683ca9afe1c51feb6185.webp)
:::

:::{card} Triggered Lysis of beta-Galactosidase-Loaded GUVs by Cell-Free Expressed Phospholipase A1
:link: https://devnotes.nucleus.engineering/articles/01a12d42-ca2e-70e7-b78b-66fcf11c400a
:footer: Mary Kelly, Ojaswita Pant · DevStudio 2026

![](https://pub.curvenote.com/01a1fa13-9345-7c96-896f-ffdcf93f8541/public/fig1-pla1-guv-lysis--613413e22e49b3c705ea9d1a77dc733c.webp)
:::

:::{card} Two Vesicle Colorimetric pH Sensor System
:link: https://devnotes.nucleus.engineering/articles/01a0ea82-2101-7fed-82f9-1d8ef9258009
:footer: Sung-Won Hwang, Samuel Chen, Allen P. Liu · DevStudio 2026

![](https://pub.curvenote.com/01a1fa13-c6fb-7f9a-a1a1-632d636726e0/public/overview-schematic-08a74743b9e6c2c2111bc4685b549640.webp)
:::

:::{card} Understanding Liposome Behaviour in Hydrogel Matrices
:link: https://devnotes.nucleus.engineering/articles/01a10dfe-c1df-7c2d-ba5a-035280a349f7
:footer: Ojaswita Pant, Manuel Bibrowski · DevStudio 2026

![](https://pub.curvenote.com/01a1fa13-851d-7654-8d9e-eff684aa3093/public/schematic-hydrogel-o-54702d2804d2bec09c5e6e3bbd4cd0cd.webp)
:::

::::
