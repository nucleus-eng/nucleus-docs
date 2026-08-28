---
title: "Effector: PLA1"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The PLA1 Lysis Module uses phospholipase A1 (PLA1) to genetically encode lysis. Once expressed, PLA1 degrades the phospholipid membrane and lyses the cell and its neighbors. This can be used to release chemical payloads from neighboring liposomes (e.g. [CPRG-SUV cells](../substrate-cprg-suv/spec.md)) into an external solution (e.g., of [LacZ](../reporter-lacz/spec.md), triggering a [colorimetric signal](../../processes/colorimetric-readout/main.md)). PLA1 can sit downstream of a sensing circuit (e.g. a [TetO detector module](../detector-tetr-atc/spec.md)) that controls when it is expressed, and upstream of a reporter module requiring lysis (e.g., [LacZ](../reporter-lacz/spec.md)).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} PLA1 is characterized without a sensing circuit, but never without a readout chain
One configuration removes the gate — constitutive expression in Nucleus Cytosol, described under Expected Behavior below. It supplies the only DNA dose and timing figures attributable to PLA1 alone. Every other result on this page comes from a cascade, where the sensing circuit and PLA1 cannot be separated.

No result isolates PLA1 from the CPRG/LacZ readout. Lysis is always scored by the color it releases, never by a direct measure of membrane rupture or of enzyme activity, so no efficiency figure exists for PLA1 in any configuration.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{table}
| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| `T7pro-PLA1-T7term` | not yet determined | — | pT7; Chicago theophylline and pH cascades |
| `LuxR-PLA1` | 2237 | — | Constitutive `BBa_J23101`→`luxR` with `pLux`-driven PLA1, one molecule; London AHL cascade. Also referred to as `P70lux-PLA1-term`. |
:::

:::{attention} Neither construct is in `nucleus-eng/DNA`
Neither has a confirmed sequence file in [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA). Do not add a length or file entry until one lands there and its identity is confirmed against the construct name.
:::

::::

::::{tab-item} Cytosol

PLA1 is expressed from one of the constructs above rather than added as a reagent, so it has no working concentration of its own.

:::{table} PLA1 DNA dose, by configuration.
:label: comp-pla1-cytosol

| Configuration | Construct | Working concentration |
| --- | --- | --- |
| London constitutive, ungated | `T7pro-PLA1-T7term` | 14 ng/µL, in a 20 µL reaction with 5% Optiprep |
| Chicago aTc | `TetO-PLA1` | 1 nM (also tested at 0.5 nM) |
| London AHL | `LuxR-PLA1` | 15 ng/µL |
| Chicago pH | Toehold-switch-gated PLA1 template | 2 nM |
| Chicago theophylline | `T7pro-PLA1-T7term` | Not documented |
:::

The cytosol itself is whichever the host configuration uses — [Base Cytosol](../base-cytosol/spec.md) for the Chicago cascades and for the ungated London run, [S30 Lysate](../s30-lysate/spec.md) for the London AHL cascade.

::::

<!-- composition-tabs: no-table (PLA1 acts on any phospholipid membrane in reach, so a single lipid table would be wrong) -->
::::{tab-item} Membrane

PLA1 lyses a membrane, so a membrane is part of every configuration that uses it. No lipid composition is specific to this Module: PLA1 acts on any phospholipid membrane it reaches, whether or not that membrane belongs to the cell that expressed it. The membranes it has been used with are [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md) and [London Membrane: POPC](../membrane-popc/spec.md).

Both a self-lysis target and, in the two-liposome cascades, a neighboring [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md) membrane are required.

::::

:::::

(effector-pla1-expected-behavior)=
# Expected Behavior

## Cells

PLA1 lyses synthetic cells in which this module is expressed, as well as synthetic cells in their vicinity. This module has been used in five (5) documented contexts. The first is the only one with no upstream gate, so it is the only one that reports on PLA1 rather than on a cascade:

- **London constitutive expression, ungated.** `T7pro-PLA1-T7term` at 14 ng/µL in [Base Cytosol](../base-cytosol/spec.md) liposomes, with no sensing circuit, drives the two-liposome CPRG/LacZ handoff. Color appears from about 3 h at 37 °C and is easily discernible by 16 h, against a minus-DNA control in the same run, and has been reproduced across multiple days. Expect a visible result on that timescale at this dose. The reaction format — solution or hydrogel — is not recorded with the result.
- **Chicago theophylline cascade.** A [theophylline riboswitch](../detector-theophylline/spec.md) gates PLA1 expression. PLA1 ruptures its own synthetic cell and a neighboring [CPRG-loaded synthetic cell](../substrate-cprg-suv/spec.md), releasing CPRG to an external [LacZ](../reporter-lacz/spec.md) solution and producing a visible color change after ~16 h in an alginate hydrogel. Confirmed at the synthetic cell/hydrogel level, with a known caveat: the color change currently occurs with or without theophylline present (riboswitch leak), so target specificity is not yet solved.
- **[Chicago pH cascade](../ph-cascade/spec.md).** A [pH-responsive toehold switch](../detector-ph/spec.md) gates PLA1. The same two-liposome CPRG/LacZ handoff produces a visible yellow-to-purple change at pH 6.5 in solution. Confirmed at the solution level only; not yet moved into the hydrogel-embedded chassis.
- **[Chicago aTc cascade](../atc-cascade/spec.md).** See the [tetR-aTc Detector Module](../detector-tetr-atc/spec.md) spec, "Chicago Cascade Encapsulation (TetO-PLA1 / LacZ-CPRG Readout)" section: a `TetO-PLA1` construct is co-encapsulated with LacZ in a synthetic cell, with CPRG outside so that lysis is what brings them together, showing a detectable but **non-graded** absorbance response to aTc (saturating at or below 1 µM). This is the only PLA1 result reduced to numbers; the rest are scored by eye.
- **[London AHL cascade](../london-cascade/spec.md).** A [LuxR/pLux quorum-sensing promoter](../detector-3oc6-hsl/spec.md) gates PLA1 expression in [S30 Lysate](../s30-lysate/spec.md). PLA1 lysis again triggers the CPRG/LacZ handoff. As of the latest report, this shows a discernible but still leaky difference in color change between +AHL and −AHL conditions; the team is optimizing DNA and AHL concentrations to widen this gap.

:::{attention} Four of these five are cascade results
Only the ungated configuration reports on PLA1 by itself. In the other four, PLA1 and the sensing circuit that gates it cannot be told apart — a weak result there may be either. None of the five isolates PLA1 from the CPRG/LacZ readout it drives.
:::

:::{attention} Premature lysis has two independent causes
**Gramicidin A causes premature lysis; it does not prevent it.** Used as a proton channel for the pH cascade's GFP-expression result, it was left out of the colorimetric demonstration because it ruptured a portion of the CPRG-loaded liposomes, producing nonspecific color. Its absence can reduce pH-sensing efficiency, but proton diffusion into the more permeable liposomes was enough to drive PLA1 expression and initiate the lysis cascade.

**Acidic conditions alone rupture some CPRG-loaded liposomes**, independent of PLA1, which confounds attributing a color change to the sensing pathway.

Account for both routes rather than assuming a liposome stays intact until the intended trigger.
:::

(effector-pla1-requirements)=
# Requirements

Requires a phospholipid membrane to lyse (e.g. [London Membrane](../membrane-popc/spec.md), [Chicago Membrane](../membrane-popc-chol-chicago/spec.md)).

Requires an upstream sensing circuit (e.g. [Detector: AHL](../detector-3oc6-hsl/spec.md), [Detector: tetR-aTc](../detector-tetr-atc/spec.md)) only where lysis must be conditional. Expressed constitutively, PLA1 lyses on its own schedule.

Requires pT7 transcription and translation, when using `T7pro-PLA1-T7term` (e.g. [Base Cytosol](../base-cytosol/spec.md)).

Requires sigma-70 transcription and translation, when using `LuxR-PLA1` (e.g. [S30 Lysate](../s30-lysate/spec.md)).

Do not add Gramicidin A to a colorimetric cascade. See [Expected Behavior](#effector-pla1-expected-behavior) for why.

(effector-pla1-implementations)=
# Implementations

- [Chicago DevCell](../../implementations/chicago-devcell/main.md): PLA1 drives the aTc, pH and theophylline colorimetric readouts.
- [London DevCell](../../implementations/london-devcell/main.md): PLA1 drives the AHL quorum-sensing colorimetric readout.

# Processes

- [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) — applies only where LacZ is encapsulated. Proteinase K does not distinguish one LacZ from another, so in a configuration that puts LacZ in the outer solution it digests the reporter.
- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the CPRG conversion that produces the visible signal
- [Alginate Hydrogel Embedding](../../processes/embed-alginate-hydrogel/main.md) — the Chicago hydrogel format
- [ULGA Hydrogel Embedding](../../processes/embed-ulga-hydrogel/main.md) — the London hydrogel format

# Credits

Developed by Jonah McDonald and Charlie Newell (London Node) and Mary Kelly (Chicago Node, Kamat Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
