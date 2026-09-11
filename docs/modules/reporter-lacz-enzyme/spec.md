---
title: "Reporter: LacZ Enzyme"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The LacZ Enzyme is β-galactosidase from *E. coli*, the hydrolase half of the [LacZ Reporter](../reporter-lacz/spec.md) colorimetric pair. It cleaves [CPRG](../substrate-cprg/spec.md) from yellow chlorophenol red-β-D-galactopyranoside to magenta chlorophenol red.

**It is a separate Module from its substrate because the two are routinely in different compartments.** In the London Cascade the enzyme is dispersed free in the gel while CPRG is held inside a liposome population; in the aTc path the enzyme is encapsulated with the sensing reaction and CPRG stays outside. Which compartment each occupies is set by the process that places it, not by the reporter chemistry — so a page describing the pair cannot state a single location for either.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} LacZ Enzyme working concentrations by context.
| Context | Working concentration | Notes |
| --- | --- | --- |
| Encapsulated with the sensing reaction | 20 U/mL | [aTc Sensor Cytosol](../atc-sensor-cytosol/spec.md). Co-encapsulating the enzyme with CPRG would make the readout constitutive |
| Dispersed in the gel | Not documented | London Cascade, ULGA embedding |
:::

:::{attention} Two numbers, and neither is settled
**The gel-dispersed working concentration is missing outright.** @Editor(london): the London Cascade disperses this enzyme through the ULGA gel and no concentration is recorded for it anywhere. Without it that half of the cascade cannot be reproduced.

**The encapsulated figure of 20 U/mL is used everywhere and sourced nowhere.** @Editor(chicago): it appears on ten pages across both demos, and no titration, assay or reference is recorded behind it. We are not asking what concentration to use — we are asking what it was measured against, and whether the value carries across from the aTc format to the others.

@Editor(chicago): separately, the commercial enzyme is β-galactosidase from *E. coli* and London sources it as Sigma-Aldrich G5635. Confirm whether Chicago uses the same product.
:::

# Requirements

Requires [CPRG](../substrate-cprg/spec.md) to produce a signal — the enzyme alone has no readout.

**Requires that enzyme and substrate be separated until the moment of readout.** Any route that puts both in one compartment before the trigger gives color with no analyte present. That separation is the reporter's whole mechanism, and it is a property of the composition rather than of either Module.

Proteinase K does not distinguish one LacZ from another, so [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) cannot be applied to a format that disperses the enzyme through the matrix on purpose.

# Processes

- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the CPRG conversion this enzyme performs, read at 575 nm and by eye.
- [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) — digests enzyme that escaped the sensing cells, for encapsulated formats only.

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
