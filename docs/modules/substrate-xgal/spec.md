---
title: "Substrate: X-Gal"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

X-Gal is 5-bromo-4-chloro-3-indolyl-β-D-galactopyranoside, a second chromogenic substrate for the [LacZ Reporter](../reporter-lacz/spec.md) pair. It is colorless; [LacZ](../reporter-lacz-enzyme/spec.md) cleaves it to an indigo product that is **insoluble and precipitates where it forms**.

**That precipitation is the reason to use it, and it is the one thing [CPRG](../substrate-cprg/spec.md) cannot do.** Cleaved CPRG is highly soluble, so in a patterned gel the magenta product diffuses out of the shape that produced it — visibly within hours. X-Gal's product stays put. A pattern read at 15 h has smeared in CPRG and held in X-Gal, and a gel kept for two weeks still showed the pattern.

**The same enzyme, so it composes the same way.** Anywhere the reporter pair appears, either substrate can fill the substrate half. The choice is between a fast soluble readout and a slow spatially stable one.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. One result from one lab stands behind it.
:::

(substrate-xgal-reference-composition)=
# Reference Composition

:::{table} X-Gal by format.
:label: comp-substrate-xgal

| Format | Working concentration | Notes |
| --- | --- | --- |
| Free in the gel | 0.49–6.12 mM | Chicago Node, Liu Lab, in 0.7% agarose. Two sources disagree with the arithmetic — see the note below. Do not cite a single value |
| Encapsulated in a liposome | **not possible** | see Requirements — X-Gal needs DMSO, and DMSO ruins liposome formation |
:::

:::{attention} The working concentration is not established
Sources give X-Gal free in the gel as **2.5 mg/mL (6.12 mM)**, but the protocol that states that figure adds 1 µL of a 1% stock to a 50 µL gel, which is **0.2 mg/mL (0.49 mM)** — a 12.5-fold disagreement inside one document. The stated final is the likelier error, so **0.49 mM** is the working figure pending the Node. Until it is resolved, treat **0.49 mM to 6.12 mM** as the bracket and do not cite a single value.

Specify X-Gal in **molar units**. A mass concentration hides the comparison with [CPRG](../substrate-cprg/spec.md), which is specified molar, and the two are substrates for the same enzyme.
:::

@Editor(chicago): is the dye line 1 µL or 5 µL? At 1 µL of a 1% stock the inset gel gets 0.49 mM, not the 2.5 stated in either unit. 5.11 µL would give 2.5 mM. Also say whether the figure carries to gels other than 0.7% agarose.

(substrate-xgal-expected-behavior)=
# Expected Behavior

## Gels

Expect a visible blue color change more slowly than CPRG, and a pattern that survives far longer.

| | CPRG | X-Gal |
| --- | --- | --- |
| First visible change | ~15 min | ~1 h |
| Robust change | ~1 h | ~2 h |
| Pattern at 15 h | diffused | held |
| Pattern at 2 weeks | — | still held |

Both figures are from one experiment: a two-population agarose gel with β-galactosidase encapsulated in GUVs, substrate free in the bulk, and PLA1 supplied as a bulk cell-free product, at 37 °C.

:::{attention} Not yet validated in Nucleus Cytosol
This substrate has not been used with a Nucleus Cytosol cascade. The result behind it used a purified enzyme system and bulk PLA1, not a sensing cell.
:::

(substrate-xgal-requirements)=
# Requirements

Requires [LacZ Enzyme](../reporter-lacz-enzyme/spec.md) to produce a signal — X-Gal alone is inert and colorless.

**Requires that enzyme and substrate stay apart until the readout**, as the reporter pair always does. Here that is done by keeping the substrate free in the gel and the enzyme inside a liposome, rather than the other way round.

**Cannot be liposome-loaded.** X-Gal has limited aqueous solubility and is dissolved in DMSO, and DMSO ruins liposome formation — attempts to make SUVs with it gave poor vesicles. So X-Gal can only be the free half of the pair, which inverts the arrangement CPRG allows. Where CPRG can be held in a substrate liposome and released by lysis, X-Gal requires that the **enzyme** be the encapsulated half.

**Expected to be light-sensitive**, as CPRG is, so a photodeveloped gel should add it after crosslinking rather than before. @Editor(chicago): this has not been tested — CPRG's UV bleaching is documented and X-Gal's is inferred from it.

# Processes

- [Colorimetric Readout](../../processes/colorimetric-readout/main.md) — the conversion this substrate undergoes.
- [Hydrogel Embedding: Alginate](../../processes/embed-alginate-hydrogel/main.md) and the agarose routes — where the substrate is dosed free into the matrix.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::

Demonstrated by Samuel J. Chen ([ORCID](https://orcid.org/0000-0001-8501-7175)) (Chicago Node, Liu Lab).
