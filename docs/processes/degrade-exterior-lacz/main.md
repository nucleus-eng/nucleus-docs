---
title: "Degrade Exterior LacZ"
subtitle: "Process"
status: draft  # draft | unvalidated-published | validated-published — see CLAUDE.md "Page status"
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

Degrade Exterior LacZ uses proteinase K to break down LacZ reporter enzyme that has leaked outside a liposome, cutting the background color signal that this exterior LacZ would otherwise add to a colorimetric readout. Proteinase K is added to the sample, given time to digest the exterior (non-encapsulated) LacZ, then removed by pelleting the liposomes and resuspending them in fresh solution.

This protocol was raised in the 2026-08-14 DevStudio status meeting, in answer to a London question about exterior LacZ leakage from synthetic cells. It responds to a general problem — LacZ that ends up outside a liposome can hydrolyze CPRG (or another chromogenic substrate) in solution and produce color that is not from the intended, liposome-triggered handoff. This affects any DevCells cascade that relies on a clean, lysis-triggered LacZ/CPRG color change, including the [PLA1 Lysis Module](../../modules/effector-pla1/spec.md).

:::{attention} Concentrations and volumes not yet specified
The source material (meeting transcript only; not in the accompanying slide deck) names the steps and temperatures below, but does not give a proteinase K concentration, a reaction volume, or a buffer. This is a real gap, not an oversight in transcription — flag it rather than filling it in. Confirm working values with the team before running this protocol, and update this page once they exist.
:::

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Why proteinase K, and why two temperatures
:class: dropdown
:icon: false

Proteinase K is a broad-spectrum serine protease: it digests LacZ (and other exterior protein) without needing to enter the liposome, since the target is already outside. The two-temperature protocol reported in the meeting — 50 °C for 10 min, then 40 °C for about 1 h — was described only as "chew up exterior lacZ" followed by those two incubation steps. No source material explains the purpose of the specific temperature split (e.g., whether 50 °C is a faster digestion step and 40 °C a lower-temperature hold to protect liposome integrity, or the reverse). Treat this as the reported protocol, not a mechanistically justified one, until the team documents the rationale.

::::::

::::::{caution} Not yet validated; only a partial, related result exists
:class: dropdown
:icon: false

No result from running this exact proteinase K protocol was reported in the meeting — it was raised as a proposed protocol, not a completed one. The closest existing data point is a prior, separate attempt on the London side using Trypsin (a different protease) instead of proteinase K: this reduced background signal but was not run at a fully optimized concentration. Treat the Trypsin result as a weak, related precedent for "digesting exterior protein reduces background," not as validation of the proteinase K steps below.

A chemical inhibitor of proteinase K was also mentioned as a possible next step, to stop digestion at a defined point (e.g., before it starts affecting intact liposomes) rather than relying on temperature or timing alone. This has not been tried. Do not assume an inhibitor is currently part of the protocol.

::::::

::::::{attention} Critical Materials
:class: dropdown
:icon: false

- **Proteinase K** — the digestion enzyme. Concentration not yet specified (see gap flagged above).
- A chemical inhibitor of proteinase K (e.g., PMSF or a similar serine-protease inhibitor) is under consideration for a future revision of this protocol, to give a controlled stopping point. Not yet selected or tested — do not add one without confirming with the team first.

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
Only the items directly named in source material are listed above. A dry bath or heat block (for the 50 °C and 40 °C incubation steps) and a centrifuge (for the final spin-down) are also required but were not itemized in the meeting notes — add specific models once confirmed, rather than guessing at part numbers here.
:::

# Protocol

:::{attention} Steps below are as reported, not independently optimized
Each step reflects what was described in the 2026-08-14 meeting transcript. Where a concentration, volume, or buffer is missing, the step says so explicitly rather than proposing a placeholder value.
:::

## Digest Exterior LacZ

- [ ] Resuspend proteinase K to a working concentration.

:::{attention} Gap: working concentration not specified
Source material does not give a proteinase K concentration or resuspension buffer. Confirm with the team before running this step.
:::

- [ ] Add the resuspended proteinase K to the synthetic cell (or other liposome) sample, in a volume sufficient to digest exterior LacZ without diluting the sample beyond what downstream steps require.

:::{attention} Gap: reaction volume and ratio not specified
Source material does not give a proteinase K-to-sample volume ratio. Confirm with the team before running this step.
:::

- [ ] Incubate at 50 °C for 10 min.
- [ ] Incubate at 40 °C for approximately 1 h.

## Recover Liposomes

- [ ] Spin down the synthetic cells (or other liposomes) to pellet them and separate them from the digested exterior LacZ and proteinase K remaining in solution.

:::{attention} Gap: centrifugation speed and time not specified
Source material does not give a centrifuge speed or duration for this step. See [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) for a comparable spin-down step (9000 g / RT / 10 min) as a starting point to confirm against, not as a substitute value for this protocol.
:::

- [ ] Remove the supernatant and resuspend the liposome pellet in fresh outer solution.

# Quality Control

:::{attention} No confirmed QC metric yet
No result from running this exact protocol was reported in the source material, so no target background-reduction value or pass/fail threshold can be given yet. The items below are proposed checks, not validated criteria.
:::

- **Background signal**: Compare CPRG (or other chromogenic substrate) hydrolysis in the outer solution before and after this protocol, without triggering intended liposome lysis. A successful run should measurably reduce background absorbance relative to an untreated control.
- **Liposome integrity**: Confirm that synthetic cell counts and morphology (round, intact liposomes) are not reduced by the 50 °C step relative to an untreated control, since 50 °C is close to conditions known to affect membrane stability in other processes.

# Known Future Work

:::{attention} Gap: proteinase K concentration, reaction volume, and buffer
Proteinase K concentration, reaction volume, and buffer are not specified in available source material; do not substitute values from another protocol.
:::

# Credits

Raised in the 2026-08-14 DevStudio status meeting in response to a London question about exterior LacZ leakage from synthetic cells.

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
