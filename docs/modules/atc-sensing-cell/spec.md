---
title: "aTc Sensing Cell"
subtitle: "Module Specification"
status: draft
thumbnail: mechanism-schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The aTc Sensing Cell combines the [Chicago Chassis](../chicago-chassis/spec.md) with a `TetO-PLA1` / LacZ-CPRG sensing-and-readout circuit, giving a synthetic cell that reports anhydrotetracycline (aTc) dose as a colorimetric (absorbance) signal. It encapsulates the constituent modules below into a single GUV: the [aTc Sensing Module](../detector-tetr_atc/spec.md) supplies the `TetO-PLA1` sensing construct, the [PLA1 Lysis Module](../effector-pla1/spec.md) supplies the lysis trigger that couples sensing to readout, and the [LacZ Reporter Module](../reporter-lacz/spec.md) supplies the enzyme and CPRG substrate chemistry that produce the visible color change.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Interim source
The dose-response result on this page is sourced from the Chicago Module Integration Status notes and the August DevCell Status Update meeting (2026-08-14). See the [aTc Sensing Module](../detector-tetr_atc/spec.md#chicago-cascade-encapsulation-teto-pla1-lacz-cprg-readout) spec's "Chicago Cascade Encapsulation" section for the same result at the module level.
:::

:::{figure} mechanism-schematic.png
:name: fig-atc-sensing-cell-schematic
:align: center
:width: 75%

Mechanism of the aTc Sensing Cell. Inside the GUV, the `TetO-PLA1` construct is transcribed and translated to produce PLA1; co-encapsulated LacZ is also expressed. Membrane-permeable aTc (ATC) enters the GUV and (via TetR, not shown) de-represses `TetO-PLA1` expression. CPRG substrate is co-loaded in the same reaction. Figure by Mary Kelly, Kamat Lab, from the 2026-08-14 DevCell Studio status meeting slide "aTc sensor working in b.next cytosol: Encapsulating TetO-PLA1 with LacZ"; cropped from the original slide (data panels omitted).
:::

## Reference Composition

:::::{tab-set}

::::{tab-item} Cytosol

The inner solution follows the [Chicago Chassis](../chicago-chassis/spec.md) cytosol at reaction concentration, with the `TetO-PLA1` construct from the [aTc Sensing Module](../detector-tetr_atc/spec.md) and LacZ from the [LacZ Reporter Module](../reporter-lacz/spec.md) added as the sensing and reporter DNA, and CPRG substrate ([LacZ Reporter Module](../reporter-lacz/spec.md#substrate)) co-loaded for the colorimetric handoff. The table below flattens the combined GUV reaction one level deep, to the four constituent modules — see each module's own spec for its full internal composition (not repeated here).

:::{table} Combined GUV reaction, one level deep (Chicago node, 2026-08-14)
| Constituent | Working concentration in combined GUV reaction | Notes |
| --- | --- | --- |
| [Chicago Chassis](../chicago-chassis/spec.md) | Base Cytosol at reaction concentration, in a 9:1 POPC:cholesterol GUV membrane | Supplies the reaction mix and encapsulation shell; see that page for its own reference composition — not re-expanded here. |
| [aTc Sensing Module](../detector-tetr_atc/spec.md) (`TetO-PLA1` DNA + TetR) | Three DNA/TetR combinations tested: 1 nM DNA + 50 nM TetR (headline condition); 0.5 nM DNA + 50 nM TetR; 1 nM DNA + 100 nM TetR | aTc analyte dosed at 0/1/5/10 µM against each combination — see [Expected Behavior](#expected-behavior) below. All three combinations are documented as tested; none is singled out as canonical. |
| [PLA1 Lysis Module](../effector-pla1/spec.md) | No independent concentration — PLA1 is expressed from the `TetO-PLA1` construct already counted in the aTc Sensing Module row above, not added as a separate reagent | No dedicated PLA1 devnote exists yet; see that page's documentation-gap notice. |
| [LacZ Reporter Module](../reporter-lacz/spec.md) | LacZ: 20 U/mL; CPRG substrate: 0.5 mM | LacZ and CPRG are both encapsulated in the same GUV per the source slide. |
:::

Source: DevCell Studio status meeting slide "aTc sensor working in b.next cytosol: Encapsulating TetO-PLA1 with LacZ" (Mary Kelly, Kamat Lab, 2026-08-14), cross-checked against the [aTc Sensing Module](../detector-tetr_atc/spec.md#chicago-cascade-encapsulation-teto-pla1-lacz-cprg-readout) spec's "Chicago Cascade Encapsulation" section.

::::

::::{tab-item} Membrane

The membrane follows the [Chicago Chassis](../chicago-chassis/spec.md) reference composition (9:1 POPC:cholesterol, GUV scale) — see that page for the full membrane spec.

::::

:::::

## Expected Behavior

This configuration shows a confirmed graded dose-response to aTc at the solution/GUV level: absorbance at 575 nm increased with aTc dose (0/1/5/10 µM) over a 5 h read, across three DNA/TetR combinations — 1 nM DNA with 50 nM TetR, 0.5 nM DNA with 50 nM TetR, and 1 nM DNA with 100 nM TetR — each compared against −TetR and −DNA controls. Full detail on this dose-response result, including the concentration grid and readout chemistry, is documented in the [aTc Sensing Module](../detector-tetr_atc/spec.md) spec's "Chicago Cascade Encapsulation (TetO-PLA1 / LacZ-CPRG Readout)" section and is not duplicated here.

:::{warning}
**Gel integration not yet complete.** This result is confirmed at the solution/GUV level only. Hydrogel integration was reported as "just... in the process of putting this into our gel" and had not been completed. Do not treat the aTc Sensing Cell as validated for hydrogel-embedded (Chicago Cascade) use yet — the edge from this cell into the Chicago Cascade should be kept dashed/in-progress until a gel-integrated result is confirmed.
:::

## Requirements

The aTc Sensing Cell shares its LacZ/CPRG readout with the Theophylline Sensing Cell. Theophylline is understood to inhibit the LacZ/CPRG colorimetric reaction — see the [aTc Sensing Module](../detector-tetr_atc/spec.md#requirements) and [LacZ Reporter Module](../reporter-lacz/spec.md#requirements) Requirements sections for the confirmed mutual-exclusion decision on the current Chicago Cascade design. This page does not repeat that constraint's rationale.

# Constituent Modules

- [Chicago Chassis](../chicago-chassis/spec.md) — chassis (cytosol + 9:1 POPC:cholesterol GUV membrane)
- [aTc Sensing Module](../detector-tetr_atc/spec.md) — `TetO-PLA1` sensing construct, gated by aTc/TetR
- [PLA1 Lysis Module](../effector-pla1/spec.md) — lysis trigger coupling sensing to readout
- [LacZ Reporter Module](../reporter-lacz/spec.md) — LacZ/CPRG colorimetric readout chemistry

# Credits

- Mary Kelly, Kamat Lab (Chicago node) — TetO-PLA1/LacZ-CPRG encapsulation result, from the 2026-08-14 DevCell Studio status meeting.
