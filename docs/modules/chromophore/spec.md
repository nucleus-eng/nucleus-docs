---
title: "Chromophore"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [deGFP Reporter](../reporter-degfp/spec.md), [mNeonGreen Reporter](../reporter-mneongreen/spec.md), [Substrate: CPRG](../substrate-cprg/spec.md), [Substrate: X-Gal](../substrate-xgal/spec.md).
<!-- /gen:position -->

A class: a Module whose subject is a molecule that absorbs visible light.

Every member has a conjugated system, and that is what both makes it colored and makes it bleach. The class fixes what members are made of. What they are used for varies: one is a substrate an enzyme cleaves, another is a protein a cell expresses.

It cuts across the rest of the tree rather than sitting in it. A member is also a [Substrate](../substrate/spec.md), or a [Reporter](../reporter/spec.md), and `refines:` carries both.

This class is not Color. Color is what an object emits that a reader can detect, which is the codomain of an emitting operation. A chromophore is what the emission comes out of, which is the domain. Making one class of both confuses what goes in with what comes out.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [CPRG](../substrate-cprg/spec.md) | Yellow as supplied. Cleavage yields a second chromophore, the red product. |
| [X-Gal](../substrate-xgal/spec.md) | Colorless as supplied; the indigo product is the chromophore. |
| [deGFP Reporter](../reporter-degfp/spec.md) | A fluorescent protein. Absorbs and re-emits rather than absorbing alone. |
| [mNeonGreen Reporter](../reporter-mneongreen/spec.md) | A fluorescent protein. Absorbs and re-emits rather than absorbing alone. |

# Expected Behavior

Any member bleaches under enough ultraviolet light. How much is enough varies by member and is not claimed here.

# Requirements

A member used as a readout requires that nothing in the path has already bleached it. A photopatterned gel is the case this corpus meets: the patterning step emits at 405 nm, and a member present during patterning is exposed before it is read.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
