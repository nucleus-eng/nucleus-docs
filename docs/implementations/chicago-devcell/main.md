---
title: "Chicago DevCell: Patterned Multiplexed Biosensor"
subtitle: Implementation
status: draft
site:
    hide-toc: true
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

The Chicago DevCell is a hydrogel-embedded, spatially patterned biosensor that turns the detection of two independent analytes into a visible color change. Synthetic cells carrying a sensing circuit express phospholipase A1 (PLA1) on detection; PLA1 lyses the cell and its neighboring [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md), releasing CPRG to LacZ in the surrounding matrix, which converts it from yellow to purple.

The device is a cascade Module placed in a physical operating context: a specific hydrogel chemistry, a specific spatial pattern, and a specific readout format.

## What the demo is

**Two sensors.** The device carries the aTc and pH sensors. The theophylline sensor is not part of the device. See [Theophylline Sensing Module](../../modules/detector-theophylline/spec.md).

**Hydrogel chemistry.** The confirmed unpatterned result used ~1% alginate. Spatial patterning uses PEG-norbornene (PEG4Nb), which supports synthetic cell stability but bleaches pre-loaded CPRG under UV — see the workaround on [LacZ Reporter Module](../../modules/reporter-lacz/spec.md#reporter-lacz-requirements).

# Modules

| Role | Module | State |
| --- | --- | --- |
| Chassis | [Chicago Chassis](../../modules/chicago-chassis/spec.md) | ★ |
| Membrane | [Membrane: POPC/Chol (9:1)](../../modules/membrane-popc-chol-chicago/spec.md) | ★ |
| Sensing (aTc) | [SensorCell[aTc ⟶ PLA1]](../../modules/atc-sensing-cell/spec.md) → [aTc Cascade](../../modules/atc-cascade/spec.md) | detectable response, not dose-graded |
| Sensing (pH) | [SensorCell[pH ⟶ PLA1]](../../modules/ph-sensing-cell/spec.md) → [pH Cascade](../../modules/ph-cascade/spec.md) | integration paths confirmed separately; chain not run end to end |
| Lysis | [PLA1 Lysis Module](../../modules/effector-pla1/spec.md) | ★ |
| Substrate | [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md) | ★ |
| Readout | [LacZ Reporter Module](../../modules/reporter-lacz/spec.md) | ★ |
| Readout (alternate) | [XylE / C23DO Reporter Module](../../modules/reporter-xyle/spec.md) | proposed, not used |

## Choosing the colorimetric readout

Two colorimetric readouts are available. **LacZ is the one this demo uses.** It has been demonstrated together with the aTc sensing and PLA1 lysis constructs in a single synthetic cell, and produced the aTc-response data.

[XylE / C23DO](../../modules/reporter-xyle/spec.md) is a second, orthogonal colorimetric enzyme (catechol 2,3-dioxygenase) and the alternative readout. It is validated only in bulk cytosol, using a different TetR/aTc-inducible construct (`pT7-TetO-catecholase` / `pMN067`), with no synthetic cell encapsulation or hydrogel data, and it has never been run with the PLA1 lysis trigger. See [XylE / C23DO Reporter Module](../../modules/reporter-xyle/spec.md#reporter-xyle-expected-behavior) for that result.

# Processes

| Step | Process |
| --- | --- |
| Form synthetic cells | [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) |
| Form substrate liposomes | [Encapsulation: Extrusion](../../processes/encapsulate-suv/main.md) |
| Embed | [Embedding: Ionic Crosslinking](../../processes/embed-ionic-crosslinking/main.md) |
| Pattern | [Embedding: Photodevelopment](../../processes/embed-photodevelopment/main.md) |
| Read out | [Colorimetric Readout](../../processes/colorimetric-readout/main.md) |
| Reduce background | [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) — proposed, never run |

# Performance

No integrated performance data exists. What is confirmed sits at the level of individual integration paths, on the Module pages above.

:::{attention} Integration not yet demonstrated
Every arrow between the Modules above is an integration step that is not yet verified end to end. Three are open:

1. **Multiplexing.** The aTc and pH integration paths have never been run in one reaction. The only documented multiplex attempt — aTc with theophylline — is blocked by a shared-readout constraint.
2. **Gel integration.** The aTc integration path is confirmed in synthetic cells, but hydrogel integration of that cascade has not been completed.
3. **Patterned readout.** PEGDA patterning has been shown to hold structure and confine color, but a macroscopically visible readout from a patterned gel has not been demonstrated — component volumes are too small.
:::

# Credits

Developed by the Chicago Node — Kamat Lab and Liu Lab.

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
