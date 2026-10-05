---
title: "SensorCytosol[3OC6-HSL ⟶ PLA1]"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`sensor-cytosol`](../sensor-cytosol/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

The SensorCytosol[3OC6-HSL ⟶ PLA1] is the aqueous phase of the [SensorCell[3OC6-HSL ⟶ PLA1]](../ahsl-sensing-cell/spec.md): [S30 Lysate](../s30-lysate/spec.md) carrying the [3OC6-HSL Sensing Module](../detector-3oc6-hsl/spec.md) and, through it, the [PLA1 Lysis Module](../effector-pla1/spec.md). It is mixed before encapsulation, not added to a closed compartment.

The [aTc](../atc-sensor-cytosol/spec.md) and [pH](../ph-sensor-cytosol/spec.md) sensor cytosols fill the same role for the Chicago Node, on a [Base Cytosol](../base-cytosol/spec.md) background instead of S30 Lysate.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    S30_LYSATE["Cytosol: S30 Lysate"]
    DETECTOR_3OC6_HSL["Detector: 3OC6-HSL (LuxR)"]
    EFFECTOR_PLA1_LUXR["Gated lysis DNA: pOpen-LuxR-PLA1"]

    P1_ASSEMBLE_CYTOSOL_0(["Assemble Cytosol (mixing)"])
    AHSL_SENSOR_CYTOSOL["SensorCytosol[3OC6-HSL ⟶ PLA1]"]

    S30_LYSATE --> P1_ASSEMBLE_CYTOSOL_0
    DETECTOR_3OC6_HSL --> P1_ASSEMBLE_CYTOSOL_0
    EFFECTOR_PLA1_LUXR --> P1_ASSEMBLE_CYTOSOL_0
    P1_ASSEMBLE_CYTOSOL_0 --> AHSL_SENSOR_CYTOSOL


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class S30_LYSATE,DETECTOR_3OC6_HSL,EFFECTOR_PLA1_LUXR leaf;
    class AHSL_SENSOR_CYTOSOL composed;
    class P1_ASSEMBLE_CYTOSOL_0 process;

    click S30_LYSATE "/docs/modules/s30-lysate/spec"
    click DETECTOR_3OC6_HSL "/docs/modules/detector-3oc6-hsl/spec"
    click P1_ASSEMBLE_CYTOSOL_0 "/docs/processes/assemble-cytosol/assemble-cytosol-main"
    click AHSL_SENSOR_CYTOSOL "/docs/modules/ahsl-sensor-cytosol/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

:::{table} Constructs in the SensorCytosol[3OC6-HSL ⟶ PLA1].
| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| `pOpen-LuxR-PLA1` | 4175 | [pOpen-LuxR-PLA1.gb](https://github.com/nucleus-eng/DNA/blob/devcells/devstudio-constructs/effectors/detector-3oc6-hsl/pOpen-LuxR-PLA1.gb) | **Circular.** S30 Lysate degrades linear DNA, so this route takes the plasmid |
| `LuxR-PLA1-linear` | 2237 | [LuxR-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/devcells/devstudio-constructs/effectors/detector-3oc6-hsl/LuxR-PLA1-linear.gb) | Cassette form. **Not for this cytosol** — listed so the two are not confused |
:::

One molecule carries the detector and the effector, so [PLA1](../effector-pla1/spec.md) has no construct of its own here.

::::

::::{tab-item} Cytosol

:::{table} Cytosolic components of the SensorCytosol[3OC6-HSL ⟶ PLA1], at reaction concentration.
| Module | Working concentration | Notes |
| --- | --- | --- |
| [S30 Lysate](../s30-lysate/spec.md) | At reaction concentration, per kit | Transcription and translation. **Requires circular DNA** — no GamS is added, so a linear template is degraded |
| [3OC6-HSL Sensing Module](../detector-3oc6-hsl/spec.md) | `LuxR-deGFP` sensor plasmid at 40 ng/µL final, from a 1056 ng/µL stock — 0.95 µL per reaction | One molecule carries constitutive `BBa_J23101`→`luxR` and the `pLux`-driven payload, so LuxR is never supplied separately |
| [PLA1 Lysis Module](../effector-pla1/spec.md) | Covered by the sensor plasmid | The `LuxR-PLA1` variant puts the effector on the same molecule as the detector |
:::

::::

:::::



# Process

- [Assemble Cytosol](../../processes/assemble-base-cytosol/main.md) — the mixing step that produces this Module. Every constituent above enters the same compartment.

This cytosol is consumed by [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md), which combines it with the [Membrane: POPC](../membrane-popc/spec.md) to form the [SensorCell[3OC6-HSL ⟶ PLA1]](../ahsl-sensing-cell/spec.md).

# Constituent Modules

- [S30 Lysate](../s30-lysate/spec.md) — transcription and translation
- [3OC6-HSL Sensing Module](../detector-3oc6-hsl/spec.md) — the sensor plasmid
- `pOpen-LuxR-PLA1` — the gated construct. One molecule carries the receiver and PLA1, so neither is a separate addition. PLA1 itself is described on the Lysis: PLA1 page, `../effector-pla1/spec.md`

# Credits

Developed by the London Node.

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
