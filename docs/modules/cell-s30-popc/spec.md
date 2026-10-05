---
title: "Cell: S30 Lysate, POPC"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
---
# Overview

<!-- gen:position -->
**Position.** Refines [`cell`](../cell/spec.md) and [`guv`](../guv/spec.md). Refined by [`ahsl-sensing-cell`](../ahsl-sensing-cell/spec.md).
<!-- /gen:position -->

The Cell: S30 Lysate, POPC combines [S30 Lysate](../s30-lysate/spec.md) with a [100% POPC membrane](../membrane-popc/spec.md). This cell is extended in downstream demo variants by adding sensing and reporter modules (e.g., the [3OC6-HSL Sensing Module](../detector-3oc6-hsl/spec.md), giving the [SensorCell[3OC6-HSL ⟶ PLA1]](../ahsl-sensing-cell/spec.md)).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    S30_LYSATE["Cytosol: S30 Lysate"]
    MEMBRANE_POPC["Membrane: POPC"]

    P1_ENCAPSULATE_0(["Encapsulation: Phase Transfer (packing)"])
    CELL_S30_POPC["Cell: S30 Lysate, POPC"]

    S30_LYSATE --> P1_ENCAPSULATE_0
    MEMBRANE_POPC --> P1_ENCAPSULATE_0
    P1_ENCAPSULATE_0 --> CELL_S30_POPC


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class S30_LYSATE,MEMBRANE_POPC leaf;
    class CELL_S30_POPC composed;
    class P1_ENCAPSULATE_0 process;

    click S30_LYSATE "/docs/modules/s30-lysate/spec"
    click MEMBRANE_POPC "/docs/modules/membrane-popc/spec"
    click P1_ENCAPSULATE_0 "/docs/processes/assemble-base-cell/main"
    click CELL_S30_POPC "/docs/modules/cell-s30-popc/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Cytosol

The inner solution encapsulated into the Cell: S30 Lysate, POPC is [S30 Lysate](../s30-lysate/spec.md) at reaction concentration, with sucrose to assist [encapsulation by phase transfer](../../processes/assemble-base-cell/main.md), and RNase inhibitor to improve performance.

:::{table}
:label: comp-london-cytosol

| Component                                                | Final Concentration                                | Volume for one reaction (µL) |
| -------------------------------------------------------- | -------------------------------------------------- | ---------------------------- |
| S30 Lysate (premix + extract + amino acid mix, combined) | 1× (kit components, each at working concentration) | 20.00                        |
| Sucrose                                                  | 276 mM                                             | 3.75                         |
| RNase inhibitor                                          | 1840 U/mL                                          | 1.25                         |
| Nuclease-free water                                      | —                                                  | 2.2                          |
| Total volume (µL)                                        |                                                    | 27.20                        |

:::
::::

::::{tab-item} Membrane

The membrane is the [Membrane: POPC](../membrane-popc/spec.md) (100% POPC), optionally functionalized with red fluorescent Cyanine 5 PC, or DSPE-PEG2000. The two optional lipids come from two separate documented preparations and are not combined in one membrane.

:::{table} Membrane: POPC preparations, as documented on the [Membrane: POPC](../membrane-popc/spec.md) spec.
:label: comp-london-membrane

| Preparation                    | Target composition (mol %)     | POPC (µL) | DSPE-PEG2000 (µL) | 18:1 Cyanine 5 PC (µL) | Total lipid (mg) |
| ------------------------------ | ------------------------------ | --------- | ----------------- | ---------------------- | ---------------- |
| PEGylated membrane             | 99.15 POPC : 0.85 DSPE-PEG2000 | 130.4     | 10.32             | —                      | 3.36             |
| Fluorescently labeled membrane | 99.9 POPC : 0.1 Cyanine 5 PC   | 79.863    | —                 | 3.423                  | 2.00             |

:::

::::

::::{tab-item} Outer Solution

:::{table}
:label: comp-london-outer

| Component                        | Concentration |
| -------------------------------- | ------------- |
| Potassium L-glutamate            | 578 mM        |
| HEPES (pH 7.4)                   | 72 mM         |
| Glucose                          | 300 mM        |

:::

Osmolarity of inner and outer solutions target ~920 mOsm.

::::

:::::

(cell-s30-popc-expected-behavior)=
# Expected Behavior

## Cells

Three phase-transfer routes have been compared for encapsulating S30 Lysate in POPC. The Elani-lab protocol with Optiprep in the inner solution gives the cleanest and highest-yield preparation. The same protocol without Optiprep gives fewer cells, and the Schroeder route (JoVE, 2020) gives yields too low to use.

Yield is counted as cells at or above 5 µm per imaging field. In the Elani route, adding 5 mg/mL BSA and raising Optiprep to 15% raised that count about 1.5×, from roughly 27 to roughly 42. Counts hold through incubation at 37 °C, and in the Optiprep condition cells stay round and abundant for 48 h, averaging 80 per field at 1 h and 66 at 48 h. Membrane stability is therefore not what limits yield.

**Yield and expression pull against each other.** Optiprep above about 5% of the inner solution suppresses cell-free expression, so the conditions that give the most cells give no signal at all — see [SensorCell[3OC6-HSL ⟶ PLA1]](../ahsl-sensing-cell/spec.md) for that result and its controls. The configuration demonstrated to express is the one without Optiprep, at the cost of yield. Expect to choose. The ceiling binds only compartments that have to express. Dye populations carry no transcription or translation machinery and tolerate more. A CPRG dye population has been run at 10%.

:::{attention} Source needed
@Editor(london): cite the source for the 10% Optiprep figure of the CPRG dye population.
:::

:::{attention} Size is a threshold, not a distribution
Cell size is recorded only as the ≥5 µm cutoff used for counting. @Editor(london): a size distribution, a measure of brightness, and reference images are still needed.
:::

# Requirements

Requires a membrane to encapsulate the cytosol (e.g. [Membrane: POPC](../membrane-popc/spec.md)).

# Implementations

- [LuxR-GFP Demo](../../implementations/devstudio-luxr-gfp-demo/main.md): its chassis — the empty chassis this builds on.

# Processes

The chassis is formed by encapsulating [S30 Lysate](../s30-lysate/spec.md) in a [100% POPC membrane](../membrane-popc/spec.md) using  [emulsion phase transfer](../../processes/assemble-base-cell/main.md). Use this cell in outer solution at 920 mOsm, or empirically match your outer and inner solution osmolarities by measuring with a vapor-pressure osmometer. 

- [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) — sets this Cell in a thermally set gel

# Constituent Modules

- [S30 Lysate](../s30-lysate/spec.md)
- [Membrane: POPC](../membrane-popc/spec.md)

# Credits

Developed by Ion Ioannou and Jonah McDonald (London Node, Elani Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
