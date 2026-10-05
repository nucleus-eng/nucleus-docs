---
title: "LuxR-GFP Demo"
subtitle: Implementation
status: draft
site:
    hide-toc: true
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

The LuxR-GFP Demo detects a bacterial quorum-sensing signal and reports it as fluorescence from inside a gel. Synthetic cells built on [Cytosol: S30 Lysate](../../modules/s30-lysate/spec.md) carry a LuxR/pLux circuit. 3OC6-HSL released by bacteria outside the gel crosses the membrane, LuxR binds it, and the cells express [Reporter: deGFP](../../modules/reporter-degfp/spec.md).

**The input is a living bacterial culture, not a dosed small molecule.** That makes this a bacteria-detection device rather than a chemical sensor, and it is what distinguishes it from the aTc and pH demos.

What the embedding step builds is [LuxR-GFP Sensor Cascade](../../modules/luxr-gfp-cascade/spec.md).

# Modules

| Role | Module | In the demo |
| --- | --- | --- |
| Cascade | [LuxR-GFP Sensor Cascade](../../modules/luxr-gfp-cascade/spec.md) | what the embedding step builds |
| Cytosol | [Cytosol: S30 Lysate](../../modules/s30-lysate/spec.md) | inside the synthetic cells |
| Detector | [Detector: 3OC6-HSL (LuxR)](../../modules/detector-3oc6-hsl/spec.md) | LuxR with its pLux promoter |
| Reporter | [Reporter: deGFP](../../modules/reporter-degfp/spec.md) | the fluorescent output |
| Membrane | [Membrane: POPC](../../modules/membrane-popc/spec.md) | around the synthetic cells |
| Chassis | [Cell: S30 Lysate, POPC](../../modules/cell-s30-popc/spec.md) | the empty chassis this builds on |
| Outer solution | [Outer Solution: Glutamate-HEPES-Glucose](../../modules/outer-solution-glutamate/spec.md) | the phase the gel sets in |
| Gel | [Gel: ULGA](../../modules/gel-ulga/spec.md) | 1% (w/v), set by cooling |

:::{attention} The detector has no source document
@Editor(london): name the DevNote or paper that backs [Detector: 3OC6-HSL (LuxR)](../../modules/detector-3oc6-hsl/spec.md).
:::

# Processes

| Step | Process | In the demo |
| --- | --- | --- |
| 1 | Plasmid assemble | the LuxR and deGFP halves into one construct. **No Process page documents this step** |
| 2 | [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md) | the plasmid into S30 Lysate |
| 3 | [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) | the synthetic cells |
| 4 | [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) | ULGA at 1% (w/v), set by cooling |

# Performance

## In a gel

Embedded in 1% ULGA, POPC synthetic cells give a GFP response after 2.5 h with either an overnight bacterial culture or its supernatant. **Confirmed by Z-stack imaging**, which places the signal in intact embedded cells rather than in the surrounding gel. An LB-only control gives no signal at matched imaging settings.

This is the readout furthest along of the four demos: it is the only one confirmed in the gel format the demo calls for.

:::{attention} What this does not show
- **No dose response.** Two positive conditions and one negative. Nothing establishes how the signal varies with the amount of 3OC6-HSL, or how little the cells can detect.
- **No colorimetric readout.** This demo reports fluorescence. The LuxR path that reports color instead is a different composition, the LuxR-LacZ Sensor Cascade, and its results stay on that Module's page. It is named and not linked, because a Module link on this page reads as a claim that the demo is built from it.
- **Encapsulated expression is not fully controlled.** The Optiprep-free result that restores expression has no minus-inducer control, no no-DNA control, and no biological replicates.
:::

:::{attention} Reaction conditions do not reconcile
@Editor(london): the 3OC6-HSL row of the London demo's reaction table is off by 50×, and the plasmid dose appears as both 37 and 80 ng/µL. Give the final values.
:::

:::{attention} No process documents the reading
@Editor(london): the readout is a spectrometer reading of deGFP fluorescence under a UV lamp, and no Process page covers it.
:::

# Credits

Developed by the London Node (Elani Lab), with contributions from Ion Ioannou, Jonah McDonald, Charlie Newell and Manuel.

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
