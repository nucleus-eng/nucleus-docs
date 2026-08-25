---
title: "aTc Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The aTc Cascade turns anhydrotetracycline (aTc) exposure into a visible colorimetric readout. The [aTc Sensing Cell](../atc-sensing-cell/spec.md) supplies the `TetO-PLA1` sensing circuit, the [PLA1 Lysis Module](../effector-pla1/spec.md) supplies the lysis trigger, and a colorimetric reporter converts the released substrate into a visible signal.

The whole chain runs in one compartment: the aTc Sensing Cell co-encapsulates the `TetO-PLA1` construct, PLA1 and the LacZ reporter in a single synthetic cell, and that configuration produced the 2026-08-14 aTc-response data.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

The aTc Cascade combines its Modules as follows:

- **Sensing input:** [aTc Sensing Cell](../atc-sensing-cell/spec.md) — the `TetO-PLA1` sensing construct, gated by aTc/TetR, encapsulated in the Chicago Chassis synthetic cell.
- **Lysis trigger:** [PLA1 Lysis Module](../effector-pla1/spec.md) — expressed once the aTc/TetR sensing circuit fires; couples sensing to readout. In the confirmed result, this is co-encapsulated in the same synthetic cell as the sensing construct rather than triggering a separate neighboring liposome.
- **Colorimetric readout:** [LacZ Reporter Module](../reporter-lacz/spec.md) — LacZ/CPRG chemistry, co-encapsulated with the sensing and lysis constructs.

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    ATC_CASCADE["aTc Cascade"]
    ATC_SENSING_CELL["aTc Sensing Cell"]
    BASE_CYTOSOL["Base Cytosol"]
    CHICAGO_CHASSIS["Chicago Chassis"]
    DETECTOR_TETR_ATC["Detector: tetR-aTc"]
    EFFECTOR_PLA1["Effector: PLA1"]
    MEMBRANE_POPC_CHOL_CHICAGO["Chicago Membrane: POPC/Chol"]
    REPORTER_LACZ["Reporter: LacZ"]

    ATC_SENSING_CELL --> ATC_CASCADE
    EFFECTOR_PLA1 --> ATC_CASCADE
    REPORTER_LACZ --> ATC_CASCADE
    CHICAGO_CHASSIS --> ATC_SENSING_CELL
    DETECTOR_TETR_ATC --> ATC_SENSING_CELL
    EFFECTOR_PLA1 --> ATC_SENSING_CELL
    REPORTER_LACZ --> ATC_SENSING_CELL
    BASE_CYTOSOL --> CHICAGO_CHASSIS
    MEMBRANE_POPC_CHOL_CHICAGO --> CHICAGO_CHASSIS

    classDef constituent fill:#6B7280,color:#ffffff,stroke:#4B5563;
    classDef this fill:#374151,color:#ffffff,stroke:#111827;
    class ATC_SENSING_CELL,BASE_CYTOSOL,CHICAGO_CHASSIS,DETECTOR_TETR_ATC,EFFECTOR_PLA1,MEMBRANE_POPC_CHOL_CHICAGO,REPORTER_LACZ constituent;
    class ATC_CASCADE this;

    click ATC_CASCADE "/docs/modules/atc-cascade/spec"
    click ATC_SENSING_CELL "/docs/modules/atc-sensing-cell/spec"
    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click CHICAGO_CHASSIS "/docs/modules/chicago-chassis/spec"
    click DETECTOR_TETR_ATC "/docs/modules/detector-tetr-atc/spec"
    click EFFECTOR_PLA1 "/docs/modules/effector-pla1/spec"
    click MEMBRANE_POPC_CHOL_CHICAGO "/docs/modules/membrane-popc-chol-chicago/spec"
    click REPORTER_LACZ "/docs/modules/reporter-lacz/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

:::{table}
| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| `TetO-PLA1` | not documented | — | Expressed in the synthetic cell; distinct from `pT7-tetO-plamGFP` |
| TetR repressor | not applicable | — | Co-encapsulated as purified protein |
| β-galactosidase (LacZ) | not applicable | — | Co-encapsulated as purified enzyme, not expressed |
:::

:::{note} Where these constructs are specified
The `TetO-PLA1` sensing construct is specified on [Detector: tetR-aTc](../detector-tetr-atc/spec.md), and the PLA1 constructs on [Effector: PLA1](../effector-pla1/spec.md).
:::

:::{attention} Construct not yet in `nucleus-eng/DNA`
`TetO-PLA1` has no sequence file in [`nucleus-eng/DNA`](https://github.com/nucleus-eng/DNA) and no recorded length. It is distinct from `pT7-tetO-plamGFP`, so that file cannot stand in for it. The same gap is recorded on [aTc Sensing Cell](../atc-sensing-cell/spec.md). Do not add a length or file entry here until the construct is confirmed and its length verified against the source file.
:::

::::

::::{tab-item} Cytosol

Every component below is co-encapsulated in a single synthetic cell.

:::{table} Confirmed aTc Cascade integration path (Chicago, 2026-08-14).
:label: comp-atc-cascade

| Component | Working concentration |
| --- | --- |
| `TetO-PLA1` DNA | 1 nM (headline condition); also tested at 0.5 nM |
| TetR | 50 nM (headline condition); also tested at 100 nM |
| CPRG substrate | 0.5 mM |
| LacZ enzyme | 20 U/mL |
| Base Cytosol components | At reaction concentration; not separately documented for this cascade |
:::

Whether aTc is added to the inner or the outer solution is not established.

PLA1 has no row of its own: it is expressed from the `TetO-PLA1` construct already listed, not added as a reagent.

::::

::::{tab-item} Membrane

:::{table} Synthetic cell membrane — [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md).
:label: comp-atc-cascade-membrane

| Component | Target percentage (%) |
| --- | --- |
| POPC | 89.9 |
| Cholesterol | 10 |
| Liss-Rhod PE | 0.1 |
:::

::::

:::::

# Expected Behavior

## Cells

The aTc Cascade is expected to run the full sensing → lysis → LacZ readout chain in one compartment and to produce a detectable aTc-dependent color change, confirmed in synthetic cytosols and in synthetic cells. **The response is not graded.** Fold change in absorbance at 5 h (n = 3) separates dosed from undosed at roughly 1.15× to 1.33×, across three DNA/TetR combinations dosed at 0, 1, 5, and 10 µM aTc. It is non-monotonic in two of the three combinations, and the error bars across the 1, 5, and 10 µM points overlap in all three. Expect a working end-to-end chain with a detectable signal, not a characterized dose-response.

The [aTc Sensing Module](../detector-tetr-atc/spec.md#chicago-cascade-encapsulation-teto-pla1-lacz-cprg-readout) spec covers why the 0 µM point is a normalization baseline rather than a negative control.

## Gels

:::{warning} Not yet validated
This Module has not been validated in hydrogels. The aTc-response result above is confirmed in synthetic cytosols and in synthetic cells only. Hydrogel integration has not been completed — see the [aTc Sensing Cell](../atc-sensing-cell/spec.md#expected-behavior) spec for the same caveat. Do not treat this cascade as validated for hydrogel-embedded use.
:::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)) to express the `TetO-PLA1` construct, and TetR as the repressor holding it off in the absence of aTc (e.g. [Detector: tetR-aTc](../detector-tetr-atc/spec.md)).

Requires a lipid compartment for PLA1 to lyse (e.g. [Chicago Chassis](../chicago-chassis/spec.md)). The readout is produced by lysis releasing CPRG to co-encapsulated LacZ, so this cascade has no bulk-cytosol route.

Requires CPRG and LacZ co-encapsulated with the sensing and lysis constructs (e.g. [LacZ Reporter Module](../reporter-lacz/spec.md)).

Must not be co-encapsulated with theophylline sensing, which shares this cascade's LacZ/CPRG readout. See [Theophylline Sensing Module § Requirements](../detector-theophylline/spec.md#requirements) for the constraint and the state of the evidence behind it.

# Implementations

- [Chicago DevCell](../../implementations/chicago-devcell/main.md): places the Chicago cascades in a hydrogel with spatial patterning.

# Processes

Encapsulation follows the shared phase-transfer method in [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md), with the Chicago-specific lipid composition documented on [Chicago Membrane](../membrane-popc-chol-chicago/spec.md). Hydrogel embedding of this cascade is not documented.

:::{attention} Process gap
@Editor: no process page covers hydrogel embedding for this cascade, and [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) has not been confirmed to apply as written at synthetic-cell scale. Both need process pages.
:::

# Constituent Modules

- [aTc Sensing Cell](../atc-sensing-cell/spec.md) — `TetO-PLA1` sensing construct gated by aTc/TetR, encapsulated in the Chicago Chassis synthetic cell
- [PLA1 Lysis Module](../effector-pla1/spec.md) — lysis trigger coupling sensing to readout
- [LacZ Reporter Module](../reporter-lacz/spec.md) — LacZ/CPRG colorimetric readout chemistry — the confirmed readout, used in the 2026-08-14 aTc-response data

# Credits

Developed by Mary Kelly (Chicago Node, Kamat Lab).
