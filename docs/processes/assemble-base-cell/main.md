---
title: "Encapsulation: Phase Transfer"
subtitle: "Process"
---

# Overview

Emulsion phase transfer is a general method for encapsulating an aqueous inner solution (e.g., [Cytosol](../../modules/base-cytosol/spec.md)) inside a lipid bilayer to form liposomes. In this protocol, you will prepare your lipid mixture, form a water-in-oil emulsion from your inner solution and lipid mixture, and transfer that emulsion across an oil–water interface into an outer solution, yielding liposomes.

Each [Module specification](../../modules/modules-main.md) gives its own reference composition, outer solution requirements, and expected behavior once encapsulated. This page covers the encapsulation process given those parameters.

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

 **Chloroform** - Irritant, possible carcinogen. Work in fume hood and use gloves.

::::::

:::::{tab-set}
::::{tab-item} Membrane Composition
:::{table}
:label: comp-membrane-default

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

| Name                            | Category   | Product                                                                                                                                | Manufacturer          | Part #      | Price   | Storage                 | Link                                                                                                                                                                                                                      |
| ------------------------------- | ---------- | -------------------------------------------------------------------------------------------------------------------------------------- | --------------------- | ----------- | ------- | ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Optiprep                        | Reagent    | OptiPrep™                                                                                                                              | STEMCELL Technologies | 07820       | $289.00 | RT                      | [link](https://www.stemcell.com/products/optipreptm.html)                                                                                                                                                                 |
| POPC                            | Lipid      | 16:0-18:1 PC 25 mg/mL                                                                                                                  | Avanti Lipids         | A80557      | $435.00 | -20 °C                  | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc)                                                                                                                                      |
| Cholesterol                     | Lipid      | Cholesterol (plant)                                                                                                                    | Avanti Research       | A80100      | $261.00 | -20 °C                  | [link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant)                                                                                                                                    |
| Liss-Rhod PE                    | Lipid      | 18:0 Liss Rhod PE 1 mg/mL                                                                                                              | Avanti Lipids         | A81179      | $273.47 | -20 °C                  | [link](https://www.avantiresearch.com/en-gb/products/product/810179-180-liss-rhod-pe)                                                                                                                                     |
| Glucose                         | Chemical   | D-(+)-Glucose, 99%                                                                                                                     | Thermo Scientific     | A16828-36   | $41.65  | RT                      | [link](https://www.thermofisher.com/order/catalog/product/A16828.36)                                                                                                                                                      |
| Chloroform                      | Chemical   | Chloroform, suitable for HPLC, ≥99.8%, contains 0.5-1.0% ethanol as stabilizer                                                         | Sigma-Aldrich         | 366927      | $94.30  | RT (flammables cabinet) | [link](https://www.sigmaaldrich.com/US/en/product/sigald/366927)                                                                                                                                                          |
| Mineral oil                     | Chemical   | Mineral oil, mixed weight                                                                                                              | Thermo Scientific     | AC415080010 | $53.40  | RT                      | [link](https://www.thermofisher.com/order/catalog/product/AC415080010)                                                                                                                                                    |
| Glass syringe 250 µL            | Equipment  | Hamilton glass syringe                                                                                                                 | Hamilton              | 14-815-238  | $150.15 | RT                      | [link](https://www.fishersci.com/shop/products/800-microliter-syringes-rn-termination/14815238)                                                                                                                           |
| Glass serological pipette 10 mL | Equipment  | PYREX® 10 mL Disposable Glass Serological Pipets, TD, Individually Wrapped, Sterile, Plugged                                           | Corning               | 7077-10N    | $690.49 | RT                      | [link](https://ecatalog.corning.com/life-sciences/b2c/US/en/Glassware/Serological-Pipets%2C-Glass/PYREX%C2%AE-Disposable-Glass-Serological-Pipets%2C-Individually-Wrapped%2C-Sterile%2C-Plugged%2C-To-Deliver/p/7077-10N) |
| Glass vials                     | Consumable | Vials, screw top, graduated, solid cap, preassembled, volume 4 mL, clear glass vial, thread 13-425, O.D. x H 15 mm x 45 mm, PTFE liner | Supelco               | 27506-U     | $157.41 | RT                      | [link](https://www.sigmaaldrich.com/US/en/product/supelco/27506u)                                                                                                                                                         |
| 384-well glass bottom plate     | Consumable | 384 well glass bottom plate, 1.5 cover glass (20/case)                                                                                 | Cellvis               | P384-1.5H-N | $423.00 | RT                      | [link](https://www.cellvis.com/_384-well-glass-bottom-plate-with-high-performance-number-1.5-cover-glass_/product_detail.php?product_id=53)                                                                               |

:::

# Protocol

## Prepare Lipids in Mineral Oil

- [ ] Add 1 mL of mineral oil to the glass vial using a 1 mL pipette.

:::{warning} Warning
:class: simple
:icon: false
Work inside of a fume hood when handling chloroform.
:::

- [ ] Add the lipids in the above {ref}`comp-membrane-default` to the glass vial on top of the mineral oil using the appropriate glass syringe.
- [ ] Briefly vortex the lipid-oil mixture for 5 s to mix.
- [ ] Evaporate the chloroform from the lipid–oil mixture:
    - [ ] Place glass vial in a 55 °C dry bath in a fume hood.
    - [ ] Shield with aluminum foil to protect from light.
    - [ ] Evaporate uncovered for 4 h.
- [ ] Meanwhile, clean your glass syringe. 
	- [ ] Add 4 mL of chloroform to a glass bottle using a glass 10 mL serological pipette.
	- [ ] Rinse your syringe with that chloroform 5 times. 
	- [ ] Dry the syringes with the plunger removed inside the fume hood for 3 h to 4 h to allow remaining chloroform to evaporate.
- [ ] Cool the lipid-oil mixture to room temperature (between 10 min and 15 min). Your lipid-oil mixture is now ready for use. 

:::{hint} Note
:class: simple
:icon: false
The lipid–oil mixture can be used immediately after cooling to room temperature or stored at 4 °C for up to one week. Protect from light by storing in an opaque container or wrapping the vial with aluminum foil.
:::

- [ ] Return the plungers to the syringes and store them in their designated location.
- [ ] Dispose of chloroform waste following applicable chemical safety guidelines.

## Assemble Outer Solutions

- [ ] Prepare 1.5 mL microcentrifuge tubes labeled with the appropriate reaction.
- [ ] Prepare outer solution by mixing glucose stock solution and water to reach your target osmolarity:

:::{table} Preparation of outer solutions. These values are approximates and may vary based on the measured osmolarity of your inner solution (here: targeting 1140 mOsm).
:name: os-prep

| **Component**     | **Outer Solution (µL)** |
| ----------------- | ----------------------- |
| **Glucose (2 M)** | 570                     |
| **Water**         | 430                     |
| **Total**         | 1000                    |

:::

:::{hint} Note
:class: simple
:icon: false
The values shown are for encapsulating [Base Cytosol](../../modules/base-cytosol/spec.md). Measure the osmolarity of your inner solution and adjust the outer solution's glucose concentration so its osmolarity is 100 mOsm to 120 mOsm lower than the inner solution. Check the osmolarity of your inner solution by measuring with an Osmometer (e.g., Wescor EliTech Vapro 5600 Vapor Pressure Osmometer).
:::

## Encapsulate Inner Solution

- [ ] Allow lipid-oil mixture to come to room temperature as you perform these next steps.
- [ ] For each liposome encapsulation, set up a 1.5 mL tube rack with two 1.5 mL microcentrifuge tubes. Number the tubes according to the number of reactions assembled. Label the two tubes for each reaction:
    - [ ] **T**—transfer
    - [ ] **L**—liposomes
- [ ] Add 300 µL of the appropriate glucose outer solution to each of the tubes labeled **T**. Vortex thoroughly and spin down.
- [ ] Assemble at least 30 µL of your inner solution per reaction (see [Assemble Base Cytosol](../assemble-base-cytosol/main.md) for an example).
- [ ] Once at room temperature, add 150 µL of the lipid-oil mixture on top of each assembled inner solution reaction.
- [ ] Emulsify the lipid-oil and inner solution reaction by running the tube along a row of empty slots on the 1.5 mL tube rack. Drag your tube across empty slots at least 50 times until you form a stable emulsion with a homogeneous milky appearance.

:::{hint} Tip
:class: simple
:icon: false
While running the tubes over the tube rack, hold the cap firmly to prevent it from coming off during vigorous mixing. 
:::

- [ ] Immediately layer each emulsion on top of the outer solution by slowly pipetting down the side of the corresponding **T** tube.
- [ ] Centrifuge **T** tubes at 9000 g for 10 min at room temperature to pellet the liposomes.

:::{hint} Tip
:class: simple
:icon: false
Align the hinges of each T tube towards the outside of the centrifuge rotor, so that the final pellet location will be indicated by the tube hinge since the liposome pellet may not always be visible.
:::

- [ ] Extract the liposomes from each **T** tube:
    - [ ] Gently remove the oil layer and lipid debris from the top of each **T** tube with a 1000 µL pipette.
    - [ ] Gently resuspend the pellet by mixing by pipette 10-15 times.
    - [ ] Extract liposomes by pipetting 50 µL to 100 µL of pellet and outer solution from **T** and transfer liposome sample to the respective liposome tube **L**.

:::{hint} Tip
:class: simple
:icon: false
While removing the oil layer from your preps, do not submerge the pipette tip! Just _barely_ touch your pipette tip to the oil surface and aspirate slowly. Switch from a 1000 µL pipette to a 200 µL if necessary.

While extracting liposomes, it is more important to avoid transferring residual oil than to recover your entire liposome prep. Only extract less than 100 µL.

While handling liposomes, be gentle! Liposomes are fragile. Do not vortex and only mix by gentle pipetting.
:::

- [ ] Hold liposomes on ice until you are prepared to begin measurement.
- [ ] Transfer 5 µL liposomes and 20 µL of corresponding outer solution onto a 384-well glass bottom plate (5x dilution). If the density of liposomes appears too high under the microscope, dilute them with outer solution to facilitate data analysis.
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
