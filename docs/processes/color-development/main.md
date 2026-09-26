---
title: Color Development
subtitle: "Process"
status: draft
---

# Overview

Color Development brings a gel to the conditions its reporter enzyme needs, after the sensing step has run under conditions the enzyme cannot work in. A basic buffer carrying [LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) goes into the gel, and only then does color appear.

**It is not the readout.** [Colorimetric Readout](../colorimetric-readout/main.md) observes a change; this process creates the conditions under which the change can happen at all. A device that needs no development goes straight from its trigger to its readout.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} One demo needs this and three do not, and that is the point
Written 2026-09-24. Jon: *"color development is distinct from colorimetric readout. that's a step only for the pH sensor because LacZ doesn't work as well in acidic conditions. doesn't affect other demos."*

The aTc, LuxR and EsaR paths all run at a pH their reporter tolerates, so their trigger and their readout are adjacent. **The pH path is the one whose sensing chemistry and whose reporting chemistry want incompatible conditions**, which is why it alone has a step between them.
:::

# Why the step exists

**The sensing and the reporting want different pH.** The pH path triggers between pH 6 and 6.5, which is what detaches the pH-responsive strand and frees the trigger. β-galactosidase is pH dependent and works poorly there. So the enzyme cannot be present while the device senses, and the gel cannot stay acidic while the device reports.

**The resolution is order, not formulation.** The enzyme is withheld until after embedding and arrives with a neutralizing buffer. Nothing about either chemistry changes; only when each one is present.

**This is a requirement shape rather than a one-off.** A condition on state whose required value differs between two steps, discharged by a step that changes the state. Separation is the other instance this corpus carries: an enzyme and its substrate must be apart, and then must not be, and a breach discharges it.

# The step

1. Confirm the sensing incubation is complete. Developing early reads an unfinished reaction.
2. Add the basic buffer with [LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) to the embedded gel.
3. Incubate until the color is stable.
4. Read the result. See [Colorimetric Readout](../colorimetric-readout/main.md).

:::{attention} No figures are recorded for any of these steps
No buffer composition, no enzyme concentration, no incubation time and no target pH after neutralization appear in any source here. **The gel-dispersed LacZ concentration is already an open ask** on the enzyme's own page and this process is a second place it is needed. Treat the four steps above as the shape of the process and not as a protocol.
:::

# Requirements

Requires a reporter whose working conditions the sensing step does not provide. **A device whose reporter tolerates its own sensing conditions must not use this process**, because the step adds handling and an off-state risk for nothing.

Requires that the enzyme is withheld until after the gel is embedded. Adding it earlier puts it in the device during the acid phase, which is what the step exists to avoid.

Requires a buffer that neutralises without disturbing what is embedded.

# Modules

- [LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) — what the buffer carries
- [Analyte: pH](../../modules/analyte-ph/spec.md) — the analyte whose range forces the step
- [pH Cascade](../../modules/ph-cascade/spec.md) — the one path that uses it

# Processes

- [Colorimetric Readout](../colorimetric-readout/main.md) — what follows this step, and what it is not
