---
title: "Base: Cytosol"
subtitle: "Module Specification"
site:
    hide-toc: true
    numbered_references: false
---

# Overview

A molecular system with a defined set of components including T7 RNA Polymerase, ribosomes, and tRNA capable of transcription and translation. Base Cytosol builds on the [PURE system](https://doi.org/10.1038/90802), and is optimized for integration and extension. The Base Cell is formed by encapsulating Base Cytosol in a liposome.  

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} schematic.png
:width: 100%
:align: center

Schematic of components in Cytosol and their function. Figure by [Ganesh, R. B. & Maerkl, S. J.](https://doi.org/10.1101/2024.04.03.587879) used under CC-BY-4.0 / cropped from original with numerical annotations removed.
:::
::::

::::{tab-item} Designs

Plasmid designs are included in the documentation of the [DNA Distribution](../../dna-distro.md).

::::
:::::

## Reference Composition

:::{table} Composition of Base Cytosol. 
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
| Ribonucleics | tRNA | 3.5 | μg/mL |
| | Ribosomes | 1.8 | μM |
| tRNA Synthetases | AlaRS | 139 | ng/μL |
| | ArgRS | 3.87 | ng/μL |
| | AsnRS | 43.7 | ng/μL |
| | AspRS | 16.0 | ng/μL |
| | CysRS | 2.32 | ng/μL |
| | GlnRS | 7.49 | ng/μL |
| | GluRS | 25.1 | ng/μL |
| | GlyRS | 19.1 | ng/μL |
| | HisRS | 1.55 | ng/μL |
| | IleRS | 79.6 | ng/μL |
| | LeuRS | 8.01 | ng/μL |
| | LysRS | 12.7 | ng/μL |
| | MetRS | 4.66 | ng/μL |
| | PheRS | 33.9 | ng/μL |
| | ProRS | 19.9 | ng/μL |
| | SerRS | 3.87 | ng/μL |
| | ThrRS | 12.4 | ng/μL |
| | TrpRS | 12.4 | ng/μL |
| | TyrRS | 1.29 | ng/μL |
| | ValRS | 3.62 | ng/μL |
| Initiation Factors | IF1 | 19.9 | ng/μL |
| | IF2 | 79.6 | ng/μL |
| | IF3 | 19.9 | ng/μL |
| Elongation Factors | EF-G | 99.5 | ng/μL |
| | EF-Tu | 994 | ng/μL |
| | EF-Ts | 99.5 | ng/μL |
| Release Factors | RF1 | 19.9 | ng/μL |
| | RF2 | 19.9 | ng/μL |
| | RF3 | 19.9 | ng/μL |
| | RRF | 19.9 | ng/μL |
| Metabolism | MTF | 39.8 | ng/μL |
| | CK | 8.01 | ng/μL |
| | MK | 5.94 | ng/μL |
| | NDK | 2.07 | ng/μL |
| | PPiase | 2.07 | ng/μL |
| Transcription | T7RNAP | 19.9 | ng/μL |

:::

## Expected Behavior

The behavior of Base Cytosol is characterized using the [deGFP Reporter](../reporter-degfp/spec.md) Module. 

## Protocols

Protocols for assembling Base Cytosol and making its components from scratch can be found on [Base Cytosol Processes](../../processes/processes-main.md#base-cytosol-processes).