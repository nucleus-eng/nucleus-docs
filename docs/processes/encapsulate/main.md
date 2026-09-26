---
title: Encapsulation
subtitle: "Process"
status: draft
---

# Overview

Encapsulation closes a lipid bilayer around an aqueous inner solution, so the result has an inside, a boundary and an outside where it had one phase before. It is the act that makes a compartment, and every route below it inherits that behavior rather than choosing one.

Its two instances:

- [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) — an inner solution is emulsified in a lipid-in-oil phase and drawn through an interface into an outer solution. Produces synthetic cells.
- [Encapsulation: SUV](../encapsulate-suv/main.md) — a dried lipid film is hydrated with the payload and extruded to a target size. Produces small unilamellar vesicles.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Written 2026-09-24 because four whiteboards reached for it
The DevStudio day-one boards label this step `Encapsulation`, without naming a route, and the two routes each had a page while the thing they are routes of did not. This page is that parent. It states what both share and it is not a protocol: each route's own page is.
:::

# What every instance shares

**The result keeps two compartments, so this process packs.** The inner solution and the bilayer do not mix into one phase. That is the whole point of a boundary, and it is what separates this process from [Assemble Solution](../assemble-solution/assemble-solution-main.md), whose result shares one volume.

**The operator lives here, not on the routes.** Because the result keeps its parts separate, this process packs; and because both routes are instances of it, both pack too. A newly written route needs no decision about which operator applies.

**What is inside is set before the boundary closes, not after.** Neither route loads a preformed compartment. The payload is present while the bilayer forms, which is why a payload that cannot survive the formation conditions cannot use that route.

# What the two routes do not share

| | Phase Transfer | SUV |
| --- | --- | --- |
| Product size class | synthetic cells, micron scale | SUVs, sub-micron |
| Method | emulsion and transfer through an interface | film hydration and extrusion |
| Target size | set by the emulsion | set by the extrusion membrane |
| Solvent exposure | the payload meets an oil phase | none |

**The size classes are never interchangeable.** [Encapsulation: SUV](../encapsulate-suv/main.md) says so on its own page, and a cascade that specifies one and receives the other is a different device. The routes are alternatives only where the size does not carry a function.

# Requirements

Requires a lipid phase that will form a bilayer, and an aqueous payload stable in it.

Requires an outer solution whose osmolarity is matched to the interior. A mismatch drives the contents across the bilayer before the device can do anything, and the matching is a relation rather than a property of either solution. See [Outer Solution](../../modules/outer-solution/spec.md).

**Requires that the payload survives the route, which is a property of the payload.** The oil phase in phase transfer is the case this corpus has met.

# Modules

- [Membrane](../../modules/membrane/spec.md) — the class this process closes
- [Cell](../../modules/cell/spec.md) — what phase transfer produces when the payload is a cytosol
- [Substrate Carrier](../../modules/substrate-carrier/spec.md) — what either route produces when the payload is a substrate

# Processes

- [Encapsulation: Phase Transfer](../assemble-base-cell/main.md)
- [Encapsulation: SUV](../encapsulate-suv/main.md)
