---
title: Make Protein Mix (36-pot)
---

# Overview
Protein Mix (PMix) is a combination of thirty-six (36) proteins that collectively implement [Nucleus Cytosol](../../modules/base-cytosol/spec.md) along with Small Molecule Mix (SMix), tRNAs, and Ribosomes. These proteins include all 20 canonical aminoacyl-tRNA synthetases (AlaRS, ArgRS, AsnRS, etc) and methionyl-tRNA formyltransferase (MTF); *E. coli* translation initiation factors (IF1, IF2, IF3), elongation factors (EF-G, EF-Ts, EF-Tu), and release factors (RF1, RF2, RF3, RRF); energy regeneration enzymes (AK, CK, NDK, PPiase), and T7 phage RNA polymerase (T7RNAP). This protocol explains how to prepare PMix once each of these proteins has been individually prepared (see [Making Individual Proteins](../make-protein/make-protein-main.md) for protocols describing how to purify each protein).

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

- [nucleus-eng/DNA/PURE/expression/](https://github.com/nucleus-eng/DNA/tree/main/PURE/expression)

::::::

::::::{note} Composition
:class: dropdown
:icon: false

:::{table}
:label: tbl:composition-36pot
:align: center

| **Component** | **Stock Concentration** | **Reaction Concentration** |
| ------------- | ----------------------- | -------------------------- |
| PMix          | 15 mg/mL                | 1.8 mg/mL                  |

:::

| Protein   | Concentration in PMix (ng/µL) | Reaction Concentration (ng/µL) |
| --------- | ----------------------------- | ------------------------------ |
| AlaRS     | 1086                          | 130.3                          |
| ArgRS     | 30                            | 3.6                            |
| AsnRS     | 341                           | 40.9                           |
| AspRS     | 125                           | 15.0                           |
| CysRS     | 18                            | 2.2                            |
| GlnRS     | 59                            | 7.0                            |
| GluRS     | 196                           | 23.5                           |
| GlyRS     | 149                           | 17.9                           |
| HisRS     | 12                            | 1.5                            |
| IleRS     | 622                           | 74.6                           |
| LeuRS     | 63                            | 7.5                            |
| LysRS     | 99                            | 11.9                           |
| MetRS     | 36                            | 4.4                            |
| PheRS     | 264                           | 31.7                           |
| ProRS     | 155                           | 18.7                           |
| SerRS     | 30                            | 3.6                            |
| ThrRS     | 97                            | 11.6                           |
| TrpRS     | 97                            | 11.6                           |
| TyrRS     | 10                            | 1.2                            |
| ValRS     | 28                            | 3.4                            |
| IF1       | 155                           | 18.7                           |
| IF2       | 622                           | 74.6                           |
| IF3       | 155                           | 18.7                           |
| EF-G      | 777                           | 93.3                           |
| EF-Tu     | 7764                          | 931.7                          |
| EF-Ts     | 777                           | 93.3                           |
| RF1       | 155                           | 18.7                           |
| RF2       | 155                           | 18.7                           |
| RF3       | 155                           | 18.7                           |
| RRF       | 155                           | 18.7                           |
| MTF       | 311                           | 37.3                           |
| CK        | 63                            | 7.5                            |
| AK        | 46                            | 5.6                            |
| NDK       | 16                            | 1.9                            |
| PPiase    | 16                            | 1.9                            |
| T7RNAP    | 155                           | 18.7                           |
| **Total** | **15 000**                    | **1800**                       |

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

- [ ] Open the [Protein Mix Assembly Calculator](https://docs.google.com/spreadsheets/d/1OLFNVuiL5-f6FAD-eY3rEHRrYya3oPlh2JK1UhwY7qs/edit?usp=sharing) and follow the directions therein.
    - [ ] Enter how many 10 µL PURE reactions you'd like to prepare next to "PURE Reactions (#)" (default: 200) into the blue-highlighted cell. This defines the total volume of PMix needed.
    - [ ] Enter the concentrations for each of your protein stocks into the blue highlighted cells under "Stock Conc (ng/µL)". This is needed to calculate the required volume for each protein stock.
    - [ ] Check the "Checklist" tab for any yellow-highlighted cells and resolve flagged items before proceeding.

:::{hint} Note: if your Protein Mix target concentration is too dilute, you can concentrate it after assembly.
:class: dropdown
Combining components dilutes each one, thus your assembled PMix may be too dilute even if the molar ratios of each protein are correct. You can concentrate the final PMix after assembly using a 3 kDa Amicon centrifugal filter (see [Exchange Buffers and Concentrate by Spin Filtration](../make-protein/buff-ex-spin-filters/main.md)). We routinely design assembly reactions at low target concentration and concentrate afterward.
:::

## Step 2: Assemble Protein Mix

- [ ] Thaw protein stocks on ice.
- [ ] Combine proteins according to the volumes calculated in Step 1.
    - [ ] Pipette each protein into a single microfuge tube in the order listed on the calculator sheet.
    - [ ] Mix gently by pipetting after all proteins have been added.

## Step 3: Wash and Concentrate

- [ ] Wash assembled PMix by diluting 10x in Protein Buffer (e.g., 2.4 mL Protein Buffer for 240 µL PMix).

:::{hint} Note: washing reduces salt carry-over from purification buffers and removes glycerol.
:class: dropdown
Washing the assembled mix before concentrating removes residual salts (Na+, Imidazole) carried over from individual protein purifications, and removes glycerol, which makes the PMix easier to concentrate. Use a 3 kDa Amicon centrifugal filter for concentration. See [Exchange Buffers and Concentrate by Spin Filtration](../make-protein/buff-ex-spin-filters/main.md) for detailed spin-filtration instructions.
:::

- [ ] Concentrate using a 3 kDa Amicon centrifugal filter until the mix is at or above your target final concentration.

## Step 4: Measure Total Protein Concentration

- [ ] Prepare 10x dilutions of Protein Mix in triplicate (1 µL Protein Mix + 9 µL ultrapure water per replicate).
- [ ] Measure total protein concentration by [Pierce660 Assay](../pierce660/main.md) on the diluted triplicates.
- [ ] Calculate total protein concentration: average the three replicates and multiply by 10.

## Step 5: Dilute to Final Concentration

- [ ] If concentration exceeds target, dilute PMix to 15 mg/mL in Protein Buffer (30% glycerol).
    - [ ] Add the calculated volume to reach target concentration and mix gently.
- [ ] If concentration is below target, return to Step 3 — concentrate further, then re-measure.

## Step 6: Aliquot and Store

- [ ] Aliquot PMix into PCR tubes or microcentrifuge tubes.
- [ ] Store aliquots at -80°C.

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
