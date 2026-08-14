---
title: "GUV Encapsulation: Lipid Variants"
subtitle: "Process"
status: draft  # draft | unvalidated-published | validated-published — see CLAUDE.md "Page status"
---

# Overview

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

GUV Encapsulation uses the same core method as [Encapsulation: Phase Transfer](../assemble-base-cell/main.md): a lipid-in-mineral-oil mixture is layered over an aqueous inner solution, emulsified, and centrifuged through the oil into an outer solution, where liposomes pellet at the bottom of the tube and are recovered. This page does not restate that protocol. For the lipid-in-oil prep, emulsification, phase-transfer, centrifugation, and recovery steps, follow [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) directly.

This page documents only what is different for the Chicago and London GUV work: the lipid composition of the membrane, and a documented Optiprep/BSA additive tradeoff and QC criteria from that experimental work. "GUV" here names the vesicle-size outcome of these specific formulations; it is not evidence of a separate encapsulation method from [Encapsulation: Phase Transfer](../assemble-base-cell/main.md). This process is used for the [Chicago Chassis](../../modules/chicago-chassis/spec.md) (Base Cytosol in a 9:1 POPC:cholesterol membrane) and the [London Chassis](../../modules/london-chassis/spec.md) (S30 Lysate in a 100% POPC membrane). Each chassis spec gives its own reference composition (inner solution, membrane, outer solution).

This process is unrelated to [SUV Encapsulation](../encapsulate-suv/main.md), which uses an extrusion + size-exclusion-chromatography (SEC) method — a genuinely different technique, not just a different lipid recipe.

:::::::{card}
:header: **Important Information**

Please read this section carefully. It contains important notes, resources, and safety information. Not all information included here is included in the lab-ready protocol.

::::::{note} Three phase-transfer routes were compared; Optiprep trades yield for expression
:class: dropdown
:icon: false

Three phase-transfer routes for encapsulating a cell-free lysate in POPC GUVs have been compared: the Elani-lab protocol with Optiprep in the inner solution, the same Elani-lab protocol without Optiprep, and the Schroeder protocol (JoVE, 2020). The Schroeder protocol gave very low yield and was dropped. Between the two Elani-lab variants:

- **With Optiprep:** gives the cleanest, highest-yield encapsulation. Adding 5 mg/mL BSA and raising Optiprep to 15% raised yield about 1.5x (~42 vs. ~27 GUVs ≥5 µm per field). GUV counts held stable across 37 °C incubation, so membrane stability is not the yield bottleneck. **But Optiprep above ~5% of the inner solution suppresses cell-free expression** — the 10% and 15% Optiprep conditions tested gave abundant, stable GUVs (round and intact through 48 h) but no reporter signal at 1 h or 48 h, with membrane stability and plasmid dose both ruled out as the cause.
- **Without Optiprep:** gives fewer GUVs, but restores expression — the encapsulated cell-free sensor expresses its reporter on induction, with reporter-positive puncta co-localizing with round vesicles across imaged fields.

Choose the route based on what the experiment needs: Optiprep for maximum GUV yield when no functional cell-free reaction is required (e.g., membrane-only imaging), or no Optiprep when the encapsulated reaction must remain active.

::::::

::::::{caution} Not yet controlled
:class: dropdown
:icon: false

The Optiprep-free expression result has no minus-inducer or no-DNA negative controls yet, and no biological replicates. Treat reporter expression from Optiprep-free encapsulation as promising but unattributed until those controls are run.

Encapsulation is also inherently stochastic: not every vesicle captures an active cell-free reaction, so expect a reporter-positive subpopulation rather than uniform signal across all GUVs.

::::::

::::::{attention} Critical Materials
:class: dropdown
:icon: false

- **Optiprep** — optional density medium. Improves GUV yield but suppresses cell-free expression above ~5% of the inner solution; omit when the encapsulated reaction must stay functional.
- **BSA** — optional additive (5 mg/mL) that further raises yield when combined with 15% Optiprep. Only relevant to the Optiprep route.
- Match inner and outer solution osmolarity to keep encapsulated GUVs stable. A denser outer solution against a lighter inner solution causes GUVs to sediment and drift, which complicates imaging. The two chassis recipes documented so far target ~920 mOsm (London) and ~1180 mOsm (Chicago); measure with a vapor-pressure osmometer and adjust the outer solution to match your specific inner solution rather than assuming either value.

::::::

::::::{note} Lipid composition
:class: dropdown
:icon: false

Two lipid-composition variants are documented so far. Both use the same lipid-in-oil prep and phase-transfer steps as [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) — only the lipid mixture itself, and the resulting inner/outer solutions, differ from that page's Base Membrane default (70% POPC / 29.95% cholesterol / 0.05% Liss-Rhod PE).

:::{tab-set}

::::{tab-item} Chicago (9:1 POPC:Chol)

:::{table}
:label: comp-membrane-guv-chicago

| Component  | Target Percentage (%) | Molecular Weight (g/mol) |
| ---------- | ---------------------- | -------------------------- |
| POPC       | 89.9                    | 760.076                     |
| Cholesterol | 10                      | 386.66                      |
| Rhod PE    | 0.1                      | 1301.72                     |

:::

Dried and resuspended in mineral oil to 0.5 mM lipid-in-oil. See [Chicago Membrane: POPC/Chol](../../modules/membrane-popc-chol-chicago/spec.md) for the full membrane spec.

::::

::::{tab-item} London (100% POPC)

:::{table}
:label: comp-membrane-guv-london

| Component | Target Percentage (%) |
| --------- | ---------------------- |
| POPC      | 100                     |

:::

POPC film (2 mg from 80 µL of 25 mg/mL chloroform stock) dried and resuspended in 500 µL mineral oil, to a 4 mg/mL working lipid concentration. Unlike the Chicago recipe, this membrane carries no cholesterol. See [London Chassis](../../modules/london-chassis/spec.md) for the full reference composition, including the matched outer solution (potassium L-glutamate, HEPES, glucose).

::::

:::::

::::::

:::::::

# Materials and Equipment

The lipids, chloroform, mineral oil, glass syringe, glass vials, and 384-well imaging plate are the same items listed in [Encapsulation: Phase Transfer](../assemble-base-cell/main.md)'s Materials and Equipment, substituting the lipid quantities for the Chicago or London composition above. The table below lists only the reagents specific to the Optiprep/BSA yield-vs-expression work on this page.

:::{table}
:label: bom-encapsulate-guv
:align: center

| Name      | Category | Product                                                        | Manufacturer   | Part #      | Price   | Storage | Link                                                                    |
| --------- | -------- | --------------------------------------------------------------- | -------------- | ----------- | ------- | ------- | ------------------------------------------------------------------------ |
| Optiprep  | Reagent  | OptiPrep™ Density Gradient Medium                              | Sigma-Aldrich  | D1556-250ML | $373.00 | 4 °C    | [link](https://www.sigmaaldrich.com/US/en/product/sigma/d1556)          |
| BSA       | Reagent  | Bovine Serum Albumin, Fraction V                                | Sigma-Aldrich  | A9418       | $52.00  | 4 °C    | [link](https://www.sigmaaldrich.com/US/en/product/sigma/a9418)          |

:::

# Protocol

## Complete the Shared Phase-Transfer Protocol

- [ ] Complete the Prepare Lipids in Mineral Oil, Assemble Outer Solutions, and Encapsulate Inner Solution sections of [Encapsulation: Phase Transfer](../assemble-base-cell/main.md) — including its centrifugation and emulsification parameters, which are not superseded by this page — using the substitutions below in place of the Base Membrane / Base Cytosol defaults.

## Substitutions for This Variant

- [ ] Use the Chicago or London lipid composition above (see the Lipid composition dropdown) in place of the Base Membrane default.
- [ ] Assemble the inner solution per the corresponding chassis Module spec ([Chicago Chassis](../../modules/chicago-chassis/spec.md), [London Chassis](../../modules/london-chassis/spec.md)) in place of Base Cytosol.
- [ ] If maximizing GUV yield without requiring a functional encapsulated reaction, supplement the inner solution with Optiprep (see the Critical Materials dropdown above for the yield/expression tradeoff). Otherwise, omit Optiprep.
- [ ] Prepare the outer solution per the chassis Module spec, and confirm its osmolarity matches the inner solution using a vapor-pressure osmometer (e.g., Wescor EliTech Vapro 5600). Adjust as needed — do not assume the ~920 mOsm or ~1180 mOsm values documented for London and Chicago apply to a different inner solution without checking.

# Quality Control

- **Yield and morphology**: Count round, intact GUVs ≥5 µm per imaging field by fluorescence or brightfield microscopy. GUV counts should remain stable across incubation at the encapsulated reaction's working temperature (e.g., 37 °C) — a drop in counts over time indicates membrane instability rather than an expression problem.
- **Functional encapsulation**: If the inner solution carries an active cell-free reaction with a reporter, confirm reporter expression on induction. Expect a reporter-positive subpopulation rather than uniform signal, since not every GUV captures an active reaction.

:::{attention} Optiprep above ~5% of the inner solution suppresses cell-free expression
No documented condition combines high Optiprep-driven yield with confirmed functional cell-free expression. Confirm which of the two your experiment needs before choosing whether to include Optiprep in the inner solution.
:::

# Downloads

::::{grid} 1 1 1 1

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/encapsulate-guv-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/encapsulate-guv-bom.pdf>`
:::

::::
