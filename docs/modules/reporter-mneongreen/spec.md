---
title: "Reporter: mNeonGreen"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

(reporter-mneongreen-overview)=
# Overview

<!-- gen:position -->
**Position.** Refines [Reporter](../reporter/spec.md) and [Fluorophore](../fluorophore/spec.md). Refined by nothing declared.
<!-- /gen:position -->

The mNeonGreen Reporter Module produces mNeonGreen, a monomeric green fluorescent protein derived from the lancelet *Branchiostoma lanceolatum* that can be read directly on a green fluorescence channel.

mNeonGreen excites at 506 nm and emits at 517 nm, with an extinction coefficient of 116 000 M⁻¹ cm⁻¹ and a quantum yield of 0.80. It matures in about 10 min, has a fluorescence lifetime of 3.1 ns, and has a pKa of 5.7. Reference values come from [FPbase: mNeonGreen](https://www.fpbase.org/protein/mneongreen/). [Shaner et al., 2013](https://doi.org/10.1038/nmeth.2413) first reported the protein.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. 
:::

(reporter-mneongreen-reference-composition)=
# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    BASE_CYTOSOL["Base Cytosol"]
    MNEONGREEN_DNA["mNeonGreen template"]

    P1_EXPRESS_THE_REPORTER_0(["Expression (mixing)"])
    REPORTER_MNEONGREEN["mNeonGreen Reporter"]

    BASE_CYTOSOL --> P1_EXPRESS_THE_REPORTER_0
    MNEONGREEN_DNA --> P1_EXPRESS_THE_REPORTER_0
    P1_EXPRESS_THE_REPORTER_0 --> REPORTER_MNEONGREEN


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class BASE_CYTOSOL,MNEONGREEN_DNA leaf;
    class REPORTER_MNEONGREEN composed;
    class P1_EXPRESS_THE_REPORTER_0 process;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click P1_EXPRESS_THE_REPORTER_0 "/docs/processes/express/main"
    click REPORTER_MNEONGREEN "/docs/modules/reporter-mneongreen/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

:::{table} Templates carrying the mNeonGreen coding sequence.
:label: comp-reporter-mneongreen-constructs

| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `T7-mNG-T7term` | 1079 | Not yet in `nucleus-eng/DNA` |
| `T7-[EsaO]2-mNG-T7term` | 1118 | [pT7-EsaO-EsaO-mNG-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/detector-esar/pT7-EsaO-EsaO-mNG-linear.gb) |
| `T7-[EsaO]-mNG-T7term` | 1098 | [pT7-EsaO-mNG-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/detectors/detector-esar/pT7-EsaO-mNG-linear.gb) |
:::

The coding sequence is mNeonGreen as published (711 bp, 236 amino acids plus a stop codon).

`T7-mNG-T7term` contains the coding sequence of mNeonGreen under constituitive expression. The other two constructs carry the same coding sequence under control of an operator site (`EsaO` belonging to [Detector: 3OC6-HSL (EsaR)](../detector-esar/spec.md).

:::{attention} The sequence file for `T7-mNG-T7term` is not in `nucleus-eng/DNA`
The DevNote holds the sequence. Every gated reading is scaled against this template, so its file is the one to add first.

@Editor: London Node to add the file to `nucleus-eng/DNA` as a linear sequence and compare its length with its `LOCUS` line. The DevNote's copy reads `circular` in its `LOCUS` line, and the template is linear.
:::

::::

::::{tab-item} Cytosol

:::{table} The reporter reaction as assembled in Base Cytosol, with no repressor and no operator in it.
:label: comp-reporter-mneongreen-cytosol

| Component | Stock concentration | Final concentration |
| --- | --- | --- |
| [Base Cytosol](../base-cytosol/spec.md) | - | 1× |
| `T7-mNG-T7term` template | - | 3 nM |
| RNase inhibitor | 40 U/µL | 1 U/µL |
:::
::::

:::::

(reporter-mneongreen-expected-behavior)=
# Expected Behavior

The mNeonGreen Reporter Module is expected to give green fluorescence that rises over the course of a reaction, with no substrate added and no second molecule required.

(reporter-mneongreen-cytosols)=
## Cytosols

The Module runs in both [Base Cytosol](../base-cytosol/spec.md) and [S30 Lysate](../s30-lysate/spec.md). In Base Cytosol, fluorescence was read on a Synergy 2 plate reader as a 6 h kinetic at 37 °C with a reading every 5 min. The readings were made against a fluorescein ladder at (0, 0.5, 1 and 2) µM. No reaction yield or kinetics, or DNA template concentration is recorded.

:::{attention} mNeonGreen fluorescence is at the blue end of the standard green channel.
Every reading reported here was recorded on the standard green channel: 485/20 excitation, 528/20 emission. mNeonGreen own maxima (ex: 506 nm, em: 517 nm) sit on the blue end of the filter's range. Monochromators set to the specific excitation and emission peaks of mNeonGreen may collect more of the signal. 
:::

:::{attention} Missing primary data.
No plot of this Module alone exists. 
:::

(reporter-mneongreen-cells)=
## Cells

:::{warning} Not yet validated
This Module has not been demonstrated in a synthetic cell. Every reading on record is bulk cytosol.
:::

(reporter-mneongreen-requirements)=
# Requirements

Requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md), [S30 Lysate](../s30-lysate/spec.md)).

Requires a reader that can excite near 506 nm and collect near 517 nm (e.g. a standard green channel, which collects the protein at the blue edge of its range).

mNeonGreen is sensitive to acid. Its reported pKa is 5.7, so fluorescence falls as a compartment acidifies.

(reporter-mneongreen-processes)=
# Processes

- [Expression](../../processes/express/main.md): makes the protein from the template, in the compartment that reads it.

