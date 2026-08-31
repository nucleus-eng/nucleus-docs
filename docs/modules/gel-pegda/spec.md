---
title: "Gel: PEGDA"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

PEGDA Gel is a poly(ethylene glycol) diacrylate hydrogel crosslinked by 405 nm light in the presence of a photoinitiator. It gels only where the light falls, so its geometry is set by a projected image rather than by its container. That is what makes it a route to the spatial separation a cascade needs when two populations must be kept apart — though not the only route: a block-pattern result has also been produced in agarose, by a different method. Compare to [Alginate Gel](../gel-alginate/spec.md) and [ULGA Gel](../gel-ulga/spec.md), which set uniformly and impose no illumination, and to [PEG-Norbornene Gel](../gel-peg-norbornene/spec.md), which patterns by a different chemistry.

PEGDA crosslinks by chain-growth radical polymerization of its acrylate groups, with no separate crosslinker.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

(gel-pegda-reference-composition)=
# Reference Composition

:::{table} PEGDA precursor solution.
:label: comp-gel-pegda

| Component | Working concentration | Notes |
| --- | --- | --- |
| PEGDA monomer | not established | dissolved in PBS or deionized water |
| LAP photoinitiator | not established | lithium phenyl-2,4,6-trimethylbenzoylphosphinate; keep the solution dark until patterning |
:::

:::{attention} The concentrations are not recorded
@Editor(chicago): neither the PEGDA monomer concentration nor the LAP concentration is established. Exposure time depends on both, so the (15–30) s window below cannot be reproduced without them.
:::

A multimaterial variant mixes 1.6 wt% alginate into this precursor and crosslinks each component by its own route. What that yields is not a blended gel: the demonstrated construct is **a PEGDA frame around an alginate core**, two regions with a boundary between them. So the mixture names the ingredients and not the product — the product is a structure. See [Alginate Gel](../gel-alginate/spec.md); the CaCl₂ concentration and exposure time for the alginate step are not established.

(gel-pegda-expected-behavior)=
# Expected Behavior

## Gels

Expect a gel that forms only where the light falls, so the pattern is set by the projected image rather than by the mold. Patterning runs at 405 nm for 15 s to 30 s through a digital light processing projector, adjusted for monomer concentration, layer thickness and feature size — no single exposure time covers every condition.

Chain-growth acrylate polymerization is prone to oxygen inhibition at the gel surface and produces more heterogeneous networks than a step-growth chemistry would.

:::{warning} Not yet validated with a cascade
No result embeds a working sensing cascade in this gel. It is documented as a route to the spatial separation the [Chicago Cascade](../chicago-cascade/spec.md) Requirements section calls for, but that combination has not been run.
:::

:::{attention} No feature-size or mechanical data
No quantitative feature size, imaging methodology or mechanical-integrity measurement exists for this gel.
:::

(gel-pegda-requirements)=
# Requirements

Requires 405 nm illumination and a photoinitiator, so anything embedded must tolerate light exposure and the radical species LAP generates.

Requires the precursor solution to be protected from light until patterning.

Requires a 405 nm projector, an equipment requirement neither ionically nor thermally set gels carry.

Does not require the CPRG-after-crosslinking ordering that [PEG-Norbornene Gel](../gel-peg-norbornene/spec.md) does — the confirmed photobleaching is that chemistry's, and the PEGDA process page states it does not apply here. Whether the ordering is still worth keeping as a precaution is [an open question](../atc-cascade/spec.md).

# Processes

Prepared and patterned by [Photopatterning, PEGDA](../../processes/photopattern-pegda/main.md). [Photopattern Gel](../../processes/photopattern-gel/photopattern-gel-main.md) carries the steps this route shares with the [PEG-norbornene route](../../processes/photopattern-peg-norbornene/main.md).

# Materials

:::{table} Purchased materials.

| Name | Category | Product | Manufacturer | Part # | Link |
| --- | --- | --- | --- | --- | --- |
| PEGDA monomer | Chemical | Poly(ethylene glycol) diacrylate | Sigma-Aldrich | 437441-500ML | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/437441) |
| LAP photoinitiator | Chemical | Lithium phenyl-2,4,6-trimethylbenzoylphosphinate | Sigma-Aldrich | 900889-1G | [link](https://www.sigmaaldrich.com/US/en/product/aldrich/900889) |
| DLP projector (405 nm) | Equipment | PRO4500-92-405 optical engine | Wintech Digital Systems Technology | PRO4500-92-405 | [link](https://wintechdigital.com/products/pro4500-wintech-production-ready-optical-engine/) |
:::

# Credits

Developed by Ojaswita Pant (Chicago Node, Truby Lab).
