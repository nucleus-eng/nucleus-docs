---
title: "Reporter: deGFP"
subtitle: "Module Specification"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The deGFP Reporter Module produces deGFP, a green fluorescent protein.

:::{figure} schematic.png
:width: 40%
:align: center

A schematic representation of PURE converting template DNA into a fluorescent reporter.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA
:::{table}
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pOpen-deGFP` | 2812 | [pOpen-deGFP.gbk](https://github.com/nucleus-eng/DNA/blob/main/reporters/pOpen-deGFP.gbk) |
:::
::::

::::{tab-item} Cytosol

:::{table} This composition was evaluated in this [DevNote ](https://doi.org/10.63765/fppr8928)
![](xref:devnote-01#rc)
:::

::::

::::{tab-item} Cell

**Inner solution**

:::{table}
:label: comp-degfp-cell-inner

| Component | Input concentration | Unit | Final concentration | Unit | Volume for one reaction (µL) |
| --- | --- | --- | --- | --- | --- |
| SMix | 3.33 | × | 1 | × | 12 |
| PMix | 15 | mg/mL | 1.80 | mg/mL | 4.8 |
| Ribosomes | 10 | µM | 1.8 | µM | 7.2 |
| `pOpen-deGFP` DNA | 124 | nM | 3 | nM | 0.95 |
| tRNA | 35 | mg/ml | 3.5 | mg/ml | 4 |
| Magnesium acetate | 200 | mM | 8 | mM | 1.6 |
| Optiprep | 1.32 | mg/µL | 0.043 | mg/µL | 1.33 |
| RNase Inhibitor | 40000 | U/mL | 2000 | U/mL | 2 |
| Water |  |  |  |  | 6.12 |
| Total volume (µL) |  |  |  |  | 40 |
:::

**Membrane**

:::{table}
:label: comp-degfp-cell-membrane

| Component    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 70                    | 760.076                  | 25                          | 162.17             |
| Cholesterol  | 29.95                 | 386.654                  | 50                          | 17.65              |
| Liss-Rhod PE | 0.05                  | 1301.71                  | 1                           | 4.96               |

:::

**Outer solution**

:::{table}
:label: comp-degfp-cell-outer

| Component | Concentration |
| --- | --- |
| Glucose | 850 mM |
:::

::::

:::::

# Expected Behavior

## Cytosols

<!-- :::::{tab-set}
::::{tab-item} Kinetics
:::{figure}
![](xref:devnote-01#fig:kinetics-exp1)
:::
::::

::::{tab-item} Endpoint
:::{figure}
![](xref:devnote-01#fig:endpoint-exp1)
:::
::::
::::: -->

:::::{tab-set}
::::{tab-item} Kinetics
:::{figure} cytosol-kinetics.png
Translation kinetics of Cytosol and PURExpress reactions using two different pOpen-deGFP DNA preps. Cytosol w/o DNA refers to the Cytosol reaction lacking the pOpen-deGFP template. Data in [DevNote](https://doi.org/10.63765/fppr8928).
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-endpoint.png
Final protein yields of the reactions measured at steady state. Data from [DevNote](https://doi.org/10.63765/fppr8928).
:::
::::
:::::

## Cells

:::::{tab-set}
::::{tab-item} Image 1
:::{figure} cell-image1.png
Combined green (488 nm) and red (561 nm) fluorescence channels. Timepoint 0 (t = 0) corresponds to 30 min after preparation of the inner solution, reflecting the time required to prepare liposomes.
:::
::::

::::{tab-item} Image 2
:::{figure} cell-image2.png
Combined green (488 nm) and red (561 nm) fluorescence channels. Timepoint 0 (t = 0) corresponds to 30 min after preparation of the inner solution, reflecting the time required to prepare liposomes.
:::
::::
:::::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Step-by-Step Cytosol Protocol**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <module-protocol-cytosol-degfp.pdf>`
:::

:::{card}
:header: **Cytosol Materials**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <module-bom-reporter-degfp.pdf>`
:::

:::{card}
:header: **Step-by-Step Cell Protocol**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <module-protocol-cells-degfp.pdf>`
:::

:::{card}
:header: **Cell Materials**
:footer: *Implemented using Nucleus Cytosol*
{button}`Download <module-bom-reporter-cells-degfp.pdf>`
:::

::::

# Credits

Developed by Surendra Yadav (b.next).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
