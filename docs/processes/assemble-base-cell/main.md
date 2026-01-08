---
title: "Assemble Base Cell"
subtitle: "Process"
---

# Overview

Base Cells are liposome-based synthetic cells that can perform transcription and translation.

In this protocol, you will make the necessary precursors for liposome encapsulation, and then assemble and encapsulate Cytosol that expresses Green Fluorescent Protein (GFP). The Base Cell is deployed in a gluocose outer solution.

Successfully built Base Cells will start dark and then increase in green fluorescence over time as GFP is produced.


:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Notes
:class: dropdown
:icon: false

- None

::::::

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- None

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

- None

::::::

::::::{attention} Critical Materials
:class: dropdown
:icon: false

- None

::::::

::::::{attention} Genetically Encoded Components
:class: dropdown
:icon: false

- None

::::::

::::::{note} Composition
:class: dropdown
:icon: false


:::::{tab-set}

::::{tab-item} Cytosol

:::{table}
:label: comp-cytosol
| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction [µL] |
| --- | --- | --- | --- | --- | --- |
| SMix | 3.33 | × | 1 | × | 12 |
| PMix | 15 | mg/mL | 1.80 | mg/mL | 4.8 |
| Ribosomes | 10 | µM | 1.8 | µM | 7.2 |
| `pOpen-deGFP` DNA | 124 | nM | 3 | nM | 0.95 |
| tRNA | 35 | mg/ml | 3.5 | mg/ml | 4 |
| Magnesium acetate | 200 | mM | 8 | mM | 1.6 |
| Optiprep | 1.32 | mg/uL | 0.043 | mg/uL | 1.33 |
| RNase Inhibitor | 40000 | U/mL | 2000 | U/mL | 2 |
| Water |  |  |  |  | 6.12 |
| Total volume [µL] |  |  |  |  | 40 |
:::

::::

::::{tab-item} Membrane
:::{table}
:label: comp-membrane
| Component | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (uL) |
| --- | --- | --- | --- | --- |
| POPC | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.654 | 50 | 17.65 |
| Liss-Rhod PE | 0.05 | 1301.71 | 1 | 4.96 |

:::
::::

::::{tab-item} Outer Solution

:::{table}
| Component | Concentration |
| --- | --- |
| Glucose | 850 mM |
:::

::::
:::::

::::::

::::::{note} References
:class: dropdown
:icon: false

- None

::::::

:::::::

# Protocol

## Prepare Stock Solutions

**Prepare lipids in mineral oil**
- [ ]  Add 1 mL of mineral oil to the 1.8 mL glass vial using a 1 mL pipette.

:::{warning} Warning
:class: simple
:icon: false
Work inside of a fume hood when handling chloroform and lipids.
:::

- [ ]  Add the lipids in the above {ref}`comp-membrane` to the glass vial on top of the mineral oil using the appropriate glass syringe.
- [ ]  Briefly vortex the lipid-oil mixture for 5 seconds to mix.
- [ ]  Evaporate the chloroform from the lipid–oil mixture:
    - [ ]  Place glass vial in a 55°C dry bath in a fume hood.
    - [ ]  Shield with aluminum foil to protect from light.
    - [ ]  Evaporate uncovered for 4 hours.
- [ ]  In a glass bottle, add 4 mL of chloroform using a glass 10 mL serological pipette.
- [ ]  Clean syringes by rinsing with chloroform 5 times into an empty glass bottle. Store the syringes with the plunger removed inside the fume hood for 3–4 hours to allow remaining chloroform to evaporate.
- [ ]  After 4 hours of incubation at 55°C in a dry bath in a fume hood, allow the lipid-oil mixture to cool to room temperature for 10-15 minutes.

:::{hint} Note
:class: simple
:icon: false
The lipid–oil mixture can be used immediately after cooling to room temperature or stored at 4°C for up to one week. Protect from light by storing in an opaque container or wrapping the vial with aluminum foil.
:::

- [ ]  Return the plungers to the syringes and store them in their designated location.
- [ ]  Dispose of chloroform waste following applicable chemical safety guidelines.

## Assemble Outer Solutions

- [ ]  Prepare 1.5 mL microcentrifuge tubes labelled with the appropriate reaction.
- [ ]  Mix glucose stock solution and water according to the following table:

:::{table} Preparation of outer solutions. These values are approximates and may vary based on the measured osmolarity of your inner solution.
:name: os-prep

| **Component** | **Cells + deGFP DNA [µL]** | **Cells - deGFP DNA [µL]** |
| --- | --- | --- |
| **Glucose (2 M)** | 570 | 570 |
| **Water** | 430 | 430 |
| **Total** | 1000 | 1000 |

:::

:::{hint} Note
:class: simple
:icon: false
These outer solution concentrations may vary and should be based on the measured osmolarity of your inner solution.
:::

## Assemble Cytosol Reactions

- [ ]  Remove all components listed in the Composition {ref}`comp-cytosol` above from appropriate cold storage.
- [ ]  Thaw reagents on ice.
- [ ]  Prepare 1.5 mL microcentrifuge tubes, on ice, to assemble reactions into.

:::{hint} Tip
:class: simple
:icon: false
Prepare the reaction on ice or a cold block to prevent protein expression from starting during assembly. This ensures the plate reader captures the complete fluorescence kinetics for deGFP expression.
:::

- [ ]  For a given reaction, assemble by adding the volume of reagents from the Composition {ref}`comp-cytosol` in the order listed. Pay special attention to the handling of the Cytosol components:
    - [ ]  Vortex SMix: Ensure thorough mixing; 10s vortex / 10s rest on ice; should be transparent with no visible precipitate; and add to the reaction tubes.
    - [ ]  Vortex or pipette mix tRNA, and add to the reaction tubes.
    - [ ]  Vortex or pipette mix PMix, and add to the reaction tubes.
    - [ ]  **Do NOT vortex** ribosomes: *gently* pipette mix or flick the tube, and add to the reaction tubes.
    - [ ]  Add remaining reactions in the order they appear
- [ ]  Mix the master mix thoroughly by pipetting up and down 10–15 times until it appears homogeneous and clear.
- [ ]  Close lids on the microcentrifuge tubes and briefly spin down to eliminate bubbles.
- [ ]  Pipette out 10 µL of the reaction for osmolarity check using a Vapor Pressure Osmometer before starting encapsulation.

:::{danger} Critical
:class: simple
:icon: false
Adjust the outer solution concentration so its osmolarity is 100–120 units lower than the inner solution when measured on a Wescor EliTech Vapro 5600 Vapor Pressure Osmometer. 
:::

- [ ]  Hold assembled reactions on ice until ready for encapsulation.

## Encapsulate Cytosols into Liposomes

- [ ]  Set up a 1.5 mL tube rack with two 1.5 mL microcentrifuge tubes for each liposome encapsulation. Number the tubes according to the number of reactions assembled. Label the two tubes for each reaction:
    - [ ]  **T**—transfer
    - [ ]  **L**—liposomes
- [ ]  Add 300 uL of the appropriate glucose outer solution to each of the tubes labelled **T**.
- [ ]  Add 150 uL of the lipid-oil mixture (at room temperature) on top of each assembled Cytosol reaction.
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
    - [ ]  Remove the oil layer and lipid debris from the top of each **T** tube by gently pipetting with a 1000 uL pipette set to 800 uL.
    - [ ]  Gently pipette mix the pellet 10-15 times with the outer solution.
    - [ ]  Extract liposomes by pipetting 50-100 uL of pellet and outer solution from **T** and transfer liposome sample to the respective liposome tube **L**.

:::{danger} Critical
:class: simple
:icon: false
Do not transfer the entire solution. It is important to avoid transferring the top of the solution which may contain a residual oil layer. 
:::

- [ ]  Hold liposomes on ice until you are prepared to begin measurement.
- [ ]  Pipette the liposomes into a well on a 384-well glass bottom plate. If the density appears too high under the microscope, dilute the liposomes with the outer solution for better data analysis.
- [ ]  Begin measurement.

**Return reagents to their appropriate storage locations.**
- [ ]  Add a black dot to the lid of each of Cytosol component. The number of dots indicates freeze–thaw cycles.

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**
:align: center

{button}`download <module-protocol-cells-degfp.pdf>`
:::

:::{card}
:header: **Bill of Materials**
{button}`download <module-bom-reporter-cells-degfp.pdf>`
:::

::::
