---
title: "Solution"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [Container](../container/spec.md). Refined by [Cytosol](../cytosol/spec.md), [Outer Solution](../outer-solution/spec.md).
<!-- /gen:position -->

A class: a [Container](../container/spec.md) whose contents are dissolved in one phase.

What a Solution holds is free to move. It keeps its solutes in one phase and separates them from nothing.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [Outer Solution](../outer-solution/spec.md) | The solutes of the phase a synthetic cell is suspended in are dissolved in one phase. |
| [Cytosol](../cytosol/spec.md) | The machinery of a cell-free reaction is dissolved in one compartment. |

# Expected Behavior

Every solute in a Solution is free to move through the whole phase. Nothing inside separates one part from another.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
