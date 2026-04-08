---
title: "Assemble Base Cytosol"
subtitle: "Process"
---

# Overview


This protocol shows you how to assemble Base Cytosol from the following components: small molecule mix (SMix), tRNA, protein mix (PMix), ribosomes. To test the functionality of the assembled Cytosol we use the [Reporter Module deGFP](/docs/modules/reporter-degfp/spec.md). 

**Protocols and other resources are available for download at the bottom of this page.**

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Notes
:class: dropdown
:icon: false

- You can make Base Cytosol components yourself by following the Base Cytsol Processes
- Base Cytosol components can be acquired as a premade reagent kit from b.next

::::::

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- If you are preparing Base Cytosol components yourself, use the following protocols:
  - [Make Small Molecule Mix](../make-small-molecule-mix/main.md)
  - [Make tRNAs](../make-trna/main.md)
  - Make Protein Mix
    - [Protein Mix](docs/processes/make-protein-mix/main.md)
    - [OnePot Protein Mix](docs/processes/make-onepot-protein-mix/main.md)
  - [Make Ribosomes](../make-ribosomes/main.md)
<!-- - [Reporter Module deGFP](/docs/modules/reporter-degfp/spec) -->

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

:::{table}
:label: tbl:critical-materials
:align: center

| Name | Type | Specification |
| --- | --- | --- |
| `pOpen-deGFP` | Reporter | [pOpen-GFP]() |
:::

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::{table} 
:label: tbl:comp-cytosol
:align: center

| **Component**             | **Volume per Reaction ($\mu$L)** |
| ------------------------- | -------------------------------- |
| Small Molecule Mix (SMix) | 3.0                              |
| tRNA                      | 1.0                              |
| Protein Mix (PMix)        | 1.2                              |
| Ribosomes                 | 1.8                              |
| RNase Inhibitor           | 0.5                              |
| `pOpen-deGFP`             | 0.5                              |
| User Additives            | X                                |
| Nuclease Free Water       | 2.0 - X                          |
| Total                     | 10                               |

:::

::::::

::::::{note} References
:class: dropdown
:icon: false

- Yadav, S. First Nucleus Cytosol Testing. *Nucleus Developer Notes.* (2025) doi:10.63765/fppr8928.

::::::

:::::::


# Protocol

## Cytosol Reaction Setup

:::{table} Reaction Setup.
:label: rxn-setup

| **Component**                | **Cytosol +deGFP DNA (µL)** | **Cytosol -deGFP DNA (µL)** |
| ---------------------------- | --------------------------- | --------------------------- |
| SMix                         | 10.5                        | 10.5                        |
| Water                        | 7                           | 8.75                        |
| RNAse Inhibitor              | 1.75                        | 1.75                        |
| PMix                         | 4.2                         | 4.2                         |
| tRNA                         | 3.5                         | 3.5                         |
| Ribosomes                    | 6.3                         | 6.3                         |
| `pOpen-deGFP` DNA template   | 1.75                        | 0                           |
| Total master mix volume (µL) | 35                          | 35                          |

:::

## Assemble Cytosol Reactions
- [ ] Thaw reagents above on ice.
- [ ] Chill two (2) PCR tubes on ice to assemble reaction master mixes.
    
:::{hint} Note
:class: simple
:icon: false
Prepare the reaction on ice or a cold block to prevent reactions from starting during your assembly. This reduces the affect of assembly time on your measured kinetics.
:::

- [ ] Resuspend each component according to the following instructions: 
    - [ ]  Vortex SMix aggressively until visibly clear. Alternate 10s vortex / 10s rest on ice to maintain cool temperature. SMix should be transparent with no visible precipitate when ready.
    - [ ]  Vortex or pipette mix tRNA.
    - [ ]  Pipette mix PMix.
    - [ ]  **Do NOT vortex** ribosomes! *Gently* pipette mix or flick the tube.
- [ ] For each reaction, assemble reaction master mix in a chilled PCR tube by adding each reagent in the order and volume listed in the table above. 
- [ ] Mix the master mix thoroughly by pipette (6-10x) until visibly homogenous.
- [ ] Hold assembled reactions on ice or at 4C until ready for measurement.
- [ ] On a 384-well optical plate, array 10 µL of each reaction master mix into three (3) wells and note their locations.

:::{hint} Tip
:class: simple
:icon: false
To avoid introducing bubbles, use reverse pipetting to array your samples. With your p20 pipette set to "10" µL, push your plunger down past the second (blowout) stop, aspirate your sample, and dispense up to the first stop. Repeat for the remaining two (2) replicates.
:::

- [ ] In a plate reader set to 37°C, measure deGFP expression using the standard green fluorescence channel (ex: 485 nm, em: 515 nm).
  
## Return reagents to their appropriate storage locations
- [ ] Mark the lid of each Cytosol component that you used. The number of dots indicates how many freeze–thaw cycles each component has gone through.

# Downloads

:::::{card}
:header: **Resources**
::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**
{button}`download <module-protocol-cytosol-degfp.pdf>`
:::


:::{card}
:header: **Bill of Materials**
{button}`download <module-bom-reporter-degfp.pdf>`
:::

::::
:::::