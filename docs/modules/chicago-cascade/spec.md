---
title: "Chicago Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Chicago Cascade is the top-level, multiplexed Chicago demo node: the attempted merge of the [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md) and the [aTc Sensing Cell](../atc-sensing-cell/spec.md) into one combined cascade, with both sensing legs feeding a shared [PLA1 Lysis Module](../effector-pla1/spec.md) trigger and [LacZ Reporter Module](../reporter-lacz/spec.md) colorimetric readout. The goal is multiplexed detection: theophylline and aTc sensed side by side in the same reaction, each independently driving a visible color change.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Sensing legs cannot currently be combined
Each sensing leg works standalone: the [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md) and the [aTc Sensing Cell](../atc-sensing-cell/spec.md) are each confirmed working on their own. They cannot currently be combined into one cascade: both depend on the same LacZ/CPRG readout, which theophylline is understood to inhibit. A combined multiplexed reaction has not been demonstrated. Per the source transcript, even very low amounts of theophylline were "kind of inhibiting that conversion." This is a hedged, source-quoted finding, not a fully characterized mechanistic claim. See the [Theophylline Sensing Module](../detector-theophylline/spec.md#requirements) and [aTc Sensing Module](../detector-tetr_atc/spec.md#requirements) Requirements sections, and the [LacZ Reporter Module](../reporter-lacz/spec.md#requirements) Requirements section, for the same constraint stated at each affected Module. This page does not repeat the underlying rationale — it documents the cascade-level consequence.
:::

This does not describe either individual leg. The [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md) and [aTc Sensing Cell](../atc-sensing-cell/spec.md) pages each document their own standalone-confirmed status, independent of this page. Only the combined, multiplexed cascade — both sensing legs sharing one readout — cannot currently be combined.

:::{note} Cross-module compatibility tracking
A general cross-module compatibility matrix does not currently exist. This page documents only the specific theophylline/LacZ-CPRG relationship that affects this cascade — it does not attempt a general-purpose compatibility framework.
:::

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    THEO["Theophylline Sensing Cell"]
    ATC["aTc Sensing Cell"]
    PLA1["Effector: PLA1"]
    LACZ["Reporter: LacZ"]
    CASCADE(("Chicago Cascade"))

    THEO --x CASCADE
    ATC --x CASCADE
    PLA1 -.-> CASCADE
    LACZ -.-> CASCADE

    classDef chicago fill:#e3f0f8,stroke:#0072B2,color:#063a57;
    class THEO,ATC,PLA1,LACZ,CASCADE chicago;
    style CASCADE stroke-dasharray: 5 5

    click THEO "/docs/modules/theophylline-sensing-cell/spec"
    click ATC "/docs/modules/atc-sensing-cell/spec"
    click PLA1 "/docs/modules/effector-pla1/spec"
    click LACZ "/docs/modules/reporter-lacz/spec"
```

## Composition — Not Applicable (Merge Blocked)

:::::{tab-set}

::::{tab-item} Cytosol

No combined reference composition exists, and none is given here — not even a hypothetical one — for two reasons. First, the merge is blocked before reaching a formulation step: the multiplexed cytosol was never built. Second, a hypothetical recipe would have nothing real to flatten one level deep into: neither leg's own cytosol has a complete, numbered composition yet — the [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md#reference-composition) page flags its PLA1-linked construct as not yet identified, and the [aTc Sensing Cell](../atc-sensing-cell/spec.md#reference-composition) page flags its per-component reaction table as not yet documented. Inventing working concentrations for a recipe that has never been run, on top of constituents that do not yet have their own numbers, would misrepresent this as more real than it is. Each leg's own cytosol is documented on its own Sensing Cell page: [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md#reference-composition), [aTc Sensing Cell](../atc-sensing-cell/spec.md#reference-composition).

::::

::::{tab-item} Membrane

Both feeder legs use the same [Chicago Chassis](../chicago-chassis/spec.md) membrane (9:1 POPC:cholesterol, GUV scale). If the multiplex is unblocked in the future, this membrane would carry over unchanged — the blocking issue is specific to the LacZ/CPRG readout chemistry, not the membrane.

::::

:::::

## Process

No combined assembly process exists for this cascade — it has not been built, because the readout-level incompatibility blocks the merge before an assembly process would be needed. See [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md) and [aTc Sensing Cell](../atc-sensing-cell/spec.md) for each leg's own process status.

## Requirements

The Chicago Cascade cannot currently combine the [Theophylline Sensing Module](../detector-theophylline/spec.md) and [aTc Sensing Module](../detector-tetr_atc/spec.md) sensing pathways in the same reaction: both depend on the same [LacZ Reporter Module](../reporter-lacz/spec.md) LacZ/CPRG readout, which theophylline is understood to inhibit. A combined multiplexed reaction has not been demonstrated. See each constituent Module's own Requirements section for the same constraint stated at that level:

- [Theophylline Sensing Module Requirements](../detector-theophylline/spec.md#requirements)
- [aTc Sensing Module Requirements](../detector-tetr_atc/spec.md#requirements)
- [LacZ Reporter Module Requirements](../reporter-lacz/spec.md#requirements)

# Constituent Modules

- [Theophylline Sensing Cell](../theophylline-sensing-cell/spec.md) — confirmed working standalone; blocked from combining with the aTc Sensing Cell in this cascade
- [aTc Sensing Cell](../atc-sensing-cell/spec.md) — confirmed working standalone; blocked from combining with the Theophylline Sensing Cell in this cascade
- [PLA1 Lysis Module](../effector-pla1/spec.md) — shared lysis trigger, intended to couple sensing to readout in the combined cascade
- [LacZ Reporter Module](../reporter-lacz/spec.md) — shared colorimetric readout; the specific point of incompatibility between the two sensing legs

# Implementations

No Implementation page exists for this cascade. Building one is blocked by the mutual-exclusion requirement above — a combined Implementation would need either a resolved readout incompatibility or a redesigned cascade (e.g. separate readouts per sensor) before it could be authored.

# Credits

- b.next
