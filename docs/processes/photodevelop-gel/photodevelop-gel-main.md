---
title: Photodevelop Gel
status: draft
---

# Overview

Photopatterning crosslinks a light-sensitive polymer precursor into a gel only where light falls, so the gel's geometry comes from a projected image rather than from its container. It is the route Nucleus uses when populations have to be held apart in defined regions rather than dispersed through one matrix.

This page covers what the two chemistries share. Each has its own page, because the precursor, the crosslinking mechanism and what the exposure does to the payload all differ:

- [Photodevelopment, PEGDA](../photodevelop-pegda/main.md) — radical polymerization of acrylate groups.
- [Photodevelopment, PEG-Norbornene](../photodevelop-peg-norbornene/main.md) — step-growth thiol-ene addition, with a separate thiol crosslinker.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Neither chemistry has a recorded precursor concentration
Exposure time depends on monomer concentration, layer thickness and feature size, and none of the three is established for either route. Both child pages carry the same gap. Treat the exposure figures on them as the conditions of one run rather than as a specification.
:::

# The shared procedure

Both routes run the same four steps. What changes between them is what goes into step 1 and how long step 3 takes.

1. **Dissolve the precursor** in an aqueous buffer, and add the PEG4SH crosslinker and the LAP photoinitiator. Both routes use PEG4SH.
2. **Protect the solution from light** until the moment of patterning. A photocrosslinking precursor begins to react on ambient exposure.
3. **Expose the pattern** through a digital light processing projector at 405 nm, for a time adjusted to the precursor concentration, layer thickness and target feature size.
4. **Confirm the pattern** by microscopy against the intended design, and confirm structural integrity by visual or mechanical inspection.

# What the two chemistries do not share

| | PEGDA | PEG-Norbornene |
| --- | --- | --- |
| Mechanism | radical polymerization of acrylates | step-growth thiol-ene |
| Oxygen inhibition at the surface | prone | less prone |
| Network uniformity | more heterogeneous | more uniform |
| Effect on pre-loaded CPRG | none recorded | **bleaches it** — see the child page |

The last row is the one that decides which route a colorimetric cascade can use, and it is the reason these are two pages rather than one page with a parameter.

# Requirements

Requires a 405 nm light source, normally a DLP projector. This is the only gel-forming route in this documentation with an equipment requirement beyond ordinary labware.

Requires that anything embedded tolerates light exposure and the radical species the photoinitiator generates. Neither [Alginate Hydrogel Embedding](../embed-alginate-hydrogel/main.md) nor [ULGA Hydrogel Embedding](../embed-ulga-hydrogel/main.md) illuminates its contents at all, so this is the constraint that distinguishes the photodeveloped routes from the other two.

# Modules

- [Gel: PEGDA](../../modules/gel-pegda/spec.md)
- [Gel: PEG-Norbornene](../../modules/gel-peg-norbornene/spec.md)
