---
title: "Chicago Chassis"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
---

# Overview

The Chicago Chassis combines [Base Cytosol](../base-cytosol/spec.md) with the [Chicago Membrane](../membrane-popc-chol-chicago/spec.md), a 9:1 POPC:cholesterol formulation, encapsulated by the same mineral-oil phase-transfer method used for the general-purpose Base Cell. This chassis is not the general-purpose Base Cell: it uses a different membrane Module than the default [Base Membrane](../membrane-popc-chol/spec.md) (9:1 POPC:cholesterol here vs. 70:30 for Base Cell) — the encapsulation method itself is the same. On its own the chassis is an empty encapsulation shell — downstream demo variants add sensing and reporter DNA to this cytosol before encapsulation (for example the theophylline-riboswitch-driven PLA1 construct used in the current demo).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

## Schematic

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    Cytosol["Base Cytosol\n(aqueous droplet)"] -->|"Coated with lipid monolayer\nin mineral oil"| Droplet["Lipid-Coated Droplet\n(9:1 POPC:Chol monolayer)"]
    Lipid["9:1 POPC:Cholesterol\nin mineral oil"] -.-> Droplet
    Droplet -->|"Phase transfer across\noil/water interface"| GUV["Chicago Chassis\n(GUV, bilayer-encapsulated Base Cytosol)"]
    Outer(("Outer aqueous\nbuffer")) -.-> GUV

    style Cytosol fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Lipid fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Droplet fill:#6B7280,color:#ffffff,stroke:#4B5563
    style GUV fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Outer fill:none,stroke:#4B5563
```

This diagram shows the inverted-emulsion (lipid-in-oil) mechanism used to form the chassis: an aqueous droplet of Base Cytosol picks up a lipid monolayer from the surrounding 9:1 POPC:cholesterol lipid-in-oil mixture, then transfers across the oil/outer-aqueous interface, acquiring a second leaflet to complete the bilayer and yield the GUV. No published schematic exists for this mechanism; the diagram below is a simplified summary, not a reproduction of a lab figure.

## Reference Composition

The table below is a one-level-deep aggregate: it states what each constituent contributes to the GUV-formation recipe, without re-expanding either constituent's own internal composition (see each linked spec for that detail — notably, Base Cytosol's own PMix/SMix breakdown runs to ~100 individual PURE-system components and stays on its own page).

:::{table} Chicago Chassis composition — aggregated from constituent Modules
:label: comp-chicago-chassis

| Constituent | Contributes | Working concentration / fraction in this recipe |
| --- | --- | --- |
| [Base Cytosol](../base-cytosol/spec.md) | Inner (aqueous) solution — the cell-free PURE-system reaction mix | 1x reaction concentration. Demo variants add DNA encoding the sensing/reporter circuit for that variant (out of scope for this page — see the corresponding sensing-module spec) |
| [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md) | Bilayer membrane — 9:1 POPC:cholesterol | 0.5 mM lipid-in-oil, prepared at a 3 mL lipid-in-oil scale (see that page for the full stock-concentration/per-lipid-volume breakdown) |

:::

:::{attention} Gap: cytosol-to-membrane ratio not documented
The volume ratio at which the Base Cytosol inner solution is actually combined with the 9:1 POPC:cholesterol lipid-in-oil during the inverted-emulsion GUV-formation step (e.g. µL of inner solution per mL of lipid-in-oil, or the resulting final GUV composition/size) is not documented in the available sourcing (`chicago.md`, from `Demo Status - Chicago.docx`). That source documents each constituent's own recipe (Base Cytosol's reaction-mix volumes; the membrane's 3 mL lipid-in-oil prep) but not the combination step itself. Do not invent a ratio — this ratio is not documented in available source material (see Process below).
:::

## Process

The chassis is formed by encapsulating Base Cytosol in the 9:1 POPC:cholesterol membrane, following the same mineral-oil phase-transfer method documented in [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md). See [GUV Encapsulation: Lipid Variants](../../processes/encapsulate-guv/main.md) for the Chicago-specific lipid composition and the Optiprep/BSA yield-vs-expression tradeoff; that page defers to Encapsulation: Phase Transfer for the shared method steps rather than restating them.

# Constituent Modules

- [Base Cytosol](../base-cytosol/spec.md)
- [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md)

# Credits

- b.next
