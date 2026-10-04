---
title: "pH Demo"
subtitle: Implementation
status: draft
site:
    hide-toc: true
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

The pH Demo turns acidic pH into a color change in a gel. [SensorCell[pH ⟶ PLA1]](../../modules/ph-sensing-cell/spec.md) synthetic cells and CPRG-loaded large unilamellar vesicles (LUVs) are set together in low-gelling agarose. At pH 6.0 to 6.5 the synthetic cells express phospholipase A1 (PLA1), which breaks the LUVs' membranes and releases CPRG into the gel. A basic buffer carrying [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) then goes into the gel, and LacZ turns the released CPRG from yellow to purple.

LacZ is added only after the sensing step, because it works poorly at the acidic pH the sensor needs. What the gel embedding builds is [pH Cascade](../../modules/ph-cascade/spec.md).

This page specifies the demo as it is intended. The demo has not run.

# Modules

| Role | Module | In the demo |
| --- | --- | --- |
| Cascade | [pH Cascade](../../modules/ph-cascade/spec.md) | what the gel embedding builds |
| Sensing cell | [SensorCell[pH ⟶ PLA1]](../../modules/ph-sensing-cell/spec.md) | set in the gel |
| Detector | [Detector: pH-Sensing](../../modules/detector-ph/spec.md) | the pH-responsive and trigger strands, annealed 3:1 |
| Lysis | [Lysis: PLA1](../../modules/effector-pla1/spec.md) | expressed from the `pT7-toehold9-PLA1` template |
| Cytosol | [Base Cytosol](../../modules/base-cytosol/spec.md) | inside the synthetic cells |
| Membrane | [Membrane: POPC/Chol (9:1)](../../modules/membrane-popc-chol-9-1/spec.md) | with 0.1 mol% Liss Rhod PE, on both the synthetic cells and the LUVs |
| Substrate | [Substrate: CPRG](../../modules/substrate-cprg/spec.md) | 14.25 mg/mL inside the LUVs |
| Gel | [Gel: LGA](../../modules/gel-lga/spec.md) | 0.7% (w/v) in the set gel |
| Reporter | [Reporter: LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) | in the basic buffer, added after the sensing step |

The CPRG-loaded LUV has no Module page.

# Processes

| Step | Process | In the demo |
| --- | --- | --- |
| 1 | [Anneal pH-Responsive Trigger Duplex](../../processes/anneal-ph-trigger-duplex/main.md) | pH-responsive strand to trigger, 3:1 |
| 2 | [Assemble Cytosol](../../processes/assemble-cytosol/assemble-cytosol-main.md) | the trigger duplex and the PLA1 template, into Base Cytosol |
| 3 | [Encapsulation: Freeze-Thaw](../../processes/encapsulate-luv/main.md) | the CPRG-loaded LUVs |
| 4 | [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) | the synthetic cells |
| 5 | [Embedding: Thermal Setting](../../processes/embed-thermal-setting/main.md) | synthetic cells and LUVs set in LGA, then incubated at 37 °C |
| 6 | [Color Development](../../processes/color-development/main.md) | the basic buffer carrying LacZ Enzyme goes into the gel |
| 7 | [Colorimetric Readout](../../processes/colorimetric-readout/main.md) | the color is read |

:::{attention} What the demo does not yet specify
- **How the gel is brought to acidic pH.** No step adds the acid. @Editor: record how, and at what pH.
- **The amounts.** @Editor: record the synthetic cells and LUVs per volume of gel, and the LacZ Enzyme in the basic buffer.
- **The color development conditions in the gel.** @Editor: confirm them. The one test on record ran in solution: pH 9.9 buffer, 37 °C, 3 h.
- **The readout.** @Editor: record whether the color is read by eye, by plate reader or by imaging.
:::

# Performance

:::{attention} Not yet run
@Editor: record the run here when it happens: its date, its conditions and what the readout showed.
:::

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
