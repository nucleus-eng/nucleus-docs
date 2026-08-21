---
title: "Chicago DevCell: Patterned Multiplexed Biosensor"
subtitle: Implementation
status: draft
site:
    hide-toc: true
---

# Overview

:::{attention} 🚧 Draft — stub
This page is a placeholder for the Chicago demo device. It records what the demo is composed of and what is confirmed as of 2026-08-19; the integrated result does not exist yet and will be written up during DevStudio (23 Sep – 13 Oct 2026).
:::

The Chicago DevCell is a hydrogel-embedded, spatially patterned biosensor that turns the detection of two independent analytes into a visible color change. Synthetic cells carrying a sensing circuit express phospholipase A1 (PLA1) on detection; PLA1 lyses the cell and its neighboring [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md), releasing CPRG to LacZ in the surrounding matrix, which converts it from yellow to purple.

This is an Implementation rather than a Module because it is a cascade Module placed in a physical operating context: a specific hydrogel chemistry, a specific spatial pattern, and a specific readout format. The Modules themselves are documented on their own pages and not restated here.

## What the demo is, as of 2026-08-19

**Two sensors, not three.** Chicago is focusing on the aTc and pH sensors (14 Aug 2026 deck, slides 2 and 34). The theophylline sensor has been **removed from this demo** — it remains a DevStudio bulk-replication target, but it is not part of the device. See [Theophylline Sensing Module](../../modules/detector-theophylline/spec.md).

**Hydrogel chemistry is in transition.** The confirmed unpatterned result used ~1% alginate. Spatial patterning work has moved to PEG-norbornene (PEG4Nb), which supports synthetic cell stability but bleaches pre-loaded CPRG under UV — see the workaround on [LacZ Reporter Module](../../modules/reporter-lacz/spec.md#requirements).

# Modules

| Role | Module | State |
| --- | --- | --- |
| Chassis | [Chicago Chassis](../../modules/chicago-chassis/spec.md) | ★ |
| Membrane | [Chicago Membrane: POPC/Chol](../../modules/membrane-popc-chol-chicago/spec.md) | ★ |
| Sensing (aTc) | [aTc Sensing Cell](../../modules/atc-sensing-cell/spec.md) → [aTc Cascade](../../modules/atc-cascade/spec.md) | detectable response, not dose-graded |
| Sensing (pH) | [pH Sensing Cell](../../modules/ph-sensing-cell/spec.md) → [pH Cascade](../../modules/ph-cascade/spec.md) | integration paths confirmed separately; chain not run end to end |
| Lysis | [PLA1 Lysis Module](../../modules/effector-pla1/spec.md) | ★ |
| Substrate | [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md) | ★ |
| Readout | [LacZ Reporter Module](../../modules/reporter-lacz/spec.md) | ★ |
| Multiplex | [Chicago Cascade](../../modules/chicago-cascade/spec.md) | not built |

# Process

| Step | Process |
| --- | --- |
| Form synthetic cells | [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) |
| Form substrate liposomes | [SUV Encapsulation](../../processes/encapsulate-suv/main.md) |
| Embed | [Alginate Hydrogel Embedding](../../processes/embed-alginate-hydrogel/main.md) |
| Pattern | [Photopatterning, PEGDA](../../processes/photopattern-pegda/main.md) |
| Read out | [Colorimetric Readout](../../processes/colorimetric-readout/main.md) |
| Reduce background | [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) — proposed, never run |

# Performance

No integrated performance data exists. What is confirmed sits at the level of individual integration paths, on the Module pages above.

:::{attention} The integration itself is what DevStudio is for
Every arrow between the Modules above is an integration step that has to be verified in San Francisco. Three are known open:

1. **Multiplexing.** The aTc and pH integration paths have never been run in one reaction. The only documented multiplex attempt — aTc with theophylline — is blocked by a shared-readout constraint.
2. **Gel integration.** The aTc integration path is confirmed in synthetic cytosols and in synthetic cells, but hydrogel embedding of that cascade was still in progress as of 2026-08-14.
3. **Patterned readout.** PEGDA patterning has been shown to hold structure and confine color, but a macroscopically visible readout from a patterned gel has not been demonstrated — component volumes are reported as too small.
:::

# Credits

Developed by the Chicago Node — Kamat Lab and Liu Lab. Individual results are credited on their own Module pages.
