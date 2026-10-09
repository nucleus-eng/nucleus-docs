---
title: "Standard: Fluorescein"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

A plate reader reports fluorescence in relative units. Those units are a property of the instrument, the gain setting and the day, not of the sample, so two reads of the same well are not comparable across any of the three. This Module is the ladder that converts them: a set of known fluorescein concentrations read alongside the samples, giving a fit that puts the run on a concentration scale instead of an instrument scale.

**It is a Module and not a Process because it has a Composition and a Function.** The composition is four prepared levels; the function is to make a reading comparable. The reading itself is somebody else's step.

It is read against by [Detector: EsaR](../detector-esar/spec.md), as a titration across the four levels, and by [Detector: tetR-aTc](../detector-tetr-atc/spec.md), as the older single-point normalization at 1 µM.

# Reference Composition

Four levels in a four-tube PCR strip, one replicate of each, 50 µL per tube. One strip per experiment.

| Level | Fluorescein | Volume | What it is for |
| --- | --- | --- | --- |
| 1 | 0 µM | 50 µL | The blank offset — what the instrument reads with no fluorophore present |
| 2 | 0.5 µM | 50 µL | The low end of the fit |
| 3 | 1 µM | 50 µL | The single point an older normalization used on its own |
| 4 | 2 µM | 50 µL | The high end of the fit |

All four come from one bought stock, so the levels are related by dilution rather than by independent weighing.

**The 1 µM level is kept for continuity and the other three make it a fit.** A single point can normalize one run against another; it cannot show that the response is linear, nor where it stops being linear. The three added levels are what turn a normalization into a calibration.

# Expected Behavior

Linearity is a property of the channel, not of the standards, and one channel in common use does not have it.

| Channel | Response | Use |
| --- | --- | --- |
| Green, excitation 485 nm / emission 528 nm | Linear | The intended use |
| Cy3 monochromator | Linear | Acceptable |
| Cy5 monochromator | Linear | Acceptable |
| Syn2 | Linear | Acceptable |
| Cy3 filter set | **Not linear** | **A fit is invalid here.** The response compresses across the range |

**Only green-channel standards exist today.** Red-channel standards are intended and are not prepared yet, so nothing on this page covers a red readout.

# Requirements

**The usable range is 0.5 µM to 2 µM.** The fit is poor below 0.5 µM, and it must not be extrapolated above 2 µM.

**Check the 2 µM standard for detector saturation before fitting anything.** A saturated top point flattens the slope and silently biases every concentration read off it. If it saturates, either lower the gain and re-read, or drop that point from the fit — and drop it only if the samples are also clear of saturation, because a fit that excludes the top of its range cannot be applied to a sample above it.

# Materials

| Material | Description | Manufacturer | Part # |
| --- | --- | --- | --- |
| Fluorescein | Fluorescein standard, NIST-traceable | Invitrogen | F36915 |

NIST-traceable matters here rather than being a procurement preference: the point of the ladder is that a concentration means the same thing on another instrument, and that only holds if the stock is traceable to something outside the lab.

# Processes

No Process page documents the reading itself. The SOP this page comes from ends by saying to follow your normal plate reader and analysis protocols, so the steps below are the preparation and nothing downstream of it.

- [ ] Use one strip per analysis plate.
- [ ] Thaw the strip, vortex it, and spin it down.
- [ ] Pipette 10 µL per well with a multi-channel p20, or match the reaction volume if it differs.
- [ ] Repeat for duplicates, or ideally triplicates.
- [ ] Read the plate as normal.

@Editor(london): the reading and its analysis have no Process page. [Colorimetric Readout](../../processes/colorimetric-readout/main.md) is the shape to copy if one is written.

# Credits

Developed by the London Node.

:::{attention} Credits are draft
:class: dropdown

@Editor(london): name the SOP's author here.
:::
