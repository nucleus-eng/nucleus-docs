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
    J --> |"Encapsulate"| BaseCell["Base Cell"]
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

- [Encapsulation: Phase Transfer](./assemble-base-cell/main.md)

## DevCell Encapsulation Processes

DevCell integrations (e.g., the Chicago colorimetric readout system) build on two liposome preparations. Small unilamellar vesicles (SUVs) carry pre-loaded chromogenic substrate and feed into alginate hydrogel embedding — these use the extrusion + SEC method documented in SUV Encapsulation, a genuinely different technique. synthetic cells carry the sensing and cell-free expression machinery and feed into both alginate and ULGA hydrogel embedding — these use the same mineral-oil phase-transfer method as [Encapsulation: Phase Transfer](./assemble-base-cell/main.md); GUV Encapsulation: Lipid Variants documents only the Chicago/London lipid-composition variants on top of that shared method.

- [SUV Encapsulation](./encapsulate-suv/main.md)

## DevCell Readout Processes

Every DevCells sensing cascade (Chicago and London alike) ends at the same downstream step: a chromogenic substrate hydrolyzed by a reporter enzyme to give a visible, absorbance-measurable signal.

- [Colorimetric Readout](./colorimetric-readout/main.md)
- [Degrade Exterior LacZ](./degrade-exterior-lacz/main.md) — proteinase K treatment to cut background signal from LacZ that has leaked outside a liposome; concentrations and volumes not yet specified.

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

## Hydrogel Embedding Processes

Sensing cells (synthetic cell format) and reporter liposomes (SUV format) are embedded together in a hydrogel matrix to couple a lysis-triggered colorimetric handoff between them. Different DevCells demos use different hydrogel chemistries — see each process page for the chemistry it covers and how it differs from the others.

- [Alginate Hydrogel Embedding](./embed-alginate-hydrogel/main.md) — Chicago-specific; ionic (CaCl₂) crosslinking of sodium alginate.
- [ULGA Hydrogel Embedding](./embed-ulga-hydrogel/main.md) — London-specific; thermal gelation of ultra-low-gelling-temperature agarose, fed by GUV Encapsulation only.

## Photopatterning Processes

Beyond simple hydrogel embedding, spatial patterning within the hydrogel matrix can compartmentalize multiple sensing modules. PEGDA is one hydrogel chemistry explored for this — see the process page for its current status and open gaps.

- [Photopatterning, PEGDA](./photopattern-pegda/main.md) — 405 nm-crosslinked PEGDA hydrogel; not yet demonstrated to link through to a macroscopically visible colorimetric readout.

