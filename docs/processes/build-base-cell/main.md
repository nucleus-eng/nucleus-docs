---
title: "Build a Base Cell"
subtitle: "Process"
status: unvalidated-published
---

# Overview

This protocol takes you from starting materials to finished [Base Cells](../../modules/base-cell/spec.md) in one pass. It joins three parts that are documented on separate pages: the lipid–oil mixture for the [Base Membrane: POPC/Chol](../../modules/membrane-popc-chol/spec.md), the outer solution, and an inner solution made of [Base Cytosol](../../modules/base-cytosol/spec.md). [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) then closes the membrane around the inner solution.

:::{attention} Not yet validated
Every step comes from a validated protocol, but the outer-solution starting recipe (1140 mM glucose, with the RNase inhibitor in the inner solution) has not been measured against this inner solution. Part 3 has you measure both solutions and adjust before you encapsulate.
:::

**Plan the day around the lipids.** The lipid–oil mixture takes about 4.5 h and keeps for one week at 4 °C, so make it first, or up to a week before. Assemble the inner solution last, on ice, immediately before you encapsulate, because it starts to express as soon as it is warm.

| Part | Time | When |
| --- | --- | --- |
| 1. Prepare lipids in mineral oil | about 4.5 h, mostly unattended | first, or up to one week before |
| 2. Assemble the outer solution | 15 min | any time before part 3 |
| 3. Assemble the inner solution | 20 min, with an osmometer reading | immediately before part 4 |
| 4. Encapsulate | about 30 min | last |

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information.

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

**Chloroform** - Irritant, possible carcinogen. Work in fume hood and use gloves.

::::::

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

The inner solution needs the Base Cytosol components. You can get them as a premade reagent kit from b.next, or make them by these protocols:

- [Make Small Molecule Mix](../make-small-molecule-mix/main.md)
- [Make tRNAs](../make-trna/main.md)
- [Make Protein Mix](../make-36pot/main.md), or [Make OnePot Protein Mix](../make-1pot/main.md)
- [Make Ribosomes](../make-ribosomes/main.md)

::::::

::::::{note} Materials and Equipment
:class: dropdown
:icon: false

The lipids, mineral oil, chloroform, glucose, Optiprep, glassware and imaging plate are listed in the Materials and Equipment table of [Encapsulation: Phase Transfer](../assemble-base-cell/main.md). You also need the Base Cytosol components above, RNase inhibitor (optional), and a vapor-pressure osmometer (e.g., Wescor EliTech Vapro 5600 Vapor Pressure Osmometer).

::::::

:::::::

# Protocol

## 1. Prepare Lipids in Mineral Oil

:::{table} Lipids for 1 mL of mineral oil.
:label: base-cell-build-membrane

| Component    | Target (mmol/mol)     | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 699.3                 | 760.076                  | 25                          | 162.01             |
| Cholesterol  | 299.7                 | 386.654                  | 50                          | 17.66              |
| Liss-Rhod PE | 1                     | 1301.71                  | 1                           | 9.92               |
:::

:::{hint} Which Liss-Rhod PE
:class: simple
:icon: false
Use 18:1 Liss Rhod PE (Avanti A81150), the product in [Nucleus Base Cell Testing](https://devnotes.nucleus.engineering/articles/base-cell-01). Its molecular weight is the 1301.71 g/mol in the table. The 18:0 product, A81179, is another option with its own molecular weight: if you use it, recompute the volume from that weight. The label is 1 mmol/mol (0.1 mol %), and POPC and cholesterol share the rest in a 7:3 ratio, so the table sums to 1000 mmol/mol. It makes 7.62 µmol of lipid in 1 mL of oil.
:::

- [ ] Add 1 mL of mineral oil to the glass vial using a 1 mL pipette.

:::{warning} Warning
:class: simple
:icon: false
Work inside of a fume hood when handling chloroform.
:::

- [ ] Add the lipids in {ref}`base-cell-build-membrane` to the glass vial on top of the mineral oil using the appropriate glass syringe.
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

## 2. Assemble the Outer Solution

- [ ] Mix 2 M glucose and water as below. This makes 1 mL of 1140 mM glucose, which is enough for three encapsulations.

:::{table} Outer solution, starting recipe: 1140 mM glucose.
:label: base-cell-build-outer

| Component     | Volume (µL) |
| ------------- | ----------- |
| Glucose (2 M) | 570         |
| Water         | 430         |
| Total         | 1000        |
:::

- [ ] Read the outer solution's osmotic concentration on the osmometer, and record it.

:::{hint} Why the outer solution is measured, and not only mixed
:class: simple
:icon: false
The outer solution must read 100 mOsm/kg to 150 mOsm/kg lower than the inner solution. That gap keeps the liposomes intact as they form: a larger gap ruptures them and their contents leak, and a smaller one lets them shrink ([Nucleus Base Cell Testing](https://devnotes.nucleus.engineering/articles/base-cell-01)). A glucose concentration is not an osmometer reading. In that DevNote the inner solution read 1060 mOsm/kg and 850 mM glucose read 950 mOsm/kg, a gap of 110 mOsm/kg. That inner solution had no RNase inhibitor. The one in part 3 does, and the inhibitor is stored in glycerol, which raises its osmotic concentration, so this page starts from a stronger outer solution: 1140 mM glucose. Scaled from the DevNote's pair, that would read about 1275 mOsm/kg, a computed figure that no one has measured. It is a starting point, not an answer, and you check your own gap in part 3.
:::

## 3. Assemble the Inner Solution

The inner solution is Base Cytosol with Optiprep. Each reaction is 40 µL: 10 µL goes to the osmometer, and the remaining 30 µL is what one encapsulation takes.

:::{table} Inner solution, one reaction.
:label: base-cell-build-inner

| Component                                 | Stock concentration | Final concentration | Volume (µL) |
| ----------------------------------------- | ------------------- | ------------------- | ----------- |
| SMix                                      | 3.33x               | 1x                  | 12          |
| tRNA                                      | 35 mg/mL            | 3.5 mg/mL           | 4           |
| PMix                                      | 15 mg/mL            | 1.80 mg/mL          | 4.8         |
| Ribosomes                                 | 10 µM               | 1.8 µM              | 7.2         |
| RNase Inhibitor                           | 40 000 U/mL         | 2000 U/mL           | 2           |
| Optiprep                                  | 1.32 mg/µL          | 0.044 mg/µL         | 1.33        |
| Optional additions, such as template DNA  |                     |                     | X           |
| Water                                     |                     |                     | 8.67 − X    |
| Total                                     |                     |                     | 40          |
:::

:::{hint} What goes in the optional additions
:class: simple
:icon: false
Base Cytosol leaves 2.5 µL of every 10 µL free for additions, which is 10 µL in this reaction. The Base Cell uses 1.33 µL of it for Optiprep, a density agent that lets the inner-solution droplets pellet through the oil–water interface in part 4. The other 8.67 µL takes whatever you add, such as template DNA, and water fills what you do not use. To see the cells express, add [`pOpen-deGFP`](../../modules/reporter-degfp/spec.md) to 3 nM: 0.95 µL of a 124 nM stock, with 7.72 µL of water. Keep the RNase inhibitor in: the outer-solution recipe in part 2 assumes it. Each choice here changes the inner solution's osmotic concentration, so read it with everything in, as part 3 says.
:::

- [ ] Thaw SMix, tRNA, PMix, ribosomes and RNase inhibitor on ice.
- [ ] Chill one 1.5 mL microcentrifuge tube per reaction on ice.

:::{hint} Note
:class: simple
:icon: false
Prepare the reaction on ice or a cold block to prevent expression from starting before encapsulation.
:::

- [ ] Resuspend each component:
    - [ ] Vortex SMix aggressively until visibly clear. Alternate 10 s vortex / 10 s rest on ice to maintain cool temperature. SMix should be transparent with no visible precipitate when ready.
    - [ ] Vortex or pipette mix tRNA.
    - [ ] Pipette mix PMix.
    - [ ] **Do NOT vortex** ribosomes! *Gently* pipette mix or flick the tube.
- [ ] Add each component to its chilled tube, in the order and volume of {ref}`base-cell-build-inner`.
- [ ] Mix thoroughly by pipette (6-10x) until visibly homogeneous.
- [ ] Take 10 µL of the inner solution and read its osmotic concentration on the osmometer.
- [ ] Compare it with the outer solution's reading from part 2. The outer solution must read 100 mOsm/kg to 150 mOsm/kg lower. If it does not, adjust its glucose concentration and read it again.
- [ ] Hold the inner solution on ice until part 4.

## 4. Encapsulate

- [ ] Allow the lipid-oil mixture to come to room temperature as you perform these next steps.
- [ ] For each liposome encapsulation, set up a 1.5 mL tube rack with two 1.5 mL microcentrifuge tubes. Number the tubes according to the number of reactions assembled. Label the two tubes for each reaction:
    - [ ] **T**—transfer
    - [ ] **L**—liposomes
- [ ] Add 300 µL of the outer solution to each of the tubes labeled **T**. Vortex thoroughly and spin down.
- [ ] Once at room temperature, add 150 µL of the lipid-oil mixture on top of each 30 µL inner solution.
- [ ] Emulsify the lipid-oil and inner solution by running the tube along a row of empty slots on the 1.5 mL tube rack. Drag your tube across empty slots at least 50 times until you form a stable emulsion with a homogeneous milky appearance.

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
- [ ] Transfer 5 µL liposomes and 20 µL of the outer solution onto a 384-well glass bottom plate (5x dilution). If the density of liposomes appears too high under the microscope, dilute them with outer solution to facilitate data analysis.
- [ ] Observe liposomes by fluorescence microscopy. Base Cells have red fluorescent membranes. With `pOpen-deGFP` in the inner solution, green fluorescence rises over time; see [Base Cell](../../modules/base-cell/spec.md) for the expected kinetics.

## 5. Return Reagents

- [ ] Return the Base Cytosol components to their storage locations.
- [ ] Mark the lid of each Base Cytosol component that you used. The number of dots indicates how many freeze–thaw cycles each component has gone through.

# Downloads

::::{grid} 1 1 1 1

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/build-base-cell-protocol.pdf>`
:::

::::
