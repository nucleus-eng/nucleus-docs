---
title: "Report"
subtitle: "Function"
status: draft
---

# Overview

Report gives a signal a reader can see. Four Modules here do it, and they split in two by **whether the protein is the signal or only makes it**. A fluorescent protein is the signal itself and needs nothing added. A color reporter is an enzyme, and the color appears only when it meets its substrate — which means the two have to be kept apart until something brings them together.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Report takes the reporter and returns it together with a signal. Every member here expresses its reporting protein from a DNA template, so [Transcribe](../transcribe/main.md) and [Translate](../translate/main.md) come first. See [Reporter](../../modules/reporter/spec.md).

**Turning a substrate into a color is the same operation, narrowed.** It is not a separate function: it is Report, restricted to members whose signal is a color made from a substrate. See [Color Change](../../modules/color-change/spec.md).

# Substrates and products

| | Consumes | Produces | Unchanged |
| --- | --- | --- | --- |
| **Fluorescent protein** | nothing beyond expressing the protein | the protein, which is the signal | — |
| **Color-making enzyme** | its substrate, one molecule for each one turned | the colored product | the enzyme, which turns over many molecules |

**What this does to the number of dissolved particles.** A fluorescent reporter changes nothing beyond what expressing it costs, which is [Translate](../translate/main.md)'s. An enzyme that cuts one substrate molecule into two colored or colorless pieces adds one particle for each molecule it turns over, so a color reporter's contribution grows with how much substrate it gets through. No run has measured it.

# Routes

| Route | What makes the signal | Needs a substrate | Realized by |
| --- | --- | --- | --- |
| Fluorescent protein | the protein itself, read on a fluorescence channel | no | [Reporter: deGFP](../../modules/reporter-degfp/spec.md), [Reporter: mNeonGreen](../../modules/reporter-mneongreen/spec.md) |
| Color-making enzyme | the enzyme turns a colorless or differently colored substrate into a colored product | yes | [Reporter: LacZ](../../modules/reporter-lacz/spec.md) with CPRG or X-Gal; [Reporter: XylE / C23DO](../../modules/reporter-xyle/spec.md) with catechol |

# What selects a route

- **Whether a reader is available for it.** A fluorescent reporter needs a reader at its wavelengths: mNeonGreen's page asks for excitation near 506 nm and collection near 517 nm. A color reporter can be read by eye, which is why it is the one the cascades here use.
- **Whether the readout needs an off state.** An enzyme and its substrate in one compartment react at once, so there is nothing to switch on. A color route therefore holds the two apart and waits for a trigger, which in every built member is [Lyse](../lyse/main.md). A fluorescent route needs no separation, so it needs no trigger.
- **The pairing, which is chemistry and not a choice.** LacZ works with CPRG and with X-Gal, and XylE with catechol. A crossed pair, such as LacZ with catechol, is wrong chemistry and makes no color.
- **Whether the protein is expressed at all.** LacZ can be added as purified enzyme instead, and in the synthetic cells documented here it always is. So the Module's Function is attested while the expression half of it is not.

# Not yet attested

- LacZ expressed from DNA inside a synthetic cell. Every documented cell adds it as purified enzyme, at amounts that vary about sixty-fold between formats.
- A quantitative yield for any reporter: how much protein, or how much color per unit of analyte.
- A reporter whose signal is neither fluorescence nor color.
- Two reporters read side by side in one compartment without interfering.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
