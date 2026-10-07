---
title: "Lipid"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [Membrane Components](../membrane-components/spec.md). Refined by [18:1 Cyanine 5 PC](../lipid-cyanine5-pc/spec.md), [Liss-Rhod PE](../lipid-liss-rhod-pe/spec.md).
<!-- /gen:position -->

A class: a [Membrane Component](../membrane-components/spec.md) that is itself amphiphilic, so it takes its place in the bilayer by having a head and a tail.

**Not every membrane component is one.** Cholesterol is a sterol: it sits in a bilayer and changes how it behaves, and it does not form one. That is why its parent class is not called Lipids, and it is why this class sits below that one rather than replacing it.

**A labeled lipid is a member and so is a plain one.** A dye hung off a lipid head group does not stop the lipid being a lipid, which is why the two membrane labels here refine this class and [Fluorophore](../fluorophore/spec.md) at once.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [Liss-Rhod PE](../lipid-liss-rhod-pe/spec.md) | A phosphoethanolamine lipid carrying a rhodamine dye. |
| [18:1 Cyanine 5 PC](../lipid-cyanine5-pc/spec.md) | A phosphocholine lipid carrying a cyanine dye. |

# Expected Behavior

A member put into a bilayer-forming mixture ends up in the bilayer rather than in the solution on either side of it. A member carrying a dye therefore reports where the bilayer is, and not where the lumen is.

# Requirements

None beyond what [Membrane Components](../membrane-components/spec.md) requires.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
