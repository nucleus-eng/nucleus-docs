---
title: Instance (Instance Name)
site:
    hide-toc: true
---

## Overview

The Overview says what this module is and what it does. Nothing else. A reader should be able to tell in a few seconds whether they're on the right page. Most Module overviews in the codebase are one sentence. Open with the name, state the function, and include key parameters that define scope (a pore diameter, a substrate, a cutoff). Use precise terms: "acyl-homoserine lactone," not "signaling molecule." Don't explain what a ribosome does. The reader knows. Skip preamble like "welcome to this page" or "in this document we describe." Just start:

"The ClpXP control Module uses the ClpXP protease complex to enable the programmable degradation of ssrA-tagged target proteins in an ATP-dependent manner."
"The α-hemolysin membrane pore module produces a self-inserting membrane pore with diameter ~3 nm, permitting the passage of molecules < ~3000 kDa."
"The PPK energy Module generates ATP and GTP from AMP and GDP, respectively, using inorganic polyphosphate (100mer) as a phosphate donor."
When in doubt, read the existing Module specs.

:::{figure} ./resources/schematic-example-2.png
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

