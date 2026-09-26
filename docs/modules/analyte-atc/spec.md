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
| **Effective induction, Nucleus Cytosol** | **0.1 µM to 0.5 µM**, optimum ~0.25 µM to 0.35 µM | The working window in this cytosol |
| **Expression poisoning** | **above ~1 µM** | aTc inhibits the cell-free reaction itself, cutting baseline expression by 30–40% |
| Effective induction, lysate | 2.5 µM to 5 µM | The figure this page previously gave without qualification. It is a lysate figure |
| Interference | above 50 µM to 100 µM | aTc's own yellow color overwhelms GFP fluorescence |
:::

:::{attention} The window is about ten times lower in Nucleus Cytosol than in lysate
Chicago Node, 2026-09-11. Lysate work — including the lab that has run this sensor longest — uses around 10 µM, and that concentration does not work in Nucleus Cytosol: at 10 µM the reaction is poisoned rather than induced, down to the level of a no-DNA control. A titration found induction between 0.1 µM and 0.5 µM, with an optimum near 0.25–0.35 µM, confirmed both in solution and in a patterned gel.

**The mechanism is proposed, not established.** Anhydrotetracycline is a 30S ribosome inhibitor, and ribosomes sit at roughly 1.8 µM in this reaction — the same order as the dose. Magnesium sequestration was considered and argued down on stoichiometry: magnesium is near 8 mM, about 10⁴ higher.

**One thing that follows and is not measured:** TetR binds aTc, so a repressed reaction may see less free aTc than an unrepressed one at the same nominal dose. That would make the poisoning threshold depend on TetR concentration. @Editor(chicago): confirm.
:::

**The first two bands are different kinds of claim.** The effective window is a property of what the Detector responds to. The interference threshold is a property of the *assay* — it says the readout stops working, not that the Module does. They are recorded together because they arrive together on the detector page, not because they are the same thing.

:::{attention} The two dose statements in the corpus do not obviously agree
[tetR-aTc Detector](../detector-tetr-atc/spec.md) gives (2.5–5) µM as the effective window. [aTc Sensing Cell](../atc-sensing-cell/spec.md) reports its own configuration as **not graded**, saturating at or below 1 µM with no resolvable dose-dependence from 1 to 10 µM.

These are different configurations — `pT7-tetO-plamGFP` with a fluorescent readout against `TetO-PLA1` with a LacZ color readout — so they need not agree.

**Resolved 2026-09-11, and the split is cytosol against lysate rather than fluorescent against colorimetric.** The (2.5–5) µM band is a lysate figure. Nucleus Cytosol wants roughly ten times less, in both readouts: the fluorescent system peaked near 0.35 µM in encapsulated imaging, and the colorimetric one worked at 0.25–0.35 µM in a patterned gel.
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
