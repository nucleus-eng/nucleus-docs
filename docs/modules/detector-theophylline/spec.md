---
title: "Detector: Theophylline"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

The Theophylline Sensing Module is a translational riboswitch, designed by [Lynch and Gallivan](https://doi.org/10.1093/nar/gkn924), that controls expression of a downstream effector gene in response to theophylline, a xanthine derivative. Two effector configurations exist in current source material and should not be conflated: a bulk-cytosol validation build places the riboswitch directly upstream of a LacZ reporter (see Expected Behavior), while the Chicago Cascade design places it upstream of PLA1, so that theophylline detection triggers a two-liposome lysis cascade read out by a separate LacZ/CPRG system. This page covers the sensing Module itself; the PLA1-linked cascade use is a separate Implementation (see Implementations).

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

:::{attention} Removed from the Chicago demo; retained as a DevStudio replication target
Three distinct status facts, which earlier revisions of this page collapsed into "deprioritized":

1. **Out of the Chicago demo.** Chicago is "focusing on ATC and H+ sensors" (14 Aug 2026 deck, slide 2), and its Integration Assessment Framework now lists "Two sensors (aTC/pH)" (slide 34). The team also flagged "theophylline sensor removed from Chicago demo" as a diagram inaccuracy to correct (2026-08-14 meeting notes).
2. **Still in scope for DevStudio.** The module appears under "Replicating Modules in Bulk Reactions" (slide 28) — queued for bulk replication during the program, not abandoned.
3. **The riboswitch is leaky.** In bulk (slide 28, `10 nM T7-theo-lacZ`), the no-theophylline condition still drives LacZ to Abs₅₇₀ ≈ 3.0 AU by 3.5 h. Adding theophylline roughly doubles the *rate* (≈3.9 AU by 1.7 h), and 1 mM and 2 mM are indistinguishable from each other.

Do not treat this page as a validated, ready-to-use Module.
:::

# Requirements

The Theophylline Sensing Module must not be co-encapsulated with the [aTc Sensing Module](../detector-tetr_atc/spec.md). Both pathways read out through the same LacZ/CPRG chemistry, and the two were agreed to be mutually exclusive in the current Chicago Cascade design.

**The requirement is settled; the mechanism behind it is not.** The decision is recorded directly: the 2026-08-14 meeting resolved to "add a hard requirement on the theophylline and ATC sensor module pages: these two sensors cannot be co-encapsulated." Treat the requirement as binding. Do not treat the explanation below as characterized. A general Nucleus compatibility matrix covering other module pairs is out of scope for this page — the meeting scoped that as a platform-level decision.

:::{attention} Unresolved: the stated mechanism runs against the only primary figure available
The mutual exclusion has been explained as theophylline *inhibiting* the LacZ/CPRG conversion, reportedly "even at very low amounts". That explanation is currently unsupported and partly contradicted:

- **The one bulk figure points the other way.** In the 14 Aug 2026 deck (slide 28), adding 1 mM or 2 mM theophylline made the LacZ/CPRG reaction roughly **twice as fast**, not slower. Riboswitch activation producing more LacZ could in principle mask direct enzyme inhibition, so both effects can coexist — but no figure showing inhibition has been located.
- **The supporting titration data has not been seen.** The 2026-08-14 meeting notes state that "titration data exists showing even very low theophylline concentrations inhibit CPRG-lacZ conversion," and that it should go into a devnote. That data is not in the status documents or the slide deck.
- **Every verbal source is hedged** ("somewhat inhibit", "kind of inhibiting"), and one literature spot-check found only weak, millimolar-range inhibition, which is inconsistent with the "very low amounts" framing.

Flagged for Chicago rather than resolved here. Until the titration data is in hand, cite the requirement and the decision behind it — not the inhibition mechanism.
:::

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

In [a bulk-cytosol devnote](https://github.com/nucleus-eng/2026-CERN-OHL-P/tree/main/devnotes/chicago-theophylline-lacz) (`chicago-theophylline-lacz`), the riboswitch-LacZ sensor converts CPRG from yellow to a red product faster in the presence of 1.5 mM theophylline than without it, measured by absorbance at 570 nm in standard Nucleus Cytosol conditions with 5 nM sensor DNA. This is a single preliminary experiment (one condition each, no replicates reported) demonstrating that the sensor is compatible with Nucleus Cytosol — it is not a fully characterized dose-response.

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

Separately, the Chicago Cascade integration status writeup describes a 9:1 POPC:cholesterol synthetic cell encapsulating the b.next cell-free cytosol and DNA encoding a theophylline-responsive riboswitch controlling PLA1 expression, producing PLA1 upon detection of 1 mM theophylline. PLA1 expression then initiates a liposome lysis cascade read out by separate CPRG-loaded SUVs embedded with LacZ. This configuration has not been independently validated by a primary devnote at the time of writing — cite the Chicago integration status material and flag pending confirmation.

## Later replication finding (leakiness)

A later bulk-reaction replication (status deck, p. 28) found the theophylline-LacZ module leaky: it expressed LacZ without theophylline at levels comparable to the 1 mM to 2 mM condition. This directly reinforces the unreliable-behavior status above and should be read alongside, not instead of, the earlier bulk-cytosol result — the two do not agree, and neither should be treated as the final word.

# Implementations

No Implementation page exists yet for either the Theophylline Sensing Cell (synthetic cell encapsulation) or the Chicago Cascade.

# Credits

- [Maram Naji](https://orcid.org/0000-0003-1409-4194) — bulk-cytosol validation (`chicago-theophylline-lacz` devnote)
