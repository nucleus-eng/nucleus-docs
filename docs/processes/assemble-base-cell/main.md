---
title: "Encapsulation: Phase Transfer"
subtitle: "Process"
---

# Overview

Emulsion phase transfer is a general method for encapsulating an aqueous inner solution (e.g., [Cytosol](../../modules/base-cytosol/spec.md)) inside a lipid bilayer to form liposomes. In this protocol, you will make the necessary lipid precursors, form a water-in-oil emulsion from your inner solution, and transfer that emulsion across a lipid-stabilized oil–water interface into an outer solution, yielding liposomes suspended in the outer solution.

Each [Module specification](../../modules/modules-main.md) gives its own reference composition, outer solution requirements, and expected behavior once encapsulated. This page covers the encapsulation process given those parameters.

:::::{tab-set}
::::{tab-item} Membrane Composition
:::{table}
:label: comp-membrane

| Component    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 70                    | 760.076                  | 25                          | 162.17             |
| Cholesterol  | 29.95                 | 386.654                  | 50                          | 17.65              |
| Liss-Rhod PE | 0.05                  | 1301.71                  | 1                           | 4.96               |
:::

See [Base Membrane](../../modules/membrane-popc-chol/spec.md) for the full membrane spec.

::::

::::{tab-item} Assembly Composition
:::{table}
:label: comp-assembly

| **Component**  | **Volume (µL)** |
| -------------- | --------------- |
| Inner Solution | 30              |
| Lipid-oil      | 150             |
| Outer Solution | 300             |

:::

::::

:::::

# Materials and Equipment

:::{table}
:label: bom-assemble-base-cell
:align: center

| Name                            | Category   | Product                                                                                                                                | Manufacturer          | Part #      | Price        | Storage        | Link                                                                                                                                                                                                                      |
| ------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----------- | ------------ | -------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Optiprep                        | Reagent    | OptiPrep™                                                                                                                              | STEMCELL Technologies | 07820       | $289.00      | RT             | [link](https://www.stemcell.com/products/optipreptm.html)                                                                                                                                                                 |
| POPC                            | Lipid      | 16:0-18:1 PC 25 mg/mL                                                                                                                  | Avanti Lipids         | A80557      | $435.00      | -20 °C         | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc)                                                                                                                                      |
| Cholesterol                     | Lipid      | Cholesterol (plant)                                                                                                                    | Avanti Research       | A80100      | $261.00      | -20 °C         | [link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant)                                                                                                                                    |
| Liss-Rhod PE                    | Lipid      | 18:0 Liss Rhod PE 1 mg/mL                                                                                                              | Avanti Lipids         | A81179      | $273.47      | -20 °C         | [link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe)                                                                                                                                     |
| Glucose                         | Chemical   | D-(+)-Glucose, 99%                                                                                                                     | Thermo Scientific     | A16828-36   | $41.65       | RT             | [link](https://www.thermofisher.com/order/catalog/product/A16828.36)                                                                                                                                                      |
| Chloroform                      | Chemical   | Chloroform, suitable for HPLC, ≥99.8%, contains 0.5-1.0% ethanol as stabilizer                                                         | Sigma-Aldrich         | 366927      | $94.30       | RT (fume hood) | [link](https://www.sigmaaldrich.com/US/en/product/sigald/366927)                                                                                                                                                          |
| Mineral oil                     | Chemical   | Mineral oil, mixed weight                                                                                                              | Thermo Scientific     | AC415080010 | $53.40       | RT             | [link](https://www.thermofisher.com/order/catalog/product/AC415080010)                                                                                                                                                    |
| Glass syringe 250 µL            | Equipment  | Hamilton glass syringe                                                                                                                 | Hamilton              | 14-815-238  | $150.15      | RT             | [link](https://www.fishersci.com/shop/products/800-microliter-syringes-rn-termination/14815238)                                                                                                                           |
| Glass serological pipette 10 mL | Equipment  | PYREX® 10 mL Disposable Glass Serological Pipets, TD, Individually Wrapped, Sterile, Plugged                                           | Corning               | 7077-10N    | $690.49/case | RT             | [link](https://ecatalog.corning.com/life-sciences/b2c/US/en/Glassware/Serological-Pipets%2C-Glass/PYREX%C2%AE-Disposable-Glass-Serological-Pipets%2C-Individually-Wrapped%2C-Sterile%2C-Plugged%2C-To-Deliver/p/7077-10N) |
| Glass vials                     | Consumable | Vials, screw top, graduated, solid cap, preassembled, volume 4 mL, clear glass vial, thread 13-425, O.D. x H 15 mm x 45 mm, PTFE liner | Supelco               | 27506-U     | $157.41      | RT             | [link](https://www.sigmaaldrich.com/US/en/product/supelco/27506u)                                                                                                                                                         |
| 384-well glass bottom plate     | Consumable | 384 well glass bottom plate, 1.5 cover glass (20/case)                                                                                 | Cellvis               | P384-1.5H-N | $423.00      | RT             | [link](https://www.cellvis.com/_384-well-glass-bottom-plate-with-high-performance-number-1.5-cover-glass_/product_detail.php?product_id=53)                                                                               |

:::

# Protocol

## Prepare Lipids in Mineral Oil

- [ ] Add 1 mL of mineral oil to the glass vial using a 1 mL pipette.

:::{warning} Warning
:class: simple
:icon: false
Work inside of a fume hood when handling chloroform and lipids.
:::

- [ ] Add the lipids in the above {ref}`comp-membrane` to the glass vial on top of the mineral oil using the appropriate glass syringe.
- [ ] Briefly vortex the lipid-oil mixture for 5 s to mix.
- [ ] Evaporate the chloroform from the lipid–oil mixture:
    - [ ] Place glass vial in a 55 °C dry bath in a fume hood.
    - [ ] Shield with aluminum foil to protect from light.
    - [ ] Evaporate uncovered for 4 h.
- [ ] In a glass bottle, add 4 mL of chloroform using a glass 10 mL serological pipette.
- [ ] Clean syringes by rinsing with chloroform 5 times into an empty glass bottle. Store the syringes with the plunger removed inside the fume hood for 3 h to 4 h to allow remaining chloroform to evaporate.
- [ ] After 4 h of incubation at 55 °C in a dry bath in a fume hood, allow the lipid-oil mixture to cool to room temperature for 10 min to 15 min.

:::{hint} Note
:class: simple
:icon: false
The lipid–oil mixture can be used immediately after cooling to room temperature or stored at 4 °C for up to one week. Protect from light by storing in an opaque container or wrapping the vial with aluminum foil.
:::

- [ ] Return the plungers to the syringes and store them in their designated location.
- [ ] Dispose of chloroform waste following applicable chemical safety guidelines.

## Assemble Outer Solutions

- [ ] Prepare 1.5 mL microcentrifuge tubes labeled with the appropriate reaction.
- [ ] Mix glucose stock solution and water according to the following table:

:::{table} Preparation of outer solutions. These values are approximates and may vary based on the measured osmolarity of your inner solution.
:name: os-prep

| **Component**     | **Cells + deGFP DNA (µL)** | **Cells - deGFP DNA (µL)** |
| ----------------- | -------------------------- | -------------------------- |
| **Glucose (2 M)** | 570                        | 570                        |
| **Water**         | 430                        | 430                        |
| **Total**         | 1000                       | 1000                       |

:::

:::{hint} Note
:class: simple
:icon: false
The values shown are for encapsulating [Base Cytosol](../../modules/base-cytosol/spec.md). Measure the osmolarity of your inner solution and adjust the outer solution's glucose concentration so its osmolarity is 100 mOsm to 120 mOsm lower than the inner solution.
:::

:::{danger} Critical
:class: simple
:icon: false
Adjust the outer solution concentration so its osmolarity is 100 mOsm to 120 mOsm lower than the inner solution when measured on a Wescor EliTech Vapro 5600 Vapor Pressure Osmometer. 
:::

## Encapsulate Inner Solution

- [ ] Set up a 1.5 mL tube rack with two 1.5 mL microcentrifuge tubes for each liposome encapsulation. Number the tubes according to the number of reactions assembled. Label the two tubes for each reaction:
    - [ ] **T**—transfer
    - [ ] **L**—liposomes
- [ ] Add 300 µL of the appropriate glucose outer solution to each of the tubes labeled **T**.
- [ ] Add 150 µL of the lipid-oil mixture (at room temperature) on top of each assembled inner solution reaction.
- [ ] Emulsify the lipid-oil and inner solution reaction by running the tube along a row of empty slots on the 1.5 mL tube rack. Run it down 20–30 times until the solution forms a stable emulsion with a consistent milky color.

:::{hint} Tip
:class: simple
:icon: false
While running the tubes on the tube rack, hold the cap firmly to prevent it from coming off during vigorous mixing. 
:::

- [ ] Immediately layer each emulsion over the outer solution. Slowly pipette the entire emulsion down the side of the corresponding **T** tube.
- [ ] Centrifuge **T** tubes at 9000 g for 10 min at room temperature to pellet the liposomes.

:::{hint} Tip
:class: simple
:icon: false
Align the hinges of each T tube towards the outside of the centrifuge rotor, so that the final pellet location will be indicated by the tube hinge since the liposome pellet may not always be visible.
:::

- [ ] Extract the liposomes from each **T** tube:
    - [ ] Remove the oil layer and lipid debris from the top of each **T** tube by gently pipetting with a 1000 µL pipette set to 800 µL.
    - [ ] Gently pipette mix the pellet 10-15 times with the outer solution.
    - [ ] Extract liposomes by pipetting 50 µL to 100 µL of pellet and outer solution from **T** and transfer liposome sample to the respective liposome tube **L**.

:::{danger} Critical
:class: simple
:icon: false
Do not transfer the entire solution. It is important to avoid transferring the top of the solution which may contain a residual oil layer. 
:::

- [ ] Hold liposomes on ice until you are prepared to begin measurement.
- [ ] Pipette the liposomes into a well on a 384-well glass bottom plate. If the density appears too high under the microscope, dilute the liposomes with the outer solution for better data analysis.
- [ ] Observe liposomes by fluorescence microscopy.

# Downloads

::::{grid} 1 1 1 1

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/assemble-base-cell-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/assemble-base-cell-bom.pdf>`
:::

::::
