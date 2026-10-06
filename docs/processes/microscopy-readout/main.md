---
title: "Microscopy Readout"
subtitle: "Process"
status: draft
---

# Overview

Microscopy Readout reads a sample one object at a time and yields an image. It is the readout for any question whose answer is per cell rather than per well.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. Acquisition settings are recorded for one run in the whole corpus — see Materials and Equipment.
:::

Four jobs in this corpus, each stated on the page that owns the result:

- **Yield and morphology** — count round, intact cells per imaging field, and watch whether the count holds through incubation. [Cell: Base Cytosol, POPC/Chol (9:1)](../../modules/cell-base-cytosol-popc-chol/spec.md).
- **Encapsulation and expression** — confirm a lumen holds what it was built to hold, and that a reporter is being made inside it. [Dye Liposomes](../../modules/dye-liposomes/spec.md).
- **Retention over time** — image the same field repeatedly and watch a dye leave or stay. [Membrane Pore: Cx43](../../modules/membrane-pore-cx43/spec.md) reads leakage this way; [pH Cascade](../../modules/ph-cascade/spec.md) reads lysis this way.
- **Embedding** — confirm a signal belongs to intact embedded cells and not to the matrix around them. [Embedding: Thermal Setting](../embed-thermal-setting/main.md).

**The sample survives the reading.** Nothing is added to the well and nothing is taken out of it, so the same well can be imaged again, and a timeseries over hours is a normal use rather than a special case. Illumination costs signal through photobleaching, which makes a later read dimmer and not impossible.

**It is not [Colorimetric Readout](../colorimetric-readout/main.md).** That process reads a bulk property of a whole well and gives one figure for it. This one resolves single objects, so it can say which population a signal came from and how much of that population still holds it. The two share no instrument, no plate and no analysis, and their results do not go on one axis.

# Materials and Equipment

A fluorescence microscope that can resolve a single cell, select one channel per label, and collect a z-stack. A plate the objective can image through: [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) ends by preparing one.

:::{attention} One instrument is recorded in this corpus, on one page
[Responder Cell: aTc ⟶ IV-HSL](../../implementations/responder-atc-ivhsl/main.md) records a Revvity Operetta CLS at 40×, collecting two fluorescent channels and brightfield. No other run records an instrument, objective, filter set, laser line, exposure or gain, and no run records how many z-planes it took or how deep the stack ran. @Editor: supply them per run, and decide whether this page should recommend an instrument or stay neutral between them.
:::

# Protocol

- [ ] Prepare the sample at a density you can count. [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) ends with the three steps that do this — hold on ice, dilute onto the plate, and dilute again if the field is too crowded to analyse.
- [ ] Select one channel per label you need to tell apart. One channel cannot separate two things that share it.
- [ ] Take each dye from the composition, never from the channel name. A microscope names a channel after a representative fluorophore for the band it passes, not after what is in the well.
- [ ] Collect a z-stack, not one plane. A cell is a sphere, and a single plane cuts most of a field off-centre. 1.5 µm between planes sections a cell without oversampling it, and 0.333 µm in the plane resolves its membrane.
- [ ] Use the same optical and contrast settings for every condition in a comparison, the negative control included.
- [ ] Write one store per well, OME-Zarr version 0.5. One per well and not one per plate, because the analysis opens a well at a time.
- [ ] Record the instrument, objective, channels, exposure and gain with the run. This page states none of them.

:::{danger} The channel name is not the dye name
A channel labelled `Alexa Fluor 647` reports whatever that band passes, which may be a different dye entirely. A reader who takes the label as the dye will call a lumen marker a membrane label, and that is a claim about where the signal is, inverted. Read the dye off the composition table.
:::

# Quality Control

**Score against a negative control imaged in the same session, at matched settings.** [Embedding: Thermal Setting](../embed-thermal-setting/main.md) states this for its own gel and it holds for every reading here. A brightness difference read off two different settings is a settings difference.

**A channel that separates nothing is not a control.** Where two populations carry the same membrane label, that channel shows both and distinguishes neither. The separating channel is the one whose dye is in one population only, and the reading rests on that dye being absent from the other. [pH Cascade](../../modules/ph-cascade/spec.md) is the case this corpus has.

**This process gives no bulk figure.** It reports per object and per field, so it does not go on one axis with an absorbance value, and a fraction counted off an image is not a concentration. Where both readouts ran on one plate, report them side by side.

**Brightness is not uniform between cells.** Expect a spread within one field. A single dim cell is not a failed reaction, and a single bright one is not a result.

**Loss of a dye is loss of the dye.** Reading it as lysis, or as transport through a pore, assumes the dye stays put in the intact state over the same time under the same illumination. That is a claim about the specimen, and it belongs on the Module page that makes it.

# Processes

- [Assay](../assay/main.md) — the abstraction this process is an instance of. It reads something and yields a value.
- [Colorimetric Readout](../colorimetric-readout/main.md) — the other readout a sensing cascade ends at, and the one this is not.
- [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) — its last three steps prepare a sample for this readout.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
