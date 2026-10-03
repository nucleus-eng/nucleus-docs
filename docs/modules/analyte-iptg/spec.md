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
No induction concentration or working range is documented. @Editor: supply the IPTG concentration if this Module is used, or leave the bands empty and say so.
:::

# Requirements

Requires a [LacI-IPTG Detector](../detector-laci-iptg/spec.md) to be sensed at all.

:::{attention} Transport across a bilayer is not documented
@Editor: establish whether IPTG crosses a POPC bilayer unaided or needs a transport route. [aTc](../analyte-atc/spec.md) crosses unaided, which is why its sensing cell needs no pore.
:::

# Processes

None. An analyte is supplied to an assay rather than produced by a Nucleus process.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
