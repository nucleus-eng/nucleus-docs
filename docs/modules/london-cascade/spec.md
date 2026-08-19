---
title: "London Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The London Cascade combines the [AHL Sensing Cell](../ahl-sensing-cell/spec.md) with the [PLA1 Lysis Module](../effector-pla1/spec.md) and the [LacZ Reporter](../reporter-lacz/spec.md) to turn AHL exposure into a visible color change. AHL activates the LuxR/pLux promoter inside the sensing cell, but here the promoter drives a LuxR/pLux-controlled PLA1 construct (`P70lux-PLA1-term`) instead of the GFP payload documented on the AHL Sensing Cell page. Expressed PLA1 ruptures its own liposome and a neighboring CPRG-loaded liposome, releasing CPRG into an exterior β-galactosidase (LacZ) solution, which converts the yellow CPRG substrate into a magenta chlorophenol red product. This is the composed synthetic-cell readout used in the London quorum-sensing demo. On its own, the AHL Sensing Cell reports AHL exposure only through GFP; the London Cascade is the variant that swaps in PLA1 as cargo so that AHL exposure instead produces a colorimetric handoff through the PLA1/LacZ chemistry shared with the Chicago cascades (see the [PLA1 Lysis Module](../effector-pla1/spec.md) spec, "London AHL cascade").

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{note}
**Source of this page.** Composition and behavior data below come from `Demo Status - London.docx` (London Module 6, "PLA1-based colour-change module," contributors Jonah McDonald and Charlie Newell) and the 2026-08-14 DevCells status meeting (transcript and an accompanying 40-page slide deck, pp. 15–17). The backing devnotes for this cascade — `devnotes/london-quorum-sensing-polymersome/main.md` and `devnotes/london-lacz-xyle-module/main.md` — are both confirmed still template stubs, so neither is cited here as a completed primary source. See the [AHL Sensing Cell](../ahl-sensing-cell/spec.md) spec for the underlying LuxR/pLux sensing data (encapsulation, plasmid dosing, temperature dependence) rather than duplicating it here — this page covers only what changes when PLA1 replaces GFP as the sensed cascade's output.
:::

## Schematic

No published schematic exists for this mechanism; the diagram below is a simplified summary, not a reproduction of a lab figure.

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    AHL["AHL (3-oxo-C6-HSL)<br/>5 µM, exterior"] --> SENSE["AHL Sensing Cell:<br/>LuxR/pLux binds AHL,<br/>drives P70lux-PLA1-term<br/>(15 ng/µL DNA)"]
    SENSE -->|"PLA1 expressed"| LYSIS["PLA1 Lysis Module:<br/>self-lysis of the<br/>sensing synthetic cell"]
    LYSIS -->|"ruptures neighboring<br/>CPRG-loaded synthetic cell"| RELEASE["CPRG released into<br/>exterior solution"]
    RELEASE -->|"β-galactosidase"| READOUT["LacZ Reporter:<br/>yellow CPRG →<br/>magenta chlorophenol red"]

    classDef confirmed fill:#def5ee,stroke:#009E73,color:#00402e;
    classDef leaky fill:#fff3cd,stroke:#b8860b,color:#5c4400;

    class AHL,SENSE,LYSIS,RELEASE confirmed;
    class READOUT leaky;

    click SENSE "/docs/modules/ahl-sensing-cell/spec"
    click LYSIS "/docs/modules/effector-pla1/spec"
    click READOUT "/docs/modules/reporter-lacz/spec"
```

The readout step is shaded to flag it as the currently only slightly discernible, leaky part of the chain (see [Expected Behavior](#expected-behavior) below); the status meeting deck describes the underlying rupture step itself as "temperamental... sometimes SynCells do not rupture" (deck p. 17).

## Reference Composition

The table below aggregates the working concentrations of the three constituent Modules in the combined cascade, flattened one level deep, for the S30 lysate condition reported in `Demo Status - London.docx` (Module 6): 15 ng/µL `P70lux-PLA1-term` plasmid DNA plus 5 µM purified AHSL (AHL). It does not re-expand any constituent's own internal composition — see each linked spec for that detail.

:::{table} Reference composition — London Cascade, S30 lysate condition (15 ng/µL DNA + 5 µM AHL)
:label: comp-london-cascade

| Module | Component | Working concentration |
| --- | --- | --- |
| [AHL Sensing Cell](../ahl-sensing-cell/spec.md) | `P70lux-PLA1-term` plasmid DNA (in place of `pLux-GFP`) | 15 ng/µL |
| [AHL Sensing Cell](../ahl-sensing-cell/spec.md) | AHL (3-oxo-C6-HSL) inducer | 5 µM, exterior |
| [PLA1 Lysis Module](../effector-pla1/spec.md) | PLA1 lysis trigger | Co-encapsulated with the sensing construct in the same synthetic cell; no separate working concentration documented beyond the DNA dose above |
| [LacZ Reporter](../reporter-lacz/spec.md) | CPRG substrate | Encapsulated in a second, dedicated liposome population; working concentration not reported for this cascade configuration |
| [LacZ Reporter](../reporter-lacz/spec.md) | β-galactosidase (LacZ), exterior solution | Working concentration not reported for this cascade configuration — see the [LacZ Reporter](../reporter-lacz/spec.md) spec for the enzyme's general characterization |
:::

:::{attention} Construct not yet in `nucleus-eng/DNA`
`P70lux-PLA1-term` is not yet confirmed in [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA) — see the [PLA1 Lysis Module](../effector-pla1/spec.md) Designs tab for the same gap. Do not add a Designs table entry here until the construct is confirmed and its length verified against the source file.
:::

Source material does not report a full outer-solution table (glucose/salt osmolarity components) specific to this cascade, or a separate reaction-composition table confirming that the S30 lysate premix, extract, amino acid mix, sucrose, and RNase inhibitor concentrations carry over unchanged from the AHL Sensing Cell's own inner-solution table for the PLA1 payload — see the [AHL Sensing Cell](../ahl-sensing-cell/spec.md) spec for the closest documented analog on both counts.

## Expected Behavior

With S30 lysate-encapsulated liposomes and quorum sensing active, a color change is observed both in the presence and absence of AHSL — at 15 ng/µL plasmid DNA and 5 µM purified AHSL, the difference in color between the +AHSL and −AHSL conditions is described as only slightly discernible after 16 h at 37 °C. The team is still testing other DNA/AHSL concentrations and hydrogel concentrations to widen this gap and reduce time-to-signal.

The status meeting deck separately reports this same AHL-gated lysate colorimetric configuration (both solution and gel formats, deck pp. 16–17) as having been repeated across two different labs in gel format, but describes it as "temperamental... sometimes SynCells do not rupture" (deck p. 17). The deck also flags "leaky expression [as] a bigger issue than first thought" for the London node generally (deck p. 13, discussing the earlier GFP-based AHL sensor module) — a separate module from the PLA1/LacZ cascade on this page, but the same leakiness recurs here: the deck's own p. 17 notes "also have some leaky expression (but still discernible)" for this cascade specifically.

:::{attention} Net characterization
The AHL-gated PLA1/LacZ colorimetric readout is not yet a robust, confirmed result. The signal is real — a color difference between +AHSL and −AHSL conditions has been observed — but it is explicitly described as only slightly discernible, and the underlying two-liposome lysis-and-release mechanism is reported as unreliable ("temperamental," inconsistent rupture) even where repeated across labs. Treat this Module as an in-progress optimization target, not as a validated colorimetric cascade.
:::

:::{note} Related, non-gated result — do not conflate
A separate constitutive (non-AHL-gated) configuration of the same PLA1/CPRG two-liposome chemistry, run in nucleus cytosol without quorum sensing, shows a clearer result: a color change observable from ~3 h at 37 °C, easily discernible by 16 h, reproduced across multiple days (`Demo Status - London.docx`, Module 6). This confirms the PLA1/LacZ/CPRG chemistry itself works, but it is not the AHL-sensing cascade described on this page — it has no LuxR/pLux gating and is not a demonstration of AHL detection.
:::

## Process

The London Cascade requires encapsulating two separate liposome populations (the PLA1-payload sensing population and the CPRG-loaded reporter population) and combining them in a shared exterior LacZ solution, following the same synthetic cell mineral-oil phase-transfer route documented on the [London Chassis](../london-chassis/spec.md) and [AHL Sensing Cell](../ahl-sensing-cell/spec.md) specs.

:::{attention} Process gap
The constituent steps are documented: [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md), [SUV Encapsulation](../../processes/encapsulate-suv/main.md), and [ULGA Hydrogel Embedding](../../processes/embed-ulga-hydrogel/main.md). What is **not** documented is the co-incubation step that combines the two liposome populations at the ratio this cascade needs — that remains a gap.
:::

:::{attention} Exterior LacZ leakage — mitigation not yet written up
Exterior LacZ (or LacZ/CPRG product) leakage after PLA1-triggered lysis was raised as an open issue in the status meeting, specific to this kind of two-liposome cascade. A proteinase K treatment (50 °C for 10 min, then 40 °C for 1 h, then spin down) was proposed as a candidate mitigation but is not yet a written-up process — see the [PLA1 Lysis Module](../effector-pla1/spec.md) "Known Future Work" section, which owns this gap rather than duplicating it here.
:::

# Constituent Modules

- [AHL Sensing Cell](../ahl-sensing-cell/spec.md)
- [PLA1 Lysis Module](../effector-pla1/spec.md)
- [LacZ Reporter](../reporter-lacz/spec.md)

# Credits

- Jonah McDonald (PLA1-based colour-change module)
- Charlie Newell (PLA1-based colour-change module)
