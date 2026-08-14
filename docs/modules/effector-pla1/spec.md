---
title: "Effector: PLA1"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The PLA1 Lysis Module uses phospholipase A1 (PLA1) as a genetically encoded lysis trigger. Once expressed inside a vesicle, PLA1 degrades the vesicle's own phospholipid membrane, rupturing it. In every DevCells cascade that uses it, this self-lysis also breaches a neighboring, dye-loaded vesicle, releasing a chromogenic substrate (chlorophenol red-β-D-galactopyranoside, CPRG, or catechol) into an external reporter-enzyme solution and starting a colorimetric readout. PLA1 supplies the lysis step only — it is not itself a sensor or a reporter. It sits downstream of a sensing circuit (a theophylline riboswitch, a pH-responsive toehold switch, a TetO/aTc promoter, or a LuxR/pLux quorum-sensing promoter) that controls when it is expressed, and upstream of a reporter enzyme (typically LacZ, occasionally XylE/C23DO) that produces the visible signal.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Documentation gap — no dedicated PLA1 devnote
No PLA1-specific devnote with primary experimental data exists yet — this is a known documentation gap. This page is built by inference from the cascades that use PLA1 as their shared lysis-triggering component: `chicago-teto-catecholase` and `london-lacz-xyle-module` document the sensing and reporter chemistry paired with PLA1 in those cascades, but neither devnote describes PLA1 itself. See [Known Implementations](#known-implementations) below for how each cascade uses it, and the [tetR-aTc Detector Module](../detector-tetr_atc/spec.md) spec for the one PLA1-encapsulation result with primary (if interim) data behind it. Treat everything on this page as inferred/interim until a dedicated PLA1 devnote is written.
:::

:::::{tab-set}

::::{tab-item} Schematic
```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    A["Inducer<br/>(theophylline / pH / aTc / AHL)"] --> B["Sensing circuit<br/>(riboswitch, toehold switch,<br/>TetO/aTc, or LuxR/pLux)"]
    B --> C["PLA1 expressed<br/>inside its own vesicle"]
    C --> D["PLA1 degrades that vesicle's<br/>own phospholipid membrane"]
    D --> E["Vesicle ruptures, breaching a<br/>neighboring substrate-loaded vesicle"]
    E --> F["Chromogenic substrate released<br/>(CPRG or catechol)"]
    F --> G["External reporter enzyme<br/>(LacZ or XylE/C23DO)"]
    G --> H["Colorimetric readout"]
```

No published schematic exists for this mechanism; the diagram above is a simplified summary, not a reproduction of a lab figure.
::::

::::{tab-item} Designs
:::{attention} Not yet in `nucleus-eng/DNA`
Source material names two PLA1 constructs — a constitutive/riboswitch-gated `T7pro-PLA1-T7term` used in Chicago's PURE-based theophylline and pH cascades, and a LuxR/pLux-controlled `P70lux-PLA1-term` used in London's PURE/lysate AHL cascade — but neither has a confirmed sequence file in [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA). Sequence files are reported to already exist on Nucleus Hub; the pending step is linking them into a shared materials spreadsheet, not a docs-side branch of the DNA repo. Do not add a Designs-table row here until a file lands in `nucleus-eng/DNA` and its identity is confirmed against this row's construct name — flag the gap to Surendra (tracking sequence files via Nucleus Hub / the shared materials spreadsheet) rather than guessing at a filename.
:::
::::

:::::

# Known Implementations

PLA1 lyses a vesicle in every DevCells cascade that needs a two-vesicle colorimetric handoff. None of these are documented in a PLA1-specific devnote — each is described in the sensing or reporter devnote for that cascade, with PLA1's role inferred from the cascade's overall behavior.

- **Chicago theophylline cascade.** A theophylline riboswitch (Lynch & Gallivan design) gates PLA1 expression. PLA1 ruptures its own GUV and a neighboring CPRG-loaded GUV, releasing CPRG to an external LacZ solution and producing a visible color change after ~16 h in an alginate hydrogel. Confirmed at the GUV/hydrogel level, with a known caveat: the color change currently occurs with or without theophylline present (riboswitch leak), so target specificity is not yet solved.
- **Chicago pH cascade.** A pH-responsive toehold switch gates PLA1. The same two-vesicle CPRG/LacZ handoff produces a visible yellow-to-purple change at pH 6.5 in solution. Confirmed at the solution level only; not yet moved into the hydrogel-embedded chassis.
- **Chicago aTc cascade.** See the [tetR-aTc Detector Module](../detector-tetr_atc/spec.md) spec, "Chicago Cascade Encapsulation (TetO-PLA1 / LacZ-CPRG Readout)" section: a `TetO-PLA1` construct is co-encapsulated with LacZ and CPRG substrate in a GUV, showing a confirmed graded absorbance response to aTc dose. This is currently the only PLA1 result with primary (if interim) supporting data behind it, rather than a description inferred purely from cascade-level behavior.
- **London AHL cascade.** A LuxR/pLux quorum-sensing promoter gates PLA1 expression in S30 lysate. PLA1 lysis again triggers the CPRG/LacZ handoff. As of the latest report, this shows a discernible but still leaky difference in color change between +AHL and −AHL conditions; the team is optimizing DNA and AHL concentrations to widen this gap.

:::{attention} Interim source — formal devnote pending
The cascade summaries above are sourced from the Chicago and London Module Integration Status notes and the 2026-08-14 DevCell Studio status meeting ("August DevCell Status Update"). Treat these as interim primary sources, not as validated Module-level performance data for PLA1 itself.
:::

# Composition & Usage

:::{attention} Only one cascade has PLA1-specific numbers
Of the four cascades in [Known Implementations](#known-implementations), only the Chicago aTc cascade's encapsulation result gives concentrations for the PLA1 construct itself. The theophylline, pH, and AHL cascade devnotes describe the paired sensing/reporter chemistry (riboswitch, toehold switch, LuxR/pLux, LacZ/XylE, CPRG/catechol) in quantitative detail but do not report a DNA, protein, or timing value for PLA1 itself — the PLA1 step in those cascades is described only qualitatively ("PLA1 ruptures its own GUV..."). That is a genuine documentation gap: no PLA1-specific reaction data exists independent of the cascades that use it.
:::

The table below is built from the "Chicago Cascade Encapsulation (TetO-PLA1 / LacZ-CPRG Readout)" section of the [tetR-aTc Detector Module spec](../detector-tetr_atc/spec.md#chicago-cascade-encapsulation-teto-pla1-lacz-cprg-readout) — the only source with primary (if interim) numbers for a PLA1 construct's own expression conditions, as opposed to whole-cascade description.

:::{table} TetO-PLA1 encapsulation parameters — Chicago aTc cascade (2026-08-14)
:name: pla1-chicago-encapsulation

| Parameter | Value | Notes |
| --- | --- | --- |
| Construct | `TetO-PLA1` | Distinct from `pT7-tetO-plamGFP` used elsewhere in the tetR-aTc Detector Module |
| DNA concentration tested | 1 nM or 0.5 nM | Three DNA/TetR combinations tested; see below |
| TetR concentration tested | 50 nM or 100 nM | Co-encapsulated repressor |
| aTc inducer dose range | 0, 1, 5, 10 µM | Graded dose-response confirmed across all three DNA/TetR combinations |
| Co-encapsulated reporter | LacZ + CPRG substrate | Same GUV as the `TetO-PLA1` construct |
| Readout | Absorbance at 575 nm | Colorimetric, via the LacZ/CPRG reaction |
| Validation level | Solution/GUV only | Hydrogel integration has not been completed. |

:::

# Requirements

PLA1 is a lysis effector, not a standalone module — it only produces an observable effect when paired with a sensing circuit and a downstream reporter/substrate vesicle. Premature lysis is a known failure mode: the Chicago pH cascade uses a gramicidin A proton channel specifically to prevent the PLA1-carrying vesicle from rupturing before its sensing circuit fires, and removing gramicidin A causes background color development from acid-driven leakage. Any implementation adding PLA1 to a new cascade should account for this premature-lysis risk rather than assuming the vesicle stays intact until the intended trigger.

# Known Future Work

:::{attention} Separate gap — not the same issue as PLA1 documentation
This is about mitigating **exterior** LacZ leakage, not PLA1's lysis function (covered above).
:::

A proteinase K treatment (50 °C/10 min, then 40 °C/1 h, then spin down) mitigates exterior LacZ leakage in cascades that use PLA1. It is documented as its own process page: [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md).

:::{attention} Documentation gap
Proteinase K concentration, reaction volume, and buffer are not specified in available source material.
:::

# Credits

Contributor attribution is pending confirmation. Source material names Jonah McDonald and Charlie Newell (London node) in connection with the PLA1-based colour-change module, and Mary Kelly (Kamat Lab, Chicago node) in connection with the TetO-PLA1/LacZ encapsulation result cited above — but neither is yet backed by a published devnote, so this page does not assert formal authorship.
