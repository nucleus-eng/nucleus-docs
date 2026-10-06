---
title: "Detector: 3OC6-HSL (EsaR)"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`repressor-detector`](../repressor-detector/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

A 3OC6-HSL detector built on a repressor rather than an activator. EsaR is a LuxR homolog that represses where LuxR activates, so the logic is inverted: analyte relieves repression instead of switching a promoter on.

The [CRAIC](../craic-cascade/spec.md) cascade composes it, as design intent.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use. Every claim below is design intent, not a result.

@Editor(london): supply the EsaR construct, a working concentration and titration data.
:::

**Identity.** [UniProt P54293](https://www.uniprot.org/uniprotkb/P54293/entry) — Transcriptional activator protein EsaR, *Pantoea stewartii subsp. stewartii*, 249 residues. **The entry names it an activator; it is a repressor**, which is how every page here and the CRAIC design treat it.

# Reference Composition

The operator is `[EsaO]2`, two EsaO sites in tandem. A single-site version was built and is not in use.

The repressor is supplied in two steps, which is one more than every other detector has: the [CRAIC](../craic-cascade/spec.md) cascade expresses EsaR from a DNA template in one Base Cytosol, incubated overnight at 30 °C, and titrates the resulting protein into a second reaction carrying the operator construct.

:::{attention} Open question
@Editor(london): state whether the two-step expression belongs to this Module or to the cascade that uses it.
:::

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    ESAR["EsaR repressor"]
    DNA_REGULATORY_ELEMENT["DNA regulatory element"]

    P1_ASSEMBLE_THE_REPRESSOR_PAIR_0(["Assemble the repressor and its regulatory element (mixing) — no page"])
    DETECTOR_ESAR["Detector: 3OC6-HSL (EsaR)"]

    ESAR --> P1_ASSEMBLE_THE_REPRESSOR_PAIR_0
    DNA_REGULATORY_ELEMENT --> P1_ASSEMBLE_THE_REPRESSOR_PAIR_0
    P1_ASSEMBLE_THE_REPRESSOR_PAIR_0 --> DETECTOR_ESAR


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class ESAR,DNA_REGULATORY_ELEMENT leaf;
    class DETECTOR_ESAR composed;
    class P1_ASSEMBLE_THE_REPRESSOR_PAIR_0 process;

    click DETECTOR_ESAR "/docs/modules/detector-esar/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} DNA

:::{table} Linear templates. No sequence file is in `nucleus-eng/DNA` for any of them, so no length is claimed.
:label: comp-detector-esar-constructs

| Construct | Role |
| --- | --- |
| `T7-EsaR(D91G)-T7term` | The repressor template. **The repressor is a point mutant, D91G.** Expressed in its own reaction and titrated in as protein |
| `T7-[EsaO]2-mNG-T7term` | Characterization: two operator sites driving mNeonGreen, read as fluorescence |
| `T7-[EsaO]-mNG-T7term` | Single operator site. Built and used once, then dropped in favor of the dual-site construct |
| `T7-[EsaO]2-PLA1-T7term` | The cascade's own construct: the operator driving PLA1 |
| `T7-mNG-T7term` | The unrepressed control, with no operator |
:::

::::

:::::

# Expected Behavior

3OC6-HSL binds EsaR and relieves repression of the downstream coding sequence. **Repressors give lower noise floors than activators**.

**Characterized on a fluorescent reporter, not on the cascade's own output.** `[EsaO]2-mNG` was titrated against template at (0.1, 0.5 and 1) nM, with and without 5 µM 3OC6-HSL, against a fluorescein ladder at (0, 0.5, 1 and 2) µM. EsaR was held at a fixed dose. **This is the same split the aTc detector uses** — characterized on a reporter, built with PLA1 — so the measurement does not make the demonstration fluorescent.

:::{table} Repression against template concentration, at a fixed repressor dose.
:label: comp-detector-esar-repression

| Template | Repressor | Fold change, minus against plus 3OC6-HSL |
| --- | --- | --- |
| 0.1 nM | fixed, concentration not known | ~1.5 |
| 0.5 nM | fixed, concentration not known | ~2 |
| 1 nM | fixed, concentration not known | ~1, the readout gone |

:::

**A 1 hr pre-incubation at 37 °C raises fold change to 5x, and it is the largest effect on this page.** EsaR and the template are held together before the reaction starts, so the repressor is bound to the operator by the time transcription begins rather than competing with it. Nothing else here moves the readout that far.

**Magnesium does not.** A sweep at 0, 5, 10 and 20 mM *"had very little influence"*. That null is the control that isolates the pre-incubation: it says the gain comes from when the repressor meets the template, not from the reaction chemistry around it. **A reader given the magnesium sweep alone would take the wrong lesson** — that this Module is insensitive to its conditions, when it is strongly sensitive to one of them.

**Repression fails by template excess, not by a dead repressor.** A first titration moved the repressor against a fixed template and found no difference in output at either operator count. Reversing it — moving the template against a fixed repressor — gives the table above, so the repressor works and the earlier template dose was too high for it.

**The ratio that governs this has no measured value.** No build sheet records a stock or working concentration for the pre-expressed repressor, so the molar ratio cannot be computed from recorded numbers. The only figure anywhere is an estimate of **37.5:1** repressor to template, which assumes a repressor concentration of 576 nM that nothing measured. A target of **100:1** is named against it, and b.next works at **1000:1** purified TetR to tetO DNA.

:::{attention} The governing number is the one with no measurement behind it
The molar ratio of repressor to template decides whether this Module works, and it rests on an assumed repressor concentration. @Editor(london): measure the pre-expressed repressor, so the ratio stops being an estimate.
:::

:::{attention} No figure yet
@Editor(london): the titration above has no plot on this page. Add it, with the dose that was fixed.
:::

# Requirements

Requires the analyte to reach the repressor.

# Implementations

- [CRAIC Demo](../../implementations/devstudio-craic-demo/main.md): its detector — expressed from its own template, then gating PLA1.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.
:::
