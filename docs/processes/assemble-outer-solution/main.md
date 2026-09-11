---
title: Assemble Outer Solution
subtitle: "Process"
status: draft
---

# Overview

Assemble Outer Solution mixes the salts, buffer and sugar that synthetic cells are suspended in. It is one of the two instances of [Assemble Aqueous Solution](../assemble-aqueous-solution/assemble-aqueous-solution-main.md), so it mixes into a single compartment, and it reserves no headroom — unlike [Assemble Cytosol](../assemble-cytosol/assemble-cytosol-main.md), it is made to a composition and used.

The outer solution does two jobs at once, and the second is easy to overlook. It sets the osmotic environment the cells sit in, and it is also **what the gel is made from** — a hydrogel polymer is dissolved into this solution rather than into water, so the gel has no osmolarity of its own and inherits this one.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Composition

Three formulations are attested, and they are not interchangeable — each is matched to the cytosol it surrounds.

:::{table} Outer solutions in use.
:label: comp-outer-solutions

| Configuration | Composition | Osmolarity | Used with |
| --- | --- | --- | --- |
| London | Potassium L-glutamate 578 mM · HEPES pH 7.4 72 mM · Glucose 300 mM | ≈ 920 mOsm | [S30 Lysate](../../modules/s30-lysate/spec.md) cells, in [ULGA Gel](../../modules/gel-ulga/spec.md) |
| Chicago | Tris-HEPES buffer stock (0.5 M Tris base, 1.7 M HEPES, pH ≈ 7.4) at 42.5% (v/v) in water, plus energy solution | ≈ 1180 mOsm | [Base Cytosol](../../modules/base-cytosol/spec.md) cells, in [Alginate Gel](../../modules/gel-alginate/spec.md) |
| High-glucose | Glucose 1200 mM · CaCl₂ 0.1 mM | ≈ 1200 mOsm | Base Cytosol cells where CPRG retention matters |
:::

:::{attention} The energy solution is not specified
@Editor(chicago): the Chicago configuration supplements the buffer with an energy solution whose contents are not recorded anywhere in this documentation. See [Chicago Chassis](../../modules/chicago-chassis/spec.md).
:::

# Requirements

**Requires matching to the interior it will surround.** [AHL Sensing Cell](../../modules/ahl-sensing-cell/spec.md) matches inner to outer at about 920 mOsm; a mismatch drives encapsulated contents across the bilayer before the system does anything else. Match empirically with a vapor-pressure osmometer where the figure is not already established.

**Above roughly 1200 mOsm, CPRG stops leaking.** In glucose-based outer solutions, dye leakage from loaded liposomes falls sharply above that osmolarity. That is the reason for the high-glucose configuration: leaked CPRG meets external enzyme with no lysis and raises background before the cascade fires. See [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md).

**Whatever dissolves into it inherits its osmolarity.** A gel polymer — ULGA, alginate, or a photodevelopable precursor — is dissolved into this solution, so the gel imposes no osmotic environment of its own. Changing the outer solution changes the gel.

# Processes

Every process that takes an outer solution as an operand:

- [Hydrogel Embedding: ULGA](../embed-ulga-hydrogel/main.md)
- [Hydrogel Embedding: Alginate](../embed-alginate-hydrogel/main.md)
- [Photodevelop Gel](../photodevelop-gel/photodevelop-gel-main.md)
