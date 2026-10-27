---
title: "Protein Mix (PMix)"
subtitle: "Module Specification"
status: validated-published
site:
    hide-toc: true
    numbered_references: false
---

(pmix-overview)=
# Overview

Protein Mix (PMix) contains the 36 proteins of the PURE system at a total of 15 µg/µL in Protein Buffer: the 20 aminoacyl-tRNA synthetases, three initiation factors, three elongation factors, four release factors, five metabolic enzymes (MTF, CK, AK, NDK, PPiase), and T7 RNA polymerase (T7RNAP). With [Small Molecule Mix (SMix)](../smix/spec.md), ribosomes, and tRNA, it makes [Base Cytosol](../base-cytosol/spec.md).

(pmix-reference-composition)=
# Reference Composition

:::::{tab-set}

::::{tab-item} Proteins
:::{table} Composition of the Protein Mix (PMix) at stock concentration. Molecular weight, stoichiometry, and molarity are computed as described in the note below.
:label: comp-pmix

| Category           | Protein | Concentration (ng/µL) | Molecular Weight (kDa) | Stoichiometry         | Molarity (µM) |
| ------------------ | ------- | --------------------- | ---------------------- | --------------------- | ------------- |
| tRNA Synthetases   | AlaRS   | 1086                  | 96.0                   | Homotetramer          | 2.83          |
|                    | ArgRS   | 30                    | 64.7                   | Monomer               | 0.464         |
|                    | AsnRS   | 341                   | 52.6                   | Homodimer             | 3.24          |
|                    | AspRS   | 125                   | 65.9                   | Homodimer             | 0.948         |
|                    | CysRS   | 18                    | 52.2                   | Monomer               | 0.345         |
|                    | GlnRS   | 59                    | 63.5                   | Monomer               | 0.929         |
|                    | GluRS   | 196                   | 53.8                   | Monomer               | 3.64          |
|                    | GlyRS\* | 149                   | 223.2                  | Heterotetramer (α₂β₂) | 0.668         |
|                    | HisRS   | 12                    | 47.0                   | Homodimer             | 0.128         |
|                    | IleRS   | 622                   | 104.4                  | Monomer               | 5.96          |
|                    | LeuRS   | 63                    | 97.2                   | Monomer               | 0.648         |
|                    | LysRS   | 99                    | 57.6                   | Homodimer             | 0.859         |
|                    | MetRS   | 36                    | 76.3                   | Homodimer             | 0.236         |
|                    | PheRS\* | 264                   | 248.4                  | Heterotetramer (α₂β₂) | 1.06          |
|                    | ProRS   | 155                   | 63.7                   | Homodimer             | 1.22          |
|                    | SerRS   | 30                    | 48.4                   | Homodimer             | 0.310         |
|                    | ThrRS   | 97                    | 74.0                   | Homodimer             | 0.655         |
|                    | TrpRS   | 97                    | 37.4                   | Homodimer             | 1.30          |
|                    | TyrRS   | 10                    | 47.5                   | Homodimer             | 0.105         |
|                    | ValRS   | 28                    | 108.2                  | Monomer               | 0.259         |
| Initiation Factors | IF1     | 155                   | 8.2                    | Monomer               | 18.9          |
|                    | IF2     | 622                   | 97.3                   | Monomer               | 6.39          |
|                    | IF3     | 155                   | 20.6                   | Monomer               | 7.52          |
| Elongation Factors | EF-G    | 777                   | 77.6                   | Monomer               | 10.0          |
|                    | EF-Tu   | 7764                  | 43.3                   | Monomer               | 179           |
|                    | EF-Ts   | 777                   | 30.4                   | Monomer               | 25.6          |
| Release Factors    | RF1     | 155                   | 40.5                   | Monomer               | 3.83          |
|                    | RF2     | 155                   | 41.3                   | Monomer               | 3.75          |
|                    | RF3     | 155                   | 59.6                   | Monomer               | 2.60          |
|                    | RRF     | 155                   | 20.6                   | Monomer               | 7.52          |
| Metabolism         | MTF     | 311                   | 34.2                   | Monomer               | 9.09          |
|                    | CK      | 63                    | 43.3                   | Homodimer             | 0.727         |
|                    | AK      | 46                    | 23.6                   | Monomer               | 1.95          |
|                    | NDK     | 16                    | 15.5                   | Homohexamer           | 0.172         |
|                    | PPiase  | 16                    | 19.7                   | Homohexamer           | 0.135         |
| Transcription      | T7RNAP  | 155                   | 98.9                   | Monomer               | 1.57          |
| **Total**          |         | **15 000**            |                        |                       |               |
:::

:::{note} Molecular weight calculations
Molarity is computed as monomer molarity (µM) = mass concentration (ng/µL) ÷ monomer MW (kDa); for an assembled complex the monomer molarity is then divided by the oligomeric state.

\* **GlyRS, PheRS** — both are α₂β₂ heterotetramers of two different subunits (GlyRS: GlyQ 34.8 kDa + GlyS 76.8 kDa; PheRS: PheS 36.8 kDa + PheT 87.4 kDa). The Molecular Weight column reports the combined complex mass (2 × (α + β)); molarity is mass concentration ÷ this combined mass, since the two subunits cannot be reduced to one monomer MW times a single n.
:::
::::

::::{tab-item} Small Molecules
:::{table} Small molecules of the Protein Mix (PMix) at stock concentration. All come from Protein Buffer with 30 % glycerol.
:label: comp-pmix-small-molecules

| Component          | Concentration |
| ------------------ | ------------- |
| HEPES-KOH (pH 7.6) | 50 mM         |
| Potassium chloride | 100 mM        |
| Magnesium chloride | 10 mM         |
| TCEP               | 1 mM          |
| Glycerol           | 300 mL/L      |
:::
::::

:::::

(pmix-processes)=
# Processes

- [Make Protein Mix](../../processes/make-36pot/main.md) — from the 36 proteins, each purified on its own
- [Make OnePot Protein Mix](../../processes/make-1pot/main.md) — makes OnePot Protein Mix, a functional equivalent of PMix with the same proteins at molar ratios that cannot be controlled
- [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md) — 1.2 µL of PMix per 10 µL reaction

(pmix-credits)=
# Credits

Reformulated by Yemo Ku and Jon Calles (b.next) from the PURE system, developed by the Ueda Lab ([Shimizu et al., 2001](https://doi.org/10.1038/90802)).
