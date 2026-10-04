---
title: "Detector: 3OC6-HSL (EsaR)"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`repressor-detector`](../repressor-detector/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

A 3OC6-HSL detector built on a repressor rather than an activator. EsaR is a LuxR homolog that represses where LuxR activates, so the logic is inverted: analyte relieves repression instead of switching a promoter on.

The [CRAIC](../craic-cascade/spec.md) cascade composes it, as design intent.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. Every claim below is design intent, not a result.

@Editor(london): supply the EsaR construct, a working concentration and titration data.
:::

# Reference Composition

The composition is not established. The [CRAIC](../craic-cascade/spec.md) cascade expresses EsaR from a DNA template in one Base Cytosol and mixes the resulting protein into a second, which is two steps where every other detector has one.

:::{attention} Open question
@Editor(london): state whether the two-step expression belongs to this Module or to the cascade that uses it.
:::

# Expected Behavior

3OC6-HSL binds EsaR and relieves repression of the downstream coding sequence. **Repressors give lower noise floors than activators**.

# Requirements

Requires the analyte to reach the repressor.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
