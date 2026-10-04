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
**Position.** Refines nothing declared. Refined by nothing on this branch.
<!-- /gen:position -->

A sensing cascade that detects 3OC6-HSL in S30 lysate and reports fluorescence. LuxR binds the analyte and relieves repression of deGFP, which a spectrometer reads under a UV lamp.

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
    REPORTER_DEGFP["Reporter: deGFP"]
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
    REPORTER_DEGFP --> P1_ASSEMBLE_PLASMID_0
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
    class S30_LYSATE,DETECTOR_3OC6_HSL,REPORTER_DEGFP,MEMBRANE_POPC,OUTER_SOLUTION_GLUTAMATE,ULGA_POWDER leaf;
    class LUXR_GFP_PLASMID,LUXR_GFP_SENSOR_CYTOSOL,LUXR_GFP_SENSING_CELL,LUXR_GFP_CASCADE composed;
    class P1_ASSEMBLE_PLASMID_0,P2_ASSEMBLE_CYTOSOL_0,P3_ENCAPSULATE_0,P4_EMBED_ULGA_0 process;

    click S30_LYSATE "/docs/modules/s30-lysate/spec"
    click DETECTOR_3OC6_HSL "/docs/modules/detector-3oc6-hsl/spec"
    click REPORTER_DEGFP "/docs/modules/reporter-degfp/spec"
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

- [Cytosol: S30 Lysate](../s30-lysate/spec.md)
- [Detector: 3OC6-HSL (LuxR)](../detector-3oc6-hsl/spec.md)
- [Reporter: deGFP](../reporter-degfp/spec.md)
- [Membrane: POPC](../membrane-popc/spec.md)
- [Outer Solution: Glutamate-HEPES-Glucose](../outer-solution-glutamate/spec.md)
- [Gel: ULGA](../gel-ulga/spec.md)

::::

:::::

# Expected Behavior

3OC6-HSL crosses the membrane, LuxR binds it, and deGFP is expressed. The readout is fluorescence rather than a color change.

# Requirements

Requires a spectrometer reading of deGFP fluorescence under a UV lamp.

:::{attention} No process page documents the reading
@Editor: add a process page for the spectrometer reading under a UV lamp and link it here. The reading is not yet a step in the composition above.
:::

# Processes

- [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md)
- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md)
- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md)

# Implementations

- [LuxR-GFP Demo](../../implementations/devstudio-luxr-gfp-demo/main.md): the cascade that demo builds.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
