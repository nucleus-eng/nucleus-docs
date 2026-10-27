---
title: "Encapsulation: Freeze-Thaw"
subtitle: "Process"
status: draft
---

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Overview

Encapsulation: Freeze-Thaw encapsulates an aqueous inner solution in liposomes. A dried lipid film is hydrated directly with the inner solution. The suspension is then sonicated and freeze-thawed. Repeated centrifugation washes away the solution that was not encapsulated. The route gives large unilamellar vesicles (LUVs). An extra extrusion through a 400 nm membrane gives small unilamellar vesicles (SUVs). Use this process for liposomes that carry a substrate, such as [Substrate LUV: CPRG](../../modules/substrate-cprg-luv/spec.md) and [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md). Each [Module specification](../../modules/modules-main.md) gives its own lipid composition, inner solution and outer solution.

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

**Chloroform** - Irritant, possible carcinogen. Work in a fume hood and use gloves.

**Liquid nitrogen** - Causes cold burns. Wear cryogenic gloves and eye protection.

::::::

:::{table} Parameters that differ between the LUV and SUV routes.
:label: tbl-encapsulate-freeze-thaw-routes
:align: center

| Parameter | LUV | SUV |
| --- | --- | --- |
| Inner solution added to the film | 500 µL | 1 mL |
| Extrusion | none | 400 nm membrane, 13 passes |
| Centrifugation to pellet | 10 000 g, 10 min to 20 min | 15 000 g, 10 min to 20 min |
| Pellet taken for washing | 90 µL | 75 µL |
| Outer solution added to reach 250 µL | 160 µL | 175 µL |
| Centrifugation per wash | 4000 g, 10 min | 10 000 g, 10 min |
:::

# Materials and Equipment

:::{table} Bill of Materials
:label: bom-encapsulate-freeze-thaw
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| ---- | -------- | ------- | ------------ | ------ | ----- | ------- | ---- |
| POPC | Lipid | 16:0-18:1 PC 25 mg/mL | Avanti Lipids | A80557 | $435.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc) |
| Cholesterol | Lipid | Cholesterol (plant) | Avanti Research | A80100 | $261.00 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant) |
| Liss-Rhod PE | Lipid | 18:0 Liss Rhod PE 1 mg/mL | Avanti Lipids | A81179 | $273.47 | -20 °C | [link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe) |
| Optiprep | Reagent | OptiPrep™ | STEMCELL Technologies | 07820 | $289.00 | RT | [link](https://www.stemcell.com/products/optipreptm.html) |
| Liposome extruder | Equipment | Mini Extruder Pro Kit with base | Avanti Lipids | A81411 | | RT | [link](https://www.avantiresearch.com/en-gb/products/product/1000061-mini-extruder-pro-kit-with-base) |
| Membrane filter, 400 nm | Consumable | PC Membranes 0.4 µm, 19 mm | Avanti Lipids | A89040 (legacy 610007) | | RT | [link](https://www.avantiresearch.com/en-gb/products/product/610007-pc-membranes-04m) |
:::

A 1 mL glass vial, argon or nitrogen gas, a vacuum desiccator, a bath sonicator, liquid nitrogen, a 35 °C water bath, and a centrifuge for 1.5 mL tubes are also required. The inner solution and outer solution come from the Module specification.

# Protocol

## Prepare the Lipid Film

- [ ] **Add the lipids from chloroform stocks to the bottom of a 1 mL glass vial.** The Module specification gives the lipids and volumes.
- [ ] **Dry the lipids under argon or N₂ gas.**
- [ ] **Dry the film under vacuum for 20 min.**

## Hydrate and Freeze-Thaw

- [ ] **Add the inner solution directly to the dried lipid film.** Use the volume for your route in the route table in the Overview.
- [ ] **Vortex until the film is no longer visible.**
- [ ] **Sonicate the suspension for 10 min.**
- [ ] **Run 5 freeze-thaw cycles.** One cycle is three operations:
    - [ ] Freeze in liquid nitrogen.
    - [ ] Thaw in a 35 °C water bath.
    - [ ] Vortex for 30 s.

## Extrude (SUV Only)

- [ ] **Assemble a liposome extruder with a 400 nm pore size membrane filter.**
- [ ] **Pass the lipid suspension through the extruder 13 times.**

## Wash the Liposomes

- [ ] **LUV only: dilute the suspension in outer solution.**
    - [ ] Split the suspension into tubes that each hold 50 µL of LUVs.
    - [ ] Add 200 µL of outer solution to each tube.
- [ ] **Pellet the liposomes.** Centrifuge at the speed for your route in the route table in the Overview.
- [ ] **Pool the pellets into two tubes.**
- [ ] **Take 15 µL of pellet from each of six tubes.** The total is 90 µL for LUVs and 75 µL for SUVs.
- [ ] **Add outer solution to each tube to reach a final volume of 250 µL.** Use the volume for your route in the route table in the Overview.
- [ ] **Wash 10 times.** One wash is three operations:
    - [ ] Centrifuge for 10 min at the speed for your route in the route table in the Overview.
    - [ ] Remove 200 µL of supernatant without disturbing the pellet.
    - [ ] Add 200 µL of fresh outer solution.

:::{hint} Note: Alternate the tube orientation with each wash.
:class: dropdown
Alternating the orientation moves the pellet to the opposite side of the tube. This releases unencapsulated or trapped solution that is held between liposomes.
:::

- [ ] **After the final wash, leave the tubes on ice for at least 30 min.**
- [ ] **Tap the tubes gently to resuspend the pellet.** Do not pipette.

:::{attention}
@Developer: Reconcile the pooling volumes. Six tubes at 15 µL give 90 µL, which fits the LUV route (90 µL + 160 µL = 250 µL). The SUV route also states six tubes, but 75 µL + 175 µL = 250 µL needs five tubes. The pooled pellets go into two tubes, and each tube is brought to 250 µL: say how the 90 µL or 75 µL divides between them. The LUV dilution step uses 12 tubes of 50 µL, which need 600 µL, while the CPRG LUV preparation is 500 µL. Give the number of tubes for each route.
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
