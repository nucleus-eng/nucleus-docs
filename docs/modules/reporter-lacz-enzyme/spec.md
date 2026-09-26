---
title: "Reporter: LacZ Enzyme"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`lacz`](../lacz/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

The LacZ Enzyme is β-galactosidase from *E. coli*, the hydrolase half of the [LacZ Reporter](../reporter-lacz/spec.md) colorimetric pair. It cleaves [CPRG](../substrate-cprg/spec.md) from yellow chlorophenol red-β-D-galactopyranoside to magenta chlorophenol red.

**The monomer is 116.3 kDa and the active form is the tetramer at 465 kDa** (Jon, 2026-09-24; no vendor page cited for these two figures). **The active form is two orders of magnitude above the largest pore cutoff in this corpus**, ~3 kDa for [α-hemolysin](../membrane-pore-ahly/spec.md), so this enzyme never crosses a membrane. **That does not force lysis on a format that encloses it**, because the readout only needs the two to meet and [CPRG](../substrate-cprg/spec.md) is small enough to come in. See [LacZ Reporter](../reporter-lacz/spec.md).

**It is a separate Module from its substrate because the two are routinely in different compartments.** In the London Cascade the enzyme is dispersed free in the gel while CPRG is held inside a liposome population; in the aTc path the enzyme is encapsulated with the sensing reaction and CPRG stays outside. Which compartment each occupies is set by the process that places it, not by the reporter chemistry — so a page describing the pair cannot state a single location for either.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**This Module has been used across a roughly sixty-fold range, and no single figure is canonical.** The range is what this page states; a page that composes the enzyme states the figure its own result used.

:::{table} LacZ Enzyme — the range in use.
| Context | Working concentration | Source |
| --- | --- | --- |
| Encapsulated in a GUV, in PEG-norbornene | **2.5 U/mL** final — 0.5 µL of a 125 U/mL stock into a 25 µL cell-free reaction | Chicago Node, Kamat Lab, 2026-09-11 |
| Encapsulated in a GUV, in 0.7% agarose | **156 U/mL** | Chicago Node, Liu Lab, 2026-09-11 |
| Dispersed in the gel | not documented | London Cascade, ULGA embedding |
:::

**Both encapsulated figures are for the same arrangement** — enzyme inside the cell, substrate outside — and they differ by about 60×. Co-encapsulating the enzyme with its substrate would make the readout constitutive, which is why neither format does it.

:::{attention} The 20 U/mL this documentation used to state is withdrawn
Ten pages carried 20 U/mL as the encapsulated working concentration. No titration, assay or reference was ever recorded behind it, and when the Chicago Node was asked directly what concentration it uses in the synthetic cells, the answer computed to **2.5 U/mL** — the same arrangement, eight-fold lower.

**Not a difference of context.** The question and the answer were both about the aTc sensing cells. So 20 U/mL is withdrawn rather than kept as a third entry: a figure with nothing behind it should not anchor a range of measured ones.
:::

:::{attention} The gel-dispersed concentration is still missing
@Editor(london): the London Cascade disperses this enzyme through the ULGA gel and no concentration is recorded for it anywhere. Without it that half of the cascade cannot be reproduced.

**The Chicago figures do not carry across.** Both are encapsulated; London's is dispersed through the matrix. Different arrangement, different requirement.
:::

**Potency degrades in storage.** A stock kept at 4 °C loses activity over time, visibly slowing the color change. The figures above are for fresh enzyme.

@Editor(chicago): the commercial enzyme is β-galactosidase from *E. coli* and London sources it as Sigma-Aldrich G5635. Both nodes hold it at the same pack size, 2 × 3 KU. Confirm it is the same product.

# Requirements

Requires [CPRG](../substrate-cprg/spec.md) to produce a signal — the enzyme alone has no readout.

**Requires that enzyme and substrate be separated until the moment of readout.** Any route that puts both in one compartment before the trigger gives color with no analyte present. That separation is the reporter's whole mechanism, and it is a property of the composition rather than of either Module.

Proteinase K does not distinguish one LacZ from another, so [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) cannot be applied to a format that disperses the enzyme through the matrix on purpose.

**The enzyme and its substrate are one parameter, and that parameter is a set of pairs.** This
corpus carries three: `(LacZ, CPRG)`, `(LacZ, X-Gal)` and `(XylE, catechol)`. Writing the enzyme
and the substrate as two independent lists would give six combinations and invent three that are
wrong chemistry: `(LacZ, catechol)`, `(XylE, CPRG)` and `(XylE, X-Gal)`. Per-component ranges are
projections of the joint set, and a projection loses the joint.

**The rule, not the enumeration, is what holds.** The valid set is every pair `(E, S)` where `S`
is a substrate of `E`. The three pairs above are what that rule returns over the enzymes this
corpus documents today, and a fourth enzyme joins without anything here changing. The materials
tracker lists **tyrosinase, also called catechol oxidase**, alongside XylE, so catechol's enzyme
may already not be unique.

**This also settles how not to write it.** *"Substrate, with the enzyme derived from it"* fails
on CPRG and X-Gal, which share an enzyme.

# Processes

- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the CPRG conversion this enzyme performs, read at 575 nm and by eye.
- [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) — digests enzyme that escaped the sensing cells, for encapsulated formats only.

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
