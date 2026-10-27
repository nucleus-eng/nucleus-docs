---
title: Modules
description: A catalog of validated biochemical modules — detectors, reporters, emitters, membrane pores, and energy systems — for extending Nucleus synthetic cells.
---

# Overview

A Module is a useful biochemical formulation, often incorporating a genetically encoded component, that performs a particular function. Modules Specifications answer the questions 1) "What is it?" and 2) "What should I expect when I implement it?".

## PURExpress

Modules validated in [NEB PURExpress](https://www.neb.com/en-us/products/e6800-purexpress-invitro-protein-synthesis-kit).

:::{table}

| Module Class    | Specification                               | DevNotes |
| --------------- | ------------------------------------------- | -------- |
| Membrane (Base) | [POPC/Chol](./membrane-popc-chol/spec.md)   | 4        |
| Detector        | [tetR-aTc](./detector-tetr-atc/spec.md)     | 4        |
|                 | [LacI-IPTG](./detector-laci-iptg/spec.md)   | 0        |
| Emitter         | [IV-HSL](./emitter-ivhsl/spec.md)           | 1        |
| Control         | [ClpXP](./control-clpxp/spec.md)            | 4        |
| Energy          | [PPK](./energy-ppk/spec.md)                 | 4        |
| Membrane Pore   | [α-Hemolysin](./membrane-pore-ahly/spec.md) | 0        |
|                 | [Cx43](./membrane-pore-cx43/spec.md)        | 2        |

:::

## Nucleus Cytosol

Modules validated in [Nucleus Cytosol](./base-cytosol/spec.md).

:::{table}

| Module Class       | Specification                                       | DevNotes |
| ------------------ | --------------------------------------------------- | -------- |
| Cytosol (Base)     | [Cytosol](./base-cytosol/spec.md)                   | 10       |
| Protein Mix        | [PMix](./pmix/spec.md)                              | 0        |
| Small Molecule Mix | [SMix](./smix/spec.md)                              | 0        |
| Membrane (Base)    | [POPC/Chol](./membrane-popc-chol/spec.md)           | 4        |
| Reporter           | [deGFP](./reporter-degfp/spec.md)                   | 7        |
| Cell (Base)        | [Base Cell](./base-cell/spec.md)                    | 6        |
| Cell (Dye)         | [Dye Liposomes](./dye-liposomes/spec.md)            | 0        |
| Detector           | [pH-Sensing](./detector-ph/spec.md)                 | 1        |
| Reporter           | [LacZ Enzyme](./reporter-lacz-enzyme/spec.md)       | 1        |
| Cell (Sensing)     | [pH Sensing Cell](./ph-sensing-cell/spec.md)        | 1        |
| Cell (Substrate)   | [Substrate LUV: CPRG](./substrate-cprg-luv/spec.md) | 3        |
| Cell (Substrate)   | [Substrate SUV: CPRG](./substrate-cprg-suv/spec.md) | 1        |
| Cascade            | [pH Cascade](./ph-cascade/spec.md)                  | 1        |
| Reporter           | [Color Change](./color-change/spec.md)              | 1        |
| Detector           | [3OC6-HSL (EsaR)](./detector-esar/spec.md)          | 1        |
:::

## Gels

Modules that hold a sample in a polymer network set in an outer solution.

:::{table}

| Module Class         | Specification                       | DevNotes |
| -------------------- | ----------------------------------- | -------- |
| Gel (Thermal)        | [Gel: ULGA](./gel-ulga/spec.md)     | 2        |
| Gel (Thermal)        | [Gel: LGA](./gel-lga/spec.md)       | 2        |
| Gel (Photopatterned) | [Gel: PEG-nb](./gel-peg-nb/spec.md) | 2        |
:::

# Contributing a Module

Modules specifications are derived from DevNotes that follow the adhere to the [Module Contribution Guidelines](../../guides/contribution-guide.md).

<!-- # List of Modules

## Reporter: deGFP
- [Specification](./reporter-degfp/spec.md)
- Base Module: Base Cytosol
- Status: Cell

## Membrane Pore: α-Hemolysin
- [Specification](./reporter-degfp/spec.md)
- Base Module: PURExpress
- Status: Cell

## Membrane Pore: Cx43
- [Specification](./membrane-pore-cx43/spec.md)
- Base Module: PURExpress
- Status: Cell

## Detector: tetR-aTc
- [Specification](./detector-tetr-atc/spec.md)
- Base Module: PURExpress
- Status: Cell
  
## Emitter: IV-HSL
- [Specification](./emitter-ivhsl/spec.md)
- Base Module: PURExpress
- Status: Cell

## Energy: PPK

- [Specification](./energy-ppk/spec.md)
- Base Module: PURExpress
- Status: Cell

## Control: ClpXP
- [Specification](./control-clpxp/spec.md)
- Base Module: PURExpress
- Status: Cytosol

## Chaperone: SecYEG
- [Specification](./control-clpxp/spec.md)
- Base Module: -
- Status: planned





<!-- :::{figure} ./resources/flowchart-2.png
:width: 50%
Modules can be combined with Process Protocols to create Implementations.
::: -->

<!-- Module Specifications contain the following information:

- Brief description
- Expected behavior
- Where to access the materials
- design file of genetic components, if applicable
- schematic describing basic use
- List of reference implementations -->



<!-- ## List of Modules

:::{table}

| Module Class | Module Implementation | Base Module | Status |
| --- | --- | --- | --- |
| Reporter | [deGFP](./reporter-degfp/spec.md) | **Nucleus Cytosol;** PURExpress Cell | Distribution |
| Membrane | POPC/Chol | PURExpress Cell | Distribution |
| Membrane Pore | [alpha-Hemolysin](./membrane-pore-ahly/spec.md) | PURExpress Cell  | Distribution |
|  | [Cx43](./membrane-pore-cx43/spec.md) | PURExpress Cell | DevNote |
| Detector | [tetR-aTc](./detector-tetr-atc/spec.md) | PURExpress Cell | Distribution |
| Emitter | [IV-HSL](./emitter-ivhsl/spec.md) | PURExpress Cell | Distribution |
| Energy | [PPK](./energy-ppk/spec.md) | PURExpress Cell | Distribution |
| Control | [ClpXP](./control-clpxp/spec.md) | PURExpress Cytosol | Distribution |
| Chaperone | SecYEG | - | Planned |

:::

## Module contribution standards

- Cytosol Module Standard
 --> 
