---
title: "Control: ClpXP"
subtitle: "Module Specification"
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The ClpXP control module enables the ATP-dependent, targeted degradation of ssrA-tagged proteins. It is based on the complex formed by the AAA+ ATPase ClpX and the tetradecameric peptidase ClpP. The module can be implemented using purified protein, *in situ* expressed proteins from DNA templates, or combinations thereof.

:::::{tab-set}

::::{tab-item} Schematic
:::{figure} mechanism-schematic.png
Cartoon of the general mechanism of protein degradation by ClpXP, an ATP-dependent protease. Adapted from [R. Wedam, et al.](https://doi.org/10.3390/cancers15071936)
:::
::::

::::{tab-item} Designs
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-ClpX` | N/A | Nucleus v0.5.0 Distribution Plate *(upcoming)* |
| `pT7-ClpP` | N/A | Nucleus v0.5.0 Distribution Plate *(upcoming)* |
| `pT7-deGFP-ssrA` | N/A | Nucleus v0.5.0 Distribution Plate *(upcoming)* |
::::

:::::

## Cytosols

### Usage

The module can be implemented from purified proteins alone, from *in situ* expressed proteins encoded on DNA templates, or from combinations thereof.

:::::{tab-set}

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

### Expected Performance

:::::{tab-set}

::::{tab-item} Purified Proteins
:::{figure} performance-purified-protein.png
GFP fluorescence of samples containing purified proteins incubated at 37°C for 4 hours. These results correspond to Reaction Table 1.
:::
::::

::::{tab-item} In Situ Expression
:::{figure} performance-insitu.png
GFP fluorescence signal produced using pT7-deGFP-ssrA DNA in PURE reactions incubated at 37°C for 6 hours. ClpX and ClpP DNAs are co-expressed in the same PURE reaction. These results correspond to Reaction Table 2.
:::
::::

:::::

## Cells

:::{attention}
Cell context implementation is under development. No cell-context performance data is currently available.
:::

:::{figure} clpxp-overview.png
The ClpXP Control Module in the context of the [Developer Cell](https://devnotes.nucleus.engineering/articles/developer-cell-introduction). Other Developer Cell Modules are grayed out.
:::

## References

- Hsu, Y. (2025). [ClpXP Module Validation in PURE](https://devnotes.nucleus.engineering/articles/bnext-devnotes-clpx-in-pure-01). *Nucleus Developer Notes.*
- Hsu, Y. (2025). [ClpXP Module Validation in Cells](https://devnotes.nucleus.engineering/articles/bnext-devnotes-clpxp-pure-cells-01). *Nucleus Developer Notes.*
- Wedam, R., Greer, Y. E., Wisniewski, D. J., Weltz, S., Kundu, M., Voeller, D., & Lipkowitz, S. (2023). Targeting Mitochondria with ClpP Agonists as a Novel Therapeutic Opportunity in Breast Cancer. *Cancers*, *15*(7), 1936. [10.3390/cancers15071936](https://doi.org/10.3390/cancers15071936)
