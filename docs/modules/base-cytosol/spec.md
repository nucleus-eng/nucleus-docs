---
title: "Base Cytosol"
subtitle: "Module Specification"
status: validated-published
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Base Cytosol is a molecular system with a defined set of components, including purified proteins and _E. coli_ ribosomes and tRNAs that together can perform transcription and translation. It builds on the [PURE system](https://doi.org/10.1038/90802) and is optimized for integration and extension. The [Base Cell](../base-cell/spec.md) is formed by encapsulating Base Cytosol in a liposome. Base Cytosol transcribes a DNA template that carries a T7 promoter and translates a transcript encoding an _E. coli_ ribosome binding site (RBS) and a coding sequence (CDS). It also recycles energetic molecules (rNTPs) from creatine phosphate (CP) and processes waste products (PPi) with a simple energy module (PPiase, Creatine Kinase, adenylate kinase and nucleoside diphosphate kinase). Plasmid designs for the PURE proteins are maintained as pET28a expression vectors in the [DNA Distribution](https://github.com/nucleus-eng/DNA/tree/main/PURE/expression) repository.

:::{figure} schematic.png
:width: 100%
:align: center

Schematic of components in Base Cytosol and their function. Figure by [Ganesh and Maerkl, 2024](https://doi.org/10.1101/2024.04.03.587879) used under CC-BY-4.0 / cropped from original with numerical annotations removed.
:::

# Reference Composition

Base Cytosol is assembled from five components — a protein mix (PMix), a small molecule mix (SMix), ribosomes, tRNA, and an optional RNase inhibitor. The tabs below give the composition of PMix, SMix, ribosomes and tRNA at their **stock** concentration, plus the **Final Reaction** composition with every component at its in-reaction concentration.

:::::{tab-set}

::::{tab-item} PMix
The Protein Mix (PMix) contains all 36 PURE proteins at a total stock concentration of 15 µg/µL.

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

::::{tab-item} SMix
The Small Molecule Mix (SMix) contains the buffers, nucleotides, amino acids, stabilizers, and cofactors. Concentrations below are in the assembled SMix.

:::{table} Composition of the Small Molecule Mix (SMix) at stock concentration.
:label: comp-smix

| Category    | Molecule            | Concentration | Units |
| ----------- | ------------------- | ------------- | ----- |
| Buffers     | HEPES-KOH (pH 7.6)  | 125           | mM    |
|             | Potassium Glutamate | 250           | mM    |
|             | Magnesium Acetate   | 18.75         | mM    |
| Nucleotides | rATP                | 5             | mM    |
|             | rGTP                | 5             | mM    |
|             | rCTP                | 2.5           | mM    |
|             | rUTP                | 2.5           | mM    |
| Amino Acids | Each (Ala–Val)      | 0.75          | mM    |
| Stabilizers | Spermidine          | 5             | mM    |
|             | TCEP-HCl            | 2.5           | mM    |
| Cofactors   | Creatine Phosphate  | 50            | mM    |
|             | Folinic Acid        | 0.05          | mM    |
:::
::::

::::{tab-item} Ribosomes
:::{table} Ribosome stock concentration.
:label: comp-ribosomes

| Component | Stock Concentration | Reaction Concentration |
| --------- | ------------------- | ---------------------- |
| Ribosomes | 10 µM (5.55×)       | 1.8 µM                 |
:::
::::

::::{tab-item} tRNA
:::{table} tRNA stock concentration.
:label: comp-trna

| Component | Stock Concentration | Reaction Concentration |
| --------- | ------------------- | ---------------------- |
| tRNA      | 35 µg/µL (10×)      | 3.5 µg/µL              |
:::
::::

::::{tab-item} Final Reaction
PMix is added at 1.2 µL per 10 µL reaction, a 0.12× dilution from its stock: the 15 000 ng/µL total in the PMix tab becomes 1800 ng/µL, and each protein is at 0.12 times its PMix stock concentration. Protein molecular weights are those of the assembled complex (monomer weight × oligomeric state, as listed in the PMix tab), and molar concentrations are of that complex. See [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md) for the volumes of every component.

:::{table} Composition of Base Cytosol at reaction concentration.
:label: comp-base-cytosol

| Category | Molecule | Molecular Weight | Concentration (molar) | Concentration (mass) |
|----------|----------|------------------|-----------------------|----------------------|
| Buffers | HEPES-KOH | 238.3 g/mol | 50 mM | 11.9 µg/µL |
| | Potassium Glutamate | 203.23 g/mol | 100 mM | 20.3 µg/µL |
| | Magnesium Acetate | 214.45 g/mol | 7.5 mM | 1.61 µg/µL |
| Nucleotides | rATP |  | 2 mM |  |
| | rGTP | | 2 mM | |
| | rCTP | | 1 mM | |
| | rUTP | | 1 mM | |
| Amino Acids | Alanine (Ala) | 89.1 g/mol | 0.3 mM | 26.7 ng/µL |
| | Arginine (Arg) | 210.66 g/mol | 0.3 mM | 63.2 ng/µL |
| | Asparagine (Asn) | 132.1 g/mol | 0.3 mM | 39.6 ng/µL |
| | Aspartic Acid (Asp) | 133.1 g/mol | 0.3 mM | 39.9 ng/µL |
| | Cysteine (Cys) | 157.62 g/mol | 0.3 mM | 47.3 ng/µL |
| | Glutamic Acid (Glu) | 147.1 g/mol | 0.3 mM | 44.1 ng/µL |
| | Glutamine (Gln) | 146.2 g/mol | 0.3 mM | 43.9 ng/µL |
| | Glycine (Gly) | 75.1 g/mol | 0.3 mM | 22.5 ng/µL |
| | Histidine (His) | 209.63 g/mol | 0.3 mM | 62.9 ng/µL |
| | Isoleucine (Ile) | 131.2 g/mol | 0.3 mM | 39.4 ng/µL |
| | Leucine (Leu) | 131.2 g/mol | 0.3 mM | 39.4 ng/µL |
| | Lysine (Lys) | 182.65 g/mol | 0.3 mM | 54.8 ng/µL |
| | Methionine (Met) | 149.2 g/mol | 0.3 mM | 44.8 ng/µL |
| | Phenylalanine (Phe) | 165.2 g/mol | 0.3 mM | 49.6 ng/µL |
| | Proline (Pro) | 115.1 g/mol | 0.3 mM | 34.5 ng/µL |
| | Serine (Ser) | 105.1 g/mol | 0.3 mM | 31.5 ng/µL |
| | Threonine (Thr) | 119.1 g/mol | 0.3 mM | 35.7 ng/µL |
| | Tryptophan (Trp) | 204.2 g/mol | 0.3 mM | 61.3 ng/µL |
| | Tyrosine (Tyr) | 181.2 g/mol | 0.3 mM | 54.4 ng/µL |
| | Valine (Val) | 117.1 g/mol | 0.3 mM | 35.1 ng/µL |
| Stabilizers | Spermidine | 145.25 g/mol | 2 mM | 290 ng/µL |
| | TCEP-HCl | 286.65 g/mol | 1 mM | 287 ng/µL |
| Cofactors | Creatine Phosphate | 327.14 g/mol | 20 mM | 6.54 µg/µL |
| | Folinic Acid | 511.5 g/mol | 0.02 mM | 10.2 ng/µL |
| Ribonucleics | tRNA |  |  | 3.5 µg/µL |
| | Ribosomes | ~2.7 MDa | 1.8 µM | 4.9 µg/µL |
| tRNA Synthetases | AlaRS | 384.0 kDa | 0.340 µM | 130.3 ng/µL |
| | ArgRS | 64.7 kDa | 0.0557 µM | 3.6 ng/µL |
| | AsnRS | 105.2 kDa | 0.389 µM | 40.9 ng/µL |
| | AspRS | 131.8 kDa | 0.114 µM | 15.0 ng/µL |
| | CysRS | 52.2 kDa | 0.0414 µM | 2.2 ng/µL |
| | GlnRS | 63.5 kDa | 0.111 µM | 7.0 ng/µL |
| | GluRS | 53.8 kDa | 0.437 µM | 23.5 ng/µL |
| | GlyRS | 223.2 kDa | 0.0802 µM | 17.9 ng/µL |
| | HisRS | 94.0 kDa | 0.0154 µM | 1.5 ng/µL |
| | IleRS | 104.4 kDa | 0.715 µM | 74.6 ng/µL |
| | LeuRS | 97.2 kDa | 0.0778 µM | 7.5 ng/µL |
| | LysRS | 115.2 kDa | 0.103 µM | 11.9 ng/µL |
| | MetRS | 152.6 kDa | 0.0283 µM | 4.4 ng/µL |
| | PheRS | 248.4 kDa | 0.127 µM | 31.7 ng/µL |
| | ProRS | 127.4 kDa | 0.146 µM | 18.7 ng/µL |
| | SerRS | 96.8 kDa | 0.0372 µM | 3.6 ng/µL |
| | ThrRS | 148.0 kDa | 0.0786 µM | 11.6 ng/µL |
| | TrpRS | 74.8 kDa | 0.156 µM | 11.6 ng/µL |
| | TyrRS | 95.0 kDa | 0.0126 µM | 1.2 ng/µL |
| | ValRS | 108.2 kDa | 0.0311 µM | 3.4 ng/µL |
| Initiation Factors | IF1 | 8.2 kDa | 2.27 µM | 18.7 ng/µL |
| | IF2 | 97.3 kDa | 0.767 µM | 74.6 ng/µL |
| | IF3 | 20.6 kDa | 0.902 µM | 18.7 ng/µL |
| Elongation Factors | EF-G | 77.6 kDa | 1.2 µM | 93.3 ng/µL |
| | EF-Tu | 43.3 kDa | 21.5 µM | 931.7 ng/µL |
| | EF-Ts | 30.4 kDa | 3.07 µM | 93.3 ng/µL |
| Release Factors | RF1 | 40.5 kDa | 0.46 µM | 18.7 ng/µL |
| | RF2 | 41.3 kDa | 0.45 µM | 18.7 ng/µL |
| | RF3 | 59.6 kDa | 0.312 µM | 18.7 ng/µL |
| | RRF | 20.6 kDa | 0.902 µM | 18.7 ng/µL |
| Metabolism | MTF | 34.2 kDa | 1.09 µM | 37.3 ng/µL |
| | CK | 86.6 kDa | 0.0872 µM | 7.5 ng/µL |
| | AK | 23.6 kDa | 0.234 µM | 5.6 ng/µL |
| | NDK | 93.0 kDa | 0.0206 µM | 1.9 ng/µL |
| | PPiase | 118.2 kDa | 0.0162 µM | 1.9 ng/µL |
| Transcription | T7RNAP | 98.9 kDa | 0.188 µM | 18.7 ng/µL |
:::

@Editor: confirm the RNase inhibitor stock concentration. `Base Cell` and `Reporter: deGFP` give 40 000 U/mL, which makes 0.5 µL in 10 µL equal to 2000 U/mL; no Make page or bill of materials states it.
::::

:::::

# Expected Behavior

The behavior of Base Cytosol is characterized using the [Reporter: deGFP](../reporter-degfp/spec.md) Module.

@Editor: State the validation data for Base Cytosol. Tracked in [nucleus-eng/nucleus-docs#306](https://github.com/nucleus-eng/nucleus-docs/issues/306).

# Processes

- [Make Protein Mix](../../processes/make-36pot/main.md): makes PMix, the 36 purified PURE proteins at set molar ratios.
- [Make OnePot Protein Mix](../../processes/make-1pot/main.md): makes OnePot Protein Mix, which has the same proteins as PMix but at molar ratios that cannot be controlled. It is a functional equivalent of PMix, with less control.
- [Make Small Molecule Mix](../../processes/make-small-molecule-mix/main.md): makes SMix.
- [Make Amino Acid Mix](../../processes/make-amino-acid-mix/main.md): makes the equimolar mix of the 20 canonical amino acids that SMix uses.
- [Make Ribosomes](../../processes/make-ribosomes/main.md): makes the ribosomes.
- [Make tRNAs](../../processes/make-trna/main.md): makes the tRNA.
- [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md): combines the mixes into the reaction.

# Credits

Reformulated by Yemo Ku and Jon Calles (b.next) from the PURE system, developed by the Ueda Lab ([Shimizu et al., 2001](https://doi.org/10.1038/90802)).

