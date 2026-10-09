---
title: "Fluorophore"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [Chromophore](../chromophore/spec.md). Refined by [Sulfo-Cyanine5](../fluorophore-sulfo-cyanine5/spec.md), [18:1 Cyanine 5 PC](../lipid-cyanine5-pc/spec.md), [Liss-Rhod PE](../lipid-liss-rhod-pe/spec.md), [deGFP Reporter](../reporter-degfp/spec.md), [mNeonGreen Reporter](../reporter-mneongreen/spec.md).
<!-- /gen:position -->

A class: a [Chromophore](../chromophore/spec.md) that re-emits what it absorbs, at a longer wavelength than it took in.

**Re-emission is the operation its parent does not have.** A chromophore absorbs, and what a reader measures is the light that did not come back. A fluorophore absorbs and then emits, and what a reader measures is light the molecule itself produced. That is why a plate reader needs two wavelengths for a member of this class and one for a member that only absorbs.

**The gap between the two wavelengths is what lets a reader separate members.** Two fluorophores far enough apart can be read in one sample, one channel each. Two that are close cannot, and no channel tells them apart.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [deGFP Reporter](../reporter-degfp/spec.md) | A fluorescent protein. The signal is the protein itself. |
| [mNeonGreen Reporter](../reporter-mneongreen/spec.md) | A fluorescent protein. The signal is the protein itself. |
| [Liss-Rhod PE](../lipid-liss-rhod-pe/spec.md) | A dye on a lipid, so it reports where the bilayer is. |
| [18:1 Cyanine 5 PC](../lipid-cyanine5-pc/spec.md) | A dye on a lipid, so it reports where the bilayer is. |
| [Sulfo-Cyanine5](../fluorophore-sulfo-cyanine5/spec.md) | A free dye, so it reports where the lumen is. |

# Expected Behavior

A member excited in its own band emits in another, and a reader that collects the second band sees it. Any member bleaches as it is read, because the light that excites it is the light that destroys it: that is inherited from [Chromophore](../chromophore/spec.md) and is not special to this class.

**A channel is named for a dye and reports a band.** A channel labeled for one member will report any member whose emission falls in that band. Read the dye off the composition, never off the channel name.

# Requirements

A member used to tell two things apart requires that nothing else in the sample emits in its band. Where something does, the channel reports both and separates neither.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
