---
title: Process
subtitle: Assemble Base Cell
---

# Overview

PURE liposomes are the basis of a synthetic cell that can perform the fundamental operations of biology: transcription, and translation.

In this protocol, you will make the necessary precursors to creating liposomes, assemble a PURE cell-free reaction that will express Green Fluorescent Protein (GFP), and encapsulate it within a liposome. For the outer solution, you will use the same simple sugar solution that was used in Buffer-in-Buffer Liposomes.

Successfully built PURE liposomes will start dark and then increase in green fluorescence over time as GFP is produced.

::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

:::{note} Notes
:class: dropdown

- ‼️All reagents and materials must be prepared RNase-free. Use RNaseZap or 10% bleach to decontaminate plastic and glassware and rinse with nuclease-free water. We find ultrapure water (18.2 MOhm) is often sufficient for RNase-free work.

:::

:::::{card}
:header: **Resources**
::::{grid} 1 1 1 3

:::{card}
:header: **Lab-ready Protocol**
:align: center

{button}`download <protocol-make_template.pdf>`
:::

:::{card}
:header: **Assembly Worksheet**
{button}`download <Nucleus_v0.3.0_AA_worksheet.xlsx>`
:::

:::{card}
:header: **Bill of Materials**
{button}`download <protocol-Make_tRNAs.pdf>`
:::

::::
:::::

:::::{tip} Composition
:class: dropdown

::::{card}
:header: **Composition of Small Molecule Mix**
:::{table} 
:label: tbl:composition-table
:align: center

| **Reagent** | **Concentration in Energy Mix (mM)** | **Concentration in Final Reaction (mM)** |
| --- | --- | --- |
| HEPES-KOH (pH 7.6) | 125 | 50 |
| Potassium glutamate | 250 | 100 |
| Magnesium acetate | 18.75 | 7.5 |
| rATP  | 5 | 2 |
| rGTP | 5 | 2 |
| rCTP | 2.5 | 1 |
| rUTP | 2.5 | 1 |
| Amino Acids (each) | 0.75 | 0.3 |
| Creatine phosphate | 50 | 20 |
| Folinic acid | 0.05 | 0.02 |
| Spermidine | 5 | 2 |
| TCEP | 2.5 | 1 |

:::
::::
:::::

:::{seealso} Prerequisite Documentation
:class: dropdown
- None

:::

::::{important} Critical Materials
:class: dropdown

:::{table}
:label: tbl:critical-materials
:align: center

| Reagent | **Product Name** | **Manufacturer** | **Part #** | **Price** | Storage Conditions | **Link** |
| --- | --- | --- | --- | --- | --- | --- |
| Amino Acids | L-Amino acids, analytical standard | Sigma-Aldrich | LAA21-1KT | $558 | 1C to 4C | [[link](https://www.sigmaaldrich.com/US/en/product/sial/laa21)] |
| Low Bind Protein Tubes | X | X | X | X | X | X |

::::

::::{important} Genetically Encoded Components
:class: dropdown

:::{table}
:label: tbl:critical-materials
:align: center

| Reagent | **Product Name** | **Manufacturer** | **Part #** | **Price** | Storage Conditions | **Link** |
| --- | --- | --- | --- | --- | --- | --- |
| Amino Acids | L-Amino acids, analytical standard | Sigma-Aldrich | LAA21-1KT | $558 | 1C to 4C | [[link](https://www.sigmaaldrich.com/US/en/product/sial/laa21)] |
| Low Bind Protein Tubes | X | X | X | X | X | X |

::::

::::{danger} Hazardous Materials
:class: dropdown

- **Acid Phenol**
    - Corrosive, toxic, rapidly absorbed through skin, & respiratory irritant
    - Use in fume hood, wear neoprene gloves, & PPE

- **Acetic Acid**
    - Corrosive to skin and eyes
    - Use appropriate PPE and handle under fume-hood

- **Chloroform**
    - Irritant, possible carcinogen
    - Work in fume hood & appropriate gloves

- **Ethanol**
    - Highly flammable, toxic, and irritant
    - Wear PPE, use in well-ventilated areas, and keep away from open flames

::::

::::{note} References
:class: dropdown

- None

::::

::::::

# Protocol

## Prepare Stock Buffers and Lipids

- **Prepare lipids in mineral oil**

  - [ ]  Clean glass syringes.
      - [ ]  Pour a small amount of 95% ethanol into a glass container (e.g. a 10 mL beaker).
      - [ ]  Assemble the glass syringe and prime it by drawing ethanol into the glass syringe, then empty into a waste bottle.
  - [ ]  Weigh 2.67 g (or pipette 3.25mL) mineral oil into a glass test tube or beaker
  - [ ]  Add the lipids to the mineral oil using the appropriate glass syringe:
      - [ ]  Add 480 uL 25 mg/mL POPC.
      - [ ]  *Rinse the syringe with ethanol.*
      - [ ]  Add 15 uL 1 mg/mL Liss Rhod PE.
      - [ ]  *Rinse the syringe with ethanol.*
  - [ ]  Evaporate the chloroform from the lipid–oil mixture:
      - [ ]  Place lipid beaker in a 55°C dry bath in a fume hood.
      - [ ]  *(optional)* Shield with aluminum foil to protect from light.
      - [ ]  Evaporate uncovered for 3 h.
  - [ ]  Clean syringes and store with plunger removed
  - [ ]  Let the sample cool to room temperature in the fume hood.
      - [ ]  If lipids settle towards the bottom, stir them using a pipette tip.
      - [ ]  Aliquot the lipid–oil mixture into 1.5 mL aliquots, in glass jars.
      - [ ]  The lipid–oil mixture can be stored for a week or more at room temperature, or up to one month at 4C.
      - [ ]  Invert gently 3 times before use. Make sure the solution is not cloudy.

- **Prepare sugar stock stock solutions**

  - [ ]  Make 3M glucose stock solution:
      - [ ]  Combine 5.40 g glucose and 5.0 mL ddH2O in a 50 mL tube.
      - [ ]  Heat for 15 s in a microwave and mix vigorously to dissolve material completely.
      - [ ]  Add additional ddH2O to achieve a final volume of 10 mL.
      - [ ]  Filter sterilize while warm using a 0.22 um filter and store at -20 C.
  - [ ]  Make 2M sucrose stock solution:
      - [ ]  Combine 10.27 g sucrose and 5.0 mL ddH2O in a 50 mL tube.
      - [ ]  Heat for 15 s and mix vigorously to dissolve material completely.
      - [ ]  Add additional ddH2O to achieve a final volume of 15 mL.
      - [ ]  Filter sterilize using a 0.22 um filter and store at -20 C.

| Buffer | Target Concentration (M) | MW (kDa) | Weight (g) | Final Volume (mL) |
| --- | --- | --- | --- | --- |
| **3M Glucose Stock** | 3.0 | 180.16 | 5.40 | 10.0 |
| **2M Sucrose Stock** | 2.0 | 342.3 | 10.27 | 15.0 |

- **Prepare outer buffer**

  - [ ]  Make a 800 mM glucose outer solution:
      - [ ]  Add 0.8 mL 3M glucose stock solution to a 15 mL tube.
      - [ ]  Add ddH2O water to a final volume of 3 mL.
      - [ ]  Vortex vigorously to mix.

