---
title: "Base Membrane: POPC/Chol"
subtitle: "Module Specification"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

(membrane-popc-chol-overview)=
# Overview

The Base Membrane specifies a phospholipid bilayer composed of POPC, cholesterol, and a fluorescent lipid label. Liss-Rhod PE or 18:1 Cy5-PC can serve as the label. The Base Membrane is the recommended default membrane for making synthetic cells by using [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).

:::{figure} schematic.png
:width: 50%
:align: center

Schematic of a POPC/Chol liposome.
:::

(membrane-popc-chol-reference-composition)=
# Reference Composition

:::{table}
:label: comp-membrane-popc-chol

| Component    | Target (mmol/mol)     | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 699.3                 | 760.076                  | 25                          | 162.01             |
| Cholesterol  | 299.7                 | 386.654                  | 50                          | 17.66              |
| Fluorescent lipid label | 1 | See the dye menu | See the dye menu | See the dye menu |

:::

:::{table} Dye menu. One dye fills the fluorescent lipid label row, at the same 1 mmol/mol.
:label: comp-membrane-popc-chol-dyes
:align: center

| Dye | Catalog | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| --- | --- | --- | --- | --- |
| Liss-Rhod PE | Avanti A81150 | 1301.71 | 1 | 9.92 |
| 18:1 Cy5-PC | Avanti A85483 | 1316.26 | 1 | 10.03 |
:::

:::{table} Recipes of the Base Membrane. The default is the first row.
:label: comp-membrane-popc-chol-recipes
:align: center

| Recipe | POPC (mmol/mol) | Cholesterol (mmol/mol) | Fluorescent lipid label (mmol/mol) | Used for |
| --- | --- | --- | --- | --- |
| Default | 699.3 | 299.7 | 1 | [Base Cell](../base-cell/spec.md) |
| 9:1 | 899.1 | 99.9 | 1 | GUVs by inverted emulsion transfer, with the [tetR-aTc Detector](../detector-tetr-atc/spec.md) |
| Pure POPC | 999 | 0 | 1 | Cells with the EsaR detector or the LuxR detector, including the LuxR demo |
:::

@Editor: link the Implementations that use the pure POPC recipe once their pages exist.

(membrane-popc-chol-expected-behavior)=
# Expected Behavior

(membrane-popc-chol-cells)=
## Cells

The Base Membrane Module is expected to hold an inner solution (the "cytosol") separate from an outer solution.

A recipe with a different cholesterol fraction is expected to differ in bilayer permeability.

@Editor: cite a source for the cholesterol and permeability claim.

(membrane-popc-chol-processes)=
# Processes

- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) — prepares synthetic cells by encapsulating an inner solution in a membrane.

(membrane-popc-chol-credits)=
# Credits

Developed by b.next, with dye menu and recipes from Mary Kelly (Chicago Node, Kamat Lab).

@Editor: name the authors of the membrane comparison DevNote, "London Exchange Meeting: Liposome Protocol Survey", which lists its authors only as "London Exchange Meeting Participants", or confirm it is not a source of the recipes.