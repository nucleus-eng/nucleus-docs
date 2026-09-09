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

:::{attention} Supply and concentration in the gel format
@Editor(chicago): the commercial enzyme is β-galactosidase from *E. coli*; London sources it as Sigma-Aldrich G5635. Confirm whether Chicago uses the same product, and give the working concentration for the gel-dispersed format.
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
