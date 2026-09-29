---
title: "Detector: EsaR"
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

**This page is a position that the corpus has been describing for some time without occupying.** [Detector](../detector/spec.md) marks it in its Analyte × Mechanism table as *"EsaR — in redesign, no page"*, and [Repressor Detector](../repressor-detector/spec.md) carries the same gap in its own member table, where the row reads *"no. London is designing it."*

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. **This corpus holds no EsaR construct and no EsaR data.** Every claim below is design intent carried from [Detector: 3OC6-HSL](../detector-3oc6-hsl/spec.md), not a result.
:::

# Reference Composition

Not established. The [CRAIC](../craic-cascade/spec.md) board expresses EsaR from a DNA template in one Base Cytosol and mixes the resulting protein into a second, which is two steps where every other detector in this corpus has one. Whether that split belongs to this Module or to the cascade that uses it is not settled.

# Expected Behavior

3OC6-HSL binds EsaR and relieves repression of the downstream coding sequence. **Repressors give lower noise floors than activators**, which is why the London Node is redesigning around this one.

# Requirements

Requires the analyte to reach the repressor. Nothing here states a working concentration, because no run has produced one.

# Implementations

Not used in a documented Implementation. [CRAIC](../craic-cascade/spec.md) composes it as design intent.

# Credits

Facts carried from [Detector: 3OC6-HSL](../detector-3oc6-hsl/spec.md), which records the homology, the inverted logic, the noise-floor argument and the Biocrest source. Position read from [Detector](../detector/spec.md) and [Repressor Detector](../repressor-detector/spec.md).
