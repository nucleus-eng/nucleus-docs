---
title: "pH Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The pH Cascade combines the [pH Sensing Cell](../ph-sensing-cell/spec.md) with the [PLA1 Lysis Module](../effector-pla1/spec.md) and the [LacZ Reporter Module](../reporter-lacz/spec.md), giving a synthetic cell that turns a drop in pH into a visible colorimetric readout. In this cascade, the pH Sensing Cell's toehold switch gates expression of PLA1, which lyses its own vesicle and a neighboring CPRG-loaded vesicle; the released CPRG then reacts with LacZ to produce the yellow-to-purple color change. This page names that pH-sensor-to-readout chain as its own Module — see each constituent spec for its own reference composition, requirements, and expected performance.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Cascade composition is proposed, not a demonstrated combined result
This page documents a proposed chain of three constituent Modules, not a single validated result for the combination. The pieces have been shown to work in different, partial combinations — see "Expected Performance" below — but no experiment has run the full pH Sensing Cell → PLA1 → LacZ chain together in one format. Do not treat this page as describing a completed cascade.
:::

## Schematic

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    PH["pH Sensing Cell:\npH-responsive ssDNA : trigger ssDNA\n(4.625 µM trigger ssDNA, final)"] -->|"pH drops to ~6.5,\ntoehold switch opens"| PLA1["PLA1 Lysis Module:\ntoehold-gated PLA1 construct\n(2 nM, final)"]
    PLA1 -->|"PLA1 expressed,\nlyses own + neighboring vesicle"| LYSIS["Lysis:\nCPRG released from\nneighboring vesicle"]
    LYSIS -->|"CPRG reacts with\nexternal LacZ"| READOUT["LacZ Reporter Module:\nyellow CPRG to purple CPR"]
    READOUT -.->|"proposed: hydrogel-embedded\nChicago Chassis format"| GEL["Combined, gel-integrated\npH Cascade"]

    classDef confirmed fill:#def5ee,stroke:#009E73,color:#00402e;
    classDef proposed fill:#f5f5f5,stroke:#999999,color:#555555,stroke-dasharray: 5 5;

    class PH,PLA1,LYSIS,READOUT confirmed;
    class GEL proposed;
```

Mechanism of the confirmed, solution-phase pH Cascade leg: the pH-sensing toehold switch releases at pH ≈ 6.5 and turns on expression of a co-encapsulated PLA1 construct, which lyses its own vesicle and a neighboring CPRG-loaded vesicle; the released CPRG then reacts with external LacZ to produce the yellow-to-purple color change. This part of the chain is confirmed at the solution level (see [Reference Composition](#reference-composition) and [Expected Performance](#expected-performance) below). The final step — running this same chain inside a hydrogel-embedded Chicago Chassis GUV — is proposed, not yet demonstrated, so it is drawn dashed/gray, matching the proposed-edge convention used in the [module-integration diagram](../chicago-cascade/spec.md). No published schematic exists for this mechanism; the diagram above is a simplified summary, not a reproduction of a lab figure.

## Composition

The pH Cascade combines its constituent Modules as follows:

- **Sensing input:** [pH Sensing Cell](../ph-sensing-cell/spec.md) — the pH-responsive toehold switch encapsulated in the Chicago Chassis GUV, gating downstream expression at pH ≈ 6.5.
- **Lysis trigger:** [PLA1 Lysis Module](../effector-pla1/spec.md) — expressed once the pH switch fires; ruptures its own vesicle and a neighboring CPRG-loaded vesicle, coupling sensing to readout.
- **Colorimetric readout:** [LacZ Reporter Module](../reporter-lacz/spec.md) — reacts with the released CPRG substrate to produce the visible yellow-to-purple color change.

None of the three constituent pages documents the combined three-part chain directly. This page exists to name that chain as the Chicago diagram's `PHCAS` node.

## Reference Composition

The table below aggregates the working concentrations behind the confirmed, solution-phase two-vesicle result described in [Expected Performance](#expected-performance), one row per constituent Module, flattened one level deep. Two of the three rows come from the pH-sensing/PLA1 vesicle's own reaction table, sourced from the Chicago node's status materials ("Demo Status – Chicago," Module 2 – pH Sensor, "Key Experiment: inner solution condition") rather than from either constituent Module's own spec page — this data has not yet been transcribed into the [pH Sensing Cell](../ph-sensing-cell/spec.md) or [PLA1 Lysis Module](../effector-pla1/spec.md) pages.

:::{table} Reference composition — confirmed solution-phase pH Cascade leg (Chicago)
:label: comp-ph-cascade

| Module | Component | Working concentration |
| --- | --- | --- |
| pH Sensing Cell | pH-responsive ssDNA : trigger ssDNA (3:1, annealed) | 4.625 µM trigger ssDNA, final — co-encapsulated with the PLA1 construct below in one vesicle |
| PLA1 Lysis Module | Toehold-switch-gated PLA1 DNA template | 2 nM, final — co-encapsulated with the pH-sensing ssDNA above; this is a distinct, PLA1-fused construct, not the standalone toehold-LacZ/XylE construct listed on the [pH-Sensing Module](../detector-ph/spec.md) page's Designs tab |
| LacZ Reporter Module | CPRG substrate | Not documented at a reaction concentration for this specific two-vesicle pairing — CPRG is loaded into a separate vesicle population and reacts with external β-galactosidase after lysis, but no working concentration for either is recorded in the surveyed source material for this pairing |
:::

:::{attention} CPRG/LacZ concentration is a real documentation gap, not a stand-in number
Unlike the [aTc Cascade](../atc-cascade/spec.md#reference-composition) (0.5 mM CPRG, 20 U/mL LacZ, encapsulated) or the theophylline cascade's CPRG-loaded SUVs (50 mM CPRG loading), no CPRG or LacZ concentration is documented anywhere for this pH cascade's own solution-phase, two-vesicle pairing. Do not substitute a number from a different cascade's readout leg to fill this row — that would misrepresent an undocumented gap as a real, sourced value. Flag this for follow-up once a formal devnote for the Chicago pH cascade's two-vesicle reaction is written.
:::

## Expected Performance

No result has been generated for the full pH Sensing Cell → PLA1 → LacZ chain run together. The closest available data are the constituent-level results documented on each Module's own page, none of which is the combined cascade:

- **pH-sensing color change, solution-phase, two-vesicle system:** a visible yellow-to-purple color change at pH 6.5, using separate pH-sensing and CPRG-loaded vesicle populations in solution. See [pH Sensing Cell](../ph-sensing-cell/spec.md#expected-performance) for detail.
- **pH-sensing, bulk hydrogel, no vesicles:** embedding the pH-sensing reaction directly in 0.7% low-gelling agarose gives a real but modest color change — "slight pink," not as bright as expected (Sung-Won Hwang, Liu Lab). Full detail, including the concentration-dependent absorbance data, is documented on the [pH Sensing Cell](../ph-sensing-cell/spec.md#expected-performance) spec and is not duplicated here.
- **PLA1-driven lysis coupling to CPRG/LacZ readout:** confirmed at the solution level for the Chicago pH cascade — see [PLA1 Lysis Module](../effector-pla1/spec.md#known-implementations), "Chicago pH cascade."

:::{warning}
**Not yet demonstrated as a working multiplexed cascade.** The pH Sensing Cell's own integration into the Chicago Chassis's GUV/hydrogel format is itself still proposed, not confirmed (see [pH Sensing Cell](../ph-sensing-cell/spec.md)). This page's cascade — pH Sensing Cell driving PLA1-triggered lysis and LacZ/CPRG readout, together in one format — has not been run as a single experiment. Keep this cascade's edge into the combined, multiplexed Chicago Cascade dashed/proposed until a gel-integrated, combined result is confirmed.
:::

## Requirements

The PLA1 Lysis Module's Requirements section flags premature lysis as a known failure mode: the Chicago pH cascade uses a gramicidin A proton channel to keep the PLA1-carrying vesicle intact until the pH switch fires, and removing gramicidin A causes background color development from acid-driven leakage. See the [PLA1 Lysis Module](../effector-pla1/spec.md#requirements) spec for detail; this page does not repeat that constraint's rationale.

## Process

No process page documents assembling this three-part cascade end to end. The [pH Sensing Cell](../ph-sensing-cell/spec.md#process) spec already flags its own GUV-encapsulation/hydrogel-embedding gap; combining that cell with PLA1 and LacZ into one cascade is a further, undocumented step. Do not assume any existing process page covers this combination — flag for a follow-up process page rather than treating a citation here as equivalent.

# Constituent Modules

- [pH Sensing Cell](../ph-sensing-cell/spec.md) — pH-responsive sensing circuit in the Chicago Chassis GUV
- [PLA1 Lysis Module](../effector-pla1/spec.md) — lysis trigger coupling sensing to readout
- [LacZ Reporter Module](../reporter-lacz/spec.md) — LacZ/CPRG colorimetric readout chemistry

# Credits

- b.next
