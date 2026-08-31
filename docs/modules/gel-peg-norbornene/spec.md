---
title: "Gel: PEG-Norbornene"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

PEG-Norbornene Gel is a photocrosslinked hydrogel formed by step-growth thiol-ene chemistry: 4-arm PEG-norbornene, a PEG4SH crosslinker, and a photoinitiator. Like [PEGDA Gel](../gel-pegda/spec.md) its geometry is set by projected light, but through a different mechanism, and it is less prone to oxygen inhibition at the gel surface. Compare to [Alginate Gel](../gel-alginate/spec.md) and [ULGA Gel](../gel-ulga/spec.md), which set uniformly and never illuminate their contents.

It is the newer of the two photodevelopment chemistries. Like the PEGDA route it exposes the payload to UV, so neither can carry pre-loaded CPRG through crosslinking.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

(gel-peg-norbornene-reference-composition)=
# Reference Composition

:::{table} PEG-norbornene precursor solution.
:label: comp-gel-peg-norbornene

| Component | Working concentration | Notes |
| --- | --- | --- |
| 4-arm PEG-norbornene | not established | the backbone |
| PEG4SH | not established | thiol crosslinker, shared with the [PEGDA route](../gel-pegda/spec.md) |
| LAP photoinitiator | not established | lithium phenyl-2,4,6-trimethylbenzoylphosphinate |
:::

:::{attention} No composition is recorded
@Editor(chicago): no concentration, arm ratio, exposure time or light source is established for this gel. Everything below describes what it does, not how to make it. It needs a composition and a process page before it can be used at the bench.
:::

(gel-peg-norbornene-expected-behavior)=
# Expected Behavior

## Gels

Expect a gel that forms where the light falls, with a more uniform network than a chain-growth acrylate gives and less inhibition at the surface where oxygen is present.

A spatial-patterning result is confirmed: a block-pattern color change, first shown in agarose, was repeated with a PEG-norbornene outer gel and LacZ added on top, with the color change still visible after roughly 1.5 h.

:::{warning} UV exposure bleaches CPRG
[CPRG](../substrate-cprg-suv/spec.md) is UV-sensitive, and this gel's crosslinking step imposes UV on the payload. The side-by-side comparison behind the finding — exposed sample visibly bleached against an unexposed control — was run on this chemistry, but the constraint follows from the UV and applies to [PEGDA](../gel-pegda/spec.md) equally. It does not apply to alginate or ULGA, which use no UV.

The workaround inverts the order: pre-add LacZ to the gel, crosslink, then add CPRG as a free dye. That path does not use the CPRG Substrate SUV module at all, so it is a different cascade rather than the same one in a different gel.
:::

(gel-peg-norbornene-requirements)=
# Requirements

Requires UV illumination and a photoinitiator, so anything embedded must tolerate light exposure and the radical species it generates.

Requires the PEG4SH crosslinker, as the PEGDA route does.

**Requires that CPRG is not pre-loaded into liposomes.** This is the one requirement here that rules a whole cascade out rather than constraining it: the two-liposome colorimetric readout cannot be run in this gel as written.

# Processes

Formed by [Photodevelopment, PEG-Norbornene](../../processes/photodevelop-peg-norbornene/main.md), which is a stub — it records the chemistry and the CPRG incompatibility but no precursor recipe or exposure conditions. [Photodevelop Gel](../../processes/photodevelop-gel/photodevelop-gel-main.md) carries the steps this route shares with [Photodevelopment, PEGDA](../../processes/photodevelop-pegda/main.md).

# Credits

Developed by the Chicago Node.
