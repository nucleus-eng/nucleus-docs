---
title: "Gel: Alginate"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

Alginate Gel is a ~1% (w/v) sodium alginate hydrogel, crosslinked ionically by divalent calcium, used as the matrix that holds synthetic cells and reporter liposomes in fixed relation to one another. It is the format the Chicago colorimetric demo runs in. Compare to [ULGA Gel](../gel-ulga/spec.md), which reaches the same result through a thermal set rather than an ionic one, and to [PEGDA Gel](../gel-pegda/spec.md), whose geometry is set by projected light rather than by its container.

Alginate is the gentlest of the four on its contents: it sets at room temperature, in the dark, with no radicals and no heat.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

(gel-alginate-reference-composition)=
# Reference Composition

:::{table} Alginate gel, as prepared.
:label: comp-gel-alginate

| Component | Working concentration | Notes |
| --- | --- | --- |
| Sodium alginate | ~1% (w/v) | dissolved in a buffer compatible with the liposomes being embedded — normally their own outer solution |
| Calcium chloride (CaCl₂) | 200 mM | applied as a separate crosslinking solution, not premixed |
:::

The alginate is dissolved in whatever outer solution the embedded populations already sit in, so the gel does not have an osmolarity of its own to specify. It inherits one.

A multimaterial variant combines 1.6 wt% alginate with a PEGDA precursor to give a gel that crosslinks both ionically and photochemically. That is a composition of two gels rather than a variant of this one — see [PEGDA Gel](../gel-pegda/spec.md).

(gel-alginate-expected-behavior)=
# Expected Behavior

## Gels

Calcium bridges adjacent alginate chains into "egg-box" junctions, setting the matrix without heat or light. Expect a gel that holds dispersed populations in place for the duration of a multi-hour incubation at 37 °C.

The confirmed result at this composition is the Chicago theophylline readout: theophylline-responsive synthetic cells, CPRG-loaded SUVs and commercial LacZ co-embedded in the same gel give a yellow-to-purple color change after about 16 h, read at (570–575) nm and by eye.

:::{attention} The gel is not what was varied
That result confirms the cascade in this gel. No experiment varies the alginate concentration, the calcium concentration or the set time and reports what changes, so the numbers above are the one condition that has been run rather than an optimum.
:::

(gel-alginate-requirements)=
# Requirements

Requires 200 mM CaCl₂ as a separate crosslinking step, so anything embedded must tolerate a divalent calcium load at that concentration.

Requires a buffer that is already compatible with the populations being embedded. The alginate is dissolved into their outer solution rather than replacing it.

Imposes no heat and no illumination on its contents, which is what distinguishes it from the other three gels.

# Processes

Prepared and set by [Alginate Hydrogel Embedding](../../processes/embed-alginate-hydrogel/main.md), which also covers co-embedding the sensing cells, SUVs and LacZ.

# Materials

:::{table} Purchased materials.

| Name | Category | Product | Manufacturer | Part # | Link |
| --- | --- | --- | --- | --- | --- |
| Sodium alginate | Chemical | Alginic acid sodium salt, low viscosity | Sigma-Aldrich | A0682 | [link](https://www.sigmaaldrich.com/US/en/product/sigma/a0682) |
| Calcium chloride | Chemical | Calcium chloride, anhydrous, ≥97% | Sigma-Aldrich | C1016 | [link](https://www.sigmaaldrich.com/US/en/product/sigma/c1016) |
:::

# Credits

Developed by [Maram Naji](https://orcid.org/0000-0003-1409-4194) (Chicago Node, Lucks Lab) and the Chicago Node (Kamat Lab and Liu Lab).
