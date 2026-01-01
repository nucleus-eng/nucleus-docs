---
title: Modules
---

# Overview

A Module is a useful biochemical formulation, often incorporating a genetically encoded component, that performs a particular function. Modules Specifications answer the questions 1) "What is it?" and 2) "What should I expect when I implement it?".

:::{figure} ./resources/flowchart-2.png
:width: 50%
Modules can be combined with Process Protocols to create Integrations.
:::

Module Specifications contain the following information:

- Brief description
- Expected behavior
- Where to access the materials
- design file of genetic components, if applicable
- schematic describing basic use
- List of reference implementations



## List of Modules

:::{table}

| Module Class | Module Implementation | Base Module | Status |
| --- | --- | --- | --- |
| Reporter | [deGFP](./reporter-degfp/spec.md) | **Nucleus Cytosol;** PURExpress Cell | Distribution |
| Membrane | POPC/Chol | PURExpress Cell | Distribution |
| Membrane Pore | [alpha-Hemolysin](./membrane-pore-ahly/spec.md) | PURExpress Cell  | Distribution |
|  | [Cx43](./membrane-pore-cx43/spec.md) | PURExpress Cell | DevNote |
| Detector | [tetR-aTc](./detector-tetr_atc/spec.md) | PURExpress Cell | Distribution |
| Emitter | [IV-HSL](./emitter-ivhsl/spec.md) | PURExpress Cell | Distribution |
| Energy | [PPK](./energy-ppk/spec.md) | PURExpress Cell | DevNote |
| Control | ClpXP | PURExpress Cytosol | DevNote* |
| Chaperone | SecYEG | - | Planned |

:::

## Module contribution standards

- Cytosol Module Standard

