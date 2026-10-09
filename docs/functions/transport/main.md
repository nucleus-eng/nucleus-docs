---
title: "Transport"
subtitle: "Function"
status: draft
---

# Overview

Transport moves cargo across a membrane through a pore. Three Modules here do it, and they split by **what each one selects on**: two pass anything below a size, and the third passes only small positive ions. All three are passive, so cargo moves down its own gradient and nothing is spent moving it.

**Every one of them is symmetric.** A pore does not know which way is in. Whatever it lets across can also leave, so opening a membrane obliges whatever is outside it as much as whatever is inside.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Transport takes a pore, a membrane and a cargo, and returns the membrane with the cargo now able to cross it. **The pore does not supply the membrane it opens**: it composes with one, and the membrane belongs to whatever the pore was added to. See [Pore](../../modules/pore/spec.md).

**What a pore passes is a property of the pore**, and every member states it differently: two as a size, one as a charge. A composition that needs a particular molecule across has to check that molecule against the pore's own statement, not against a general rule.

# Substrates and products

| | Consumes | Produces | Unchanged |
| --- | --- | --- | --- |
| **Passive transport** | nothing | the cargo, now on the other side | the pore, the membrane, and the cargo itself |

**No member consumes energy, and no member moves cargo against a gradient.** Transport here runs on the difference that is already there and stops when it is gone.

**What this does to the number of dissolved particles.** Inside and outside, taken together, nothing changes: a molecule leaves one side and arrives on the other. **What changes is each side on its own**, and that is the point of opening a membrane at all. A pore large enough to pass the solutes that set the osmotic difference across a membrane takes that difference away with them. No run has measured it.

# Routes

| Route | Selects on | Passes | Realized by |
| --- | --- | --- | --- |
| Size | the size of the cargo | molecules up to about 3 kDa, through an opening of (1.6–4.6) nm | [Membrane Pore: α-Hemolysin](../../modules/membrane-pore-ahly/spec.md) |
| Size | as above | molecules up to about 1 kDa | [Membrane Pore: Cx43](../../modules/membrane-pore-cx43/spec.md) |
| Charge | the charge and identity of the cargo, not its size | monovalent positive ions, and protons | [Membrane Pore: Gramicidin A](../../modules/membrane-pore-gramicidin/spec.md) |

**A size is a scale, not a filter.** α-Hemolysin's page says so itself: mass is one clause of what a pore passes, and a molecule near the limit is not settled by its mass alone.

# What selects a route

- **What has to cross.** Gramicidin A is used here for one job: letting H⁺ reach an encapsulated [Detector: pH-Sensing](../../modules/detector-ph/spec.md), so it can read the outer solution's pH. A pore that selects on size would pass far more than protons.
- **What must not cross.** Because transport is symmetric, the question is never only what you want in. A pore passing up to 3 kDa lets out anything inside below that size, so the outer solution has to be able to tolerate what leaves.
- **What the pore costs elsewhere.** Gramicidin A ruptured some dye-loaded liposomes in one cascade, so its own page says not to add it to a colorimetric readout. That is a reason to choose a different pore, not a property of transport. See [Lyse](../lyse/main.md).
- **Whether the Module is distributable.** α-Hemolysin is not actively supported here, because the Distribution does not support BSL-2 reagents. Its page recommends Cx43 for new work.

# Not yet attested

- Any active transport: a Module that moves cargo against a gradient, and spends energy to do it.
- A transport rate for any member, or how long a compartment takes to equalize once a pore is in it.
- A measured osmotic change from opening a membrane, in any compartment.
- A pore that selects on something other than size or charge, such as a specific molecule.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
