---
title: "pH Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

(ph-cascade-overview)=
# Overview

The pH Cascade combines the [pH Sensing Cell](../ph-sensing-cell/spec.md) with the [PLA1 Lysis Module](../effector-pla1/spec.md) and the [LacZ Reporter Module](../reporter-lacz/spec.md) to turn a drop in pH into a visible colorimetric readout. The pH Sensing Cell's toehold switch gates expression of PLA1, which lyses its own liposome and a neighboring CPRG-loaded liposome. The released CPRG reacts with LacZ in the exterior solution upon contact to produce the yellow-to-purple color change. Compare with the [aTc Cascade](../atc-cascade/spec.md), which releases the encapsulated enzyme into an outer solution with the substrate instead.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

(ph-cascade-reference-composition)=
# Reference Composition

The pH Cascade combines its Modules as follows:

- **Sensing input:** [pH Sensing Cell](../ph-sensing-cell/spec.md) — the pH-responsive toehold switch encapsulated in the Chicago Chassis synthetic cell, gating downstream expression at pH ≈ 6.5.
- **Lysis trigger:** [PLA1 Lysis Module](../effector-pla1/spec.md) — expressed once the pH switch fires; ruptures its own liposome and a neighboring CPRG-loaded liposome, coupling sensing to readout.
- **Colorimetric readout:** [LacZ Reporter Module](../reporter-lacz/spec.md) — reacts with the released CPRG substrate to produce the visible yellow-to-purple color change.

The combined three-part chain is specified here.

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    BASE_CYTOSOL["Base Cytosol"]
    DETECTOR_PH["Detector: pH-Sensing"]
    EFFECTOR_PLA1["Effector: PLA1"]
    MEMBRANE_POPC_CHOL_CHICAGO["Chicago Membrane: POPC/Chol"]
    PH_CASCADE["pH Cascade"]
    PH_SENSING_CELL["pH Sensing Cell"]
    PH_SENSOR_CYTOSOL["pH Sensor Cytosol"]
    REPORTER_LACZ_ENZYME["Reporter: LacZ Enzyme"]
    SUBSTRATE_CPRG_SUV["Substrate SUV: CPRG"]

    PH_SENSING_CELL --> PH_CASCADE
    REPORTER_LACZ_ENZYME --> PH_CASCADE
    SUBSTRATE_CPRG_SUV --> PH_CASCADE
    PH_SENSOR_CYTOSOL --> PH_SENSING_CELL
    MEMBRANE_POPC_CHOL_CHICAGO --> PH_SENSING_CELL
    BASE_CYTOSOL --> PH_SENSOR_CYTOSOL
    DETECTOR_PH --> PH_SENSOR_CYTOSOL
    EFFECTOR_PLA1 --> PH_SENSOR_CYTOSOL

    classDef constituent fill:#6B7280,color:#ffffff,stroke:#4B5563;
    classDef this fill:#374151,color:#ffffff,stroke:#111827;
    class BASE_CYTOSOL,DETECTOR_PH,EFFECTOR_PLA1,MEMBRANE_POPC_CHOL_CHICAGO,PH_SENSING_CELL,PH_SENSOR_CYTOSOL,REPORTER_LACZ_ENZYME,SUBSTRATE_CPRG_SUV constituent;
    class PH_CASCADE this;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click DETECTOR_PH "/docs/modules/detector-ph/spec"
    click EFFECTOR_PLA1 "/docs/modules/effector-pla1/spec"
    click MEMBRANE_POPC_CHOL_CHICAGO "/docs/modules/membrane-popc-chol-chicago/spec"
    click PH_CASCADE "/docs/modules/ph-cascade/spec"
    click PH_SENSING_CELL "/docs/modules/ph-sensing-cell/spec"
    click PH_SENSOR_CYTOSOL "/docs/modules/ph-sensor-cytosol/spec"
    click REPORTER_LACZ_ENZYME "/docs/modules/reporter-lacz-enzyme/spec"
    click SUBSTRATE_CPRG_SUV "/docs/modules/substrate-cprg-suv/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

:::{table}
| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| Toehold-switch-gated PLA1 template | 1203 | [pT7-toehold9-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/effectors/detector-ph/pT7-toehold9-PLA1-linear.gb) | Expressed in the pH Sensing Cell |
| pH-responsive ssDNA | 49 | [pH-responsive-ssDNA-2.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/detector-ph/pH-responsive-ssDNA-2.gb) | Synthesized oligonucleotide, added directly |
| trigger ssDNA | 36 | [trigger-ssDNA-3.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/detector-ph/trigger-ssDNA-3.gb) | Synthesized oligonucleotide, added directly |
:::

See [Detector: pH-Sensing](../detector-ph/spec.md) for the toehold-switch design and [Effector: PLA1](../effector-pla1/spec.md) for the PLA1 constructs.


::::

::::{tab-item} pH Sensing Cell

The pH-sensing ssDNA and the toehold-switch-gated PLA1 template are co-encapsulated in one liposome, in [Base Cytosol](../base-cytosol/spec.md).

:::{table} pH Sensing Cell cytosol, confirmed solution-phase integration path.
:label: comp-ph-cascade-sensing

| Component | Working concentration |
| --- | --- |
| pH-responsive ssDNA : trigger ssDNA (3:1, annealed) | 4.625 µM trigger ssDNA, final |
| Toehold-switch-gated PLA1 DNA template | 2 nM, final — a distinct, PLA1-fused construct |
| Base Cytosol components | At reaction concentration; not separately documented for this pairing |
:::

:::{table} pH Sensing Cell membrane — [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md).
:label: comp-ph-cascade-sensing-membrane

| Component | Target percentage (%) |
| --- | --- |
| POPC | 89.9 |
| Cholesterol | 10 |
| Liss-Rhod PE | 0.1 |
:::

::::

::::{tab-item} Substrate SUV

A second liposome population carrying the chromogenic substrate. See [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md).

:::{table} Substrate SUV lumen.
:label: comp-ph-cascade-suv

| Component | Working concentration |
| --- | --- |
| CPRG substrate | Not documented at a reaction concentration for this two-liposome pairing |
:::

:::{table} Substrate SUV membrane — [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md).
:label: comp-ph-cascade-suv-membrane

| Component | Target percentage (%) |
| --- | --- |
| POPC | 89.9 |
| Cholesterol | 10 |
| Liss-Rhod PE | 0.1 |
:::

::::

::::{tab-item} Outer Solution

:::{table} Outer solution.
:label: comp-ph-cascade-outer

| Component | Working concentration |
| --- | --- |
| H⁺ | pH 7.4 at rest; a drop to ≈ 6.5 opens the toehold switch |
| β-galactosidase (LacZ) | Not reported for this cascade configuration; see [LacZ Reporter](../reporter-lacz/spec.md) |
:::

LacZ sits out here rather than with its substrate; see [Overview](#ph-cascade-overview) for why.

::::

:::::

# Expected Behavior

The pH Cascade is expected to turn a drop to pH ≈ 6.5 into a visible yellow-to-purple color change: the toehold switch opens, PLA1 is expressed, and lysis releases CPRG from the substrate population to LacZ in the exterior solution.

## Cells

- **pH-sensing color change, solution-phase, two-liposome system:** a visible yellow-to-purple color change at pH 6.5, using separate pH-sensing and CPRG-loaded liposome populations in solution. See [pH Sensing Cell](../ph-sensing-cell/spec.md#ph-sensing-cell-expected-behavior) for detail.
- **PLA1-driven lysis coupling to CPRG/LacZ readout:** confirmed at the solution level for the Chicago pH cascade — see [PLA1 Lysis Module](../effector-pla1/spec.md#effector-pla1-implementations), "Chicago pH cascade."

:::{warning} Not yet validated as a combined cascade
The three Modules above have run in partial combinations, never together in one format. The pH Sensing Cell's own integration into the Chicago Chassis synthetic cell and hydrogel format is itself proposed rather than confirmed — see [pH Sensing Cell](../ph-sensing-cell/spec.md).
:::

## Gels

- **pH-sensing, bulk hydrogel, no liposomes:** embedding the pH-sensing reaction directly in 0.7% low-gelling agarose gives a real but modest color change — "slight pink," not as bright as expected (Sung-Won Hwang, Liu Lab). The concentration-dependent absorbance data is on the [pH Sensing Cell](../ph-sensing-cell/spec.md#ph-sensing-cell-expected-behavior) spec.

:::{attention} Premature lysis has two independent causes
**Gramicidin A causes premature lysis; it does not prevent it.** Used as a proton channel for the GFP-expression result, it was left out of the colorimetric demonstration because it ruptured a portion of the CPRG-loaded liposomes, producing nonspecific color. Its absence can reduce pH-sensing efficiency, but proton diffusion into the more permeable liposomes was enough to drive PLA1 expression.

**Acidic conditions alone rupture some CPRG-loaded liposomes**, independent of PLA1, which confounds attributing a color change to the sensing pathway.
:::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)) to express the toehold-switch-gated PLA1 construct, and a drop to pH ≈ 6.5 to open the toehold switch (e.g. [Detector: pH-Sensing](../detector-ph/spec.md)).

Requires two lipid compartments — a sensing/PLA1 liposome and a separate CPRG-loaded liposome (e.g. [Chicago Chassis](../chicago-chassis/spec.md)). The readout depends on lysis releasing CPRG from one compartment into another, so this cascade has no bulk-cytosol route.

Requires that no LacZ protein share a compartment with CPRG until the reporter module is turned on (see [LacZ Reporter Module](../reporter-lacz/spec.md)).

Do not add gramicidin A to the colorimetric configuration. It ruptures a portion of the CPRG-loaded liposomes by itself, producing color that did not come from sensing. Leaving it out costs some pH-sensing efficiency, but proton diffusion into the more permeable liposomes is enough to drive PLA1 expression without it.

Requires a control that separates sensing-driven color from acid-driven leakage. Acidic conditions rupture some CPRG-loaded liposomes on their own, with no PLA1 involved, so color at pH 6.5 is not by itself attributable to the sensing pathway.

# Implementations

- [Chicago DevCell](../../implementations/chicago-devcell/main.md): places the Chicago cascades in a hydrogel with spatial patterning.

# Processes

No process page documents assembling this three-part cascade end to end.

# Constituent Modules

- [pH Sensing Cell](../ph-sensing-cell/spec.md) — pH-responsive sensing circuit in the Chicago Chassis synthetic cell
- [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) — LacZ/CPRG colorimetric readout chemistry
- [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md) — the second liposome population, carrying the [CPRG](../substrate-cprg/spec.md) released on lysis. This path keeps the liposome format because alginate embedding imposes no UV

:::{attention} PLA1 is inside the sensing cell, not beside it
The effector is expressed from the same molecule as the detector, so it enters this cascade inside the sensing cell rather than as a separate ingredient a composer supplies. It is listed on [Effector: PLA1](../effector-pla1/spec.md) and in the sensing cell's own cytosol.
:::

# Credits

Developed by Sung-Won Hwang and Samuel Chen (Chicago Node, Liu Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
