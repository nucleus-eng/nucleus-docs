---
title: "Base Membrane: POPC/Chol"
subtitle: "Module Specification"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Base Membrane specifies a set of components that are used to make the lipid bilayers defining the Base Cell. The membrane is a composed of (POPC), cholesterol, and fluorescent Lissamine rhodamine PE. The Base Membrane represents a sane default for making synthetic cells. The Base Cell is made by encapsulating Base Cytosol in Base Membrane following the Process [Assemble Base Cell](../../processes/assemble-base-cell/main.md).

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} schematic.png
:width: 50%
:align: center

Schematic of a POPC/Chol liposome.
:::
::::

::::{tab-item} Designs

- None

::::
:::::

## Reference Composition

:::{table}
:label: comp-membrane
| Component | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (uL) |
| --- | --- | --- | --- | --- |
| POPC | 70 | 760.076 | 25 | 162.17 |
| Cholesterol | 29.95 | 386.654 | 50 | 17.65 |
| Liss-Rhod PE | 0.05 | 1301.71 | 1 | 4.96 |

:::

## Expected Behavior

The behavior of Base Cell composed of Base Membrane is characterized using the [deGFP Reporter](../reporter-degfp/spec.md) Module. 

## Protocols

Protocols for assembling Base Cell and making its components from scratch are described in the Process [Assembling Base Cell](../../processes/assemble-base-cell/main.md).