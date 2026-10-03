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

:::{note} Only the pH path needs this step
Color development is a separate step from [Colorimetric Readout](../colorimetric-readout/main.md). The pH path needs it because its sensing chemistry and its reporting chemistry want incompatible conditions: β-galactosidase works less well at the acidic pH the sensor uses ([Baltin et al., 2017](https://doi.org/10.11134/btp.2.2017.11), measured for the *Streptococcus thermophilus* enzyme). The aTc, LuxR and EsaR paths run at a pH their reporter tolerates, so their trigger and their readout are adjacent and need no step between them.
:::

# Why the step exists

**The sensing and the reporting want different pH.** The pH path triggers between pH 6 and 6.5, which is what detaches the pH-responsive strand and frees the trigger. β-galactosidase is pH dependent and works poorly there. So the enzyme cannot be present while the device senses, and the gel cannot stay acidic while the device reports.

**The resolution is order, not formulation.** The enzyme is withheld until after embedding and arrives with a neutralizing buffer. Nothing about either chemistry changes; only when each one is present.

# The step

1. Confirm the sensing incubation is complete. Developing early reads an unfinished reaction.
2. Add the basic buffer with [LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) to the embedded gel.
3. Incubate until the color is stable.
4. Read the result. See [Colorimetric Readout](../colorimetric-readout/main.md).

:::{attention} No figures are recorded for any of these steps
No buffer composition, enzyme concentration, incubation time or target pH after neutralization is documented. The four steps above give the shape of the process, not a protocol. @Editor: supply them, starting with the gel-dispersed LacZ concentration, which [LacZ Enzyme](../../modules/reporter-lacz-enzyme/spec.md) also needs.
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
