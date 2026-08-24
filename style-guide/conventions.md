# Conventions

## Terminology

| Use | Not | Note |
| --- | --- | --- |
| Module | constituent | `# Constituent Modules` and mermaid `classDef constituent` are protected strings |
| Node (proper noun) | node | Chicago Node, London Node |
| DevCells | — | the program |
| DevStudio | DevCell Studio | the three-week hackathon |
| liposome | vesicle | never an umbrella term; GUV, SUV and LUV are distinct and must not collapse |
| synthetic cell | liposome | wherever the liposome can reasonably be called a synthetic cell |
| integration path | leg | |
| colorimetric | colormetric | |
| ultrapure water | milliQ water | vendor-neutral |
| `SMix -CP` | `SMixΔCP` | prefer plain characters |

**"Confirmed in synthetic cytosols and in synthetic cells"** is the standard phrasing for that claim. It is a phrasing, not a find-and-replace target — applying it blindly once produced "confirmed confirmed in synthetic cytosols and in synthetic cells".

**Name the exact chemical species.** Write `rNTPs` or `dNTPs`, never the ambiguous `NTP`. Some Modules specify both on the same page, so this is not a substitution you can automate.

**Be precise about what a number means.** "Raises Mg²⁺ from 8 to 18 mM" and "raises *optimal* Mg²⁺ from 8 to 18 mM" are different claims.

**Name the specific thing built,** using real Module names: "aTc Sensing Cell + CPRG-containing SUV + LacZ in 1% alginate". If a Module name does not exist for something you keep describing, it probably should.

One item, one name (STE 1.11). American English. Renaming a shared term needs collaborator consent — a rename that reaches other Nodes is not an editorial decision.

## Headings and captions

No hedge words. "Preparations", not "Documented Preparations".

Figure captions name the figure type: "Schematic representation of X in the Base Cell", not "X in the Base Cell".

Renaming a heading is a link change, because inbound anchors do not follow it. `check-links.py` verifies fragments against MyST's slug rule.

## Figures

Parallel figures go in a tab-set — never a dropdown, never stacked. Tab names describe the data, not the format: `Microscopy Images` not `Montage`; `Fluorescence Intensity` not `Endpoint`.

Secondary or supporting figures go in a `::::{hint}` dropdown whose title states the finding.

## Diagrams

Generated diagrams carry the diagram and nothing else — no explanatory paragraphs.

Fence them as ` ```mermaid `, never ` ```{mermaid} `. Default to grayscale; use a colorblind-friendly palette only when color is requested. A generated diagram must not name specific Nodes.

A Modules flowchart shows only Modules; a Processes flowchart only Processes; a third type shows a full Implementation with both. Every node must be a dependency of something in the diagram.

## Citations

Cite inline with a DOI link where the source is discussed. Never hand-write a `# References` section — MyST generates one from the DOI links on the page, and a manual list double-renders.

DevNotes with a `10.63765/…` DOI must be cited through `doi.org` so they autogenerate.

DevNotes are never a status source. They carry methodology prose only.

A construct-to-file identity claim requires evidence, minimally a matching GenBank `LOCUS` length. Name similarity is not evidence. `check-dna-refs.py` checks this.

## Mechanics

- Tab-set fence depth: `{tab-set}` 5 colons, `{tab-item}` 4, figures and admonitions inside 3.
- Internal links use `.md`, never `.html`.
- A new module spec needs two TOC updates: `myst.yml` and `docs/modules/modules-main.md`.
- No `.gb` sequence files and no vendor PDFs in this repo.
- `generated/` and `tmp/` are never committed.
- Delete any dropdown whose only content is a placeholder.

## Before a PR

```bash
git ls-files docs/ | grep -E '\.(md|csv)$' | xargs vale
codespell docs/
python3 scripts/check-links.py --offline-only docs/
python3 scripts/check-dropdowns.py && python3 scripts/check-toc.py && python3 scripts/check-file-placement.py
grep -rn '@[A-Za-z]' docs/ && echo "LOOSE TAG — do not push"
```
