---
title: "Chicago Membrane: POPC/Chol"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Chicago Membrane specifies a 9:1 POPC:cholesterol bilayer, used for every liposome in the Chicago demo — both the synthetic cells that carry the cell-free cytosol and the CPRG-loaded SUVs that carry the substrate.

This is a distinct Module from the default [Base Membrane](../membrane-popc-chol/spec.md), which is 70:29.95 POPC:cholesterol — a ratio of about 2.3:1, not 3:1. The two are separate concrete formulations of the same POPC/cholesterol lipid system, not competing values for one Module.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
pie showData
    title Chicago Membrane base bilayer (mol %)
    "POPC" : 90
    "Cholesterol" : 10
```

No published schematic exists for this membrane; the pie chart shows lipid composition as a simplified summary, not a structural bilayer diagram. **A structural schematic — like the [Base Membrane](../membrane-popc-chol/spec.md) liposome figure — or a micrograph is still needed from the dev team.**

# Membrane Composition

One base bilayer, prepared at two scales, with the fluorescent label added or omitted depending on what the liposome is for.

## Base membrane

:::{table} Chicago Membrane base bilayer.
:label: comp-membrane-chicago-base

| Component   | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) |
| ----------- | --------------------- | ------------------------ | --------------------------- |
| POPC        | 90                    | 760.076                  | 25                          |
| Cholesterol | 10                    | 386.66                   | 50                          |

:::

Two preparations of this base are documented, at different scales and by different methods:

:::{table} Documented preparations of the Chicago base membrane.
:label: comp-membrane-chicago-preps

| Preparation | POPC (µL) | Cholesterol (µL) | Fluorescent label | Method |
| --- | --- | --- | --- | --- |
| Synthetic cells, per 3 mL lipid-in-oil (0.5 mM total lipid) | 41 | 1.16 | Liss-Rhod PE, added — see below | Inverted-emulsion phase transfer |
| CPRG-loaded SUVs | 208.51 | 6.00 | none | Lipid-film hydration and extrusion |

:::

Source: the Chicago Module Integration Status writeup (`Demo Status - Chicago.docx`).

## Fluorescent labeling (optional)

Lissamine Rhodamine PE labels the membrane for imaging. It is used for the synthetic cells and **omitted** from the CPRG-loaded SUV preparation, where the readout is absorbance rather than fluorescence.

:::{table} Fluorescent label, synthetic-cell preparation only.
:label: comp-membrane-chicago-dye

| Component    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL, per 3 mL lipid-in-oil) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ----------------------------------------- |
| Liss-Rhod PE | 0.1                   | 1301.72                  | 1                           | 1.952                                     |

:::

:::{note} Why these are one Module and not two
With the label included the composition reads 89.9 : 10 : 0.1 mol%. Drop the label and renormalize, and it is 89.99 : 10.01 — the SUV preparation's 90:10, to two decimal places. The two recipes in the source material are the same base bilayer with the dye switched on or off, so they are documented here as one Module rather than two.

An earlier revision of this page claimed the labeled 9:1 formulation was "used for both the GUVs and SUVs." That was wrong in detail — the SUV preparation carries no Liss-Rhod PE — but right in substance: the base bilayer is shared.
:::

# Expected Behavior

The Chicago Membrane forms both liposome populations in the Chicago demo. The synthetic cells encapsulate the b.next cell-free cytosol plus the sensing DNA; separate CPRG-loaded SUVs carry the chromogenic substrate. On detection, the expressed PLA1 initiates a liposome-lysis cascade that releases CPRG to LacZ, producing a visible color change. See [Chicago Chassis](../chicago-chassis/spec.md) for the chassis-level description and [SUV Encapsulation](../../processes/encapsulate-suv/main.md) for the substrate liposomes.

# Protocols

The synthetic-cell preparation uses the shared inverted-emulsion (lipid-in-oil) phase-transfer method in [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md). The SUV preparation uses a different method entirely — lipid-film hydration and extrusion, documented in [SUV Encapsulation](../../processes/encapsulate-suv/main.md).

# Credits

Developed by the Chicago node (Kamat Lab and Liu Lab, Northwestern).

:::{attention} Attribution needs confirmation
`Demo Status - Chicago.docx` leaves the contributor field blank for the module sections covering this membrane, so no individual attribution can be sourced for the recipe itself. The results that use it are credited on their own pages. Confirm with the Chicago team.
:::
