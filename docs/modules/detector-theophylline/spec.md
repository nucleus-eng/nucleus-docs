---
title: "Detector: Theophylline"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Theophylline Sensing Module is a translational riboswitch, designed by [Lynch and Gallivan](https://doi.org/10.1093/nar/gkn924), that controls expression of a downstream effector gene in response to theophylline, a xanthine derivative. Two effector configurations exist in current source material and should not be conflated: a bulk-cytosol validation build places the riboswitch directly upstream of a LacZ reporter (see Expected Behavior), while the Chicago Cascade design places it upstream of PLA1, so that theophylline detection triggers a two-vesicle lysis cascade read out by a separate LacZ/CPRG system. This page covers the sensing Module itself; the PLA1-linked cascade use is a separate Implementation (see Implementations).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Deprioritized, not canceled
This module shows unreliable, unpredictable behavior; the pH-Sensing and aTc Sensing Modules are currently prioritized over it. A bulk-reaction replication (status deck, p. 28) found the module **leaky**: it expressed LacZ without theophylline present at levels close to the 1 mM to 2 mM theophylline condition. Status is proposed, not canceled — do not treat this page as a validated, ready-to-use Module.
:::

# Requirements

The Theophylline Sensing Module cannot be present in the same cascade as the [aTc Sensing Module](../detector-tetr_atc/spec.md) (mutual exclusion). Theophylline interacts with and somewhat inhibits the LacZ/CPRG colorimetric reaction that both sensing pathways rely on for readout in the Chicago Cascade, affecting conversion "even at very low amounts" of theophylline. This is a hedged, source-quoted finding, not a fully characterized mechanistic claim, and it has not yet been written up in a formal devnote. The mutual-exclusion requirement itself is confirmed: the two sensors cannot be combined in the current Chicago Cascade. A general Nucleus compatibility matrix covering other module pairs is explicitly out of scope here.

:::::{tab-set}

::::{tab-item} Schematic

:::{attention} Diagram authored for this page — not sourced imagery
No published schematic exists for this mechanism; the diagram below is a simplified summary, not a reproduction of a lab figure. It is a simple author-created Mermaid diagram of the general Lynch and Gallivan riboswitch mechanism. Replace it with a real mechanism figure (from the source publication or a lab-drawn schematic) when one becomes available.
:::

```{mermaid}
flowchart LR
    T["Theophylline"] -->|binds| A["Aptamer domain<br/>(riboswitch 5' UTR)"]
    A --> C["Conformational change<br/>exposes ribosome binding site"]
    C --> R["Translation initiation"]
    R --> E["Downstream effector expressed<br/>(LacZ or PLA1, depending on build)"]
```

The theophylline riboswitch is a translational control element: theophylline binding to the aptamer domain in the 5' UTR triggers a conformational change that exposes the ribosome binding site, turning on translation of the downstream gene. The bulk-cytosol validation build places LacZ downstream of the riboswitch; the Chicago Cascade build places PLA1 downstream instead (see Overview).
::::

::::{tab-item} Designs
**DNA**

:::{attention} Not yet in `nucleus-eng/DNA`
The bulk-cytosol validation construct `pT7-theophylline-LacZ` (internally referenced as `pMN066`) is not present in `nucleus-eng/DNA` as of this writing (checked against the `detectors/` directory). Do not link to a placeholder or guess a filename — this construct needs to be submitted to `nucleus-eng/DNA` before this table can cite a real sequence file. The Chicago Cascade's PLA1-linked riboswitch construct is a separate, not-yet-identified design and is also not represented below.
:::

| **Name** | **Length (bp)** | **File** |
| --- | --- | --- |
| `pT7-theophylline-LacZ` (`pMN066`) | TODO — not yet in `nucleus-eng/DNA` | TODO |
::::

::::{tab-item} Maps
No sequence map is available yet; it depends on the `nucleus-eng/DNA` submission noted above.
::::

:::::

# Expected Behavior

## Bulk-cytosol validation (LacZ reporter)

In [a bulk-cytosol devnote](https://github.com/bnext-bio/nucleus-developer-notes) (`chicago-theophylline-lacz`), the riboswitch-LacZ sensor converts CPRG from yellow to a red product faster in the presence of 1.5 mM theophylline than without it, measured by absorbance at 570 nm in standard Nucleus Cytosol conditions with 5 nM sensor DNA. This is a single preliminary experiment (one condition each, no replicates reported) demonstrating that the sensor is compatible with Nucleus Cytosol — it is not a fully characterized dose-response.

### Reaction composition

Each condition was assembled as a 10 µL reaction with 0.6 mg/mL CPRG and incubated at 37 °C in a platereader. Volumes in µL.

:::{attention} Discrepancy between sources — devnote table does not sum to 10 µL
The devnote's own reaction-composition table (`chicago-theophylline-lacz/main.md`) lists the Theophylline row as 0.95 µL in **both** the − theophylline and + 1.5 mM theophylline columns, and the Water row as 0.54 µL / 0 µL. That version does not sum to 10 µL in either column (10.59 µL and 9.05 µL) and would put theophylline in the negative control, contradicting the devnote's own stated conditions. The Chicago Module Integration Status writeup (`chicago.md`, "Proposed Specification: Key Experiment" table, repeated four times) carries an internally consistent version of the same table — Theophylline at 0 µL / 0.95 µL and Water at 0.95 µL / 0 µL — which sums to 10.05 µL in both columns and matches the devnote's stated negative control (no theophylline). The table below uses the consistent `chicago.md` values. Flag this for the dev team so the devnote's table can be corrected at the source.
:::

| Component | Stock Concentration | Final Concentration | − theophylline (µL) | + 1.5 mM theophylline (µL) |
| --- | --- | --- | --- | --- |
| SMix | 3.33x | 1x | 3 | 3 |
| PMix | 15 mg/mL | 1.80 mg/mL | 1.2 | 1.2 |
| Ribosomes | 10 µM | 1.8 µM | 1.8 | 1.8 |
| tRNA | 35 mg/mL | 3.5 mg/mL | 1 | 1 |
| `pT7-theophylline-LacZ` (`pMN066`) DNA template | 49.55 nM | 5 nM | 1 | 1 |
| CPRG | 10 mg/mL | 0.6 mg/mL | 0.6 | 0.6 |
| Theophylline | 10 mM | 1.5 mM | 0 | 0.95 |
| RNase Inhibitor | 40,000 U/mL | 2,000 U/mL | 0.5 | 0.5 |
| Water | — | — | 0.95 | 0 |
| **Total** | | | **10.05** | **10.05** |

## PLA1-linked cascade design (Chicago Cascade)

Separately, the Chicago Cascade integration status writeup describes a 9:1 POPC:cholesterol GUV encapsulating the b.next cell-free cytosol and DNA encoding a theophylline-responsive riboswitch controlling PLA1 expression, producing PLA1 upon detection of 1 mM theophylline. PLA1 expression then initiates a vesicle lysis cascade read out by separate CPRG-loaded SUVs embedded with LacZ. This configuration has not been independently validated by a primary devnote at the time of writing — cite the Chicago integration status material and flag pending confirmation.

## Later replication finding (leakiness)

A later bulk-reaction replication (status deck, p. 28) found the theophylline-LacZ module leaky: it expressed LacZ without theophylline at levels comparable to the 1 mM to 2 mM condition. This directly reinforces the unreliable-behavior status above and should be read alongside, not instead of, the earlier bulk-cytosol result — the two do not agree, and neither should be treated as the final word.

# Implementations

No Implementation page exists yet for either the Theophylline Sensing Cell (GUV encapsulation) or the Chicago Cascade.

# Credits

- [Maram Naji](https://orcid.org/0000-0003-1409-4194) — bulk-cytosol validation (`chicago-theophylline-lacz` devnote)
