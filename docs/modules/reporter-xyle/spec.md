---
title: "Reporter: XylE / C23DO"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The XylE / C23DO Reporter Module produces a visible color change by expressing catechol 2,3-dioxygenase (C23DO, the *xylE* gene product), which oxidises colorless catechol into 2-hydroxymuconate semialdehyde, a yellow ring-fission product readable by absorbance near (375–385) nm ([Kunz and Chapman, 1981](https://doi.org/10.1128/jb.146.1.179-191.1981)). It is a second colorimetric reporter enzyme alongside LacZ/CPRG, giving the platform an orthogonal readout for multiplexed sensing.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Gap / proposed module — do not overstate maturity
This module's chemistry is confirmed only at bulk-cytosol scale, with one construct, in one lab context (see Expected Performance below). No GUV/vesicle encapsulation or hydrogel-embedded data exist for this reporter, and it is not part of any confirmed cascade result. In the aTc Cascade, the XylE leg is explicitly still dashed/gap — the confirmed 2026-08-14 aTc encapsulation data used the LacZ leg, not XylE. Do not read this module as being at the same readiness level as its sibling [LacZ Reporter](../reporter-lacz/spec.md), which does have confirmed GUV/hydrogel-level results.
:::

Two source lines both reference "XylE," at different levels of readiness, and they should not be conflated:

1. **Chicago node** — a TetR/aTc-inducible construct, `pT7-TetO-catecholase` (`pMN067`), expressing C23DO downstream of the [tetR-aTc Detector](../detector-tetr_atc/spec.md). Validated in bulk Nucleus Cytosol (see Expected Performance). Source: [`devnotes/chicago-teto-catecholase`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-teto-catecholase).
2. **London node** — XylE proposed as one of two candidate reporter enzymes (alongside LacZ) for the London color-change module, in two linear-DNA formats (`T7pro-XylE-T7term` and a higher-expression `T7pro-UTR1-G10_leader_peptide-XylE-T7term` variant). As of that devnote, the London-specific XylE DNA was still "to be designed" — not yet synthesized. Source: [`devnotes/london-lacz-xyle-module`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/london-lacz-xyle-module).

Because *xylE* encodes C23DO, these are the same enzyme referenced by two different programs, not two distinct reporters. Whether the Chicago `pMN067` construct and the still-undesigned London construct will end up as the same DNA design is **not established** in the source material — treat this as open rather than assuming a shared construct.

A 2026-08-14 status-meeting slide deck ("DevCell Project Meeting, 14 Aug 2026") lists "XylE / C23DO Reporter" as a labeled box in a system-architecture module-dependency diagram (module list spanning Chicago/London/Shared/Proposed categories), confirming the module is tracked at the program level, but the deck gives no additional experimental data for it beyond that label.

:::::{tab-set}

::::{tab-item} Schematic
```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    A["Catechol<br/>(colorless)"] -->|"C23DO<br/>(xylE gene product)"| B["2-Hydroxymuconate<br/>semialdehyde<br/>(yellow)"]
    style A fill:#ffffff,stroke:#555555
    style B fill:#f7e34d,stroke:#555555
```

No published schematic exists for this mechanism; the diagram below is a simplified summary, not a reproduction of a lab figure. The devnote's kinetics figure (`pT7_TetO_catecholase.png`) and the meeting-slide well-plate photo both show absorbance/color-change *data*, not the reaction mechanism, so neither is a substitute for a schematic. A real schematic (e.g. depicting the ring-fission mechanism or the reporter construct) is still needed from the dev team.
::::

::::{tab-item} Designs

:::{attention} Not yet in `nucleus-eng/DNA`
`pT7-TetO-catecholase` (`pMN067`) is not present in the [Nucleus DNA repository](https://github.com/nucleus-eng/DNA). A sequence file exists in the source devnote (`chicago-teto-catecholase/experiments/sequences/pMN067_T7_TetO_C23DO_entireconstruct.dna`), but per repository convention this page does not link to or copy it directly — flag for follow-up so the construct can be submitted to `nucleus-eng/DNA` before this page is used at the bench. The London-specific `T7pro-XylE-T7term` and `T7pro-UTR1-G10_leader_peptide-XylE-T7term` constructs are not yet designed at all (per the London devnote), so no equivalent Designs-table entry exists for them.
:::

| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-TetO-catecholase` (`pMN067`) | not verified | not yet in `nucleus-eng/DNA` |

::::

:::::

## Cytosols

### Reference Composition

The Chicago-node construct was tested downstream of the tetR-aTc Detector at three conditions — unregulated (no TetR), regulated (TetR, no aTc), and derepressed (TetR + aTc) — in a 10 µL Nucleus Cytosol reaction with `pT7-TetO-catecholase` (`pMN067`) at 20 nM final concentration and 1 mM catechol.

:::{table} Reaction composition (Chicago node)
| Component | Stock Concentration | Final concentration | Unregulated [µL] | Regulated [µL] | Derepressed [µL] |
| --- | --- | --- | --- | --- | --- |
| SMix | 3.33× | 1× | 3 | 3 | 3 |
| PMix | 15 mg/mL | 1.80 mg/mL | 1.2 | 1.2 | 1.2 |
| Ribosomes | 10 µM | 1.8 µM | 1.8 | 1.8 | 1.8 |
| tRNA | 35 mg/mL | 3.5 mg/mL | 1 | 1 | 1 |
| `pT7-TetO-catecholase` (`pMN067`) DNA template | 275.7 nM | 20 nM | 0.73 | 0.73 | 0.73 |
| Catechol | 100 mM | 1 mM | 0.2 | 0.2 | 0.2 |
| TetR | 1305.6 nM | 75 nM | 0 | 0.57 | 0.57 |
| Anhydrotetracycline (aTc) | 100 µM | 10 µM | 0 | 0 | 1 |
| RNase Inhibitor | 40000 U/mL | 2000 U/mL | 0.5 | 0.5 | 0.5 |
| Water | | | 1.57 | 1 | 0 |
:::

:::{attention} TetR concentration — flagged inconsistency, do not resolve silently
A separate, later status update (2026-08-14 meeting slide deck, "DevCell Project Meeting") re-runs the same TetR/aTc/C23DO-catechol chemistry as a bulk-reaction replication ahead of a September/October DevCell Studio, and reports clean induced/repressed/unregulated separation — but at TetR concentrations of 500 nM and 1000 nM, a different scale than the 75 nM used in the reference reaction above. The deck slide does not state whether this is the same DNA construct (`pMN067`) or a newly prepared one. Treat these as two separate data points at different TetR scales, not as replicated confirmation of a single condition, until reconciled.
:::

### Expected Performance

The construct was validated in standard Nucleus Cytosol conditions with 20 nM sensor DNA, 1 mM catechol, in 10 µL reactions incubated at 37 °C in a platereader, monitored by absorbance at 385 nm. Color conversion (colorless to yellow) occurred faster to a visually detectable level only in the derepressed condition (TetR + 10 µM aTc); the regulated (TetR, no aTc) condition remained visually below a prior-calibrated visual threshold of absorbance 1.0. A homemade TetR stock stored in glycerol was used for this preliminary result; glycerol can cause reaction poisoning in Nucleus Cytosol and is not an optimal long-term storage buffer for TetR — a caveat noted directly in the source devnote.

:::{hint} Figure not yet migrated
:class: dropdown
The source devnote includes a kinetics figure (`pT7_TetO_catecholase.png`, absorbance at 385 nm over time for Unregulated/Regulated/Derepressed conditions). It has not been copied into this page — see [`devnotes/chicago-teto-catecholase`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-teto-catecholase) for the original.
:::

This preliminary result shows the TetR/aTc sensor with a C23DO reporter is compatible with Nucleus Cytosol at bulk scale. It has **not** been tested encapsulated (GUV) or in a hydrogel — the source devnote states that "encapsulation of the sensor will inform whether 10 µM aTc is sufficient for derepression," i.e. that step had not yet been done as of authoring.

## Cells

:::{note}
No encapsulated (GUV/vesicle) or hydrogel data exist for this module. Unlike the [LacZ Reporter](../reporter-lacz/spec.md), which the 2026-08-14 aTc Cascade result used at the GUV/hydrogel-embedded level, the XylE/C23DO leg has not progressed past bulk cytosol. The aTc Cascade page keeps this leg dashed/proposed for that reason.
:::

# Requirements

- Requires anhydrotetracycline (aTc) as the derepressing input when paired with the tetR-aTc Detector, and catechol as substrate.
- Per the 2026-08-14 status-meeting decision to represent module incompatibility as a stated Requirement (rather than a general cross-Nucleus compatibility matrix, which is explicitly out of scope for this tranche): if this reporter is ever co-located with the Theophylline Sensing Module in the same reaction or compartment, note that theophylline has been reported (hedged: "somewhat inhibit," not a flatly confirmed mechanism) to interfere with the related LacZ/CPRG color reaction — whether the same interference applies to the catechol/C23DO chemistry used here has not been tested and should not be assumed either way.

# Implementations

No confirmed Implementation uses this Module yet. It is named (dashed/gap) as the XylE leg of the proposed aTc Cascade in the current module-integration diagram; that leg is not used in the confirmed 2026-08-14 aTc Cascade data, which used the LacZ leg instead.

# Credits

- Chicago node bulk-cytosol result: see [`devnotes/chicago-teto-catecholase`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-teto-catecholase) for contributor attribution.
- London node module design: see [`devnotes/london-lacz-xyle-module`](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/london-lacz-xyle-module) for contributor attribution.
