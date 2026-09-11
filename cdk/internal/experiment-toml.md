---
title: "The experiment.toml File"
---

:::{warning}
:class: simple
:icon: false

This documents internal tooling. See [Internal Reference](./internal-main.md).
:::

# Overview

A discovery-plate experiment is described by a single `experiment.toml` in the experiment
directory. Sibling CSVs are referenced from it by relative path. This page is the complete
schema.

The schema is enforced, not advisory: **any unknown section or key raises `ValueError`**
naming what is allowed. That makes typos loud rather than silently ignored, but it also
means a key that looks reasonable will be rejected if it is not on the list below.

```toml
[meta]
name = "Discovery Plate R1"
created = 2026-03-14
notes = "Third replicate; PMix lot MFG-98."

[reaction]
final_rxn_vol_ul = 5.0          # ← required; everything else has a default
buffer_reagent = "water"

[pipetting]
min_pipetting_vol_ul = 0.5
pipetting_scalar = 1.1          # ← 10% overage on every mix
conc_decimals = 3
vol_decimals = 3

[base_master_mix]
use = true
add_buffer = true
exclude_from_base = ["tcep"]    # ← reagents kept out of the shared base MM

[files]
reagents = "reagents.csv"
fixed = "fixed_rxn_concs.csv"
samples_final_concs = "samples_titration.csv"

[wells]
add_ids = true
layout_mode = "centered_random"
order = "column"

[doe.lhs]
bounds = "bounds.csv"
n_samples = 20
seed = 42

[doe.control]
replicates = 3
```

## Sections

Every section is optional except `[reaction]`, and every key within a section is optional
except `final_rxn_vol_ul`.

### `[meta]`

Human notes. the calculator ignores them.

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `name` | string | — | Experiment name |
| `created` | date | — | Creation date |
| `notes` | string | — | Free text |

### `[reaction]`

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `final_rxn_vol_ul` | float | **required** | Final per-well reaction volume in µL |
| `buffer_reagent` | string | `"water"` | Reagent used to bring wells to final volume |

:::{attention} `final_rxn_vol_ul` is the one hard requirement
:icon: false
:class: simple

Omitting it raises `AssertionError`, not `ValueError` — the config parses fine, then
fails the required-field check. The message is
`[reaction].final_rxn_vol_ul must be provided in experiment.toml.`
:::

### `[pipetting]`

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `min_pipetting_vol_ul` | float | `0.5` | Smallest volume the handler will dispense |
| `pipetting_scalar` | float | `1.1` | Overage factor on mix volumes |
| `conc_decimals` | int | `3` | Rounding for concentrations in output |
| `vol_decimals` | int | `3` | Rounding for volumes in output |

`min_pipetting_vol_ul` is one of the two usual causes of an infeasible solve — raising it
narrows the window the master-mix solver has to work in.

### `[base_master_mix]`

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `use` | bool | `true` | Build a shared base master mix at all |
| `add_buffer` | bool | `true` | Include the buffer reagent in the base MM |
| `exclude_from_base` | list of string | `[]` | Reagents to keep out of the base MM |

### `[files]`

Paths are relative to the experiment directory.

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `reagents` | path | `"reagents.csv"` | Reagent stock concentrations |
| `fixed` | path | none | Reagents held at a fixed final concentration |
| `samples_final_concs` | path | `"samples_final_concs.csv"` | Per-condition concentrations — the DOE output, and the calculator's input |
| `fixed_overwrite_existing` | bool | `false` | Let fixed reagents overwrite columns that already exist |

### `[wells]`

| Key | Type | Default | Description |
| --- | --- | --- | --- |
| `add_ids` | bool | `true` | Assign 384-well IDs to conditions |
| `layout_mode` | string | `"centered_random"` | Placement strategy |
| `order` | string | `"column"` | Fill order |
| `skip` | bool | `true` | Skip every other well |
| `randomize` | bool | `true` | Randomize placement within the layout |

## `[doe]` — generating conditions

The `[doe]` section configures which condition generators run. Each generator is a
self-contained sub-table; there is no `params = "<sibling>.toml"` indirection. Configure
as many as you need and their outputs are concatenated.

Allowed sub-tables: `lhs`, `ratio_sweep`, `standards`, `control`, `external`, plus an
`output` key.

Every generated row carries a `Type` column naming where it came from — `lhs`,
`ratio_sweep`, `standards`, `control`, or `external`. The calculator routes on it:
`standards` rows take a simple dilution path, everything else goes through the master mix.

### `[doe.lhs]` — Latin hypercube sampling

| Key | Type | Description |
| --- | --- | --- |
| `bounds` | path | CSV of `Component`, `Lower Bound`, `Upper Bound` |
| `n_samples` | int | Number of design points |
| `seed` | int | Random seed |
| `log_space` | bool | Sample in log space |
| `replicates` | int | Replicates per condition |
| `fixed_reagents` | path | Overrides `[files].fixed` for this generator |
| `output_name` | string | Output filename |

### `[doe.ratio_sweep]`

| Key | Type | Description |
| --- | --- | --- |
| `col_a`, `col_b` | string | The two components whose ratio is swept |
| `lower_bound`, `upper_bound` | float | Total-concentration range |
| `ratios` | list of float | Ratios of `col_a` to `col_b` |
| `n_total_concs` | int | Number of total-concentration steps |
| `log_total` | bool | Space totals logarithmically |
| `replicates` | int | Replicates per condition |
| `fixed_reagents` | path | Overrides `[files].fixed` |
| `output_name` | string | Output filename |

### `[doe.standards]`

| Key | Type | Description |
| --- | --- | --- |
| `compounds` | array of tables | One entry per standard curve |
| `replicates` | int | Replicates per point |
| `output_name` | string | Output filename |

Each `[[doe.standards.compounds]]` entry accepts:

| Key | Type | Description |
| --- | --- | --- |
| `compound` | string | Reagent name |
| `unit` | string | Concentration unit |
| `min_conc`, `max_conc` | float | Range of the curve |
| `n_points` | int | Number of points |
| `log_space` | bool | Space points logarithmically |

### `[doe.control]`

| Key | Type | Description |
| --- | --- | --- |
| `replicates` | int | Number of control wells |
| `output_name` | string | Output filename |

:::{note} Control coverage is enforced
:icon: false
:class: dropdown

When `[doe.control]` is configured, every reagent column appearing in non-control rows
must also appear in the control row. The check runs on canonicalized `(reagent, unit)`
keys, so `[PMix] (mg/mL)` and `pmix mg/ml` are recognized as the same column.

To opt a swept reagent into the control baseline, add it to the fixed-reagents CSV with
value `0`.
:::

### `[doe.external]`

Bring in a design generated elsewhere.

| Key | Type | Description |
| --- | --- | --- |
| `source` | path | The externally-supplied conditions CSV |
| `fixed_reagents` | path | Overrides `[files].fixed` |
| `replicates` | int | Replicates per condition |

`source` is an input path, distinct from `[files].samples_final_concs`, which is where
the concatenated result is written. Keeping them separate is what makes the orchestrator
idempotent — it never reads its own output as input.

## The second validation layer

Schema validation above is structural and raises. A separate advisory pass in
`cdk.calculators.validation` checks the *contents*: that referenced files exist, that
reagent and sample CSVs carry their required columns, that units are consistent, that
stock concentrations are present, and that pipetting parameters are sane.

That pass **never raises**. It returns a list of issues, each with a severity
(`ERROR` or `WARNING`) and a stable code, so a caller can decide what to do. This is what
drives live feedback in the Marimo builder.
