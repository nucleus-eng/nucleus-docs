---
title: "Hold"
subtitle: "Function"
status: draft
---

# Overview

Hold keeps what is inside a container in a fixed relation to what is outside it, and to the other things inside. Nineteen Modules here do it, by three mechanisms: a membrane holds a volume behind a barrier, a gel holds things in position, and a solution holds its solutes in one phase. **It is the most widely held Function in this corpus**, because every cytosol and every outer solution is a solution, and a solution holds.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Hold takes a container and a thing, and returns the container with the thing inside it in a fixed relation. **The class does not fix what the boundary is made of**, whether it is a surface or a network, or whether the inside is a volume or a position. See [Container](../../modules/container/spec.md).

**Holding is what makes a compartment a compartment**, so most other Functions here happen inside something that is holding. A cytosol transcribes, and it also holds what transcribes.

# Substrates and products

| | Consumes | Produces | Unchanged |
| --- | --- | --- | --- |
| **Every member** | nothing | the contents, now in a fixed relation to each other and to what is outside | the container and the contents |

**Holding is a relation and not a reaction.** Nothing is used up, and nothing new is made.

**What this does to the number of dissolved particles.** Nothing. **What holding does instead is make the count mean something**: it is only because a membrane holds that an inside and an outside can have different counts at all, which is what every osmotic figure in this corpus is about.

# Routes

| Route | How it holds | What it does not do | Realized by |
| --- | --- | --- | --- |
| Membrane | a closed lipid bilayer. The contents are a volume, and something must cross a barrier to get in or out | does not fix position within the volume | [Membrane: POPC](../../modules/membrane-popc/spec.md), [Membrane: POPC/Chol (7:3)](../../modules/membrane-popc-chol/spec.md), [Membrane: POPC/Chol (9:1)](../../modules/membrane-popc-chol-9-1/spec.md) |
| Gel | a polymer network. The contents are fixed in position and stay in contact with the solution around them | does not separate the contents from that solution | [Gel: Alginate](../../modules/gel-alginate/spec.md), [Gel: LGA](../../modules/gel-lga/spec.md), [Gel: PEG-Norbornene](../../modules/gel-peg-norbornene/spec.md), [Gel: PEGDA](../../modules/gel-pegda/spec.md), [Gel: ULGA](../../modules/gel-ulga/spec.md) |
| Solution | dissolution. The contents are free to move through one phase | separates them from nothing | the cytosols — [Base Cytosol](../../modules/base-cytosol/spec.md), [S30 Lysate](../../modules/s30-lysate/spec.md), [SensorCytosol[3OC6-HSL ⟶ PLA1]](../../modules/ahsl-sensor-cytosol/spec.md), [SensorCytosol[aTc ⟶ PLA1]](../../modules/atc-sensor-cytosol/spec.md), [SensorCytosol[pH ⟶ PLA1]](../../modules/ph-sensor-cytosol/spec.md), [SensorCytosol[theophylline ⟶ LacZ]](../../modules/theophylline-sensor-cytosol/spec.md), [Emitter: IV-HSL](../../modules/emitter-ivhsl/spec.md), [Energy: PPK](../../modules/energy-ppk/spec.md) — and the outer solutions: [Outer Solution: Glutamate-HEPES-Glucose](../../modules/outer-solution-glutamate/spec.md), [Outer Solution: Tris-HEPES](../../modules/outer-solution-tris-hepes/spec.md), [Outer Solution: Glucose-HEPES](../../modules/outer-solution-glucose-hepes/spec.md) |

**Nothing is left out of this list.** Every Module that refines Container holds, by Container's own definition, so there is no member here that the walk reaches and the page declines.

# What selects a route

- **Whether the contents must be separated, or only placed.** A membrane separates and a gel does not. A gel holds cells in fixed relation to one another while leaving them in contact with the solution around them, which is what a readout outside the cells needs.
- **Whether something must cross.** A membrane's barrier is the thing that makes [Transport](../transport/main.md) a question and [Lyse](../lyse/main.md) a trigger. Neither applies to a gel or a solution, because neither has a barrier to cross or to break.
- **They compose, and in practice all three are used at once.** A cascade here is cells held by membranes, suspended in a solution, set into a gel. Each layer holds what the one inside it does not.

# Not yet attested

- How long any member holds. Every figure here is from formation or from a single reading, and nothing records a container failing over time except where something was added to make it fail.
- A container that holds by a fourth mechanism.
- Whether a gel changes what reaches the cells it holds, beyond what its solution already sets.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
