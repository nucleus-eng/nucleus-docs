---
title: "GUV: CPRG"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

A CPRG GUV is a giant unilamellar liposome carrying chlorophenol red-β-D-galactopyranoside (CPRG) and nothing else. It is the substrate population of the [London Cascade](../london-cascade/spec.md), and it exists so that CPRG and its enzyme never meet until something lyses the membrane.

CPRG is yellow. β-galactosidase (LacZ) cleaves it to chlorophenol red, which is magenta. Holding the substrate inside a liposome makes that conversion triggerable: while the bilayer is intact, [LacZ](../reporter-lacz-enzyme/spec.md) sits outside in the gel and reaches nothing. When a neighboring sensing cell expresses [PLA1](../effector-pla1/spec.md) and lyses, it breaches these liposomes too, and the released CPRG meets the enzyme.

This Module is not a reporter on its own. It supplies one half of a two-part colorimetric readout, and needs the [LacZ Reporter Module](../reporter-lacz/spec.md) to produce an output.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{note} This population replaced an SUV population
The London Node moved this population from small unilamellar vesicles to GUVs on 2026-09-09. Both cell populations in the cascade now come from the same phase-transfer route, which removes a whole process from the build. Compare [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md), which the Chicago pH path still uses, made by film hydration and extrusion.
:::

(guv-cprg-reference-composition)=
# Reference Composition

:::::{tab-set}

::::{tab-item} Membrane

:::{table} CPRG GUV bilayer — [London Membrane: POPC](../membrane-popc/spec.md).
:label: comp-guv-cprg-membrane

| Component | Target percentage (%) |
| --- | --- |
| POPC | 100 |
:::

[Substrate: CPRG](../substrate-cprg/spec.md) accepts either POPC or POPC:cholesterol, so the 100% POPC bilayer here is a choice rather than a constraint. It matches the [AHL Sensing Cell](../ahl-sensing-cell/spec.md), which is what lets both populations be made by one method.

::::

::::{tab-item} Inner Solution

:::{table} CPRG GUV lumen.
:label: comp-guv-cprg-lumen

| Component | Working concentration |
| --- | --- |
| CPRG | 50 mM at hydration, approx. 30 mg/mL — per [Substrate: CPRG](../substrate-cprg/spec.md) |
:::

The loading concentration does not depend on the bilayer, so it carries over unchanged from the SUV form.

::::

:::::

(guv-cprg-expected-behavior)=
# Expected Behavior

An intact CPRG GUV produces no signal. That is the whole function: the population must stay dark until a lysis trigger arrives.

On PLA1-triggered lysis of a neighboring sensing cell, released CPRG meets LacZ in the surrounding gel and gives a yellow-to-magenta change, read by absorbance and by eye.

:::{attention} Not yet characterized in this form
This population has no performance data of its own. The [London Cascade](../london-cascade/spec.md) results were obtained with the SUV form it replaces, and rupture in that cascade is temperamental — the cells do not always lyse. Treat the GUV form as unvalidated until the cascade is re-run with it.
:::

(guv-cprg-requirements)=
# Requirements

Requires an external β-galactosidase source in the surrounding matrix (e.g. [LacZ Enzyme](../reporter-lacz-enzyme/spec.md)), held in a different compartment from this one.

Requires a lysis trigger to breach the membrane (e.g. [PLA1 Lysis Module](../effector-pla1/spec.md)). With no trigger there is no readout, because an intact liposome is the resting state.

Requires that no LacZ share a compartment with the CPRG before the trigger fires. Co-encapsulating the two makes the readout constitutive.

Requires an outer solution matched to the lumen. The [London Chassis](../london-chassis/spec.md) outer solution sits at about 920 mOsm, and matching it keeps CPRG from being driven across the bilayer before the cascade fires.

:::{warning} Do not expose CPRG to UV light
CPRG photobleaches under UV, including the UV a 405 nm source emits. This rules out any photodeveloped gel for this population. ULGA sets thermally and involves no illumination, so it is compatible — see [Gel: ULGA](../gel-ulga/spec.md).
:::

# Implementations

- [London DevCell](../../implementations/london-devcell/main.md): supplies the substrate for the AHL colorimetric readout.

# Processes

- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) — forms the population. The same process and the same page as the sensing population, applied with a different inner solution.
- [Hydrogel Embedding: ULGA](../../processes/embed-ulga-hydrogel/main.md) — combines this population with the sensing population and the gel, at 1:1:2.
- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the readout itself.

# Credits

Developed by Jonah McDonald and Charlie Newell (London Node).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
