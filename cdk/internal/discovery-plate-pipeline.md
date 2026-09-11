---
title: "Discovery Plate Pipeline"
---

:::{warning}
:class: simple
:icon: false

This page is under development, and documents internal tooling. See [Internal Reference](./internal-main.md).
:::

# Overview

How a discovery-plate experiment goes from an `experiment.toml` config to a per-well pipetting plan, covering the DOE generators, the base master-mix solver, and the output files the liquid handler consumes.

The configuration format is documented in full at [The `experiment.toml` file](./experiment-toml.md).
