---
title: "London DevCell: AHL Colorimetric Reporter"
subtitle: Implementation
status: draft
site:
    hide-toc: true
---

# Overview

:::{attention} 🚧 Draft — stub
This page is a placeholder for the London demo device. It records what the demo is composed of and what is confirmed as of 2026-08-19; the integrated result does not exist yet and will be written up during DevStudio (23 Sep – 13 Oct 2026).
:::

The London DevCell detects a bacterial quorum-sensing signal and reports it as a visible color change from inside a hydrogel. Synthetic cells built on [S30 Lysate](../../modules/s30-lysate/spec.md) carry a LuxR/pLux circuit; AHL diffusing in from an external bacterial source drives expression of phospholipase A1 (PLA1), which lyses the cell and its neighboring [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md), releasing CPRG to LacZ and turning the gel purple.

The distinguishing feature against the Chicago device is the analyte source: the input is a **living bacterial culture**, not a dosed small molecule. That makes this a bacteria-detection device rather than a chemical sensor.

## What the demo is, as of 2026-08-19

**Polymersomes are out.** London is not pursuing diblock-copolymer polymersomes. The device is lipid-based throughout. This invalidates [`london-quorum-sensing-polymersome`](https://devnotes.nucleus.engineering/articles/019b13f8-9a25-7553-a88d-fa4f19790d13) as a source document, which leaves the [AHL Detector](../../modules/detector-3oc6-hsl/spec.md) with no backing document at all.

**Two readouts, at different maturity.** GFP output in ULGA hydrogel is confirmed with Z-stack imaging. The PLA1-driven color change is confirmed in bulk over repeated runs, but the two have not been combined into one device.

**The readout is leaky.** Discernible but incomplete separation between +AHL and −AHL, with DNA and AHL concentrations still being optimized. Exterior LacZ leakage is a known contributor, and its mitigation ([Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md)) has never been run.

# Modules

| Role | Module | State |
| --- | --- | --- |
| Cytosol | [S30 Lysate](../../modules/s30-lysate/spec.md) | ★ |
| Membrane | [London Membrane: POPC](../../modules/membrane-popc/spec.md) | ★ |
| Chassis | [London Chassis](../../modules/london-chassis/spec.md) | ★ |
| Sensing | [AHL Detector](../../modules/detector-3oc6-hsl/spec.md) → [AHL Sensing Cell](../../modules/ahl-sensing-cell/spec.md) | characterized in lysate; leaky |
| Lysis | [PLA1 Lysis Module](../../modules/effector-pla1/spec.md) | ★ |
| Substrate | [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md) | ★ |
| Readout | [LacZ Reporter](../../modules/reporter-lacz/spec.md) · [XylE / C23DO](../../modules/reporter-xyle/spec.md) | LacZ used; XylE proposed |
| Cascade | [London Cascade](../../modules/london-cascade/spec.md) | integration paths confirmed separately |

:::{note} This device uses a different AHL sensor from the published Nucleus one
The distribution's existing AHL work is the [IV-HSL Emitter](../../modules/emitter-ivhsl/spec.md): BjaI makes a branched AHL and a co-cultured *E. coli* strain carrying `bjaR-GFP-native` does the sensing. This device instead senses 3OC6-HSL with LuxR/pLux, inside a synthetic cell. Different analyte, different receptor, different host for the sensing step. Both are AHL sensors; they are not interchangeable.
:::

# Processes

| Step | Process |
| --- | --- |
| Form synthetic cells | [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) |
| Form substrate liposomes | [SUV Encapsulation](../../processes/encapsulate-suv/main.md) |
| Embed | [ULGA Hydrogel Embedding](../../processes/embed-ulga-hydrogel/main.md) |
| Read out | [Colorimetric Readout](../../processes/colorimetric-readout/main.md) |
| Reduce background | [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) — proposed, never run |

# Performance

No integrated performance data exists. Confirmed results sit at the level of individual integration paths, on the Module pages above.

:::{attention} Open integration steps
1. **GFP and color-change integration paths have not been combined.** Each works; the device needs both in one construct.
2. **Encapsulated expression is not fully controlled.** The Optiprep-free result that restores expression has no minus-inducer or no-DNA controls and no biological replicates.
3. **A synthetic cell + SUV + AHL result has not been reproduced.** Negative controls in that test turned purple, attributed to leaky old-stock liposomes. Reproducing it is an open action item.
4. **Source-document arithmetic is unresolved.** The AHL reaction table in `Demo Status - London.docx` does not reconcile — the AHL row is off by 50× — and the plasmid dose appears as both 37 and 80 ng/µL.
:::

# Credits

Developed by the London Node — Elani Lab. Contributors named in the source material: Ion Ioannou, Jonah McDonald, Charlie Newell, Manuel. Individual results are credited on their own Module pages.

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
