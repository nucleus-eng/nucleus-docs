---
title: "Processes"
---

# Overview

Processes represent the core protocols. They tell you how to transform physical materials into Base Cytosol and Cell. Modules extend the functionality of Base Cytosol and Cell. 

## Base Cell Processes

The Base Cell is formed by encapsulating Base Cytosol (see below) in a liposome.

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#408E69', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#006837', 'lineColor': '#555555'}}}%%
flowchart TB
    BaseCytosol["Base Cytosol"] --> Cytosol["Cytosol"]
    ModDNA["Module DNA"] --> ModSpec["Module Specifications"]
    ModSpec -.-> Cytosol
    Cytosol --> AssembleCell["Assemble Base Cell"]
    MemSpec["Membrane Specification"] -.-> AssembleCell
    AssembleCell --> BaseCell["Base Cell"]

    style BaseCytosol fill:#408E69,color:#ffffff,stroke:#006837
    style Cytosol fill:#408E69,color:#ffffff,stroke:#006837
    style AssembleCell fill:#907BB8,color:#ffffff,stroke:#6B4FA0
    style BaseCell fill:#907BB8,color:#ffffff,stroke:#6B4FA0
    style ModDNA fill:#D15D62,color:#ffffff,stroke:#C1272D
    style ModSpec fill:#D15D62,color:#ffffff,stroke:#C1272D
    style MemSpec fill:#D15D62,color:#ffffff,stroke:#C1272D

    click BaseCytosol "./assemble-base-cytosol/main"
    click AssembleCell "./assemble-base-cell/main"
    click ModDNA "../dna-distro"
    click ModSpec "../modules/modules-main"
    click MemSpec "../modules/modules-main"
```

- [Assemble Base Cell](./assemble-base-cell/main.md)

## Base Cytosol Processes

Base Cytosol is a molecular system with a defined set of components including T7 RNA Polymerase, ribosomes, and tRNA capable of transcription and translation. Base Cytosol builds on the [PURE system](https://doi.org/10.1038/90802), and is optimized for integration and extension.

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'primaryColor': '#006837', 'primaryTextColor': '#ffffff', 'primaryBorderColor': '#006837', 'lineColor': '#555555'}}}%%
flowchart LR
    AAMix["Amino Acid Mix"] --> SMix["SMix"]
    SMix --> BaseCytosol["Base Cytosol"]
    tRNA["tRNA"] --> BaseCytosol
    PMix["PMix"] --> BaseCytosol
    Ribosomes["Ribosomes"] --> BaseCytosol
    BaseCytosol --> Cytosol["Cytosol"]
    ModDNA["Module DNA"] --> ModSpec["Module Specifications"]
    ModSpec -.-> Cytosol

    style AAMix fill:#408E69,color:#ffffff,stroke:#006837
    style SMix fill:#408E69,color:#ffffff,stroke:#006837
    style tRNA fill:#408E69,color:#ffffff,stroke:#006837
    style PMix fill:#408E69,color:#ffffff,stroke:#006837
    style Ribosomes fill:#408E69,color:#ffffff,stroke:#006837
    style BaseCytosol fill:#408E69,color:#ffffff,stroke:#006837
    style Cytosol fill:#408E69,color:#ffffff,stroke:#006837
    style ModDNA fill:#D15D62,color:#ffffff,stroke:#C1272D
    style ModSpec fill:#D15D62,color:#ffffff,stroke:#C1272D

    click AAMix "./make-amino-acid-mix/main"
    click SMix "./make-small-molecule-mix/main"
    click tRNA "./make-trna/main"
    click PMix "./make-36pot/main"
    click Ribosomes "./make-ribosomes/main"
    click BaseCytosol "./assemble-base-cytosol/main"
    click ModDNA "../dna-distro"
    click ModSpec "../modules/modules-main"
```

- [Assemble Base Cytosol](./assemble-base-cytosol/main.md)

### Make Base Cytosol Components

- [Make Amino Acid Mix](./make-amino-acid-mix/main.md)
- [Make Small Molecule Mix](./make-small-molecule-mix/main.md)
- [Make tRNAs](./make-trna/main.md)
- [Make Ribosomes](./make-ribosomes/main.md)
- [Make PMix](./make-36pot/main.md)
- [Make OnePot PMix](./make-1pot/main.md)
- [Make Individual Proteins](./make-protein/make-protein-main.md)

### Quality Control Processes

- [Protein Gel](./protein-gel/main.md)
- [Pierce660 Assay](./pierce660/main.md)

