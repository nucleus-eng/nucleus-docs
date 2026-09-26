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

:::{attention} Written 2026-09-25 because three steps run it and none can name it
`reporter/spec.yml` runs `express-the-reporter`, `reporter-xyle/spec.yml` runs `express-catecholase`, and `membrane-pore-cx43/spec.yml` expresses Cx43 from a co-encapsulated plasmid. **All three carry `process.page: null`.** The DevStudio CRAIC board draws a fourth, a pre-expression step before the sensor is assembled.

**Neither instance is written, so this parent arrives before its children.** That inverts the usual order and the corpus has the case already: [Detector](../../modules/detector/spec.md) records an abstraction that predicts a Module rather than recording one.
:::

# What every instance shares

**Expression is two operations, not one.** `compositional-biology-theory` `signature.md:261` at `06527cf` writes `express = translate ∘ transcribe`, and marks it **composite, not a generator**. So this page names a composition that the register already has, and it adds no operation.

**One compartment throughout, and the register says so with its operator.** The two profiles read `transcribe : Cytosol ⊞ DNA[promoter p] ⟶ Cytosol′ ⊞ RNA` and `translate : Cytosol ⊞ RNA ⟶ Cytosol′ ⊞ Protein`. **`⊞` is mixing**, so the product is in the reaction and not behind a boundary. **All three steps in this corpus use `mixing`**, which agrees.

**The cytosol survives and is altered.** `Cytosol′` is the register's mark for *present and changed*, `signature.md:162`. The reaction that expressed a protein is not the reaction it started as. Its nucleotides are spent and its transcript is in it.

**The guard sits on transcription.** `p ∈ P(cytosol)`: the template's promoter must be one this cytosol's polymerase reads. A T7 promoter needs a cytosol carrying T7 polymerase. **The translation guard is declared and empty**, so nothing in the register restricts what may be translated.

# The two instances are two compositions of one generator

**The difference is not in the operation.** It is an identity question about two operands, and a
composition graph already states it.

**In situ is one cytosol.** `express` runs and the protein is used in the compartment that made it.
The producing and the consuming cytosol are the same object.

**Standalone is two.** `express` runs in the first, and a `mixing` step carries `Cytosol′ ⊞ Protein`
into a fresh one. **One node against two, with a mixing step between them.**

**So naming the split on `express` would record in the operation what the composition says**, which
is the mistake this corpus refuses elsewhere: an operator is selected per instance and not per type.
The `compositional-biology-theory` session reaches the same reading and reports Jon reaching it
first, 2026-09-25, in their words: *"the output of that process is just the input into another
assemble cytosol step, using some of the headroom of the fresh Cytosol."*

**One half of the difference does not dissolve, and no schema records it.** Standalone expression
spends the receiving cytosol's headroom. `spec.yml` has `headroom.provides` for what a Module
**gives**, used on 2 of 95 steps, and **no key for what an operand takes.**

# What the instances do not share

| | In situ | Standalone |
| --- | --- | --- |
| When the protein appears | during the reaction that uses it | before that reaction starts |
| What the working reaction receives | a template | a volume of spent reaction |
| Who pays the energy | the working reaction | a separate one |
| Dose control | let the protein accumulate, then add the analyte | a known volume at an unknown concentration |

**The dose row is the one that matters and it is asymmetric.** In situ expression gives no concentration, so the practice is to wait rather than to measure. Standalone expression gives a volume and still no concentration. **Neither route yields a number**, which is why every amount recorded for an expressed protein in this corpus is a volume or a time.

# What the corpus knows about choosing between them

**One comparison exists and it cannot separate the route from the preparation.** [tetR-aTc Detector](../../modules/detector-tetr-atc/spec.md) records three formats of TetR: purified protein, expression in situ from `pT7-tetR`, and expression overnight followed by combination with a fresh reaction. **Only the third has induced** in Nucleus Cytosol.

**That result does not license a rule.** The page states the problem itself: the only preparation that induced was also the only cell-free one, and both purified arms failed. **In situ expression was not tested at all.** So nothing here says that expression beats purification, and nothing says which expression route is better.

**Read it as one route that worked, not as a ranking.**

# Requirements

Requires a cytosol whose polymerase reads the template's promoter. See [Base Cytosol](../../modules/base-cytosol/spec.md).

Requires energy and machinery that other reactions in the same compartment also want. **Expression competes for ribosomes**, which is why the register marks an untouched operand `X*` and treats that mark as a claim that can be false.

**Standalone expression carries its whole reaction across.** The Chicago route adds 2.5 µL of an 18 h reaction run at 30 °C. Everything else in that volume arrives with the protein.

# Modules

- [Base Cytosol](../../modules/base-cytosol/spec.md) — supplies transcription and translation
- [Reporter](../../modules/reporter/spec.md) — runs `express-the-reporter`
- [Reporter: XylE](../../modules/reporter-xyle/spec.md) — runs `express-catecholase`
- [Membrane Pore: Cx43](../../modules/membrane-pore-cx43/spec.md) — expressed in situ from a co-encapsulated plasmid
- [tetR-aTc Detector](../../modules/detector-tetr-atc/spec.md) — records all three supply formats and compares them

# Processes

**Neither instance has a page.** When they are written, they belong here.
