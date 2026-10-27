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

Base Cytosol is assembled from five components — [Protein Mix (PMix)](../pmix/spec.md), [Small Molecule Mix (SMix)](../smix/spec.md), ribosomes, tRNA, and an optional RNase inhibitor. The tabs below give each component at its **stock** concentration, plus the **Final Reaction** composition with every component at its in-reaction concentration.

:::::{tab-set}

::::{tab-item} PMix
PMix contains all 36 PURE proteins.

:::{table} Protein Mix (PMix) stock concentration.
:label: comp-base-cytosol-pmix

| Component | Stock Concentration | Reaction Concentration |
| --------- | ------------------- | ---------------------- |
| [Protein Mix (PMix)](../pmix/spec.md) | 15 µg/µL (8.33×) | 1.8 µg/µL |
:::
::::

::::{tab-item} SMix
SMix contains the buffers, rNTPs, amino acids, stabilizers, and cofactors.

:::{table} Small Molecule Mix (SMix) stock concentration.
:label: comp-base-cytosol-smix

| Component | Stock Concentration | Reaction Concentration |
| --------- | ------------------- | ---------------------- |
| [Small Molecule Mix (SMix)](../smix/spec.md) | 3.33× | 1× |
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
PMix is added at 1.2 µL per 10 µL reaction, a 0.12× dilution from its stock: the 15 000 ng/µL total of [Protein Mix (PMix)](../pmix/spec.md) becomes 1800 ng/µL, and each protein is at 0.12 times its PMix stock concentration. Protein molecular weights are those of the assembled complex (monomer weight × oligomeric state, as listed for PMix), and molar concentrations are of that complex. See [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md) for the volumes of every component.

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

# Constituent Modules

- [Protein Mix (PMix)](../pmix/spec.md) — the 36 PURE proteins in Protein Buffer
- [Small Molecule Mix (SMix)](../smix/spec.md) — the buffers, rNTPs, amino acids, stabilizers, and cofactors

# Credits

Reformulated by Yemo Ku and Jon Calles (b.next) from the PURE system, developed by the Ueda Lab ([Shimizu et al., 2001](https://doi.org/10.1038/90802)).

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this specification include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} Characterizing the Limited Operational Lifetime of Cytosol Reactions
:link: https://devnotes.nucleus.engineering/articles/019ef6d5-3a27-787f-9ebd-fe80645b1068
:footer: Surendra Yadav · Nucleus Core

![](https://pub.curvenote.com/01a08cd1-0bda-777d-90ea-ef62ac077bf8/public/kinetics-normalized-8268e61917aa794a036d5761bad675cd.webp)
:::

:::{card} ClpXP Control Module: Deployment in Nucleus Cytosol
:link: https://devnotes.nucleus.engineering/articles/019f05cb-6be8-7189-8c0d-f8f51d170541
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a15336-ad4c-7145-b48c-b467190898c0/public/control-module-456a08ae6157de8014ea7b8b5895035f.webp)
:::

:::{card} DevCells: Kickoff Workshop
:link: https://devnotes.nucleus.engineering/articles/019b286c-a610-70b5-af71-648d569e650b
:footer: DevCells Kickoff Workshop · Workshops and Courses

![](https://pub.curvenote.com/019fd5ca-4c24-7770-b729-48979db36122/public/devcells-2b40a8a3f1dbd3889b2872ba14c99fb9.webp)
:::

:::{card} Developer Studio
:link: https://devnotes.nucleus.engineering/articles/01a0588e-dcf0-7ff3-b7d6-852cdac2734a
:footer: Developer Studio Workshop Participants · Workshops and Courses

![](https://pub.curvenote.com/01a10d00-b216-7d54-9a79-7163b3d8a2e5/public/thumbnail-7701ce0b0d15b06de49caf4609224388.webp)
:::

:::{card} Double Vesicle Lysis System Leveraging deGFP CFPE
:link: https://devnotes.nucleus.engineering/articles/01a16026-42c1-71ad-842a-463d52fae7d8
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-f37b-7cd9-ac05-7f491b920d6e/public/fig1-two-vesicle-kin-b2f2e21461dd910150fd25955247d4e8.webp)
:::

:::{card} First Nucleus Cytosol Testing
:link: https://devnotes.nucleus.engineering/articles/019a7511-0b68-702b-8909-0fe96ef8d5d2
:footer: Surendra Yadav · Nucleus Core

![](https://pub.curvenote.com/019fcdbd-d48a-7319-be07-15b772037c88/public/illustration2-63bd8a34b4a90292a066abf875d462eb.png)
:::

:::{card} Nucleus Base Cell Testing
:link: https://devnotes.nucleus.engineering/articles/019b13f9-1ec6-757c-b5ed-68cdd8e91fb0
:footer: Surendra Yadav · Nucleus Core

![](https://pub.curvenote.com/01a04676-8d9d-7f8f-96e1-2eefb52a607d/public/Image1-97e36bb3a38f167a4409ef588837c5fa.webp)
:::

:::{card} Quorum Sensing in Nucleus Cytosol using EsaO/EsaR Transcriptional Regulation
:link: https://devnotes.nucleus.engineering/articles/01a108c6-4719-7833-92af-daf6f91ed06a
:footer: Charlie Newell, Manuel Bibrowski, Jonah McDonald, Niall McIntyre, Julia Purrinos de Oliveira · DevStudio 2026

![](https://pub.curvenote.com/01a1650a-b201-7bf1-8f59-f37bce646feb/public/EsaR-sensing-6354ffdd322f6b6aca0909ed8f894e30.png)
:::

:::{card} Synthetic Cells Course Lab Manual: Cell-free Gene Expression and Liposome Encapsulation
:link: https://devnotes.nucleus.engineering/articles/019f7d1d-98b9-7fa0-a691-ea286ab8a96f
:footer: Maia Grace Lambson, Clara Lillie, Grace Nicole Montgomery, Sunayana Nguyen, Javin P Oza · Workshops and Courses

![](https://pub.curvenote.com/01a14b4a-c04a-7d1b-ace2-50afec134578/public/grace-0306-fluoresce-17622626d5e8d521e944e518fe250407.png)
:::

:::{card} TetO-Regulated PLA1 Sensor in Vesicles: aTc Titration and Spatial Patterning
:link: https://devnotes.nucleus.engineering/articles/01a1304b-1c56-7352-a082-ba84a2684f82
:footer: Mary Kelly, Madison Briggs · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-ebfe-71b5-b20a-66b33af95dfb/public/fig7-patterned-gel-5fc6273fa124c69e6d78ac4caafe3ce4.webp)
:::

:::{card} What is a Cytosol Landscape?
:link: https://devnotes.nucleus.engineering/articles/01a08c2d-2898-7f60-8f62-6bee069fddca
:footer: Sharon Newman · Nucleus Core

![](https://pub.curvenote.com/01a14c37-92c9-709e-91b5-af7303081a95/public/thumbnail-223faeab72d3f8699de21fbcfcf44279.webp)
:::

::::
