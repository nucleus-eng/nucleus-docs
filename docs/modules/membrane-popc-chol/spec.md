---
title: "Base Membrane: POPC/Chol"
subtitle: "Module Specification"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Base Membrane specifies a phospholipid bilayer composed of (POPC), cholesterol, and fluorescent Lissamine Rhodamine PE (Liss-Rhod PE). The Base Membrane is our recommended default membrane for making synthetic cells by using [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} schematic.png
:width: 50%
:align: center

Schematic of a POPC/Chol liposome.
:::
::::

:::::

## Reference Composition

:::{table}
:label: comp-membrane

| Component    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 70                    | 760.076                  | 25                          | 162.17             |
| Cholesterol  | 29.95                 | 386.654                  | 50                          | 17.65              |
| Liss-Rhod PE | 0.05                  | 1301.71                  | 1                           | 4.96               |

:::

## Expected Behavior

The behavior of Base Membrane is characterized using the [deGFP Reporter](../reporter-degfp/spec.md) Module in [Base Cell](../base-cell/spec.md).

## Protocols

Protocols for assembling Base Cell and making its components from scratch are described in the Process [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).