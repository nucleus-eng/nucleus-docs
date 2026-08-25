---
title: "Chicago Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Chicago Cascade is the top-level, multiplexed Chicago demo node: two integration paths running side by side in one system, each detecting a different analyte, both reporting through a shared colorimetric readout. The two integration paths are the [aTc Cascade](../atc-cascade/spec.md) and the [pH Cascade](../ph-cascade/spec.md).

The goal is multiplexed detection — aTc and pH sensed in the same reaction, with a visible color change that reflects the combination of the two inputs.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Rewritten 2026-08-19 — the integration paths have changed
Theophylline interferes with the LacZ/CPRG readout, so the theophylline path is not part of this cascade.

That is superseded. Chicago is now focused on the aTc and pH sensors (14 Aug 2026 deck, slides 2 and 34, which lists "Two sensors (aTC/pH)"), and the theophylline sensor has been removed from the demo — its riboswitch drives the reporter with no analyte present, so it does not discriminate. See [Theophylline Sensing Module](../detector-theophylline/spec.md).

The theophylline/aTc co-encapsulation constraint remains true and is still documented on the affected Modules. It is simply no longer this cascade's blocker, because theophylline is no longer one of its integration paths.
:::

# Reference Composition

No combined reference composition exists, and none is given here — not even a hypothetical one. The combination has never been assembled, so there are no working concentrations to report.

Each integration path's own composition is documented on its own page.

:::{attention} Merged recipe not documented
@Editor: no combined recipe exists for the two paths together. The per-population tables below are each path's own composition, carried over unchanged; nothing records what changes when they share one reaction. Confirm with the Chicago Node.
:::


:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    ATC_CASCADE["aTc Cascade"]
    ATC_SENSING_CELL["aTc Sensing Cell"]
    BASE_CYTOSOL["Base Cytosol"]
    CHICAGO_CASCADE["Chicago Cascade"]
    CHICAGO_CHASSIS["Chicago Chassis"]
    DETECTOR_PH["Detector: pH-Sensing"]
    DETECTOR_TETR_ATC["Detector: tetR-aTc"]
    EFFECTOR_PLA1["Effector: PLA1"]
    MEMBRANE_POPC_CHOL_CHICAGO["Chicago Membrane: POPC/Chol"]
    PH_CASCADE["pH Cascade"]
    PH_SENSING_CELL["pH Sensing Cell"]
    REPORTER_LACZ["Reporter: LacZ"]
    SUBSTRATE_CPRG_SUV["Substrate SUV: CPRG"]

    ATC_SENSING_CELL --> ATC_CASCADE
    EFFECTOR_PLA1 --> ATC_CASCADE
    REPORTER_LACZ --> ATC_CASCADE
    CHICAGO_CHASSIS --> ATC_SENSING_CELL
    DETECTOR_TETR_ATC --> ATC_SENSING_CELL
    EFFECTOR_PLA1 --> ATC_SENSING_CELL
    REPORTER_LACZ --> ATC_SENSING_CELL
    ATC_CASCADE --> CHICAGO_CASCADE
    PH_CASCADE --> CHICAGO_CASCADE
    BASE_CYTOSOL --> CHICAGO_CHASSIS
    MEMBRANE_POPC_CHOL_CHICAGO --> CHICAGO_CHASSIS
    PH_SENSING_CELL --> PH_CASCADE
    EFFECTOR_PLA1 --> PH_CASCADE
    REPORTER_LACZ --> PH_CASCADE
    SUBSTRATE_CPRG_SUV --> PH_CASCADE
    CHICAGO_CHASSIS --> PH_SENSING_CELL
    DETECTOR_PH --> PH_SENSING_CELL

    classDef constituent fill:#6B7280,color:#ffffff,stroke:#4B5563;
    classDef this fill:#374151,color:#ffffff,stroke:#111827;
    class ATC_CASCADE,ATC_SENSING_CELL,BASE_CYTOSOL,CHICAGO_CHASSIS,DETECTOR_PH,DETECTOR_TETR_ATC,EFFECTOR_PLA1,MEMBRANE_POPC_CHOL_CHICAGO,PH_CASCADE,PH_SENSING_CELL,REPORTER_LACZ,SUBSTRATE_CPRG_SUV constituent;
    class CHICAGO_CASCADE this;

    click ATC_CASCADE "/docs/modules/atc-cascade/spec"
    click ATC_SENSING_CELL "/docs/modules/atc-sensing-cell/spec"
    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click CHICAGO_CASCADE "/docs/modules/chicago-cascade/spec"
    click CHICAGO_CHASSIS "/docs/modules/chicago-chassis/spec"
    click DETECTOR_PH "/docs/modules/detector-ph/spec"
    click DETECTOR_TETR_ATC "/docs/modules/detector-tetr-atc/spec"
    click EFFECTOR_PLA1 "/docs/modules/effector-pla1/spec"
    click MEMBRANE_POPC_CHOL_CHICAGO "/docs/modules/membrane-popc-chol-chicago/spec"
    click PH_CASCADE "/docs/modules/ph-cascade/spec"
    click PH_SENSING_CELL "/docs/modules/ph-sensing-cell/spec"
    click REPORTER_LACZ "/docs/modules/reporter-lacz/spec"
    click SUBSTRATE_CPRG_SUV "/docs/modules/substrate-cprg-suv/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

The constructs are those of the two integration paths; no construct is specific to the merge.

:::{attention} Constructs not yet in `nucleus-eng/DNA`
Neither PLA1-expressing construct below is confirmed in [`nucleus-eng/DNA`](https://github.com/nucleus-eng/DNA), and neither has a recorded length. `TetO-PLA1` carries the same gap where it is specified, on [aTc Sensing Cell](../atc-sensing-cell/spec.md). The toehold-switch-gated template is not separately recorded, and whether it is one of the two constructs listed on [Effector: PLA1](../effector-pla1/spec.md) or a third design is not established — do not assume it from the name. Do not add a length or file entry here until each construct is confirmed and its length verified against the source file.
:::

:::{table}
| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| `TetO-PLA1` | not documented | — | Expressed; see [aTc Cascade](../atc-cascade/spec.md) |
| Toehold-switch-gated PLA1 template | not documented | — | Expressed; see [pH Cascade](../ph-cascade/spec.md) |
| pH-responsive ssDNA : trigger ssDNA | not applicable | — | Synthesized oligonucleotides |
| β-galactosidase (LacZ) | not applicable | — | Purified enzyme, not expressed |
:::

::::

::::{tab-item} Membrane

**All three populations carry the same membrane.** Both integration paths are built on the [Chicago Chassis](../chicago-chassis/spec.md), and the Substrate SUV uses the same lipid composition, so one table covers the aTc Sensing Cell, the pH Sensing Cell and the Substrate SUV alike. That identity is load-bearing — see [Requirements](#requirements).

:::{table} Synthetic cell and SUV membrane — [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md).
:label: comp-chicago-cascade-membrane

| Component | Target percentage (%) |
| --- | --- |
| POPC | 89.9 |
| Cholesterol | 10 |
| Liss-Rhod PE | 0.1 |
:::

::::

::::{tab-item} aTc Sensing Cell

The aTc integration path is one compartment: sensing, lysis and readout are co-encapsulated together, so this population carries its own LacZ and CPRG and needs nothing from the exterior.

:::{table} aTc Sensing Cell cytosol — as on [aTc Cascade](../atc-cascade/spec.md#reference-composition).
:label: comp-chicago-cascade-atc-cell

| Component | Working concentration |
| --- | --- |
| `TetO-PLA1` DNA | 1 nM |
| TetR | 50 nM |
| CPRG substrate | 0.5 mM |
| LacZ enzyme | 20 U/mL |
| Base Cytosol components | At reaction concentration |
:::

::::

::::{tab-item} pH Sensing Cell

The pH integration path is two compartments. This population carries sensing and lysis only; its substrate is in the Substrate SUV and its LacZ is in the outer solution.

:::{table} pH Sensing Cell cytosol — as on [pH Cascade](../ph-cascade/spec.md#reference-composition).
:label: comp-chicago-cascade-ph-cell

| Component | Working concentration |
| --- | --- |
| pH-responsive ssDNA : trigger ssDNA (3:1, annealed) | 4.625 nM trigger ssDNA, final |
| Toehold-switch-gated PLA1 DNA template | 2 nM, final |
| Base Cytosol components | At reaction concentration |
:::

::::

::::{tab-item} Substrate SUV

A second liposome population carrying the chromogenic substrate, entering this cascade through the [pH Cascade](../ph-cascade/spec.md). See [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md).

:::{table} Substrate SUV lumen.
:label: comp-chicago-cascade-suv

| Component | Working concentration |
| --- | --- |
| CPRG substrate | Not documented at a reaction concentration for the multiplexed cascade |
:::

The aTc integration path co-encapsulates free CPRG instead, so it contributes no SUV population.

::::

::::{tab-item} Outer Solution

The medium all three populations sit in, and the only compartment with no membrane of its own. The pH integration path reports through LacZ here; the aTc path carries its own LacZ internally and does not depend on it.

:::{table} Outer solution.
:label: comp-chicago-cascade-outer

| Component | Working concentration |
| --- | --- |
| β-galactosidase (LacZ) | Not documented at a working concentration for the multiplexed cascade |
| Osmotic balance | Matched to the inner solutions, per [Chicago Chassis](../chicago-chassis/spec.md#reference-composition) |
:::

::::

:::::

# Expected Behavior

**Status: not attempted.** No experiment has run the two integration paths together. The merge is not blocked; it has not been tried.

There is, however, a known design question standing in front of it, described below.

## Cells

:::{warning} Not yet validated
This Module has not been validated in synthetic cells.
:::

# Requirements

Requires both integration paths in one system — [aTc Cascade](../atc-cascade/spec.md) and [pH Cascade](../ph-cascade/spec.md) — on a shared [Chicago Chassis](../chicago-chassis/spec.md) membrane, reporting through one shared [LacZ Reporter](../reporter-lacz/spec.md).

Requires each integration path's own requirements to hold unchanged. Neither path has a bulk-cytosol route, so this cascade does not either.

Requires spatial separation between the two integration paths. PLA1 lyses any phospholipid membrane it reaches, not only the membrane of the cell that expressed it — see [PLA1 Lysis Module](../effector-pla1/spec.md#requirements) — and all three populations here carry the same membrane. Co-locating the paths in one region therefore lets either analyte lyse every compartment in that region. Spatial patterning of the hydrogel supplies the separation; the pattern itself is an Implementation-level choice, documented on [Chicago DevCell](../../implementations/chicago-devcell/main.md).

**Something has to decide what the readout does when both paths fire.** Both the aTc and pH integration paths end at the same LacZ/CPRG chemistry. Two inputs arriving at one output is not, by itself, a design — it needs a stated rule for how the two signals combine. Should the color change when *either* analyte is present, only when *both* are, or only when exactly one is? Each of those is a different device, and each needs a different mechanism.

That rule has not been chosen. Until it is, "multiplexed detection" describes an intent rather than a specification.

:::{attention} This is the cascade's central open question
Two things follow from it, and both are worth stating plainly.

**First, without spatial separation the paths are not independent.** Either analyte alone drives PLA1, and PLA1 lyses every compartment within reach: the aTc path releases its own internal LacZ and CPRG *and* opens the Substrate SUV, while the pH path opens the SUV *and* the aTc cell, releasing that cell's LacZ. Color appears by several routes with only one analyte present. This is not the readout chemistry being shared — it is the membrane being shared, with an effector that does not discriminate.

**Second, a shared readout with no combining rule is not neutral.** If both paths simply drive the same enzyme reaction, the result is whatever the chemistry does when both are active — which is closer to an uncontrolled "either" than to a designed behavior. Getting a specified behavior means adding a mechanism, not just co-locating the two paths.

**Third, the three candidate rules are not equally easy to build.** "Either analyte" is close to what co-locating the paths already gives, so the work is making it controlled and reproducible rather than incidental. "Both analytes" needs a coincidence mechanism — some step that only proceeds when two inputs are present at once — and that mechanism has to survive the cross-lysis above, since either analyte alone otherwise destroys the compartments the coincidence would have to be read from. It cannot be solved by making PLA1 selective: neighbor lysis is the mechanism the readout depends on. "Exactly one" is harder still, because it needs the system to suppress output when a signal *is* present, and inhibition is a mechanism this cascade does not currently have anywhere.

So the choice of rule is not a labeling decision to make at write-up time. It determines what has to be built.
:::

**A second, separate question.** The pH path's readout adds a neutralization buffer step before the color develops, while the aTc path reads out directly. @Editor: whether one shared readout can serve both paths when one requires a pH adjustment is unresolved. Confirm with the Chicago Node.

# Implementations

This cascade is the sensing core of the [Chicago DevCell](../../implementations/chicago-devcell/main.md), which places it in a hydrogel and adds spatial patterning. That page carries the demo-level status.

# Processes

No combined assembly process exists. Both integration paths are formed by the same method — see [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) — and both are embedded and read out through the processes listed on their own pages. What is missing is not a technique for making either path, but the step that brings them together and the mechanism that combines their outputs.

# Constituent Modules

- [aTc Cascade](../atc-cascade/spec.md) — the aTc integration path, confirmed in synthetic cytosols and in synthetic cells; hydrogel embedding still in progress
- [pH Cascade](../ph-cascade/spec.md) — the pH integration path; its individual results are confirmed but the three-part chain has not been run end to end

Both integration paths terminate at the [LacZ Reporter Module](../reporter-lacz/spec.md), which is shared rather than duplicated. That sharing is the subject of the Requirements section above.

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).
