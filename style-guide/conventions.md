# Conventions

<!-- names only, no claim: this page names other repos inside the list of pointers it
     forbids. It asserts nothing about their contents, so it carries no pin. -->

## Terminology

| Use | Not | Note |
| --- | --- | --- |
| Module | constituent | `# Constituent Modules` and mermaid `classDef constituent` are protected strings |
| Node (proper noun) | node | Chicago Node, London Node |
| DevCells | — | the program |
| DevStudio | DevCell Studio | the three-week hackathon |
| liposome | vesicle | never an umbrella term; GUV, SUV and LUV are distinct and must not collapse |
| synthetic cell | liposome | wherever the liposome can reasonably be called a synthetic cell |
| integration path | — | `leg` is an accepted synonym for a path on a graph, not a refused spelling. `integration path` stays preferred |
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

Renaming *or removing* a heading is a link change, because inbound anchors do not follow it. Deleting a section this guide bans — revision history, future work — is the common case. The `author-myst-content` skill says which anchors are safe to write in the first place.


**An analyte is a condition on a Detector and a component of a Cascade.** A Detector's plus- and minus-analyte columns are test conditions, not two compositions, so the analyte is not an operand of its steps. A Cascade is built from a trigger solution that carries the analyte, so there the analyte is an operand as well as a condition. A Cascade still has plus- and minus-analyte conditions.

## Diagrams

Generated diagrams carry the diagram and nothing else — no explanatory paragraphs.

A generated diagram must not name specific Nodes.

A Modules flowchart shows only Modules; a Processes flowchart only Processes; a third type shows a full Implementation with both. Every node must be a dependency of something in the diagram.

## Citations

Cite inline with a DOI link where the source is discussed. Never hand-write a `# References` section — MyST generates one from the DOI links on the page, and a manual list double-renders.

DevNotes with a `10.63765/…` DOI must be cited through `doi.org` so they autogenerate.

DevNotes are never a status source. They carry methodology prose only.

A construct-to-file identity claim requires evidence, minimally a matching GenBank `LOCUS` length. Name similarity is not evidence. `check-dna-refs.py` checks this.

A page whose subject is one molecule cites its UniProt entry, as `[UniProt P00722](https://www.uniprot.org/uniprotkb/P00722/entry)`, with the entry's own name, organism and length beside it. The entry is authoritative for mass and sequence length, so where the page and the entry disagree the entry wins and the page says it changed.

**An accession is an identity claim and name similarity is not evidence**, the same rule the DNA constructs follow. Three ways it goes wrong, all of them found on the first pass through this corpus:

- **The first hit is the wrong class.** Searching "Tetracycline repressor" returns class D, `P0ACT4`. The TetR this corpus uses is class B from transposon Tn10, `P04483`. Both are *E. coli*, both are 200-odd residues, and only one is right.
- **The entry disagrees with the corpus about what the protein does.** `P54293` is titled *Transcriptional activator protein EsaR* and carries no alternative name, while every page here treats EsaR as a repressor that the analyte de-represses. Cite it and say so; do not quietly adopt either name.
- **An engineered variant is not its parent.** **deGFP is not wild-type GFP** and must not be cited as `P42212`. mNeonGreen is engineered from a *Branchiostoma* protein and is not that protein. A variant page cites the parent only when it says which part is the parent's.

**Before citing an identifier, ask whether it distinguishes the subject from its siblings.** If something else carries it, it names their parent — see [principles.md](principles.md#a-shared-identifier-is-a-shared-parent). CAS numbers, UniProt accessions, filenames and supplier part numbers all fail this way, and they fail at different grains.

**No check covers supplier part numbers.** `check-dna-refs.py` and `check-protein-refs.py` each cover one identifier system. `check-links.py` passes a 403 as tolerated, so a live URL pointing at the wrong product is indistinguishable from a right one. Treat a part number as an unverified claim and say what the page relies on.

**Cite nothing when the subject is a preparation rather than a gene product.** "Tyrosinase from mushroom" is a supplier's preparation and *Agaricus bisporus* has several polyphenol oxidases; there is no single entry to name.

## Mechanics

- A new module spec needs two TOC updates: `myst.yml` and `docs/modules/modules-main.md`.
- No `.gb` sequence files and no vendor PDFs in this repo.
- `generated/` and `tmp/` are never committed.

## What never appears

The test is the question in [principles.md](principles.md#every-page-is-world-readable-because-it-is): does this describe the Module, or our work on it? These are the categories seen so far — a seed list, never a checklist.

- **Internal documents** — questionnaires, status decks, meeting transcripts, `.docx` filenames, slide numbers. Including inside `# Credits`.
- **Project management** — milestones, open action items, "still at the planning stage", "waiting for Twist", "mitigation in progress", "tracked separately", "pending".
- **Who decided, and how** — "*name* ruled on *date* that…", "on *name*'s word", "*name*, *date*: …", "the 2026-08-14 meeting resolved to…", "that requirement is settled". State the result. The commit message that applied it records who decided and when.
- **Our own records** — "Figure not yet migrated", "not yet transcribed", "interim source", "no dedicated devnote", "documented on each Module's own page". If a figure has not been migrated, migrate it.
- **Editor-directed text** — use an `@Editor:` or `@Developer:` tag, never prose.
- **Revision history** — "Earlier revisions of this page…", "Written *date* because…", "Corrected *date*", "until *date*, when…", "previously referred to here as…". These describe the document, and git records them.
- **Meta-commentary** — "flattened one level deep", "not duplicated here", "this page specifies it", "this corpus", "this page cannot tell them apart".
- **Hedged attribution** — never "attribution is pending confirmation".
- **Pointers into our working notes** — `compositional-biology-theory`, "the theory corpus", `open.md#O21`, `rulings.md#D04`, commit hashes. A reader cannot follow them. State the content, or leave it out.
- **Our tooling** — a script, a generator, `spec.yml` or "the composition source" as the subject of a sentence: "`one_member_classes()` reported this class", "`spec.yml` declares no `process_steps`". Tooling keeps the pages right. It is not what a page describes.
- **Argument aimed at a reviewer** — a defense of a choice against an alternative the reader never proposed: "Gel does not refine Solution, and the near miss is worth stating", "this does not reopen the cancellation". State what the Module is; see [principles.md](principles.md#write-for-an-unknown-composer).

`check-reference-voice.py` blocks the commonest markers of these: a contributor named as the source of a decision, a ruling, a pointer into our working notes, a stray review tag. It warns on dates, "this corpus", tooling and commit hashes. It is a net, not the rule: a page can pass it and still read as a decision log.

## Before a PR

```bash
git ls-files docs/ | grep -E '\.(md|csv)$' | xargs vale
codespell docs/
python3 scripts/check-composition-tabs.py
python3 scripts/check-implementations.py
python3 scripts/check-links.py --offline-only docs/
python3 scripts/check-anchors.py
python3 scripts/check-dna-refs.py
python3 scripts/check-dropdowns.py && python3 scripts/check-toc.py && python3 scripts/check-file-placement.py
python3 scripts/check-reference-voice.py
grep -rnE '@[A-Za-z]' docs/ --include='*.md' | grep -vE '@(Editor|Developer):'
```

`check-anchors.py` catches the failure the `author-myst-content` skill describes under Cross-references — an `#anchor` whose slug is not unique, which MyST binds to whichever page won. It reads sources only, so it runs in well under a second and needs no build.

`check-dna-refs.py` reads a local checkout of `nucleus-eng/DNA`, so CI never runs it and only a local run will catch a Designs table whose bp claim disagrees with the target's GenBank `LOCUS`. That link resolves, so no other check sees it.

The last line flags stray tags. `@Editor:` and `@Developer:` are sanctioned and expected on a draft page; resolve them before the page is published.
