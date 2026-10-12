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
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    BASE_CELL["Base Cell"]
    BASE_CYTOSOL["Base Cytosol"]
    MEMBRANE_POPC_CHOL["Base Membrane: POPC/Chol"]

    BASE_CYTOSOL --> BASE_CELL
    MEMBRANE_POPC_CHOL --> BASE_CELL

    classDef constituent fill:#6B7280,color:#ffffff,stroke:#4B5563;
    classDef this fill:#374151,color:#ffffff,stroke:#111827;
    class BASE_CYTOSOL,MEMBRANE_POPC_CHOL constituent;
    class BASE_CELL this;

    click BASE_CELL "/docs/modules/base-cell/spec"
    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click MEMBRANE_POPC_CHOL "/docs/modules/membrane-popc-chol/spec"
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
| Optiprep          | 1.32 mg/µL          | 0.044 mg/µL         | 1.33                         |
| Template DNA (optional), e.g. `pOpen-deGFP` | 124 nM | 3 nM     | X, e.g. 0.95                 |
| Water             |                     |                     | 8.67 − X                     |
| Total volume (µL) |                     |                     | 40                           |
:::

::::

::::{tab-item} Membrane

:::{table}

| Component    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 69.93                 | 760.076                  | 25                          | 162.01             |
| Cholesterol  | 29.97                 | 386.654                  | 50                          | 17.66              |
| Liss-Rhod PE | 0.1                   | 1301.71                  | 1                           | 9.92               |

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

