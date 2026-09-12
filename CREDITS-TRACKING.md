---
title: "Credits tracking — working file"
---

:::{danger} 🚧 Delete this file before merging to `main`
This is a working model of who did what, assembled from meeting sources so that
Credits blocks can be filled in later. **It is not documentation and must not
ship.** Remove it, and remove `credits-tracking.md` from `ALLOWED_ROOT_FILES` in
`scripts/check-file-placement.py`, in the same commit that merges this branch.
:::

# What this is

Every Module and Process spec carries a `# Credits` section, and most of them carry this admonition:

> Contributor attribution on this page has not been confirmed with the Node. Assign each credit explicitly before this page is merged to `main`.

This file is the raw material for discharging those. It records **who is reported to have done which piece of work, and where that report came from**, so that a Credits line can later be written with a source behind it rather than from memory.

**It does not assign credit.** Attribution is the Node's to confirm. A row here is a claim about a source, not a decision.

## How to read the confidence column

| Value | Meaning |
| --- | --- |
| **corpus** | Already credited on a page in `docs/`, with a full name and usually an affiliation. Treat as settled unless it conflicts with a newer source |
| **footer** | From a slide footer in the September deck. Names the presenter of that slide's work; terse, and the affiliation may apply to only one of several names |
| **spoken** | From a PI or presenter introducing the work in a transcript. Autotranscribed, so first names are reliable and surnames often are not |
| **conflict** | Two sources disagree. Do not write a Credits line from these until resolved |

---

# People already credited in the corpus

These have full names and, in several cases, ORCIDs. **Use these spellings** — the meeting sources give first names only for most of them.

| Name | Affiliation | Credited on | Confidence |
| --- | --- | --- | --- |
| Samuel J. Chen ([ORCID](https://orcid.org/0000-0001-8501-7175)) | Chicago Node, Liu Lab | `anneal-ph-trigger-duplex` | corpus |
| Sung-Won Hwang | Chicago Node, Liu Lab | `anneal-ph-trigger-duplex`, `ph-cascade` | corpus |
| Allen Liu | Chicago Node, Liu Lab | `anneal-ph-trigger-duplex` | corpus |
| Mary Kelly | Chicago Node, Kamat Lab | `atc-cascade`, `atc-sensing-cell`, `detector-tetr-atc` figures | corpus |
| Maram Naji ([ORCID](https://orcid.org/0000-0003-1409-4194)) | Chicago Node, **Lucks Lab** | six pages, incl. `colorimetric-readout` | corpus — C1 explains the slide-footer mismatch |
| Charlie Newell | London Node | `colorimetric-readout` | corpus |
| Ion Ioannou | London Node | `ahl-sensing-cell` | corpus |
| Jonah McDonald | London Node | `ahl-sensing-cell` | corpus |
| Surendra Yadav | b.next | `base-cell` | corpus |
| Yemo Ku | b.next | `base-cytosol` | corpus |
| Jon Calles | b.next | `base-cytosol` | corpus |
| Yen-Yu Hsu ([ORCID](https://orcid.org/0000-0003-0866-6184)) | b.next | `control-clpxp` | corpus |

---

# New attributions from the 11 September sources

**Sources.** `tmp/DevCell Project Meeting, 11 Sep 2026.pptx` (slide numbers below); the DevCells All-Hands transcript, Notion, 2026-09-11; the Chicago↔b.next standup transcript, Notion, 2026-09-11.

## Chicago Node

| Person | Work | Source | Confidence |
| --- | --- | --- | --- |
| Samuel J. Chen | QR-code patterning in 0.7% agarose; the two-vesicle system loading β-Gal into GUVs with substrate in bulk; the smartphone detection app | Slide 23 footer; presented at length in the all-hands | footer + spoken |
| Ojaswita Pant | Photolithographic patterning of PEG-norbornene; the Chicago Northside logo; the pectin/alginate composite frame | Slide 24 footer, stated twice | footer — C2 resolved |
| Mary Kelly | aTc sensor in Nucleus Cytosol; the TetR root-cause work; the aTc titration; the patterned-gel color result | Slides 25–30 footers; presented in the all-hands | footer + spoken |
| Maddie Briggs | aTc sensor work with Mary Kelly; the encapsulated-GUV imaging that found the 0.35 µM optimum | Slides 25, 28, 29, 30 footers | footer |
| Maram Naji | TetR troubleshooting | Slide 26 footer | footer — see conflict C1 |
| Sung-Won Hwang | H⁺ sensor, in progress | All-hands, introduced by the Chicago PI | spoken |
| Neha Kamat | Chicago Node PI — introduced the node's work | All-hands | spoken |

## London Node

| Person | Work | Source | Confidence |
| --- | --- | --- | --- |
| Charlie Newell | Built the London slides; the oil/leakage result with Jonah McDonald; the color-change assay in cytosol | All-hands, named by the presenting PI | spoken |
| Jonah McDonald | The oil/leakage result, jointly with Charlie Newell — the King's vs UCL oil comparison and the moisture hypothesis | All-hands, both named and both on the call | spoken |
| **Niall** (surname not captured) | The open-source flow meter, referred to throughout as the "Niall bot" — 10-channel photodiode, about \$20 | All-hands; answered questions about it directly | spoken — **surname wanted** |
| **Manuel** (surname not captured) | Cytosol expression work; the minus-T7 and holoenzyme results | All-hands; not on the call, referred to by others | spoken — **surname wanted** |
| Michael Booth | London Node PI — presented the four demonstration levels | All-hands | spoken |
| Yuval Elani | London Node PI | Agenda slide 1 | footer |

## b.next

| Person | Work | Source | Confidence |
| --- | --- | --- | --- |
| Surendra Yadav | Plasmid cloning and function verification for DevStudio; the AHL/DMSO troubleshooting; TetR with His-tag (no SUMO) working consistently | All-hands and standup, throughout | spoken |
| Jon Calles | The integration/wiring diagrams and the documentation audit presented to both nodes | All-hands | spoken |
| Richard Murray | Funding and node-planning updates; chaired | Slides 42–44; all-hands | footer + spoken |
| Anton Molina | DevStudio data and documentation workflow | All-hands | spoken |

---

# Conflicts — both resolved

## C1 — Maram Naji's lab — near-resolved, keep Lucks Lab

`colorimetric-readout` credits her to the **Lucks Lab**. Slide 26's footer reads `Mary Kelly | Maram Naji | Kamat Lab`.

**The corpus settles this in a single sentence.** `docs/processes/colorimetric-readout/main.md:114` names both people with different labs in one line:

> Developed by [Maram Naji](https://orcid.org/0000-0003-1409-4194) (Chicago Node, **Lucks Lab**), [Charlie Newell](https://orcid.org/0000-0001-9208-7542) and Michael Booth (London Node, Booth Lab), Mary Kelly (Chicago Node, **Kamat Lab**)…

So the slide footer's trailing "Kamat Lab" attaches to Mary Kelly, not to both names. That is how these footers read throughout the deck.

**Lucks Lab is credited on six pages** — `colorimetric-readout`, `embed-alginate-hydrogel`, `reporter-lacz`, `theophylline-sensing-cell`, `reporter-xyle`, `gel-alginate` — and on a seventh, `detector-theophylline`, she is credited to the Chicago Node with no lab.

**Resolution: keep Lucks Lab. No question needed for the Node.** Listed here only so the slide footer does not get read as a contradiction later.

## C2 — RESOLVED. Credit Ojaswita Pant; "Archie Sweeney" is a transcription garble

Slide 24 is footered twice, both times: `Ojaswita Pant | Truby Lab | Chicago Node`.

The all-hands transcript introduces the same work with "Are you here, Archie Sweeney?", and a person answers and presents it.

**Jon, 2026-09-11: "Archie Sweeney is a garble of some kind."**

So there is **no second contributor**. The transcript mangled a name, as it does throughout — the same transcript renders homoserine lactone as "homicidal lactone" and PEG-norbornene as "Pegnor boronene".

**Credit Ojaswita Pant (Truby Lab, Chicago Node)**, per the slide footer, which is stated twice and is the better-sourced of the two.

**One residue, and it is small.** The ruling says the name is a garble; it does not say it garbles *Ojaswita Pant* specifically. Nothing here depends on that — the slide is the source for the credit either way — but do not cite the transcript as independent confirmation of the spelling.

# Wanted

- **Surnames for Niall and Manuel** (London). Both did work that will want a Credits line — the flow meter is a demonstration level of its own, and the cytosol expression results underpin Demo 4.
- **Maddie Briggs' affiliation.** Footered alongside Mary Kelly on Kamat Lab slides; not yet credited anywhere in `docs/`.
- **Whether slide footers are authoritative for affiliation at all.** C1 and C2 both turn on this. One answer settles both.

# Where these land

1. **`# Credits` sections** on the affected Module and Process specs, replacing the "not been confirmed with the Node" admonition once a Node confirms.
2. **`docs/about/contributors.md`**, the public contributors page — distinct from root `CONTRIBUTORS.md`, which is a contributing guide and not a credits list.

**Neither is done by this file.** Both are page edits and go through the normal staging route.
