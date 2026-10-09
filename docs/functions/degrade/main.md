---
title: "Degrade"
subtitle: "Function"
status: draft
---

# Overview

Degrade breaks down a molecule that is mixed with the thing doing it. It has four kinds, by what is broken down: protein, RNA, DNA and pyrophosphate (PPi). Within each kind, an instance differs in **how specific it is**. [Control: ClpXP](../../modules/control-clpxp/spec.md) breaks down only proteins that carry a tag. Proteinase K breaks down any protein. Inorganic pyrophosphatase splits only pyrophosphate. [S30 Lysate](../../modules/s30-lysate/spec.md), an *E. coli* extract, breaks down protein, RNA and DNA at a baseline rate, as a side effect of what it is made from.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Type

Degrade takes the degrader and what it acts on, and returns the degrader unchanged, with the target broken down. It acts on everything it can reach and recognizes, not on one chosen molecule. So a degrader placed with something it recognizes breaks it down whether or not that was intended, and what protects a molecule is being outside what the degrader recognizes, or out of its reach.

# Substrates and products

| | Consumes | Produces | Unchanged |
| --- | --- | --- | --- |
| **Tag-specific protease**, ClpXP | the tagged protein, and ATP, which becomes ADP and phosphate | the protein, in pieces | ClpX, ClpP, and every protein without the tag |
| **Nonspecific protease** | any protein it reaches | the protein, in pieces | the protease |
| **RNase** | RNA | the RNA, in pieces | the RNase |
| **DNase** | DNA | the DNA, in pieces | the DNase |
| **Pyrophosphatase** | one pyrophosphate | two phosphates | the pyrophosphatase |

**What this does to the number of dissolved particles.** Breaking one molecule into pieces raises the count, and so does each ATP that ClpXP turns into ADP and phosphate. For pyrophosphate the count is exact, as an estimate for an ideal solution: one PPi becomes two phosphates, so each split adds one. For the others it depends on how many pieces each molecule gives and how much ATP each costs, and no page records either. No run has measured any of it.

# Routes

| Kind | Instance | Specificity | Realized by |
| --- | --- | --- | --- |
| Protein | tag-specific | only proteins carrying the ssrA tag, using ATP | [Control: ClpXP](../../modules/control-clpxp/spec.md), a member of [Control](../../modules/control/spec.md) |
| Protein | nonspecific | any protein | proteinase K, added in [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md). The baseline protease activity of [S30 Lysate](../../modules/s30-lysate/spec.md) |
| RNA | nonspecific | any RNA | the baseline RNase activity of S30 Lysate |
| DNA | nonspecific | any DNA; a linear molecule is broken down from its ends, and a circular one is spared | the baseline DNase activity of S30 Lysate |
| Pyrophosphate | specific | only pyrophosphate | inorganic pyrophosphatase (PPiase), in [Base Cytosol](../../modules/base-cytosol/spec.md) and the sensor cytosols built on it: [SensorCytosol[aTc ⟶ PLA1]](../../modules/atc-sensor-cytosol/spec.md), [SensorCytosol[pH ⟶ PLA1]](../../modules/ph-sensor-cytosol/spec.md), [SensorCytosol[theophylline ⟶ LacZ]](../../modules/theophylline-sensor-cytosol/spec.md) |

Everything said of S30 Lysate here holds for [SensorCytosol[3OC6-HSL ⟶ PLA1]](../../modules/ahsl-sensor-cytosol/spec.md), which is built on it. Every [Protein](../../modules/protein/spec.md) is sensitive to a protease, and every [RNA](../../modules/rna/spec.md) to an RNase. Those pages state the sensitivity; this page states what imposes it.

# What selects a route

- **What the target carries, for ClpXP.** ClpXP breaks down a protein only if it carries the ssrA tag. A protein is protected from it by leaving the tag off, and made a target by adding it. See [Control: ClpXP](../../modules/control-clpxp/spec.md).
- **Where the degrader is, for proteinase K.** It breaks down any protein it reaches, so it is used only where the protein to keep is behind a membrane and the protein to remove is outside. See [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md).
- **Whether the cytosol carries it, for pyrophosphatase.** [Transcribe](../transcribe/main.md) and [Translate](../translate/main.md) both release pyrophosphate. Where nothing splits it, it binds Mg²⁺ and the two can precipitate together. Base Cytosol lists the enzyme with an amount, so its pyrophosphate is split as it is made.
- **What is added against it, for S30 Lysate.** Its activity is not chosen: it comes with the extract. A recipe works around it. An RNase inhibitor is added against the RNase, and a DNA template is supplied as a circular plasmid, because a linear one is broken down from its ends and nothing is added to protect it. See [S30 Lysate](../../modules/s30-lysate/spec.md).

# Not yet attested

- How much ATP ClpXP uses for each protein it breaks down, or how fast it works at a given amount.
- A proteinase K concentration, reaction volume or time. [Degrade Exterior LacZ](../../processes/degrade-exterior-lacz/main.md) flags all three as not yet established.
- How fast S30 Lysate breaks down protein, RNA or DNA, or whether adding GamS, which blocks the breakdown of linear DNA in *E. coli* extracts, would let a linear template work in it.
- A Module that breaks down RNA or DNA by design.
- Whether S30 Lysate, or NEB PURExpress as used in [Emitter: IV-HSL](../../modules/emitter-ivhsl/spec.md), carries a pyrophosphatase. Neither composition is stated.
- Whether Base Cytosol, which is assembled from purified components, has any of this activity. Its page accepts a linear template, which suggests it breaks down little or no DNA.
- A measured osmotic change from degradation, in any compartment.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node.
:::
