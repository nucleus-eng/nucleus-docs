---
title: "Detector: pH-Sensing"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Overview

The pH-Sensing Detector turns acidic pH into expression of a downstream gene. Its design target is a drop in pH to about 6.5 ([Module Development Plan: DevCell-based pH sensor](https://devnotes.nucleus.engineering/articles/chicago-m1-5-1)). Two oligonucleotides do the sensing. The pH-responsive ssDNA is a triplex-forming strand: it releases the trigger ssDNA on acidification, and the annealing length between the two strands sets the pH at which the trigger is released ([Hwang et al., 2025](https://doi.org/10.1101/2025.11.16.688650)). At neutral pH the pH-responsive strand holds the trigger ([Module Development Plan: DevCell-based pH sensor](https://devnotes.nucleus.engineering/articles/chicago-m1-5-1)). A toehold switch RNA blocks translation of the downstream gene until the free trigger strand binds its toehold ([Module Development Plan: DevCell-based pH sensor](https://devnotes.nucleus.engineering/articles/chicago-m1-5-1)). A linear DNA template carries the toehold switch and the gene. In the documented instance the gene is phospholipase A1 (PLA1), on the same molecule as the toehold switch. The Detector is a constituent of the [pH Sensing Cell](../ph-sensing-cell/spec.md).

The signal that the Detector passes on is the released trigger strand. Protein expression downstream of the toehold switch is the output.

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{table} DNA of the pH-Sensing Detector.
:label: comp-detector-ph-dna

| Name | Length | Supply | File |
| --- | --- | --- | --- |
| `pH-responsive-ssDNA-2` | 49 nt | Single-stranded oligo, annealed with the trigger strand | [pH-responsive-ssDNA-2.gb](https://github.com/nucleus-eng/DNA/blob/f06e12cbc43da77dbb3c9d2d9a4ecc790fdd75b9/detectors/detector-ph/pH-responsive-ssDNA-2.gb) |
| `trigger-ssDNA-3` | 36 nt | Single-stranded oligo, annealed with the pH-responsive strand | [trigger-ssDNA-3.gb](https://github.com/nucleus-eng/DNA/blob/f06e12cbc43da77dbb3c9d2d9a4ecc790fdd75b9/detectors/detector-ph/trigger-ssDNA-3.gb) |
| `pT7-toehold9-PLA1-linear` | 1203 bp | Linear DNA template, added to the reaction at 2 nM | [pT7-toehold9-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/f06e12cbc43da77dbb3c9d2d9a4ecc790fdd75b9/effectors/detector-ph/pT7-toehold9-PLA1-linear.gb) |
:::

:::{attention}
@Editor: These files are on the `devcells/devstudio-constructs` branch of `nucleus-eng/DNA`, and the links are pinned to a commit on that branch. Point the links at `main` when the branch is merged.
:::
::::

::::{tab-item} Cytosol

:::{table} Components of the pH-Sensing Detector in a cell-free reaction, at the design concentrations of the [Module Development Plan: DevCell-based pH sensor](https://devnotes.nucleus.engineering/articles/chicago-m1-5-1). The pH-responsive strand and the trigger strand are annealed at 3:1 by mole before they are added.
:label: comp-detector-ph-cytosol

| Component | Design concentration |
| --- | --- |
| Trigger ssDNA | 4.8 µM |
| pH-responsive ssDNA | 14.4 µM |
| Toehold-switch DNA template | 2 nM |
:::

:::{attention}
@Developer: The design concentration of the trigger strand is 4.8 µM, and the toehold test below used 4.8 nM, a thousandth of it. Confirm the unit of each.
:::
::::

:::::

# Expected Behavior

## Cytosols

The toehold switch is expected to express the downstream gene only when the trigger strand is present. In Nucleus Cytosol at neutral pH, a linear toehold-pHtdGFP template at 2 nM expressed pHtdGFP gated by the presence of the trigger ssDNA, which was at 4.8 nM. GFP fluorescence was read in a plate reader over 6 h at 37 °C ([Toehold switch-enabled translation regulation verified in Nucleus Cytosol](https://devnotes.nucleus.engineering/articles/chicago-m1-5-2)).

:::{warning} Not yet validated
The test was preliminary and was done at neutral pH. Expression in response to acidic pH is not reported for the Detector alone in Nucleus Cytosol. It is reported for the [pH Sensing Cell](../ph-sensing-cell/spec.md).
:::

:::{attention}
@Editor: No Process page documents the plate-reader GFP readout.
:::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)).

# Implementations

- [Colorimetric pH Sensor](../../implementations/colorimetric-ph-sensor/main.md)

# Processes

- [Anneal pH Trigger Duplex](../../processes/anneal-ph-trigger-duplex/main.md) anneals the pH-responsive strand and the trigger strand.

# Credits

Developed by [Sung-Won Hwang](https://orcid.org/0000-0003-1686-7090), [Samuel Chen](https://orcid.org/0000-0001-8501-7175) and [Allen P. Liu](https://orcid.org/0000-0002-0309-7018) (University of Michigan).

:::{attention}
@Editor: Add the Node and Lab to this credit.
:::
