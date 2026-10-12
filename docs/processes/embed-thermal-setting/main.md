---
title: "Embedding: Thermal Setting"
subtitle: "Process"
status: draft
---

# Overview

Embedding: Thermal Setting holds a sample in an agarose gel that sets on cooling. The agarose is dissolved hot in the outer solution and kept warm until the sample is mixed in. This page covers [Gel: ULGA](../../modules/gel-ulga/spec.md) and [Gel: LGA](../../modules/gel-lga/spec.md), which share the steps and differ in the parameters below.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{figure} ./resources/schematic.png
:label: fig-gel-schematic
:width: 100%
:align: center

Schematic representation of unilamellar liposomes held in a hydrogel matrix.
:::

:::{table} Parameters of each gel.
| Parameter | Gel: ULGA | Gel: LGA |
| --- | --- | --- |
| Stock concentration | 10 mg/mL | 28 mg/mL |
| Dissolve | Microwave | 95 °C heat block |
| Hold until use | 55 °C bead bath | 45 °C |
| Stock per well, before mixing | 15 µL of stock | 7.5 µL of stock and 7.5 µL of outer solution |
| Final concentration | 5 mg/mL | 7 mg/mL |
| Gel point | About 8 °C to 15 °C | About 24 °C to 28 °C |
:::

# Materials and Equipment

:::{table} Reagents.
| Item | Used for | Supplier and part number |
| --- | --- | --- |
| Ultra-low gelling agarose | Gel: ULGA | Not stated |
| Low gelling agarose | Gel: LGA | Sigma-Aldrich A9414-5G |
| Glucose | Outer solution | Sigma-Aldrich |
| HEPES | Outer solution | Sigma-Aldrich |
:::

:::{table} Equipment.
| Item | Used for |
| --- | --- |
| Microwave | Dissolving ULGA |
| 95 °C heat block | Dissolving LGA |
| 55 °C bead bath | Holding ULGA |
| Not stated | Holding LGA at 45 °C |
| Vortex mixer | Dissolving LGA |
| 96-well or 384-well plate | Plating |
:::

:::{attention} Some suppliers, part numbers and instruments are not stated
@Editor: give the supplier and catalog number of the ULGA, the catalog numbers of the glucose and the HEPES, and say which instrument holds the 45 °C temperature.
:::

# Protocol

## Prepare the Outer Solution

- [ ] **Prepare the outer solution.**
    - [ ] Use the outer solution the sample was prepared in: glucose and 50 mM HEPES, at a final osmolarity of about 1200 mOsm.

:::{attention} Glucose concentration is not stated
@Editor: give the glucose concentration of the outer solution and how its osmolarity is measured and adjusted. Link the step to `assemble-solution` (Layer 1), with the outer solution's components as its inputs, once it is on `main`.
:::

:::{attention} Two stocks have two recipes
@Editor: confirm the ULGA outer solution and the LGA stock. The DevNote's supplement gives the ULGA outer solution as 1057 Osm of glucose, against about 1200 mOsm here. It gives the LGA stock as 2.70 % in ultrapure water (40.5 mg in 1500 µL), which is 27 mg/mL, against 28 mg/mL in the outer solution here.
:::

## Prepare the ULGA Stock

- [ ] **Dissolve the ULGA.**
    - [ ] Prepare ULGA at 10 mg/mL in the outer solution.
    - [ ] Microwave in 10 s bursts, 5–7 times, until the ULGA is fully dissolved.
- [ ] **Hold the stock.**
    - [ ] Keep the stock on a 55 °C bead bath until use.

## Prepare the LGA Stock

- [ ] **Dissolve the LGA.**
    - [ ] Dissolve LGA at 28 mg/mL in the outer solution, adjusting to a final osmolarity of about 1200 mOsm.
    - [ ] Heat the solution in a 95 °C heat block until the LGA is fully dissolved. Vortex occasionally to help it dissolve.
- [ ] **Hold the stock.**
    - [ ] Transfer an aliquot to a tube and keep it at 45 °C until use.

:::{hint} LGA can set at room temperature
:class: dropdown
Keeping the stock warm prevents it from setting before it is mixed with the sample.
:::

- [ ] **Dilute the stock for each well.**
    - [ ] Combine 7.5 µL of the LGA stock with 7.5 µL of the outer solution.

:::{attention} Dilution per well is inferred
@Editor: confirm that the 15 µL of gel stock per well is 7.5 µL of LGA stock and 7.5 µL of outer solution. The DevNote gives the final LGA concentration as 7 mg/mL with the parenthetical 7.5 µL and 7.5 µL of outer solution.
:::

## Mix with the Sample and Plate

- [ ] **Mix the sample with the gel precursor.**
    - [ ] For ULGA, combine 15 µL of sample with 15 µL of the ULGA stock.
    - [ ] For LGA, combine 15 µL of sample with the 15 µL of diluted LGA stock at 45 °C.
- [ ] **Plate the mixture.**
    - [ ] Dispense 30 µL per well into a 96-well or 384-well plate. Plate each sample in duplicate.
    - [ ] Plate the sample in its outer solution, with no gel, as a reference.

:::{attention} Mixing and setting are not described for ULGA
@Editor: state the temperature at which the ULGA stock is mixed with the sample, and how and where each plated mixture is cooled to its gel point.
:::
