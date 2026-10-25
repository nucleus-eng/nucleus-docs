---
title: "Assemble Base Cytosol"
subtitle: "Process"
---

# Overview


This protocol shows you how to assemble Base Cytosol from the following components: small molecule mix (SMix), tRNA, protein mix (PMix), ribosomes. To test the functionality of the assembled Cytosol we use the [Reporter Module deGFP](/docs/modules/reporter-degfp/spec.md). Initial validation of the assembled Cytosol is documented in [Yadav (2025)](https://doi.org/10.63765/fppr8928). 

**Protocols and other resources are available for download at the bottom of this page.**

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Notes
:class: dropdown
:icon: false

- You can make Base Cytosol components yourself by following the Base Cytosol Processes
- Base Cytosol components can be acquired as a premade reagent kit from b.next

::::::

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- If you are preparing Base Cytosol components yourself, use the following protocols:
  - [Make Small Molecule Mix](../make-small-molecule-mix/main.md)
  - [Make tRNAs](../make-trna/main.md)
  - Make Protein Mix
    - [Protein Mix](../make-36pot/main.md)
    - [OnePot Protein Mix](../make-1pot/main.md)
  - [Make Ribosomes](../make-ribosomes/main.md)
<!-- - [Reporter Module deGFP](/docs/modules/reporter-degfp/spec) -->

::::::

::::::{attention} Genetically Encoded Components
:class: dropdown
:icon: false

:::{table}
:label: tbl:critical-materials
:align: center

| Name          | Type     | Specification                                       |
| ------------- | -------- | --------------------------------------------------- |
| `pOpen-deGFP` | Reporter | [pOpen-deGFP](/docs/modules/reporter-degfp/spec.md) |
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
| Optional additions, such as template DNA (e.g. `pOpen-deGFP`) or Optiprep for encapsulation by phase transfer | X |
| Nuclease Free Water       | 2.5 - X                          |
| Total                     | 10                               |

:::

::::::

:::::::


# Materials and Equipment

This is an assembly process: it combines components produced by other Nucleus processes (Small Molecule Mix, Protein Mix, ribosomes, tRNAs, and the genetically encoded components listed above) rather than introducing new reagents. Its materials are itemized in those component processes' Bills of Materials — see the consolidated [Materials Reference](../../../guides/materials-reference.md).

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
    - [ ]  Vortex SMix aggressively until visibly clear. Alternate 10 s vortex / 10 s rest on ice to maintain cool temperature. SMix should be transparent with no visible precipitate when ready.
    - [ ]  Vortex or pipette mix tRNA.
    - [ ]  Pipette mix PMix.
    - [ ]  **Do NOT vortex** ribosomes! *Gently* pipette mix or flick the tube.
- [ ] For each reaction, assemble reaction master mix in a chilled PCR tube by adding each reagent in the order and volume listed in the table above. 
- [ ] Mix the master mix thoroughly by pipette (6-10x) until visibly homogeneous.
- [ ] Hold assembled reactions on ice or at 4 °C until ready for measurement.
- [ ] On a 384-well optical plate, array 10 µL of each reaction master mix into three (3) wells and note their locations.

:::{hint} Tip
:class: simple
:icon: false
To avoid introducing bubbles, use reverse pipetting to array your samples. With your p20 pipette set to "10" µL, push your plunger down past the second (blowout) stop, aspirate your sample, and dispense up to the first stop. Repeat for the remaining two (2) replicates.
:::

- [ ] In a plate reader set to 37 °C, measure deGFP expression using the standard green fluorescence channel (ex: 485 nm, em: 515 nm).
  
## Return reagents to their appropriate storage locations
- [ ] Mark the lid of each Cytosol component that you used. The number of dots indicates how many freeze–thaw cycles each component has gone through.

# Downloads

:::::{card}
:header: **Resources**
::::{grid} 1 1 1 1

:::{card}
:header: **Lab-ready Protocol**
{button}`download <generated/assemble-base-cytosol-protocol.pdf>`
:::

::::
:::::

# Supported by

DevNotes that reference this page, not curated attribution.

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Expressing Cell-Free TetO-GFP in Solution with aTc Titration
:link: https://devnotes.nucleus.engineering/articles/01a12d61-686f-7790-8068-f3638be6d7d2
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1650b-08b5-76a5-a679-ac13b0944c15/public/fig2-endpoint-gfp-at-09c04f5579c52340f211668c43f87209.webp)
:::

:::{card} Implementing of a bulk color change module into bacterial quorum sensing
:link: https://devnotes.nucleus.engineering/articles/01a12e6c-b511-7d30-aa95-002d386f751e
:footer: Manuel Bibrowski, Charlie Newell, Jonah McDonald, Niall McIntyre, Julia Purrinos de Oliveira · DevStudio 2026

![](https://pub.curvenote.com/01a1650a-90b4-729f-875b-e4f1ddce3bec/public/colorchange-overnigh-520d47ff723d53997b42c0e1c8c68cdc.webp)
:::

:::{card} TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning
:link: https://devnotes.nucleus.engineering/articles/01a1304b-1c56-7352-a082-ba84a2684f82
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-ebfe-71b5-b20a-66b33af95dfb/public/fig7-patterned-gel-5fc6273fa124c69e6d78ac4caafe3ce4.webp)
:::

::::
