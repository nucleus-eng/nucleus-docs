---
title: "TODO: Implementation Name"
subtitle: Implementation
status: draft  # draft | unvalidated-published | validated-published — see CLAUDE.md "Page status"
site:
    hide-toc: true
---

# Overview

The Overview says what this implementation is and what it does. Nothing else. A reader should be able to tell in a few seconds whether they're on the right page. An implementation combines one or more Module specs with a Process — the overview should name both and state what the combination produces. Include key parameters that define scope. Use precise terms. Don't explain what a ribosome does. The reader knows. Skip preamble. Just start:

"The IV-HSL Emitter implementation combines the IV-HSL Emitter Module with the Assemble Base Cell process to produce synthetic cells that secrete N-(3-hydroxybutanoyl)-L-homoserine lactone (IV-HSL) and activate GFP expression in neighboring E. coli reporter cells."

"The PPK energy implementation combines the PPK energy Module with the Assemble Base Cytosol process to produce a CP/CK-free cell-free transcription–translation system powered by inorganic polyphosphate regeneration."

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
{button}`Download BOM <TODO: bom.pdf>`
:::

:::{card}
:header: **Lab-Ready Protocol**
:align: center
{button}`Download Protocol <TODO: protocol.pdf>`
:::

:::{card}
:header: **Platemap Template**
{button}`Download Platemap <TODO: platemap.pdf>`
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

# Process

Link to the base Process this implementation follows. If this implementation deviates from the standard process (different volumes, modified steps, additional preparation), note that here.

- [TODO: Process Name](../../processes/TODO/main.md)

# Modules

List the modules used in this implementation. Link each to its spec page. If a module is used in a non-standard configuration (different concentration, modified construct), note that here.

- [TODO: Module Name](../../modules/TODO/spec.md)
- [TODO: Module Name](../../modules/TODO/spec.md)

# Credits

<!-- List the people who developed or validated this implementation.
Link to ORCID or personal pages where available. -->

- [TODO: Name](https://orcid.org/TODO)
