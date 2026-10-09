---
title: Encapsulation
subtitle: "Process"
status: draft
---

# Overview

Encapsulation closes a lipid bilayer around an aqueous inner solution, so the result has an inside, a boundary and an outside where it had one phase before. It is the act that makes a compartment, and every route below it inherits that behavior rather than choosing one.

Its three instances:

- [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) — an inner solution is emulsified in a lipid-in-oil phase and drawn through an interface into an outer solution. Produces synthetic cells.
- [Encapsulation: Extrusion](../encapsulate-suv/main.md) — a dried lipid film is hydrated with the payload and extruded to a target size. Produces small unilamellar vesicles.
- [Encapsulation: Freeze-Thaw](../encapsulate-luv/main.md) — a dried lipid film is hydrated with the payload, sonicated and freeze-thawed, then washed by centrifugation. Produces large unilamellar vesicles.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# What every instance shares

**The result keeps two compartments, so this process packs.** The inner solution and the bilayer do not mix into one phase. That is the whole point of a boundary, and it is what separates this process from [Assemble Solution](../assemble-solution/assemble-solution-main.md), whose result shares one volume.

**The operator lives here, not on the routes.** Because the result keeps its parts separate, this process packs; and because every route is an instance of it, every route packs too. A newly written route needs no decision about which operator applies.

**What is inside is set before the boundary closes, not after.** No route loads a preformed compartment. The payload is present while the bilayer forms, which is why a payload that cannot survive the formation conditions cannot use that route.

# What the routes do not share

| | Phase Transfer | Extrusion | Freeze-Thaw |
| --- | --- | --- | --- |
| Product size class | synthetic cells, micron scale | SUVs, sub-micron | LUVs, size not measured |
| Method | emulsion and transfer through an interface | film hydration and extrusion | film hydration, sonication and freeze-thaw, washed by centrifugation |
| Target size | set by the emulsion | set by the extrusion membrane | not set by any step |
| Solvent exposure | the payload meets an oil phase | none | none |

**The size classes are never interchangeable.** A cascade that specifies one and receives the other is a different device. The routes are alternatives only where the size does not carry a function.

# Inputs

**Every route takes the same three and differs only in how it brings them together.** They are stated here once, and a route refines them rather than restating them — narrowing an input to a particular thing, or adding something the route itself imposes.

| Input | What it is | What a route may narrow it to |
| --- | --- | --- |
| [Membrane Components](../../modules/membrane-components/spec.md) | the molecules the bilayer will be made from | a named lipid mix |
| Inner solution | the aqueous phase that ends up inside | a cytosol, a substrate solution |
| [Outer solution](../../modules/outer-solution/spec.md) | the aqueous phase the result sits in | a named outer solution |

**The result is a membrane made of those components, holding the inner solution, in the outer one.**

**The membrane is an output here, not an input.** No route loads a preformed compartment: the bilayer closes around the payload while the payload is present. A page that makes a lipid film is making one of the three inputs above, not performing this process.

**What makes one solution "inner" is where it ends up, not what it is made of.** The same solution can be either, and on the pH route it is the outer solution that carries the trigger.

**The osmolarity of the two solutions must match.** That is a relation between the inputs rather than a property of either, so it is stated here once and holds for every route. A mismatch drives the contents across the bilayer before the device can do anything. See [Outer Solution](../../modules/outer-solution/spec.md).

# Requirements

**Requires that the payload survives the route, which is a property of the payload and the one thing the routes do not share.** The oil phase in phase transfer is one such case. Freeze-thaw also exposes the payload to freezing in liquid nitrogen and to sonication.

# Modules

- [Membrane Components](../../modules/membrane-components/spec.md) — what the bilayer is made from, and an input
- [Membrane](../../modules/membrane/spec.md) — the bilayer this process forms and closes
- [Cell](../../modules/cell/spec.md) — what phase transfer produces when the payload is a cytosol
- [Substrate Carrier](../../modules/substrate-carrier/spec.md) — what either route produces when the payload is a substrate
- [GUV](../../modules/guv/spec.md), [SUV](../../modules/suv/spec.md), [LUV](../../modules/luv/spec.md) — the size class each route produces

# Processes

- [Encapsulation: Phase Transfer](../assemble-base-cell/main.md)
- [Encapsulation: Extrusion](../encapsulate-suv/main.md)
- [Encapsulation: Freeze-Thaw](../encapsulate-luv/main.md)
