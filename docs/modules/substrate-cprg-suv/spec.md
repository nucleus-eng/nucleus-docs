---
title: "Substrate SUV: CPRG"
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

Substrate SUV: CPRG encapsulates the chromogenic substrate chlorophenol red-β-D-galactopyranoside (CPRG) in small unilamellar vesicles (SUVs) with a POPC/cholesterol membrane. It is a substrate population of the [pH Cascade](../ph-cascade/spec.md). The SUVs are made by [Encapsulation: Freeze-Thaw](../../processes/encapsulate-freeze-thaw/main.md) with an extra extrusion through a 400 nm membrane. Intact SUVs keep CPRG inside. A lytic enzyme such as phospholipase A1 (PLA1) disrupts the membrane, and CPRG is released into the outer solution. There, [β-galactosidase](../reporter-lacz-enzyme/spec.md) converts the yellow CPRG into the purple chlorophenol red (CPR).

:::{attention}
@Developer: The DevNote calls liposomes extruded through a 400 nm membrane SUVs. Confirm the size term, or give the measured size.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} Inner Solution

:::{table} Inner solution of Substrate SUV: CPRG.
:label: comp-substrate-cprg-suv-inner-solution

| Component | Final concentration | Volume for one preparation (µL) |
| --- | --- | --- |
| CPRG | not documented | not documented |
| Other components | not documented | not documented |
| Total volume (µL) | | 1000 |
:::

:::{attention}
@Developer: Give the composition of the SUV inner solution.
:::
::::

::::{tab-item} Membrane

:::{table} Membrane. Volumes are for the lipid stocks that make 2 µmol of total lipid, the same film as Substrate LUV: CPRG.
:label: comp-substrate-cprg-suv-membrane

| Component | Target (mmol/mol) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| --- | --- | --- | --- | --- |
| POPC | 899.1 | 760.076 | 25 | 54.67 |
| Cholesterol | 99.9 | 386.654 | 50 | 1.55 |
| Liss-Rhod PE | 1 | 1301.71 | 1 | 2.60 |
:::
::::

::::{tab-item} Outer Solution

:::{table} Suspension buffer, the outer solution after preparation. Its pH is 8, and its osmolarity is 1170 mOsm/kg to 1180 mOsm/kg.
:label: comp-substrate-cprg-suv-outer-solution

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

Substrate SUV: CPRG is expected to stay yellow in solution when pH Sensing Cells are present at pH 7.6, 5.5 h after β-galactosidase is added. Data are in the [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md), read by [Colorimetric Readout](../../processes/colorimetric-readout/main.md).

## Gels

Substrate SUV: CPRG is expected to stay yellow in 3.5 mg/mL low-gelling agarose when pH Sensing Cells are present at pH 7.6, 5.5 h after β-galactosidase is added. In 7 mg/mL low-gelling agarose, the color difference between the pH arms and the control was not visible by eye, and the yields of SUVs and cells were lower. Data are in the [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md), read by [Colorimetric Readout](../../processes/colorimetric-readout/main.md).

# Requirements

Requires a membrane-lytic activity to release CPRG (e.g. the [pH Sensing Cell](../ph-sensing-cell/spec.md), which expresses PLA1).

Requires β-galactosidase in the outer solution to convert released CPRG (e.g. [Reporter: LacZ Enzyme](../reporter-lacz-enzyme/spec.md)).

# Implementations

- [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md)

# Processes

- [Encapsulation: Freeze-Thaw](../../processes/encapsulate-freeze-thaw/main.md) makes the SUVs: the lipid film is hydrated in 1 mL of inner solution, and the suspension is extruded through a 400 nm membrane in 13 passes.
- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) places them in a gel.
- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) develops the color of released CPRG.

# Materials

:::{table}
:label: bom-substrate-cprg-suv
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| ---- | -------- | ------- | ------------ | ------ | ----- | ------- | ---- |
| CPRG | Reagent | Chlorophenol Red-β-D-galactopyranoside | Roche | 10884308001 | $160.00 | -20 °C in water at 20 mg/mL | [link](https://www.sigmaaldrich.com/US/en/product/roche/10884308001) |
| Optiprep | Reagent | OptiPrep™ | STEMCELL Technologies | 07820 | $289.00 | RT | [link](https://www.stemcell.com/products/optipreptm.html) |
| HEPES | Salts | HEPES, Crystalline Powder, ≥99.5% (titration), Poly bottle | Sigma-Aldrich | H3375-500G | $431 | 4 °C to 30 °C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/h3375) |
| POPC | Lipid | 16:0-18:1 PC 25 mg/mL | Avanti Lipids | A80557 | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Cholesterol | Lipid | Cholesterol (plant) | Avanti Research | A80100 | $261.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant) |
| Liss-Rhod PE | Lipid | 18:0 Liss Rhod PE 1 mg/mL | Avanti Lipids | A81179 | $273.47 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe) |
| Liposome extruder | Equipment | Mini Extruder Pro Kit with base | Avanti Lipids | A81411 | | RT | [link](https://www.avantiresearch.com/en-gb/products/product/1000061-mini-extruder-pro-kit-with-base) |
| Membrane filter, 400 nm | Consumable | PC Membranes 0.4 µm, 19 mm | Avanti Lipids | A89040 (legacy 610007) | | RT | [link](https://www.avantiresearch.com/en-gb/products/product/610007-pc-membranes-04m) |
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
