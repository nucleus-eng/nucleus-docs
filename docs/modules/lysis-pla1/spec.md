---
title: "Lysis: PLA1"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

(lysis-pla1-overview)=
# Overview

The PLA1 Lysis Module uses phospholipase A1 (PLA1) to genetically encode lysis. Once expressed, PLA1 degrades phospholipid membranes and lyses cells, including its neighbors. Lysis releases chemical payloads from neighboring liposomes (e.g. [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md)) into an external solution. An example is a solution that contains [Reporter: LacZ](../reporter-lacz/spec.md), which triggers a [colorimetric signal](../../processes/colorimetric-readout/main.md). PLA1 can sit downstream of a sensing circuit that controls when it is expressed (e.g. [Detector: tetR-aTc](../detector-tetr-atc/spec.md)).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} PLA1 is characterized only through a color readout
One configuration removes the sensing circuit: constitutive expression in Base Cytosol, described under Expected Behavior. It supplies the only DNA dose and timing figures attributable to PLA1 alone.

No result isolates PLA1 from the CPRG/LacZ readout. Every lysis result is scored by the color it releases. No result comes from a direct measure of membrane rupture or of enzyme activity. No efficiency figure exists for PLA1 in any configuration.
:::

(lysis-pla1-reference-composition)=
# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    BASE_CYTOSOL["Base Cytosol"]
    PLA1_DNA["T7pro-PLA1-T7term"]
    OPTIPREP["OptiPrep"]

    P1_ASSEMBLE_PLA1_INNER_SOLUTION_0(["Assemble the ungated PLA1 inner solution (mixing) — no page"])
    LYSIS_PLA1["Lysis: PLA1"]

    BASE_CYTOSOL --> P1_ASSEMBLE_PLA1_INNER_SOLUTION_0
    PLA1_DNA --> P1_ASSEMBLE_PLA1_INNER_SOLUTION_0
    OPTIPREP --> P1_ASSEMBLE_PLA1_INNER_SOLUTION_0
    P1_ASSEMBLE_PLA1_INNER_SOLUTION_0 --> LYSIS_PLA1


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class BASE_CYTOSOL,PLA1_DNA,OPTIPREP leaf;
    class LYSIS_PLA1 composed;
    class P1_ASSEMBLE_PLA1_INNER_SOLUTION_0 process;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click LYSIS_PLA1 "/docs/modules/lysis-pla1/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

:::{table} DNA constructs that express PLA1, with their supply route.
:label: comp-pla1-dna

| Name | Length (bp) | File | Supply route |
| --- | --- | --- | --- |
| `T7pro-PLA1-T7term` | Not yet determined | Not yet in `nucleus-eng/DNA` | pT7 (constitutive). Supply form unknown. |
| `pT7-tetO-PLA1-linear` | 1202 | [pT7-tetO-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/effectors/detector-tetr-atc/pT7-tetO-PLA1-linear.gb) | Linear template with `T7`, `TetO`, an RBS, the `T7hyb6` terminator and PLA1 on one molecule. aTc-gated configuration. |
| `pOpen-T7-tetO-PLA1` | 3140 | [pOpen-T7-tetO-PLA1.gb](https://github.com/nucleus-eng/DNA/blob/main/effectors/detector-tetr-atc/pOpen-T7-tetO-PLA1.gb) | Circular plasmid in the pOpen backbone, carrying the `T7`, `TetO`, RBS and PLA1 elements of `pT7-tetO-PLA1-linear`. |
| `LuxR-PLA1-linear` | 2237 | [LuxR-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/effectors/detector-3oc6-hsl/LuxR-PLA1-linear.gb) | `BBa_J23101`→`luxR` (constitutive σ70) with `pLux`-driven PLA1 on one molecule. Used in the London 3OC6-HSL cascade. Also referred to as `P70lux-PLA1-term`. |
| `pOpen-LuxR-PLA1` | 4175 | [pOpen-LuxR-PLA1.gb](https://github.com/nucleus-eng/DNA/blob/main/effectors/detector-3oc6-hsl/pOpen-LuxR-PLA1.gb) | Circular plasmid in the pOpen backbone, carrying the `BBa_J23101`→`luxR` and `pLux`-driven PLA1 elements of `LuxR-PLA1-linear`. |
| `pT7-toehold9-PLA1-linear` | 1203 | [pT7-toehold9-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/main/effectors/detector-ph/pT7-toehold9-PLA1-linear.gb) | Linear template with `T7`, `toehold 9`, PLA1 and the `T7hyb6` terminator on one molecule. pH-gated configuration. |
:::

:::{attention} `T7pro-PLA1-T7term` is not in `nucleus-eng/DNA`
@Editor: `T7pro-PLA1-T7term` has no confirmed sequence file in [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA). b.next to add the file there. Then confirm that it matches the construct by `LOCUS` length, not by name, and add its length and file to the table above.
:::

The two sequences are interchangeable at the protein level and distinct at the DNA level (codon usage). Substituting one sequence for the other changes the construct, but not the resulting enzyme or behavior. Length cannot tell them apart.

::::

::::{tab-item} Cytosol

PLA1 is expressed from one of the constructs above rather than added as a reagent, so it has no working concentration of its own.

:::{table} PLA1 DNA dose, by configuration.
:label: comp-pla1-cytosol

| Configuration | Construct | Working concentration |
| --- | --- | --- |
| Constitutive, ungated | `T7pro-PLA1-T7term` | 14 ng/µL |
| aTc-gated | `TetO-PLA1` | 1 nM |
| 3OC6-HSL-gated | `LuxR-PLA1` | 15 ng/µL |
| pH-gated | Toehold-switch-gated PLA1 template | 2 nM |
:::

The cytosol depends on the host configuration. The aTc-gated, pH-gated and theophylline-gated cascades and the ungated run use [Base Cytosol](../base-cytosol/spec.md). The London 3OC6-HSL cascade uses [S30 Lysate](../s30-lysate/spec.md).

::::

<!-- composition-tabs: no-table (PLA1 acts on any phospholipid membrane in reach, so a single lipid table would be wrong) -->
::::{tab-item} Membrane

PLA1 lyses a membrane, so a membrane is part of every configuration that uses it. No lipid composition is specific to this Module. The membranes used with it are [Membrane: POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md) and [Membrane: POPC](../membrane-popc/spec.md).

The two-liposome cascades also use the membrane of a neighboring [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md).

::::

:::::

(lysis-pla1-expected-behavior)=
# Expected Behavior

(lysis-pla1-cells)=
## Cells

The PLA1 Lysis Module is expected to lyse the synthetic cell that expresses PLA1 and the synthetic cells near it. One documented configuration reports on PLA1 rather than on a cascade, because nothing gates it.

In the London constitutive configuration, `T7pro-PLA1-T7term` at 14 ng/µL in [Base Cytosol](../base-cytosol/spec.md) liposomes drives the two-liposome CPRG/LacZ handoff with no sensing circuit. Color appears from about 3 h at 37 °C and is easily discernible by 16 h, against a minus-DNA control in the same run (read as in [Colorimetric Readout](../../processes/colorimetric-readout/main.md)). The result was reproduced across multiple days, so a visible result is expected on that timescale at this dose. The outer solution is 1200 mM glucose and 0.1 mM CaCl₂ with 15 mg/mL ultra-low-gelling agarose (ULGA), which makes this the gel format (see [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md)).

Every other configuration on record puts a sensing circuit in front of PLA1, so PLA1 and its gate cannot be told apart. A weak result there can come from either.

:::{attention} Source for the constitutive result
@Editor: Cite the DevNote or data for the constitutive timing and for the reproduction across days.
:::

(lysis-pla1-requirements)=
# Requirements

Requires a phospholipid membrane to lyse (e.g. [Membrane: POPC](../membrane-popc/spec.md), [Membrane: POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md)).

PLA1 imposes lysis on any phospholipid membrane in reach. It cannot distinguish the membrane that expressed it from a neighbor's, or one population from another that shares its composition. Take a sensing cell and a substrate carrier that share one membrane formulation. PLA1 reaching the carrier is the intended path. PLA1 reaching another sensing cell is not. Nothing in the chemistry separates them. A composition that needs them separated must state that requirement itself.

PLA1 requires a low noise floor in whatever drives it, and any color change module built on PLA1 inherits that requirement. Three separate causes break that requirement:

1. Leaky promoter. In [SensorCell[3OC6-HSL ⟶ PLA1]](../ahsl-sensing-cell/spec.md), PLA1 is expressed without 3OC6-HSL. It colors nearly as much as the induced state, so the dynamic range is gone.
2. Membrane that does not outlive the reaction. In [Cell: Base Cytosol, POPC/Chol (9:1)](../cell-base-cytosol-popc-chol/spec.md) GUVs, PLA1 takes 10 to 12 h to lyse them, and the GUVs leak on their own over that window. The negative control also colors: slightly purple against slightly more purple when induced.
3. Leaky gate. The pH path's own template is leaky. The function test for `pT7-toehold9-PLA1` is recorded as leaky, so the toehold gate passes some transcription with no trigger present.

The detector is the component that fails this requirement. The LacZ/CPRG reaction does not fail it. No numeric threshold is defined for how low the noise floor has to be.

:::{attention} Sources for the noise-floor observations
@Editor: The London Node to cite the DevNote or data for the background PLA1 expression without 3OC6-HSL.

@Editor: The Chicago Node to cite the GUV leak, and the statement that the detector, not the LacZ/CPRG reaction, fails the requirement. State whether that statement covers the gel-driven release described below, which is not a detector failure.

@Editor: Cite a source for the leaky function test on `pT7-toehold9-PLA1`.

The negative-control color above comes from a gel attempt in which CPRG-loaded LUVs with β-galactosidase and no PLA1-expressing cells developed color on their own. That color is a release of substrate, not a detector failure. @Editor: Cite that gel attempt.
:::

Requires an upstream sensing circuit (e.g. [Detector: 3OC6-HSL (LuxR)](../detector-3oc6-hsl/spec.md), [Detector: tetR-aTc](../detector-tetr-atc/spec.md)) only where lysis needs to be conditional. Expressed constitutively, PLA1 lyses on its own schedule.

Requires pT7 transcription and translation, when using `T7pro-PLA1-T7term` (e.g. [Base Cytosol](../base-cytosol/spec.md)).

Requires σ70 transcription and translation, when using `LuxR-PLA1` (e.g. [S30 Lysate](../s30-lysate/spec.md)).

Do not add Gramicidin A to a colorimetric cascade. See [Expected Behavior](#lysis-pla1-expected-behavior) for why.

(lysis-pla1-implementations)=
# Implementations

- [aTc Demo](../../implementations/devstudio-atc-demo/main.md): the lysis step, expressed from `TetO-PLA1`.
- [CRAIC Demo](../../implementations/devstudio-craic-demo/main.md): the lysis step, expressed once repression lifts.
- [pH Demo](../../implementations/devstudio-ph-demo/main.md): the lysis step, expressed from the `pT7-toehold9-PLA1` template.

(lysis-pla1-processes)=
# Processes

- [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md): applies only where LacZ is encapsulated. Proteinase K cannot distinguish one LacZ from another, so in a configuration that puts LacZ in the outer solution, it digests the reporter.
- [Colorimetric Readout](../../processes/colorimetric-readout/main.md): the CPRG conversion that produces the visible signal.
- [Embedding: Ionic Crosslinking](../../processes/embed-ionic-crosslinking/main.md): ionic crosslinking of alginate.
- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md): thermal gelation of ultra-low-gelling agarose.

(lysis-pla1-constituent-modules)=
# Constituent Modules

- [Base Cytosol](../base-cytosol/spec.md): transcription and translation, for the ungated configuration.

(lysis-pla1-credits)=
# Credits

Developed by Jonah McDonald and Charlie Newell (London Node) and Mary Kelly (Chicago Node, Kamat Lab).

:::{attention} Credits need confirmation
@Editor: Confirm each credit with the Node before this page merges to `main`.
:::
