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
**Position.** Refines [Cascade](../cascade/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

A sensing cascade that detects 3OC6-HSL in [Base Cytosol](../base-cytosol/spec.md) and reports a color change. EsaR relieves repression of PLA1, PLA1 lyses the compartments, and LacZ reaches CPRG to produce chlorophenol red.

**CRAIC expands to "Colorimetric Reporter for AHL In Cytosol".** The "AHL" in the name stands for the analyte, 3OC6-HSL.

**This is one of two 3OC6-HSL demos.** The other is [LuxR-GFP Sensor Cascade](../luxr-gfp-cascade/spec.md), which senses the same analyte in S30 lysate and reports fluorescence.

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
    EFFECTOR_PLA1_ESAO["Gated lysis DNA: [EsaO]2-PLA1"]
    MEMBRANE["Membrane"]
    OUTER_SOLUTION["Outer Solution"]
    SUBSTRATE_CPRG["Substrate: CPRG"]
    REPORTER_LACZ_ENZYME["LacZ Enzyme"]
    ULGA_POWDER["ULGA powder"]
    ANALYTE_3OC6_HSL["Analyte: 3OC6-HSL"]

    P1_EXPRESS_REPRESSOR_0(["Expression (mixing)"])
    DETECTOR_ESAR["Detector: 3OC6-HSL (EsaR)"]
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
    P1_EXPRESS_REPRESSOR_0 --> DETECTOR_ESAR

    BASE_CYTOSOL --> P2_ASSEMBLE_CYTOSOL_0
    DETECTOR_ESAR --> P2_ASSEMBLE_CYTOSOL_0
    EFFECTOR_PLA1_ESAO --> P2_ASSEMBLE_CYTOSOL_0
    P2_ASSEMBLE_CYTOSOL_0 --> CRAIC_SENSOR_CYTOSOL

    CRAIC_SENSOR_CYTOSOL --> P3_ENCAPSULATE_SENSING_0
    MEMBRANE --> P3_ENCAPSULATE_SENSING_0
    OUTER_SOLUTION --> P3_ENCAPSULATE_SENSING_0
    P3_ENCAPSULATE_SENSING_0 --> CRAIC_SENSING_CELL

    SUBSTRATE_CPRG --> P4_ENCAPSULATE_SUBSTRATE_0
    MEMBRANE --> P4_ENCAPSULATE_SUBSTRATE_0
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
    class BASE_CYTOSOL,ESAR_DNA,EFFECTOR_PLA1_ESAO,MEMBRANE,OUTER_SOLUTION,SUBSTRATE_CPRG,REPORTER_LACZ_ENZYME,ULGA_POWDER,ANALYTE_3OC6_HSL leaf;
    class DETECTOR_ESAR,CRAIC_SENSOR_CYTOSOL,CRAIC_SENSING_CELL,CRAIC_SUBSTRATE_CARRIER,CRAIC_CASCADE,CRAIC_CASCADE_DEVELOPED composed;
    class P1_EXPRESS_REPRESSOR_0,P2_ASSEMBLE_CYTOSOL_0,P3_ENCAPSULATE_SENSING_0,P4_ENCAPSULATE_SUBSTRATE_0,P5_EMBED_ULGA_0,P6_DEVELOP_0 process;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click OUTER_SOLUTION "/docs/modules/outer-solution/spec"
    click SUBSTRATE_CPRG "/docs/modules/substrate-cprg/spec"
    click REPORTER_LACZ_ENZYME "/docs/modules/reporter-lacz-enzyme/spec"
    click ULGA_POWDER "/docs/modules/gel-ulga/spec"
    click ANALYTE_3OC6_HSL "/docs/modules/analyte-3oc6-hsl/spec"
    click P1_EXPRESS_REPRESSOR_0 "/docs/processes/express/main"
    click DETECTOR_ESAR "/docs/modules/detector-esar/spec"
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

:::{table} The Modules this cascade is built from.
:label: comp-craic-cascade-modules

| Module | Role in this cascade |
| --- | --- |
| [Base Cytosol](../base-cytosol/spec.md) | Transcription and translation |
| Sensor: EsaR DNA template | Expresses the EsaR repressor. No page |
| `[EsaO]2-PLA1` | The gated lysis construct. Two tandem EsaO operator sites driving PLA1, on one molecule. No page and no sequence file |
| Membrane | Closes the cytosol. Formulation not specified |
| [Outer Solution](../outer-solution/spec.md) | The phase the cell is formed into |
| [Substrate: CPRG](../substrate-cprg/spec.md) | Held in a second population of carriers, apart from the enzyme |
| [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) | Added as purified enzyme, not expressed |
| [Gel: ULGA](../gel-ulga/spec.md) | Holds both populations |
| [Analyte: 3OC6-HSL](../analyte-3oc6-hsl/spec.md) | The trigger, supplied at development |
:::

**PLA1 is not a separate addition.** It is carried on `[EsaO]2-PLA1` together with the operator that gates it, so the protein is expressed inside the cell rather than mixed in. The protein itself is described on the Lysis: PLA1 page, `../effector-pla1/spec.md`.

::::

::::{tab-item} DNA

:::{warning} Both constructs were built. Neither has a sequence file
`T7-[EsaO]2-PLA1-T7term` and `T7-EsaR(D91G)-T7term` were prepared as linear templates on 2026-09-23, with the five other templates of that batch, and the repressor template has been run in four experiments. So the constructs are attested.

**The sequence files are not.** Neither is in the Nucleus DNA repository: no `esa` file, no `esar` entry and no manifest row, while the equivalent gated construct is present for each of the other three demos. The repressor template's length is read from a sequence held outside that repository; the gated lysis construct has no sequence anywhere. **No file is linked on a name resemblance.**

@Editor: submit both sequences before this Module is used at the bench.
:::

:::{table} Constructs named by the design. A length is given only where a sequence exists to read it from.
:label: comp-craic-cascade-dna

| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| `T7-[EsaO]2-PLA1-T7term` | not documented | none | The gated lysis construct. Two tandem EsaO sites driving PLA1. Expressed in the sensing cell |
| `T7-EsaR(D91G)-T7term` | 1118 | none in `nucleus-eng/DNA` | Expresses the repressor, a D91G point mutant, which binds the operator above until the analyte arrives |
| LacZ | — | — | Not DNA here. Added as purified enzyme |
:::

:::{note} The second construct on the detector page characterizes rather than builds
`[EsaO]2-mNG` puts the same operator on a fluorescent reporter. It measures the detector and is not part of this cascade, which is colorimetric.
:::

::::

::::{tab-item} Cytosol

The sensing cell interior.

:::{table} Sensing cell interior. No working concentration is documented for this cascade.
:label: comp-craic-cascade-cytosol

| Component | Working concentration |
| --- | --- |
| [Base Cytosol](../base-cytosol/spec.md) components | At reaction concentration; not separately documented for this cascade |
| EsaR DNA template | not documented |
| `[EsaO]2-PLA1` | not documented |
:::

**No dose is recorded for this cascade.** The other three demos each state one for their gated construct. This tab lists the components so the composition is stated, and says the figures are absent rather than leaving the tab out.

::::

::::{tab-item} Membrane

:::{table} Synthetic cell membrane. The formulation is not specified.
:label: comp-craic-cascade-membrane

| Component | Target percentage (%) |
| --- | --- |
| not documented | — |
:::

**The source names two membranes and no formulation for either.** They are written only as distinct, one for the sensing cell and one for the substrate carrier, so this tab records that a membrane exists and that its composition is unstated.

::::

::::{tab-item} Substrate

:::{table} CPRG in the CRAIC path.
:label: comp-craic-cascade-substrate

| Component | Working concentration | Notes |
| --- | --- | --- |
| [Substrate: CPRG](../substrate-cprg/spec.md) | not documented | Held in its own carrier population, separate from the LacZ enzyme, until lysis releases it |
:::

::::

:::::

# Expected Behavior

3OC6-HSL relieves EsaR repression, PLA1 is expressed and lyses the compartments, and LacZ meets CPRG in the gel. The readout is the yellow-to-red change of chlorophenol red.

# Requirements

Requires EsaR as the 3OC6-HSL-responsive repressor (see [Detector: 3OC6-HSL (EsaR)](../detector-esar/spec.md)).

Requires an observation step to read the color change.

:::{attention} Gaps in this cascade's specification
@Editor: name the membrane formulation, add a Module page for the EsaR DNA template, and add a Process page for the observation step.
:::

# Implementations

- [CRAIC Demo](../../implementations/devstudio-craic-demo/main.md): the cascade that demo builds.

# Processes

- [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md)
- [Encapsulation](../../processes/encapsulate/main.md)
- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md)
- [Color Development](../../processes/color-development/main.md)

# Credits

:::{attention} Credits missing
@Editor: name the developers of this cascade, with their Node and Lab.
:::
