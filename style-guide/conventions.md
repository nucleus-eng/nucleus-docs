# Conventions

## Terminology

**The terms are not here any more.** They live in the Nucleus glossary, shared by every repo that
installs the `nucleus` plugin: a definition for each term, the spellings it refuses, and which of
those refusals are rules.

> `plugins/nucleus/references/glossary.md` — `nucleus-eng/nucleus-skills`, branch `feat/glossary`,
> `2fb9ba03c27879cbc2eb61dffe454f98c47dc611`.

**Ten of its refusals run here as Vale rules.** `.vale.ini` sets the severity, because severity is
each repo's own call: a refusal that collapses two meanings blocks, a house preference advises.

**The rest cannot be rules and are not weaker for it.** A refused word that collides with a
required heading, a filename or ordinary English is enforced by reading, which is the `style-guide`
skill's job. The glossary marks which are which, and why.

**Renaming a shared term needs collaborator consent** — a rename that reaches other Nodes is not an
editorial decision. That holds for the glossary itself, not just for pages.

## Headings and captions

No hedge words. "Preparations", not "Documented Preparations".

Figure captions name the figure type: "Schematic representation of X in the Base Cell", not "X in the Base Cell".

Renaming *or removing* a heading is a link change, because inbound anchors do not follow it. Deleting a section this guide bans — revision history, future work — is the common case. The `author-myst-content` skill says which anchors are safe to write in the first place.


## Diagrams

Generated diagrams carry the diagram and nothing else — no explanatory paragraphs.


A Modules flowchart shows only Modules; a Processes flowchart only Processes; a third type shows a full Implementation with both. Every node must be a dependency of something in the diagram.

## Citations

Cite inline with a DOI link where the source is discussed. Never hand-write a `# References` section — MyST generates one from the DOI links on the page, and a manual list double-renders.

DevNotes with a `10.63765/…` DOI must be cited through `doi.org` so they autogenerate.

DevNotes are never a status source. They carry methodology prose only.

A construct-to-file identity claim requires evidence, minimally a matching GenBank `LOCUS` length. Name similarity is not evidence. `check-dna-refs.py` checks this.

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
