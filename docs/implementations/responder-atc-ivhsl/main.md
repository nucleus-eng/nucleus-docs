---
title: "Responder: aTc IV-HSL Responder Cell"
site:
    hide-toc: true
---

## Overview

The aTc IV-HSL Responder Cell produces IV-HSL, an acyl-homoserine lactone, in response to detection of aTc. E. coli in co-culture detect IV-HSL and produce a fluorescent signal. 

:::{attention}

This Instance has not been validated in Nucleus Cytosol $\ge$ v0.5. Documentation can be found on the legacy site [here](https://nucleus.bnext.bio/Responder-Cells-196ae616eb5180488db1f8b9e21473eb). 

:::

<!-- :::{figure} ./resources/schematic-example-2.png
:name: fig2-kinetics
:align: center
:width: 75%

This is a schematic of the module of the system.
:::

## Resources

::::{grid} 1 1 2 3

:::{card}
:header: **Bill of Materials**
{button}`Download BOM <./resources/BOM-template.pdf>`
:::

:::{card}
:header: **Lab-Ready Protocol**
:align: center
{button}`Download Protocol <./resources/protocol_example.pdf>`
:::

:::{card}
:header: **Platemap Template**
{button}`Download Platemap <./resources/BOM-template.pdf>`
:::
::::

## Expected Behavior

The transcription factors moved to their promoter sites. They did this quietly, without ceremony. RNA polymerase followed. It always did. In the mitochondria, the cristae worked. They made ATP the way they had always made it. Through gradients. Through chemistry older than thought. The ribosomes assembled. They read the RNA like fishermen reading water. Each amino acid found its place. The chain grew longer. Vesicles carried their cargo through the cell's narrow passages. From the rough ER to the Golgi. Some proteins were marked. Others were not. The cell knew which ones mattered. The checkpoints watched over replication. DNA split and reformed. When something went wrong, the cell stopped. It had learned this lesson before.

:::::{tab-set}

::::{tab-item} Time series
:sync: tab1-1
:::{figure} ./behavior/ppk-kinetics.png
:name: fig2-kinetics
:align: center
:width: 75%

Translation kinetics of PURE reactions using the custom energy solution with or without CP. The "PURE Positive" refers to the PURExpress reaction using Solutions A and B. Data sourced from [DevNote](https://devnotes.bnext.bio/articles/cytosol-module-mthfs).
:::
::::

::::{tab-item} End point
:sync: tab1-2
:::{figure} ./behavior/ppk-endpoint.png
:name: fig3-endpoint
:align: center
:width: 75%

Final protein yields of the three reactions measured at steady state. [DevNote](https://devnotes.bnext.bio/articles/cytosol-module-mthfs).
:::
::::

:::::

## Modules

This instance made use of the following modules.

- [plamGFP](/docs/modules/mod-list/mod-plamGFP/specification)
- [my-module](/docs/modules/mod-list/module-template/specification)
 -->
