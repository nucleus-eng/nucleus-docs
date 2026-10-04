---
title: "XylE"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by nothing on this branch.
<!-- /gen:position -->

XylE is catechol 2,3-dioxygenase (C23DO), the *xylE* gene product. It oxidizes colorless catechol into 2-hydroxymuconate semialdehyde, a yellow product read by absorbance near 375 nm to 385 nm ([Kunz and Chapman, 1981](https://doi.org/10.1128/jb.146.1.179-191.1981)). It is supplied as the DNA template pT7-TetO-catecholase (pMN067), expressed in a cell-free reaction.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Expected Behavior

XylE oxidizes catechol to 2-hydroxymuconate semialdehyde, which is yellow and absorbs near 375 nm to 385 nm. Catechol is its one documented substrate. @Editor: no rate or yield is recorded for the enzyme on its own.

# Requirements

Requires pT7 transcription and translation when supplied as the DNA template (e.g. [Base Cytosol](../base-cytosol/spec.md)).

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
