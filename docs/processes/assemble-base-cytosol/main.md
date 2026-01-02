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

- Base Cytosol components can be made from scratch by following the relevant documentation in the Distribution
- Base Cytosol components can be acquired as a premade reagent kit from b.next

::::::

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- If you are making Base Cytosol from scratch:
  - [Make Small Molecule Mix](../make-small-molecule-mix/main.md)
  - [Make tRNAs](../make-trna/main.md)
  - Make Protein Mix
    - [1Pot Protein Mix](../make-1pot/main.md)
    - [36Pot Protein Mix](../make-36pot/main.md)
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
| `pT7-plamGFP` | Reporter | [pT7-plamGFP](https://github.com/bnext-bio/nucleus/blob/main/dna-distribution/v0.1.0-001/plamGFP-PURE.gb) |
:::

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::{table} 
:label: tbl:comp-cytosol
:align: center

| **Component** | **Volume per Reaction ($\mu$L)** |
| --- | --- |
| Small Molecule Mix | 3.0 |
| tRNA | 1.0 |
| Protein Mix | 1.2 |
| Ribosomes | 1.8 |
| RNase Inhibitor | 0.5 |
| `pT7-plamGFP` | 0.5 |
| User Additives | X |
| Nuclease Free Water | 2.0 - X |
| Total | 10 |

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

## Assemble Cytosol Reactions
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

:::{hint} Tip
:class: simple
:icon: false
Set the P20 pipette to 10.1 µL to draw the master mix, then dispense into the plate well by pushing the plunger to the first stop only—this prevents bubble generation in the reaction.
:::

- [ ]  Measure deGFP fluorescence in the plate reader while incubating at 37°C.
  
## Return reagents to their appropriate storage locations
- [ ]  Add a black dot to the lid of each of Cytosol component. The number of dots indicates freeze–thaw cycles.

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