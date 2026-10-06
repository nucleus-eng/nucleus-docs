---
title: "Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [`atc-cascade`](../atc-cascade/spec.md), [`craic-cascade`](../craic-cascade/spec.md), [`luxr-gfp-cascade`](../luxr-gfp-cascade/spec.md), [`luxr-lacz-cascade`](../luxr-lacz-cascade/spec.md), [`ph-cascade`](../ph-cascade/spec.md).
<!-- /gen:position -->

A class: a Module that runs sensing, lysis and readout as one chain.

Every member ends at a color change. What varies is what it senses and how the readout is reached, not whether the chain closes.

A Cascade is a Cell, not a thing that contains cells. Its final step packs a cytosol and a membrane like any other, and the chain is what its Composition records.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [aTc Cascade](../atc-cascade/spec.md) | Senses aTc through TetR. |
| [CRAIC Cascade](../craic-cascade/spec.md) | Two populations, sensing and substrate-carrying, in one gel. |
| [LuxR-deGFP Cascade](../luxr-gfp-cascade/spec.md) | Fluorescent readout rather than colorimetric. |
| [LuxR-LacZ Cascade](../luxr-lacz-cascade/spec.md) | Senses 3OC6-HSL, reads out through LacZ. |
| [pH Cascade](../ph-cascade/spec.md) | Senses pH through a toehold switch. |
| [pH Cascade, One Vesicle](../ph-cascade-one-vesicle/spec.md) | The same cascade with sensing and substrate in one compartment. |

# Expected Behavior

Any member takes a stimulus and returns a signal a reader can see. The chain is sense, then lyse, then develop. A member that stops short of the readout is a Sensing Cell rather than a Cascade.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
