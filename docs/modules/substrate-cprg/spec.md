---
title: "Substrate: CPRG"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

CPRG is chlorophenol red-β-D-galactopyranoside, the chromogenic substrate half of the [LacZ Reporter](../reporter-lacz/spec.md) pair. It is yellow; [LacZ](../reporter-lacz-enzyme/spec.md) cleaves it to chlorophenol red, which is magenta.

**This page is about the substrate, not about a container for it.** Holding CPRG inside a liposome keeps it away from the enzyme until a lysis event releases it, but the liposome format is the business of the process that encapsulates it: the London Node uses GUVs made by phase transfer, and the Chicago Node uses SUVs made by film hydration and extrusion. Both hold the same substrate. See [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md) for the SUV format specifically.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} CPRG loading by format.
| Format | Loading concentration | Notes |
| --- | --- | --- |
| SUV, film hydration and extrusion | 50 mM | Chicago Node. 400 nm target size |
| GUV, phase transfer | Not documented | London Node, since the move away from SUVs |
| Free in the gel | Not documented | Photodevelopment routes, where UV would bleach encapsulated CPRG |
:::

:::{attention} The Chicago loading figures have no primary data behind them
@Editor(chicago): the 400 nm target size and the 50 mM loading concentration are stated in the Chicago integration status but have no DevNote behind them. No DLS traces or absorbance QC data has been located.
:::

# Requirements

Requires [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) to produce a signal — CPRG alone is inert and yellow.

**CPRG is UV-sensitive**, so any photodeveloped format adds it after crosslinking rather than embedding it with everything else. That reordering makes it a free dye rather than an encapsulated one, which changes what the reporter is composed of.

# Processes

- [SUV Encapsulation](../../processes/encapsulate-suv/main.md) — the Chicago format: film hydration and extrusion, then purification away from unencapsulated CPRG.
- [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) — the London format, since the move to GUVs.
- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the conversion this substrate undergoes.

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
