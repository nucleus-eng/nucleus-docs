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

The pH-Sensing Module produces a colorimetric signal in cell-free reactions when pH drops to about 6.5. The module has three parts: a pH-responsive single-strand DNA (ssDNA), a trigger ssDNA, and a linear toehold switch construct. At neutral pH, the trigger ssDNA stays bound to the pH-responsive ssDNA and the toehold switch blocks translation of a reporter enzyme. When pH drops to about 6.5, the trigger ssDNA releases and binds the toehold switch instead, which opens translation of the reporter enzyme. The reporter enzyme is either β-galactosidase (LacZ) or catechol 2,3-dioxygenase (XylE/C23DO), each paired with its own colorimetric substrate — CPRG for LacZ, catechol for XylE — to produce a visible color change.

The design follows [Chen, Hwang, et al., 2025](https://doi.org/10.1101/2025.11.16.688650). Target pH sensing is 6.5 ± 0.1, with a visible colorimetric response expected within 1 h.

:::{attention} Backing DevNote is a template stub
The formal DevNote for this module — [Module Development Plan: DevCell-based pH sensor](https://github.com/nucleus-eng/2026-CERN-OHL-P/blob/main/devnotes/chicago-ph-sensor-plan/main.md) (`chicago-ph-sensor-plan`, authors Samuel J. Chen and Sung-Won Hwang) — is a template stub, not a completed writeup. Its `title` field is still the literal placeholder `"[Title]"`, and it carries no populated figures, milestone completion notes, or dated results. This page draws on that DevNote's design description (components, milestones, reference citation) and combines it with quantitative results reported separately at the 2026-08-14 DevCell status meeting (see Expected Performance below), because the DevNote itself has not yet been filled in with that data. **This is a real documentation gap** — the module's formal DevNote should be populated with the meeting's results before this page is treated as fully sourced.
:::

:::{figure} schematic.png
:name: fig-schematic
:align: center
:width: 75%

Schematic of the pH-Sensing Module. At neutral pH, trigger ssDNA is bound to pH-responsive ssDNA and the toehold switch stays closed. At pH 6.5, trigger ssDNA releases and opens the toehold switch, allowing translation of a colorimetric reporter enzyme (LacZ or XylE).
:::

:::::{tab-set}

::::{tab-item} Designs
| **Name** | **Expected Concentration** | **Status** | **File** |
| --- | --- | --- | --- |
| `T7-toehold-LacZ-T7term` | 2 nM | Designed | — |
| `T7-toehold-XylE-T7term` | 2 nM | Designed | — |
| Trigger ssDNA | 4.8 µM | Synthesized | — |
| pH-responsive ssDNA | 14.4 µM | Synthesized | — |

:::{attention} Constructs not yet in `nucleus-eng/DNA`
None of the four constructs above have a corresponding file in [`nucleus-eng/DNA`](https://github.com/nucleus-eng/DNA) yet (checked `detectors/` and the repo root; none found). The DevNote lists them as "Designed" or "Synthesized" but does not link sequence files. Do not treat the names above as identity claims against any existing DNA-repo file — flag for follow-up so these constructs can be submitted to `nucleus-eng/DNA` before this page is used at the bench.
:::
::::

:::::

# Components

:::{table}
:name: components-critical-materials

| Material | Description | Manufacturer | Item # | Notes |
| --- | --- | --- | --- | --- |
| `T7-toehold-[LacZ/XylE]-T7term` | Reporter enzyme under a T7 promoter | — | — | See Designs above |
| CPRG / catechol | Colorimetric substrate for LacZ / XylE respectively | CPRG: Roche; Catechol: TCI America | CPRG: 10884308001; Catechol: P031725G | Catechol is a phenolic compound |
| POPC | Phospholipid for synthetic cell production | Avanti Polar Lipids | A80557C/0200/4C11M | — |
| Cholesterol | Membrane component for synthetic cell production | Sigma-Aldrich | C3045-5G | — |
| Gramicidin A | Proton channel for membrane pH equilibration | Sigma-Aldrich | 50845-5MG | Stock in DMSO, stored at -80 °C. Needed only for a liposome-encapsulated format — the bulk hydrogel result below does not use liposomes |
| Nucleus Cytosol | Cell-free expression system | b.next | — | — |

:::

**Membrane (for a future liposome-encapsulated format)**

:::{table}
:name: components-membrane

| Lipid | Volume fraction |
| --- | --- |
| POPC | 89.9% |
| Cholesterol | 10% |
| Rhod-PE | 0.1% |

:::

# Requirements

:::{warning}
**Trigger ssDNA purity and formulation strongly affect signal.** IDT-desalted ssDNA in water gave about 25,000 RFU, while HPLC-purified ssDNA in duplex buffer gave about 800,000 RFU — over 30× higher signal from the purification/formulation change alone. Use HPLC-purified ssDNA in duplex buffer; do not substitute desalted ssDNA in water without expecting a large drop in signal.
:::

## Cytosols

### Usage

Embed the reaction in 0.7% low-gelling agarose in place of a standard aqueous PURE or Nucleus Cytosol reaction. Add β-galactosidase (LacZ) reporter DNA with a neutralization buffer to set the target pH, then incubate at 37 °C.

### Expected Performance

A test (Sung-Won Hwang, Liu Lab), reported in DevCell status notes, embedded the pH-sensing reaction directly in 0.7% low-gelling agarose in a 96-well plate, added β-galactosidase with neutralization buffer, and incubated 5 h at 37 °C (with 13 h of Z-stack fluorescence imaging also collected at 37 °C). Absorbance at 570 nm at the 5 h timepoint:

| Condition | Abs₅₇₀ (5 h) |
| --- | --- |
| Positive control (Triton X) | ~0.46 |
| Negative control | ~0.31 |
| pH 7.4 | ~0.31 |
| pH 6.5 | ~0.39 |

:::{attention} Real but modest signal — not yet a robust reproduction
This is a genuine, concentration-dependent difference between pH 7.4 (~0.31) and pH 6.5 (~0.39), and the fluorescence channel showed no Cy5 dye signal at pH 6.5, consistent with reporter expression at the acidic condition. But the gap between the two pH conditions is small relative to the positive control (~0.46), and the presenter described the visible color change at the time as "slight pink" and "not as bright as I wanted," with an open plan to increase CPRG loading concentration. Treat this as a real, modest, concentration-dependent lead worth building on — not a robust or complete reproduction of the intended pH 6.5 ± 0.1 colorimetric response.
:::

## Cells

This module has not yet been demonstrated in a liposome-encapsulated or hydrogel-embedded synthetic cell format. The result above is a bulk agarose-hydrogel reaction without liposomes — a different, earlier step than embedding a pH Sensing Cell in the [Chicago Chassis](../chicago-chassis/spec.md).

:::{attention} Chicago Chassis integration is proposed, not confirmed
In the current module-integration diagram, the edge from the Chicago Chassis to the pH Sensing Cell is drawn dashed (proposed), not solid (confirmed). Hydrogel integration of this module remains early-stage: the bulk agarose result above shows a real signal, but liposome encapsulation and embedding in the Chicago Chassis have not been demonstrated. Do not represent this integration as confirmed elsewhere in the docs until that step is done.
:::
