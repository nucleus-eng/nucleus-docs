---
title: "Protocol: Inverted Emulsion"
subtitle: "Encapsulation: Phase Transfer"
status: draft
---

# Overview

This is a second protocol for [Encapsulation: Phase Transfer](./main.md), not a second way of closing a bilayer. It performs the same operation the parent page describes — emulsify an inner solution into a lipid-in-oil dispersion, then drive the droplets through an oil–water interface into an outer solution — and it does so at different settings, for giant unilamellar vesicles (GUVs).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. The steps below are one recorded preparation and have not been run against these docs. No yield, size distribution or lamellarity is recorded for them here.
:::

**The settings are not interchangeable with the parent protocol's.** The spin is the clearest case: 2500 g for 15 min at 15 °C here, against 9000 g for 10 min at room temperature there. Running one protocol's steps at the other's figures is a third thing, untested.

:::{table} What differs from the protocol on the parent page. Everything not listed is shared.
:name: assemble-base-cell-guv-differences

| | [Phase Transfer](./main.md) | This protocol |
| --- | --- | --- |
| Mineral oil | 1 mL | 3 mL |
| Total lipid | stated as a composition, not a molarity | 1.5 µmol, which is 0.5 mM in 3 mL |
| Chloroform removal | 55 °C dry bath, uncovered, 4 h | gentle argon flow, then a vacuum desiccator for 30 min |
| Dispersing the lipids | vortex 5 s | sonicate 20 min, 60 °C for 1 h, vortex 2 min, sonicate 20 min |
| Interface | the emulsion is layered onto 300 µL of outer solution | 300 µL of lipid-in-oil is layered over 400 µL of outer solution and left to stand 10 min to 20 min |
| Lipid-in-oil per emulsion | 150 µL onto at least 30 µL of inner solution | 600 µL |
| Emulsifying | drag the tube across an empty rack at least 50 times | pipette up and down for 3 min |
| Spin | 9000 g, 10 min, room temperature | 2500 g, 15 min, 15 °C |
| Collection | 50 µL to 100 µL into a 1.5 mL tube | the whole volume into a 0.2 mL PCR tube |

:::

**The interface is made before the emulsion, and it rests.** On the parent page the emulsion is layered onto outer solution immediately. Here the lipid-in-oil goes over the outer solution first and stands for 10 min to 20 min while the inner solution is prepared, so a lipid monolayer has time to form at the interface before any droplet reaches it.

# Materials and Equipment

The [parent page's materials](./main.md#bom-assemble-base-cell) cover the lipids, the mineral oil, the chloroform and the glassware for handling them. This protocol also needs:

- A 20 mL glass vial. The parent protocol's 4 mL vials do not hold 3 mL of oil with headroom to vortex.
- A bath sonicator.
- A vacuum desiccator.
- Argon, with a regulator and a line fine enough to play gently over a solvent surface.
- A 60 °C incubator or dry bath.
- 0.2 mL PCR tubes.

# Protocol

:::{warning} Warning
:class: simple
:icon: false
Work inside of a fume hood when handling chloroform.
:::

## Prepare the Lipid-in-Oil Dispersion

- [ ] Combine the three lipid stocks in a 20 mL glass vial. All three are in chloroform.
    - [ ] 41.0 µL of POPC at 25 mg/mL.
    - [ ] 1.16 µL of cholesterol at 50 mg/mL.
    - [ ] 1.95 µL of Liss-Rhod PE at 1 mg/mL.
- [ ] Remove the chloroform under a gentle argon flow.
- [ ] Dry the vial in a vacuum desiccator for 30 min.
- [ ] Rehydrate the lipids in 3 mL of mineral oil, giving 0.5 mM total lipid in oil.
- [ ] Seal the vial, then disperse the lipids in four steps:
    - [ ] Bath sonicate for 20 min.
    - [ ] Incubate at 60 °C for 1 h.
    - [ ] Vortex for 2 min.
    - [ ] Bath sonicate for 20 min.

:::{hint} Note
:class: simple
:icon: false
Those three volumes give 89.9 / 10 / 0.1 mol% POPC, cholesterol and Liss-Rhod PE, and 1.5 µmol of lipid in total. The same membrane is also recorded at a 5 mL scale, which is 2.5 µmol at the same mol% and the same 0.5 mM.
:::

## Form the Interface

- [ ] Layer 300 µL of the lipid-in-oil dispersion gently over 400 µL of outer solution in a 1.5 mL tube.
- [ ] Leave the tube at room temperature for 10 min to 20 min.

:::{hint} Note
:class: simple
:icon: false
The outer solution is matched to the inner solution by osmolality, not by recipe — see [Assemble Outer Solutions](./main.md#assemble-outer-solutions) on the parent page, and measure both by [Osmometry Readout](../osmometry-readout/main.md).
:::

## Form the Emulsion

- [ ] Prepare the inner solution in a separate 1.5 mL tube while the interface stands.
- [ ] Add 600 µL of the lipid-in-oil dispersion to the inner solution.
- [ ] Pipette up and down for 3 min, until the mixture is a water-in-oil emulsion.

## Transfer

- [ ] Add the emulsion on top of the interface formed above.
- [ ] Centrifuge at 2500 g for 15 min at 15 °C.
- [ ] Remove the oil phase carefully with a pipette.
- [ ] Collect the vesicles into a 0.2 mL PCR tube with a fresh pipette tip.
- [ ] Resuspend the vesicles gently.

:::{hint} The sample is not washed
:class: simple
:icon: false
The vesicles come with the outer solution around them, and that solution carries any inner solution that was not encapsulated. An enzyme in it works outside the vesicles. Where a readout must tell inside from outside, wash the sample first by [Wash Vesicles](../wash-vesicles/main.md), which is optional.
:::
