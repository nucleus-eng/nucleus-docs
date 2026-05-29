---
title: Make Protein Mix (36-pot)
---

# Overview

Make Protein Mix (36-pot) combines thirty-six individually purified His-tagged proteins of the PURE system into a single Protein Mix, then concentrates and quality-checks the mix before aliquoting for storage. Each protein is purified separately using the [Make Protein](../make-protein/make-protein-main.md) subprocess family; this protocol covers only the final assembly, concentration, measurement, and aliquoting steps. The output is a Protein Mix at **[TODO: confirm — 15 mg/mL?]** total protein in Protein Buffer (30% glycerol), stored as 13 µL aliquots at -80°C.

<!-- Delete any dropdown whose only content is "- None" before publishing.
     If all dropdowns are removed, delete this entire card block. -->
:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{seealso} Prerequisite Documentation
:class: dropdown
:icon: false

Complete all of the following before beginning this protocol. Each of the thirty-six proteins must be individually purified and stored at -80°C in Protein Buffer (30% glycerol).

- [Prepare Protein Purification Buffers and Media](../make-protein/prep-consumables/main.md)
- [Grow and Induce Expression Strains](../make-protein/grow-bacteria/main.md)
- [Lyse Bacteria by Sonication](../make-protein/lysis-sonication/main.md)
- [Purify Proteins by Ni2+ Gravity Column](../make-protein/purify-proteins-grav-column/main.md)
- [Exchange Buffers and Concentrate by Spin Filtration](../make-protein/buff-ex-spin-filters/main.md)
- [Pierce660 Assay](../pierce660/main.md) — for measuring individual protein concentrations before assembly and total Protein Mix concentration after assembly
- [Protein Gel](../protein-gel/main.md) — for verifying purity of individual proteins before assembly

::::::

::::::{attention} Genetically Encoded Components
:class: dropdown
:icon: false

All thirty-six PURE system expression constructs (pET28a backbone, T7 promoter, kanamycin resistance) are maintained in the Nucleus DNA repository:

- [nucleus-eng/DNA — PURE/expression/](https://github.com/nucleus-eng/DNA/tree/main/PURE/expression)

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::{table}
:label: tbl:composition-36pot
:align: center

| **Component** | **Stock Concentration** | **Reaction Concentration** |
| --- | --- | --- |
| Protein Mix | [TODO: confirm — 15 mg/mL?] (total protein) | [TODO: reaction concentration] |

:::

::::::

::::::{note} References
:class: dropdown
:icon: false

- [Cell-free translation reconstituted with purified components](https://doi.org/10.1038/90802)
- [A Simple, Robust, and Low-Cost Method To Produce the PURE Cell-Free System](https://doi.org/10.1021/acssynbio.8b00427)
- [OnePot PURE Cell-Free System](https://dx.doi.org/10.3791/62625)

::::::

:::::::

# Protocol

## Step 1: Compute Mix Volumes

- [ ] **Open the [Protein Mix Assembly Calculator](https://docs.google.com/spreadsheets/d/1OLFNVuiL5-f6FAD-eY3rEHRrYya3oPlh2JK1UhwY7qs/edit?usp=sharing) and follow the directions therein.**
    - [ ] Enter the desired number of 10 µL PURE reactions into the blue-highlighted cell.
    - [ ] Enter the measured concentration and available volume for each of the thirty-six protein stocks into the blue-highlighted cells.
    - [ ] Check the "Checklist" tab for any yellow-highlighted cells and resolve flagged items before proceeding.

:::{hint} Note: if your Protein Mix will be dilute, you can concentrate it after assembly.
:class: dropdown
When combining dilute protein stocks, the assembled Protein Mix may have the correct molar ratios but a total concentration that is too low. You can concentrate the final mix after assembly using a 3 kDa Amicon centrifugal filter (see [Exchange Buffers and Concentrate by Spin Filtration](../make-protein/buff-ex-spin-filters/main.md)). We routinely design assembly reactions at low target concentration and concentrate afterward.
:::

## Step 2: Assemble Protein Mix

- [ ] **Thaw protein stocks on ice.**
- [ ] **Combine proteins according to the volumes calculated in Step 1.**
    - [ ] Pipette each protein into a single tube in the order listed on the calculator sheet.
    - [ ] Mix gently by pipetting after all proteins have been added.

## Step 3: Wash and Concentrate

- [ ] **Wash assembled Protein Mix by diluting 10x in Protein Buffer** (e.g., 2.4 mL Protein Buffer for 240 µL Protein Mix).

:::{hint} Note: washing removes purification buffer carry-over and glycerol.
:class: dropdown
Washing the assembled mix before concentrating removes residual salts (Na+, Imidazole) carried over from individual protein purifications, and removes glycerol, which makes the mix easier to concentrate. Use a 3 kDa Amicon centrifugal filter for concentration. See [Exchange Buffers and Concentrate by Spin Filtration](../make-protein/buff-ex-spin-filters/main.md) for detailed spin-filtration instructions.
:::

- [ ] **Concentrate using a 3 kDa Amicon centrifugal filter** until the mix is at or above your target final concentration.

## Step 4: Measure Total Protein Concentration

- [ ] **Prepare 10x dilutions of Protein Mix in triplicate** (1 µL Protein Mix + 9 µL ultrapure water per replicate).
- [ ] **Measure total protein concentration by [Pierce660 Assay](../pierce660/main.md)** on the diluted triplicates.
- [ ] **Calculate total protein concentration**: average the three replicates and multiply by 10.

## Step 5: Dilute to Final Concentration

- [ ] **If concentration exceeds target, dilute Protein Mix to [TODO: confirm — 15 mg/mL?] in Protein Buffer (30% glycerol).**
    - [ ] Prepare Protein Buffer (30% glycerol) by mixing equal volumes of Protein Buffer and Protein Buffer (60% glycerol).
    - [ ] Add the calculated volume to reach target concentration and mix gently.
- [ ] **If concentration is below target, return to Step 3** — concentrate further, then re-measure.

## Step 6: Aliquot and Store

- [ ] **Aliquot Protein Mix into PCR tubes or microcentrifuge tubes** (12 µL + 1 µL headroom = 13 µL per tube).
- [ ] **Store aliquots at -80°C.**

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**
:align: center

{button}`download <TODO: protocol.pdf>`
:::

:::{card}
:header: **Protein Mix Assembly Calculator**

[Open in Google Sheets](https://docs.google.com/spreadsheets/d/1OLFNVuiL5-f6FAD-eY3rEHRrYya3oPlh2JK1UhwY7qs/edit?usp=sharing)

{button}`download <resources/protein-mix-calculator.xlsx>`
:::

::::
