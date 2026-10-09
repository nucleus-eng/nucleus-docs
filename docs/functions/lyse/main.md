---
title: "Lyse"
subtitle: "Function"
status: draft
---

# Overview

Lyse breaks a membrane and releases what it held into the surrounding solution. One Module here does it by design, [Lysis: PLA1](../../modules/effector-pla1/spec.md), which expresses an enzyme that breaks down the membrane's phospholipids. Lysis is how a cascade here hands a signal from one compartment to the next: a sensing cell lyses itself and the dye-loaded liposomes near it, and the dye meets an enzyme outside.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Lyse takes the lysing Module and a membrane with something inside it, and returns the lysing Module with the contents now loose in the solution around them. The membrane is gone, so the difference between inside and outside that it kept is gone too.

**It acts on every phospholipid membrane in reach, not on one.** A lysing Module does not tell the membrane that made it from a neighbor's. So lysis reaches the whole compartment the lysing Module shares, and a design that needs one membrane spared has to keep it out of reach. See [Lysis](../../modules/lysis/spec.md).

# Substrates and products

| | Consumes | Produces | Unchanged |
| --- | --- | --- | --- |
| **PLA1** | the membrane's phospholipids | the membrane, broken down, and its contents, released | the PLA1 enzyme |

Phospholipase A1 cuts the fatty acid chain at the first position of a phospholipid.

**What this does to the number of dissolved particles.** The phospholipids broken down are few next to the solutes on either side. What changes is that the inside and the outside become one solution, so the osmotic difference the membrane held no longer exists. No run has measured it.

# Routes

| Route | How it breaks the membrane | Realized by |
| --- | --- | --- |
| Phospholipase | an expressed enzyme breaks down the bilayer's phospholipids | [Lysis: PLA1](../../modules/effector-pla1/spec.md) |

# What selects a route

- **What drives the enzyme.** PLA1 is expressed from DNA, so it lyses only once it is made. Expressed with nothing in front of it, it lyses on its own schedule. Placed behind a sensing circuit, such as [Detector: 3OC6-HSL (LuxR)](../../modules/detector-3oc6-hsl/spec.md) or [Detector: tetR-aTc](../../modules/detector-tetr-atc/spec.md), it lyses when the analyte arrives.
- **Which construct, and so which cytosol.** `T7pro-PLA1-T7term` needs T7 transcription, as in [Base Cytosol](../../modules/base-cytosol/spec.md). `LuxR-PLA1` needs σ70 transcription, as in [S30 Lysate](../../modules/s30-lysate/spec.md). See [Transcribe](../transcribe/main.md).
- **How low the background is.** A lysing Module needs its uninduced state not to lyse already. PLA1's page records three cases where it does not meet that today. See the Requirements of [Lysis: PLA1](../../modules/effector-pla1/spec.md).
- **What else breaks membranes in the same compartment.** [Membrane Pore: Gramicidin A](../../modules/membrane-pore-gramicidin/spec.md) ruptured some dye-loaded liposomes in one cascade, and acidic conditions alone rupture some too. Neither is lysis by design, and both release dye with no lysis signal, so a readout cannot tell them from PLA1.

# Not yet attested

- A direct measure of a membrane breaking, or of PLA1's enzyme activity. Every result scores lysis by the color the released dye makes, so no efficiency figure exists.
- A numeric limit for how low the uninduced background must be.
- Lysis of a membrane that is not made of phospholipids.
- A second lysing Module, or lysis by a route other than a phospholipase.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
