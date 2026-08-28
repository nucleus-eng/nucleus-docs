---
title: "Control: ClpXP"
subtitle: "Module Specification"
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The ClpXP control module enables the ATP-dependent, targeted degradation of ssrA-tagged proteins [McGinness, Baker, and Sauer, 2006](https://doi.org/10.1016/j.molcel.2006.04.027). It is based on the complex formed by the AAA+ ATPase ClpX and the tetradecameric peptidase ClpP. The module can be implemented using purified protein, *in situ* expressed proteins from DNA templates, or combinations thereof.

:::{figure} mechanism-schematic.png
Cartoon of the general mechanism of protein degradation by ClpXP, an ATP-dependent protease. Adapted from  [R. Wedam, et al.](https://doi.org/10.3390/cancers15071936)
:::

# Reference Composition

The module can be implemented from purified proteins alone, from *in situ* expressed proteins encoded on DNA templates, or from combinations thereof.

:::::{tab-set}

::::{tab-item} DNA
:::{table}
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-ClpX` | 3394 | [pOpen-ClpX-CHis.gb](https://github.com/nucleus-eng/DNA/blob/main/control/pOpen-ClpX-CHis.gb) |
| `pT7-ClpP` | 2746 | [pOpen-ClpP-CHis.gb](https://github.com/nucleus-eng/DNA/blob/main/control/pOpen-ClpP-CHis.gb) |
| `pT7-deGFP-ssrA` | 2863 | [pOpen-deGFP-CHis-ssrA.gb](https://github.com/nucleus-eng/DNA/blob/main/control/pOpen-deGFP-CHis-ssrA.gb) |
:::
::::

::::{tab-item} Purified Proteins
**Reaction Table 1.** The control module implemented from purified proteins. Volumes in µL.

| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Control** |
| --- | --- | --- | --- | --- |
| Purified deGFP-ssrA (41.2 µM) | 0.5 | 0.5 | 0.5 | 0.5 |
| Purified ClpP (79.9 µM) | 0.5 | 0.5 | 0 | 0 |
| Purified ClpX (53.7 µM) | 0.5 | 0 | 0.5 | 0 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1 | 1.5 | 1.5 | 2 |
| **Total** | **10** | **10** | **10** | **10** |
::::

::::{tab-item} In Situ Expression
**Reaction Table 2.** The control module implemented from *in situ* expressed proteins. Steady-state levels can be tuned by varying the concentration of *in situ* expressed ClpXP proteins. Volumes in µL.

| **Component** | **Sample 1** | **Sample 2** | **Sample 3** | **Sample 4** |
| --- | --- | --- | --- | --- |
| pT7-deGFP-ssrA (63.5 ng/µL) | 0.5 | 0.5 | 0.5 | 0.5 |
| pT7-ClpP (17.5 ng/µL) | 0.4 | 0.4 | 0.6 | 0.8 |
| pT7-ClpX (17.5 ng/µL) | 0.4 | 0.4 | 0.6 | 0.8 |
| NEB PURExpress Solution A | 4 | 4 | 4 | 4 |
| NEB PURExpress Solution B | 3 | 3 | 3 | 3 |
| RNase Inhibitor | 0.5 | 0.5 | 0.5 | 0.5 |
| Nucleus Free Water | 1.6 | 1.2 | 0.8 | 0.4 |
| **Total** | **10** | **10** | **10** | **10** |
::::

:::::

# Expected Behavior

## Cytosols

Module performance in PURE is documented in the DevNote [ClpXP Module Validation in PURE](https://devnotes.nucleus.engineering/articles/bnext-devnotes-clpx-in-pure-01).

:::::{tab-set}

::::{tab-item} Purified Proteins
:::{figure} performance-purified-protein.png
GFP fluorescence of samples containing purified proteins incubated at 37 °C for 4 h. These results correspond to Reaction Table 1.
:::
::::

::::{tab-item} In Situ Expression
:::{figure} performance-insitu.png
GFP fluorescence signal produced using pT7-deGFP-ssrA DNA in PURE reactions incubated at 37 °C for 6 h. ClpX and ClpP DNAs are co-expressed in the same PURE reaction. These results correspond to Reaction Table 2.
:::
::::

:::::

## Cells

:::{figure} clpxp-overview.png
The ClpXP Control Module in the context of the [Developer Cell](https://devnotes.nucleus.engineering/articles/developer-cell-introduction). Other Developer Cell Modules are grayed out.
:::

Cell-context validation of the ClpXP module is documented in the DevNote [ClpXP Module Validation in Cells](https://devnotes.nucleus.engineering/articles/bnext-devnotes-clpxp-pure-cells-01).

Three liposome populations were prepared to test whether the control module functions inside a synthetic cell. All three encapsulated purified deGFP-ssrA together with the PURE system. The first also encapsulated two linear DNAs, `pT7-ClpX` and `pT7-ClpP`; the second encapsulated `pT7-ClpP` DNA with purified ClpX protein; the control contained no DNA.

Liposomes containing functional ClpXP — whether assembled from two co-encapsulated DNAs or from DNA plus purified protein — show a clear decrease in green fluorescence over the incubation. Liposomes carrying both `pT7-ClpX` and `pT7-ClpP` degrade GFP more slowly than those carrying only `pT7-ClpP` with purified ClpX, which is consistent with competition for limited transcription and translation resources when several DNAs share one PURE reaction. Control liposomes show no substantial decrease; the slight reduction that does appear is most likely photobleaching. Expect a modest rise in green fluorescence over the first ~20 min, which reflects liposomes settling to the bottom of the imaging well rather than a change in expression.

<!-- TODO: move to process page — imaging conditions (488 channel, 200 ms exposure, 40% intensity, 460–490 nm excitation, 500–550 nm emission) are protocol-level detail and belong in a Process page, not this spec. -->

:::::{tab-set}

::::{tab-item} ClpXP — two DNAs
:::{figure} cell-clpxp-2dna.png
:name: fig-clpxp-cell-2dna

Time-series fluorescence microscopy of liposomes encapsulating `pT7-ClpX` and `pT7-ClpP` DNA with purified deGFP-ssrA, incubated at 37 °C. Green fluorescence decreases over time.
:::
::::

::::{tab-item} ClpXP — one DNA
:::{figure} cell-clpxp-1dna.png
:name: fig-clpxp-cell-1dna

Time-series fluorescence microscopy of liposomes encapsulating `pT7-ClpP` DNA with purified ClpX and purified deGFP-ssrA, incubated at 37 °C. Green fluorescence decreases faster than in the two-DNA condition.
:::
::::

::::{tab-item} Control — no DNA
:::{figure} cell-control-nodna.png
:name: fig-clpxp-cell-control

Time-series fluorescence microscopy of control liposomes encapsulating purified deGFP-ssrA only, incubated at 37 °C. Fluorescence stays substantially stable.
:::
::::

::::{tab-item} Single Cell Intensity Histograms

:::{figure} cell-intensity-histograms.png
:name: fig-clpxp-cell-histograms
:align: center
:width: 90%

Time-resolved histograms of mean GFP fluorescence intensity for individual liposomes, at 0, 45, 90, 135, 180, and 225 min. **Top row:** both ClpX and ClpP DNA. **Middle row:** a single ClpXP DNA component. **Bottom row:** control liposomes lacking ClpXP. A persistent high-intensity subpopulation appears in all three conditions.


Quantifying single-liposome GFP intensity as time-resolved histograms reproduces the same trend: in ClpXP-containing liposomes the distribution shifts progressively toward lower intensity, while control liposomes hold steady. A small subpopulation of highly fluorescent liposomes persists in every condition, including the ClpXP ones — most likely liposomes that failed to encapsulate functional ClpXP during formation.
:::

::::
:::::

# Requirements

Requires ATP and ssrA-tagged protein targets. Using DNA components additionally requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)). 

# Credits

Developed by [Yen-Yu Hsu](https://orcid.org/0000-0003-0866-6184) (b.next).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
