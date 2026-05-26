---
title: "TODO: Category: Module Name"
# Title format: "Category: Name" — e.g. "Reporter: deGFP", "Energy: PPK", "Base: Cytosol"
subtitle: "Module Specification"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

One paragraph. State what the module is, what it does, and what it adds to or modifies in Base Cytosol. Lead with the module name and its function. Include the key parameters that define its function (e.g., substrate, pore diameter, purification tag, excitation wavelength). Use precise terms. Don't open with preamble. Just start with the thing:

"The PPK energy Module generates ATP and GTP from AMP and GDP, respectively, using inorganic polyphosphate (100mer) as a phosphate donor."

"The ClpXP control Module uses the ClpXP protease complex to enable the programmable degradation of ssrA-tagged target proteins using ATP for energy."

When in doubt, read the existing Module specs.

<!-- If this module has not been validated in Nucleus Cytosol ≥ v0.5, include the
attention block below. Delete it if the module is fully validated. -->

:::{attention}

This Module has not been validated in Nucleus Cytosol $\ge$ v0.5. Documentation can be found on our legacy site [TODO: update link]() and in the following DevNotes:

- [TODO: DevNote Title](https://doi.org/TODO)

:::

:::{figure} schematic.png
:name: fig-schematic
:align: center
:width: 75%

TODO: One sentence describing what the schematic shows. If the figure is not original, credit the source and include the license (e.g. "Figure by Author et al. used under CC-BY-4.0 / cropped from original.").
:::

:::::{tab-set}

::::{tab-item} Designs
<!-- Two tables: one for DNA constructs, one for purified protein components.
Delete whichever is not applicable and replace with "- None".
DNA files link to .gb files in the nucleus GitHub repository.
Protein files link to sequence files (.fasta, .gb) or expression constructs. -->

**DNA**

:::{table}
| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `TODO: pConstruct-Name` | TODO | [TODO: filename.gb](https://github.com/bnext-bio/nucleus/blob/main/TODO) |
:::

**Proteins**

:::{table}
| **Name** | **MW (kDa)** | **File** |
| --- | --- | --- |
| `TODO: ProteinName-Tag` | TODO | [TODO: filename.fasta](https://github.com/bnext-bio/nucleus/blob/main/TODO) |
:::
::::

::::{tab-item} Maps
<!-- Sequence maps for the constructs listed in the Designs tab.
One figure per construct. Generated from .gb files using Benchling, SnapGene, or equivalent. -->

:::{figure} TODO: map.png
:name: fig-map
:align: center
:width: 75%

TODO: `pConstruct-Name`. Brief description of key features (promoter, insert, selection marker). Generated from [TODO: filename.gb](https://github.com/bnext-bio/nucleus/blob/main/TODO).
:::
::::

:::::

# Properties

Key intrinsic properties of this module sourced from databases, literature, or supplier datasheets. Include only values that are independent of experimental context — things you would find in a reference database or datasheet. For example:

| Property | Value | Source |
| --- | --- | --- |
| TODO: Excitation max (nm) | TODO | TODO |
| TODO: Emission max (nm) | TODO | TODO |
| TODO: MW (kDa) | TODO | TODO |

# Implementations

List the Implementations that use this Module. Link each to its page.

- [TODO: Implementation Name](../../implementations/TODO/implementation-template.md)

# References

<!-- Intrinsic properties cited in the Overview — database entries, primary literature, supplier datasheets.
Use numbered references or inline links as appropriate. -->

- TODO: Author et al. (YYYY). *Title*. Journal. [https://doi.org/TODO](https://doi.org/TODO)

# Credits

<!-- List the people who developed or validated this module.
Link to ORCID or personal pages where available. -->

- [TODO: Name](https://orcid.org/TODO)
