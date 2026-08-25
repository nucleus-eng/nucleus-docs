---
title: "SUV Encapsulation"
subtitle: "Process"
status: draft
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

SUV Encapsulation prepares small unilamellar vesicles (SUVs) by lipid-film hydration and extrusion, then loads them with a chromogenic substrate. In the Chicago colorimetric readout system, SUVs carry chlorophenol red-β-D-galactopyranoside (CPRG) as a pre-loaded cargo. CPRG is a yellow substrate that turns purple (chlorophenol red, CPR) when cleaved by β-galactosidase (LacZ). SUVs are one half of a two-liposome system: synthetic cells carry the sensing and cell-free expression machinery and, on activation, express phospholipase A1 (PLA1), which lyses neighboring CPRG-loaded SUVs. Released CPRG then reacts with LacZ in the surrounding matrix to produce the visible color change.

SUVs and synthetic cells are distinct particle-size classes and are never interchangeable. This process produces SUVs only. For synthetic cell production, see [Encapsulation: Phase Transfer](../assemble-base-cell/main.md).

SUV Encapsulation feeds only the alginate hydrogel embedding step of the process-dependency diagram. This differs from [Encapsulation: Phase Transfer](../assemble-base-cell/main.md), whose synthetic cells feed both alginate hydrogel embedding and ULGA hydrogel embedding.

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{attention} Known limitation: CPRG-loaded SUVs are incompatible with PEG-norbornene gelation
:class: dropdown
:icon: false

CPRG pre-loaded into SUVs photobleaches during the UV crosslinking step of PEG-norbornene hydrogel formation. Side-by-side comparisons confirm that UV exposure during PEG-norbornene crosslinking visibly bleaches the CPRG color, while an unexposed control retains it.

This is specific to PEG-norbornene. Agarose, alginate, and ULGA hydrogel embedding do not expose SUVs to a UV crosslinking step and do not show this problem — the SUV pre-loading approach described in this process is compatible with the alginate hydrogel embedding process it is normally paired with.

**Confirmed workaround for PEG-norbornene only:** add CPRG as a free dye after crosslinking, instead of pre-loading it into SUVs, with LacZ pre-added to the gel. Do not use this workaround as a default — it is only needed when pairing SUVs with PEG-norbornene gelation.
::::::

::::::{danger} Hazardous Materials
:class: dropdown
:icon: false

**Chloroform** - Irritant, possible carcinogen. Work in a fume hood and use gloves.

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::{table}
:label: comp-membrane-suv

| Component   | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ----------- | ---------------------- | ------------------------- | ---------------------------- | -------------------- |
| POPC        | 90                      | 760.076                    | 25                             | 208.51               |
| Cholesterol | 10                      | 386.654                    | 50                             | 6.00                 |

:::

See [Base Membrane](../../modules/membrane-popc-chol/spec.md) for the lipid source. This process uses a 9:1 POPC:cholesterol ratio, matching the Chicago colorimetric readout system's SUV composition, rather than the Base Membrane's default 70:29.95:0.05 POPC:cholesterol:Liss-Rhod PE ratio used for synthetic cells.

::::::

:::::::

# Materials and Equipment

:::{table}
:label: bom-encapsulate-suv
:align: center

| Name                             | Category   | Product                                                                        | Manufacturer      | Part #      | Price   | Storage          | Link                                                                                                                                                                                              |
| --------------------------------- | ----------- | -------------------------------------------------------------------------------- | ------------------- | ------------ | -------- | ------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| POPC                              | Lipid       | 16:0-18:1 PC 25 mg/mL                                                            | Avanti Lipids      | A80557       | $435.00 | -20 °C            | [link](https://www.avantiresearch.com/en-gb/products/product/850457-160-181-pc-popc)                                                                                                                |
| Cholesterol                       | Lipid       | Cholesterol (plant)                                                              | Avanti Research    | A80100       | $261.00 | -20 °C            | [link](https://www.avantiresearch.com/en-gb/products/product/700100-cholesterol-plant)                                                                                                              |
| Chloroform                        | Chemical    | Chloroform, suitable for HPLC, ≥99.8%, contains 0.5-1.0% ethanol as stabilizer   | Sigma-Aldrich      | 366927       | $94.30  | RT (flammables cabinet) | [link](https://www.sigmaaldrich.com/US/en/product/sigald/366927)                                                                                                                                     |
| CPRG                               | Reagent     | Chlorophenol red-β-D-galactopyranoside                                          | Roche              | 10884308001  | $160.00 | -20 °C, in water at 10 mg/mL | [link](https://www.sigmaaldrich.com/US/en/product/roche/10884308001)                                                                                                                                 |
| Glass round-bottom flask (25 mL)  | Equipment   | Round bottom flask, single neck, 25 mL, 24/40 joint                              | Chemglass          | CG-1506-06   | $58.00  | RT               | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/z564494)                                                                                                                                   |
| Rotary evaporator                 | Equipment   | Benchtop rotary evaporator                                                       | Buchi              | R-100        | -       | RT               | [link](https://www.buchi.com/en)                                                                                                                                                                     |
| Mini-extruder                     | Equipment   | Avanti Mini-Extruder Set                                                        | Avanti Lipids      | 610000       | $780.00 | RT               | [link](https://www.avantilipids.com/product/610000)                                                                                                                                                  |
| Polycarbonate membrane (400 nm)   | Consumable  | Whatman Nuclepore Track-Etched Membrane, 400 nm pore, 19 mm                      | Avanti Lipids      | 610007       | $110.00 | RT               | [link](https://www.avantilipids.com/product/610007)                                                                                                                                                  |
| Size-exclusion column              | Consumable  | PD-10 Desalting Column, Sephadex G-25 resin                                     | Cytiva             | 17085101     | $6.50   | RT               | [link](https://www.cytivalifesciences.com/en/us/shop/protein-purification/gel-filtration-chromatography/desalting-columns/pd-10-desalting-columns-p-05808)                                          |
| Glass syringes (1 mL)             | Equipment   | Hamilton gastight glass syringe, 1 mL                                            | Hamilton           | 81320        | $99.00  | RT               | [link](https://www.hamiltoncompany.com/laboratory-products/syringes/81320)                                                                                                                           |

:::

# Protocol

## Prepare Lipid Film

- [ ] Combine the lipids in {ref}`comp-membrane-suv` in a 25 mL glass round-bottom flask using a glass syringe.

:::{warning} Warning
:class: simple
:icon: false
Work inside of a fume hood when handling chloroform.
:::

- [ ] Evaporate the chloroform under reduced pressure on a rotary evaporator until a thin, uniform lipid film forms on the flask wall.
- [ ] Place the flask under vacuum for at least 1 h to remove residual chloroform.

:::{hint} Note
:class: simple
:icon: false
The dried lipid film can be stored under argon or nitrogen at -20 °C for up to one week, wrapped in foil to protect from light, before hydration.
:::

## Hydrate with CPRG

- [ ] Prepare a hydration buffer containing 50 mM CPRG.
- [ ] Add hydration buffer to the dried lipid film to reach a total lipid concentration of 25 mg/mL.
- [ ] Hydrate the film by gentle vortexing until the lipid is fully resuspended and the solution appears uniformly turbid, then rest at room temperature for 30 min.

:::{hint} Note
:class: simple
:icon: false
Hydration produces a heterogeneous population of large, multilamellar liposomes. Extrusion (below) narrows this population to small unilamellar vesicles of a defined size.
:::

## Extrude

- [ ] Assemble the mini-extruder with a 400 nm polycarbonate membrane per the manufacturer's instructions.
- [ ] Load the hydrated lipid suspension into one glass syringe and pass it through the membrane into the second syringe.
- [ ] Pass the suspension back and forth through the membrane at least 21 times (an odd number of passes to avoid retaining larger, unextruded liposomes in the final syringe).
- [ ] Collect the extruded SUV suspension from the final syringe.

## Purify by Size-Exclusion Chromatography

- [ ] Equilibrate a size-exclusion column with hydration buffer lacking CPRG.
- [ ] Load the extruded SUV suspension onto the column and elute with CPRG-free buffer, collecting the liposome fraction (elutes in the column void volume, ahead of free CPRG).
- [ ] Repeat the size-exclusion step a second time on the collected liposome fraction to remove residual unencapsulated CPRG.

:::{hint} Tip
:class: simple
:icon: false
A single SEC pass leaves detectable free CPRG in the eluate. Two passes are needed to reduce background color development from unencapsulated substrate.
:::

- [ ] Hold purified CPRG-loaded SUVs on ice or at 4 °C until ready to combine with synthetic cells and LacZ.

# Quality Control

Confirm successful encapsulation and purification before combining SUVs with other components:

- **Size**: Confirm a mean diameter near 400 nm by dynamic light scattering (DLS). A single narrow peak indicates a homogeneous, well-extruded population.
- **Free CPRG removal**: Measure absorbance at 575 nm of the SEC flow-through (not the liposome fraction). A flat, low-absorbance flow-through after the second SEC pass indicates unencapsulated CPRG has been removed. Residual absorbance in the flow-through after two passes indicates incomplete purification — repeat the SEC step.

:::{attention} Primary data not located
@Editor: the 400 nm target size and 50 mM CPRG loading concentration are not independently verified against primary data — no devnote with DLS traces or absorbance QC data for this process exists yet.
:::

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).

# Downloads

::::{grid} 1 1 1 1

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/encapsulate-suv-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/encapsulate-suv-bom.pdf>`
:::

::::
