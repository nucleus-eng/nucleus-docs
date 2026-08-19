---
title: "London Membrane: POPC"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The London Membrane specifies a pure POPC bilayer — no cholesterol — used for every synthetic cell in the London demo. It is the membrane half of the [London Chassis](../london-chassis/spec.md), which encapsulates [S30 Lysate](../s30-lysate/spec.md) rather than [Base Cytosol](../base-cytosol/spec.md).

This is a different lipid system from the two cholesterol-containing membranes in the distribution, not a different ratio of the same one: [Base Membrane](../membrane-popc-chol/spec.md) is 70:30 POPC:cholesterol and [Chicago Membrane](../membrane-popc-chol-chicago/spec.md) is 90:10. The London Membrane carries no cholesterol at all.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Membrane Composition

Three variants are documented, and they share one base. The base bilayer is 100% POPC; the two additive tables below are optional layers on top of it — a fluorescent label for imaging, and a PEGylated lipid for steric stabilization. Pick the additives the experiment needs; the base does not change.

## Base membrane

:::{table} London Membrane base bilayer.
:label: comp-membrane-popc-base

| Component | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| --------- | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC      | 100                   | 760.076                  | 25                          | 80                 |

:::

A 2 mg POPC film (80 µL of a 25 mg/mL chloroform stock) is dried and resuspended in 500 µL mineral oil, giving a 4 mg/mL working lipid concentration. This is the recipe used for the S30/POPC encapsulation work documented on [S30 Lysate](../s30-lysate/spec.md).

## Functional membrane components

DSPE-PEG2000 is a PEGylated lipid used in the London colorimetric (PLA1) work. The PEG headgroup provides steric stabilization at the bilayer surface — a functional change, not a labeling one.

:::{table} PEGylated variant, as used in the London PLA1 colorimetric work.
:label: comp-membrane-popc-pegylated

| Component     | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------- | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC          | 99.15                 | 760.076                  | 25                          | 130.4              |
| DSPE-PEG2000  | 0.85                  | 2805.5                   | 10                          | 10.32              |

:::

These volumes prepare 3.5 batches. One batch is 320 µL of lipid-in-oil at 3 mg/mL: 120 µL for layering the emulsion phase-transfer column, and 200 µL for preparing emulsions, at 20 µL of inner solution per 200 µL of lipid-in-oil.

:::{note} This is the one documented cytosol-to-lipid ratio in the DevCells set
The 20 µL inner solution per 200 µL lipid-in-oil figure above (1:10) is the only explicitly documented ratio for this combination step. [Chicago Chassis](../chicago-chassis/spec.md) flags the equivalent ratio as an open gap for the Chicago formulation — do not carry this London figure across to it without confirming.
:::

## Fluorescent labeling (optional)

18:1 Cyanine 5 PC is the fluorescent label used for the ULGA hydrogel-embedding work, where it reports membrane integrity by imaging. It plays the same role Liss-Rhod PE plays in the Base and Chicago membranes.

:::{table} Fluorescently labeled variant, as used in the ULGA hydrogel work.
:label: comp-membrane-popc-labeled

| Component          | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC               | 99.9                  | 760.076                  | 25                          | 79.863             |
| 18:1 Cyanine 5 PC  | 0.1                   | 1316.26                  | 1                           | 3.423              |

:::

:::{attention} Two values corrected against the source — confirm with the London team
The source table (`Demo Status - London.docx`, Module 4) lists the Cyanine 5 PC stock as **25 mg/mL** and POPC's target percentage as **0.99**. Neither reconciles with the stated volumes:

- At a 25 mg/mL Cy5 stock, the given volumes yield 97.58 mol% POPC and 2.42 mol% Cy5 — roughly 24× more dye than a 0.1% target.
- At a **1 mg/mL** Cy5 stock, the same volumes yield **99.90 mol% POPC and 0.099 mol% Cy5**, matching the intended 99.9 : 0.1 exactly.

A 1 mg/mL dye stock is also the convention elsewhere in this distribution — Liss-Rhod PE is stocked at 1 mg/mL in both [Base Membrane](../membrane-popc-chol/spec.md) and [Chicago Membrane](../membrane-popc-chol-chicago/spec.md). The table above therefore uses 1 mg/mL and 99.9%, and the `25` in the source reads as a copy-paste from the POPC row above it. Flagged rather than applied silently: confirm before use at the bench.
:::

# Expected Behavior

Encapsulating S30 Lysate in this membrane produces synthetic cells that express an encapsulated reporter on induction. The characterization, including the Optiprep yield-versus-expression tradeoff and the controls still outstanding, is documented on [S30 Lysate](../s30-lysate/spec.md) and is not duplicated here.

# Protocols

The membrane is prepared and encapsulated by the shared mineral-oil phase-transfer method in [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md). Hydrogel embedding of the labeled variant is documented in [ULGA Hydrogel Embedding](../../processes/embed-ulga-hydrogel/main.md).

# Credits

Developed by Ion Ioannou and Jonah McDonald (London node, Elani Lab) — S30/POPC encapsulation and the base membrane recipe.

Developed by Jonah McDonald and Charlie Newell (London node) — the PEGylated variant used in the PLA1 colorimetric work.

:::{attention} Attribution needs confirmation
Contributor names and their mapping to each variant are taken from the module sections of `Demo Status - London.docx`. The split between who developed which variant has not been confirmed by the London team.
:::
