---
title: "Analyte: IPTG"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Isopropyl β-d-1-thiogalactopyranoside (IPTG) is the inducer the [LacI-IPTG Detector](../detector-laci-iptg/spec.md) responds to. It binds LacI allosterically, causing the repressor to release the `lacO` operator and recovering expression of the downstream gene.

**This is an Analyte, so it is not a constituent of anything.** It reaches a sensing cell from outside, after the cell is closed.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

:::{table} Working concentrations.
| Band | Value | Source |
| --- | --- | --- |
| Induction | not documented | — |
| Transport across a bilayer | not documented | — |
:::

:::{attention} No dose figures are recorded
[LacI-IPTG Detector](../detector-laci-iptg/spec.md) describes the mechanism but states no induction concentration or working range, and the Module is not composed into any DevCells demo. @Editor: supply the IPTG concentration if this Module is used, or leave the bands empty and say so.
:::

# Requirements

Requires a [LacI-IPTG Detector](../detector-laci-iptg/spec.md) to be sensed at all.

**Whether it requires a transport route is not established.** Nothing in the corpus says whether IPTG crosses a POPC bilayer unaided. Compare [aTc](../analyte-atc/spec.md), which does, and which is the reason its sensing cell needs no pore.

# Processes

None. An analyte is supplied to an assay rather than produced by a Nucleus process.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
