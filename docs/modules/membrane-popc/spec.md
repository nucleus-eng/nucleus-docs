---
title: "London Membrane: POPC"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The London Membrane uses a pure POPC bilayer without cholesterol and is used for every synthetic cell in the London demo. Compare to [Base Membrane](../membrane-popc-chol/spec.md) (70:30 POPC:cholesterol) and [Chicago Membrane](../membrane-popc-chol-chicago/spec.md) (90:10 POPC:cholesterol), which include cholesterol. Optionally, this membrane can include 0.1 mol% fluorescently tagged lipids to facilitate visualization.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Membrane Composition

:::{table} London Membrane base bilayer.
:label: comp-membrane-popc-base

| Component                    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) (@Claude: recalculate! these are wrong) | Notes                                                           |
| ---------------------------- | --------------------- | ------------------------ | --------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------- |
| POPC                         | 99                    | 760.076                  | 25                          | 80                                                         | -                                                               |
| (Optional) DSPE-PEG2000      | 0.85                  | 2805.5                   | 10                          | 10.32                                                      | stabilizes membrane (@Claude: verify, and add to questionnaire) |
| (Optional) 18:1 Cyanine 5 PC | 0.1                   | 1316.26                  | 1                           | 3.423                                                      | red fluorescence                                                |

:::

DSPE-PEG2000 is a PEGylated lipid used in the London colorimetric (PLA1) work. The PEG headgroup provides steric stabilization at the bilayer surface — a functional change, not a labeling one. 18:1 Cyanine 5 PC is a red fluorescently-tagged lipid that is used similarly to Liss-Rhod PE. 

# Expected Behavior

The London Membrane is used in all synthetic cell preps in the London Demo. This membrane module can be used generally to encapsulate Cytosolic modules. See [London Chassis](../london-chassis/spec.md) for more information.

# Protocols

The membrane is prepared and encapsulated by the shared mineral-oil phase-transfer method in [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md). Hydrogel embedding of the labeled variant is documented in [ULGA Hydrogel Embedding](../../processes/embed-ulga-hydrogel/main.md).

To prepare this membrane, assemble 2 mg total lipids (e.g., 80 µL of a 25 mg/mL chloroform stock). Dry, then resuspend in 500 µL mineral oil (4 mg/mL working concentration). 

# Credits

Developed by Ion Ioannou and Jonah McDonald (London node, Elani Lab), and extended by Jonah McDonald and Charlie Newell (London node) with PEGylated lipids.
