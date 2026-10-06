---
title: "Analyte"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines nothing declared. Refined by [`analyte-3oc6-hsl`](../analyte-3oc6-hsl/spec.md), [`analyte-atc`](../analyte-atc/spec.md), [`analyte-iptg`](../analyte-iptg/spec.md), [`analyte-ph`](../analyte-ph/spec.md), [`analyte-theophylline`](../analyte-theophylline/spec.md).
<!-- /gen:position -->

A class: the substance an assay is run against.

Every member is supplied to an assay rather than produced by a Nucleus process. That is what separates an analyte from everything else in this corpus: a Module with no composition and no step, whose whole role is to be present or absent while something else is measured.

A Module that detects an analyte is not a member. [Detector](../detector/spec.md) holds those, and each names the analyte it responds to.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Members

| Member | What makes it a member |
| --- | --- |
| [3OC6-HSL](../analyte-3oc6-hsl/spec.md) | The quorum-sensing signal the LuxR receiver binds. |
| [aTc](../analyte-atc/spec.md) | Anhydrotetracycline, which relieves TetR repression. |
| [IPTG](../analyte-iptg/spec.md) | Relieves LacI repression. |
| [pH](../analyte-ph/spec.md) | Not a substance. A condition of the solution, and the one member that cannot be pipetted. |
| [Theophylline](../analyte-theophylline/spec.md) | Bound by the riboswitch aptamer. |

# Expected Behavior

An analyte is dosed, not assembled. A reader looking for what one does should read the Detector that responds to it, because an analyte's behavior is the detector's response and not a property of the analyte.

# Requirements

Every member requires a Detector that responds to it. None requires anything of the system it is dosed into, which is why no member declares a composition.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
