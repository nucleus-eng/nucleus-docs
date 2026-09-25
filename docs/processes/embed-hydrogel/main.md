---
title: Hydrogel Embedding
subtitle: "Process"
status: draft
---

# Overview

Hydrogel Embedding sets a polymer network around compartments that already exist, so they are held in place instead of settling or diffusing apart. The gel dissolves into the outer solution the compartments were already suspended in, so it adds a position without adding a barrier.

Its two instances:

- [Hydrogel Embedding: Alginate](../embed-alginate-hydrogel/main.md) — sodium alginate set ionically by calcium.
- [Hydrogel Embedding: ULGA](../embed-ulga-hydrogel/main.md) — ultra-low-gelling agarose set by cooling.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Written 2026-09-24 because three whiteboards reached for it
The DevStudio day-one boards label this step `Gel embed`, without naming a chemistry. Both chemistries had a page and the thing they are chemistries of did not, which is the same gap [Encapsulation](../encapsulate/main.md) had and the opposite of [Photodevelop Gel](../photodevelop-gel/photodevelop-gel-main.md), which has carried its parent page all along.
:::

# What every instance shares

**The gel holds position, not contents.** What is embedded stays in contact with the phase around it, because the gel *is* that phase with a polymer in it. [Container](../../modules/container/spec.md) states the three ways of holding and this is the middle one: a membrane encloses a volume, a solution separates nothing, a gel fixes a place.

**That is what the colorimetric cascades depend on.** An enzyme and its substrate can sit in one gel and not react, because the gel separates them in space and not by a boundary. A route that enclosed its contents would have no off state to break.

**The result keeps its parts' compartments, so this process packs.** A liposome embedded in a gel is still a liposome.

**No instance illuminates its contents.** This is the distinction [Photodevelop Gel](../photodevelop-gel/photodevelop-gel-main.md) draws against itself: the photodeveloped routes impose UV on whatever is present at crosslinking, and neither route here does. A UV-sensitive payload can be embedded and cannot be photopatterned.

# What the instances do not share

| | Alginate | ULGA |
| --- | --- | --- |
| Setting trigger | ionic, calcium crosslink | thermal, cooling |
| What must be tolerated | the calcium source | the melt temperature on the way in |
| Reversible | not by temperature | yes, the gel melts |

**The setting trigger is the refinement axis and no field holds it.** [Gel](../../modules/gel/spec.md)'s composition source records that gap directly, and this table is the same finding stated as a process.

:::{attention} A third chemistry is in use and has no page
The pH path embeds in **low-gelling agarose**, which is not ULGA: the two gel at different temperatures and are ordered as different products. [Gel: LGA](../../modules/gel-lga/spec.md) is the module; **no embedding process is written for it**, so a composition using it has this parent page and no instance to name.
:::

# Requirements

Requires an outer solution for the polymer to dissolve into, and its osmolarity is the compartments' requirement rather than the gel's. See [Outer Solution](../../modules/outer-solution/spec.md).

Requires that whatever is embedded tolerates the setting trigger. **Neither trigger is neutral**: one adds calcium, the other requires the payload to survive the temperature at which the polymer is still liquid.

# Modules

- [Gel](../../modules/gel/spec.md) — the class this process produces
- [Gel: Alginate](../../modules/gel-alginate/spec.md), [Gel: ULGA](../../modules/gel-ulga/spec.md), [Gel: LGA](../../modules/gel-lga/spec.md)

# Processes

- [Hydrogel Embedding: Alginate](../embed-alginate-hydrogel/main.md)
- [Hydrogel Embedding: ULGA](../embed-ulga-hydrogel/main.md)
