---
title: "London Chassis"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
---

# Overview

The London Chassis combines [S30 Lysate](../s30-lysate/spec.md) with a 100% POPC membrane, encapsulated by the same mineral-oil phase-transfer method used for the general-purpose Base Cell, to produce the synthetic-cell substrate used in the London AHL-sensing demo. This chassis is not the general-purpose Base Cell: it swaps S30 Lysate (a commercial *E. coli* cell-free system) in for Base Cytosol, and it uses a 100% POPC membrane instead of Base Cell's 70:30 POPC:cholesterol default — the encapsulation method itself is the same. On its own the chassis is an empty encapsulation shell — the London demo adds the AHL Sensing Module's `pLux-GFP` reporter plasmid to the S30 reaction before encapsulation.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

```{mermaid}
flowchart LR
    S30["S30 Lysate<br/>+ `pLux-GFP` plasmid"]
    POPCOIL["POPC in mineral oil<br/>(4 mg/mL working lipid)"]
    DROPLET["Lipid-monolayer droplet<br/>(inner solution in oil)"]
    OUTER["Outer solution<br/>(glutamate / HEPES / glucose)"]
    SYNCELL["POPC-bilayer synthetic cell<br/>encapsulating S30 Lysate"]

    S30 --> DROPLET
    POPCOIL --> DROPLET
    DROPLET -->|mineral-oil phase transfer,<br/>across oil/water interface| SYNCELL
    OUTER --> SYNCELL

    classDef node fill:#efefef,stroke:#666666,color:#222222;
    class S30,POPCOIL,DROPLET,OUTER,SYNCELL node;
```

No published schematic exists for this mechanism; the diagram above is a simplified summary, not a reproduction of a lab figure.

## Reference Composition

:::::{tab-set}

::::{tab-item} Cytosol

The inner solution encapsulated into the London Chassis is [S30 Lysate](../s30-lysate/spec.md) at reaction concentration, combined with the AHL Sensing Module's `pLux-GFP` reporter plasmid, sucrose (for osmotic matching to the outer solution), and RNase inhibitor. The table below is the actual synthetic-cell formation recipe (condition 2, +DNA) from the S30/POPC encapsulation experiment.

:::{table}
:label: comp-london-cytosol

| Component | Final Concentration | Volume for one reaction (µL) |
| --------- | -------------------- | ----------------------------- |
| S30 Lysate (premix + extract + amino acid mix, combined) | 1× (kit components, each at working concentration) | 20.00 |
| `pLux-GFP` sensor plasmid              | 37 ng/µL             | 0.95                          |
| Sucrose                                 | 276 mM                | 3.75                           |
| RNase inhibitor                         | 1840 U/mL             | 1.25                           |
| Nuclease-free water                     | —                     | 1.25                           |
| Total volume (µL)                       |                       | 27.20                          |

:::

S30 Lysate's own internal breakdown (premix, extract, amino acid mix) is not re-expanded here — those three kit-supplied components are aggregated into the single line above, at 20 µL of the 27.2 µL total inner-solution volume (~73.5% v/v). See [S30 Lysate](../s30-lysate/spec.md) for that internal breakdown and the source encapsulation experiment. The `pLux-GFP` plasmid itself is out of scope for this page — see the AHL Sensing Module spec for the sensor construct.

::::

::::{tab-item} Membrane

The membrane is the [London Membrane](../membrane-popc/spec.md) base bilayer — 100% POPC, no cholesterol — at a **4 mg/mL working lipid concentration** in mineral oil. That page carries the full composition, the two optional additive variants (a Cyanine 5 PC label and a DSPE-PEG2000 PEGylated form), and the prep scales; they are not re-expanded here.

Unlike [Base Membrane](../membrane-popc-chol/spec.md), this is not a POPC:cholesterol ratio — it is a different lipid system.

::::

::::{tab-item} Outer Solution

:::{table}
:label: comp-london-outer

| Component                          | Concentration |
| ----------------------------------- | ------------- |
| Potassium L-glutamate                | 578 mM        |
| HEPES (pH 7.4)                       | 72 mM         |
| Glucose                              | 300 mM        |
| AHL (3OC6-HSL, + condition only)     | 10 µM         |

:::

Inner and outer osmolarity are matched (~920 mOsm) to keep encapsulated synthetic cells stable; a sucrose inner solution against a denser outer solution makes liposomes sediment and drift, complicating imaging.

::::

:::::

## Process

The chassis is formed by encapsulating S30 Lysate in a 100% POPC membrane, following the same mineral-oil phase-transfer method documented in [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).

Three phase-transfer routes were compared for this chassis: the Elani-lab protocol with Optiprep, the same protocol without Optiprep, and the Schroeder protocol (JoVE, 2020). The Elani protocol with Optiprep gave the cleanest, highest-yield encapsulation, but Optiprep above ~5% of the inner solution suppresses cell-free expression — the 10% and 15% Optiprep conditions tested gave abundant, stable synthetic cells but no reporter signal. Dropping Optiprep restores expression: the AHL sensor expresses GFP on induction, with liposome-associated GFP puncta co-localizing with round liposomes across imaged fields. See [S30 Lysate](../s30-lysate/spec.md) for the full expected-behavior writeup, including outstanding controls.

:::{caution}
**Not yet controlled.** The Optiprep-free expression result has no minus-AHL or no-DNA negative controls yet, and no biological replicates. Treat the GFP signal as promising but unattributed until those controls are run.
:::

# Constituent Modules

- [S30 Lysate](../s30-lysate/spec.md)
- [London Membrane: POPC](../membrane-popc/spec.md)

# Credits

Developed by Ion Ioannou and Jonah McDonald (London node, Elani Lab) — S30 Lysate encapsulation in POPC synthetic cells.

:::{attention} Attribution needs confirmation
Contributor names are taken from the 14 Aug 2026 status deck, where they appear printed on the slides, and from the module sections of the Chicago and London status documents. Mappings from person to result have not been confirmed by the teams themselves.
:::
