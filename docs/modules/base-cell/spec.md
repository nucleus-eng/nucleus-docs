---
title: "Base Cell"
subtitle: "Module Specification"
status: validated-published
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Base Cell is [Base Cytosol](../base-cytosol/spec.md) encapsulated in [Base Membrane](../membrane-popc-chol/spec.md) via [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md). The Base Cell is deployed in a glucose outer solution and represents the default synthetic cell for the Nucleus distribution. Base Cells have red fluorescent membranes (Liss-Rhod PE). With `pOpen-deGFP` as their template DNA, they express GFP over time if functioning correctly.

:::{figure} schematic.png
:width: 100%
:align: center

Overview of Base Cell, composed of [Base Cytosol](/docs/modules/base-cytosol/spec.md) encapsulated with [Base Membrane](/docs/modules/membrane-popc-chol/spec.md). Constitutive components of each module schematically depicted.
:::

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    OUTER_SOLUTION["Outer solution"]
    BASE_CYTOSOL["Base Cytosol"]
    MEMBRANE_POPC_CHOL["Base Membrane: POPC/Chol"]
    DENSITY_REAGENT["Density reagent"]

    P1_ASSEMBLE_INNER_SOLUTION_0(["Assemble Base Cytosol (mixing)"])
    BASE_CELL_INNER_SOLUTION["Base Cell inner solution"]
    P2_ENCAPSULATE_0(["Encapsulation: Phase Transfer (packing)"])
    BASE_CELL["Base Cell"]

    BASE_CYTOSOL --> P1_ASSEMBLE_INNER_SOLUTION_0
    DENSITY_REAGENT --> P1_ASSEMBLE_INNER_SOLUTION_0
    P1_ASSEMBLE_INNER_SOLUTION_0 --> BASE_CELL_INNER_SOLUTION

    BASE_CELL_INNER_SOLUTION --> P2_ENCAPSULATE_0
    MEMBRANE_POPC_CHOL --> P2_ENCAPSULATE_0
    OUTER_SOLUTION --> P2_ENCAPSULATE_0
    P2_ENCAPSULATE_0 --> BASE_CELL


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class OUTER_SOLUTION,BASE_CYTOSOL,MEMBRANE_POPC_CHOL,DENSITY_REAGENT leaf;
    class BASE_CELL_INNER_SOLUTION,BASE_CELL composed;
    class P1_ASSEMBLE_INNER_SOLUTION_0,P2_ENCAPSULATE_0 process;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click MEMBRANE_POPC_CHOL "/docs/modules/membrane-popc-chol/spec"
    click P1_ASSEMBLE_INNER_SOLUTION_0 "/docs/processes/assemble-base-cytosol/main"
    click P2_ENCAPSULATE_0 "/docs/processes/assemble-base-cell/main"
    click BASE_CELL "/docs/modules/base-cell/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Cytosol

The inner solution encapsulated into the Base Cell is [Base Cytosol](/docs/modules/base-cytosol/spec.md) at reaction concentration, with Optiprep for phase transfer. Template DNA is optional; the cell was validated with `pOpen-deGFP` DNA as a reporter.

:::{table}
:label: comp-cytosol

| Component         | Input concentration | Final concentration | Volume for one reaction (µL) |
| ----------------- | ------------------- | ------------------- | ---------------------------- |
| SMix              | 3.33x               | 1x                  | 12                           |
| PMix              | 15 mg/mL            | 1.80 mg/mL          | 4.8                          |
| Ribosomes         | 10 µM               | 1.8 µM              | 7.2                          |
| tRNA              | 35 mg/mL            | 3.5 mg/ml           | 4                            |
| RNase Inhibitor   | 40 000 U/mL         | 2000 U/mL           | 2                            |
| Optiprep          | 1.32 mg/µL          | 0.043 mg/µL         | 1.33                         |
| Template DNA (optional), e.g. `pOpen-deGFP` | 124 nM | 3 nM     | X, e.g. 0.95                 |
| Water             |                     |                     | 8.67 − X                     |
| Total volume (µL) |                     |                     | 40                           |
:::

::::

::::{tab-item} Membrane

:::{table}

| Component    | Target (mmol/mol)     | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 699.3                 | 760.076                  | 25                          | 162.01             |
| Cholesterol  | 299.7                 | 386.654                  | 50                          | 17.66              |
| Liss-Rhod PE | 1                     | 1301.71                  | 1                           | 9.92               |

:::

See [Base Membrane](../membrane-popc-chol/spec.md) for the full membrane spec.

::::

::::{tab-item} Outer Solution

:::{table}

| Component | Concentration |
| --------- | ------------- |
| Glucose   | 1140 mM, a starting recipe: adjust it until its osmotic concentration is 100 mOsm/kg to 150 mOsm/kg below the inner solution's |
:::

::::

:::::

# Expected Behavior

With `pOpen-deGFP` as their template DNA, Base Cells express deGFP over time, starting dark and increasing in green fluorescence as translation proceeds. Kinetics data are reported in [DevNote bnext-devnotes-base-cell-01](https://devnotes.nucleus.engineering/articles/bnext-devnotes-base-cell-01).

:::{figure} cell-image.png
:width: 100%
:align: center

Combined green (488 nm) and red (561 nm) fluorescence channels. First time point (labeled "t = 0") corresponds to 30 min after preparation of the inner solution, reflecting the time required to prepare liposomes.
:::

# Process

[Build a Base Cell](../../processes/build-base-cell/main.md) gives every step at the bench, in order, as one protocol. Base Cells are assembled and encapsulated using [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).

# Constituent Modules

- [Base Cytosol](../base-cytosol/spec.md) — inner solution, encapsulated at reaction concentration
- [Base Membrane](../membrane-popc-chol/spec.md) — 70:30 POPC:cholesterol bilayer

# Credits

Developed by Surendra Yadav (b.next).

# Supported by

DevNotes that reference this spec, not curated attribution; see Credits for that.

::::{grid} 1 1 1 1
:class: devnote-cards

:::{card} DevCells: Kickoff Workshop
:link: https://devnotes.nucleus.engineering/articles/019c3f08-25a7-752c-8821-cd4634bde800
:footer: DevCells Kickoff Workshop · Developer Cells

![](https://pub.curvenote.com/019c3f08-11b4-7285-9e08-de469c094495/public/devcells-b208c3b985734c1e5ca43f66e4b787dd.webp)
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

:::{card} Liposome encapsulation: A tractable and reproducible approach
:link: https://devnotes.nucleus.engineering/articles/019f7d5b-f635-7e77-b7fc-c2e7d8d09f8a
:footer: Chris Falcon, Katie Drew · Workshops and Courses

![](https://pub.curvenote.com/019fd5ca-1b63-72a0-8114-3da28983a0b5/public/fig1-timecourse-a4cbaed41b7f5c4852fa6e1e409b5180.webp)
:::

:::{card} Nucleus Base Cell Testing
:link: https://devnotes.nucleus.engineering/articles/019b13f9-1ec6-757c-b5ed-68cdd8e91fb0
:footer: Surendra Yadav · Nucleus Core

![](https://pub.curvenote.com/01a04676-8d9d-7f8f-96e1-2eefb52a607d/public/Image1-97e36bb3a38f167a4409ef588837c5fa.webp)
:::

:::{card} Understanding Liposome Behaviour in Hydrogel Matrices
:link: https://devnotes.nucleus.engineering/articles/01a10dfe-c1df-7c2d-ba5a-035280a349f7
:footer: Ojaswita Pant, Manuel Bibrowski · DevStudio 2026

![](https://pub.curvenote.com/01a1659b-f2a7-7372-93d6-8ea9f387f61d/public/schematic-hydrogel-o-d7d3affce66c5490e22c9a76d4696445.webp)
:::

::::
