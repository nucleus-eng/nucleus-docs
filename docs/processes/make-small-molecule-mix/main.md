---
title: "Make Small Molecule Mix"
subtitle: "Process"
---

# Overview

Small Molecule Mix (SMix) is a combination of thirty-one (31) small molecules (*e.g.*, rNTPs, amino acids, buffering salts, etc.) needed to fuel transcription and translation. Here, we describe the components of SMix, how to make it, and how to store it properly.


:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

- [Make Amino Acid Mix (3.25 mM)](../make-amino-acid-mix/main.md)

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

:::::::

# Materials and Equipment

:::{table} Bill of Materials
:label: bom-make-small-molecule-mix

| Name                    | Category | Product                                                                | Manufacturer      | Part #      | Price   | Storage        | Link                                                                                 |
| ----------------------- | -------- | ---------------------------------------------------------------------- | ----------------- | ----------- | ------- | -------------- | ------------------------------------------------------------------------------------ |
| Potassium Hydroxide     | Salts    | Potassium hydroxide - ACS reagent, ≥85%, pellets                       | Sigma-Aldrich     | 221473-1KG  | $99.90  | 4°C to 30°C    | [link](https://www.sigmaaldrich.com/US/en/product/sigald/221473)                     |
| Hydrochloric acid (1 M) | Salts    | Hydrochloric acid 1 N, Reagent Grade, 500 mL                           | VWR               | E447-500L   | $72.46  | 4°C to 30°C    | [link](https://www.vwr.com/us/en/product/NA2214615/hydrochloric-acid-1-n-reagent-grade?isCatNumSearch=true&searchedCatalogNumber=97064-756) |
| HEPES                   | Salts    | HEPES, Crystalline Powder, ≥99.5% (titration), Poly bottle             | Sigma-Aldrich     | H3375-500G  | $431    | 4°C to 30°C    | [link](https://www.sigmaaldrich.com/US/en/product/sigma/h3375)                       |
| Potassium Glutamate     | Salts    | L-Glutamic acid potassium monohydrate                                  | Sigma-Aldrich     | G1501-100G  | $74.80  | 4°C to 30°C    | [link](https://www.sigmaaldrich.com/US/en/product/sigma/g1501)                       |
| Magnesium acetate       | Salts    | Magnesium acetate tetrahydrate                                         | Sigma-Aldrich     | M0631-100G  | $34.80  | 4°C to 30°C    | [link](https://www.sigmaaldrich.com/US/en/product/sigald/m0631)                      |
| rATP                    | NTP      | Adenosine 5′-triphosphate disodium salt hydrate, BioXtra, ≥99% (HPLC)  | Sigma-Aldrich     | A7699-1G    | $125.00 | -25°C to -15°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/a7699)                       |
| rGTP                    | NTP      | Guanosine 5′-triphosphate sodium salt hydrate, ≥95% (HPLC), powder     | Sigma-Aldrich     | G8877-100MG | $155    | -25°C to -15°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/g8877)                       |
| rCTP                    | NTP      | Cytidine 5′-triphosphate disodium salt, ≥95%                           | Sigma-Aldrich     | C1506-100MG | $102.00 | -25°C to -15°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/c1506)                       |
| rUTP                    | NTP      | Uridine 5′-triphosphate trisodium salt hydrate, Type IV, ≥93.0% (HPLC) | Sigma-Aldrich     | U6750-100MG | $58.20  | -25°C to -15°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/u6750)                       |
| Creatine phosphate      | Reagent  | Sodium creatine phosphate dibasic tetrahydrate, ≥98.0%(NT)             | Sigma-Aldrich     | 27920-1G    | $102    | -25°C to -15°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/27920)                       |
| TCEP-HCl (500 mM)       | Reagent  | Bond-Breaker® TCEP Neutral Solution, MW 286.65, 5 mL                   | Thermo Scientific | 77720       | $175.65 | 4°C to 30°C    | [link](https://www.thermofisher.com/order/catalog/product/77720)                     |
| Folinic acid            | Reagent  | Folinic acid calcium salt hydrate                                      | Sigma-Aldrich     | F7878-100MG | $108    | 4°C to 30°C    | [link](https://www.sigmaaldrich.com/US/en/product/sial/f7878)                        |
| BME                     | Reagent  | 2-Mercaptoethanol                                                      | Sigma-Aldrich     | M6250-100ML | $65.50  | 4°C to 30°C    | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/m6250)                     |
| Spermidine              | Reagent  | Spermidine, ≥99% (GC)                                                  | Sigma-Aldrich     | S2626-5G    | $176    | -25°C to -15°C | [link](https://www.sigmaaldrich.com/US/en/product/sigma/s2626)                       |
| tRNA                    | Biologic | Nucleus Total tRNA (50 µg/µL)                                          | b.next            | —           | —       | -25°C to -15°C | [Make tRNAs](../make-trna/main.md)                                                   |
| Amino Acids             | Biologic | Amino Acid Mix (3.25 mM)                                               | b.next            | —           | —       | -80°C to -20°C | [Make Amino Acid Mix](../make-amino-acid-mix/main.md)                                |
:::

# Protocol

## Prepare Folinic Acid Stock (5 mM).
- [ ]  Weigh 12.5 mg folinic acid.
- [ ]  Dissolve to a final volume of 4.89 mL.
- [ ]  Aliquot and freeze at -20°C.

## Make All Other Stock Solutions.
- [ ] Use the table below to prepare the specified stock solutions: 

:::{table}
:label: tbl:stock-solutions
:align: center

| Reagent                     | **MW (g/mol)** | **Amount (g)** | **Final Volume (mL)**                                     | **Storage**     | **Needs pH adjustment?** | **Needs Sterilization?** |
| --------------------------- | -------------- | -------------- | --------------------------------------------------------- | --------------- | ------------------------ | ------------------------ |
| Potassium Hydroxide (1 M)   | 56.11          | 14.0           | 250                                                       | 4°C to 30°C       | no                       | no                       |
| HEPES-KOH (pH 7.6, 1 M)     | 238.3          | 59.5           | 250                                                       | 4°C to 30°C; dark | yes                      | no                       |
| Potassium glutamate (2.5 M) | 203.23         | 21.8           | 50                                                        | 4°C to 30°C       | no                       | no                       |
| Magnesium acetate (1 M)     | 214.45         | 10.8           | 50                                                        | 4°C to 30°C       | no                       | no                       |
| Creatine phosphate (500 mM) | 327.14         | 1              | 9.43                                                      | -25°C to -15°C    | no                       | no                       |
| Folinic acid (5 mM)         | 511.50         | See above      |                                                           | -25°C to -15°C    | no                       | no                       |
| Spermidine (500 mM)         | 145.25         | 1              | 13.77                                                     | -25°C to -15°C    | no                       | no                       |
| Amino Acid Mix              |                |                | see [Make Amino Acid Mix](../make-amino-acid-mix/main.md) | -85°C to -15°C    | yes                      | yes                      |

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
- [ ]  Aliquot Small Molecule Mix into 1.5 mL microfuge tubes (between 50 µL and 100 µL per aliquot) and store at -80°C.


# Downloads

:::::{card}
:header: **Resources**
::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**
{button}`download <generated/make-small-molecule-mix-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**
{button}`download <generated/make-small-molecule-mix-bom.pdf>`
:::

:::{card}
:header: **Assembly Worksheet**
{button}`download <Nucleus_v0.3.0_EMix-worksheet.xlsx>`
:::

::::
:::::
