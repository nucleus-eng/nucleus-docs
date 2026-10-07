---
title: "Detergent"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [Detergent: Triton X-100](../detergent-triton-x-100/spec.md), [Detergent: Tween 80](../detergent-tween-80/spec.md).
<!-- /gen:position -->

A class: a Module whose subject is an amphiphilic molecule that partitions into a lipid bilayer.

Every member has a water-loving head and an oil-loving tail, which is what lets it sit in a bilayer rather than beside one. At a low enough concentration a member makes a bilayer leak. At a high enough concentration it takes the bilayer apart.

The class exists because the two effects are the same mechanism at two doses, and because a detergent reaches a reaction without anybody choosing to add one. A purified protein stock is formulated with a detergent to keep the protein soluble, so the detergent arrives with the protein.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [Triton X-100](../detergent-triton-x-100/spec.md) | Used here at a dose that dissolves the bilayer, as the positive lysis control. |
| [Tween 80](../detergent-tween-80/spec.md) | Arrives as a formulation component of a purified protein stock, at a dose that makes the bilayer leak. |

# Expected Behavior

Any member makes a lipid bilayer leak at some concentration, and dissolves it at a higher one. Where either threshold sits is not claimed here, and no run documented here records it.

A device that reads out by holding two things in separate compartments stops working when the bilayer between them leaks. The failure looks like a readout that is on before it is triggered, because the thing that was being held apart is no longer held apart.

# Requirements

None. A member needs nothing to act on a bilayer.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
