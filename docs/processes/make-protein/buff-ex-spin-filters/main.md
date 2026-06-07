---
title: Exchange Buffers and Concentrate by Spin Filtration
---

# Overview

You have a sample of a biomolecule (e.g., T7RNAP, tRNA, ribosomes, plasmid, etc.) that is either (1) in the wrong buffer (e.g., has 500 mM Imidazole) or (2) is too dilute.

You can use centrifugal spin filters to concentrate your sample and change its buffer. These filters allow buffer and small molecules to flow through them, retaining large molecules bigger than the filter's specified molecular weight.


# Materials and Equipment

We use two different volume spin filters, depending on how much sample volume we need to process: 15 mL or 0.5 mL.


:::{table} Bill of Materials
:label: bom-buff-ex-spin-filters

| Name | Category | Product | Manufacturer | Part # | Price | Storage | Link |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 15 mL spin filters (3 kDa cutoff) | Consumables | Amicon® Ultra Centrifugal Filter, 3 kDa MWCO | Millipore Sigma | UFC9003 | $125 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/mm/ufc9003) |
| 0.5 mL spin filters (3 kDa cutoff) | Consumables | Amicon® Ultra Centrifugal Filter, 3 kDa MWCO | Millipore Sigma | UFC5003 | $63 | 4°C to 30°C | [link](https://www.sigmaaldrich.com/US/en/product/mm/ufc5003) |
:::

# Protocol

- [ ] Dilute your sample ~10x with your new buffer (e.g., add 54 mL Protein Buffer to 6 mL eluted protein).
- [ ] Load your sample onto a centrifugal filter column.

:::{hint} Note: use filter cutoffs 3x smaller than your sample.
:class: dropdown

Make sure your filter cutoff is at least 3x smaller than your protein size. Otherwise, your may lose your sample in the flowthrough. Using a smaller cutoff filter is fine, but will increase the time you need to spin your sample. If unsure, we recommend using 3 kDa filters for all samples.

:::

- [ ] Centrifuge samples at either 4000 rcf (4 mL or 15 mL filters) or 14 000 rcf (0.5 mL filters) at 4°C until you've reached your target volume. Check on your sample volume in the first 10 min, then again as needed.

:::{hint} Note: if you have too much sample, load in tranches.
:class: dropdown

If you have more sample than you can fit onto your centrifugal filter column, you can load your sample in tranches. Fill your column, spin down your sample, and repeat. See instructions below for details on each spin step.

:::

- [ ] Continue to dilute and spin your sample, noting your sample volume and dilution volume at each step, until you've reached your target dilution factor (we recommend ≥ 300x).

:::{hint} Note: how to calculate dilution factor.
:class: dropdown

Each time you dilute your sample, note the volume of your concentrated sample ($V_{conc}$) and the volume of your sample after diluting ($V_{dilute}$). Calculate the dilution factor for that step ($f_n$) by dividing $V_{dilute}$ by $V_{conc}$.

$$
f_n = \frac{V_{dilute}(n)}{V_{conc}(n)}
$$

To calculate the total dilution factor after multiple dilution steps ($f_{total}$), multiply the dilution factor for each step.

$$
f_{total} = \prod_n f_n = f_1 \times f_2 \times \dots \times f_n
$$

:::
- [ ] Add an equal volume of Protein Buffer (60% glycerol) to your sample to bring the final glycerol concentration to 30%. Freeze samples at -80°C for storage.
- [ ] Store columns for later use.
  - [ ] Wash columns by loading with ddH2O and spinning.
  - [ ] Load columns with EtOH 20% (v/v) and store at room temp.

:::{hint} Note: If you see precipitate, dilute your sample immediately.
:class: dropdown

If your protein precipitates out in any of the concentration steps, dilute the protein further before concentrating. The proteins are precipitating/aggregating out because of high salt concentrations; therefore, diluting the proteins will reduce the chances of the protein to aggregate/precipitate.

:::

# Downloads

::::{grid} 1 1 1 2

:::{card}
:header: **Lab-ready Protocol**

{button}`download <generated/buff-ex-spin-filters-protocol.pdf>`
:::

:::{card}
:header: **Bill of Materials**

{button}`download <generated/buff-ex-spin-filters-bom.pdf>`
:::

::::

# References

- [Cell-free translation reconstituted with purified components](https://doi.org/10.1038/90802)
- [A Simple, Robust, and Low-Cost Method To Produce the PURE Cell-Free System](https://doi.org/10.1021/acssynbio.8b00427)
- [OnePot PURE Cell-Free System](https://dx.doi.org/10.3791/62625)

# Acknowledgements

Yan Zhang, Zoila Jurado, and Miki Yun (Richard Murray Lab, Caltech)
