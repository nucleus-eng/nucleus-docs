---
title: "Chicago Cascade"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Chicago Cascade is the top-level, multiplexed Chicago demo node: two integration paths running side by side in one system, each detecting a different analyte, both reporting through a shared colorimetric readout. The two integration paths are the [aTc Cascade](../atc-cascade/spec.md) and the [pH Cascade](../ph-cascade/spec.md).

The goal is multiplexed detection — aTc and pH sensed in the same reaction, with a visible color change that reflects the combination of the two inputs.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Rewritten 2026-08-19 — the integration paths have changed
Earlier revisions of this page described this cascade as a merge of the **theophylline** and aTc integration paths, blocked because theophylline interferes with the LacZ/CPRG readout.

That is superseded. Chicago is now focused on the aTc and pH sensors (14 Aug 2026 deck, slides 2 and 34, which lists "Two sensors (aTC/pH)"), and the theophylline sensor has been removed from the demo — its riboswitch drives the reporter with no analyte present, so it does not discriminate. See [Theophylline Sensing Module](../detector-theophylline/spec.md).

The theophylline/aTc co-encapsulation constraint remains true and is still documented on the affected Modules. It is simply no longer this cascade's blocker, because theophylline is no longer one of its integration paths.
:::

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    ATCIN(("aTc")) --> ATCPATH["aTc Cascade"]
    PHIN(("H⁺")) --> PHPATH["pH Cascade"]
    ATCPATH -.->|"not yet attempted"| LOGIC{"How are two<br/>signals combined?<br/>undecided"}
    PHPATH -.->|"not yet attempted"| LOGIC
    LOGIC -.-> READOUT["Shared LacZ/CPRG readout<br/>visible color change"]

    classDef path fill:#6b7280,stroke:#374151,color:#ffffff;
    classDef open fill:#e5e7eb,stroke:#6b7280,color:#111827;
    class ATCPATH,PHPATH,READOUT path;
    class LOGIC open;
    style ATCIN fill:none,stroke:#6b7280
    style PHIN fill:none,stroke:#6b7280
    style LOGIC stroke-dasharray: 5 5
    style READOUT stroke-dasharray: 5 5

    click ATCPATH "/docs/modules/atc-cascade/spec"
    click PHPATH "/docs/modules/ph-cascade/spec"
    click READOUT "/docs/modules/reporter-lacz/spec"
```

Schematic representation of the intended Chicago Cascade design. No published schematic exists for this cascade; the diagram above is a simplified summary of the intended design, not a reproduction of a lab figure.

# Reference Composition

No combined reference composition exists, and none is given here — not even a hypothetical one. The combination has never been assembled, so there are no working concentrations to report, and inventing them would present this as more real than it is.

Each integration path's own composition is documented on its own page.

:::::{tab-set}

<!-- gen:composition-diagram -->
::::{tab-item} Module Dependencies

```mermaid
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart TD
    ATC_CASCADE["aTc Cascade"]
    ATC_SENSING_CELL["aTc Sensing Cell"]
    BASE_CYTOSOL["Base Cytosol"]
    CHICAGO_CASCADE["Chicago Cascade"]
    CHICAGO_CHASSIS["Chicago Chassis"]
    DETECTOR_PH["Detector: pH-Sensing"]
    DETECTOR_TETR_ATC["Detector: tetR-aTc"]
    EFFECTOR_PLA1["Effector: PLA1"]
    MEMBRANE_POPC_CHOL_CHICAGO["Chicago Membrane: POPC/Chol"]
    PH_CASCADE["pH Cascade"]
    PH_SENSING_CELL["pH Sensing Cell"]
    REPORTER_LACZ["Reporter: LacZ"]

    ATC_SENSING_CELL --> ATC_CASCADE
    EFFECTOR_PLA1 --> ATC_CASCADE
    REPORTER_LACZ --> ATC_CASCADE
    CHICAGO_CHASSIS --> ATC_SENSING_CELL
    DETECTOR_TETR_ATC --> ATC_SENSING_CELL
    ATC_CASCADE --> CHICAGO_CASCADE
    PH_CASCADE --> CHICAGO_CASCADE
    BASE_CYTOSOL --> CHICAGO_CHASSIS
    MEMBRANE_POPC_CHOL_CHICAGO --> CHICAGO_CHASSIS
    PH_SENSING_CELL --> PH_CASCADE
    EFFECTOR_PLA1 --> PH_CASCADE
    REPORTER_LACZ --> PH_CASCADE
    CHICAGO_CHASSIS --> PH_SENSING_CELL
    DETECTOR_PH --> PH_SENSING_CELL

    classDef constituent fill:#6B7280,color:#ffffff,stroke:#4B5563;
    classDef this fill:#374151,color:#ffffff,stroke:#111827;
    class ATC_CASCADE,ATC_SENSING_CELL,BASE_CYTOSOL,CHICAGO_CHASSIS,DETECTOR_PH,DETECTOR_TETR_ATC,EFFECTOR_PLA1,MEMBRANE_POPC_CHOL_CHICAGO,PH_CASCADE,PH_SENSING_CELL,REPORTER_LACZ constituent;
    class CHICAGO_CASCADE this;

    click ATC_CASCADE "/docs/modules/atc-cascade/spec"
    click ATC_SENSING_CELL "/docs/modules/atc-sensing-cell/spec"
    click BASE_CYTOSOL "/docs/modules/base-cytosol/spec"
    click CHICAGO_CASCADE "/docs/modules/chicago-cascade/spec"
    click CHICAGO_CHASSIS "/docs/modules/chicago-chassis/spec"
    click DETECTOR_PH "/docs/modules/detector-ph/spec"
    click DETECTOR_TETR_ATC "/docs/modules/detector-tetr_atc/spec"
    click EFFECTOR_PLA1 "/docs/modules/effector-pla1/spec"
    click MEMBRANE_POPC_CHOL_CHICAGO "/docs/modules/membrane-popc-chol-chicago/spec"
    click PH_CASCADE "/docs/modules/ph-cascade/spec"
    click PH_SENSING_CELL "/docs/modules/ph-sensing-cell/spec"
    click REPORTER_LACZ "/docs/modules/reporter-lacz/spec"
```

::::
<!-- /gen:composition-diagram -->

::::{tab-item} Cytosol

See [aTc Cascade](../atc-cascade/spec.md#reference-composition) and [pH Cascade](../ph-cascade/spec.md). Note that the pH Cascade's own combined-recipe concentrations are themselves flagged as undocumented, so a merged recipe would rest on an incomplete Module.

::::

::::{tab-item} Membrane

Both integration paths are built on the [Chicago Chassis](../chicago-chassis/spec.md), so both use the same 9:1 POPC:cholesterol membrane. This part of the merge is straightforward — the membrane carries over unchanged, and it is not implicated in either open question below.

::::

:::::

# Expected Behavior

**Status: not yet attempted.** This combination has not been built. That is different from the previous framing — the merge is **not blocked**, it is **unattempted**. No experiment has run the two integration paths together.

There is, however, a known design question standing in front of it, described below.

## Cells

:::{warning} Not yet validated
This Module has not been validated in synthetic cells.
:::

# Requirements

Requires both integration paths in one system — [aTc Cascade](../atc-cascade/spec.md) and [pH Cascade](../ph-cascade/spec.md) — on a shared [Chicago Chassis](../chicago-chassis/spec.md) membrane, reporting through one shared [LacZ Reporter](../reporter-lacz/spec.md).

Requires each integration path's own requirements to hold unchanged. Neither path has a bulk-cytosol route, so this cascade does not either.

**Something has to decide what the readout does when both paths fire.** Both the aTc and pH integration paths end at the same LacZ/CPRG chemistry. Two inputs arriving at one output is not, by itself, a design — it needs a stated rule for how the two signals combine. Should the color change when *either* analyte is present, only when *both* are, or only when exactly one is? Each of those is a different device, and each needs a different mechanism.

That rule has not been chosen. Until it is, "multiplexed detection" describes an intent rather than a specification.

:::{attention} This is the cascade's central open question
Two things follow from it, and both are worth stating plainly.

**First, a shared readout with no combining rule is not neutral.** If both paths simply drive the same enzyme reaction, the result is whatever the chemistry does when both are active — which is closer to an uncontrolled "either" than to a designed behavior. Getting a specified behavior means adding a mechanism, not just co-locating the two paths.

**Second, the three candidate rules are not equally easy to build.** "Either analyte" is close to what co-locating the paths already gives, so the work is making it controlled and reproducible rather than incidental. "Both analytes" needs a coincidence mechanism — some step that only proceeds when two inputs are present at once. "Exactly one" is harder still, because it needs the system to suppress output when a signal *is* present, and inhibition is a mechanism this cascade does not currently have anywhere.

So the choice of rule is not a labeling decision to make at write-up time. It determines what has to be built.
:::

**A second, separate question.** The pH path's readout adds a neutralization buffer step before the color develops (14 Aug 2026 deck, slide 9), while the aTc path reads out directly. Whether one shared readout can serve both paths when one of them requires a pH adjustment is unresolved, and it is a distinct issue from the combining rule above. Flagged for the Chicago team.

# Implementations

This cascade is the sensing core of the [Chicago DevCell](../../implementations/chicago-devcell/main.md), which places it in a hydrogel and adds spatial patterning. That page carries the demo-level status.

# Process

No combined assembly process exists. Both integration paths are formed by the same method — see [Encapsulation: Phase Transfer](../../processes/assemble-base-cell/main.md) — and both are embedded and read out through the processes listed on their own pages. What is missing is not a technique for making either path, but the step that brings them together and the mechanism that combines their outputs.

# Constituent Modules

- [aTc Cascade](../atc-cascade/spec.md) — the aTc integration path, confirmed in synthetic cytosols and in synthetic cells; hydrogel embedding still in progress
- [pH Cascade](../ph-cascade/spec.md) — the pH integration path; its individual results are confirmed but the three-part chain has not been run end to end

Both integration paths terminate at the [LacZ Reporter Module](../reporter-lacz/spec.md), which is shared rather than duplicated. That sharing is the subject of the Requirements section above.

# Credits

Developed by the Chicago Node (Kamat Lab and Liu Lab).

This cascade has no result of its own; the multiplexed combination has not been built. Attributions for the individual integration paths are on their own pages.

Contributor names come from the 14 Aug 2026 status deck and from the module sections of the Chicago status document, and have not been confirmed by the team.
