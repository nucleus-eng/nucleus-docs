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

# Reference Composition

:::::{tab-set}

::::{tab-item} Lipid Composition

:::{table} London Membrane lipids.
:label: comp-membrane-popc-base

| Component                    | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Notes                |
| ---------------------------- | ------------------------ | --------------------------- | -------------------- |
| POPC                         | 760.076                  | 25                          | bilayer-forming lipid |
| (Optional) DSPE-PEG2000      | 2805.5                   | 10                          | stabilizes membrane   |
| (Optional) 18:1 Cyanine 5 PC | 1316.26                  | 1                           | red fluorescence      |

:::

DSPE-PEG2000 is a PEGylated lipid used in the London colorimetric (PLA1) work. The PEG headgroup provides steric stabilization at the bilayer surface — a functional change, not a labeling one. 18:1 Cyanine 5 PC is a red fluorescently-tagged lipid that is used similarly to Liss-Rhod PE. The two optional lipids come from two separate documented preparations and have never been combined in one membrane.

::::

::::{tab-item} Documented Preparations

:::{table} Documented preparations of the London membrane. Each row is a self-consistent recipe; the two optional lipids are not mixed.
:label: comp-membrane-popc-preps

| Preparation                 | Target composition (mol %)      | POPC (µL) | DSPE-PEG2000 (µL) | 18:1 Cyanine 5 PC (µL) | Total lipid (mg) |
| --------------------------- | ------------------------------- | --------- | ----------------- | ---------------------- | ---------------- |
| PEGylated membrane          | 99.15 POPC : 0.85 DSPE-PEG2000  | 130.4     | 10.32             | —                      | 3.36             |
| Fluorescently labeled membrane | 99.9 POPC : 0.1 Cyanine 5 PC | 79.863    | —                 | 3.423                  | 2.00             |

:::

Both rows reconcile against the stocks in the Lipid Composition tab. The PEGylated recipe gives 99.150 mol% POPC and 0.850 mol% DSPE-PEG2000; the labeled recipe gives 99.901 mol% POPC and 0.099 mol% Cyanine 5 PC. The PEGylated preparation is a 3.5× batch (1× batch = 320 µL lipid-in-oil at 3 mg/mL); the labeled preparation is the 2 mg single-batch scale described under Process below.

:::{warning} Cyanine 5 stock concentration is disputed
One record gives the 18:1 Cyanine 5 PC stock as **25 mg/mL**. At 25 mg/mL the volumes above give 2.42 mol% dye — about 24× the 0.1 mol% target. At **1 mg/mL** they give 0.099 mol%, matching the target exactly, and 1 mg/mL is the dye-stock convention used for Liss-Rhod PE in both other Nucleus membranes. The table above uses 1 mg/mL on that reasoning.

@Editor(london): confirm the Cyanine 5 PC stock concentration with the London Node before bench use.
:::

::::

:::::

# Expected Behavior

The London Membrane is used in all synthetic cell preps in the London Demo. This membrane module can be used generally to encapsulate Cytosolic modules. See [London Chassis](../london-chassis/spec.md) for more information.

# Processes

The membrane is prepared and encapsulated by the shared mineral-oil phase-transfer method in [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md). Hydrogel embedding of the labeled variant is documented in [ULGA Hydrogel Embedding](../../processes/embed-ulga-hydrogel/main.md).

To prepare this membrane, assemble 2 mg total lipids (e.g., 80 µL of a 25 mg/mL chloroform stock). Dry, then resuspend in 500 µL mineral oil (4 mg/mL working concentration). 

# Implementations

- [London DevCell](../../implementations/london-devcell/main.md): the membrane of the London demo's synthetic cells.

# Credits

Developed by Ion Ioannou and Jonah McDonald (London Node, Elani Lab), and extended by Jonah McDonald and Charlie Newell (London Node) with PEGylated lipids.

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
