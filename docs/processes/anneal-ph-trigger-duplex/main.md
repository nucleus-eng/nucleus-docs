---
title: "Anneal pH-Responsive Trigger Duplex"
subtitle: "Process"
status: draft
---

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Overview

This process anneals the pH-responsive ssDNA and the trigger ssDNA into the single duplex reagent used by the [pH-Sensing Module](../../modules/detector-ph/spec.md). The duplex holds the trigger until acidic pH releases it, so the two strands are combined and stored as one reagent rather than added to a reaction separately.

# Protocol

## Prepare the strands

- [ ] Resuspend the pH-responsive ssDNA in Duplex Buffer (Integrated DNA Technologies) to 100 µM.
- [ ] Resuspend the trigger ssDNA in Duplex Buffer to 100 µM.
- [ ] Combine the two stocks at a 3:1 volume ratio of pH-responsive ssDNA to trigger ssDNA. This gives 25 µM trigger ssDNA and 75 µM pH-responsive ssDNA in the mixture.

## Anneal

Run the following in a thermocycler. The melting temperature of the construct is 52 °C.

- [ ] Hold at 95 °C for 5 min.
- [ ] Cool at 2 min per degree to 52 °C.
- [ ] Cool at 30 min per degree from 52 °C to 42 °C.
- [ ] Cool at 2 min per degree to 25 °C.

## Store

- [ ] Store the annealed construct at -20 °C.

:::{attention} Working concentration not recorded
@Editor: the annealed construct is stored at 25 µM trigger ssDNA, and the dilution between that stock and the reaction is not recorded in the source. Confirm the working concentration with the Chicago Node before use.
:::
