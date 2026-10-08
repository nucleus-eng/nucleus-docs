---
title: "Processes"
description: Step-by-step lab protocols for preparing PURE system-based cytosol, ribosomes, membranes, and assembling synthetic cells from physical materials.
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

## Encapsulation Processes

Three routes close a bilayer around an aqueous payload. Which route to use depends on what goes inside and on what the product feeds into. Small unilamellar vesicles (SUVs) carry pre-loaded chromogenic substrate and feed into alginate gel embedding — these use the extrusion + SEC method documented in [Encapsulation: Extrusion](./encapsulate-suv/main.md), a genuinely different technique. Large unilamellar vesicles (LUVs) fill the same substrate role, made by [Encapsulation: Freeze-Thaw](./encapsulate-luv/main.md). Synthetic cells carry the sensing and cell-free expression machinery and feed into both alginate and agarose gel embedding — these use the same mineral-oil phase-transfer method as [Encapsulation: Phase Transfer](./assemble-base-cell/main.md), with each system's lipid composition documented on its own membrane Module spec rather than as a separate process.

- [Encapsulation](./encapsulate/main.md) — the abstraction every route below is an instance of. Closes a bilayer around an aqueous payload, and packs rather than mixes.
  - [Encapsulation: Phase Transfer](./assemble-base-cell/main.md) — emulsion and transfer through an interface; produces synthetic cells.
  - [Encapsulation: Extrusion](./encapsulate-suv/main.md) — film hydration and extrusion; produces SUVs, which are never interchangeable with synthetic cells.
  - [Encapsulation: Freeze-Thaw](./encapsulate-luv/main.md) — film hydration, sonication and freeze-thaw; produces LUVs.

## Sensing Cascade Processes

These three steps serve a sensing cascade. None of them is a reading: one brings a sample to the pH its reporter enzyme needs, one makes a reagent a cascade is built with, and one cuts signal from outside the compartment. The reading itself is in [Assays](#assays).

- [Color Development](./color-development/main.md) — brings a gel to the pH its reporter enzyme needs, after a sensing step that ran where the enzyme cannot work. Only the pH path uses it.
- [Anneal pH-Responsive Trigger Duplex](./anneal-ph-trigger-duplex/main.md) — anneals the pH-responsive and trigger ssDNA into the single duplex reagent the pH-Sensing Module uses
- [Degrade Exterior LacZ](./degrade-exterior-lacz/main.md) — proteinase K treatment to cut background signal from LacZ that has leaked outside a liposome.

## Assays

An assay reads something and yields a value. Nothing it produces goes back into a tube, which is what sets this section apart from every other one on this page.

- [Assay](./assay/main.md) — the abstraction the readouts below are instances of.
  - [Colorimetric Readout](./colorimetric-readout/main.md) — the stage every sensing cascade ends at. A plate-reader absorbance read, or an endpoint score by eye.
  - [Microscopy Readout](./microscopy-readout/main.md) — reads a sample one object at a time. Counts and morphology, encapsulation, retention over time, and which of two populations a signal came from.
  - [Osmometry Readout](./osmometry-readout/main.md) — the osmolality of a solution, read from a 10 µL aliquot that is spent. How an outer solution is set against an inner one.
  - [Pierce660 Assay](./pierce660/main.md) — total protein against a standard curve. The reagent reacts with the protein it measures, so the aliquot is spent.
  - [Protein Gel](./protein-gel/main.md) — a mixture separated roughly by molecular weight and read as bands.

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

- [Assemble Solution](./assemble-solution/assemble-solution-main.md) — the abstraction both mixing processes below are instances of.
  - [Assemble Cytosol](./assemble-cytosol/assemble-cytosol-main.md) — a reaction that will be encapsulated; reserves headroom for what a particular reaction adds.
    - [Assemble Base Cytosol](./assemble-base-cytosol/main.md) — the unit case, with the headroom filled by water.
  - [Assemble Outer Solution](./assemble-outer-solution/main.md) — what cells sit in, and what a gel dissolves into.
- [Expression](./express/main.md) — the abstraction both supply routes are instances of. Makes a protein from a template in the reaction, and mixes rather than packs.

### Make Base Cytosol Components

- [Make Amino Acid Mix](./make-amino-acid-mix/main.md)
- [Make Small Molecule Mix](./make-small-molecule-mix/main.md)
- [Make tRNAs](./make-trna/main.md)
- [Make Ribosomes](./make-ribosomes/main.md)
- [Make PMix](./make-36pot/main.md)
- [Make OnePot PMix](./make-1pot/main.md)
- [Make Individual Proteins](./make-protein/make-protein-main.md)
- [Amplify Linear Template](./amplify-linear-template/main.md) — a DNA template rather than a cytosol ingredient: prepared the same way and spent in the same reaction.

Check a finished prep with [Pierce660 Assay](./pierce660/main.md) for total protein, or a [Protein Gel](./protein-gel/main.md) for purity. Both sit in [Assays](#assays), with the rest of the readouts.

## Embedding Processes

Embedding holds compartments that already exist in place. The gel fixes a position without enclosing anything, so a cascade can keep an enzyme and its substrate in one gel with no reaction until something lyses. Two gel chemistries are documented here, one set ionically and one set thermally — see each process page for the chemistry it covers and how it differs from the others.

- [Embedding](./embed-gel/main.md) — the abstraction both routes below are instances of. Holds position rather than contents, and illuminates nothing.
  - [Embedding: Ionic Crosslinking](./embed-ionic-crosslinking/main.md) — ionic crosslinking of sodium alginate by calcium, at ~1% (w/v) alginate with 200 mM CaCl₂.
  - [Embedding: Thermal Setting](./embed-thermal-setting/main.md) — thermal gelation of agarose in two grades, ULGA and LGA; fed by phase-transfer synthetic cells only.

## Photopatterning Processes

Beyond simple gel embedding, spatial patterning within the gel matrix can compartmentalize multiple sensing modules.

- [Embedding: Photodevelopment](./embed-photodevelopment/main.md) — what the two photocrosslinking routes share, and the table of what they do not.
  - [Embedding: Photodevelopment](./embed-photodevelopment/main.md) — 405 nm-crosslinked PEGDA gel; not yet demonstrated to link through to a macroscopically visible colorimetric readout.
- [Embedding: Photodevelopment](./embed-photodevelopment/main.md) — step-growth thiol-ene route (PEG-norbornene).

