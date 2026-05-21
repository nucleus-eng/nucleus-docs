# Contributing to Nucleus Docs

Thank you for contributing to the Nucleus Distribution documentation! This guide covers the conventions and workflows you should follow when adding or editing process pages.

## Authoring a new process page

Start from the template at `templates/process-template/process-make_template.md`. Copy it into the appropriate subdirectory under `docs/processes/` and fill in the content.

The template's `# Overview` card includes all possible dropdown sections as a starting scaffold:

| Dropdown | When to keep it |
| --- | --- |
| **Notes** | Any general notes that don't fit elsewhere |
| **Prerequisite Documentation** | Links to protocols that must be completed before this one |
| **Hazardous Materials** | Any reagents with significant safety considerations |
| **Critical Materials** | Materials where substitution or quality issues would affect the outcome |
| **Genetically Encoded Components** | Plasmids, strains, or other genetic constructs required |
| **Composition** | Buffer recipes or mixture compositions specific to this protocol |
| **References** | Primary literature or external resources |

**Delete any dropdown that you don't have content for.** An empty dropdown (one whose only content is `- None`) adds visual clutter and signals to readers that something is missing. The rule is simple: if a section doesn't apply to your protocol, remove it entirely rather than leaving a `- None` placeholder.

## Reviewing a process page

When reviewing a PR that adds or modifies a process page:

1. Check the Overview card for any dropdowns that still contain `- None`.
2. Flag each one to the author and ask whether it should be deleted or filled in.
3. Do not approve the PR while empty dropdowns remain — they should be resolved (deleted or filled) before merge.

> **Note for Claude Code users:** If you ask Claude to review a process page, it will flag empty dropdowns and ask you how to handle each one before making any changes.

## MyST formatting conventions

See `CLAUDE.md` for full details. Key points:

- All table rows must be at **0 indentation** (no leading spaces), even when a table follows a list item.
- Inline hints use `:::{hint} Note: <title>` with `:class: dropdown`.
- Protocol steps use `- [ ]` checkboxes.
- Add every new page to the `toc:` section in `myst.yml`.
