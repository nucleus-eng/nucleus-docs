---
title: "Module Specification (Module Name)"
site:
    hide-toc: true
    numbered_references: false
---

## Overview

Mitochondria consectetur adipiscing phylum, sed do ribosomes tempor incididunt ut chlorophyll et dolore magna cytoplasm. Ut enim ad minim chromosome, quis nostrud photosynthesis ullamco laboris nisi ut enzyme aliquip ex ea commodo peptide. Duis aute nucleotide in reprehenderit in voluptate vesicle esse cillum genome fugiat nulla pariatur.

### Schematic

::::{aside}
:::{dropdown} TODO

What are good guidelines for a schematic representations of different modules?
:::
::::

:::{figure} schematic.png

This is a schematic of the module.
:::

### Designs

::::{aside}
:::{dropdown} TODO

What should belong in this table?
:::
::::

| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pOpen-pT7-ClpP-CHis` | 2500 | [path-to-design-01.gb](https://github.com/bnext-bio/nucleus/blob/main/components/modules/detector/lacI.gb#L56-L66) |
| `pOpen-pT7-ClpX-linker-CHis` | 1699 | path-to-design-01.gb |
| `pET28a-ClpP-CHis` | 3145 | path-to-design-01.gb |

### Compatible processes

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
::::
