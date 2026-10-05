---
title: "aTc Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The aTc Cascade turns anhydrotetracycline (aTc) exposure into a visible colorimetric readout. The [SensorCell[aTc ⟶ PLA1]](../atc-sensing-cell/spec.md) supplies the `TetO-PLA1` sensing circuit, the [PLA1 Lysis Module](../effector-pla1/spec.md) supplies the lysis trigger, and [LacZ Reporter Module](../reporter-lacz/spec.md) provides a visible color change as a signal.

The sensing cell encapsulates `TetO-PLA1` and LacZ, with aTc and CPRG in the surrounding outer solution. aTc transits the membrane to the interior of the synthetic cell, activating expression of PLA1, which then ruptures the membrane and releases LacZ into the outer solution that then reacts with CPRG. Compare with the [pH Cascade](../ph-cascade/spec.md), which encapsulates the substrate and leaves the enzyme in the outer solution instead.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

(atc-cascade-reference-composition)=
# Reference Composition

The aTc Cascade combines its Modules as follows:

- **Sensing input:** [SensorCell[aTc ⟶ PLA1]](../atc-sensing-cell/spec.md) — the `TetO-PLA1` sensing construct, gated by aTc/TetR, encapsulated in the Cell: Base Cytosol, POPC/Chol (9:1) synthetic cell.
- **Lysis trigger:** [PLA1 Lysis Module](../effector-pla1/spec.md) — expressed once the aTc/TetR sensing circuit fires; couples sensing to readout. In the confirmed result, this is co-encapsulated in the same synthetic cell as the sensing construct rather than triggering a separate neighboring liposome.
- **Colorimetric readout:** [LacZ Reporter Module](../reporter-lacz/spec.md) — LacZ/CPRG chemistry, with the enzyme encapsulated and the substrate outside, so color appears only once lysis brings them together.

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    BASE_CYTOSOL["Base Cytosol"]
    DETECTOR_TETR_ATC["Detector: tetR-aTc"]
    EFFECTOR_PLA1_TETO["Gated lysis DNA: pT7-tetO-PLA1"]
    REPORTER_LACZ_ENZYME["LacZ Enzyme"]
    MEMBRANE_CHICAGO["Membrane: POPC/Chol (9:1)"]
    SUBSTRATE_CPRG["Substrate: CPRG"]
    MINERAL_OIL["Mineral oil"]
    ANALYTE_ATC["Analyte: aTc"]
    GLUCOSE["Glucose"]
    HEPES_KOH["HEPES-KOH buffer"]
    ENERGY_SOLUTION["Energy solution"]
    PEG_NORBORNENE_MONOMER["4-arm PEG-norbornene"]
    PEG4SH["PEG4SH crosslinker"]
    LAP["LAP photoinitiator"]

    P1_ASSEMBLE_OUTER_SOLUTION_0(["Assemble Outer Solution (mixing)"])
    OUTER_SOLUTION_GLUCOSE_HEPES["Outer Solution: Glucose-HEPES"]
    P2_ASSEMBLE_CYTOSOL_0(["Assemble Cytosol (mixing)"])
    ATC_SENSOR_CYTOSOL["SensorCytosol[aTc ⟶ PLA1]"]
    P3_ENCAPSULATE_0(["Encapsulation: Phase Transfer (packing)"])
    P3_ENCAPSULATE_1(["Degrade Exterior LacZ"])
    ATC_SENSING_CELL["SensorCell[aTc ⟶ PLA1]"]
    P4_EMBED_PHOTODEVELOPMENT_0(["Embedding: Photodevelopment (packing, 2 pairs mixing)"])
    ATC_GEL["aTc gel piece"]
    P5_ASSEMBLE_TRIGGER_SOLUTION_0(["Trigger Solution (mixing) — no page"])
    ATC_TRIGGER_SOLUTION["Trigger Solution"]
    P6_DOSE_TRIGGER_SOLUTION_0(["Addition of Solution to gel (packing) — no page"])
    ATC_CASCADE["aTc Cascade"]

    GLUCOSE --> P1_ASSEMBLE_OUTER_SOLUTION_0
    HEPES_KOH --> P1_ASSEMBLE_OUTER_SOLUTION_0
    P1_ASSEMBLE_OUTER_SOLUTION_0 --> OUTER_SOLUTION_GLUCOSE_HEPES

    BASE_CYTOSOL --> P2_ASSEMBLE_CYTOSOL_0
    DETECTOR_TETR_ATC --> P2_ASSEMBLE_CYTOSOL_0
    EFFECTOR_PLA1_TETO --> P2_ASSEMBLE_CYTOSOL_0
    REPORTER_LACZ_ENZYME --> P2_ASSEMBLE_CYTOSOL_0
    P2_ASSEMBLE_CYTOSOL_0 --> ATC_SENSOR_CYTOSOL

    ATC_SENSOR_CYTOSOL --> P3_ENCAPSULATE_0
    MEMBRANE_CHICAGO --> P3_ENCAPSULATE_0
    MINERAL_OIL --> P3_ENCAPSULATE_0
    P3_ENCAPSULATE_0 --> P3_ENCAPSULATE_1
    P3_ENCAPSULATE_1 --> ATC_SENSING_CELL

    PEG_NORBORNENE_MONOMER --> P4_EMBED_PHOTODEVELOPMENT_0
    PEG4SH --> P4_EMBED_PHOTODEVELOPMENT_0
    LAP --> P4_EMBED_PHOTODEVELOPMENT_0
    OUTER_SOLUTION_GLUCOSE_HEPES --> P4_EMBED_PHOTODEVELOPMENT_0
    ATC_SENSING_CELL --> P4_EMBED_PHOTODEVELOPMENT_0
    P4_EMBED_PHOTODEVELOPMENT_0 --> ATC_GEL

    SUBSTRATE_CPRG --> P5_ASSEMBLE_TRIGGER_SOLUTION_0
    ANALYTE_ATC --> P5_ASSEMBLE_TRIGGER_SOLUTION_0
    P5_ASSEMBLE_TRIGGER_SOLUTION_0 --> ATC_TRIGGER_SOLUTION

    ATC_GEL --> P6_DOSE_TRIGGER_SOLUTION_0
    ATC_TRIGGER_SOLUTION --> P6_DOSE_TRIGGER_SOLUTION_0
    P6_DOSE_TRIGGER_SOLUTION_0 --> ATC_CASCADE


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class BASE_CYTOSOL,DETECTOR_TETR_ATC,EFFECTOR_PLA1_TETO,REPORTER_LACZ_ENZYME,MEMBRANE_CHICAGO,SUBSTRATE_CPRG,MINERAL_OIL,ANALYTE_ATC,GLUCOSE,HEPES_KOH,ENERGY_SOLUTION,PEG_NORBORNENE_MONOMER,PEG4SH,LAP leaf;
    class OUTER_SOLUTION_GLUCOSE_HEPES,ATC_SENSOR_CYTOSOL,ATC_SENSING_CELL,ATC_GEL,ATC_TRIGGER_SOLUTION,ATC_CASCADE composed;
    class P1_ASSEMBLE_OUTER_SOLUTION_0,P2_ASSEMBLE_CYTOSOL_0,P3_ENCAPSULATE_0,P3_ENCAPSULATE_1,P4_EMBED_PHOTODEVELOPMENT_0,P5_ASSEMBLE_TRIGGER_SOLUTION_0,P6_DOSE_TRIGGER_SOLUTION_0 process;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click DETECTOR_TETR_ATC "/docs/modules/detector-tetr-atc/spec"
    click REPORTER_LACZ_ENZYME "/docs/modules/reporter-lacz-enzyme/spec"
    click MEMBRANE_CHICAGO "/docs/modules/membrane-popc-chol-9-1/spec"
    click SUBSTRATE_CPRG "/docs/modules/substrate-cprg/spec"
    click ANALYTE_ATC "/docs/modules/analyte-atc/spec"
    click PEG_NORBORNENE_MONOMER "/docs/modules/gel-peg-norbornene/spec"
    click P1_ASSEMBLE_OUTER_SOLUTION_0 "/docs/processes/assemble-outer-solution/main"
    click OUTER_SOLUTION_GLUCOSE_HEPES "/docs/modules/outer-solution-glucose-hepes/spec"
    click P2_ASSEMBLE_CYTOSOL_0 "/docs/processes/assemble-cytosol/assemble-cytosol-main"
    click ATC_SENSOR_CYTOSOL "/docs/modules/atc-sensor-cytosol/spec"
    click P3_ENCAPSULATE_0 "/docs/processes/assemble-base-cell/main"
    click P3_ENCAPSULATE_1 "/docs/processes/degrade-exterior-lacz/main"
    click ATC_SENSING_CELL "/docs/modules/atc-sensing-cell/spec"
    click P4_EMBED_PHOTODEVELOPMENT_0 "/docs/processes/embed-photodevelopment/main"
    click ATC_CASCADE "/docs/modules/atc-cascade/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

:::{table}
| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| `pT7-tetO-PLA1-linear` | 1202 | [pT7-tetO-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/devcells/devstudio-constructs/effectors/detector-tetr-atc/pT7-tetO-PLA1-linear.gb) | Expressed in the synthetic cell; distinct from `pT7-tetO-plamGFP`. The file carries the `TetO` and `PLA1 (codon-optimized to E. coli)` features |
:::

::::

::::{tab-item} Cytosol

The sensing cell interior. It carries the enzyme but not its substrate — see the note under Outer Solution.

:::{table} Sensing cell interior.
:label: comp-atc-cascade

| Component | Working concentration |
| --- | --- |
| `TetO-PLA1` DNA | 1 nM (headline condition); also tested at 0.5 nM |
| TetR | 50 nM (headline condition); also tested at 100 nM |
| LacZ enzyme | 2.5 U/mL |
| Base Cytosol components | At reaction concentration; not separately documented for this cascade |
:::

::::

::::{tab-item} Membrane

:::{table} Synthetic cell membrane — [Membrane: POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md).
:label: comp-atc-cascade-membrane

| Component | Target percentage (%) |
| --- | --- |
| POPC | 89.9 |
| Cholesterol | 10 |
| Liss-Rhod PE | 0.1 |
:::

::::

::::{tab-item} Substrate

[CPRG](../substrate-cprg/spec.md) reaches this cascade as a **free dye dosed into the gel after crosslinking**, not inside a liposome. The photodeveloped gel this path uses imposes UV, which bleaches CPRG, so the substrate goes in once crosslinking is done.

:::{table} CPRG in the aTc path.
| Component | Working concentration | Notes |
| --- | --- | --- |
| CPRG | 0.5 mM final in the gel | about 11 µL of a 5 mM stock per 100 µL of gel |
:::

::::

::::{tab-item} Outer Solution

:::{table} Outer solution.
:label: comp-atc-cascade-outer

| Component | Working concentration |
| --- | --- |
| CPRG substrate | 0.5 mM |
| aTc | 1 µM — the response saturates at or below this, so higher doses add nothing. See [Expected Behavior](#atc-cascade-expected-behavior) for the dose series. |
:::

In the photodeveloped format CPRG is added to the gel **after** crosslinking rather than pre-loaded, because the UV that crosslinks the gel bleaches it. This holds for both photodevelopment routes — see [Embedding: Photodevelopment](../../processes/embed-photodevelopment/main.md).

::::

:::::

(atc-cascade-expected-behavior)=
# Expected Behavior

## Cells

The aTc Cascade is expected to run the full sensing → lysis → LacZ readout chain in one compartment and to produce a detectable aTc-dependent color change, confirmed in synthetic cells. **The response is not graded.** Fold change in absorbance at 5 h (n = 3) separates dosed from undosed at roughly 1.15× to 1.33×, across three DNA/TetR combinations dosed at 0, 1, 5, and 10 µM aTc. It is non-monotonic in two of the three combinations, and the error bars across the 1, 5, and 10 µM points overlap in all three. Expect a working end-to-end chain with a detectable signal, not a characterized dose-response.

The [aTc Sensing Module](../detector-tetr-atc/spec.md#teto-pla1-encapsulated-with-lacz) spec covers why the 0 µM point is a normalization baseline rather than a negative control.

## Gels

:::{warning} Not yet validated
This Module has not been validated in gels. The aTc-response result above is confirmed in synthetic cells only. Gel integration has not been completed — see the [SensorCell[aTc ⟶ PLA1]](../atc-sensing-cell/spec.md#atc-sensing-cell-expected-behavior) spec for the same caveat. Do not treat this cascade as validated for gel-embedded use.
:::

# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)) to express the `TetO-PLA1` construct, and TetR as the repressor holding it off in the absence of aTc (e.g. [Detector: tetR-aTc](../detector-tetr-atc/spec.md)).

Requires a lipid compartment for PLA1 to lyse (e.g. [Cell: Base Cytosol, POPC/Chol (9:1)](../cell-base-cytosol-popc-chol/spec.md)). The readout is produced by lysis releasing CPRG to LacZ, so this cascade has no bulk-cytosol route.

Requires that no LacZ protein share a compartment with CPRG until the reporter module is turned on (see [LacZ Reporter Module](../reporter-lacz/spec.md)).

Must not be exposed to theophylline, which is reported to interfere with LacZ activity. See [LacZ Reporter Module § Requirements](../reporter-lacz/spec.md#reporter-lacz-requirements) for the constraint and the state of the evidence behind it.

# Implementations

- [aTc Demo](../../implementations/devstudio-atc-demo/main.md): the cascade that demo builds.

# Processes

Encapsulation follows the shared phase-transfer method in [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md), with the Chicago-specific lipid composition documented on [Membrane: POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md). Gel embedding of this cascade is not documented.

:::{attention} Process gap
@Editor(chicago): no process page covers gel embedding for this cascade, and [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) has not been confirmed to apply as written at synthetic-cell scale. Both need process pages.
:::

# Constituent Modules

- [SensorCell[aTc ⟶ PLA1]](../atc-sensing-cell/spec.md) — `TetO-PLA1` sensing construct gated by aTc/TetR, encapsulated in the Cell: Base Cytosol, POPC/Chol (9:1) synthetic cell
- [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) — encapsulated with the sensing reaction at 2.5 U/mL
- [Substrate: CPRG](../substrate-cprg/spec.md) — dosed free into the gel after crosslinking, because UV bleaches it. This path carries no substrate liposome

:::{attention} PLA1 is inside the sensing cell, not beside it
The effector is expressed from the same molecule as the detector, so it enters this cascade inside the sensing cell rather than as a separate ingredient a composer supplies. It is listed on [Lysis: PLA1](../effector-pla1/spec.md) and in the sensing cell's own cytosol.
:::

# Credits

Developed by Mary Kelly (Chicago Node, Kamat Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
