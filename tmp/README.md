# `tmp/`

Scratch space. **Everything here is gitignored** — see `.gitignore`.

## Staging location

**Staging documents go in `~/.claude/staging/nucleus-docs/`**, named `STAGED-<date>-<topic>.md`. This folder is outside every checkout. Use the full expanded path (for example `/Users/<you>/.claude/staging/nucleus-docs/`) with the Write and Edit tools.

Applied and superseded documents move to `~/.claude/staging/nucleus-docs/archive/<date>-<kind>/`, where `<kind>` is `applied`, `superseded`, `parked` or `absorbed`.

### Why the folder is outside the checkout

- Claude sessions often run in git worktrees under `.claude/worktrees/`. The Claude desktop app blocks the Write and Edit tools from writing into the base checkout or a sibling worktree from a worktree session. The app does not let anyone change this.
- A relative `tmp/staging/` resolves to a private folder inside the worktree the session is in. Other sessions cannot see it. The app deletes it when it recycles the worktree, and the staging documents go with it.
- The app allows writes to paths outside the repo. One folder at one absolute path is the same folder from every checkout and every worktree, and it survives a recycle.

This declaration is what the `staging` skill looks for: it takes the nearest README that declares a location. It also holds the archive of applied and superseded documents.

Nothing else in `tmp/` is a staging document. `tmp/` itself stays gitignored scratch space.
