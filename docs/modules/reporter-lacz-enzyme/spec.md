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

**The monomer is 116.5 kDa and the active form is the tetramer at 465.9 kDa** ([UniProt P00722](https://www.uniprot.org/uniprotkb/P00722/entry), β-galactosidase, *E. coli* K12, 1024 residues). The page carried 116.3 and 465 before the citation was checked; the figures here are the ones the entry gives. **The active form is two orders of magnitude above the largest pore cutoff on these pages**, ~3 kDa for [α-hemolysin](../membrane-pore-ahly/spec.md), so this enzyme never crosses a membrane. **That does not force lysis on a format that encloses it**, because the readout only needs the two to meet and [CPRG](../substrate-cprg/spec.md) is small enough to come in. See [LacZ Reporter](../reporter-lacz/spec.md).

**The enzyme and its substrate are routinely in different compartments.** In the LuxR-LacZ Sensor Cascade the enzyme is dispersed free in the gel while CPRG is held inside a liposome population; in the aTc path the enzyme is encapsulated with the sensing reaction and CPRG stays outside. Which compartment each occupies is set by the process that places it, not by the reporter chemistry.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**This Module has been used across a roughly sixty-fold range, and no single figure is canonical.** A Module that composes the enzyme states the figure its own result used.

:::{table} LacZ Enzyme — the range in use.
| Context | Working concentration |
| --- | --- |
| Encapsulated in a GUV, in PEG-norbornene | **2.5 U/mL** final — 0.5 µL of a 125 U/mL stock into a 25 µL cell-free reaction |
| Encapsulated in a GUV, in 0.7% agarose | **156 U/mL** |
| Dispersed in the gel | not documented |
:::

**Both encapsulated figures are for the same arrangement** — enzyme inside the cell, substrate outside — and they differ by about 60×. Co-encapsulating the enzyme with its substrate would make the readout constitutive, which is why neither format does it.

:::{attention} The gel-dispersed concentration is not documented
@Editor(london): the LuxR-LacZ Sensor Cascade disperses this enzyme through the ULGA gel and no concentration is recorded for it anywhere. Without it that half of the cascade cannot be reproduced.

**The Chicago figures do not carry across.** Both are encapsulated; London's is dispersed through the matrix. Different arrangement, different requirement.
:::

**Potency degrades in storage.** A stock kept at 4 °C loses activity over time, visibly slowing the color change. The figures above are for fresh enzyme.

@Editor(chicago): the commercial enzyme is β-galactosidase from *E. coli* and London sources it as Sigma-Aldrich G5635. Both nodes hold it at the same pack size, 2 × 3 KU. Confirm it is the same product.

# Requirements

Requires [CPRG](../substrate-cprg/spec.md) to produce a signal — the enzyme alone has no readout.

**Requires that enzyme and substrate be separated until the moment of readout.** Any route that puts both in one compartment before the trigger gives color with no analyte present. That separation is the reporter's whole mechanism, and it is a property of the composition rather than of either Module.

Proteinase K does not distinguish one LacZ from another, so [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) cannot be applied to a format that disperses the enzyme through the matrix on purpose.

Requires the enzyme and the substrate to be a valid pair: the substrate must be one the enzyme acts on. The valid pairs are `(LacZ, CPRG)`, `(LacZ, X-Gal)` and `(XylE, catechol)`. A cross pair such as `(LacZ, catechol)`, `(XylE, CPRG)` or `(XylE, X-Gal)` is wrong chemistry.

A new enzyme adds its own pairs without changing these.

# Processes

- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the CPRG conversion this enzyme performs, read at 575 nm and by eye.
- [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) — digests enzyme that escaped the sensing cells, for encapsulated formats only.

# Implementations

- [aTc Demo](../../implementations/devstudio-atc-demo/main.md): its reporter — encapsulated with the circuit, at 2.5 U/mL.
- [CRAIC Demo](../../implementations/devstudio-craic-demo/main.md): its reporter — in the gel, meeting CPRG only after lysis.
- [pH Demo](../../implementations/devstudio-ph-demo/main.md): its reporter — in the basic buffer, added after the sensing step.

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
