---
title: "Sense"
subtitle: "Function"
status: draft
---

# Overview

Sense takes something from outside and turns it into a difference in what gets made. Six Modules here do it, by four mechanisms. **The analyte does not fix the mechanism**: two of the six sense the same molecule, one by switching a promoter on and one by letting go of a promoter it was holding off.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Sense takes the detector and its analyte, and returns the detector with a gene's expression changed. **The change is in what gets made, not in the detector**, so the signal a detector produces is whatever sits downstream of it, and every member leaves that choice to the composer.

**What the detector restricts is written in brackets**, which is the [Detector](../../modules/detector/spec.md) class's own notation: the analyte, the mechanism, or the pair of analyte and effector.

# Substrates and products

**The analyte is not consumed.** No member here breaks its analyte down or uses it up: it binds, or it changes the shape of something, and it is still there afterwards. What is consumed is whatever the downstream gene costs to express, which belongs to [Transcribe](../transcribe/main.md) and [Translate](../translate/main.md) rather than here.

| | Takes | Changes | Unchanged |
| --- | --- | --- | --- |
| **Every member** | its analyte, from the solution it sits in | how much of the downstream gene is expressed | the analyte, and the detector's own parts |

**What this does to the number of dissolved particles.** Nothing directly. The expression it turns on or off does change the count, and that change is Transcribe's and Translate's. No run has measured it.

# Routes

| Mechanism | What the analyte does | Analyte | Realized by |
| --- | --- | --- | --- |
| Transcriptional activator | binds the activator, which then switches its promoter on | 3OC6-HSL | [Detector: 3OC6-HSL (LuxR)](../../modules/detector-3oc6-hsl/spec.md) |
| Repressor | binds the repressor, which lets go of the DNA it was holding | 3OC6-HSL | [Detector: 3OC6-HSL (EsaR)](../../modules/detector-esar/spec.md) |
| Repressor | as above | IPTG | [Detector: LacI-IPTG](../../modules/detector-laci-iptg/spec.md) |
| Repressor | as above | aTc | [Detector: tetR-aTc](../../modules/detector-tetr-atc/spec.md) |
| Riboswitch | binds the RNA itself, which changes shape so the message can be translated | theophylline | [Detector: Theophylline](../../modules/detector-theophylline/spec.md) |
| Toehold switch | acid frees a trigger strand from a duplex, and the trigger opens the switch | H⁺, at pH ≤ 6.5 | [Detector: pH-Sensing](../../modules/detector-ph/spec.md) |

# What selects a route

- **The analyte, but not on its own.** Both 3OC6-HSL detectors sense the same molecule and do opposite things with it: LuxR switches a promoter on, and EsaR lets one go. So a composition that needs the inverted logic picks the mechanism, not the analyte.
- **Where the analyte is, and whether it can reach the detector.** A detector inside a synthetic cell senses only what crosses the membrane. 3OC6-HSL crosses on its own, so it needs nothing added. IPTG does not, and its detector's page asks for a pore. The pH detector asks either to be left unencapsulated, or for a way to let H⁺ across.
- **Which cytosol, through the construct.** Most of these need T7 transcription, as in [Base Cytosol](../../modules/base-cytosol/spec.md). The LuxR detector needs sigma-70 transcription instead, as in [S30 Lysate](../../modules/s30-lysate/spec.md), and its page says T7 will not drive it. See [Transcribe](../transcribe/main.md).
- **Only one mechanism is a class.** Three members share the repressor mechanism, and the thing they share has a page of its own: [Repressor Detector](../../modules/repressor-detector/spec.md). The other three mechanisms have one member each, so nothing yet generalizes them.
- **Where the mechanism acts.** Three of the four act on transcription, by holding or releasing a promoter. The riboswitch and the toehold switch act on the message after it is made, so they gate [Translate](../translate/main.md) instead.

# Not yet attested

- A detection limit, or a dose-response curve, for most members.
- Any member sensing an analyte that is not a small molecule or a proton.
- A member whose downstream effect is anything but the expression of a gene.
- Two detectors sensing two analytes in one compartment without interfering.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
