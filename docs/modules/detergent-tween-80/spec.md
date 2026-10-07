---
title: "Detergent: Tween 80"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Tween 80 (polysorbate 80) is a non-ionic [Detergent](../detergent/spec.md). It is used to keep a purified protein soluble and to stop it sticking to the wall of its tube, so it reaches a reaction as a formulation component of somebody else's stock rather than as a reagent anybody chose to add.

**This Module is here because of what it does to a bilayer, not because of what it is for.** It makes a [Membrane](../membrane/spec.md) leak. In a device that works by holding an enzyme apart from its substrate, a leaking bilayer removes the off state, and the readout reads as triggered when nothing has triggered it.

**The route in is a protein stock.** The purified His-tagged TetR used by the [tetR-aTc Detector](../detector-tetr-atc/spec.md) (MedChemExpress, HY-P71520A) is lyophilized from a solution containing 0.02% Tween 80. The concentration that reaches a reaction depends on the volume the powder is reconstituted into and on the dilution into the reaction, and neither is recorded for any run here.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} What is known about the dose.
| Quantity | Value | Where it comes from |
| --- | --- | --- |
| In the supplied formulation | 0.02% (w/v) | The vendor's formulation for MedChemExpress HY-P71520A |
| After reconstitution | not recorded | Depends on the volume the powder is taken up in |
| In the reaction | not recorded | Depends on the dilution of the protein stock |
| Threshold for leakage | not measured | — |
:::

# Expected Behavior

Liposomes in a reaction that received this stock leaked enough to disrupt a colorimetric readout. No concentration series was run, so the figure at which the effect starts is not known, and the four rows above are why: three of them are unrecorded.

# Requirements

None.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
