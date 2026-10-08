---
title: "Control"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [Control: ClpXP](../control-clpxp/spec.md).
<!-- /gen:position -->

A class: a Module whose Function is to break down a defined set of proteins in its compartment.

What every member shares is selectivity. It breaks down only the proteins that carry its mark, and leaves the rest.

**One member today, as [Lysis](../lysis/spec.md) has.** A class is written when a Module needs its functional parent, and it does not wait for a second member.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [Control: ClpXP](../control-clpxp/spec.md) | ClpX and ClpP together, which break down only proteins carrying the ssrA tag, and use ATP to do it. |

# Expected Behavior

A member shortens the life of the proteins it targets, and leaves other proteins alone.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
