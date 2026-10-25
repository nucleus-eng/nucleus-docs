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

| Component    | Target (mmol/mol)     | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 699.3                 | 760.076                  | 25                          | 162.01             |
| Cholesterol  | 299.7                 | 386.654                  | 50                          | 17.66              |
| Liss-Rhod PE | 1                     | 1301.71                  | 1                           | 9.92               |
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
| Liss-Rhod PE                    | Lipid      | 18:1 Liss Rhod PE                                                                                                                      | Avanti Research       | A81150      | —       | -20 °C                  | —                                                                                                                                                                                                                         |
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

- [ ] Add 1 mL of mineral oil to a 4 mL glass vial using a 1 mL pipette.

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
- [ ] Prepare outer solution by mixing glucose stock solution and water. The table is a starting recipe; the target is a reading, set in the note below:

:::{table} Outer solution, starting recipe: 1140 mM glucose. A glucose concentration is not a reading of osmotic concentration: this solution is expected to read about 1275 mOsm/kg, scaled from one reading in [Nucleus Base Cell Testing](https://devnotes.nucleus.engineering/articles/base-cell-01) and not measured. Adjust it to your inner solution's reading, as the note below says.
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
Measure the osmotic concentration of your inner solution, and adjust the outer solution's glucose concentration until the outer solution reads 100 mOsm/kg to 150 mOsm/kg lower. That gap keeps the liposomes intact as they form: a larger gap ruptures them and their contents leak, and a smaller one lets them shrink ([Nucleus Base Cell Testing](https://devnotes.nucleus.engineering/articles/base-cell-01)). **Measure the outer solution as well, because its glucose concentration is not its reading.** In that DevNote the inner solution read 1060 mOsm/kg, and 850 mM glucose read 950 mOsm/kg. Scaled by glucose concentration from that pair, the recipe above would read about 1275 mOsm/kg, which would suit an inner solution of about 1375 mOsm/kg to 1425 mOsm/kg. Both figures are computed, not measured, and concentrated glucose does not scale exactly. Measure both on a vapor-pressure osmometer (e.g., Wescor EliTech Vapro 5600 Vapor Pressure Osmometer).
:::

## Encapsulate Inner Solution

- [ ] Allow lipid-oil mixture to come to room temperature as you perform these next steps.
- [ ] For each liposome encapsulation, set up a 1.5 mL tube rack with two 1.5 mL microcentrifuge tubes. Number the tubes according to the number of reactions assembled. Label the two tubes for each reaction:
    - [ ] **T**—transfer
    - [ ] **L**—liposomes
- [ ] Add 300 µL of the appropriate glucose outer solution to each of the tubes labeled **T**. Vortex thoroughly and spin down.
- [ ] Assemble at least 30 µL of your inner solution per reaction. For the Base Cell, [Build a Base Cell](../build-base-cell/main.md) gives the inner solution and every other step in order.
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

# Supported by

DevNotes that reference this page, not curated attribution.

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} ClpXP Control Module: Deployment in PURE Cells
:link: https://devnotes.nucleus.engineering/articles/019b613d-4a47-7d62-a262-77a667467a57
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a08cd1-9199-7ac0-bacf-3ac935c46856/public/control-module-bcdff4929cf964ead1956fd124d8d9d9.webp)
:::

:::{card} IV-HSL Emitter Cell
:link: https://devnotes.nucleus.engineering/articles/01945265-b728-7938-aab0-1ce134f4dffa
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a08cd1-0fa0-703d-902e-ade36c88739c/public/emitter-cell-schemat-41d2837d97b57df934b8bf6cbf9f0d3b.webp)
:::

:::{card} Integrating PPK Module in PURE Cells
:link: https://devnotes.nucleus.engineering/articles/019926c4-3341-76fc-8f36-eb96fd77c170
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a04676-f2cb-77ef-be8a-94b6945522ba/public/Developer_Cell-PPK_M-0437e9bcfcc9583145022782575f6b7b.webp)
:::

:::{card} London Exchange Meeting: Liposome Protocol Survey
:link: https://devnotes.nucleus.engineering/articles/019de275-d95d-7773-8622-59c333b056a9
:footer: London Exchange Meeting Participants · Workshops and Courses

![](https://pub.curvenote.com/01a08bf0-438a-7f89-8da9-7e1682f18642/public/thumbnail-5e1ebd3aefe4386efbd2de0f12b74635.webp)
:::

:::{card} Nucleus Base Cell Testing
:link: https://devnotes.nucleus.engineering/articles/019b13f9-1ec6-757c-b5ed-68cdd8e91fb0
:footer: Surendra Yadav · Nucleus Core

![](https://pub.curvenote.com/01a04676-8d9d-7f8f-96e1-2eefb52a607d/public/Image1-97e36bb3a38f167a4409ef588837c5fa.webp)
:::

:::{card} SecYEG-Based Membrane Translation Module in Synthetic Cells
:link: https://devnotes.nucleus.engineering/articles/019eae62-056c-7285-a994-aeb800ecdaa5
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a08cd2-12e5-77f7-ae0b-ffdbecb813d5/public/%20Schematic-SecYEG%20tr-8e0db9f6dcac44b44e156fbccbbaed6f.webp)
:::

:::{card} Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation
:link: https://devnotes.nucleus.engineering/articles/019f7d1d-98b9-7fa0-a691-ea286ab8a96f
:footer: Maia Grace Lambson, Clara Lillie, Grace Nicole Montgomery, Sunayana Nguyen, Javin P Oza · Workshops and Courses

![](https://pub.curvenote.com/01a14b4a-c04a-7d1b-ace2-50afec134578/public/grace-0306-fluoresce-17622626d5e8d521e944e518fe250407.png)
:::

:::{card} The Developer Cell Control Module: Protein Degradation by ClpXP
:link: https://devnotes.nucleus.engineering/articles/01981a5d-64c2-72f2-8055-5634d2824ede
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a08cd0-f496-7ee2-b08c-1c7e00240c3d/public/clpXP-85886080fd564ecd4e0aa3e9d696803a.webp)
:::

::::
