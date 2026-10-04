---
title: "Container"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [`gel`](../gel/spec.md), [`membrane`](../membrane/spec.md), [`solution`](../solution/spec.md).
<!-- /gen:position -->

A class: a Module that holds other things.

Every member holds: it keeps what is inside it in a defined relation to what is outside, and to the other things inside. The class does not fix what the boundary is made of, whether it is a surface or a network, or whether the inside is a volume or a position.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [Membrane](../membrane/spec.md) | A closed lipid bilayer. What it holds is a volume, separated from the outside by a barrier that something must cross. |
| [Gel](../gel/spec.md) | A polymer network. What it holds is fixed in position and stays in contact with the solution around it. |
| [Solution](../solution/spec.md) | Dissolution. What it holds is free to move in one phase, and nothing separates it from the rest. |

# Expected Behavior

What a member holds stays in the relation its way of holding sets: behind a barrier, fixed in place, or free to move.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
