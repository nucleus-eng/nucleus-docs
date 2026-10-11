---
title: "Emitter"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [Emitter: IV-HSL](../emitter-ivhsl/spec.md).
<!-- /gen:position -->

A class: a Module whose Function is to make a signal molecule and release it outside the compartment it is made in.

What every member shares is where its product goes. The signal leaves the compartment, so a Module in another compartment, or in another cell, can sense it.

**One member today, as [Lysis](../lysis/spec.md) has.** A class is written when a Module needs its functional parent, and it does not wait for a second member.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [Emitter: IV-HSL](../emitter-ivhsl/spec.md) | Expresses the enzyme BjaI, which makes N-isovaleryl-L-homoserine lactone (IV-HSL). IV-HSL crosses a synthetic cell's membrane. |

# Expected Behavior

Any member's signal ends up outside the compartment that made it, where any Module in reach that senses it can respond.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
