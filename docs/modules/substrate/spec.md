---
title: "Substrate"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [`substrate-cprg`](../substrate-cprg/spec.md), [`substrate-xgal`](../substrate-xgal/spec.md).
<!-- /gen:position -->

A class: the chromogenic reagent a reporter enzyme turns over.

Every member is held and consumed. It is not a Module that acts, and it declares no step: a substrate is put somewhere and waits for the enzyme to reach it.

A vesicle that carries one is not a member. [Substrate Carrier](../substrate-carrier/spec.md) holds those, and the distinction is the one `SubstrateCarrier := Vesicle{Substrate}` makes: the carrier is a vesicle, the payload is this class.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [CPRG](../substrate-cprg/spec.md) | Chlorophenol red-beta-D-galactopyranoside. Yellow to purple on cleavage by LacZ. |
| [X-Gal](../substrate-xgal/spec.md) | Colorless to blue on cleavage by LacZ. |

# Expected Behavior

Any member changes color when the reporter enzyme reaches it, and not before. Keeping the two apart until the readout step is what makes the change a signal rather than a background.

# Requirements

Every member requires a reporter enzyme that cleaves it, and requires to be kept away from that enzyme until the readout step.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
