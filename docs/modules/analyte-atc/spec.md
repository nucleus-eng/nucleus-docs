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

**aTc is membrane-permeable.** It crosses a POPC bilayer without help, which is why the [SensorCell[aTc ⟶ PLA1]](../atc-sensing-cell/spec.md) needs no membrane pore to be induced — the analyte reaches the cytosol on its own. That property is what makes aTc the easiest of the five analytes to use in an encapsulated format.

**This is an Analyte, so it is not a constituent of anything.** It reaches a sensing cell from outside, after the cell is closed.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} Working concentrations. Bands are from [tetR-aTc Detector](../detector-tetr-atc/spec.md); the cell-context figures are from [SensorCell[aTc ⟶ PLA1]](../atc-sensing-cell/spec.md).
| Band | Value | What it governs |
| --- | --- | --- |
| **Effective induction, Nucleus Cytosol** | **0.1 µM to 0.5 µM**, optimum ~0.25 µM to 0.35 µM | The working window in this cytosol |
| **Expression poisoning** | **above ~1 µM** | aTc inhibits the cell-free reaction itself, cutting baseline expression by 30–40% |
| Effective induction, lysate | 2.5 µM to 5 µM | The working window in lysate |
| Interference | above 50 µM to 100 µM | aTc's own yellow color overwhelms GFP fluorescence |
:::

:::{attention} The window is about ten times lower in Nucleus Cytosol than in lysate
Lysate work uses around 10 µM, and that concentration does not work in Nucleus Cytosol: at 10 µM the reaction is poisoned rather than induced, down to the level of a no-DNA control. A titration found induction between 0.1 µM and 0.5 µM, with an optimum near 0.25–0.35 µM, in solution and in a patterned gel (Group Meeting, Mary Kelly, Chicago Node, 2026-09-11).

**The mechanism is proposed, not established.** Anhydrotetracycline is a 30S ribosome inhibitor, and ribosomes sit at roughly 1.8 µM in this reaction — the same order as the dose. Magnesium sequestration was considered and argued down on stoichiometry: magnesium is near 8 mM, about 10⁴ higher.

**One thing that follows and is not measured:** TetR binds aTc, so a repressed reaction may see less free aTc than an unrepressed one at the same nominal dose. That would make the poisoning threshold depend on TetR concentration. @Editor(chicago): confirm.
:::

**The effective-induction bands and the interference threshold are different kinds of claim.** The effective window is a property of what the Detector responds to. The interference threshold is a property of the *assay* — it says the readout stops working, not that the Module does.

**Nucleus Cytosol needs about ten times less aTc than lysate, in both readouts.** The (2.5–5) µM band that [tetR-aTc Detector](../detector-tetr-atc/spec.md) gives as the effective window is a lysate figure. In Nucleus Cytosol the fluorescent system (`pT7-tetO-plamGFP`) peaked near 0.35 µM in encapsulated imaging. The colorimetric system (`TetO-PLA1` with a LacZ color readout) worked at 0.25–0.35 µM in a patterned gel; its response in [SensorCell[aTc ⟶ PLA1]](../atc-sensing-cell/spec.md) is not graded, saturating at or below 1 µM with no resolvable dose-dependence from 1 to 10 µM.

# Requirements

Requires a [tetR-aTc Detector](../detector-tetr-atc/spec.md) to be sensed at all — aTc alone does nothing.

**Requires no transport route.** Unlike an analyte that has to be carried across a bilayer, aTc diffuses through one. See [α-Hemolysin](../membrane-pore-ahly/spec.md) for the case where a pore *is* needed.

# Implementations

- [aTc Demo](../../implementations/devstudio-atc-demo/main.md): its analyte — dosed at 0, 1, 5 and 10 µM.

# Processes

None. An analyte is supplied to an assay rather than produced by a Nucleus process. It enters through whatever dosing step the readout protocol specifies — for the colorimetric route, [Colorimetric Readout](../../processes/colorimetric-readout/main.md).

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
