---
title: "Translate"
subtitle: "Function"
status: draft
---

# Overview

Translate makes protein from an RNA, inside a cytosol that carries ribosomes, tRNA and the enzymes and factors that work with them. It has two routes here, and they differ in where the machinery comes from: purified components, each listed with its amount, or an extract of *E. coli* whose composition is not stated. **Nothing recorded here makes an RNA work on one route and not the other.** A cytosol is chosen for its transcription, and translation comes with it.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Translate takes a cytosol and an RNA, and returns the cytosol, changed, together with a protein. Unlike [Transcribe](../transcribe/main.md), no condition on it is recorded here: no page names an RNA that a cytosol carrying the machinery fails to translate.

# Substrates and products

These are the same on both routes.

| | Per amino acid added | Per protein chain |
| --- | --- | --- |
| **Consumes** | one amino acid; one ATP, which becomes AMP and pyrophosphate (PPi) when the amino acid is attached to its tRNA; two GTP, which become two GDP and two phosphates as the amino acid is delivered and the ribosome moves on | GTP to start the chain and to release it |
| **Produces** | one amino acid on the chain | one protein molecule |
| **Unchanged** | the RNA, the ribosomes, the tRNA, and the enzymes and factors | |

Base Cytosol also carries methionyl-tRNA formyltransferase (MTF) and folinic acid, which put a formyl group on the methionine that starts each chain. Like transcription, translation releases pyrophosphate, and where the cytosol carries inorganic pyrophosphatase, as [Base Cytosol](../../modules/base-cytosol/spec.md) does, each PPi is split into two phosphates. That step is the pyrophosphatase's, an instance of [Degrade](../degrade/main.md), not this function's.

**The AMP and GDP are turned back into ATP and GTP by other enzymes, where the cytosol carries them.** Base Cytosol carries creatine kinase with creatine phosphate, adenylate kinase (AK) and nucleoside diphosphate kinase (NDK). [Energy: PPK](../../modules/energy-ppk/spec.md) does the same from polyphosphate. That is a separate function, [Regenerate rNTPs](../regenerate-rntps/main.md), and it lets translation run for longer.

**What this does to the number of dissolved particles, as an estimate.** Counted from the table above, as for an ideal solution, each amino acid added gives two more particles: the amino acid leaves the solution, the ATP becomes two molecules, and each of the two GTP becomes two. Where pyrophosphatase splits the PPi, each amino acid gives three. Turning AMP and GDP back into ATP and GTP does not take the count back down, because every route that does it here moves a phosphate from a carrier rather than taking one out of solution. See [Regenerate rNTPs](../regenerate-rntps/main.md). **So the phosphate released above stays in solution**: nothing here consumes it. Transcription by itself leaves the count unchanged, so in a cytosol that does both, most of the change comes from translation. No run has measured it.

# Routes

| Route | Machinery | Realized by |
| --- | --- | --- |
| Purified components | ribosomes, tRNA, the 20 aminoacyl-tRNA synthetases, and the initiation, elongation and release factors, each a defined component | [Base Cytosol](../../modules/base-cytosol/spec.md), and the sensor cytosols built on it: [SensorCytosol[aTc ⟶ PLA1]](../../modules/atc-sensor-cytosol/spec.md), [SensorCytosol[pH ⟶ PLA1]](../../modules/ph-sensor-cytosol/spec.md), [SensorCytosol[theophylline ⟶ LacZ]](../../modules/theophylline-sensor-cytosol/spec.md). The [Emitter: IV-HSL](../../modules/emitter-ivhsl/spec.md) reaction, in NEB PURExpress |
| Cell extract | *E. coli*'s own ribosomes and factors, in an extract whose composition is not stated | [S30 Lysate](../../modules/s30-lysate/spec.md), and [SensorCytosol[3OC6-HSL ⟶ PLA1]](../../modules/ahsl-sensor-cytosol/spec.md) built on it |

# What selects a route

- **The cytosol, and the cytosol is chosen for its transcription.** Every recorded use translates an RNA that the same cytosol has just transcribed, so the route is fixed by the promoter on the DNA. See [Transcribe](../transcribe/main.md).
- **Nothing at the translation step itself.** No page records an RNA that one route translates and the other does not.

# Not yet attested

- A protein yield, in mass or in moles, on either route.
- Translation of an RNA added directly. Every recorded use starts from DNA, so translation is never seen apart from transcription.
- What the S30 Lysate route uses to turn AMP and GDP back into ATP and GTP. Its premix composition is not stated.
- Which of the two routes is faster, or makes more protein from the same RNA.
- A measured osmotic change from translation, in any cytosol. The particle count above is an estimate.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
