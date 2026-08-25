---
title: "Chicago Chassis"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
---

# Overview

The Chicago Chassis is used for the Chicago Node's DevStudio Demo and combines [Base Cytosol](../base-cytosol/spec.md) with the [Chicago Membrane](../membrane-popc-chol-chicago/spec.md) (9:1 POPC:cholesterol). This cell is extended in downstream demo variants by adding sensing and reporter modules (e.g., the [Theophylline Sensing Module](../detector-theophylline/spec.md) driving the [PLA1 Lysis Module](../effector-pla1/spec.md), giving the [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md)).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    BASE_CYTOSOL["Base Cytosol"]
    CHICAGO_CHASSIS["Chicago Chassis"]
    MEMBRANE_POPC_CHOL_CHICAGO["Chicago Membrane: POPC/Chol"]

    BASE_CYTOSOL --> CHICAGO_CHASSIS
    MEMBRANE_POPC_CHOL_CHICAGO --> CHICAGO_CHASSIS

    classDef constituent fill:#6B7280,color:#ffffff,stroke:#4B5563;
    classDef this fill:#374151,color:#ffffff,stroke:#111827;
    class BASE_CYTOSOL,MEMBRANE_POPC_CHOL_CHICAGO constituent;
    class CHICAGO_CHASSIS this;

    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click CHICAGO_CHASSIS "/docs/modules/chicago-chassis/spec"
    click MEMBRANE_POPC_CHOL_CHICAGO "/docs/modules/membrane-popc-chol-chicago/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Cytosol

:::{warning} Cytosol Composition is not verified!
Below is an approximate composition table for the cytosolic components in the Chicago Chassis, based on the composition of [Base Cytosol](../base-cytosol/spec.md) and have not been verified by the module developers. 
:::

| Component         | Input concentration | Final concentration | Volume for one reaction (µL) |
| ----------------- | ------------------- | ------------------- | ---------------------------- |
| SMix              | 3.33x               | 1x                  | 12                           |
| PMix              | 15 mg/mL            | 1.80 mg/mL          | 4.8                          |
| Ribosomes         | 10 µM               | 1.8 µM              | 7.2                          |
| tRNA              | 35 mg/mL            | 3.5 mg/ml           | 4                            |
| RNase Inhibitor   | 40 000 U/mL         | 2000 U/mL           | 2                            |
| Optiprep          | 1.32 mg/µL          | 0.043 mg/µL         | 1.33                         |
| template DNA      | X nM                | Y nM                | -                            |
| Water             |                     |                     | to 40 µL final volume        |
:::

::::

::::{tab-item} Membrane

:::{table}
:label: comp-chicago-membrane

| Component               | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ----------------------- | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC                    | 89.9                  | 760.076                  | 25                          | 41                 |
| Cholesterol             | 10                    | 386.66                   | 50                          | 1.16               |
| (Optional) Liss-Rhod PE | 0.1                   | 1301.71                  | 1                           | 1.952              |

:::

Volumes are the synthetic-cell preparation at 0.5 mM total lipid. See [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md) for the full membrane spec and the SUV preparation.

::::

::::{tab-item} Outer Solution

:::{table} Outer solution.
:label: comp-chicago-chassis-outer

| Component | Working concentration |
| --- | --- |
| Glucose in ultrapure water | To 1180 mOsm |
:::

Match outer and inner solution osmolarities empirically with a vapor-pressure osmometer where possible.

:::{attention} Solutes not documented
@Editor: only the osmolarity target is recorded, not the solutes and their concentrations. Glucose in ultrapure water is the working default. Confirm with the Chicago Node.

:::

::::

:::::

# Expected Behavior

- **Yield and morphology.** Count round, intact cells ≥5 µm per imaging field by fluorescence or brightfield microscopy. Counts should stay stable through incubation at the reaction's working temperature (e.g. 37 °C); a drop over time points to membrane instability rather than an expression problem.
- **Functional encapsulation.** Confirm reporter expression (e.g., [deGFP](../reporter-degfp/spec.md)) by fluorescence microscopy. Expect cell brightness to not be uniform.

# Processes

The chassis is formed by encapsulating [Base Cytosol](../base-cytosol/spec.md) in a [9:1 POPC:cholesterol membrane](../membrane-popc-chol-chicago/spec.md) using [emulsion phase transfer](../../processes/assemble-base-cell/main.md).

# Constituent Modules

- [Base Cytosol](../base-cytosol/spec.md)
- [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md)

# Implementations

- [Chicago DevCell](../../implementations/chicago-devcell/main.md): the chassis for the Chicago demo's synthetic cells.

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).
