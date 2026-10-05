---
title: "SensorCytosol[pH ⟶ PLA1]"
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

The SensorCytosol[pH ⟶ PLA1] is the aqueous phase of the [SensorCell[pH ⟶ PLA1]](../ph-sensing-cell/spec.md): [Base Cytosol](../base-cytosol/spec.md) carrying the [pH-Sensing Module](../detector-ph/spec.md) — an annealed trigger duplex and a toehold-gated template — together with the [PLA1 Lysis Module](../effector-pla1/spec.md) the toehold switch gates. It is mixed before encapsulation, not added to a closed compartment.

Compare the [SensorCytosol[aTc ⟶ PLA1]](../atc-sensor-cytosol/spec.md), which shares the Base Cytosol background and swaps the detector. This cytosol carries **no** reporter enzyme: the pH path reports through CPRG released on lysis, and the LacZ that converts it is dispersed in the gel.

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
    PH_RESPONSIVE_SSDNA["pH-responsive ssDNA"]
    TRIGGER_SSDNA["Trigger ssDNA"]
    EFFECTOR_PLA1_TOEHOLD["Gated lysis DNA: pT7-toehold9-PLA1"]

    P1_ANNEAL_TRIGGER_DUPLEX_0(["Anneal pH-Responsive Trigger Duplex (mixing)"])
    PH_TRIGGER_DUPLEX["pH trigger duplex"]
    P2_ASSEMBLE_CYTOSOL_0(["Assemble Cytosol (mixing)"])
    PH_SENSOR_CYTOSOL["SensorCytosol[pH ⟶ PLA1]"]

    PH_RESPONSIVE_SSDNA --> P1_ANNEAL_TRIGGER_DUPLEX_0
    TRIGGER_SSDNA --> P1_ANNEAL_TRIGGER_DUPLEX_0
    P1_ANNEAL_TRIGGER_DUPLEX_0 --> PH_TRIGGER_DUPLEX

    BASE_CYTOSOL --> P2_ASSEMBLE_CYTOSOL_0
    PH_TRIGGER_DUPLEX --> P2_ASSEMBLE_CYTOSOL_0
    EFFECTOR_PLA1_TOEHOLD --> P2_ASSEMBLE_CYTOSOL_0
    P2_ASSEMBLE_CYTOSOL_0 --> PH_SENSOR_CYTOSOL


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class BASE_CYTOSOL,PH_RESPONSIVE_SSDNA,TRIGGER_SSDNA,EFFECTOR_PLA1_TOEHOLD leaf;
    class PH_TRIGGER_DUPLEX,PH_SENSOR_CYTOSOL composed;
    class P1_ANNEAL_TRIGGER_DUPLEX_0,P2_ASSEMBLE_CYTOSOL_0 process;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click P1_ANNEAL_TRIGGER_DUPLEX_0 "/docs/processes/anneal-ph-trigger-duplex/main"
    click PH_TRIGGER_DUPLEX "/docs/modules/detector-ph/spec"
    click P2_ASSEMBLE_CYTOSOL_0 "/docs/processes/assemble-cytosol/assemble-cytosol-main"
    click PH_SENSOR_CYTOSOL "/docs/modules/ph-sensor-cytosol/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

:::{table} Constructs in the SensorCytosol[pH ⟶ PLA1].
| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| `pT7-toehold9-PLA1` | 1203 | [pT7-toehold9-PLA1-linear.gb](https://github.com/nucleus-eng/DNA/blob/devcells/devstudio-constructs/effectors/detector-ph/pT7-toehold9-PLA1-linear.gb) | Expressed in the cytosol at 2 nM |
| pH-responsive ssDNA | 49 | [pH-responsive-ssDNA-2.gb](https://github.com/nucleus-eng/DNA/blob/devcells/devstudio-constructs/detectors/detector-ph/pH-responsive-ssDNA-2.gb) | Synthesized oligonucleotide, annealed before mixing |
| trigger ssDNA | 36 | [trigger-ssDNA-3.gb](https://github.com/nucleus-eng/DNA/blob/devcells/devstudio-constructs/detectors/detector-ph/trigger-ssDNA-3.gb) | Synthesized oligonucleotide, annealed before mixing |
:::

The toehold switch and the effector are on one molecule, so [PLA1](../effector-pla1/spec.md) has no construct of its own here.

::::

::::{tab-item} Cytosol

:::{table} Cytosolic components of the SensorCytosol[pH ⟶ PLA1], at reaction concentration.
| Module | Working concentration | Notes |
| --- | --- | --- |
| [Base Cytosol](../base-cytosol/spec.md) | At reaction concentration | Transcription and translation |
| [pH-Sensing Module](../detector-ph/spec.md) | `pT7-toehold9-PLA1` template at 2 nM; pH-responsive ssDNA : trigger ssDNA duplex (3:1, annealed) at 4.625 µM trigger ssDNA | The duplex is annealed before it enters this mixture — see Process |
| [PLA1 Lysis Module](../effector-pla1/spec.md) | Covered by the 2 nM toehold-gated template | The switch and the effector are on one molecule |
| Optiprep | 4.5% (v/v) | Density agent for the phase-transfer step. Present in the encapsulated reaction and not in the bulk one |
| RNase inhibitor | 1000 U/mL | Half the 2000 U/mL used in the bulk module reaction |
| Sulfo-Cyanine5 | 2 µM, optional | Membrane-independent fill marker, used when the lumen needs to be visible. Sulfo-Cyanine5 carboxylic acid, Lumiprobe 13390 |
:::

::::

:::::

# Process

- [Anneal pH-Responsive Trigger Duplex](../../processes/anneal-ph-trigger-duplex/main.md) — anneals the sensing and trigger strands into the single duplex reagent, **before** this cytosol is mixed.
- [Assemble Base Cytosol](../../processes/assemble-base-cytosol/main.md) — produces the Base Cytosol background.

This cytosol is consumed by [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md), which combines it with the [Membrane: POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md) to form the [SensorCell[pH ⟶ PLA1]](../ph-sensing-cell/spec.md).

# Constituent Modules

- [Base Cytosol](../base-cytosol/spec.md) — transcription and translation
- [pH-Sensing Module](../detector-ph/spec.md) — trigger duplex and toehold-gated template
- `pT7-toehold9-PLA1` — the gated construct. The toehold switch and PLA1 are one molecule, so PLA1 is not a separate addition. PLA1 itself is described on the Lysis: PLA1 page, `../effector-pla1/spec.md`

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
