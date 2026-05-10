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
| | Magnesium Acetate | 8 | mM |
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
| | ArgRS | 130.3 | ng/μL |
| | AsnRS | 3.6 | ng/μL |
| | AspRS | 40.9 | ng/μL |
| | CysRS | 2.2 | ng/μL |
| | GlnRS | 7.0 | ng/μL |
| | GluRS | 23.5 | ng/μL |
| | GlyRS | 17.9 | ng/μL |
| | HisRS | 1.5 | ng/μL |
| | IleRS | 74.6 | ng/μL |
| | LeuRS | 7.5 | ng/μL |
| | LysRS | 11.9 | ng/μL |
| | MetRS | 4.4 | ng/μL |
| | PheRS | 31.7 | ng/μL |
| | ProRS | 18.7 | ng/μL |
| | SerRS | 3.6 | ng/μL |
| | ThrRS | 11.6 | ng/μL |
| | TrpRS | 11.6 | ng/μL |
| | TyrRS | 1.2 | ng/μL |
| | ValRS | 3.4 | ng/μL |
| Initiation Factors | IF1 | 18.7 | ng/μL |
| | IF2 | 74.6 | ng/μL |
| | IF3 | 18.7 | ng/μL |
| Elongation Factors | EF-G | 93.3 | ng/μL |
| | EF-Tu | 932 | ng/μL |
| | EF-Ts | 93.3 | ng/μL |
| Release Factors | RF1 | 18.7 | ng/μL |
| | RF2 | 18.7 ng/μL |
| | RF3 | 18.7 ng/μL |
| | RRF | 18.7 ng/μL |
| Metabolism | MTF | 37.3 | ng/μL |
| | CK | 7.5 | ng/μL |
| | AK | 5.6 | ng/μL |
| | NDK | 1.9 | ng/μL |
| | PPiase | 1.9 | ng/μL |
| Transcription | T7RNAP | 18.7 | ng/μL |

:::

## Expected Behavior

The behavior of Base Cytosol is characterized using the [deGFP Reporter](../reporter-degfp/spec.md) Module. 

## Protocols

Protocols for assembling Base Cytosol and making its components from scratch can be found on [Base Cytosol Processes](../../processes/processes-main.md#base-cytosol-processes).