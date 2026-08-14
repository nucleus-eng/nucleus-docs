---
title: "Chicago Membrane: POPC/Chol"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Chicago Membrane specifies a phospholipid bilayer composed of POPC, cholesterol, and fluorescent Lissamine Rhodamine PE (Liss-Rhod PE), at a 9:1 POPC:cholesterol ratio. This is a distinct Module from the default [Base Membrane](../membrane-popc-chol/spec.md) (70:29.95, about 3:1) — the two are separate concrete formulations of the same underlying POPC/cholesterol lipid system, not competing values for the same Module. The Chicago Membrane is used for both the giant unilamellar vesicles (GUVs) and small unilamellar vesicles (SUVs) in the [Chicago Chassis](../chicago-chassis/spec.md) and the wider Chicago biosensing demo.

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
pie showData
    title Chicago Membrane lipid composition (mol %)
    "POPC" : 89.9
    "Cholesterol" : 10
    "Liss-Rhod PE" : 0.1
```

No published schematic exists for this mechanism; the pie chart above shows the lipid composition as a simplified summary, not a structural bilayer diagram. **A real schematic (structural, like the [Base Membrane](../membrane-popc-chol/spec.md) liposome figure, or a photo/micrograph of the GUVs/SUVs) is still needed from the dev team.**

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

## Reference Composition

:::{table}
:label: comp-membrane-chicago

| Component    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL, per 3 mL lipid-in-oil) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------------------------------ |
| POPC         | 89.9                  | 760.076                  | 25                           | 41                                          |
| Cholesterol  | 10                    | 386.66                   | 50                           | 1.16                                        |
| Liss-Rhod PE | 0.1                   | 1301.72                  | 1                            | 1.952                                       |

:::

This composition is sourced from the Chicago Module Integration Status writeup (`chicago.md`, from `Demo Status - Chicago.docx`). The volume column is scaled for a 3 mL lipid-in-oil prep, the inverted-emulsion format used to form GUVs for this demo — a different scale and format than the SUV/liposome-scale phase-transfer prep used for [Base Membrane](../membrane-popc-chol/spec.md). The DevCells module-integration diagram marks the "9:1 POPC:cholesterol" ratio as confirmed for both the GUVs and SUVs used throughout the demonstrated Chicago theophylline system.

## Expected Behavior

The Chicago Membrane forms the GUVs and SUVs used in the Chicago biosensing demo: GUVs encapsulate the b.next cell-free cytosol and DNA encoding a theophylline-responsive riboswitch controlling PLA1 expression, while separate SUVs are hydrated with CPRG substrate. Upon detection of theophylline, PLA1 expression initiates a vesicle-lysis cascade that produces a visible colorimetric change, read out via LacZ/CPRG. See the [Chicago Chassis](../chicago-chassis/spec.md) for the full chassis-level description and the [Theophylline Detector](../detector-theophylline/spec.md) for the sensing module.

## Protocols

No GUV-specific encapsulation process is yet documented in `docs/processes/`. The Chicago Module Integration Status writeup describes an inverted-emulsion (lipid-in-oil) prep for this ratio, but it has not yet been written up as a Nucleus process page. Do not assume [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) applies as written, since that page documents Base Cell's SUV/liposome-scale prep rather than GUV formation.

# Credits

- b.next
