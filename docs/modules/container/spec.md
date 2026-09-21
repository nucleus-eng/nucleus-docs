---
title: "Abstract: Container"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

An abstract Module: the class of things that hold other things. It is the parent of the Membranes and of the [abstract gel](../abstract-gel/spec.md), and it is the most general class this corpus names.

**The invariant is `hold`.** A Container keeps what is inside it in a defined relation to what is outside, and to the other things inside. Nothing in the class fixes what the boundary is made of, whether it is a surface or a network, or whether the inside is a volume or a position.

**This class is not new here, and two different things about it have different standing.** `compositional-biology-theory` declares `Container` as a shared parent in `signature.md`, in its own words *"a parent, not a page set"*, with `Gel`, `Membrane` and `Substrate` refining it. **That row's provenance column says it is that file's own reading, not a ruling.** What Jon did rule is narrower and is recorded as `rulings.md#D04`, applied at `6511b55`: *"a Gel and a Membrane are in the same poset as two Containers. both refine Containers."* So the two children this page fills in are ruled, and the sort declaration around them is the theory corpus's reading. This page is that structure given somewhere to live in `nucleus-docs`.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**Members are a different relation from constituents.** In `compositional-biology-theory`, `glossary.md#T34` makes Constituent a containment relation and `glossary.md#T13` makes membership a matter of what a sort classifies. **A class having members does not give it parts.** It does not give it none either: whether an abstract Module has constituents depends on whether its own class invariant names a composition, and that is decided per class rather than for abstract Modules in general.

**This class names no composition, so it has no constituents.** Its invariant is a single operation, `hold`, and an operation is not a composition. `T33` in the theory corpus makes a Composition an `⊗`/`⊞` expression giving an object as a combination of others, and nothing about `Container` gives it as a combination of anything.

:::{table} The children, and how each one holds.
| Child | How it holds | Members in this corpus |
| --- | --- | --- |
| Membrane | a closed lipid bilayer, so the inside is a volume | [London POPC](../membrane-popc/spec.md), [Base POPC/Chol](../membrane-popc-chol/spec.md), [Chicago POPC/Chol](../membrane-popc-chol-chicago/spec.md) |
| [Abstract gel](../abstract-gel/spec.md) | a polymer network, so the inside is a position rather than a volume | four, listed on that page |
| Substrate | **named in the theory corpus, not mapped here** | see below |
:::

**The two ways of holding are genuinely different and the difference has consequences.** A Membrane encloses a volume, so what it holds is separated from the outside by a barrier that something must cross. A gel fixes a position, so what it holds is still in contact with the outer solution and is separated only in space. **The corpus depends on that difference**: the colorimetric cascades put an enzyme and its substrate in one gel and rely on them not reacting, which works only because the gel holds position and not contents.

:::{attention} `Substrate` has no mapping into this corpus yet
The theory corpus names `Substrate` as the third child of `Container`. **Which pages here are its members is not settled.** [CPRG](../substrate-cprg/spec.md) and [X-Gal](../substrate-xgal/spec.md) are named Substrate and are chemicals rather than containers. [CPRG SUV](../substrate-cprg-suv/spec.md) and [CPRG GUV](../guv-cprg/spec.md) are loaded compartments and do hold something, but they hold it in a membrane, which would make them Membranes carrying a payload rather than a third kind of Container. **Naming this row is not the same as filling it**, and filling it is a judgement about the corpus rather than about the theory.
:::

# Requirements

None stated at this level. A class whose only invariant is `hold` imposes nothing on its Context that its members do not impose for their own reasons.

:::{attention} What this class requires of its Context is not settled
An abstract Module carries an abstract Context that its members refine, ruled 2026-09-17. **How much that Context term carries, and how much is left to Requirements, is `open.md#O21`** in the theory corpus, whose expressiveness half closed on Jon's ruling of 2026-09-21 and whose selection half is live.

**Saying "none stated" is a weaker claim than saying "none".** It may be that a Container requires nothing, or it may be that its Context term carries everything and the Requirements line is empty for that reason. Those are different and this page cannot tell them apart.
:::

**Three questions in the theory corpus wait on this class**, `O3`, `O8` and `O14`. They are that corpus's to close, not this one's, and nothing on this page depends on their answers. `O8` in particular, *"are formation and `hold` one operation?"*, is the reason no composition source here uses a `packing` step that would need it settled.

# Processes

None. An abstract Module names a class; the processes belong to its members.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
