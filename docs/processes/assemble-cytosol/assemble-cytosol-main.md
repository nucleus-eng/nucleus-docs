---
title: Assemble Cytosol
status: draft
---

# Overview

Assemble Cytosol combines a cytosol base with whatever a particular reaction needs — a sensing construct, an effector, a reporter enzyme, a density agent — into one compartment. Every derivative is the same act with a different filling, which is why they share a page rather than repeating a protocol each time.

Its derivatives, all attested in this documentation:

- [Assemble Base Cytosol](../assemble-base-cytosol/main.md) — the unit case, where nothing is added and the slot is filled with water.
- **Assemble aTc Sensor Cytosol**, **Assemble pH Sensor Cytosol**, **Assemble AHL Sensor Cytosol**, **Assemble Theophylline Sensor Cytosol** — no pages yet. Each is specified in the `composition.yml` of the Module it produces.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{note} This is one of two instances of a wider process
Assemble Cytosol and **Assemble Outer Solution** are both instances of **Assemble Aqueous Solution** — combining aqueous components into one compartment. That is why both mix, and why neither one chooses its operator. Assemble Aqueous Solution has no page of its own; module composition sources name it in their `abstract:` field.

What distinguishes a cytosol from any other aqueous solution is the headroom below. An outer solution reserves nothing.
:::

# The shared structure

**Every derivative is a base plus a filling, combined into one compartment.** Nothing else varies, and that is what makes the family generable rather than merely similar.

**The result shares one compartment**, so this process mixes. The operator is not a per-derivative choice — it follows from what the process does, and it is inherited by everything under Assemble Aqueous Solution.

## The headroom

A cytosol recipe pins its total volume and reserves part of it. [Assemble Base Cytosol](../assemble-base-cytosol/main.md) states the slot directly:

| **Component** | **Volume per Reaction (µL)** |
| --- | --- |
| User Additives | X |
| Nuclease Free Water | 2.0 - X |
| Total | 10 |

**Water is the unit.** Because the total is pinned, filling the slot with water alone leaves every other component at its reference concentration — so `Assemble Cytosol` with an empty headroom *is* Assemble Base Cytosol. That identity is realizable: you can pipette water, where a zero-volume filling could not even be expressed in a fixed-total recipe.

The protocol already uses the law. The same reaction run with and without a DNA template carries 7 µL and 8.75 µL of water, and the 1.75 µL difference is exactly the template volume, with the total held at 35 µL.

**The slot is finite, and nothing checks it.** `2.0 - X` goes negative above 2.0 µL, so `X ≤ 2.0 µL` is a hard constraint the table imposes by construction. It cannot be evaluated today, because module pages state concentrations while the headroom states a volume — see issue #224.

# What the derivatives do not share

A derivative is identified by the **pair** of base and filling. Neither alone names it: Base Cytosol with CPRG is a different mixture from S30 Lysate with CPRG, and from Base Cytosol with IPTG.

| Derivative | Base | Filling |
| --- | --- | --- |
| [Base Cytosol](../../modules/base-cytosol/spec.md) | Base | water |
| [aTc Sensor Cytosol](../../modules/atc-sensor-cytosol/spec.md) | Base Cytosol | `TetO-PLA1` · TetR · LacZ at 20 U/mL |
| [pH Sensor Cytosol](../../modules/ph-sensor-cytosol/spec.md) | Base Cytosol | trigger duplex · toehold-gated template · Optiprep · Sulfo-Cy5 |
| [Theophylline Sensor Cytosol](../../modules/theophylline-sensing-cell/spec.md) | Base Cytosol | riboswitch construct at 5 nM |
| [AHL Sensor Cytosol](../../modules/ahl-sensor-cytosol/spec.md) | S30 Lysate | `LuxR-PLA1` or `LuxR-deGFP` |

**The base carries the headroom, not this process.** [Base Cytosol](../../modules/base-cytosol/spec.md) reserves 2.0 µL of 10. [S30 Lysate](../../modules/s30-lysate/spec.md) reserves 3.75 µL of 25, implied by its total rather than named, so a composer adding to that base has to derive the capacity.

# Requirements

Requires a base whose recipe pins a total volume and reserves part of it. Without a reserved slot there is nothing to add into, and adding anyway dilutes every other component.

**Two things spend the headroom that are not sensing components**, and both are easy to miss:

- **A downstream process can claim it.** [pH Sensor Cytosol](../../modules/ph-sensor-cytosol/spec.md) carries Optiprep at 4.5% (v/v) — about 0.45 µL of a 10 µL reaction, or a fifth of the slot — because of how the cell is later encapsulated, not because the sensing function needs it. The reagent is spent before the step that needs it runs.
- **A base component may be a range rather than a figure.** Base Cytosol accepts RNase inhibitor anywhere from 0 to 2000 U/mL, so it can be left out entirely. A derivative naming one value inside that range is recording a choice, not a requirement.

# Modules

Every Module produced by a derivative of this process:

- [Base Cytosol](../../modules/base-cytosol/spec.md)
- [aTc Sensor Cytosol](../../modules/atc-sensor-cytosol/spec.md)
- [pH Sensor Cytosol](../../modules/ph-sensor-cytosol/spec.md)
- [AHL Sensor Cytosol](../../modules/ahl-sensor-cytosol/spec.md)
