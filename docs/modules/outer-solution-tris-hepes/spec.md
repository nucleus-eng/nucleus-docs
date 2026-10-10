---
title: "Outer Solution: Tris-HEPES"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [Solution](../solution/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

A member of [Outer Solution](../outer-solution/spec.md): a Tris-HEPES stock with an energy solution. It is the solution the pH path's cells sit in.

**The agarose dissolves into this and both cell populations sit in it**, so this osmotic concentration sets the gel's.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

<!-- composition-tabs: no-dna (the energy solution here is a buffer component of this
     solution, not the Energy: PPK Module. The checker prefix-matches ENERGY and cannot
     tell the two apart, so this is a false positive rather than a missing tab) -->

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    TRIS_HEPES_STOCK["Tris-HEPES buffer stock"]
    ENERGY_SOLUTION["Energy solution"]
    WATER["Water"]

    P1_ASSEMBLE_OUTER_SOLUTION_0(["Assemble Outer Solution (mixing)"])
    OUTER_SOLUTION_TRIS_HEPES["Outer Solution: Tris-HEPES"]

    TRIS_HEPES_STOCK --> P1_ASSEMBLE_OUTER_SOLUTION_0
    ENERGY_SOLUTION --> P1_ASSEMBLE_OUTER_SOLUTION_0
    WATER --> P1_ASSEMBLE_OUTER_SOLUTION_0
    P1_ASSEMBLE_OUTER_SOLUTION_0 --> OUTER_SOLUTION_TRIS_HEPES


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class TRIS_HEPES_STOCK,ENERGY_SOLUTION,WATER leaf;
    class OUTER_SOLUTION_TRIS_HEPES composed;
    class P1_ASSEMBLE_OUTER_SOLUTION_0 process;

    click P1_ASSEMBLE_OUTER_SOLUTION_0 "/docs/processes/assemble-outer-solution/main"
    click OUTER_SOLUTION_TRIS_HEPES "/docs/modules/outer-solution-tris-hepes/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Solutes

:::{table} The Tris-HEPES formulation.
| Component | Working concentration | Notes |
| --- | --- | --- |
| Tris-HEPES | 46.67% (v/v) in water | from a stock |
| Energy solution | 1× in the finished reaction | a 2× sub-mix of ten components; see the Energy solution tab |
| Osmotic concentration | ~1180 mOsm | a relation, and it sets the gel's |
:::

**Osmolarity is additive and the polymer's own term is negligible**, about 0.7% by weight, so this value carries the gel.

::::

::::{tab-item} Energy solution

The energy solution is a 2× sub-mix of ten components, made up to 4000 µL. It is used at 1×, so the last column is the concentration to reach in the finished reaction.

:::{table} Energy solution. The mix is 4000 µL.
:label: comp-outer-solution-tris-hepes-energy

| Component | Stock | Volume (µL) | In the 2× mix | At 1× |
| --- | --- | --- | --- | --- |
| Spermidine | 1 M | 12 | 3 mM | 1.5 mM |
| Creatine phosphate | 1 M | 200 | 50 mM | 25 mM |
| Magnesium acetate tetrahydrate | 1 M | 144 | 36 mM | 18 mM |
| L-Glutamic acid potassium salt monohydrate | 2 M | 1120 | 560 mM | 280 mM |
| Folinic acid calcium salt hydrate | 332 mM | 9.2 | 0.764 mM | 0.382 mM |
| ATP | 100 mM | 300 | 7.5 mM | 3.75 mM |
| GTP | 100 mM | 200 | 5 mM | 2.5 mM |
| CTP | 100 mM | 100 | 2.5 mM | 1.25 mM |
| UTP | 100 mM | 100 | 2.5 mM | 1.25 mM |
| Amino acid mix | 6 mM | 400 | 0.6 mM | 0.3 mM |
| Ultra-pure distilled water | — | 1414.8 | — | — |
| Total | | 4000 | | |
:::

Vendor data where it is recorded: creatine phosphate Millipore Sigma `10621714001`, ATP Millipore Sigma `A6419`, amino acid mix Biotechrabbit `BR1401801` as the RTS Amino Acid Sampler. Spermidine `S2626`, magnesium acetate tetrahydrate `M5661`, potassium glutamate `G1501`, folinic acid `F7878`, GTP `G8877`, CTP `C1506` and UTP `U6750` are all Millipore Sigma.

The counter-ion on the magnesium salt is a free choice among innocuous ones. Acetate is what the recipe names; glutamate is the salt the benches stock.

The energy solution follows the original PURE formulation of [Shimizu et al., 2001](https://doi.org/10.1038/90802), with adjustments from the OnePot PURE method of [Lavickova and Maerkl, 2019](https://doi.org/10.1021/acssynbio.8b00427). The same ten components are made in bulk by [Make Small Molecule Mix](../../processes/make-small-molecule-mix/main.md).

The recipe is not the energy solution of Sun et al., 2013, which is built on 3-PGA and carries tRNA, CoA, NAD and cAMP, none of which this mix has. That paper is not a source for it.

::::


:::::

# Requirements

Requires an osmotic concentration of about 1180 mOsm, matched across the membranes of the cells embedded
in the gel it forms.

# Implementations

- [pH Demo](../../implementations/devstudio-ph-demo/main.md): the outer solution both arms are built on.

# Processes

Made by [Assemble Outer Solution](../../processes/assemble-outer-solution/main.md), which is one of the two instances of [Assemble Solution](../../processes/assemble-solution/assemble-solution-main.md).

# Constituent Modules

- Tris-HEPES stock — 46.67% (v/v) in water
- Energy solution — a 2× sub-mix of ten components, used at 1×

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit
explicitly before this page is merged to `main`.
:::
