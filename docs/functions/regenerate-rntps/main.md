---
title: "Regenerate rNTPs"
subtitle: "Function"
status: draft
---

# Overview

Regenerate rNTPs turns a spent nucleotide back into a ribonucleoside triphosphate (rNTP): ATP, GTP, CTP or UTP, the forms that transcription and translation use. It draws on a store of phosphate to do it. Transcription and translation spend ATP and GTP, and regeneration lets them keep running after the starting amount would have run out. It has two routes here, which differ in **the store they draw on**: creatine phosphate, in [Base Cytosol](../../modules/base-cytosol/spec.md), or polyphosphate, in [Energy: PPK](../../modules/energy-ppk/spec.md). The two can run in the same reaction.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Regenerate rNTPs takes the regenerating enzymes and a spent nucleotide, and returns the enzymes with the nucleotide made usable again. The phosphate comes from the store, and the store is used up. So it does not make energy. It moves phosphate from the store onto the nucleotides that other functions spend.

# Substrates and products

| | Consumes | Produces | Unchanged |
| --- | --- | --- | --- |
| **Creatine phosphate** | one creatine phosphate, and one ADP | one creatine, and one ATP | creatine kinase |
| **Polyphosphate** | one phosphate from the end of a polyphosphate chain, and one AMP, ADP or GDP | a chain one phosphate shorter, and one ADP, ATP or GTP | PPK2 |

Base Cytosol also carries two enzymes that pass phosphate between nucleotides without a store. Adenylate kinase (AK) makes two ADP from one AMP and one ATP, so the AMP that translation leaves can reach creatine kinase. Nucleoside diphosphate kinase (NDK) makes GTP, CTP or UTP from its diphosphate, using one ATP.

**What this does to the number of dissolved particles, as an estimate.** Each step above exchanges two molecules for two, as for an ideal solution, so regeneration by itself does not change the count. Its effect is indirect: it keeps the functions that do change the count, such as [Translate](../translate/main.md), running for longer. No run has measured it.

# Routes

| Route | Store | Enzymes | Regenerates | Realized by |
| --- | --- | --- | --- | --- |
| Creatine phosphate | creatine phosphate | creatine kinase, with AK and NDK | ATP from ADP, and from AMP through AK. GTP, CTP and UTP from their diphosphates, through NDK, using that ATP | [Base Cytosol](../../modules/base-cytosol/spec.md), and the sensor cytosols built on it: [SensorCytosol[aTc ⟶ PLA1]](../../modules/atc-sensor-cytosol/spec.md), [SensorCytosol[pH ⟶ PLA1]](../../modules/ph-sensor-cytosol/spec.md), [SensorCytosol[theophylline ⟶ LacZ]](../../modules/theophylline-sensor-cytosol/spec.md) |
| Polyphosphate | 100-mer polyphosphate | PPK2 | ATP from AMP and ADP, and GTP from GDP | [Energy: PPK](../../modules/energy-ppk/spec.md), a member of [Energy](../../modules/energy/spec.md) |

# What selects a route

- **Both can run together, and together did best.** In PURE reactions, the polyphosphate route alone gave about 77% less protein than the creatine phosphate route alone, and the two together gave about 96% more than creatine phosphate alone. See [Energy: PPK](../../modules/energy-ppk/spec.md).
- **Magnesium.** The polyphosphate route is highly sensitive to the Mg²⁺ concentration, and needs about 10 mM more Mg²⁺ than the reaction otherwise carries. See the Requirements of [Energy: PPK](../../modules/energy-ppk/spec.md).
- **What the spent nucleotide is.** PPK2 acts on AMP directly. Creatine kinase acts on ADP, so on that route the AMP left by translation has to pass through AK first.

# Not yet attested

- The polyphosphate route in Base Cytosol. Energy: PPK's page records it as not yet validated there, and its results come from PURE reactions.
- Which route [S30 Lysate](../../modules/s30-lysate/spec.md) uses, or whether NEB PURExpress, as used in [Emitter: IV-HSL](../../modules/emitter-ivhsl/spec.md), uses creatine phosphate. Neither composition is stated.
- How long either store lasts in a reaction, or which one runs out first when both are present.
- A measured osmotic change from regeneration, in any compartment.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
