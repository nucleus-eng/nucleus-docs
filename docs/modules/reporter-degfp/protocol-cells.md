---
title: "Protocol"
subtitle: "Reporter: deGFP (Cells)"
exports:
  - format: typst
    template: https://github.com/antonrmolina/nucleus-typst-test/archive/refs/heads/main.zip
    output: module-protocol-cells-degfp.pdf
---

# Overview

This protocol show you how to validate the functionality of the Reporter Module `pOpen-deGFP` in cells using the POPC:cholesterol Membrane Module.

## Cytosol Reaction Setup

:::{table} Reaction setup.
:name: rxn-setup

| **Component** | **Cells + deGFP DNA [µL]** | **Cells - deGFP DNA [µL]** |
| --- | --- | --- |
| SMix | 12 | 12 |
| tRNA | 4 | 4 |
| PMix | 4.8 | 4.8 |
| Ribosomes | 7.2 | 7.2 |
| RNase Inhibitor | 2 | 2 |
| `pOpen-deGFP` DNA | 0.95 | 0 |
| Optiprep | 1.33 | 1.33 |
| Water | 7.72 | 8.67 |
| Total master mix volume [µL] | 40 | 40 |

:::

## Protocol

### Prepare Stock Solutions

**Prepare lipids in mineral oil**
- [ ]  Add 1 mL of mineral oil to the 1.8 mL glass vial using a 1 mL pipette.

:::{warning} Warning
:class: simple
:icon: false
Work inside of a fume hood when handling chloroform and lipids.
:::

- [ ]  Add the lipids to the glass vial on top of the mineral oil using the appropriate glass syringe.
- [ ]  Briefly vortex the lipid-oil mixture for 5 seconds to mix.
- [ ]  Evaporate the chloroform from the lipid–oil mixture:
    - [ ]  Place glass vial in a 55°C dry bath in a fume hood.
    - [ ]  Shield with aluminum foil to protect from light.
    - [ ]  Evaporate uncovered for 4 hours.
- [ ]  In a glass bottle, add 4 mL of chloroform using a glass 10 mL serological pipette.
- [ ]  Clean syringes by rinsing with chloroform 5 times into an empty glass bottle. Store the syringes with the plunger removed inside the fume hood for 3–4 hours to allow remaining chloroform to evaporate.
- [ ]  After 4 hours of incubation at 55°C in a dry bath in a fume hood, allow the lipid-oil mixture to cool to room temperature for 10-15 minutes.

<br>
<br>
<br>

:::{hint} Note
:class: simple
:icon: false
The lipid–oil mixture can be used immediately after cooling to room temperature or stored at 4°C for up to one week. Protect from light by storing in an opaque container or wrapping the vial with aluminum foil.
:::

- [ ]  Return the plungers to the syringes and store them in their designated location.
- [ ]  Dispose of chloroform waste following applicable chemical safety guidelines.

### Assemble Outer Solutions

- [ ]  Prepare 1.5 mL microcentrifuge tubes labeled with the appropriate reaction.
- [ ]  Mix glucose stock solution and water according to the following table:

:::{table} Preparation of outer solutions. These values are approximates and may vary based on the measured osmolarity of your inner solution.
:name: os-prep

| **Component** | **Cells + deGFP DNA [µL]** | **Cells - deGFP DNA [µL]** |
| --- | --- | --- |
| **Glucose (2 M)** | 570 | 570 |
| **Water** | 430 | 430 |
| Total | 1000 | 1000 |

:::

:::{hint} Note
:class: simple
:icon: false
These outer solution concentrations may vary and should be based on the measured osmolarity of your inner solution.
:::

### Assemble Cytosol Reactions

- [ ]  Remove all components listed in the Reaction Setup table above from appropriate cold storage.
- [ ]  Thaw reagents on ice.
- [ ]  Prepare 1.5 mL microcentrifuge tubes, on ice, to assemble reactions into.

:::{hint} Tip
:class: simple
:icon: false
Prepare the reaction on ice or a cold block to prevent protein expression from starting during assembly. This ensures the plate reader captures the complete fluorescence kinetics for deGFP expression.
:::

- [ ]  For a given reaction, assemble by adding the volume of reagents from the table in the order listed. Pay special attention to the handling of the Cytosol components:
    - [ ]  Vortex SMix: Ensure thorough mixing; 10s vortex / 10s rest on ice; should be transparent with no visible precipitate; and add to the reaction tubes.
    - [ ]  Vortex or pipette mix tRNA, and add to the reaction tubes.
    - [ ]  Vortex or pipette mix PMix, and add to the reaction tubes.
    - [ ]  **Do NOT vortex** ribosomes: *gently* pipette mix or flick the tube, and add to the reaction tubes.
    - [ ]  Add remaining reactions in the order they appear
- [ ]  Mix the master mix thoroughly by pipetting up and down 10–15 times until it appears homogeneous and clear.
- [ ]  Close lids on the microcentrifuge tubes and briefly spin down to eliminate bubbles.
- [ ]  Pipette out 10 µL of the reaction for osmolarity check using a Vapor Pressure Osmometer before starting encapsulation.

<br>

:::{danger} Critical
:class: simple
:icon: false
Adjust the outer solution concentration so its osmolarity is 100–120 units lower than the inner solution when measured on a Wescor EliTech Vapro 5600 Vapor Pressure Osmometer. 
:::

- [ ]  Hold assembled reactions on ice until ready for encapsulation.

### Encapsulate Cytosols into Liposomes

- [ ]  Set up a 1.5 mL tube rack with two 1.5 mL microcentrifuge tubes for each liposome encapsulation. Number the tubes according to the number of reactions assembled. Label the two tubes for each reaction:
    - [ ]  **T**—transfer
    - [ ]  **L**—liposomes
- [ ]  Add 300 µL of the appropriate glucose outer solution to each of the tubes labeled **T**.
- [ ]  Add 150 µL of the lipid-oil mixture (at room temperature) on top of each assembled Cytosol reaction.
- [ ]  Emulsify the lipid-oil and Cytosol reaction by running the tube along a row of empty slots on the 1.5 mL tube rack. Run it down 20–30 times until the solution forms a stable emulsion with an even milky color.

:::{hint} Tip
:class: simple
:icon: false
While running the tubes on the tube rack, hold the cap firmly to prevent it from coming off during vigorous mixing. 
:::

- [ ]  Immediately layer each emulsion over the outer solution. Slowly pipette the entire emulsion down the side of the corresponding **T** tube.
- [ ]  Centrifuge **T** tubes at 9000 g for 10 min at room temperature to pellet the liposomes.

:::{hint} Tip
:class: simple
:icon: false
Align the hinges of each T tube towards the outside of the centrifuge rotor, so that the final pellet location will be indicated by the tube hinge since the liposome pellet may not always be visible.
:::

- [ ]  Extract the liposomes from each **T** tube:
    - [ ]  Remove the oil layer and lipid debris from the top of each **T** tube by gently pipetting with a 1000 µL pipette set to 800 µL.
    - [ ]  Gently pipette mix the pellet 10-15 times with the outer solution.
    - [ ]  Extract liposomes by pipetting 50-100 µL of pellet and outer solution from **T** and transfer liposome sample to the respective liposome tube **L**.

:::{danger} Critical
:class: simple
:icon: false
Critical: Do not transfer the entire solution. It is important to avoid transferring the top of the solution which may contain a residual oil layer. 
:::

- [ ]  Hold liposomes on ice until you are prepared to begin measurement.
- [ ]  Pipette the liposomes into a well on a 384-well glass bottom plate. If the density appears too high under the microscope, dilute the liposomes with the outer solution for better data analysis.
- [ ]  Begin measurement.

**Return reagents to their appropriate storage locations.**
- [ ]  Add a black dot to the lid of each of Cytosol component. The number of dots indicates freeze–thaw cycles.