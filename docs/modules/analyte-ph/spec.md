---
title: "Analyte: pH"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

pH is what the [pH-Sensing Detector](../detector-ph/spec.md) responds to. Below about pH 6.5 the pH-responsive strand releases its trigger, the toehold switch opens, and the downstream effector gene is translated.

pH is not a substance. Unlike the other four analytes, which are molecules pipetted into a solution, pH is a *property of that solution*. So an Analyte is **a property of the environment a Detector responds to** — a definition that covers a concentration and a pH alike.

As an Analyte, pH is not a constituent of any Module. It is a property of the outer solution, not a component of the cell suspended in it.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

pH is a property, so it has no composition. The table gives the response band.

:::{table} Response band, from [pH-Sensing Detector](../detector-ph/spec.md).
| Band | Value | What it governs |
| --- | --- | --- |
| Switch ON | pH ≤ 6.5 | The trigger releases and the toehold switch opens |
| Switch OFF | neutral | The trigger stays bound in the duplex |
:::

:::{attention} The band is a threshold, not a window
The band has one boundary, pH 6.5. No lower bound is documented — the pH at which the cytosol, the membrane or the PURE reaction stops working before the switch does. @Editor(chicago): confirm whether an acidity floor exists.
:::

# Requirements

Requires a [pH-Sensing Detector](../detector-ph/spec.md) to be sensed at all.

**Requires the outer solution to be buffered where the readout is not the pH change itself.** The [Chicago Cascade](../chicago-cascade/spec.md) states its own outer solution at 42.5% (v/v) Tris-HEPES, and the pH path needs a neutralization step before color develops while the aTc path reads out directly. So the analyte and the buffer that holds it are coupled in a way the other four analytes are not.

# Processes

None. An analyte is supplied to an assay rather than produced by a Nucleus process. For pH specifically, it is set by the composition of the outer solution rather than dosed.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
