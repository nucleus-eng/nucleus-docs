---
title: "Protocol: Inverted Emulsion"
subtitle: "Process"
status: draft
---

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Overview

Protocol: Inverted Emulsion is a second protocol for [Encapsulation: Phase Transfer](./main.md). It encapsulates an aqueous inner solution, such as a [Cytosol](../../modules/base-cytosol/spec.md) with DNA, inside giant unilamellar vesicles (GUVs). Sonication and heat disperse the lipids in mineral oil. This lipid-in-oil dispersion rests on the outer solution for 10 min to 20 min to form the oil–water interface. The inner solution is emulsified in the dispersion by pipetting for 3 min. The droplets are layered on the interface and centrifuged through it at 2500 g and 15 °C. Use this protocol for the [pH Sensing Cell](../../modules/ph-sensing-cell/spec.md). The Module specification gives the inner solution, the membrane and the outer solution.

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

**Chloroform** - Irritant, possible carcinogen. Work in a fume hood and use gloves.

::::::

:::{table} Lipid stocks for the lipid-in-oil dispersion at the 3 mL working scale (1.5 µmol of total lipid, 899.1 / 99.9 / 1 mmol/mol). Scale all three volumes together for another volume of oil.
:label: tbl-protocol-guv-lipids
:align: center

| Component | Stock concentration (mg/mL) | Volume to add (µL) | Target (mmol/mol) |
| --- | --- | --- | --- |
| POPC | 25 | 41.0 | 899.1 |
| Cholesterol | 50 | 1.16 | 99.9 |
| Liss-Rhod PE | 1 | 1.95 | 1 |
:::

# Materials and Equipment

:::{table} Materials for the lipid-in-oil dispersion.
:label: tbl-protocol-guv-materials
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| ---- | -------- | ------- | ------------ | ------ | ----- | ------- | ---- |
| POPC | Lipid | 16:0-18:1 PC 25 mg/mL | Avanti Lipids | A80557 | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Cholesterol | Lipid | Cholesterol (plant) | Avanti Research | A80100 | $261.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant) |
| Liss-Rhod PE | Lipid | 18:0 Liss Rhod PE 1 mg/mL | Avanti Lipids | A81179 | $273.47 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe) |
| Mineral oil, light | Chemical | Mineral oil, BioReagent, for molecular biology, light oil | Millipore Sigma | M5904-500ML | $78.70 | RT | [link](https://www.sigmaaldrich.com/US/en/product/sigma/m5904) |
:::

A 20 mL glass vial, argon gas, a vacuum desiccator, a bath sonicator, a 60 °C heat block, 1.5 mL tubes, 0.2 mL PCR tubes, and a refrigerated centrifuge are also required. The inner solution and the outer solution come from the Module specification.

# Protocol

## Prepare the Lipid-in-Oil Dispersion

- [ ] **Combine the three lipid stocks in a 20 mL glass vial.** Use the volumes in the lipid table in the Overview. All three stocks are in chloroform.
- [ ] **Remove the chloroform under a gentle argon flow.**
- [ ] **Dry the vial in a vacuum desiccator for 30 min.**
- [ ] **Resuspend the lipids in 3 mL of mineral oil.** The result is 0.5 mM total lipid in oil.
- [ ] **Seal the vial and disperse the lipids.** Do four operations in this order:
    - [ ] Bath sonicate for 20 min.
    - [ ] Incubate at 60 °C for 1 h.
    - [ ] Vortex for 2 min.
    - [ ] Bath sonicate for 20 min.

## Form the Oil–Water Interface

- [ ] **Layer 300 µL of the lipid-in-oil dispersion gently over 400 µL of outer solution in a 1.5 mL tube.**
- [ ] **Incubate the tube at room temperature for 10 min to 20 min.**

## Form the Emulsion

- [ ] **Prepare the inner solution in a separate 1.5 mL tube.** Do this during the incubation. The pH Sensing Cell uses 20 µL.
- [ ] **Add 600 µL of the lipid-in-oil dispersion to the inner solution.**
- [ ] **Pipette up and down thoroughly for 3 min.** This forms water-in-oil monolayer emulsion droplets.

## Transfer and Collect the GUVs

- [ ] **Add the droplets on top of the oil–water interface.**
- [ ] **Centrifuge at 2500 g for 15 min at 15 °C.**
- [ ] **Remove the oil phase carefully with a pipette.**
- [ ] **Collect the GUVs into a 0.2 mL PCR tube with a fresh pipette tip.**
- [ ] **Resuspend the GUVs gently.**

:::{attention}
@Developer: Give the maximum time between assembling the inner solution and starting the 37 °C incubation, and the volume for the final resuspension.
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
