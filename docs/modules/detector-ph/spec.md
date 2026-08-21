---
title: "Detector: pH-Sensing"
subtitle: "Module Specification"
status: unvalidated-published
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The pH-Sensing Module drives expression of an effector gene in acidic conditions (pH ≤ 6.5). The module has three parts: (1) a pH-responsive single-strand DNA (ssDNA), (2) a trigger ssDNA, and (3) a linear toehold-switch DNA construct. At neutral pH, the trigger ssDNA stays bound to the pH-responsive ssDNA and the toehold switch remains off, preventing expression of the effector gene. At acidic pH, the pH responsive ssDNA releases the trigger ssDNA, which then binds the toehold switch, activating expression of the effector gene. The design follows [Chen, Hwang, et al., 2025](https://doi.org/10.1101/2025.11.16.688650). 

:::{figure} schematic.png
:name: fig-schematic
:align: center
:width: 75%

Schematic of the pH-Sensing Module. At neutral pH, trigger ssDNA is bound to pH-responsive ssDNA and the toehold switch stays closed. At acidic pH, trigger ssDNA releases and opens the toehold switch, allowing translation of the effector gene (e.g., a colormetric reporter). @Claude this diagram needs a citation. Where did you find it?
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} Schematic
@Claude: see [spec](../detector-theophylline/spec.md) Schematic spec as an example. notice: boxes are ONLY physical objects, and arrows represent processes. Seems like it's gonna at least have the following nouns: pH-responsive ssDNA, trigger ssDNA, toehold-switch, effector gene.
::::

::::{tab-item} DNA

| **Name**                 | **Expected Concentration** | **Status**  | **File** |
| ------------------------ | -------------------------- | ----------- | -------- |
| `T7-toehold-LacZ-T7term` | 2 nM                       | Designed    | —        |
| `T7-toehold-XylE-T7term` | 2 nM                       | Designed    | —        |
| Trigger ssDNA            | 4.8 µM                     | Synthesized | —        |
| pH-responsive ssDNA      | 14.4 µM                    | Synthesized | —        |

:::{attention} Constructs not yet in `nucleus-eng/DNA`
None of the four constructs above have a corresponding file in [`nucleus-eng/DNA`](https://github.com/nucleus-eng/DNA) yet (checked `detectors/` and the repo root; none found). The DevNote lists them as "Designed" or "Synthesized" but does not link sequence files. Do not treat the names above as identity claims against any existing DNA-repo file — flag for follow-up so these constructs can be submitted to `nucleus-eng/DNA` before this page is used at the bench.
:::
::::

::::{tab-item} Cytosol Composition
@Claude: this needs a cytosol composition table. see [spec](../detector-theophylline/spec.md) :label: comp-theophyllie-sensor for an example. Here, there isn't a (+) and a (-) condition.
::::

:::::


# Expected Behavior

Target pH sensing is 6.5 ± 0.1, with effector gene expression expected within 1 h. 

@Claude: check if there's any data on using the pH Sensing module in synthetic cytosols or cells. 
### Cytosols

:::{warning}
This module has not yet been demonstrated in a synthetic cytosol.
:::
### Cells

:::{warning}
This module has not yet been demonstrated in a synthetic cell.
:::
### Gels

Embed the reaction in 0.7% low-gelling agarose in place of Cytosol. Add β-galactosidase (LacZ) reporter DNA with a neutralization buffer to set the target pH, then incubate at 37 °C for 5 h. Measure absorbance at 570 nm 

| Condition                   | Abs₅₇₀ (5 h) |
| --------------------------- | ------------ |
| Positive control (Triton X) | ~0.46        |
| Negative control            | ~0.31        |
| pH 7.4                      | ~0.31        |
| pH 6.5                      | ~0.39        |


# Requirements

Requires pT7 transcription and translation (e.g., [Base Cytosol](/docs/mo/base-cytosol/spec)). @Claude: this requirement is true of almost all Cytosolic modules. All modules that implicitly require Cytosol SHOULD get this line.

Requires direct exposure to pH source. Either do not encapsulate OR include H+ ion transport across the membrane (e.g., Gramicidin A).

:::{attention}
**Trigger ssDNA purity and formulation strongly affects signal.** IDT-desalted ssDNA in water gave about 25 000 RFU, while HPLC-purified ssDNA in duplex buffer gave about 800 000 RFU (>30×). (@Claude: what's duplex buffer? add to questionnaire if you can't find it)
:::

# Implementations
No Implementations exists yet.

# Materials

:::{table}
:name: critical-materials

(@Claude: this critical components table is good! May be good to have these in module pages. Flag for discussion w.r.t. editing module templates and harmonizing existing pages.)

| Material                                            | Description                                            | Manufacturer                       | Item #                                             | Notes                                                               |
| --------------------------------------------------- | ------------------------------------------------------ | ---------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------- |
| DNA template (e.g., `T7-toehold-LacZ`)              | Effector gene under a T7 promoter with toehold switch. | —                                  | —                                                  | See Designs above                                                   |
| CPRG / catechol (@Claude: this should be two lines) | Colorimetric substrate for LacZ / XylE respectively    | CPRG: Roche; Catechol: TCI America | CPRG: 10884308001; Catechol: P031725G              | —                                                                   |
| POPC                                                |                                                        | Avanti Polar Lipids                | A80557C/0200/4C11M (@Claude: only one part number) | —                                                                   |
| Cholesterol                                         | Membrane component for synthetic cell production       | Sigma-Aldrich                      | C3045-5G                                           | —                                                                   |
| Gramicidin A                                        | Proton channel for membrane pH equilibration           | Sigma-Aldrich                      | 50845-5MG                                          | Stock in DMSO, stored at -80 °C. Needed for use in synthetic cells. |
| [Base Cytosol](../base-cytosol/spec.md)             | Cell-free expression system                            | —                                  | —                                                  | —                                                                   |

:::

# Credits
@Claude: wrangle the credits for this page

Sung-Won Hwang (Liu Lab) - Gel embedding.