---
title: "Amplify Linear Template"
subtitle: "Process"
---

# Overview

A linear DNA template is a PCR product: an expression cassette amplified from a gBlock or a plasmid, with no backbone around it. This Process makes one.

**The product is what the choice is about, not the method.** A linear template is for [Base Cytosol](../../modules/base-cytosol/spec.md) and the other PURE-derived systems. It is the wrong input for an S30 reaction, which degrades linear DNA, so [S30 Lysate](../../modules/s30-lysate/spec.md) takes the same cassette in a `pOpen` backbone instead. Two presentations of one cassette are functionally equivalent and not sequence-identical, and a page citing one is not citing the other.

:::::::{card}
:header: **Important Information**

::::::{note} Notes
:class: dropdown
:icon: false

- **The primer pair is M13 forward and M13 reverse** where the cassette sits in a `pOpen` plasmid, because `pOpen` carries the M13 sites either side of the insert. A cassette amplified from a gBlock takes primers designed against its own ends.

- **Q5 is used for template amplification across this corpus** because the product is read back as a sequence. A proofreading polymerase is the point; a Taq-based mix is not a substitute here.

::::::

:::::::

# Materials and Equipment

<!-- vale nucleus.magnitude-unit-spacing = NO -->
:::{table} Bill of Materials
:label: bom-amplify-linear-template

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Q5 polymerase | Enzyme | Q5 High-Fidelity DNA Polymerase | NEB | — | — | -25 °C to -15 °C | — |
| HF buffer | Buffer | Q5 High-Fidelity Reaction Buffer | NEB | — | — | -25 °C to -15 °C | — |
| Forward primer | Oligo | Synthesized to the cassette's 5' end; M13 forward where the source is a `pOpen` plasmid | — | — | — | -25 °C to -15 °C | — |
| Reverse primer | Oligo | Synthesized to the cassette's 3' end; M13 reverse where the source is a `pOpen` plasmid | — | — | — | -25 °C to -15 °C | — |
:::

**Three of these rows have a manufacturer and no part number, and that is the honest state rather than an omission.** NEB sells Q5 in several formats and most bundle the buffer, so naming one catalog number here would be a guess about which the bench uses. A synthesized primer has no catalog number at all — it is ordered to a sequence, so the vendor is real and the part is not. The reference shows whatever link a row carries and a row that carries none shows none; see [Materials Reference](../../../guides/materials-reference.md).

@Editor(london): supply the Q5 format actually used and its catalog number, and the oligo vendor. Both travel with the protocol.

# Protocol

## Set up the reaction

- [ ] Thaw the polymerase, buffer, primers and template on ice. Keep the polymerase in a cold block.

- [ ] Assemble on ice, scaling to the number of reactions plus one.

- [ ] Include a no-template control. A linear template is carried forward into a cell-free reaction, where a contaminating amplicon is indistinguishable from the intended one.

@Editor(london): record the reaction volume and the per-component volumes. The 2026-09-23 EsaO/R step is the source and is not in this repo.

## Cycle

- [ ] Run the cycling program for the primer pair in use.

@Editor(london): record the annealing temperature, extension time and cycle count for this cassette. **They are per-primer-pair and must not be copied from another construct's run** — [Responder: aTc → IV-HSL](../../implementations/responder-atc-ivhsl/main.md) records 64 °C and 25 s for its own two amplicons with an M13 reverse primer, which is a worked example of the shape and not the values for this one.

## Check and clean up

- [ ] Run an aliquot on a gel and confirm a single band at the expected length.

- [ ] Purify the product and quantify it.

- [ ] Verify the sequence before the template is used in a reaction. A Designs-table row is an identity claim, and the length alone does not establish it: two products of the same length can differ in sequence.

# Processes

- [Assemble Cytosol](../assemble-cytosol/assemble-cytosol-main.md) — where a linear template is spent.

# Credits

@Editor(london): the protocol is the London Node's. Name its author here.
