---
title: "Substrate LUV: CPRG"
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

Substrate LUV: CPRG encapsulates the chromogenic substrate chlorophenol red-β-D-galactopyranoside (CPRG) in large unilamellar vesicles (LUVs) with a POPC/cholesterol membrane. It is a substrate population of the [pH Cascade](../ph-cascade/spec.md). Intact LUVs keep CPRG inside. A lytic enzyme such as phospholipase A1 (PLA1) disrupts the membrane, and CPRG is released into the outer solution. There, [β-galactosidase](../reporter-lacz-enzyme/spec.md) converts the yellow CPRG into the purple chlorophenol red (CPR). The LUVs are made by [Encapsulation: Freeze-Thaw](../../processes/encapsulate-freeze-thaw/main.md) without extrusion. [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md) is the extruded alternative.

:::{attention}
@Developer: Give the measured size and the lamellarity of the LUVs, which are made without extrusion.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} Inner Solution

:::{table} Inner solution of Substrate LUV: CPRG.
:label: comp-substrate-cprg-luv-inner-solution

| Component | Stock concentration | Final concentration | Volume for one preparation (µL) |
| --- | --- | --- | --- |
| CPRG | 30 mg/mL | 14.25 mg/mL | 237.5 |
| Optiprep | 1000 mL/L | 100 mL/L | 50 |
| Tris1M-HEPES1.15M buffer stock | 2520 mOsm | 1071 mOsm | 212.5 |
| Total volume (µL) | | | 500 |
:::

The Tris1M-HEPES1.15M buffer stock is 1 M Tris and 1.15 M HEPES at pH 8, about 2520 mOsm/kg, measured. The 1071 mOsm is the contribution of the buffer stock to the inner solution.

:::{attention}
@Developer: The storage of CPRG is given as 20 mg/mL in water, and this table uses a 30 mg/mL stock. Confirm the stock concentration.
:::
::::

::::{tab-item} Membrane

:::{table} Membrane. Volumes are for the lipid stocks that make 2 µmol of total lipid.
:label: comp-substrate-cprg-luv-membrane

| Component | Target (mmol/mol) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| --- | --- | --- | --- | --- |
| POPC | 899.1 | 760.076 | 25 | 54.67 |
| Cholesterol | 99.9 | 386.654 | 50 | 1.55 |
| Liss-Rhod PE | 1 | 1301.71 | 1 | 2.60 |
:::
::::

::::{tab-item} Outer Solution

:::{table} Suspension buffer, the outer solution after preparation. Its pH is 8, and its osmolarity is 1170 mOsm/kg to 1180 mOsm/kg.
:label: comp-substrate-cprg-luv-outer-solution

| Component | Concentration |
| --- | --- |
| Tris1M-HEPES1.15M buffer stock | 466.7 mL/L |
:::

The Tris1M-HEPES1.15M buffer stock is 1 M Tris and 1.15 M HEPES at pH 8, about 2520 mOsm/kg, measured.

:::{attention}
@Developer: Confirm that this is the outer solution used in the wash steps, and give the diluent of the 466.7 mL/L.
:::
::::

:::::

# Expected Behavior

## Solution

:::{warning} Not yet validated
This page does not report color development of Substrate LUV: CPRG in solution.
:::

## Gels

Substrate LUV: CPRG is expected to keep CPRG inside until a lytic enzyme such as PLA1 disrupts the membrane. In 7 mg/mL low-gelling agarose it does not: LUVs develop color without PLA1, which points to CPRG leakage. The control without pH Sensing Cells turned pink after β-galactosidase was added. Data are in the [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md), read by [Colorimetric Readout](../../processes/colorimetric-readout/main.md).

# Requirements

Requires a membrane-lytic activity to release CPRG (e.g. the [pH Sensing Cell](../ph-sensing-cell/spec.md), which expresses PLA1).

Requires β-galactosidase in the outer solution to convert released CPRG (e.g. [Reporter: LacZ Enzyme](../reporter-lacz-enzyme/spec.md)).

# Implementations

- [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md)

# Processes

- [Encapsulation: Freeze-Thaw](../../processes/encapsulate-freeze-thaw/main.md) makes the LUVs, with the lipid film hydrated in 0.5 mL (4 mM total lipid).
- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) places them in a gel.
- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) develops the color of released CPRG.

# Materials

:::{table}
:label: bom-substrate-cprg-luv
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| ---- | -------- | ------- | ------------ | ------ | ----- | ------- | ---- |
| CPRG | Reagent | Chlorophenol Red-β-D-galactopyranoside | Roche | 10884308001 | $160.00 | -20 °C in water at 20 mg/mL | [link](https://www.sigmaaldrich.com/US/en/product/roche/10884308001) |
| Optiprep | Reagent | OptiPrep™ | STEMCELL Technologies | 07820 | $289.00 | RT | [link](https://www.stemcell.com/products/optipreptm.html) |
| HEPES | Salts | HEPES, Crystalline Powder, ≥99.5% (titration), Poly bottle | Sigma-Aldrich | H3375-500G | $431 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/h3375) |
| POPC | Lipid | 16:0-18:1 PC 25 mg/mL | Avanti Lipids | A80557 | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Cholesterol | Lipid | Cholesterol (plant) | Avanti Research | A80100 | $261.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant) |
| Liss-Rhod PE | Lipid | 18:0 Liss Rhod PE 1 mg/mL | Avanti Lipids | A81179 | $273.47 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe) |
:::

:::{attention}
@Developer: Give the manufacturer and part number of Tris base.
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
