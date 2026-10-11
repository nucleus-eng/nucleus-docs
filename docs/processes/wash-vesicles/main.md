---
title: "Wash Vesicles"
subtitle: "Process"
status: draft
---

# Overview

Wash Vesicles moves vesicles out of the solution they were made in and into a fresh outer solution. The membrane and what it holds come through unchanged. Only the outside is replaced. It is optional, and it can follow any [Encapsulation](../encapsulate/main.md) route.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. No wash is recorded for synthetic cells — see Protocol.
:::

**Without a wash, what was not encapsulated stays in the sample.** [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) takes its cells together with the outer solution around them, and that solution carries any inner solution that never reached a lumen. An enzyme in it works outside the cells: it meets its substrate in the well and gives a signal that no cell made. In a readout for lysis, that signal looks like lysis.

**It separates; it does not destroy.** What it removes still exists, in the supernatant or in the column's later fractions. That makes the removed solution a control: read it with the substrate, beside the washed vesicles, and it shows how much of the signal came from outside. [Degrade Exterior LacZ](../degrade-exterior-lacz/main.md) is the other way to remove an enzyme from outside, and it destroys what it removes.

**A wash costs vesicles.** Each spin and resuspension loses some, and no run records how many.

# Materials and Equipment

- Fresh outer solution, matched to the one the vesicles were made in. A fresh solution that reads differently changes the osmotic balance across the membrane, so read both by [Osmometry Readout](../osmometry-readout/main.md).
- For centrifugal exchange: a microcentrifuge.
- For size exclusion: a size-exclusion column that elutes vesicles in its void volume.

# Protocol

Two routes are recorded, each on the page for the vesicles it was run on. The figures for speed, volume and number of washes belong to that page, so follow them there.

## Centrifugal Exchange

Recorded for LUVs on [Encapsulation: Freeze-Thaw](../encapsulate-luv/main.md), which washes ten times.

- [ ] Spin the vesicles down.
- [ ] Remove the supernatant without disturbing the pellet. Keep the first supernatant if you will read it as a control.
- [ ] Add the same volume of fresh outer solution.
- [ ] Turn the tube 180° in the rotor before the next spin. The pellet then forms on the other wall, which releases solution trapped between the vesicles.
- [ ] Repeat for as many washes as the route calls for.

:::{attention} No wash is recorded for synthetic cells
[Encapsulation: Phase Transfer](../assemble-base-cell/main.md) pellets its cells once, at 9000 g for 10 min. No run records washing them, so no speed, time or number of washes is established for cells, and whether they survive repeated spins is not known. @Editor: supply them once a run has washed cells.
:::

## Size Exclusion

Recorded for SUVs on [Encapsulation: Extrusion](../encapsulate-suv/main.md), which runs it twice.

- [ ] Equilibrate the column with the solution you are moving the vesicles into.
- [ ] Load the vesicles, and collect them where they elute: in the void volume, ahead of free small molecules.
- [ ] Run the collected fraction through a second time if one pass leaves too much behind. On that page, one pass leaves detectable free CPRG.

# Quality Control

**Read the removed solution beside the washed vesicles.** Supernatant with substrate and no vesicles shows how much signal comes from outside. Without that well, a signal from outside and a signal from inside look the same.

**Count the vesicles before and after.** A wash that loses most of them has changed the sample. [Microscopy Readout](../microscopy-readout/main.md) counts them.

# Processes

- [Encapsulation](../encapsulate/main.md) — what this follows, by any of its routes.
- [Degrade Exterior LacZ](../degrade-exterior-lacz/main.md) — removes an enzyme from outside by destroying it. It ends with one centrifugal exchange of its own.
- [Osmometry Readout](../osmometry-readout/main.md) — reads the fresh outer solution against the old one.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
