---
title: "Protocol"
subtitle: "Reporter: deGFP (Cytosol)"
exports:
  - format: typst
    template: https://github.com/antonrmolina/nucleus-typst-test/archive/refs/heads/main.zip
    output: module-protocol-cytosol-degfp.pdf
---

# Overview

This protocol show you how to validate the functionality of the Reporter Module `pOpen-deGFP`.

## Cytosol Reaction Setup

:::{table} Reaction Setup.
:name: rxn-setup

| **Component** | **Cytosol + deGFP DNA [µL]** | **Cytosol - deGFP DNA [µL]** |
| --- | --- | --- |
| SMix | 10.5 | 10.5 |
| tRNA | 3.5 | 3.5 |
| PMix | 4.2 | 4.2 |
| Ribosomes | 6.3 | 6.3 |
| RNAse Inhibitor | 1.75 | 1.75 |
| `pOpen-deGFP` DNA template | 0.85 | 0 |
| Water | 7.9 | 8.75 |
| Total master mix volume [µL] | 35 | 35 |

:::


# Protocol

<!-- ### Prepare Stock Solutions -->

### Assemble Cytosol Reactions
- [ ]  Remove all components listed in the Reaction Setup table above from appropriate cold storage.
- [ ]  Thaw reagents on ice.
- [ ]  Prepare a PCR tube, on ice, to assemble reactions into.
    
:::{hint} Note
:class: simple
:icon: false
Prepare the reaction on ice or a cold block to prevent protein expression from starting during assembly. This ensures the plate reader captures the complete fluorescence kinetics for deGFP expression.
:::

- [ ] For a given reaction, assemble by adding the volume of reagents from the table in the order listed. Pay special attention to the handling of the Cytosol components:
    - [ ]  Vortex SMix: Ensure thorough mixing; 10s vortex / 10s rest on ice; should be transparent with no visible precipitate; and add to the reaction tubes.
    - [ ]  Vortex or pipette mix tRNA, and add to the reaction tubes.
    - [ ]  Vortex or pipette mix PMix, and add to the reaction tubes.
    - [ ]  **Do NOT vortex** ribosomes: *gently* pipette mix or flick the tube, and add to the reaction tubes.
    - [ ]  Add remaining reactions in the order they appear.
- [ ]  Mix the master mix thoroughly by pipetting up and down 10–15 times until it appears homogeneous and clear.
- [ ]  Close lids on the PCR tubes and briefly spin down to eliminate bubbles.
- [ ]  Hold assembled reactions on ice until ready for measurement.
- [ ]  Array 10 µL into each of three assigned wells of a black 384-well optical plate and take note of your plate map.

<br>
<br>

:::{hint} Tip
:class: simple
:icon: false
Set the P20 pipette to 10.1 µL to draw the master mix, then dispense into the plate well by pushing the plunger to the first stop only—this prevents bubble generation in the reaction.
:::

- [ ]  Measure deGFP fluorescence in the plate reader while incubating at 37°C.
  
### Return reagents to their appropriate storage locations
- [ ]  Add a black dot to the lid of each of Cytosol component. The number of dots indicates freeze–thaw cycles.