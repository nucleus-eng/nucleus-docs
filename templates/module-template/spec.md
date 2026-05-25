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

:::::

# Reference Composition

Describe how the module is implemented and in what context (e.g., synthetic cytosol, cells, etc.). Lead with any non-obvious preparation or formulation context. The table should give a reader enough information to implement the module without hunting elsewhere. Use a hint dropdown for stock solution details that would clutter the main table. For example:

"The following table describes a self-contained experiment for evaluating the performance of the PPK energy module."

"The following table describes the composition of Base Membrane for a 40 µL cell reaction."

:::{hint} Note: TODO: Note title
:class: dropdown

<!-- Optional: stock solution concentrations, preparation details, or descriptions
of reaction conditions. Delete this block if not needed. -->

| Component | Stock concentration | Unit |
| --- | --- | --- |
| TODO: Component A | TODO | TODO |

:::

:::{table}
| **Component** | **Stock concentration** | **Final concentration** | **Units** |
| --- | --- | --- | --- |
| TODO: Component A | TODO | TODO | TODO |
| TODO: Component B | TODO | TODO | TODO |
| Water | — | — | to volume |
:::

# Expected Performance

Describe what a correctly implemented module should produce. Name the expected readout (fluorescence endpoint, gel band, growth curve), the conditions under which it was obtained, and acceptance criteria where known. The figures should show representative data from a validated experiment and cite the source DevNote. The goal is to give a reader a reference point so they can tell whether their own implementation is working correctly. For example:

"A correctly implemented PPK energy module should show ≥ 50% deGFP yield relative to a CP/CK positive control when supplemented at the recommended concentration."

"A correctly assembled Base Membrane should produce liposomes with distinct GFP-positive interiors and uniform Liss-Rhod PE membrane staining by fluorescence microscopy."

:::::{tab-set}

::::{tab-item} Kinetics
:sync: tab1-1
:::{figure} kinetics.png
:name: fig-kinetics
:align: center
:width: 75%

TODO: Describe what is shown, including conditions, controls, and the key result. Cite the source DevNote or paper. Example: "Translation kinetics of PURE reactions using the PPK energy module with and without CP/CK. Data from [TODO: DevNote title](https://doi.org/TODO)."
:::
::::

::::{tab-item} Endpoint
:sync: tab1-2
:::{figure} endpoint.png
:name: fig-endpoint
:align: center
:width: 75%

TODO: Describe the endpoint metric and key result. Example: "Final deGFP yields measured at steady state across energy module conditions. Data from [TODO: DevNote title](https://doi.org/TODO)."
:::
::::

:::::

# Protocols

<!-- Update filenames to match the actual PDFs for this module.
PDF generation pipeline is tracked in issue #10. -->

::::{grid} 1 1 1 2

:::{card}
:header: **Step-by-Step Protocol**
:footer: *Implemented using Nucleus Cytosol v0.5*
{button}`Download <TODO: protocol.pdf>`
:::

:::{card}
:header: **Materials**
:footer: *Implemented using Nucleus Cytosol v0.5*
{button}`Download <TODO: bom.pdf>`
:::

::::

# Credits

<!-- List the people who developed or validated this module.
Link to ORCID or personal pages where available. -->

- [TODO: Name](https://orcid.org/TODO)
