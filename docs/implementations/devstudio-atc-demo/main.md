---
title: "aTc Demo"
subtitle: Implementation
status: draft
site:
    hide-toc: true
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

The aTc Demo turns anhydrotetracycline into a visible color change. [SensorCell[aTc ⟶ PLA1]](../../modules/atc-sensing-cell/spec.md) synthetic cells carry TetR holding a `TetO-PLA1` construct off. aTc relieves the repression, the cells express phospholipase A1 (PLA1), and PLA1 breaks the membranes around it. [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) is encapsulated with the sensing circuit, so lysis releases it to meet the [Substrate: CPRG](../../modules/substrate-cprg/spec.md) dosed into the gel, turning it from yellow to purple.

What the photodevelopment step builds is [aTc Cascade](../../modules/atc-cascade/spec.md).

**The color change is confirmed in synthetic cells and has not been run in a gel.**

# Modules

| Role | Module | In the demo |
| --- | --- | --- |
| Cascade | [aTc Cascade](../../modules/atc-cascade/spec.md) | what the photodevelopment step builds |
| Sensing cell | [SensorCell[aTc ⟶ PLA1]](../../modules/atc-sensing-cell/spec.md) | set in the gel |
| Detector | [Detector: tetR-aTc](../../modules/detector-tetr-atc/spec.md) | TetR, holding `TetO-PLA1` off until aTc arrives |
| Lysis | [Lysis: PLA1](../../modules/effector-pla1/spec.md) | expressed from `TetO-PLA1` |
| Cytosol | [Base Cytosol](../../modules/base-cytosol/spec.md) | inside the synthetic cells |
| Membrane | [Membrane: POPC/Chol (9:1)](../../modules/membrane-popc-chol-9-1/spec.md) | around the synthetic cells |
| Reporter | [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) | encapsulated with the circuit, at 2.5 U/mL |
| Substrate | [Substrate: CPRG](../../modules/substrate-cprg/spec.md) | dosed into the set gel |
| Gel | [Gel: PEG-Norbornene](../../modules/gel-peg-norbornene/spec.md) | patterned by light |
| Analyte | [Analyte: aTc](../../modules/analyte-atc/spec.md) | dosed at 0, 1, 5 and 10 µM |

This is the one demo where the enzyme is inside the cell and the substrate outside it. That arrangement is what makes [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) applicable here and nowhere else.

# Processes

| Step | Process | In the demo |
| --- | --- | --- |
| 1 | [Assemble Outer Solution](../../processes/assemble-outer-solution/main.md) | the Tris-HEPES stock with an energy solution |
| 2 | [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md) | the detector, PLA1 template and LacZ Enzyme into Base Cytosol |
| 3 | [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) | the synthetic cells |
| 4 | [Embedding: Photodevelopment](../../processes/embed-photodevelopment/main.md) | PEG-norbornene patterned at 405 nm |
| 5 | [Colorimetric Readout](../../processes/colorimetric-readout/main.md) | absorbance, read against the undosed wells |
| — | [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) | proposed to cut background; never run |

# Observed Performance

## In synthetic cells

The full chain — sensing, lysis, then the LacZ readout — runs in one compartment and gives an aTc-dependent color change. **The response is not graded.** Fold change in absorbance at 5 h (n = 3) separates dosed from undosed at roughly 1.15× to 1.33×, across three DNA and TetR combinations dosed at 0, 1, 5 and 10 µM. It is non-monotonic in two of the three combinations, and the error bars across the 1, 5 and 10 µM points overlap in all three.

So the demo reports presence, not amount.

:::{attention} What this does not show
- **The gel.** Every result above is in synthetic cells in solution. The cascade has not been run in a gel, which is what the demo is for.
- **The 0 µM point is a normalization baseline, not a negative control.** [Detector: tetR-aTc](../../modules/detector-tetr-atc/spec.md#teto-pla1-encapsulated-with-lacz) says why.
- **Patterning bleaches the substrate.** PEG-norbornene supports the synthetic cells, but the 405 nm exposure bleaches CPRG that is already in the gel, which is why CPRG is dosed after the gel is set rather than mixed in.
:::

## In a gel

:::{attention} Not yet run
@Editor(chicago): record the gel run when it happens: the patterned geometry, the CPRG dose, and whether the color is visible to the eye at that scale.
:::

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
