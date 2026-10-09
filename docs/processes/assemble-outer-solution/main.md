---
title: Assemble Outer Solution
subtitle: "Process"
status: draft
---

# Overview

Assemble Outer Solution mixes the salts, buffer and sugar that synthetic cells are suspended in. It is one of the two instances of [Assemble Solution](../assemble-solution/assemble-solution-main.md), so it mixes into a single compartment, and it reserves no headroom — unlike [Assemble Cytosol](../assemble-cytosol/assemble-cytosol-main.md), it is made to a composition and used.

The outer solution does two jobs at once, and the second is easy to overlook. It sets the osmotic environment the cells sit in, and it is also **what the gel is made from** — a gel polymer is dissolved into this solution rather than into water, so the gel has no osmolarity of its own and inherits this one.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Composition

Four formulations are attested, and they are not interchangeable — each is matched to the cytosol it surrounds.

:::{table} Outer solutions in use.
:label: comp-outer-solutions

| Configuration | Composition | Osmotic concentration | Used with |
| --- | --- | --- | --- |
| Glutamate | Potassium L-glutamate 578 mM · HEPES pH 7.4 72 mM · Glucose 300 mM | ≈ 920 mOsm | [S30 Lysate](../../modules/s30-lysate/spec.md) cells, in [ULGA Gel](../../modules/gel-ulga/spec.md) |
| Tris-HEPES | Tris-HEPES buffer stock (0.5 M Tris base, 1.7 M HEPES, pH ≈ 7.4) at 42.5% (v/v) in water, plus an [energy solution](../../modules/outer-solution-tris-hepes/spec.md) of ten components | ≈ 1180 mOsm | [Base Cytosol](../../modules/base-cytosol/spec.md) cells, in [Alginate Gel](../../modules/gel-alginate/spec.md) |
| Glucose-HEPES | Glucose 400 mM · HEPES-KOH pH 7.6 1 M | not recorded | [Base Cytosol](../../modules/base-cytosol/spec.md) cells, in the aTc path's [PEG-Norbornene Gel](../../modules/gel-peg-norbornene/spec.md) |
| High-glucose | Glucose 1200 mM · CaCl₂ 0.1 mM | ≈ 1200 mOsm/L by recipe; not recorded as read | Base Cytosol cells where CPRG retention matters |
:::

@Editor: for the glutamate row, 578 mM glutamate, 72 mM HEPES and 300 mM glucose add to 950 mOsm/L as written, and to about 1560 mOsm/L when each ion of the salts counts. Neither is 920. For the Tris-HEPES row, 0.5 M Tris with 1.7 M HEPES adds to about 2200 mOsm/L as written. 42.5% of 2200 is 935, and 42.5% of the 2700 that the Base Cell page gives is 1148. The row gives 1180.

# Requirements

**Requires matching to the interior it will surround.** [SensorCell[3OC6-HSL ⟶ PLA1]](../../modules/ahsl-sensing-cell/spec.md) matches inner to outer at about 920 mOsm; a mismatch drives encapsulated contents across the bilayer before the system does anything else. Match empirically with a vapor-pressure osmometer where the figure is not already established.

**Above roughly 1200 mOsm, CPRG stops leaking.** In glucose-based outer solutions, dye leakage from loaded liposomes falls sharply above that osmotic concentration. That is the reason for the high-glucose configuration: leaked CPRG meets external enzyme with no lysis and raises background before the cascade fires. See [Substrate SUV: CPRG](../../modules/substrate-cprg-suv/spec.md).

**Osmolarity is additive, and the solution sets it.** Every component contributes osmolytes, so a gel's osmolarity is the sum of the solution's and the polymer's own. A gel polymer — ULGA, alginate, or a photodevelopable precursor — is dissolved into this solution at a concentration whose contribution is negligible: about 1% (w/v) agarose adds on the order of 0.1 mOsm/L against a 920 mOsm background. So the polymer is not osmotically inert, only negligible, and changing the outer solution changes the gel. @Editor: PEGDA575 at 20% (w/v) is about 350 mOsm/L, which is not negligible. Which precursor does "a photodevelopable precursor" name? The sentence holds for PEG-norbornene and not for PEGDA575.

# Processes

Every process that takes an outer solution as an operand:

- [Embedding: Thermal Setting](../embed-thermal-setting/main.md)
- [Embedding: Ionic Crosslinking](../embed-ionic-crosslinking/main.md)
- [Embedding: Photodevelopment](../embed-photodevelopment/main.md)
