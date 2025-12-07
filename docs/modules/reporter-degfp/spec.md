---
title: "Module Specification"
subtitle: "Reporter: deGFP"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The deGFP Reporter Module produced deGFP, a green fluorescent protein.

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} schematic.png
:width: 40%
:align: center

A schematic representation of PURE converting template DNA into a fluorescent reporter.
:::
::::

::::{tab-item} Designs
:::{table}
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pOpen-pT7-deGFP` | 2500 | [path-to-design-01.gb](https://github.com/bnext-bio/nucleus/blob/main/components/modules/detector/lacI.gb#L56-L66) |
:::
::::
:::::

## Cytosols

### Reference Composition

:::{table} This composition was evaluated in the DevNote by [](https://doi.org/10.63765/fppr8928)
![](xref:devnote-01#rc)
:::

### Expected Behavior

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
Translation kinetics of Cytosol and PURExpress reactions using two different pOpen-deGFP DNA preps. Cytosol w/o DNA refers to the Cytosol reaction lacking the pOpen-deGFP template. Data from [](https://doi.org/10.63765/fppr8928).
:::
::::

::::{tab-item} Endpoint
:::{figure} cytosol-endpoint.png
Final protein yields of the reactions measured at steady state. Data from [](https://doi.org/10.63765/fppr8928).
:::
::::
:::::


### Protocols

::::{grid} 1 1 1 2

:::{card}
:header: **Step-by-Step Protocol**
:footer: *Implemented using Nucleus Cytosol v0.5*
{button}`Download <module-protocol-cytosol-degfp.pdf>`
:::

:::{card}
:header: **Materials**
:footer: *Implemented using Nucleus Cytosol v0.5*
{button}`Download <module-bom-reporter-degfp.pdf>`
:::

::::

## Cells

### Reference Composition

Coming soon!

### Expected Behavior

Coming soon!

### Protocols

::::{grid} 1 1 1 2

:::{card}
:header: **Step-by-Step Protocol**
:footer: *Implemented using Nucleus Cytosol v0.5*
{button}`Download <module-protocol-cells-degfp.pdf>`
:::

:::{card}
:header: **Materials**
:footer: *Implemented using Nucleus Cytosol v0.5*
{button}`Download <module-bom-reporter-cells-degfp.pdf>`
:::

::::



<!-- ### Compatible processes

My reference table (this is on same page): {ref}`spec01:tbl-36pot-formulation`
My reference table (this is on different page): [ref](xref#this-tbl-36pot-formulation)

::::{aside}
:::{dropdown} TODO

For GFP the distinction between process and instances feels overwrought or at least hard to distinguish
:::
::::

- [b.next PURE](./docs/02-collections/cytosols.md)
- [OnePot PURE]()

::::{dropdown} [36Pot PURE]()

**Formulation**. This module can be implemented in [my-process] by implementing the following formulation in the base process. TODO: can I reference a table from another page? [my rerefence](#this-tbl-36pot-formulation)


:::{table}
:name: spec01:tbl-36pot-formulation

| Component | Experiment (uL) |
| --- | --- |
| NEB Sol B -Ribos |  |
| Workshop Protein Mix( ___ ug/uL) | 3 |
| NEB Ribosomes | 4.5 |
| NEB Sol A | 10 |
| NEB Sol B |  |
| RNse Inhibitor | 1.25 |
| pT7-my-custom-plasmid (120 ng/uL) | 1.25 |
| Ultrapure water | 5 |
| **Total** | **25** |
:::

**Process** The following steps should be REMOVED, ADDED, or MODIFIED to implement the Module in the Process. 

- ADD. Preparation of PPK stock solution

::::

### Usage

**Collections**

- [Collection-1](/docs/collections/cytosols/instance-template/instance)

**DevNotes**

- [DevNote-3](https://doi.org/10.63765/djnv7772)

**Literature**

- [Wang *et al.* 2019](https://doi.org/10.1021/acssynbio.9b00456)

::::{aside}
:::{dropdown} TODO

I want to figure out how to hide the list of references from being auto generated at the bottom.
:::
:::: -->
