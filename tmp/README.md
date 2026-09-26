# `tmp/`

Scratch space. **Everything here is gitignored except this README** — see `.gitignore`.

## Staging location

**Staging documents go in `tmp/staging/`**, named `STAGED-<date>-<topic>.md`.

This declaration is what the `staging` skill looks for: it takes the nearest README that declares a location, and falls back to `tmp/STAGED-<date>-<topic>.md` when none does. Ours is one level deeper, so without this file an agent following the skill writes to the wrong place.

Applied and superseded documents move to `tmp/archive/<date>-<kind>/`, where `<kind>` is `applied`, `superseded`, `parked` or `absorbed`. Nothing else in `tmp/` is a staging document.

## Checking a staging document

The checkers live in `nucleus-skills` `scripts/` and take this repo as their first argument.
`NUCLEUS_SKILLS` names that checkout.

```bash
python3 "$NUCLEUS_SKILLS/scripts/check-sites.py" . 'tmp/staging/STAGED-*.md'
python3 "$NUCLEUS_SKILLS/scripts/check-pin-freshness.py" . 'tmp/staging/STAGED-*.md'
```

The first anchors every edit-site row against the working tree. The second reports a pinned
quotation that is no longer true at the tip. Both exit 2 when they read nothing, and neither is
a CI gate: `tmp/staging/` is gitignored and a fresh clone has nothing for them to read.

## Delivery state

**A file whose content is meant for a person carries its delivery state in its own `#`
heading** — `SENT`, `UNSENT`, `POSTED` or `FILED` — with the date and the recipient, and a link
where there is one.

Taken from `compositional-biology-theory`, where `draft-issue-224-comment.md` reads
*"— POSTED"* and `draft-issue-requirements-schema.md` reads *"— FILED"* with the issue URL on
its first line.

**The point is that the mark is visible without opening the file, and that its absence means
something.** Adopted 2026-09-18 after three files across three repos were found ending in
questions nobody could confirm had been asked. Questions that are finished, correct and
undelivered look exactly like questions that are done.
