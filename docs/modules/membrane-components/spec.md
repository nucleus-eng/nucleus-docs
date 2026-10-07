---
title: "Membrane Components"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [Lipid](../lipid/spec.md).
<!-- /gen:position -->

The molecules a bilayer is made from. **What makes a Module a member is what it does: it goes into a membrane.** They are not made by any process documented here — every one arrives as a purchased stock — and they share no formulation.

**This class exists because its members do not have pages.** POPC, cholesterol, DSPE-PEG2000 and the fluorescent labels are named on three membrane specifications and nowhere else, so a molecular weight or a stock concentration lives on whichever membrane happens to use it. Each of those three specifications already records that as an open item in the same words. The class gives the gap one home rather than three.

**Not every member is a lipid, which is why the class is not called Lipids.** Cholesterol is a sterol and forms no bilayer on its own. A fluorescent label at about 0.1 mol% reports on the bilayer rather than building it. Both are components of a membrane; neither is a bilayer-forming lipid.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

**None has a page, and that is the finding rather than an omission on this page.**

:::{table} Named across the three membrane specifications.
| Component | Role | Stated on |
| --- | --- | --- |
| POPC | the bilayer-forming lipid in every Nucleus membrane | [Membrane: POPC](../membrane-popc/spec.md), [POPC/Chol (7:3)](../membrane-popc-chol/spec.md), [POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md) |
| Cholesterol | a sterol that stiffens the bilayer; forms none alone | [POPC/Chol (7:3)](../membrane-popc-chol/spec.md), [POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md) |
| DSPE-PEG2000 | a PEGylated lipid; its headgroup gives steric stabilization at the surface | [Membrane: POPC](../membrane-popc/spec.md) |
| Liss-Rhod PE | a fluorescent label, about 0.1 mol% | [POPC/Chol (7:3)](../membrane-popc-chol/spec.md), [POPC/Chol (9:1)](../membrane-popc-chol-9-1/spec.md) |
| 18:1 Cyanine 5 PC | a fluorescent label; its stock concentration is disputed on the page that states it | [Membrane: POPC](../membrane-popc/spec.md) |
:::

# Reference Composition

**This class states no formulation.** A component is a single substance, and what varies between members is which substance it is. Proportions belong to the membrane that mixes them, because the same POPC is 70 mol% in one membrane and 89.9 mol% in another.

# Expected Behavior

A member partitions into a lipid phase and stays there. **The class says nothing more** — what a given component contributes is the member's own behavior, and only the labels have one that can be observed directly.

# Requirements

Requires a lipid phase to partition into. **A component on its own is a stock solution, not a membrane**; what makes a bilayer is [Membrane](../membrane/spec.md), which mixes these.

# Constituent Modules

None. A component is a single substance, and nothing in this corpus produces one.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
