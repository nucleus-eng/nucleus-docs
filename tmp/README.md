# `tmp/`

Scratch space. **Everything here is gitignored** — see `.gitignore`.

## Staging location

**Staging documents go in `tmp/staging/`**, named `STAGED-<date>-<topic>.md`.

This declaration is what the `staging` skill looks for: it takes the nearest README that declares a location, and falls back to `tmp/STAGED-<date>-<topic>.md` when none does. Ours is one level deeper, so without this file an agent following the skill writes to the wrong place.

Applied and superseded documents move to `tmp/archive/<date>-<kind>/`, where `<kind>` is `applied`, `superseded`, `parked` or `absorbed`. Nothing else in `tmp/` is a staging document.
