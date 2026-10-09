---
title: Functions
description: What Modules do. One page per operation, with every Module that performs it, the routes it takes, and what it consumes and produces.
---

# Overview

A Function page documents one operation that Modules perform, such as transcribing DNA. A Module page, listed under [Modules](../modules/modules-main.md), documents one thing. A Function page documents one operation across every Module that performs it: the routes the operation takes, what selects a route, and what the operation consumes and produces.

**Something a Module does, not something you do.** Encapsulating cells or reading a plate is a step you run at the bench, and it has a page under [Processes](../processes/processes-main.md). A Function is what a Module does once it is built: a cytosol transcribes, a pore lets cargo across, an enzyme breaks a membrane.

**Every declared operation is listed here, with its page or the reason it has none.** A row with neither is a gap.

# Functions

| Function | What it does | Page |
| --- | --- | --- |
| Transcribe | Makes RNA from a DNA template. | [Transcribe](./transcribe/main.md) |
| Translate | Makes protein from an RNA. | [Translate](./translate/main.md) |
| Sense | A detector responds to its analyte with a signal. | To be written |
| Report | A reporter gives a signal a reader can see. A color reporter does it by turning a substrate into a color, and that is covered on the same page. | To be written |
| Lyse | Breaks a membrane and releases what it held. | To be written |
| Transport | Moves cargo across a membrane through a pore: down a gradient, or against one with energy. | To be written |
| Emit | Releases a signal molecule outside the compartment. | To be written |
| Degrade | Breaks down a protein, an RNA or a DNA mixed with it. | To be written |
| Regenerate | Turns a spent nucleotide back into its usable form, such as ADP into ATP. | To be written |
| Hold | Keeps what is inside a container in a fixed relation to what is outside it. | To be written |
| Hydrolyze pyrophosphate | Splits pyrophosphate into two phosphates. | To be written |
| Hydrolyze ATP | Splits ATP into ADP and phosphate. | No page yet: no Module lists an enzyme that does it, so it has no attested member. Base Cytosol is only inferred to do it. |
| Encapsulate | Closes a membrane around a solution, inside another solution. | No Function page: it is something you do. Its routes are processes, under [Encapsulation](../processes/encapsulate/main.md). |
| Observe | Reads something and yields an observation. | No Function page: it is something you do. See [Assay](../processes/assay/main.md). |
| Anneal | Joins two complementary DNA strands into a duplex. | No Function page: it is a bench step, [Anneal pH-Responsive Trigger Duplex](../processes/anneal-ph-trigger-duplex/main.md). Inside a cell the duplex comes apart instead, and that is Sense. |
| Join | Joins two polymers end to end. The order matters. | No Function page: it is something you do, and no recorded run uses it. |

Express is Transcribe followed by Translate. It is not a function of its own, so it has no row.
