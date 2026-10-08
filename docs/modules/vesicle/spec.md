---
title: "Vesicle"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [GUV](../guv/spec.md), [Liposome](../liposome/spec.md), [LUV](../luv/spec.md), [Substrate Carrier](../substrate-carrier/spec.md), [SUV](../suv/spec.md).
<!-- /gen:position -->

A lipid bilayer closed around an aqueous interior. **This is the general term**, and two independent axes narrow it: **size and lamellarity** give [GUV](../guv/spec.md), [SUV](../suv/spec.md) and [LUV](../luv/spec.md); **material** gives [Liposome](../liposome/spec.md), whose sibling would be a polymersome.

**The two axes do not nest.** A GUV may be a liposome or a polymersome, so neither axis is a parent of the other and a member may take one parent from each.

**Every vesicle documented here is a liposome**, so the material axis has one value today and does no work yet.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**A membrane around a payload, and nothing more.** Every narrowing below this — which route makes it, what size it is, what the bilayer is made of — belongs to a child. Members differ in both the membrane and the interior.

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    OUTER_SOLUTION["Outer solution"]
    MEMBRANE["Membrane"]
    PAYLOAD["Payload"]

    P1_CLOSE_THE_BILAYER_AROUND_THE_PAYLOAD_0(["Encapsulation (packing)"])
    VESICLE["Vesicle"]

    MEMBRANE --> P1_CLOSE_THE_BILAYER_AROUND_THE_PAYLOAD_0
    PAYLOAD --> P1_CLOSE_THE_BILAYER_AROUND_THE_PAYLOAD_0
    OUTER_SOLUTION --> P1_CLOSE_THE_BILAYER_AROUND_THE_PAYLOAD_0
    P1_CLOSE_THE_BILAYER_AROUND_THE_PAYLOAD_0 --> VESICLE


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class OUTER_SOLUTION,MEMBRANE,PAYLOAD leaf;
    class VESICLE composed;
    class P1_CLOSE_THE_BILAYER_AROUND_THE_PAYLOAD_0 process;

    click OUTER_SOLUTION "/docs/modules/outer-solution/spec"
    click MEMBRANE "/docs/modules/membrane/spec"
    click P1_CLOSE_THE_BILAYER_AROUND_THE_PAYLOAD_0 "/docs/processes/encapsulate/main"
    click VESICLE "/docs/modules/vesicle/spec"
```

::::
<!-- /gen:composition-diagram -->


::::{tab-item} Membrane

This class does not fix the bilayer. Which lipids, and in what ratio, belongs to a member of [Membrane](../membrane/spec.md), and which member belongs to a child of this class.

:::{table} The bilayer, unnarrowed at this level.
:label: comp-vesicle-membrane

| Component | Target percentage (%) |
| --- | --- |
| not fixed here | — |
:::

::::

:::::

# Expected Behavior

A vesicle holds its interior apart from the outside until something breaches the bilayer. **The class says nothing about what that is** — lysis, a pore, or no breach at all.

# Requirements

Requires a membrane that closes, and an interior to close around. **Whether forming the boundary and holding something in it are one operation or two is unsettled**, which is why this class declares no parent.

**Requires the osmotic difference across the membrane to stay within a tolerance of a designed value, for as long as the membrane holds.** The difference is the inside minus the outside. It is set when the vesicle forms, and it goes on mattering afterwards: a reaction inside can change the inside, and anything added outside changes the outside. A lipid bilayer lets water through and holds most solutes back, so a difference moves water. Too small a difference and the vesicle shrinks; too large a one and it ruptures and its contents leak.

**The tolerance belongs to the vesicle, not to either solution: it is what the membrane survives.** This class states neither number. Each member states its own designed difference, and its tolerance where one was measured. [Base Cell](../base-cell/spec.md) runs its inside 100 mOsm/kg to 150 mOsm/kg above its outside, measured as the vesicles form ([Nucleus Base Cell Testing](https://devnotes.nucleus.engineering/articles/base-cell-01)). No measurement yet says how long a window holds.

# Processes

- [Encapsulation](../../processes/encapsulate/main.md) — the abstract operation. Each size class names one of its three routes

# Constituent Modules

- [Membrane](../membrane/spec.md) — the bilayer that closes
- **Payload** — what it closes around, and it has no class page: a cytosol, a substrate or a dye, depending on the member

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
