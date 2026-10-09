---
title: "Transcribe"
subtitle: "Function"
status: draft
---

# Overview

Transcribe makes RNA from a DNA template, inside a cytosol that carries an RNA polymerase. It is one operation with two routes here, and **the routes are not interchangeable**: each reads a different class of promoter, and one of them also needs the template to be circular.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Transcribe takes a cytosol and a DNA template, and returns the cytosol, changed, together with an RNA. It runs only where the cytosol carries a polymerase that reads the template's promoter, so each route is named by the promoters it reads.

# Substrates and products

These are the same on every route. The polymerase decides which promoter is read, not what is consumed.

| | Per nucleotide added | Per transcript |
| --- | --- | --- |
| **Consumes** | one nucleoside triphosphate: ATP, GTP, CTP or UTP, as the template dictates | — |
| **Produces** | one nucleotide on the RNA, and one pyrophosphate (PPi) | one RNA molecule, and one fewer PPi: the first nucleotide keeps its triphosphate |
| **Unchanged** | the DNA template and the RNA polymerase | |

The polymerase needs Mg²⁺ and does not consume it. The pyrophosphate it releases binds Mg²⁺, though, and where nothing splits the PPi the two can precipitate together, so Mg²⁺ is not left unchanged by what follows. Pyrophosphate is a product here and the substrate of another function. Where the cytosol carries inorganic pyrophosphatase, as [Base Cytosol](../../modules/base-cytosol/spec.md) does, that enzyme splits each PPi into two phosphates. That step is the pyrophosphatase's, an instance of [Degrade](../degrade/main.md), not this function's.

**What this does to the number of dissolved particles, as an estimate.** Counted from the table above, as for an ideal solution, transcription by itself leaves the number unchanged: each nucleotide trades one NTP for one PPi, and each transcript trades one PPi for one RNA. Where pyrophosphatase splits the PPi, each nucleotide after the first adds one particle. Where nothing splits it and it precipitates with Mg²⁺, the number falls instead. No run has measured either.

# Routes

| Route | Polymerase | Realized by | Promoter it reads | Template |
| --- | --- | --- | --- | --- |
| T7 | T7 RNA polymerase, a defined component | [Base Cytosol](../../modules/base-cytosol/spec.md), and the sensor cytosols built on it: [SensorCytosol[aTc ⟶ PLA1]](../../modules/atc-sensor-cytosol/spec.md), [SensorCytosol[pH ⟶ PLA1]](../../modules/ph-sensor-cytosol/spec.md), [SensorCytosol[theophylline ⟶ LacZ]](../../modules/theophylline-sensor-cytosol/spec.md). The [Emitter: IV-HSL](../../modules/emitter-ivhsl/spec.md) reaction, in NEB PURExpress | pT7 | linear or circular |
| *E. coli* σ70 | the host RNA polymerase in a cell extract | [S30 Lysate](../../modules/s30-lysate/spec.md), and [SensorCytosol[3OC6-HSL ⟶ PLA1]](../../modules/ahsl-sensor-cytosol/spec.md) built on it | a σ70 promoter, such as J23101 | circular only |

# What selects a route

- **The promoter.** A template is transcribed only where the cytosol carries a polymerase that reads its promoter. Base Cytosol carries T7 RNA polymerase and reads pT7; S30 Lysate reads *E. coli* σ70 promoters. See each cytosol's Requirements: [S30 Lysate](../../modules/s30-lysate/spec.md) requires *"a circular DNA template driven by an E. coli σ70 promoter"*.
- **The template's topology, on the σ70 route.** S30 Lysate degrades linear DNA, because no GamS is added to protect it, so its constructs are used in their circular, pOpen-backbone form. Base Cytosol does not require circular DNA, so the linear cassette is also valid there.
- **What uses this operation without choosing a route.** A repressor detector needs transcription in its compartment, by either route; see [Repressor Detector](../../modules/repressor-detector/spec.md).

# Not yet attested

- A transcript yield for either route.
- A pT7 template in S30 Lysate, or a σ70 promoter in Base Cytosol. Each would need the other route's polymerase added.
- Any route beyond these two, such as SP6 RNA polymerase. The substrates and products above do not depend on which polymerase is used, so a new route changes the table of routes and not the table above.
- Which polymerase NEB PURExpress carries. The T7 route is read off the `pT7` templates used with it, not off a stated composition.
- A measured osmotic change from transcription, in any cytosol. The particle count above is an estimate.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
