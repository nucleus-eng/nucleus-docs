---
title: "Degrade Exterior LacZ"
subtitle: "Process"
status: draft
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

Degrade Exterior LacZ uses proteinase K to break down LacZ reporter enzyme that has leaked outside a liposome, cutting the background color signal that this exterior LacZ would otherwise add to a colorimetric readout. Proteinase K is added to the sample, given time to digest the exterior (non-encapsulated) LacZ, then removed by pelleting the liposomes and resuspending them in fresh solution.

The problem it addresses is real wherever LacZ is meant to stay inside a compartment: enzyme that ends up outside can hydrolyze CPRG, or another chromogenic substrate, in solution and produce color that did not come from the intended lysis-triggered handoff. See the [PLA1 Lysis Module](../../modules/effector-pla1/spec.md) for the lysis step this protects.

:::{attention} This suits one architecture, not every LacZ cascade
Use it where **LacZ is encapsulated and its substrate is outside** — the [aTc Sensing Cell](../../modules/atc-sensing-cell/spec.md) and the [aTc Cascade](../../modules/atc-cascade/spec.md) both carry LacZ at 20 U/mL inside the cell, with CPRG in the outer solution. There, exterior enzyme is a contaminant and digesting it is exactly the point.

Do not use it where LacZ sits in the outer solution or is dispersed through a gel on purpose. The [London Cascade](../../modules/london-cascade/spec.md), the [pH Cascade](../../modules/ph-cascade/spec.md), and the hydrogel format of the [Chicago Cascade](../../modules/chicago-cascade/spec.md) are all of that kind. Proteinase K does not distinguish one LacZ from another, so in those systems it digests the reporter itself. Their background risk is unencapsulated substrate rather than stray enzyme, and the control for that is the purification step in [SUV Encapsulation](../encapsulate-suv/main.md).

The protocol also assumes a liposome suspension, since it removes the protease by pelleting and resuspending. It has no route to an already-embedded gel.
:::

:::{attention} Concentrations and volumes not yet specified
@Editor(chicago): no proteinase K concentration, reaction volume, or buffer is established for this protocol. This is a real gap, not an oversight — confirm working values before this protocol is used at the bench.
:::

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Why proteinase K, and why two temperatures
:class: dropdown
:icon: false

Proteinase K is a broad-spectrum serine protease: it digests LacZ (and other exterior protein) without needing to enter the liposome, since the target is already outside. The reported protocol uses two temperature steps — 50 °C for 10 min, then 40 °C for about 1 h — with no stated rationale for the split: whether 50 °C is a faster digestion step and 40 °C a lower-temperature hold to protect liposome integrity, or the reverse, is not documented. Treat this as the reported protocol, not a mechanistically justified one, until that rationale is established.

::::::

::::::{caution} Not yet validated; only a partial, related result exists
:class: dropdown
:icon: false

No result from running this exact proteinase K protocol exists yet — it is a proposed protocol, not a completed one. The closest existing data point is a prior, separate attempt using Trypsin (a different protease) instead of proteinase K: this reduced background signal but was not run at a fully optimized concentration. Treat the Trypsin result as a weak, related precedent for "digesting exterior protein reduces background," not as validation of the proteinase K steps below.

A chemical inhibitor of proteinase K has also been proposed, to stop digestion at a defined point (e.g., before it starts affecting intact liposomes) rather than relying on temperature or timing alone. This has not been tried. Do not assume an inhibitor is currently part of the protocol.

::::::

::::::{attention} Critical Materials
:class: dropdown
:icon: false

- **Proteinase K** — the digestion enzyme. Concentration not yet specified (see gap flagged above).
- A chemical inhibitor of proteinase K (e.g., PMSF or a similar serine-protease inhibitor) has been proposed for a future revision of this protocol, to give a controlled stopping point. It has not been selected or tested; do not add one without confirmation.

::::::

:::::::

# Materials and Equipment

:::{table}
:label: bom-degrade-exterior-lacz
:align: center

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Proteinase K | Reagent | Proteinase K, recombinant, PCR grade | Thermo Scientific | EO0491 | $131.00 | -20 °C | [link](https://www.thermofisher.com/order/catalog/product/EO0491) |
| Microcentrifuge tubes | Consumable | Safe-Lock microcentrifuge tubes, 1.5 mL | Eppendorf | 022363204 | $115.00 | RT | [link](https://www.fishersci.com/shop/products/eppendorf-snap-cap-microcentrifuge-biopur-safe-lock-tubes-3/0540225) |

:::

:::{attention} Bill of Materials is incomplete
@Editor(chicago): only the items directly confirmed are listed above. A dry bath or heat block (for the 50 °C and 40 °C incubation steps) and a centrifuge (for the final spin-down) are also required but do not yet have confirmed models — add specific models once confirmed, rather than guessing at part numbers here.
:::

# Protocol

:::{attention} Steps below are as reported, not independently optimized
These steps are reported, not independently optimized. Where a concentration, volume, or buffer is missing, the step says so explicitly rather than proposing a placeholder value.
:::

## Digest Exterior LacZ

- [ ] Resuspend proteinase K to a working concentration.

:::{attention} Gap: working concentration not specified
@Editor(chicago): no proteinase K concentration or resuspension buffer is established for this step.
:::

- [ ] Add the resuspended proteinase K to the synthetic cell (or other liposome) sample, in a volume sufficient to digest exterior LacZ without diluting the sample beyond what downstream steps require.

:::{attention} Gap: reaction volume and ratio not specified
@Editor(chicago): no proteinase K-to-sample volume ratio is established for this step.
:::

- [ ] Incubate at 50 °C for 10 min.
- [ ] Incubate at 40 °C for approximately 1 h.

## Recover Liposomes

- [ ] Spin down the synthetic cells (or other liposomes) to pellet them and separate them from the digested exterior LacZ and proteinase K remaining in solution.

:::{attention} Gap: centrifugation speed and time not specified
@Editor(chicago): no centrifuge speed or duration is established for this step. See [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) for a comparable spin-down step (9000 g / RT / 10 min) as a starting point to confirm against, not as a substitute value for this protocol.
:::

- [ ] Remove the supernatant and resuspend the liposome pellet in fresh outer solution.

# Quality Control

:::{attention} No confirmed QC metric yet
No result from running this exact protocol exists yet, so no target background-reduction value or pass/fail threshold can be given. The items below are proposed checks, not validated criteria.
:::

- **Background signal**: Compare CPRG (or other chromogenic substrate) hydrolysis in the outer solution before and after this protocol, without triggering intended liposome lysis. A successful run should measurably reduce background absorbance relative to an untreated control.
- **Liposome integrity**: Confirm that synthetic cell counts and morphology (round, intact liposomes) are not reduced by the 50 °C step relative to an untreated control, since 50 °C is close to conditions known to affect membrane stability in other processes.

# Credits

Developed by Jonah McDonald and Charlie Newell (London Node) and Mary Kelly (Chicago Node, Kamat Lab).

# Downloads

::::{grid} 1 1 1 1

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/degrade-exterior-lacz-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/degrade-exterior-lacz-bom.pdf>`
:::

::::

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
