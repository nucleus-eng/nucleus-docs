---
title: "Small Molecule Mix (SMix)"
subtitle: "Module Specification"
status: validated-published
site:
    hide-toc: true
    numbered_references: false
---

(smix-overview)=
# Overview

Small Molecule Mix (SMix) contains the 31 small molecules of Base Cytosol: buffers and salts, the four rNTPs, the 20 canonical amino acids, stabilizers, and cofactors. With [Protein Mix (PMix)](../pmix/spec.md), ribosomes, and tRNA, it makes [Base Cytosol](../base-cytosol/spec.md).

(smix-reference-composition)=
# Reference Composition

:::{table} Composition of the Small Molecule Mix (SMix) at 3.33× concentration. Magnesium acetate is 25 mM here, which contributes 7.5 mM to the reaction.
:label: comp-smix

| Category    | Molecule            | Concentration | Units |
| ----------- | ------------------- | ------------- | ----- |
| Buffers     | HEPES-KOH (pH 7.6)  | 166.67        | mM    |
|             | Potassium Glutamate | 333.33        | mM    |
|             | Magnesium Acetate   | 25            | mM    |
| Nucleotides | rATP                | 6.67          | mM    |
|             | rGTP                | 6.67          | mM    |
|             | rCTP                | 3.33          | mM    |
|             | rUTP                | 3.33          | mM    |
| Amino Acids | Each (Ala–Val)      | 1.00          | mM    |
| Stabilizers | Spermidine          | 6.67          | mM    |
|             | TCEP-HCl            | 3.33          | mM    |
| Cofactors   | Creatine Phosphate  | 66.67         | mM    |
|             | Folinic Acid        | 0.067         | mM    |
:::

(smix-processes)=
# Processes

- [Make Amino Acid Mix](../../processes/make-amino-acid-mix/main.md) — the equimolar amino acid stock that SMix takes
- [Make Small Molecule Mix](../../processes/make-small-molecule-mix/main.md)
- [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md)

(smix-credits)=
# Credits

Reformulated by Yemo Ku and Jon Calles (b.next) from the PURE system, developed by the Ueda Lab ([Shimizu et al., 2001](https://doi.org/10.1038/90802)).
