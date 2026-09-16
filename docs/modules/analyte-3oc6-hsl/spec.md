---
title: "Analyte: 3OC6-HSL"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

3-oxohexanoyl-L-homoserine lactone (3OC6-HSL, commonly AHL) is the *E. coli* quorum-sensing molecule the [AHL Detector](../detector-3oc6-hsl/spec.md) responds to. LuxR binds it and activates the `pLux` promoter, driving whatever effector gene sits downstream — [deGFP](../reporter-degfp/spec.md) in the [AHL Sensing Cell](../ahl-sensing-cell/spec.md), PLA1 in the [London Cascade](../london-cascade/spec.md).

**This is an Analyte, so it is not a constituent of anything.** [London Cascade](../london-cascade/spec.md) states the position for this molecule directly: *"AHL is the analyte rather than a component of the cascade, so it is listed here for completeness but is not part of the composition."* This page does not change that.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} Working concentrations.
| Band | Value | Source |
| --- | --- | --- |
| Induction | not documented | — |
| Transport across a bilayer | not documented | — |
:::

:::{attention} No dose figures are recorded anywhere in the corpus
Neither [AHL Detector](../detector-3oc6-hsl/spec.md) nor [AHL Sensing Cell](../ahl-sensing-cell/spec.md) states an induction concentration or a working range. @Editor(london): supply the AHL concentration used for induction, and say whether the cascade and the sensing cell use the same one.
:::

# Requirements

Requires an [AHL Detector](../detector-3oc6-hsl/spec.md) to be sensed at all.

**Whether it requires a transport route is not established.** Unlike [aTc](../analyte-atc/spec.md), which is membrane-permeable, nothing in the corpus says whether 3OC6-HSL crosses a POPC bilayer unaided. The [London Cascade](../london-cascade/spec.md) doses it into the outer solution and the sensing cells are encapsulated, so the question is live rather than academic. @Editor(london): confirm.

# Processes

None. An analyte is supplied to an assay rather than produced by a Nucleus process.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
