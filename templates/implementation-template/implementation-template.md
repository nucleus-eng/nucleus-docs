---
title: "TODO: Implementation Name"
subtitle: Implementation
status: draft  # draft | unvalidated-published | validated-published — see CLAUDE.md "Page status"
site:
    hide-toc: true
---

# Overview

The Overview says what this implementation is and what it does. Nothing else. A reader should be able to tell in a few seconds whether they're on the right page. An implementation combines one or more Module specs with a Process — the overview should name both and state what the combination produces. Include key parameters that define scope. Use precise terms. Don't explain what a ribosome does. The reader knows. Skip preamble. Just start:

"The CRAIC Demo detects a bacterial quorum-sensing signal and reports it as a visible color change from inside a gel."

"The aTc Demo combines the aTc Sensing Cell with Embed: Thermal Setting to produce gel-embedded synthetic cells that turn yellow to red when anhydrotetracycline reaches them."

When in doubt, read the existing Implementation pages. The four DevStudio demos — aTc, CRAIC, LuxR-GFP and pH — all follow the shape below.

:::{figure} ./resources/schematic-example-2.png
:name: fig-schematic
:align: center
:width: 75%

TODO: One sentence describing what the schematic shows. If the figure is not original, credit the source and include the license (e.g. "Figure by Author et al. used under CC-BY-4.0 / cropped from original.").
:::

# Modules

List the modules used in this implementation. Link each to its spec page. If a module is used in a non-standard configuration (different concentration, modified construct), note that here.

Modules come before Processes: a reader follows the parts to the operations performed on them.

- [TODO: Module Name](../../modules/TODO/spec.md)
- [TODO: Module Name](../../modules/TODO/spec.md)

# Processes

Link to the base Process this implementation follows. If this implementation deviates from the standard process (different volumes, modified steps, additional preparation), note that here.

- [TODO: Process Name](../../processes/TODO/main.md)

# Protocol as run

What was actually done, and what deviated from the Process pages linked above. This is a record of the procedure that was followed, not a procedure to follow — a reader who wants to run the protocol goes to the Process page. State the deviations: a substituted reagent, a changed incubation, a step skipped, an unplanned repeat.

A run that matched the linked Processes exactly can say so in one line. Do not restate the Process steps here.

*Under Construction*

# Observed Performance

Show what this implementation actually did in practice. Include representative data: time series, endpoint measurements, dose-response curves, or whatever characterizes the system's behavior. Each figure should have a caption that states the experimental conditions and links to the source DevNote. If performance varies across conditions (temperature, concentration, cytosol batch), show that. The goal is to let a reader judge whether this implementation fits their use case without having to reproduce the experiment first.

The boundary with the section above: `Protocol as run` is what was done, `Observed Performance` is what happened. A deviation from the planned protocol goes in the first; a number that came off an instrument goes in the second.

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

# Credits

<!-- List the people who developed or validated this implementation.
Link to ORCID or personal pages where available. -->

- [TODO: Name](https://orcid.org/TODO)
