---
title: "Analyte: aTc"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Anhydrotetracycline (aTc) is the inducer the [tetR-aTc Detector](../detector-tetr-atc/spec.md) responds to. It binds TetR allosterically, releasing the repressor from the `tetO` operator and recovering expression of whatever sits downstream.

**aTc is membrane-permeable.** It crosses a POPC bilayer without help, which is why the [aTc Sensing Cell](../atc-sensing-cell/spec.md) needs no membrane pore to be induced — the analyte reaches the cytosol on its own. That property is what makes aTc the easiest of the five analytes to use in an encapsulated format.

**This is an Analyte, so it is not a constituent of anything.** It reaches a sensing cell from outside, after the cell is closed. The pages that compose aTc-sensing Modules say so explicitly and this page does not change that.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} Working concentrations. Bands are from [tetR-aTc Detector](../detector-tetr-atc/spec.md); the cell-context figures are from [aTc Sensing Cell](../atc-sensing-cell/spec.md).
| Band | Value | What it governs |
| --- | --- | --- |
| Effective induction | 2.5 µM to 5 µM | Below saturating and below toxic |
| Interference | above 50 µM to 100 µM | aTc's own yellow colour overwhelms GFP fluorescence |
| Cell-context saturation | at or below 1 µM | No resolvable dose-dependence from 1 to 10 µM |
:::

**The first two bands are different kinds of claim.** The effective window is a property of what the Detector responds to. The interference threshold is a property of the *assay* — it says the readout stops working, not that the Module does. They are recorded together because they arrive together on the detector page, not because they are the same thing.

:::{attention} The two dose statements in the corpus do not obviously agree
[tetR-aTc Detector](../detector-tetr-atc/spec.md) gives 2.5–5 µM as the effective window. [aTc Sensing Cell](../atc-sensing-cell/spec.md) reports its own configuration as **not graded**, saturating at or below 1 µM with no resolvable dose-dependence from 1 to 10 µM.

These are different configurations — `pT7-tetO-plamGFP` with a fluorescent readout against `TetO-PLA1` with a LacZ colour readout — so they need not agree. Neither page acknowledges the other. @Editor(chicago): confirm whether the effective window carries into the colorimetric configuration, or is specific to the fluorescent one.
:::

# Requirements

Requires a [tetR-aTc Detector](../detector-tetr-atc/spec.md) to be sensed at all — aTc alone does nothing.

**Requires no transport route.** Unlike an analyte that has to be carried across a bilayer, aTc diffuses through one. See [α-Hemolysin](../membrane-pore-ahly/spec.md) for the case where a pore *is* needed.

# Processes

None. An analyte is supplied to an assay rather than produced by a Nucleus process. It enters through whatever dosing step the readout protocol specifies — for the colorimetric route, [Colorimetric Readout](../../processes/colorimetric-readout/main.md).

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
