---
title: "Base Cell"
subtitle: "Module Specification"
status: validated-published
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Base Cell is [Base Cytosol](../base-cytosol/spec.md) encapsulated in [Base Membrane](../membrane-popc-chol/spec.md) via [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md). The Base Cell is deployed in a glucose outer solution and represents the default synthetic cell for the Nucleus distribution. Base Cells have red fluorescent membranes and express GFP over time if functioning correctly.

## Reference Composition

:::::{tab-set}

::::{tab-item} Cytosol

The inner solution encapsulated into the Base Cell is [Base Cytosol](../base-cytosol/spec.md) at reaction concentration, with `pOpen-deGFP` DNA added as a reporter.

:::{table}
:label: comp-cytosol

| Component         | Input concentration | Final concentration | Volume for one reaction (µL) |
| ----------------- | ------------------- | ------------------- | ---------------------------- |
| SMix              | 3.33x               | 1x                  | 12                           |
| PMix              | 15 mg/mL            | 1.80 mg/mL          | 4.8                          |
| Ribosomes         | 10 µM               | 1.8 µM              | 7.2                          |
| `pOpen-deGFP` DNA | 124 nM              | 3 nM                | 0.95                         |
| tRNA              | 35 mg/mL            | 3.5 mg/ml           | 4                            |
| Optiprep          | 1.32 mg/µL          | 0.043 mg/µL         | 1.33                         |
| RNase Inhibitor   | 40 000 U/mL         | 2000 U/mL           | 2                            |
| Water             |                     |                     | 6.12                         |
| Total volume (µL) |                     |                     | 40                           |
:::

::::

::::{tab-item} Membrane

:::{table}

| Component    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 70                    | 760.076                  | 25                          | 162.17             |
| Cholesterol  | 29.95                 | 386.654                  | 50                          | 17.65              |
| Liss-Rhod PE | 0.05                  | 1301.71                  | 1                           | 4.96               |

:::

See [Base Membrane](../membrane-popc-chol/spec.md) for the full membrane spec.

::::

::::{tab-item} Outer Solution

:::{table}

| Component | Concentration |
| --------- | ------------- |
| Glucose   | 850 mM        |
:::

::::

:::::

## Expected Behavior

Base Cells express deGFP over time, starting dark and increasing in green fluorescence as translation proceeds. Kinetics data are reported in [DevNote bnext-devnotes-base-cell-01](https://devnotes.nucleus.engineering/articles/bnext-devnotes-base-cell-01).

## Process

Base Cells are assembled and encapsulated using [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).
