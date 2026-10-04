---
title: "CRAIC Demo"
subtitle: Implementation
status: draft
site:
    hide-toc: true
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

The CRAIC Demo detects a bacterial quorum-sensing signal and reports it as a visible color change from inside a hydrogel. Synthetic cells built on [Base Cytosol](../../modules/base-cytosol/spec.md) express the EsaR repressor, which holds a PLA1 construct off. 3OC6-HSL relieves the repression, the cells express [Lysis: PLA1](../../modules/effector-pla1/spec.md), and PLA1 breaks the membranes around it. That releases [Substrate: CPRG](../../modules/substrate-cprg/spec.md) from a separate carrier population to meet [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) in the gel, turning it from yellow to red.

What the embedding step builds is [CRAIC](../../modules/craic-cascade/spec.md).

**It detects the same analyte as the LuxR demos and does it a different way**: EsaR as the repressor in Base Cytosol, where [LuxR-GFP Demo](../devstudio-luxr-gfp-demo/main.md) uses LuxR in S30 lysate. The two are not variants of one build.

This page specifies the demo as it is intended. The demo has not run.

# Modules

| Role | Module | In the demo |
| --- | --- | --- |
| Cascade | [CRAIC](../../modules/craic-cascade/spec.md) | what the embedding step builds |
| Detector | [Detector: 3OC6-HSL (EsaR)](../../modules/detector-esar/spec.md) | expressed from its own template, then gating PLA1 |
| Lysis | [Lysis: PLA1](../../modules/effector-pla1/spec.md) | expressed once repression lifts |
| Cytosol | [Base Cytosol](../../modules/base-cytosol/spec.md) | inside the synthetic cells |
| Substrate | [Substrate: CPRG](../../modules/substrate-cprg/spec.md) | held in its own carrier population |
| Reporter | [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) | in the gel, meeting CPRG only after lysis |
| Gel | [Gel: ULGA](../../modules/gel-ulga/spec.md) | set by cooling |
| Outer solution | [Outer Solution](../../modules/outer-solution/spec.md) | the class; no member is chosen |
| Analyte | [Analyte: 3OC6-HSL](../../modules/analyte-3oc6-hsl/spec.md) | the input |

:::{attention} Two slots name no member
@Editor(chicago): the membrane and the outer solution are unchosen. The source names a Membrane with no page and the Outer Solution class rather than one of its members. Record which of each the demo uses.
:::

# Processes

| Step | Process | In the demo |
| --- | --- | --- |
| 1 | [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md) | express EsaR, then mix it with the PLA1 template |
| 2 | [Encapsulation](../../processes/encapsulate/main.md) | the sensing cells, and separately the substrate carrier |
| 3 | [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) | ULGA, set by cooling |
| 4 | [Color Development](../../processes/color-development/main.md) | brings the gel to the conditions LacZ needs |
| 5 | [Colorimetric Readout](../../processes/colorimetric-readout/main.md) | the color is read |

Encapsulation appears twice and is the abstract process both times: neither the sensing cells' route nor the carrier's is chosen.

# Performance

:::{attention} Not yet run
@Editor(chicago): record the run when it happens: its date, its conditions and what the readout showed.
:::

The nearest confirmed result is a different composition. [LuxR-LacZ Sensor Cascade](../../modules/luxr-lacz-cascade/spec.md) runs the same PLA1-to-LacZ handoff from the same analyte, with LuxR in S30 lysate rather than EsaR in Base Cytosol, and its page carries what that produced.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
