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

:::{attention} No PLA1-specific experimental data
@Editor: no experiment characterizes PLA1 on its own. Every result below comes from a cascade that uses it, so no PLA1 concentration, timing or efficiency figure exists independent of a sensing circuit. Confirm whether such data exists.
:::

# Reference Composition

:::::{tab-set}

::::{tab-item} DNA

:::{table}
| **Name** | **Length (bp)** | **File** | **Supply route** |
| --- | --- | --- | --- |
| `T7pro-PLA1-T7term` | not yet determined | — | pT7; Chicago theophylline and pH cascades |
| `P70lux-PLA1-term` | not yet determined | — | *E. coli* P70/pLux; London AHL cascade |
:::

:::{attention} Neither construct is in `nucleus-eng/DNA`
Neither has a confirmed sequence file in [nucleus-eng/DNA](https://github.com/nucleus-eng/DNA). Do not add a length or file entry until one lands there and its identity is confirmed against the construct name.
:::

::::

::::{tab-item} Cytosol

PLA1 is expressed from one of the constructs above rather than added as a reagent, so it has no working concentration of its own.

:::{table} PLA1 DNA dose, by cascade.
:label: comp-pla1-cytosol

| Cascade | Construct | Working concentration |
| --- | --- | --- |
| Chicago aTc | `TetO-PLA1` | 1 nM (also tested at 0.5 nM) |
| London AHL | `P70lux-PLA1-term` | 15 ng/µL |
| Chicago pH | Toehold-switch-gated PLA1 template | 2 nM |
| Chicago theophylline | `T7pro-PLA1-T7term` | Not documented |
:::

The cytosol itself is whichever the host cascade uses — [Base Cytosol](../base-cytosol/spec.md) for the Chicago cascades, [S30 Lysate](../s30-lysate/spec.md) for London.

::::

<!-- composition-tabs: no-table (PLA1 acts on any phospholipid membrane in reach, so a single lipid table would be wrong) -->
::::{tab-item} Membrane

PLA1 lyses a membrane, so a membrane is part of every configuration that uses it. No lipid composition is specific to this Module: PLA1 acts on any phospholipid membrane it reaches, whether or not that membrane belongs to the cell that expressed it. The membranes it has been used with are [Chicago Membrane: POPC/Chol](../membrane-popc-chol-chicago/spec.md) and [London Membrane: POPC](../membrane-popc/spec.md).

Both a self-lysis target and, in the two-liposome cascades, a neighboring [Substrate SUV: CPRG](../substrate-cprg-suv/spec.md) membrane are required.

::::

:::::

# Expected Behavior

## Cells

PLA1 lyses synthetic cells in which this module is expressed, as well as synthetic cells in their vicinity. This module has been used in four (4) documented contexts:

- **Chicago theophylline cascade.** A [theophylline riboswitch](../detector-theophylline/spec.md) gates PLA1 expression. PLA1 ruptures its own synthetic cell and a neighboring [CPRG-loaded synthetic cell](../substrate-cprg-suv/spec.md), releasing CPRG to an external [LacZ](../reporter-lacz/spec.md) solution and producing a visible color change after ~16 h in an alginate hydrogel. Confirmed at the synthetic cell/hydrogel level, with a known caveat: the color change currently occurs with or without theophylline present (riboswitch leak), so target specificity is not yet solved.
- **[Chicago pH cascade](../ph-cascade/spec.md).** A [pH-responsive toehold switch](../detector-ph/spec.md) gates PLA1. The same two-liposome CPRG/LacZ handoff produces a visible yellow-to-purple change at pH 6.5 in solution. Confirmed at the solution level only; not yet moved into the hydrogel-embedded chassis.
- **[Chicago aTc cascade](../atc-cascade/spec.md).** See the [tetR-aTc Detector Module](../detector-tetr-atc/spec.md) spec, "Chicago Cascade Encapsulation (TetO-PLA1 / LacZ-CPRG Readout)" section: a `TetO-PLA1` construct is co-encapsulated with LacZ in a synthetic cell, with CPRG outside so that lysis is what brings them together, showing a detectable but **non-graded** absorbance response to aTc (saturating at or below 1 µM). This is currently the only PLA1 result with primary supporting data behind it.
- **[London AHL cascade](../london-cascade/spec.md).** A [LuxR/pLux quorum-sensing promoter](../detector-3oc6-hsl/spec.md) gates PLA1 expression in [S30 Lysate](../s30-lysate/spec.md). PLA1 lysis again triggers the CPRG/LacZ handoff. As of the latest report, this shows a discernible but still leaky difference in color change between +AHL and −AHL conditions; the team is optimizing DNA and AHL concentrations to widen this gap.

:::{attention} These are cascade results, not PLA1 characterization
Each summary describes PLA1 working inside a cascade. None isolates PLA1's own performance.
:::

:::{attention} Premature lysis has two independent causes
**Gramicidin A causes premature lysis; it does not prevent it.** Used as a proton channel for the pH cascade's GFP-expression result, it was left out of the colorimetric demonstration because it ruptured a portion of the CPRG-loaded liposomes, producing nonspecific color. Its absence can reduce pH-sensing efficiency, but proton diffusion into the more permeable liposomes was enough to drive PLA1 expression and initiate the lysis cascade.

**Acidic conditions alone rupture some CPRG-loaded liposomes**, independent of PLA1, which confounds attributing a color change to the sensing pathway.

Account for both routes rather than assuming a liposome stays intact until the intended trigger.
:::

# Requirements

Requires an upstream sensing circuit to gate expression (e.g. [Detector: AHL](../detector-3oc6-hsl/spec.md), [Detector: tetR-aTc](../detector-tetr-atc/spec.md)), a phospholipid membrane to lyse (e.g. [London Membrane](../membrane-popc/spec.md), [Chicago Membrane](../membrane-popc-chol-chicago/spec.md)), and a downstream reporter enzyme with its chromogenic substrate in a neighboring liposome ([LacZ](../reporter-lacz/spec.md) with [CPRG](../substrate-cprg-suv/spec.md), or [XylE/C23DO](../reporter-xyle/spec.md) with catechol).

Using `T7pro-PLA1-T7term` requires pT7 transcription and translation (e.g. [Base Cytosol](../base-cytosol/spec.md)). Using `P70lux-PLA1-term` requires sigma-70 transcription and translation (e.g. [S30 Lysate](../s30-lysate/spec.md)).

Do not add Gramicidin A to a colorimetric cascade. See [Expected Behavior](#expected-behavior) for why.

# Implementations

- [Chicago DevCell](../../implementations/chicago-devcell/main.md): PLA1 drives the aTc, pH and theophylline colorimetric readouts.
- [London DevCell](../../implementations/london-devcell/main.md): PLA1 drives the AHL quorum-sensing colorimetric readout.

# Processes

- [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md)

- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the CPRG conversion that produces the visible signal
- [Alginate Hydrogel Embedding](../../processes/embed-alginate-hydrogel/main.md) — the Chicago hydrogel format
- [ULGA Hydrogel Embedding](../../processes/embed-ulga-hydrogel/main.md) — the London hydrogel format

# Credits

Developed by Jonah McDonald and Charlie Newell (London Node) and Mary Kelly (Chicago Node, Kamat Lab).
