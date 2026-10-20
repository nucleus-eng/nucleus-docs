---
title: "Base Cytosol"
subtitle: "Module Specification"
status: validated-published
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Base Cytosol is a molecular system with a defined set of components, including T7 RNA Polymerase, ribosomes, and tRNA, capable of transcription and translation. It builds on the [PURE system](https://doi.org/10.1038/90802) and is optimized for integration and extension. The [Base Cell](../base-cell/spec.md) is formed by encapsulating Base Cytosol in a liposome.

Base Cytosol transcribes a DNA template that carries a T7 promoter, and no other promoter, because it supplies T7 RNA polymerase; a template without a T7 promoter is not transcribed. It translates the transcript into protein. It splits the pyrophosphate (PPi) that transcription and translation release into two phosphates, using inorganic pyrophosphatase. It returns spent nucleotides to their triphosphate form from creatine phosphate, using creatine kinase together with adenylate kinase and nucleoside diphosphate kinase.

Plasmid designs for the PURE proteins are maintained as pET28a expression vectors in the [DNA Distribution](https://github.com/nucleus-eng/DNA/tree/main/PURE/expression) repository.

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
:::{table} Composition of Base Cytosol at reaction concentration.
:label: comp-base-cytosol

| Category | Molecule | Concentration | Units |
|----------|----------|----------------------|-------|
| Buffers | HEPES-KOH | 37.5 | mM |
| | Potassium Glutamate | 75 | mM |
| | Magnesium Acetate | 5.6 | mM |
| Nucleotides | rATP | 1.5 | mM |
| | rGTP | 1.5 | mM |
| | rCTP | 0.75 | mM |
| | rUTP | 0.75 | mM |
| Amino Acids  | Alanine (Ala) | 0.225 | mM |
| | Arginine (Arg) | 0.225 | mM |
| | Asparagine (Asn) | 0.225 | mM |
| | Aspartic Acid (Asp) | 0.225 | mM |
| | Cysteine (Cys) | 0.225 | mM |
| | Glutamic Acid (Glu) | 0.225 | mM |
| | Glutamine (Gln) | 0.225 | mM |
| | Glycine (Gly) | 0.225 | mM |
| | Histidine (His) | 0.225 | mM |
| | Isoleucine (Ile) | 0.225 | mM |
| | Leucine (Leu) | 0.225 | mM |
| | Lysine (Lys) | 0.225 | mM |
| | Methionine (Met) | 0.225 | mM |
| | Phenylalanine (Phe) | 0.225 | mM |
| | Proline (Pro) | 0.225 | mM |
| | Serine (Ser) | 0.225 | mM |
| | Threonine (Thr) | 0.225 | mM |
| | Tryptophan (Trp) | 0.225 | mM |
| | Tyrosine (Tyr) | 0.225 | mM |
| | Valine (Val) | 0.225 | mM |
| Stabilizers | Spermidine | 1.5 | mM |
| | TCEP-HCl | 0.75 | mM |
| Cofactors | Creatine Phosphate | 15 | mM |
| | Folinic Acid | 0.015 | mM |
| Ribonucleics | tRNA | 3.5 | µg/µL |
| | Ribosomes | 1.8 | µM |
| tRNA Synthetases | AlaRS | 130.3 | ng/µL |
| | ArgRS | 3.6 | ng/µL |
| | AsnRS | 40.9 | ng/µL |
| | AspRS | 15.0 | ng/µL |
| | CysRS | 2.2 | ng/µL |
| | GlnRS | 7.0 | ng/µL |
| | GluRS | 23.5 | ng/µL |
| | GlyRS | 17.9 | ng/µL |
| | HisRS | 1.5 | ng/µL |
| | IleRS | 74.6 | ng/µL |
| | LeuRS | 7.5 | ng/µL |
| | LysRS | 11.9 | ng/µL |
| | MetRS | 4.4 | ng/µL |
| | PheRS | 31.7 | ng/µL |
| | ProRS | 18.7 | ng/µL |
| | SerRS | 3.6 | ng/µL |
| | ThrRS | 11.6 | ng/µL |
| | TrpRS | 11.6 | ng/µL |
| | TyrRS | 1.2 | ng/µL |
| | ValRS | 3.4 | ng/µL |
| Initiation Factors | IF1 | 18.7 | ng/µL |
| | IF2 | 74.6 | ng/µL |
| | IF3 | 18.7 | ng/µL |
| Elongation Factors | EF-G | 93.3 | ng/µL |
| | EF-Tu | 931.7 | ng/µL |
| | EF-Ts | 93.3 | ng/µL |
| Release Factors | RF1 | 18.7 | ng/µL |
| | RF2 | 18.7 | ng/µL |
| | RF3 | 18.7 | ng/µL |
| | RRF | 18.7 | ng/µL |
| Metabolism | MTF | 37.3 | ng/µL |
| | CK | 7.5 | ng/µL |
| | AK | 5.6 | ng/µL |
| | NDK | 1.9 | ng/µL |
| | PPiase | 1.9 | ng/µL |
| Transcription | T7RNAP | 18.7 | ng/µL |
| Inhibitors | RNase Inhibitor (optional) | 0 to 2000 | U/mL |
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

