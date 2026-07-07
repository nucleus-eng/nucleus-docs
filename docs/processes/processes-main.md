---
title: "Processes"
---

# Overview

Processes represent the core protocols. They tell you how to transform physical materials into Base Cytosol and Cell. Modules extend the functionality of Base Cytosol and Cell. 

## Base Cell Processes

The Base Cell is formed by encapsulating Base Cytosol (see below) in a liposome.

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TB
    BaseCytosol["Base Cytosol"] -->|"Add Module"| Cytosol["Cytosol"]
    ModSpec(["Module Spec"]) -.-> Cytosol
    Cytosol & Membrane["Membrane"] --> J(( ))
    J --> |"Assemble Base Cell"| BaseCell["Base Cell"]
    MemSpec(["Membrane Spec"]) -.-> Membrane

    style BaseCytosol fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Cytosol fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Membrane fill:#6B7280,color:#ffffff,stroke:#4B5563
    style BaseCell fill:#6B7280,color:#ffffff,stroke:#4B5563
    style ModSpec fill:#6B7280,color:#ffffff,stroke:#4B5563
    style MemSpec fill:#6B7280,color:#ffffff,stroke:#4B5563
    style J fill:none,stroke:none

    click BaseCytosol "/docs/modules/base-cytosol/spec"
    click BaseCell "/docs/processes/assemble-base-cell/main"
    click ModSpec "/docs/modules/modules-main"
    click MemSpec "/docs/modules/membrane-popc-chol/spec"
```

- [Assemble Base Cell](./assemble-base-cell/main.md)

## Base Cytosol Processes

Base Cytosol is a molecular system with a defined set of components including T7 RNA Polymerase, ribosomes, and tRNA capable of transcription and translation. Base Cytosol builds on the [PURE system](https://doi.org/10.1038/90802), and is optimized for integration and extension.

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    AminoAcids["Amino Acid Mix"] -->|"Make SMix"| SMix["SMix"]
    SMix & tRNA["tRNA"] & PMix["PMix"] & Ribosomes["Ribosomes"] --> J(( ))
    
    J --> |"Assemble Base Cytosol"| BaseCytosol["Base Cytosol"]
    BaseCytosol -->|"Add Module"| Cytosol["Cytosol"]
    ModSpec(["Module Spec"]) -.-> Cytosol

    style AminoAcids fill:#6B7280,color:#ffffff,stroke:#4B5563
    style SMix fill:#6B7280,color:#ffffff,stroke:#4B5563
    style tRNA fill:#6B7280,color:#ffffff,stroke:#4B5563
    style PMix fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Ribosomes fill:#6B7280,color:#ffffff,stroke:#4B5563
    style BaseCytosol fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Cytosol fill:#6B7280,color:#ffffff,stroke:#4B5563
    style ModSpec fill:#6B7280,color:#ffffff,stroke:#4B5563
    style J fill:none,stroke:none

    click AminoAcids "/docs/processes/make-amino-acid-mix/main"
    click SMix "/docs/processes/make-small-molecule-mix/main"
    click tRNA "/docs/processes/make-trna/main"
    click PMix "/docs/processes/make-36pot/main"
    click Ribosomes "/docs/processes/make-ribosomes/main"
    click BaseCytosol "/docs/processes/assemble-base-cytosol/main"
    click ModSpec "/docs/modules/modules-main"
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

