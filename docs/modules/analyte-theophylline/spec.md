---
title: "Analyte: Theophylline"
subtitle: "Module Specification"
status: canceled
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Theophylline is a xanthine derivative and the ligand of the translational riboswitch in the [Theophylline Detector](../detector-theophylline/spec.md), designed by [Lynch and Gallivan](https://doi.org/10.1093/nar/gkn924). Binding opens the switch and permits translation of the downstream effector gene.

**This is an Analyte, so it is not a constituent of anything.** It reaches a sensing cell from outside, after the cell is closed.

:::{attention} Canceled — its detector was cut
The [Theophylline Detector](../detector-theophylline/spec.md) and [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md) are both canceled: the riboswitch expresses its effector without theophylline present, so it does not discriminate. The DevStudio DNA list records all three theophylline constructs as no longer in use, with `T7-theo-lacZ` marked leaky.

**The constraint below outlives the decision.** It is a fact about theophylline and LacZ rather than about that Detector, which is why this page is kept for reference rather than removed. Theophylline is also still named as a candidate second sensor if one is wanted during the Studio.

An analyte with no working detector is kept for reference and is not maintained. Theophylline is still named as a candidate second sensor if one is wanted during the Studio, which is why this page is kept rather than removed.
:::

# Reference Composition

:::{table} Working concentrations.
| Band | Value | Source |
| --- | --- | --- |
| Riboswitch induction | not documented | — |
| Effect on the LacZ/CPRG reaction | 1 mM and 2 mM tested | see Requirements |
:::

# Requirements

Requires a [Theophylline Detector](../detector-theophylline/spec.md) to be sensed at all.

**Theophylline and [LacZ](../reporter-lacz/spec.md) are recorded as incompatible, and this is the page that carries the pair.** The constraint holds between the analyte and the reporter — neither of which is a Detector — so stating it here puts it at the arity it actually has. [LacZ Reporter](../reporter-lacz/spec.md) currently carries it, which reads as a property of the reporter rather than of the pair.

:::{attention} The mechanism is not established, and the usual explanation is partly contradicted
The constraint is normally given as theophylline directly inhibiting the LacZ/CPRG conversion "even at very low amounts." Against that:

- The one bulk figure available shows 1 mM and 2 mM theophylline making the LacZ/CPRG reaction roughly **twice as fast**, not slower.
- Riboswitch activation producing more LacZ could mask direct enzyme inhibition, so both effects can coexist — but no figure showing inhibition has been located.
- A literature spot-check found only weak, millimolar-range inhibition, which does not match the "very low amounts" framing.

@Editor(chicago): supporting titration data is reported to exist but has not been located. Confirm with the Chicago Node. Until then the constraint stands and its reason does not.
:::

# Processes

None. An analyte is supplied to an assay rather than produced by a Nucleus process.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
