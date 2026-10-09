---
title: "Lysis"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [Lysis: PLA1](../effector-pla1/spec.md).
<!-- /gen:position -->

A class: a Module whose Function is to break a membrane.

Every member imposes on whatever shares its compartment. That is the thing the class exists to say once: the imposition belongs to Lysis, and a member inherits it by implementing the Function rather than by restating it.

A membrane that breaks is not a member. The member is what does the breaking.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [PLA1](../effector-pla1/spec.md) | Phospholipase A1, genetically encoded. Hydrolyzes the bilayer it is expressed inside. |

# Expected Behavior

Any member destroys phospholipid membranes in reach. It does not distinguish the membrane that produced it from a neighbor's, which is why the scope of the imposition is the compartment and not the Module.

# Requirements

Every member requires something to drive it with a low enough background that the uninduced state does not already lyse. A member expressed from DNA inherits the transcription and translation requirements of whatever expresses it.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
