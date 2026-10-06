---
title: Expression
subtitle: "Process"
status: draft
---

# Overview

Expression makes a protein inside a reaction from a DNA template, instead of adding the protein already purified. The cytosol supplies the machinery and the template supplies the sequence. Everything stays in one compartment, so the protein appears in the spent reaction rather than in a container of its own.

Its two instances:

- **Expression in situ**, where the protein is made in the reaction that uses it.
- **Standalone expression**, where a separate reaction runs first and a volume of it is added to a fresh one.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# What every instance shares

**Expression is two operations, not one.** It is transcription followed by translation, `express = translate ∘ transcribe`, a composition and not a primitive operation.

**One compartment throughout.** The two profiles read `transcribe : Cytosol ⊞ DNA[promoter p] ⟶ Cytosol′ ⊞ RNA` and `translate : Cytosol ⊞ RNA ⟶ Cytosol′ ⊞ Protein`. `⊞` is mixing, so the product is in the reaction and not behind a boundary. `Cytosol′` marks a cytosol that is present and changed.

**The cytosol survives and is altered.** The reaction that expressed a protein is not the reaction it started as. Its nucleotides are spent and its transcript is in it.

**The guard sits on transcription.** `p ∈ P(cytosol)`: the template's promoter must be one this cytosol's polymerase reads. A T7 promoter needs a cytosol carrying T7 polymerase. **Translation has no guard**, so nothing restricts what may be translated.

# The two instances are two compositions of one operation

**The difference is not in the operation.** It is an identity question about two operands, and a composition graph already states it.

**In situ is one cytosol.** `express` runs and the protein is used in the compartment that made it. The producing and the consuming cytosol are the same object.

**Standalone is two.** `express` runs in the first, and a `mixing` step carries `Cytosol′ ⊞ Protein` into a fresh one. **One node against two, with a mixing step between them.**

**The split belongs to the composition, not to the operation.** An operator is selected per instance and not per type. The output of standalone expression is the input to an Assemble Cytosol step, which uses some of the headroom of the fresh cytosol.

**One half of the difference does not dissolve.** Standalone expression spends the receiving cytosol's headroom (see [Assemble Cytosol](../assemble-cytosol/assemble-cytosol-main.md)).

# What the instances do not share

| | In situ | Standalone |
| --- | --- | --- |
| When the protein appears | during the reaction that uses it | before that reaction starts |
| What the working reaction receives | a template | a volume of spent reaction |
| Who pays the energy | the working reaction | a separate one |
| Dose control | let the protein accumulate, then add the analyte | a known volume at an unknown concentration |

**The dose row is the one that matters and it is asymmetric.** In situ expression gives no concentration, so the practice is to wait rather than to measure. Standalone expression gives a volume and still no concentration. **Neither route yields a number**, so every amount stated for an expressed protein is a volume or a time.

**Standalone expression has a parameter in situ does not have.** The protein exists before the working reaction starts, so it can be held with its partner first. On the EsaR route, 15 min of repressor with its template gives about a twofold change and 1 h gives about fivefold, at the same doses. In situ there is nothing to hold: the protein appears in the reaction that uses it.

# Choosing between the instances

**One comparison exists and it cannot separate the route from the preparation.** [tetR-aTc Detector](../../modules/detector-tetr-atc/spec.md) describes three formats of TetR: purified protein, expression in situ from `pT7-tetR`, and expression overnight followed by combination with a fresh reaction. **Only the third has induced** in Nucleus Cytosol.

**That result does not support a rule.** The only preparation that induced was also the only cell-free one, and both purified arms failed. **In situ expression was not tested at all.** The result shows one route that worked. It does not show that expression beats purification, or which expression route is better.

**A second comparison exists inside one route and it does support something.** The EsaR detector ran the same standalone route with two donor incubations, 3 h at 37 °C and 17 h at 30 °C, everything else held. The fold change was the same and the yield was lower for the longer donor. That compares two donors rather than two routes, so it says nothing about in situ or purified protein — but it does say the donor's incubation is a variable, not a detail of how the protein was made.

# Requirements

Requires a cytosol whose polymerase reads the template's promoter. See [Base Cytosol](../../modules/base-cytosol/spec.md).

Requires energy and machinery that other reactions in the same compartment also want. **Expression competes for ribosomes.**

**Standalone expression carries its whole reaction across.** [tetR-aTc Detector](../../modules/detector-tetr-atc/spec.md) adds 2.5 µL of an 18 h reaction run at 30 °C. [Detector: 3OC6-HSL (EsaR)](../../modules/detector-esar/spec.md) adds about a fifth of its reaction, 14 µL in 65 µL. Everything else in those volumes arrives with the protein.

**What arrives is not inert, and the donor's age decides which way it cuts.** At a held template dose the EsaR route raised reporter yield — a reaction at a tenth of the control's template reached the control's yield — which points at unspent energy. Running the same donor for 17 h at 30 °C instead of 3 h at 37 °C lowered the yield while holding the fold change, which points at byproducts, inorganic phosphate among them. **So a donor run longer is not a donor run better.**

# Modules

- [Base Cytosol](../../modules/base-cytosol/spec.md) — supplies transcription and translation
- [Reporter](../../modules/reporter/spec.md) — expresses the reporter from a DNA template
- [Reporter: XylE](../../modules/reporter-xyle/spec.md) — expresses the catecholase (XylE) from a DNA template
- [Membrane Pore: Cx43](../../modules/membrane-pore-cx43/spec.md) — expressed in situ from a co-encapsulated plasmid
- [CRAIC](../../modules/craic-cascade/spec.md) — expresses EsaR from a DNA template before the sensor is assembled
- [tetR-aTc Detector](../../modules/detector-tetr-atc/spec.md) — describes all three supply formats and compares them

# Processes

:::{attention} No Process page for either instance
@Editor: write a Process page for expression in situ and one for standalone expression, and list them here.
:::
