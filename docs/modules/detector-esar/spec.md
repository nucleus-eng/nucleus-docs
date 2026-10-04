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

The operator is `[EsaO]2`, two EsaO sites in tandem. A single-site version exists and is not the one in use.

The repressor is supplied in two steps, which is one more than every other detector has: the [CRAIC](../craic-cascade/spec.md) cascade expresses EsaR from a DNA template in one Base Cytosol, incubated overnight at 30 °C, and titrates the resulting protein into a second reaction carrying the operator construct.

:::{attention} Open question
@Editor(london): state whether the two-step expression belongs to this Module or to the cascade that uses it.
:::

:::{table} Constructs. Sequence files are on the DevStudio shared drive rather than in `nucleus-eng/DNA`.
:label: comp-detector-esar-constructs

| Construct | Role |
| --- | --- |
| `[EsaO]2-mNG` | characterization: the operator driving mNeonGreen, read as fluorescence |
| `[EsaO]2-PLA1` | the cascade's own construct: the operator driving PLA1 |

:::

# Expected Behavior

3OC6-HSL binds EsaR and relieves repression of the downstream coding sequence. **Repressors give lower noise floors than activators**.

**Characterized on a fluorescent reporter, not on the cascade's own output.** `[EsaO]2-mNG` was titrated against template at (0.1, 0.5 and 1) nM, with and without 5 µM 3OC6-HSL, against a fluorescein ladder at (0, 0.5, 1 and 2) µM. EsaR was held at a fixed dose. **This is the same split the aTc detector uses** — characterized on a reporter, built with PLA1 — so the measurement does not make the demonstration fluorescent.

:::{attention} No figure yet
@Editor(london): the titration above has no plot on this page. Add it, with the dose that was fixed.
:::

# Requirements

Requires the analyte to reach the repressor.

# Implementations

- [CRAIC Demo](../../implementations/devstudio-craic-demo/main.md): its detector — expressed from its own template, then gating PLA1.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
