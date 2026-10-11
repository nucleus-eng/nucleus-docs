---
title: "LuxR-GFP Sensor Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [Cascade](../cascade/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

A sensing cascade that detects 3OC6-HSL in S30 lysate and reports fluorescence. LuxR binds the analyte and derepresses mNeonGreen, whose green fluorescence is observed.

[CRAIC](../craic-cascade/spec.md) senses the same analyte in [Base Cytosol](../base-cytosol/spec.md) and reports color through LacZ and CPRG.

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
    REPORTER_MNEONGREEN["Reporter: mNeonGreen"]
    MEMBRANE_POPC["Membrane: POPC"]
    OUTER_SOLUTION_GLUTAMATE["Outer Solution: Glutamate-HEPES-Glucose"]
    ULGA_POWDER["ULGA powder"]

    P1_ASSEMBLE_PLASMID_0(["Plasmid assemble (mixing) — no page"])
    LUXR_GFP_PLASMID["Plasmid"]
    P2_ASSEMBLE_CYTOSOL_0(["Assemble Cytosol (mixing)"])
    LUXR_GFP_SENSOR_CYTOSOL["SensorCytosol[3OC6-HSL ⟶ GFP]"]
    P3_ENCAPSULATE_0(["Encapsulation: Phase Transfer (packing)"])
    LUXR_GFP_SENSING_CELL["SensorCell[3OC6-HSL ⟶ GFP]"]
    P4_EMBED_ULGA_0(["Embedding: Thermal Setting (packing)"])
    LUXR_GFP_CASCADE["LuxR-GFP Sensor Cascade"]

    DETECTOR_3OC6_HSL --> P1_ASSEMBLE_PLASMID_0
    REPORTER_MNEONGREEN --> P1_ASSEMBLE_PLASMID_0
    P1_ASSEMBLE_PLASMID_0 --> LUXR_GFP_PLASMID

    S30_LYSATE --> P2_ASSEMBLE_CYTOSOL_0
    LUXR_GFP_PLASMID --> P2_ASSEMBLE_CYTOSOL_0
    P2_ASSEMBLE_CYTOSOL_0 --> LUXR_GFP_SENSOR_CYTOSOL

    LUXR_GFP_SENSOR_CYTOSOL --> P3_ENCAPSULATE_0
    MEMBRANE_POPC --> P3_ENCAPSULATE_0
    OUTER_SOLUTION_GLUTAMATE --> P3_ENCAPSULATE_0
    P3_ENCAPSULATE_0 --> LUXR_GFP_SENSING_CELL

    LUXR_GFP_SENSING_CELL --> P4_EMBED_ULGA_0
    ULGA_POWDER --> P4_EMBED_ULGA_0
    P4_EMBED_ULGA_0 --> LUXR_GFP_CASCADE


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class S30_LYSATE,DETECTOR_3OC6_HSL,REPORTER_MNEONGREEN,MEMBRANE_POPC,OUTER_SOLUTION_GLUTAMATE,ULGA_POWDER leaf;
    class LUXR_GFP_PLASMID,LUXR_GFP_SENSOR_CYTOSOL,LUXR_GFP_SENSING_CELL,LUXR_GFP_CASCADE composed;
    class P1_ASSEMBLE_PLASMID_0,P2_ASSEMBLE_CYTOSOL_0,P3_ENCAPSULATE_0,P4_EMBED_ULGA_0 process;

    click S30_LYSATE "/docs/modules/s30-lysate/spec"
    click DETECTOR_3OC6_HSL "/docs/modules/detector-3oc6-hsl/spec"
    click REPORTER_MNEONGREEN "/docs/modules/reporter-mneongreen/spec"
    click MEMBRANE_POPC "/docs/modules/membrane-popc/spec"
    click OUTER_SOLUTION_GLUTAMATE "/docs/modules/outer-solution-glutamate/spec"
    click ULGA_POWDER "/docs/modules/gel-ulga/spec"
    click P2_ASSEMBLE_CYTOSOL_0 "/docs/processes/assemble-cytosol/assemble-cytosol-main"
    click P3_ENCAPSULATE_0 "/docs/processes/assemble-base-cell/main"
    click P4_EMBED_ULGA_0 "/docs/processes/embed-thermal-setting/main"
    click LUXR_GFP_CASCADE "/docs/modules/luxr-gfp-cascade/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Constituent Modules

:::{table} The Modules this cascade is built from.
:label: comp-luxr-gfp-cascade-modules

| Module | Role in this cascade |
| --- | --- |
| [Cytosol: S30 Lysate](../s30-lysate/spec.md) | Transcription and translation. Sigma-70, which this construct needs |
| [Detector: 3OC6-HSL (LuxR)](../detector-3oc6-hsl/spec.md) | Binds the analyte and activates `pLux` |
| [Reporter: mNeonGreen](../reporter-mneongreen/spec.md) | The payload `pLux` drives |
| [Membrane: POPC](../membrane-popc/spec.md) | Closes the cytosol in one encapsulation step |
| [Outer Solution: Glutamate-HEPES-Glucose](../outer-solution-glutamate/spec.md) | The phase the cell is formed into |
| [Gel: ULGA](../gel-ulga/spec.md) | Holds the cells. The board marks it `2x` against an unstated reference |
:::

::::

::::{tab-item} DNA

:::{table} The construct for this cascade is not yet in `nucleus-eng/DNA`.
:label: comp-luxr-gfp-cascade-dna

| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| `LuxR-mNeonGreen` | not recorded | — | A circular plasmid, which S30 Lysate needs because it degrades linear DNA. It is on the shared Drive as `luxr-mneongreen.gb` and is not yet in `nucleus-eng/DNA`. @Editor(london): confirm the sequence, so it can be filed there. |
| LuxR receiver | not documented | — | Not supplied separately. It is on the molecule above, under a constitutive promoter |
:::

:::{note} The two forms are not interchangeable, and this page does not say which was used
`nucleus-eng/DNA` `README.md` states that a linear cassette and its pOpen plasmid "share a cassette and are **functionally equivalent but not sequence-identical**, so a page citing one is not citing the other."

**A rule exists and one page disagrees with it.** [SensorCytosol[3OC6-HSL ⟶ PLA1]](../ahsl-sensor-cytosol/spec.md) gives the reason: **"S30 Lysate degrades linear DNA, so this route takes the plasmid."** This cascade is S30 Lysate, so that rule picks `pOpen-LuxR-deGFP`, 3890 bp. [SensorCell[3OC6-HSL ⟶ PLA1]](../ahsl-sensing-cell/spec.md) nonetheless cites the linear form, 1952 bp, for a cell that is also S30.

**Both rows are kept, and this page does not apply the rule.** Choosing one is a claim about which molecule went into a reaction, and no run record states it. @Editor(london): confirm the form, here and on the SensorCell page, and the second row can go.
:::

:::{note} Two pages give two concentrations for this plasmid
[SensorCell[3OC6-HSL ⟶ PLA1]](../ahsl-sensing-cell/spec.md) and [SensorCytosol[3OC6-HSL ⟶ PLA1]](../ahsl-sensor-cytosol/spec.md) both say `LuxR-deGFP` at **40 ng/µL** final, from a 1056 ng/µL stock, 0.95 µL per reaction. [LuxR-LacZ Sensor Cascade](../luxr-lacz-cascade/spec.md) says **37 ng/µL**. The Cytosol tab carries 40 because that row states its stock and its volume, which is the stronger claim. The disagreement is recorded here rather than resolved.
:::

::::

::::{tab-item} Cytosol

The sensing cell interior, one level deep.

:::{table} SensorCytosol[3OC6-HSL ⟶ GFP].
:label: comp-luxr-gfp-cascade-cytosol

| Component | Working concentration | Notes |
| --- | --- | --- |
| [Cytosol: S30 Lysate](../s30-lysate/spec.md) | At reaction concentration | Not separately documented for this cascade |
| `LuxR-mNeonGreen` plasmid | 40 ng/µL final | Carries both the receiver and the payload. @Editor(london): confirm the plasmid stock concentration. |
:::

::::

::::{tab-item} Membrane

:::{table} Synthetic cell membrane — [Membrane: POPC](../membrane-popc/spec.md).
:label: comp-luxr-gfp-cascade-membrane

| Component | Target percentage (%) |
| --- | --- |
| POPC | 100 |
:::

::::

:::::

# Expected Behavior

3OC6-HSL crosses the membrane, LuxR binds it, and mNeonGreen is expressed. The readout is fluorescence rather than a color change.

# Requirements

Requires observing green fluorescence, which can be done by plate reader, by microscopy, or visually under a UV lamp.

:::{attention} No process page documents the reading
@Editor: add a process page for the spectrometer reading under a UV lamp and link it here. The reading is not yet a step in the composition above.
:::

# Implementations

- [LuxR-GFP Demo](../../implementations/devstudio-luxr-gfp-demo/main.md): the cascade that demo builds.

# Processes

- [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md)
- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md)
- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md)

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
