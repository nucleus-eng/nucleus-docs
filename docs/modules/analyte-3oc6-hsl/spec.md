---
title: "Analyte: 3OC6-HSL"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

3-oxohexanoyl-L-homoserine lactone (**3OC6-HSL** in this documentation; the literature usually writes **AHL** for the acyl-homoserine lactone family this belongs to) is the *E. coli* quorum-sensing molecule the [3OC6-HSL Detector](../detector-3oc6-hsl/spec.md) responds to. LuxR binds it and activates the `pLux` promoter, driving whatever effector gene sits downstream — [deGFP](../reporter-degfp/spec.md) in the [SensorCell[3OC6-HSL ⟶ PLA1]](../ahsl-sensing-cell/spec.md), PLA1 in the [LuxR-LacZ Sensor Cascade](../luxr-lacz-cascade/spec.md).

3OC6-HSL is an Analyte, so it is not a constituent of any Module. It is the analyte of the [LuxR-LacZ Sensor Cascade](../luxr-lacz-cascade/spec.md), not a component of it.

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

:::{attention} No induction concentration documented
No induction concentration or working range is stated. @Editor(london): supply the 3OC6-HSL concentration used for induction, and say whether the cascade and the sensing cell use the same one.
:::

# Requirements

Requires an [3OC6-HSL Detector](../detector-3oc6-hsl/spec.md) to be sensed at all.

:::{attention} Transport route not established
Whether 3OC6-HSL crosses a POPC bilayer unaided is not documented. [aTc](../analyte-atc/spec.md), by contrast, is membrane-permeable. The [LuxR-LacZ Sensor Cascade](../luxr-lacz-cascade/spec.md) doses 3OC6-HSL into the outer solution and the sensing cells are encapsulated, so a transport route may be required. @Editor(london): confirm whether 3OC6-HSL crosses a POPC bilayer unaided.
:::

# Implementations

- [CRAIC Demo](../../implementations/devstudio-craic-demo/main.md): its analyte — the input.

# Processes

None. An analyte is supplied to an assay rather than produced by a Nucleus process.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
