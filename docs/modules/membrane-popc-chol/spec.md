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

# Supported by

[DevNotes](https://devnotes.nucleus.engineering) that support this specification include:

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} ClpXP Control Module: Deployment in PURE Cells
:link: https://devnotes.nucleus.engineering/articles/019b613d-4a47-7d62-a262-77a667467a57
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a08cd1-9199-7ac0-bacf-3ac935c46856/public/control-module-bcdff4929cf964ead1956fd124d8d9d9.webp)
:::

:::{card} Double emulsion optimization: inner solution, lipid concentration, and composition
:link: https://devnotes.nucleus.engineering/articles/019d64b1-f6b1-7d50-ba0d-7419f01c0141
:footer: Mary Kelly · Node: Chicago

![](https://pub.curvenote.com/01a08cd0-f69b-7910-8672-62565bc4a3cf/public/021026_Sucrose200_0T-a8401e73112bea5a69c71ef8b3d9d868.webp)
:::

:::{card} IV-HSL Emitter Cell
:link: https://devnotes.nucleus.engineering/articles/01945265-b728-7938-aab0-1ce134f4dffa
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a08cd1-0fa0-703d-902e-ade36c88739c/public/emitter-cell-schemat-41d2837d97b57df934b8bf6cbf9f0d3b.webp)
:::

:::{card} London Exchange Meeting: Liposome Protocol Survey
:link: https://devnotes.nucleus.engineering/articles/019de275-d95d-7773-8622-59c333b056a9
:footer: London Exchange Meeting Participants · Workshops and Courses

![](https://pub.curvenote.com/01a08bf0-438a-7f89-8da9-7e1682f18642/public/thumbnail-5e1ebd3aefe4386efbd2de0f12b74635.webp)
:::

:::{card} The Developer Cell Control Module: Protein Degradation by ClpXP
:link: https://devnotes.nucleus.engineering/articles/01981a5d-64c2-72f2-8055-5634d2824ede
:footer: Yen-Yu Hsu · Nucleus Core

![](https://pub.curvenote.com/01a08cd0-f496-7ee2-b08c-1c7e00240c3d/public/clpXP-85886080fd564ecd4e0aa3e9d696803a.webp)
:::

::::
