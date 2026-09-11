---
title: "Analyte: Theophylline"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Theophylline is a xanthine derivative and the ligand of the translational riboswitch in the [Theophylline Detector](../detector-theophylline/spec.md), designed by [Lynch and Gallivan](https://doi.org/10.1093/nar/gkn924). Binding opens the switch and permits translation of the downstream effector gene.

**This is an Analyte, so it is not a constituent of anything.** It reaches a sensing cell from outside, after the cell is closed.

:::{attention} The Detector is cancelled; this page is not
[Theophylline Detector](../detector-theophylline/spec.md) is marked *"Canceled — not part of the DevCells demo"*. This page exists anyway, because the constraint below is a fact about theophylline and LacZ rather than about that Detector, and it outlives the demo decision.
:::

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
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
