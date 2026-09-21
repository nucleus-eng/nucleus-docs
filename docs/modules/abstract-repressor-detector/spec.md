---
title: "Abstract: Repressor Detector"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

An abstract Module: the class of Detectors in which a repressor holds a gene off until the analyte relieves it. It refines [Abstract: Detector](../abstract-detector/spec.md), and an abstract Module is a Module.

**The invariant is two elements and a release.** A repressor element binds a DNA regulatory element and holds expression down. The analyte binds the repressor and the repressor lets go. Expression goes up.

**What varies is the analyte, the pair that implements the binding, and how the repressor element is supplied.**

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

**Members are a different relation from constituents.** In `compositional-biology-theory`, `glossary.md#T34` makes Constituent a containment relation and `glossary.md#T13` makes membership a matter of what a sort classifies.

**This class has constituents where its parent has none.** The invariant names a composition: a repressor element together with the DNA regulatory element it binds. Two things, and they are separate molecules. [Abstract: Detector](../abstract-detector/spec.md) names no composition at all, so the line between having parts and not having them falls between that page and this one.

:::{table} The constituents, abstractly.
| Constituent | What it is | Supplied as |
| --- | --- | --- |
| Repressor element | binds the regulatory element and holds the gene off | a purified protein, or DNA that expresses one in place |
| DNA regulatory element | the operator or promoter the repressor binds | DNA, always |
:::

:::{table} The members.
| Member | Analyte | Repressor and regulatory element | Built |
| --- | --- | --- | --- |
| [tetR-aTc](../detector-tetr-atc/spec.md) | aTc | TetR at a `tetO` operator | yes |
| [LacI-IPTG](../detector-laci-iptg/spec.md) | IPTG | LacI at a `lacO` operator | yes |
| Repressor AHL detector | 3OC6-HSL | EsaR | **no. London is designing it** |
:::

**The aTc detector is the concrete implementation to read first.** Jon, 2026-09-21. It is the member where every part of the invariant is present and built, so it is what this class is abstracted from rather than an example chosen after the fact.

**The third row is a position, not a Module.** It is where this class meets [Abstract: Detector](../abstract-detector/spec.md)'s AHL branch, and nothing occupies it yet. EsaR is a LuxR homolog that represses rather than activates, and it is available as purified protein, which is why the redesign can take the protein route.

# Requirements

Requires transcription and translation. Which kind follows the cytosol rather than the detector.

Requires an analyte that reaches the repressor element.

**Requires that the repressor element and the regulatory element be present together before the analyte arrives.** A repressor added after induction has nothing to relieve.

:::{attention} How the repressor is supplied is left open, and it decides how the two constituents compose
[LacI-IPTG](../detector-laci-iptg/spec.md) states the choice in its own prose: LacI is added *"either as a purified protein or by expressing it off of `pT7-lacI`."*

**Supplied as protein, the two are mixed.** Supplied as DNA, they are either two constructs mixed or one construct carrying both, which is a different operation. **So the same pair of constituents composes differently depending on a choice this class does not make.**

Both built members take the two-construct route: `pT7-tetR` with `pT7-tetO-plamGFP`, and `pT7-lacI` with `pT7-lacO-plamGFP`. Nothing in the corpus says whether that is a design choice or an accident.
:::

:::{attention} The supply choice is not functionally free, and calling it a parameter understates it
[tetR-aTc](../detector-tetr-atc/spec.md) records three formats, not two, and compares them: purified protein at 500 nM, expression in situ from `pT7-tetR`, and expression overnight followed by combination with a fresh reaction.

**All three repressed. Only the third induced.** That page states it plainly, and as of 2026-09-11 the overnight-expression format is the only one that has demonstrated induction in Nucleus Cytosol. The two that failed were a MedChem Express SUMO-His TetR and a foundry TetR, which makes the tag and the source **functional parameters rather than sourcing detail**.

**So the class leaves this open and a member cannot.** Choosing how to supply the repressor element decides how the two constituents compose, and it also decides whether the Module works at all. A page that offers the choice without saying which format has induced is offering a choice the corpus has already narrowed.
:::

:::{attention} What this class requires of its Context is not settled
An abstract Module carries an abstract Context that its members refine, ruled 2026-09-17. **How much that Context term carries, and how much is left to Requirements, is `open.md#O21`** in the theory corpus. Its expressiveness half closed on Jon's ruling of 2026-09-21 and its selection half is live.
:::

# Processes

None. An abstract Module names a class; the processes belong to its members.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
