---
title: "Base Membrane: POPC/Chol"
subtitle: "Module Specification"
thumbnail: schematic.png
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`membrane`](../membrane/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

The Base Membrane specifies a phospholipid bilayer composed of POPC, cholesterol, and fluorescent Lissamine Rhodamine PE (Liss-Rhod PE). The Base Membrane is our recommended default membrane for making synthetic cells by using [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).

:::{figure} schematic.png
:width: 50%
:align: center

Schematic of a POPC/Chol liposome.
:::

# Reference Composition

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
flowchart TD
    POPC["POPC"]
    CHOLESTEROL["Cholesterol"]
    LISS_RHOD_PE["Liss-Rhod PE"]

    P1_FORM_LIPID_FILM_0(["Encapsulation: Phase Transfer (mixing)"])
    MEMBRANE_POPC_CHOL["Base Membrane: POPC/Chol"]

    POPC --> P1_FORM_LIPID_FILM_0
    CHOLESTEROL --> P1_FORM_LIPID_FILM_0
    LISS_RHOD_PE --> P1_FORM_LIPID_FILM_0
    P1_FORM_LIPID_FILM_0 --> MEMBRANE_POPC_CHOL


    classDef leaf     fill:#e5e7eb,stroke:#6b7280,color:#111827;
    classDef composed fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef process  fill:#ffffff,stroke:#374151,color:#111827;
    class POPC,CHOLESTEROL,LISS_RHOD_PE leaf;
    class MEMBRANE_POPC_CHOL composed;
    class P1_FORM_LIPID_FILM_0 process;

    click P1_FORM_LIPID_FILM_0 "/docs/processes/assemble-base-cell/main"
    click MEMBRANE_POPC_CHOL "/docs/modules/membrane-popc-chol/spec"
```

::::
<!-- /gen:composition-diagram -->

:::::

:::{table}
:label: comp-membrane-popc-chol

| Component    | Target Percentage (%) | Molecular Weight (g/mol) | Stock concentration (mg/mL) | Volume to add (µL) |
| ------------ | --------------------- | ------------------------ | --------------------------- | ------------------ |
| POPC         | 70                    | 760.076                  | 25                          | 162.17             |
| Cholesterol  | 29.95                 | 386.654                  | 50                          | 17.65              |
| Liss-Rhod PE | 0.05                  | 1301.71                  | 1                           | 4.96               |

:::

# Expected Behavior

The behavior of Base Membrane is characterized using the [deGFP Reporter](../reporter-degfp/spec.md) Module in [Base Cell](../base-cell/spec.md).

# Processes

Protocols for assembling Base Cell and making its components from scratch are described in the Process [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md).

# Credits

Developed by b.next.
