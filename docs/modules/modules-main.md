---
title: Modules
---

# Overview

A Module is a useful biochemical formulation, often incorporating a genetically encoded component, that performs a particular function. Modules Specifications answer the questions 1) "What is it?" and 2) "What should I expect when I implement it?".

:::{table}

| Module Class | Module Implementation | Base Module | Status |
| --- | --- | --- | --- |
| Base | [Cytosol](./base-cytosol/spec.md) | - | Specification |
| Reporter | [deGFP](./reporter-degfp/spec.md) | Base Cytosol | Specification |
| Membrane | POPC/Chol | PURExpress | Specification |
| Membrane Pore | [α-Hemolysin](./membrane-pore-ahly/spec.md) | PURExpress  | Specification |
|  | [Cx43](./membrane-pore-cx43/spec.md) | PURExpress | DevNote |
| Detector | [tetR-aTc](./detector-tetr_atc/spec.md) | PURExpress | Specification |
| Emitter | [IV-HSL](./emitter-ivhsl/spec.md) | PURExpress | Specification |
| Energy | [PPK](./energy-ppk/spec.md) | PURExpress | Specification |
| Control | [ClpXP](./control-clpxp/spec.md) | PURExpress | Specification |
| Chaperone | SecYEG | - | Planned |

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
- [Specification](./detector-tetr_atc/spec.md)
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
| Detector | [tetR-aTc](./detector-tetr_atc/spec.md) | PURExpress Cell | Distribution |
| Emitter | [IV-HSL](./emitter-ivhsl/spec.md) | PURExpress Cell | Distribution |
| Energy | [PPK](./energy-ppk/spec.md) | PURExpress Cell | Distribution |
| Control | [ClpXP](./control-clpxp/spec.md) | PURExpress Cytosol | Distribution |
| Chaperone | SecYEG | - | Planned |

:::

## Module contribution standards

- Cytosol Module Standard
 --> 
