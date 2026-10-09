---
title: "Osmometry Readout"
subtitle: "Process"
status: draft
---

# Overview

Osmometry Readout reads the osmolality of a solution and yields one number, in mOsm/kg. It counts every dissolved particle, whatever it is: a sugar, a buffer, each ion of a salt, and whatever a purified stock arrived with.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. No recorded run names the standard it read before its samples — see Materials and Equipment.
:::

**Its one recorded job is setting an outer solution against an inner one.** Read the inner solution, then make the outer solution, read it, and adjust it until it reads 100 mOsm/kg to 150 mOsm/kg lower ([Nucleus Base Cell Testing](https://devnotes.nucleus.engineering/articles/base-cell-01)). [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) does this before it encapsulates. It is how the function of an [Outer Solution](../../modules/outer-solution/spec.md) is checked: every member is defined by how its osmolarity relates to the inner solution of whatever it suspends, not by its solutes.

**The sample does not survive the reading.** The 10 µL aliquot stays in the instrument and does not go back into the tube. In the DevNote above that is 10 µL of a 40 µL inner solution, and the other 30 µL is encapsulated, so plan the volume for it.

**It reads a solution, never a lumen.** Once a solution is inside a cell it is out of reach. So the inner solution is read before encapsulation, and its osmolarity afterwards is computed: from what was encapsulated, and from what the reactions inside do as they run. A comparison across a membrane therefore pairs a measured outside with a computed inside. A reaction run in parallel with no membrane around it can be read, and it is a stand-in for the lumen, not the lumen: it shares the chemistry and has no membrane.

# Materials and Equipment

- A vapor-pressure osmometer. The one on record is a Wescor EliTech Vapro 5600 Vapor Pressure Osmometer ([Nucleus Base Cell Testing](https://devnotes.nucleus.engineering/articles/base-cell-01)).
- A standard of known osmolality, close to the readings you expect.

:::{attention} No run records its standard
No page or DevNote here records which standard was read, at what value, or how often the instrument was checked against it. @Editor: supply them per run.
:::

# Protocol

- [ ] Read the standard first. Go on only if it reads within the tolerance the instrument's manual gives.
- [ ] Take a 10 µL aliquot of the solution to read. For an inner solution, take it after mixing and before encapsulation, and keep the rest on ice.
- [ ] Load and read the aliquot as the instrument's manual describes.
- [ ] Record the reading in mOsm/kg, with the solution it came from: an inner solution, an outer solution, or a reaction run in parallel with no membrane.
- [ ] Read the inner and outer solutions on the same instrument in the same session. The window is a difference between two readings, so an offset between two instruments lands inside it.

# Which Unit a Figure Takes

The instrument reads **osmolality**: osmoles per kilogram of water, in mOsm/kg. **Osmolarity** is osmoles per liter of solution, in mOsm/L. A recipe yields osmolarity, and so does any figure computed from a composition. A reading yields osmolality. The two are different quantities, so a figure takes the unit of where it came from, and the unit is written with it. A bare mOsm does not say which one it is, so it marks a figure whose origin is not recorded, and nothing else.

**A reading is recorded in mOsm/kg.** Converting it to osmolarity is optional: osmolarity is osmolality times the kilograms of water in one liter of the solution that was read.

**If you convert, take the water from the solution's composition table, and cite that table's label beside the converted figure.** A liter of solution holds less than a kilogram of water, because its solutes take up some of the room. The table says how much of each solute a liter holds.

**Where the water cannot be worked out, keep the reading in mOsm/kg and do not convert it.** Do not assume that a liter holds a kilogram of water. That is a conversion too, made without saying so, and it is furthest from true in the strongest solutions.

**A window between two readings does not convert by one factor.** Each side converts with its own water, and a sugar takes more room for each osmole than a salt does. So where the two solutions hold different solutes, as a cytosol and a glucose outer solution do, the window in mOsm/L is not the window in mOsm/kg scaled.

# Quality Control

**A reading names its sample and its unit.** A figure with no solution named against it cannot be compared with anything, and a figure with no unit cannot be compared with a recipe.

**A concentration is not a reading.** A recipe states what was pipetted, and the osmometer reads what the solution does. In the DevNote above, 850 mM glucose read 950 mOsm/kg. Measure a solution made by recipe, and do not take its concentration as its reading.

**An inner solution read before encapsulation describes that moment only.** The reactions inside change it as they run, and the window above was measured as the vesicles form. A reading says nothing about how long the balance holds.

# Processes

- [Assay](../assay/main.md) — the abstraction this process is an instance of. It reads something and yields a value.
- [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) — reads its inner and outer solutions this way before it encapsulates.
- [Assemble Outer Solution](../assemble-outer-solution/main.md) — makes the solution this process reads most often.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
