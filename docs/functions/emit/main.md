---
title: "Emit"
subtitle: "Function"
status: draft
---

# Overview

Emit makes a signal molecule and releases it outside the compartment that made it, where something in another compartment, or another cell, can respond to it. One Module here does it: [Emitter: IV-HSL](../../modules/emitter-ivhsl/spec.md), which expresses an enzyme that makes N-isovaleryl-L-homoserine lactone (IV-HSL), a small molecule that crosses a synthetic cell's membrane on its own.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Emit takes the emitting Module and returns it together with a signal now outside it. What makes the product a signal is that it leaves and that something else can read it, so the function is not finished while the molecule is still inside. See [Emitter](../../modules/emitter/spec.md).

# Substrates and products

| | Consumes | Produces | Unchanged |
| --- | --- | --- | --- |
| **IV-HSL** | S-adenosylmethionine (SAM) and isovaleryl coenzyme A (IV-CoA) | IV-HSL, which then leaves the compartment | the BjaI enzyme |

The emitter's reaction is dosed at 0.3 mM SAM and 0.08 mM IV-CoA. What else the reaction leaves behind is not recorded, and nor is how much IV-HSL one reaction makes.

**What this does to the number of dissolved particles.** Each molecule made leaves the compartment, so the count inside falls by what is consumed and does not rise by what is produced. The amounts are small next to a cytosol's salts and sugars. No run has measured it.

# Routes

| Route | Signal | Enzyme | Realized by |
| --- | --- | --- | --- |
| Homoserine lactone | IV-HSL | BjaI, expressed from `pT7-bjaI` | [Emitter: IV-HSL](../../modules/emitter-ivhsl/spec.md) |

# What selects a route

- **What the receiver reads.** A signal is only useful where something responds to it. IV-HSL activates expression in *E. coli* receiver cells carrying BjaR, at picomolar amounts. Its branched structure keeps it apart from many other homoserine lactones, so it can be used alongside them.
- **Whether the signal crosses the membrane.** IV-HSL leaves a synthetic cell by crossing the bilayer on its own. A signal that could not do that would have to be carried across by a pore, which is a different function and is not how this Module works.
- **The cytosol, through the construct.** `pOpen-pT7-bjaI` needs T7 transcription, as in [Base Cytosol](../../modules/base-cytosol/spec.md). See [Transcribe](../transcribe/main.md).

# Not yet attested

- How much IV-HSL one reaction makes, or how fast. Every result reads the receiver cells' response, not the signal itself.
- What the reaction leaves behind besides IV-HSL.
- A second emitting Module, or a signal other than a homoserine lactone.
- Emission into a gel or any matrix other than the solution around the cell.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
