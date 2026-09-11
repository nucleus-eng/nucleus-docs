---
title: "Gel: ULGA"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

ULGA Gel is an ultra-low-gelling-temperature agarose hydrogel, dissolved directly into the outer solution it will become and set by cooling. It is the matrix the London demo runs in. Compare to [Alginate Gel](../gel-alginate/spec.md), which reaches an equivalent result by ionic crosslinking instead of a thermal set, and to [PEGDA Gel](../gel-pegda/spec.md), whose geometry is set by projected light rather than by its container.

The property that makes ULGA usable with synthetic cells is its gel point. It sets at (8–17)°C, far below standard agarose, so the window between "still liquid enough to mix" and "cold enough to damage the contents" is wide.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

(gel-ulga-reference-composition)=
# Reference Composition

:::{table} ULGA gel, as prepared.
:label: comp-gel-ulga

| Component | Working concentration | Notes |
| --- | --- | --- |
| ULGA | 1% (w/v) in the prepared solution; 0.5% (w/v) once combined 1:1 with the cell suspension | dissolved into the outer solution below, not into water. Works from 0.2% to 0.5% in the set gel, and lower gives faster kinetics |
| Potassium L-glutamate | 578 mM | |
| HEPES, pH 7.4 | 72 mM | |
| Glucose | 300 mM | |
:::

Unlike the other three gels, ULGA is specified together with its solution rather than as an additive to someone else's. The salts and sugar above are the [London Chassis](../london-chassis/spec.md) outer solution, which matches inner to outer at about 920 mOsm.

A separate configuration replaces those three with 1200 mM glucose and 0.1 mM CaCl₂, used where the embedded cells carry [Base Cytosol](../base-cytosol/spec.md) rather than [S30 Lysate](../s30-lysate/spec.md). The 1200 mM figure is not arbitrary — above roughly 1200 mOsm, CPRG leakage from loaded liposomes drops sharply.

(gel-ulga-expected-behavior)=
# Expected Behavior

@Claude: somewhere in this document we should add the expected (or tolerated?) osmolarity range for Gel, as a member of Outer Solution fiber. this applies to all Outer Solution child pages. should also go into the .yml. 
## Gels

Expect a gel that stays liquid while warm, tolerates mixing with intact synthetic cells, and sets on cooling below its gel point without a crosslinker, a divalent load or any illumination.

Two results are confirmed in this matrix. At 1.5%, the two-liposome PLA1/CPRG/LacZ chemistry gives a visible color change from about 3 h at 37 °C, easily discernible by 16 h — see [PLA1 Lysis Module](../effector-pla1/spec.md). At 1%, encapsulated cells give a GFP readout scored after 2.5 h.

:::{note} The colorimetric result was measured at a superseded concentration
The 1.5% above is the condition that experiment ran at, and it is kept for that reason. New work uses 1% (w/v) in the prepared solution, which gives 0.5% (w/v) in the set gel.

The London Node confirmed the 1:1:2 combining ratio on 2026-09-09. Under that ratio 1.5% gives 0.75% (w/v) in the set gel, above the 0.2% to 0.5% working range — so the confirmed colorimetric result comes from a condition current practice does not use.
:::

:::{attention} The temperatures are not established
No dissolution temperature, hold time, or cooling target is recorded for this gel. Standard low-melting-agarose technique is to heat until the solution runs clear, then hold it above the gel point until use, but that is convention rather than a measured protocol here.
:::

(gel-ulga-requirements)=
# Requirements

Requires a heat excursion to dissolve — near boiling, with stirring — followed by cooling to a temperature that is still above the gel point but safe for the cells being mixed in. Anything mixed in at that point must survive the cooling and the set; nothing but the ULGA itself is present for the near-boiling step, and a component added onto the set gel afterwards experiences neither.

Requires the outer solution to be prepared first, since the agarose is dissolved into it rather than being added to a finished gel.

Imposes no divalent load and no illumination on its contents.

# Processes

Prepared and set by [Hydrogel Embedding: ULGA](../../processes/embed-ulga-hydrogel/main.md).

# Materials

:::{table} Purchased materials.

| Name | Category | Product | Manufacturer | Part # | Link |
| --- | --- | --- | --- | --- | --- |
| ULGA | Reagent | Ultra low gelling temperature agarose | Sigma-Aldrich | A5030 | [link](https://www.sigmaaldrich.com/GB/en/product/sial/a5030) |
:::

:::{attention} Two part numbers for the same reagent
The source records this agarose as both Sigma-Aldrich A5030 and Sigma-Aldrich A2576, "Agarose, Type IX-A, ultra low gelling temperature". @Editor(london): confirm which this process uses, or whether the imaging and embedding jobs genuinely use different agaroses.
:::

# Credits

Developed by Julia Purrinos De Oliveira (London Node), with the PLA1 colorimetric variant by Jonah McDonald and Charlie Newell.
