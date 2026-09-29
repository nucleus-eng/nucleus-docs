---
title: "CRAIC"
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

A sensing cascade that detects 3OC6-HSL in [Base Cytosol](../base-cytosol/spec.md) and reports a color change. EsaR relieves repression of PLA1, PLA1 lyses the compartments, and LacZ reaches CPRG to produce chlorophenol red.

**CRAIC expands to "Colorimetric Reporter for AHL In Cytosol".** AHL became 3OC6-HSL on 2026-09-24, so the acronym carries a retired name. It is kept because it is the demo's own name.

**This is one of two 3OC6-HSL demos, and they are not variants of one design.** The other is [LuxR-GFP Sensor Cascade](../luxr-gfp-cascade/spec.md), which senses the same analyte in S30 lysate and reports fluorescence.

**This is the only demo that builds two bounded compartments and merges them.** One branch makes the sensing cell and the other makes the substrate carrier. Both reach one gel embed, which is the separation invariant of [Color Change](../color-change/spec.md) drawn concretely: the enzyme and its substrate arrive in one gel in two compartments.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    BASE_CYTOSOL["Base Cytosol"]
    ESAR_DNA["Sensor: EsaR DNA template"]
    EFFECTOR_PLA1["Lysis: PLA1"]
    MEMBRANE_CRAIC["Membrane"]
    OUTER_SOLUTION["Outer Solution"]
    SUBSTRATE_CPRG["Substrate: CPRG"]
    REPORTER_LACZ_ENZYME["LacZ Enzyme"]
    ULGA_POWDER["ULGA powder"]
    ANALYTE_3OC6_HSL["Analyte: 3OC6-HSL"]

    P1_EXPRESS_REPRESSOR_0(["Assemble Solution (mixing)"])
    ESAR_REPRESSOR["Sensor: EsaR Repressor"]
    P2_ASSEMBLE_CYTOSOL_0(["Assemble Cytosol (mixing)"])
    CRAIC_SENSOR_CYTOSOL["SensorCytosol[3OC6-HSL ⟶ PLA1]"]
    P3_ENCAPSULATE_SENSING_0(["Encapsulation (packing)"])
    CRAIC_SENSING_CELL["SensorCell[3OC6-HSL ⟶ PLA1]"]
    P4_ENCAPSULATE_SUBSTRATE_0(["Encapsulation (packing)"])
    CRAIC_SUBSTRATE_CARRIER["Substrate Carrier{CPRG}"]
    P5_EMBED_ULGA_0(["Embedding: Thermal Setting (packing)"])
    CRAIC_CASCADE["CRAIC"]
    P6_DEVELOP_0(["Color Development (mixing)"])
    CRAIC_CASCADE_DEVELOPED["CRAIC′"]

    BASE_CYTOSOL --> P1_EXPRESS_REPRESSOR_0
    ESAR_DNA --> P1_EXPRESS_REPRESSOR_0
    P1_EXPRESS_REPRESSOR_0 --> ESAR_REPRESSOR

    BASE_CYTOSOL --> P2_ASSEMBLE_CYTOSOL_0
    ESAR_REPRESSOR --> P2_ASSEMBLE_CYTOSOL_0
    EFFECTOR_PLA1 --> P2_ASSEMBLE_CYTOSOL_0
    P2_ASSEMBLE_CYTOSOL_0 --> CRAIC_SENSOR_CYTOSOL

    CRAIC_SENSOR_CYTOSOL --> P3_ENCAPSULATE_SENSING_0
    MEMBRANE_CRAIC --> P3_ENCAPSULATE_SENSING_0
    OUTER_SOLUTION --> P3_ENCAPSULATE_SENSING_0
    P3_ENCAPSULATE_SENSING_0 --> CRAIC_SENSING_CELL

    SUBSTRATE_CPRG --> P4_ENCAPSULATE_SUBSTRATE_0
    MEMBRANE_CRAIC --> P4_ENCAPSULATE_SUBSTRATE_0
    OUTER_SOLUTION --> P4_ENCAPSULATE_SUBSTRATE_0
    P4_ENCAPSULATE_SUBSTRATE_0 --> CRAIC_SUBSTRATE_CARRIER

    CRAIC_SENSING_CELL --> P5_EMBED_ULGA_0
    CRAIC_SUBSTRATE_CARRIER --> P5_EMBED_ULGA_0
    REPORTER_LACZ_ENZYME --> P5_EMBED_ULGA_0
    ULGA_POWDER --> P5_EMBED_ULGA_0
    P5_EMBED_ULGA_0 --> CRAIC_CASCADE

    CRAIC_CASCADE --> P6_DEVELOP_0
    ANALYTE_3OC6_HSL --> P6_DEVELOP_0
    P6_DEVELOP_0 --> CRAIC_CASCADE_DEVELOPED


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class BASE_CYTOSOL,ESAR_DNA,EFFECTOR_PLA1,MEMBRANE_CRAIC,OUTER_SOLUTION,SUBSTRATE_CPRG,REPORTER_LACZ_ENZYME,ULGA_POWDER,ANALYTE_3OC6_HSL leaf;
    class ESAR_REPRESSOR,CRAIC_SENSOR_CYTOSOL,CRAIC_SENSING_CELL,CRAIC_SUBSTRATE_CARRIER,CRAIC_CASCADE,CRAIC_CASCADE_DEVELOPED composed;
    class P1_EXPRESS_REPRESSOR_0,P2_ASSEMBLE_CYTOSOL_0,P3_ENCAPSULATE_SENSING_0,P4_ENCAPSULATE_SUBSTRATE_0,P5_EMBED_ULGA_0,P6_DEVELOP_0 process;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click EFFECTOR_PLA1 "/docs/modules/effector-pla1/spec"
    click OUTER_SOLUTION "/docs/modules/outer-solution/spec"
    click SUBSTRATE_CPRG "/docs/modules/substrate-cprg/spec"
    click REPORTER_LACZ_ENZYME "/docs/modules/reporter-lacz-enzyme/spec"
    click ULGA_POWDER "/docs/modules/gel-ulga/spec"
    click ANALYTE_3OC6_HSL "/docs/modules/analyte-3oc6-hsl/spec"
    click P1_EXPRESS_REPRESSOR_0 "/docs/processes/assemble-cytosol/assemble-cytosol-main"
    click P2_ASSEMBLE_CYTOSOL_0 "/docs/processes/assemble-cytosol/assemble-cytosol-main"
    click P3_ENCAPSULATE_SENSING_0 "/docs/processes/encapsulate/main"
    click P4_ENCAPSULATE_SUBSTRATE_0 "/docs/processes/encapsulate/main"
    click P5_EMBED_ULGA_0 "/docs/processes/embed-thermal-setting/main"
    click CRAIC_CASCADE "/docs/modules/craic-cascade/spec"
    click P6_DEVELOP_0 "/docs/processes/color-development/main"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Constituent Modules

- [Base Cytosol](../base-cytosol/spec.md)
- Sensor: EsaR DNA template — no page
- [Lysis: PLA1](../effector-pla1/spec.md)
- Membrane — formulation not chosen on the board
- [Outer Solution](../outer-solution/spec.md)
- [Substrate: CPRG](../substrate-cprg/spec.md)
- [LacZ Enzyme](../reporter-lacz-enzyme/spec.md)
- [Gel: ULGA](../gel-ulga/spec.md)
- [Analyte: 3OC6-HSL](../analyte-3oc6-hsl/spec.md)

::::

:::::

# Expected Behavior

3OC6-HSL relieves EsaR repression, PLA1 is expressed and lyses the compartments, and LacZ meets CPRG in the gel. The readout is the yellow-to-red change of chlorophenol red.

# Requirements

Requires EsaR, which has no module page. [Detector: 3OC6-HSL](../detector-3oc6-hsl/spec.md) documents LuxR and mentions EsaR only in passing, so it does not specify this cascade's sensing leg.

Requires an observation step this corpus does not describe. The board draws one and `observe` carries no profile on the theory side.

# Processes

- [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md)
- [Encapsulation](../../processes/encapsulate/main.md)
- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md)
- [Color Development](../../processes/color-development/main.md)

# Credits

Transcribed from the DevStudio whiteboard of 2026-09-24. Structure follows that board.
