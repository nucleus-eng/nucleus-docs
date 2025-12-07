---
title: Processes
---

# Overview

Processes represent the core protocols. They tell you how to transform physical materials into minimal cytosols and cells. Modules extend the functionality of these basic cytosols and cells. 

## Base Cytosol Processes

:::{figure} ./resources/flowchart-cytosols.png
:align: center
:label: fig:figure1
Flow chart for building Base Cytosol and its modification through the addition of Modules.
:::


### Modify Base Cytosol

- [Assemble Base Cytosol](./assemble-base-cytosol/main.md)
- [Energy: Base Cytosol + PPK]()

### Make Base Cytosol

The base cytosol module implements transcription and translation powered by creatine phosphate/creatine kinase energy (CP/CK) system.

- [Make Amino Acid Mix](./make-amino-acid-mix/process-make_amino_acid_mix.md)
- [Make Small Molecule Mix](./make-small-molecule-mix/process-make_small_molecule_mix.md)
- [Make tRNAs](./make-trna/process-make_trnas.md)
- [Make Ribosomes](./make-ribosomes/process-make_ribosomes.md)
- [Make PMix - 1 Pot]()
- [Make PMix - 36 Pot]()


### Quality Control Processes

- [Protein Gel]()
- [Pierce660 Assay]()
- [BCA Assay]()

## Base Cell Processes

:::::{tab-set}

::::{tab-item} Base Cell
:::{figure} ./resources/flowchart-cells-dye.png
:align: center
:label: fig:figure2
Flow chart for building Base Cell and its modification through the addition of Modules.
:::
::::

::::{tab-item} Base Cell + Cytosol
:::{figure} ./resources/flowchart-cells.png
:align: center
:label: fig:figure2
Flow chart for building Base Cell and its modification through the addition of Modules.
:::
::::

:::::



- [Reporter: Base Cell + deGFP](./assemble-base-cell/process-make_base_cell.md)
- []

### Modify Base Cell

### Make Base Cell


<!-- # Overview

Processes convert Modules into something useful. A Process often coincides with the simplest possible Implementation, typyically using the plamGFP Reporter Module. For this reason, we often refer to these as ["Hello, World!"](https://en.wikipedia.org/wiki/%22Hello,_World!%22_program) implementations. Alternatively, a process will include a quality control and [unit tests](10.1109/MAHC.1983.10102) A Process will contain the following information:

- Contents of an implementation
    - lab-ready protocol
    - Bill of materials
    - List of what to have at your bench
    - Recommendations for storage and unit testing -->

<!-- ## Cytosols -->

<!-- Here are a collection of processes that are useful for making and working with Cytosols -->

<!-- :::{figure} ./resources/flowchart-cytosols.png
:align: center
:label: fig:figure1
Flow chart for building Base Cytosol and its modification through the addition of Modules.
::: -->

<!-- - [Process Template](./process-template/process-make_template.md)

- [Make Amino Acid Mix](./make-amino-acid-mix/process-make_amino_acid_mix.md)
- [Make Small Molecule Mix](./make-small-molecule-mix/process-make_small_molecule_mix.md) -->
<!-- - [Make tRNAs](https://antonrmolina.github.io/nucleus-distribution-pages/docs/processes/make-trna/process-make-trnas) -->
<!-- - [Make tRNAs](./make-trna/process-make_trnas.md)
- Make Energy Mix

- Make Protein mix (1-pot)
- Make Protein mix (36-pot) -->
<!-- - [Make Ribosomes](https://antonrmolina.github.io/nucleus-distribution-pages/docs/processes/make-ribosomes/process-make-ribosomes) -->
<!-- - [Make Ribosomes](./make-ribosomes/process-make_ribosomes.md)

- [Assemble Base Cytosol from Kit](./assemble-cytosol-from-kit/process-assemble_cytosol_from_kit.md) -->

<!-- **Quality Control**

- Protein Gel
- Pierce660 Assay
- BCA Assay
- Measuring fluorescence with plate reader [](../) -->

<!-- ## Cells -->

<!-- Here are a collection of processes that useful for making and working with Cells -->

<!-- :::{figure} ./resources/flowchart-cells.png
:align: center
:label: fig:figure2
Flow chart for building Base Cell and its modification through the addition of Modules.
::: -->

<!-- - [Make Base Cell](./assemble-base-cell/process-make_base_cell.md) -->

<!-- **Quality Control**

- Measuring fluorescence with microscope -->