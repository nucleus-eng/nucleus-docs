---
title: "TODO: Implementation Name"
subtitle: Implementation
site:
    hide-toc: true
---

# Overview

The Overview says what this implementation is and what it does. Nothing else. A reader should be able to tell in a few seconds whether they're on the right page. Most overviews are one sentence. Open with the name, state the function, and include key parameters that define scope (a pore diameter, a substrate, a cutoff). Use precise terms: "acyl-homoserine lactone," not "signaling molecule." Don't explain what a ribosome does. The reader knows. Skip preamble like "welcome to this page" or "in this document we describe." Just start:

"The ClpXP control Module uses the ClpXP protease complex to enable the programmable degradation of ssrA-tagged target proteins in an ATP-dependent manner."
"The α-hemolysin membrane pore module produces a self-inserting membrane pore with diameter ~3 nm, permitting the passage of molecules < ~3000 kDa."
"The PPK energy Module generates ATP and GTP from AMP and GDP, respectively, using inorganic polyphosphate (100mer) as a phosphate donor."

When in doubt, read the existing Implementation specs.

:::{figure} ./resources/schematic-example-2.png
:name: fig-schematic
:align: center
:width: 75%

TODO: One sentence describing what the schematic shows. If the figure is not original, credit the source and include the license (e.g. "Figure by Author et al. used under CC-BY-4.0 / cropped from original.").
:::

# Protocol

The protocol section contains the step-by-step procedure for building this implementation. Write it so someone can follow it at the bench. State volumes, concentrations, incubation times, and temperatures as concrete values, not ranges, unless the range is intentional. If a step depends on a Process documented elsewhere, link to it rather than repeating it. Include a composition table if the implementation requires assembling multiple components.

*Under Construction*

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

# Performance

Show what this implementation actually did in practice. Include representative data: time series, endpoint measurements, dose-response curves, or whatever characterizes the system's behavior. Each figure should have a caption that states the experimental conditions and links to the source DevNote. If performance varies across conditions (temperature, concentration, cytosol batch), show that. The goal is to let a reader judge whether this implementation fits their use case without having to reproduce the experiment first.

:::::{tab-set}

::::{tab-item} Time series
:sync: tab1-1
:::{figure} ./behavior/ppk-kinetics.png
:name: fig-kinetics
:align: center
:width: 75%

Translation kinetics of PURE reactions using the custom energy solution with or without CP. The "PURE Positive" refers to the PURExpress reaction using Solutions A and B. Data sourced from [DevNote](https://devnotes.bnext.bio/articles/cytosol-module-mthfs).
:::
::::

::::{tab-item} End point
:sync: tab1-2
:::{figure} ./behavior/ppk-endpoint.png
:name: fig-endpoint
:align: center
:width: 75%

Final protein yields of the three reactions measured at steady state.
[DevNote](https://devnotes.bnext.bio/articles/cytosol-module-mthfs).
:::
::::

:::::

# Modules

List the modules used in this implementation. Link each to its spec page. If a module is used in a non-standard configuration (different concentration, modified construct), note that here.

- [TODO: Module Name](../../modules/TODO/spec.md)
- [TODO: Module Name](../../modules/TODO/spec.md)

# Credits

<!-- List the people who developed or validated this implementation.
Link to ORCID or personal pages where available. -->

- [TODO: Name](https://orcid.org/TODO)
