---
title: "Make Small Molecule Mix"
subtitle: "Process"
---

# Overview

Small Molecule Mix is a combination of thirty-one (31) small molecules (*e.g.*, rNTPs, amino acids, buffering salts, etc.) needed to fuel transcription and translation. Here, we describe the components of Small Molecule Mix, how to make it, and how to store it properly.


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

- [Make Amino Acid Mix (3.25 mM)](../make-amino-acid-mix/main.md)

::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

- None

::::::

::::::{attention} Critical Materials
:class: dropdown
:icon: false

:::{table}
:label: tbl:critical-materials
:align: center

| **Reagent** | **Product Name** | **Manufacturer** | **Part #** | **Price** | Storage Conditions | **Link** |
| --- | --- | --- | --- | --- | --- | --- |
| Folinic acid | Folinic acid calcium salt hydrate | Sigma-Aldrich | F7878-100MG | $108 | 4C to 30C | [[link](https://www.sigmaaldrich.com/US/en/product/sial/f7878)] |

:::

::::::

::::::{attention} Genetically Encoded Components
:class: dropdown
:icon: false

- None

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::{table} 
:label: tbl:composition-table
:align: center

| **Reagent** | **Concentration in Small Molecule Mix (mM)** | **Concentration in Final Reaction (mM)** |
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

::::::

::::::{note} References
:class: dropdown
:icon: false

- None

::::::

:::::::

# Protocol

## Prepare Folinic Acid Stock (5 mM).
- [ ]  Weigh 12.5 mg folinic acid.
- [ ]  Dissolve to a final volume of 4.89 mL.
- [ ]  Aliquot and freeze at -20C.

## Make All Other Stock Solutions.
- [ ] Use the table below to prepare the specified stock solutions: 

:::{table}
:label: tbl:stock-solutions
:align: center

| Reagent | **MW (g/mol)** | **Amount (g)** | **Final Volume (mL)** | **Storage** | **Needs pH adjustment?** | **Needs Sterilization?** |
| --- | --- | --- | --- | --- | --- | --- |
| Potassium Hydroxide (1 M) | 56.11 | 14.0 | 250 | 4C to 30C | no | no |
| HEPES-KOH (pH 7.6, 1 M) | 238.3 | 59.5 | 250 | 4C to 30C; dark | yes | no |
| Potassium glutamate (2.5 M) | 203.23 | 21.8 | 50 | 4C to 30C | no | no |
| Magnesium acetate (1 M) | 214.45 | 10.8 | 50 | 4C to 30C | no | no |
| Creatine phosphate (500 mM) | 327.14 | 1 | 9.43 | -25C to -15C | no | no |
| Folinic acid (5 mM) | 511.50 | See above  |  | -25C to -15C | no | no |
| Spermidine (500 mM) | 145.25 | 1 | 13.77 | -25C to -15C | no | no |
| Amino Acid Mix |  |  | see [Make Amino Acid Mix](../make-amino-acid-mix/process-Make_Amino_Acid_Mix.md)  | -85C to -15C | yes | yes |

:::

## Assemble Small Molecule Mix Components.
- [ ] Use the table below to combine the previously prepared stock solutions into Small Molecule Mix:

:::{table}
:label: tbl:assembly
:align: center

| **Reagent** | **Stock Concentration (mM)** | **Concentration in Small Molecule Mix (mM)** | **Volume to Add (uL)** |
| --- | --- | --- | --- |
| HEPES-KOH (pH 7.6) | 1000 | 125 | 62.5 |
| Potassium glutamate | 2500 | 250 | 50.0 |
| Magnesium acetate | 1000 | 18.75 | 9.38 |
| rATP | 100 | 5 | 25.0 |
| rGTP | 100 | 5 | 25.0 |
| rCTP | 100 | 2.5 | 12.5 |
| rUTP | 100 | 2.5 | 12.5 |
| Creatine phosphate | 500 | 50 | 50.0 |
| TCEP | 500 | 2.5 | 2.5 |
| Folinic acid | 5 | 0.05 | 5.0 |
| Spermidine | 500 | 5 | 5.0 |
| Amino Acid Mix | 3.25 | 0.75 | 115.4 |
| Ultrapure water |  n/a |  n/a | 15.82 |
| **Total** |  |  | 500 |

:::

## Storage
- [ ]  Aliquot Small Molecule Mix into 1.5 mL microfuge tubes (between 50 uL and 100 uL per aliquot) and store at -80C.


# Downloads

:::::{card}
:header: **Resources**
::::{grid} 1 1 1 3

:::{card}
:header: **Lab-ready Protocol**
{button}`download <protocol-make_small_molecule_mix.pdf>`
:::

:::{card}
:header: **Assembly Worksheet**
{button}`download <Nucleus_v0.3.0_EMix-worksheet.xlsx>`
:::

:::{card}
:header: **Bill of Materials**
{button}`download <protocol-make_trnas.pdf>`
:::

::::
:::::