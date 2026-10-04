---
title: "pH Cascade, one-liposome design"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`ph-cascade`](../ph-cascade/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

A proposed redesign of the [pH Cascade](../ph-cascade/spec.md) with **one liposome population instead of two**. The enzyme moves inside the sensing cell, and the substrate stops being encapsulated at all: CPRG arrives in solution after the gel is set.

:::{attention} 🚧 Proposed, not run
Nothing on this page has been built. It is written so that this design and the two-liposome one can be compared as compositions rather than as intentions.
:::

**It is the aTc arrangement applied to the pH detector.** [SensorCytosol[aTc ⟶ PLA1]](../atc-sensor-cytosol/spec.md) already mixes [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) into its cytosol, and [aTc Cascade](../atc-cascade/spec.md) doses its substrate in from a trigger solution. Under this design the two Chicago demonstrations would differ only in what they sense.

**Why it is worth drawing.** The two-liposome design needs a second population whose preparation is unsettled — the extruded and freeze-thaw routes are both being run — and whose leakiness is the branch's open risk. One population removes that whole branch.

# Reference Composition

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    BASE_CYTOSOL["Base Cytosol"]
    PH_RESPONSIVE_SSDNA["pH-responsive strand"]
    TRIGGER_SSDNA["Trigger strand"]
    EFFECTOR_PLA1["Lysis: PLA1"]
    REPORTER_LACZ_ENZYME["LacZ Enzyme"]
    MEMBRANE_CHICAGO["Membrane: POPC/Chol (9:1)"]
    SUBSTRATE_CPRG["Substrate: CPRG"]
    LGA_POWDER["Gel: LGA"]
    OUTER_SOLUTION_TRIS_HEPES["Outer Solution: Tris-HEPES"]
    ANALYTE_PH["Analyte: pH"]

    P1_ANNEAL_TRIGGER_DUPLEX_0(["Anneal pH-Responsive Trigger Duplex (mixing)"])
    PH_TRIGGER_DUPLEX["pH-Responsive Trigger Duplex"]
    P2_ASSEMBLE_CYTOSOL_0(["Assemble Cytosol (mixing)"])
    PH_SENSOR_CYTOSOL_WITH_ENZYME["SensorCytosol[pH ⟶ PLA1], with LacZ"]
    P3_ENCAPSULATE_0(["Encapsulation: Phase Transfer (packing)"])
    PH_SENSING_CELL_WITH_ENZYME["SensorCell[pH ⟶ PLA1], with LacZ"]
    P4_EMBED_AGAROSE_0(["Embedding: Thermal Setting (packing)"])
    PH_GEL_ONE_LIPOSOME["pH Gel, one-liposome"]
    P5_ASSEMBLE_TRIGGER_SOLUTION_0(["Trigger Solution (mixing) — no page"])
    PH_TRIGGER_SOLUTION["Trigger Solution"]
    P6_DOSE_TRIGGER_SOLUTION_0(["Addition of Solution to gel (packing) — no page"])
    PH_CASCADE_ONE_LIPOSOME["pH Cascade, one-liposome design"]

    PH_RESPONSIVE_SSDNA --> P1_ANNEAL_TRIGGER_DUPLEX_0
    TRIGGER_SSDNA --> P1_ANNEAL_TRIGGER_DUPLEX_0
    P1_ANNEAL_TRIGGER_DUPLEX_0 --> PH_TRIGGER_DUPLEX

    BASE_CYTOSOL --> P2_ASSEMBLE_CYTOSOL_0
    PH_TRIGGER_DUPLEX --> P2_ASSEMBLE_CYTOSOL_0
    EFFECTOR_PLA1 --> P2_ASSEMBLE_CYTOSOL_0
    REPORTER_LACZ_ENZYME --> P2_ASSEMBLE_CYTOSOL_0
    P2_ASSEMBLE_CYTOSOL_0 --> PH_SENSOR_CYTOSOL_WITH_ENZYME

    PH_SENSOR_CYTOSOL_WITH_ENZYME --> P3_ENCAPSULATE_0
    MEMBRANE_CHICAGO --> P3_ENCAPSULATE_0
    P3_ENCAPSULATE_0 --> PH_SENSING_CELL_WITH_ENZYME

    LGA_POWDER --> P4_EMBED_AGAROSE_0
    OUTER_SOLUTION_TRIS_HEPES --> P4_EMBED_AGAROSE_0
    PH_SENSING_CELL_WITH_ENZYME --> P4_EMBED_AGAROSE_0
    P4_EMBED_AGAROSE_0 --> PH_GEL_ONE_LIPOSOME

    SUBSTRATE_CPRG --> P5_ASSEMBLE_TRIGGER_SOLUTION_0
    ANALYTE_PH --> P5_ASSEMBLE_TRIGGER_SOLUTION_0
    P5_ASSEMBLE_TRIGGER_SOLUTION_0 --> PH_TRIGGER_SOLUTION

    PH_GEL_ONE_LIPOSOME --> P6_DOSE_TRIGGER_SOLUTION_0
    PH_TRIGGER_SOLUTION --> P6_DOSE_TRIGGER_SOLUTION_0
    P6_DOSE_TRIGGER_SOLUTION_0 --> PH_CASCADE_ONE_LIPOSOME


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class BASE_CYTOSOL,PH_RESPONSIVE_SSDNA,TRIGGER_SSDNA,EFFECTOR_PLA1,REPORTER_LACZ_ENZYME,MEMBRANE_CHICAGO,SUBSTRATE_CPRG,LGA_POWDER,OUTER_SOLUTION_TRIS_HEPES,ANALYTE_PH leaf;
    class PH_TRIGGER_DUPLEX,PH_SENSOR_CYTOSOL_WITH_ENZYME,PH_SENSING_CELL_WITH_ENZYME,PH_GEL_ONE_LIPOSOME,PH_TRIGGER_SOLUTION,PH_CASCADE_ONE_LIPOSOME composed;
    class P1_ANNEAL_TRIGGER_DUPLEX_0,P2_ASSEMBLE_CYTOSOL_0,P3_ENCAPSULATE_0,P4_EMBED_AGAROSE_0,P5_ASSEMBLE_TRIGGER_SOLUTION_0,P6_DOSE_TRIGGER_SOLUTION_0 process;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click EFFECTOR_PLA1 "/docs/modules/effector-pla1/spec"
    click REPORTER_LACZ_ENZYME "/docs/modules/reporter-lacz-enzyme/spec"
    click MEMBRANE_CHICAGO "/docs/modules/membrane-popc-chol-9-1/spec"
    click SUBSTRATE_CPRG "/docs/modules/substrate-cprg/spec"
    click LGA_POWDER "/docs/modules/gel-lga/spec"
    click OUTER_SOLUTION_TRIS_HEPES "/docs/modules/outer-solution-tris-hepes/spec"
    click ANALYTE_PH "/docs/modules/analyte-ph/spec"
    click P1_ANNEAL_TRIGGER_DUPLEX_0 "/docs/processes/anneal-ph-trigger-duplex/main"
    click P2_ASSEMBLE_CYTOSOL_0 "/docs/processes/assemble-cytosol/assemble-cytosol-main"
    click P3_ENCAPSULATE_0 "/docs/processes/assemble-base-cell/main"
    click P4_EMBED_AGAROSE_0 "/docs/processes/embed-thermal-setting/main"
    click PH_CASCADE_ONE_LIPOSOME "/docs/modules/ph-cascade-one-liposome/spec"
```

::::
<!-- /gen:composition-diagram -->

# Expected Behavior

Acidic pH opens the toehold switch, PLA1 is expressed, and the cell lyses. Lysis releases LacZ into the gel, where it meets the CPRG already dosed in, and the yellow-to-purple change follows.

**The off state is the membrane.** While the cell is intact, enzyme and substrate are in different compartments and nothing happens. That is the [Color Change](../color-change/spec.md) invariant, satisfied with the enzyme inside rather than outside.

# Requirements

Requires the enzyme to be the encapsulated half and the substrate to be outside it. This design does not merely permit that arrangement; it depends on it, because the membrane is the only thing holding the readout off.

Requires LacZ to tolerate the sensing conditions, which is the first thing to measure — see the open items below.

# Constituent Modules

- **SensorCell[pH ⟶ PLA1], with LacZ** — the one liposome population, and it has **no page of its own**. It is not the two-liposome cascade's sensing cell: this one carries the enzyme inside, which makes it a different Module, and only one of the two is built. Named here rather than linked for that reason
- [Base Cytosol](../base-cytosol/spec.md) — the expression system inside it
- [Lysis: PLA1](../effector-pla1/spec.md) — the effector the toehold switch drives
- [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) — **inside the cell**, which is the design change
- [Membrane: POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md) — the one bilayer in the system
- [Substrate: CPRG](../substrate-cprg/spec.md) — **not encapsulated.** It arrives in the trigger solution after the gel is set
- [Analyte: pH](../analyte-ph/spec.md) — carried in with the substrate
- [Gel: LGA](../gel-lga/spec.md) — the matrix
- [Outer Solution: Tris-HEPES](../outer-solution-tris-hepes/spec.md) — the phase the agarose dissolves into

The pH-responsive and trigger strands are named by the source as the two halves annealed 3:1. The **Detector: pH-Sensing** page documents them; it is not linked here because this source names the strands rather than the Module.

# Open

:::{attention} Three things decide whether this works
**Does LacZ survive the sensing pH?** The two-liposome design keeps the enzyme out of the cell precisely because β-galactosidase works poorly at the pH the sensor needs. This design puts it in. The cytosol is buffered and the analyte acidifies the gel, so the enzyme may never see the low pH — but nothing has measured that, and if it does, the design fails at its first step.

**Can the trigger solution carry both?** The aTc cascade doses substrate and analyte together because aTc is membrane-permeable and chemically quiet. The pH analyte is an acid, and whether CPRG tolerates being carried in it is recorded nowhere.

**Does this replace the two-liposome design?** Both are specified now. That one has run; this has not. Nothing here claims to supersede it.
:::

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
