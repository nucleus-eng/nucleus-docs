---
title: "Base Cytosol"
subtitle: "Module Specification"
site:
    hide-toc: true
    numbered_references: false
---

# Overview

A molecular system with a defined set of components including T7 RNA Polymerase, ribosomes, and tRNA capable of transcription and translation. Base Cytosol builds on the [PURE system](https://doi.org/10.1038/90802), and is optimized for integration and extension. The Base Cell is formed by encapsulating Base Cytosol in a liposome.

Plasmid designs for the PURE proteins are maintained as pET28a expression vectors in the [DNA Distribution](https://github.com/nucleus-eng/DNA/tree/main/PURE/expression) repository.

:::{figure} schematic.png
:width: 100%
:align: center

Schematic of components in Cytosol and their function. Figure by [Ganesh and Maerkl, 2024](https://doi.org/10.1101/2024.04.03.587879) used under CC-BY-4.0 / cropped from original with numerical annotations removed.
:::

## Reference Composition

Base Cytosol is assembled from four components — a protein mix (PMix), a small molecule mix (SMix), ribosomes, and tRNA. The tabs below give the composition of each component at its **stock** concentration, plus the **Final Reaction** composition with every component at its in-reaction concentration.

:::::{tab-set}

::::{tab-item} PMix
The Protein Mix (PMix) contains all 36 PURE proteins at a total stock concentration of 15 µg/µL. Per-protein stock concentrations are shown below; see the [Make PMix](../../processes/make-36pot/main.md) and [Make OnePot Protein Mix](../../processes/make-1pot/main.md) processes for preparation.

:::{table} Composition of the Protein Mix (PMix) at stock concentration. Source: make-36pot process.
:label: comp-pmix
| Category | Protein | Concentration (ng/µL) |
|----------|---------|-----------------------|
| tRNA Synthetases | AlaRS | 1086 |
| | ArgRS | 30 |
| | AsnRS | 341 |
| | AspRS | 125 |
| | CysRS | 18 |
| | GlnRS | 59 |
| | GluRS | 196 |
| | GlyRS | 149 |
| | HisRS | 12 |
| | IleRS | 622 |
| | LeuRS | 63 |
| | LysRS | 99 |
| | MetRS | 36 |
| | PheRS | 264 |
| | ProRS | 155 |
| | SerRS | 30 |
| | ThrRS | 97 |
| | TrpRS | 97 |
| | TyrRS | 10 |
| | ValRS | 28 |
| Initiation Factors | IF1 | 155 |
| | IF2 | 622 |
| | IF3 | 155 |
| Elongation Factors | EF-G | 777 |
| | EF-Tu | 7764 |
| | EF-Ts | 777 |
| Release Factors | RF1 | 155 |
| | RF2 | 155 |
| | RF3 | 155 |
| | RRF | 155 |
| Metabolism | MTF | 311 |
| | CK | 63 |
| | AK | 46 |
| | NDK | 16 |
| | PPiase | 16 |
| Transcription | T7RNAP | 155 |
| **Total** | | **15 000** |
:::
::::

::::{tab-item} SMix
The Small Molecule Mix (SMix) contains the buffers, nucleotides, amino acids, stabilizers, and cofactors. Concentrations below are in the assembled SMix; see the [Make SMix](../../processes/make-small-molecule-mix/main.md) process for preparation.

:::{table} Composition of the Small Molecule Mix (SMix) at stock concentration. Source: make-small-molecule-mix process.
:label: comp-smix
| Category | Molecule | Concentration | Units |
|----------|----------|---------------|-------|
| Buffers | HEPES-KOH (pH 7.6) | 125 | mM |
| | Potassium Glutamate | 250 | mM |
| | Magnesium Acetate | 18.75 | mM |
| Nucleotides | rATP | 5 | mM |
| | rGTP | 5 | mM |
| | rCTP | 2.5 | mM |
| | rUTP | 2.5 | mM |
| Amino Acids | Each (Ala–Val) | 0.75 | mM |
| Stabilizers | Spermidine | 5 | mM |
| | TCEP | 2.5 | mM |
| Cofactors | Creatine Phosphate | 50 | mM |
| | Folinic Acid | 0.05 | mM |
:::
::::

::::{tab-item} Ribosomes
:::{table} Ribosome stock concentration. Source: [Make Ribosomes](../../processes/make-ribosomes/main.md) process.
:label: comp-ribosomes
| Component | Stock Concentration | Reaction Concentration |
|-----------|---------------------|------------------------|
| Ribosomes | 10 µM (5.55×) | 1.8 µM |
:::
::::

::::{tab-item} tRNA
:::{table} tRNA stock concentration. Source: [Make tRNAs](../../processes/make-trna/main.md) process.
:label: comp-trna
| Component | Stock Concentration | Reaction Concentration |
|-----------|---------------------|------------------------|
| tRNA | 35 µg/µL (10×) | 3.5 µg/µL |
:::
::::

::::{tab-item} Final Reaction
:::{table} Composition of Base Cytosol at reaction concentration.
:label: comp-base-cytosol
| Category | Molecule | Concentration | Units |
|----------|----------|----------------------|-------|
| Buffers | HEPES-KOH | 50 | mM |
| | Potassium Glutamate | 100 | mM |
| | Magnesium Acetate | 7.5 | mM |
| Nucleotides | rATP | 2 | mM |
| | rGTP | 2 | mM |
| | rCTP | 1 | mM |
| | rUTP | 1 | mM |
| Amino Acids  | Alanine (Ala) | 0.3 | mM |
| | Arginine (Arg) | 0.3 | mM |
| | Asparagine (Asn) | 0.3 | mM |
| | Aspartic Acid (Asp) | 0.3 | mM |
| | Cysteine (Cys) | 0.3 | mM |
| | Glutamic Acid (Glu) | 0.3 | mM |
| | Glutamine (Gln) | 0.3 | mM |
| | Glycine (Gly) | 0.3 | mM |
| | Histidine (His) | 0.3 | mM |
| | Isoleucine (Ile) | 0.3 | mM |
| | Leucine (Leu) | 0.3 | mM |
| | Lysine (Lys) | 0.3 | mM |
| | Methionine (Met) | 0.3 | mM |
| | Phenylalanine (Phe) | 0.3 | mM |
| | Proline (Pro) | 0.3 | mM |
| | Serine (Ser) | 0.3 | mM |
| | Threonine (Thr) | 0.3 | mM |
| | Tryptophan (Trp) | 0.3 | mM |
| | Tyrosine (Tyr) | 0.3 | mM |
| | Valine (Val) | 0.3 | mM |
| Stabilizers | Spermidine | 2 | mM |
| | TCEP-HCl | 1 | mM |
| Cofactors | Creatine Phosphate | 20 | mM |
| | Folinic Acid | 0.02 | mM |
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
:::
::::

:::::

## Expected Behavior

The behavior of Base Cytosol is characterized using the [deGFP Reporter](../reporter-degfp/spec.md) Module. 

## Protocols

Protocols for assembling Base Cytosol and making its components from scratch can be found on [Base Cytosol Processes](../../processes/processes-main.md#base-cytosol-processes).
