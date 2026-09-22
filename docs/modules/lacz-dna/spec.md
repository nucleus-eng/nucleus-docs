---
title: "LacZ DNA template"
subtitle: "Module Specification"
status: draft
site:
    hide-toc: true
    numbered_references: false
---

# Overview

<!-- gen:position -->
**Position.** Refines [`lacz`](../lacz/spec.md). Refined by nothing on this branch.
<!-- /gen:position -->

A member of [LacZ](../lacz/spec.md): the `T7pro-LacZ-T7term` construct.

**A template, not an enzyme.** It carries no activity itself and requires an expression system to produce any. That requirement is the whole difference between this member and [LacZ Enzyme](../reporter-lacz-enzyme/spec.md), which needs a supplier instead.

:::{attention} 🚧 Draft
This page is a work in progress and not yet ready for use.
:::

# Reference Composition

One construct, obtained rather than composed.

:::{table} The construct.
| Component | Notes |
| --- | --- |
| `T7pro-LacZ-T7term` | **not present in `nucleus-eng/DNA`** as of 2026-09-21 |
:::

# Constituent Modules

- `T7pro-LacZ-T7term` — the construct. No page: it is not in the DNA repository

# Requirements

Requires an expression system. A template in a tube reports nothing.

# Processes

None here. It is obtained rather than made.

# Credits

:::{attention} Credits are draft
Contributor attribution on this page has not been confirmed with the Node. Assign each credit
explicitly before this page is merged to `main`.
:::
