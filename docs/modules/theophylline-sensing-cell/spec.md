---
title: "Theophylline Sensing Cell"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Theophylline Sensing Cell is the [Chicago Chassis](../chicago-chassis/spec.md) loaded with the [Theophylline Sensing Module](../detector-theophylline/spec.md): a 9:1 POPC:cholesterol GUV encapsulating Base Cytosol and DNA encoding the theophylline-responsive riboswitch, here controlling PLA1 expression rather than the LacZ reporter used in the Theophylline Sensing Module's bulk-cytosol validation. Detection of theophylline drives PLA1 production, which is the trigger step for the downstream Chicago Cascade lysis reaction (out of scope for this page — see Implementations).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Deprioritized, not canceled
This Sensing Cell is deprioritized in favor of the pH-Sensing and aTc Sensing Cells; the underlying riboswitch's behavior is described as "very wonky and unpredictable." A bulk-reaction replication test (2026-08-14 status deck, p. 28) also found the riboswitch **leaky**: it drove reporter expression without theophylline present at levels close to the 1 mM to 2 mM theophylline condition. This status carries over from the [Theophylline Sensing Module](../detector-theophylline/spec.md) spec — see that page for the full discussion. Status is proposed, not canceled — do not treat this page as a validated, ready-to-use Module.
:::

This page describes the Chassis + Module integration step itself, which works standalone. It does not cover the separate, currently blocked downstream integration of this Sensing Cell into the multiplexed Chicago Cascade — that merge is documented on the Chicago Cascade page (not yet authored).

## Schematic

```{mermaid}
%%{init: {'theme': 'base', 'themeVariables': {'lineColor': '#555555', 'edgeLabelBackground': '#ffffff'}}}%%
flowchart LR
    Chassis["Chicago Chassis\n(Base Cytosol in 9:1 POPC:Chol GUV)"] -->|"Add riboswitch-to-PLA1 DNA"| Cytosol["Loaded Cytosol"]
    Module["Theophylline Sensing Module\n(riboswitch-to-PLA1 DNA)"] -.-> Cytosol
    Cytosol -->|"Encapsulate as GUV"| SensingCell["Theophylline Sensing Cell"]
    Theo(("Theophylline\n(1 mM)")) -->|"Detected by riboswitch"| SensingCell
    SensingCell -->|"Produces"| PLA1["PLA1"]
    PLA1 -.->|"Out of scope on this page"| Cascade["Chicago Cascade\nlysis reaction"]

    style Chassis fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Module fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Cytosol fill:#6B7280,color:#ffffff,stroke:#4B5563
    style SensingCell fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Theo fill:none,stroke:#4B5563
    style PLA1 fill:#6B7280,color:#ffffff,stroke:#4B5563
    style Cascade fill:none,stroke:#9CA3AF,color:#6B7280,stroke-dasharray: 5 5
```

This diagram shows the composed mechanism only: the Chicago Chassis loaded with the Theophylline Sensing Module's riboswitch-to-PLA1 DNA, encapsulated as a GUV, then producing PLA1 on theophylline detection. It stops at PLA1 output — the downstream Chicago Cascade lysis reaction is a separate, out-of-scope step (see Overview above).

## Reference Composition

:::::{tab-set}

::::{tab-item} Cytosol

The inner solution is [Base Cytosol](../base-cytosol/spec.md) at reaction concentration, per [Chicago Chassis](../chicago-chassis/spec.md), with DNA added encoding the theophylline riboswitch upstream of PLA1.

The table below is a one-level-deep aggregate: it states what each constituent contributes to the combined Sensing Cell recipe, without re-expanding either constituent's own internal composition (see each linked spec for that detail).

:::{table} Sensing Cell composition (Cytosol) — aggregated from constituent Modules
:label: comp-theo-sensing-cell-cytosol

| Constituent | Contributes | Working concentration / fraction in the Sensing Cell recipe |
| --- | --- | --- |
| [Chicago Chassis](../chicago-chassis/spec.md) | Base Cytosol reaction mix (see that page and [Base Cytosol](../base-cytosol/spec.md) for the internal recipe) | 1x reaction concentration — the chassis cytosol is not diluted to add the sensing DNA |
| [Theophylline Sensing Module](../detector-theophylline/spec.md) | DNA encoding the theophylline riboswitch upstream of PLA1 | Not documented for the PLA1-linked construct actually used in this Sensing Cell (see gap flag below). For scale only: the bulk-cytosol validation construct — `pT7-theophylline-LacZ` (`pMN066`), a different downstream gene — runs at 5 nM final DNA in a 1x cytosol reaction, per the `chicago-theophylline-lacz` devnote. That figure is cited for scale only; it is not confirmed to apply to the PLA1-linked construct. |

:::

:::{attention} Construct not yet identified
The PLA1-linked riboswitch construct used in the Chicago integration status material is a separate design from `pT7-theophylline-LacZ` (`pMN066`), the bulk-cytosol validation construct documented on the [Theophylline Sensing Module](../detector-theophylline/spec.md) page. It is not yet named or present in `nucleus-eng/DNA`. Do not link a placeholder or assume the LacZ-reporter construct's sequence applies here — flag for follow-up so the PLA1-linked construct can be identified and submitted to `nucleus-eng/DNA`.
:::

::::

::::{tab-item} Membrane

:::{table}
:label: comp-theov-membrane

| Component   | Target Percentage (%) |
| ----------- | ---------------------- |
| POPC        | ~90 (9:1 ratio)         |
| Cholesterol | ~10 (9:1 ratio)         |

:::

Same 9:1 POPC:cholesterol GUV membrane as [Chicago Chassis](../chicago-chassis/spec.md). See that page for the note on how this differs from the default [Base Membrane](../membrane-popc-chol/spec.md) ratio.

::::

:::::

## Expected Behavior

Per the Chicago integration status material, this Sensing Cell produces PLA1 upon detection of 1 mM theophylline. This result has not yet been independently confirmed by a primary devnote — cite the Chicago integration status material and treat as pending confirmation, consistent with the "PLA1-linked cascade design" discussion on the [Theophylline Sensing Module](../detector-theophylline/spec.md) page.

Separately, the bulk-cytosol devnote behind the Theophylline Sensing Module (`chicago-theophylline-lacz`) demonstrates the riboswitch itself converts CPRG faster in the presence of 1.5 mM theophylline than without it, using the LacZ-reporter construct rather than the PLA1-linked construct used here. That result supports the riboswitch's general compatibility with Nucleus Cytosol; it is not a validation of this Sensing Cell's specific PLA1 output.

As noted above, a later bulk-reaction replication (2026-08-14 status deck, p. 28) found the riboswitch leaky in the LacZ-reporter configuration, expressing reporter without theophylline at levels close to the 1 mM to 2 mM theophylline condition. Whether the same leakiness applies to the PLA1-linked construct used in this Sensing Cell has not been separately tested — flagged as an open question rather than assumed.

## Requirements

Per the [Theophylline Sensing Module](../detector-theophylline/spec.md) page, this Sensing Cell cannot be present in the same cascade as the aTc Sensing Cell (mutual exclusion). Theophylline is reported to interact with and somewhat inhibit the LacZ/CPRG colorimetric reaction used for cascade readout — a hedged, source-quoted finding, not a fully characterized mechanistic claim. See the Theophylline Sensing Module page for the full discussion; this page does not restate it.

# Constituent Modules

- [Chicago Chassis](../chicago-chassis/spec.md)
- [Theophylline Sensing Module](../detector-theophylline/spec.md) (PLA1-linked configuration — see Reference Composition above for how this differs from that page's bulk-cytosol validation construct)

# Implementations

No Implementation page exists yet for this Sensing Cell. The downstream merge into the multiplexed Chicago Cascade is tracked separately (Chicago Cascade, not yet authored). A hydrogel cross-contamination issue between co-located DevCells has been reported as a blocker for that merge; it has not been documented in a primary source, and its mechanism and scope are not yet characterized. This page covers the Chassis + Module integration only.

# Credits

- b.next
- [Maram Naji](https://orcid.org/0000-0003-1409-4194) — bulk-cytosol riboswitch validation (`chicago-theophylline-lacz` devnote)
