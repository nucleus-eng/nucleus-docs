# Cytosol Kinetics Analysis Tutorial

## Overview

This tutorial guides you through analyzing time-series fluorescence data from Cytosol cell-free expression experiments. We'll cover data loading, normalization, visualization, kinetic parameter fitting, and summary statistics.

<!-- --- -->

## 1. Setup

First, import the necessary libraries and set up the plotting environment.

The custom `platereader` module that contains specialized functions for loading plate reader data, performing kinetic analysis, and visualization. The `plot_setup()` function configures matplotlib for time-series plots.


```python
%load_ext autoreload
%autoreload 2
    
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Import the cdk platereader module
from cdk.analysis.cytosol import platereader as pr

# Set up plotting
pr.plot_setup()
```

<!-- --- -->

## 2. Load Data

Load your plate reader data and merge it with the platemap that describes experimental conditions.

- `data_file` is the location of your platereader data (ideally in biotek-cdk format)
- `platemap_file`: location of your platemap CSV with Well and experimental conditions
- `load_platereader_data()` reads your plate reader output file and parses it into a standardized format with the platemap integrated
- The resulting DataFrame contains columns: `Well`, `Row`, `Column`, `Time`, `Seconds`, `Temperature (C)`, `Read`, `Data`, plus any columns from your platemap
- `Data` column contains fluorescence measurements (RFU - Relative Fluorescence Units)
- `Time` representing elapsed time


```python
# Specify file paths
data_file = "sample-data/20251111-122213-cytation5-pure-timecourse-gfp-MFG-98-tRNA-QC-biotek-cdk.txt"
platemap_file = "sample-data/platemap.csv"


# Load data
data, platemap = pr.load_platereader_data(
    data_file=data_file,
    platemap_file=platemap_file,
    platereader="biotek-cdk"  # Options: "cytation", "envision", "biotek-cdk"
)

# Checkout first few rows
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Time</th>
      <th>Well</th>
      <th>Data</th>
      <th>Row</th>
      <th>Column</th>
      <th>Read</th>
      <th>Plate</th>
      <th>Clock Time</th>
      <th>Date</th>
      <th>Experiment Name</th>
      <th>...</th>
      <th>DNA ID</th>
      <th>[DNA] (ng/uL)</th>
      <th>PMix Vol (uL)</th>
      <th>Ribosome Vol (uL)</th>
      <th>SMS Vol (uL)</th>
      <th>tRNA Vol (uL)</th>
      <th>DNA Vol (uL)</th>
      <th>RNase Inhib Vol (uL)</th>
      <th>Water vol (uL)</th>
      <th>Rxn Volume (uL)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0 days 00:00:33</td>
      <td>B2</td>
      <td>245</td>
      <td>B</td>
      <td>2</td>
      <td>GFP-Gext</td>
      <td>Plate 1</td>
      <td>2025-11-11 12:24:37</td>
      <td>11/11/2025</td>
      <td>MFG-98-tRNA-QC</td>
      <td>...</td>
      <td>AR-805</td>
      <td>120.00</td>
      <td>3.00</td>
      <td>NaN</td>
      <td>3.00</td>
      <td>1.00</td>
      <td>0.50</td>
      <td>0.50</td>
      <td>2.00</td>
      <td>10.00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>0 days 00:05:33</td>
      <td>B2</td>
      <td>254</td>
      <td>B</td>
      <td>2</td>
      <td>GFP-Gext</td>
      <td>Plate 1</td>
      <td>2025-11-11 12:29:37</td>
      <td>11/11/2025</td>
      <td>MFG-98-tRNA-QC</td>
      <td>...</td>
      <td>AR-805</td>
      <td>120.00</td>
      <td>3.00</td>
      <td>NaN</td>
      <td>3.00</td>
      <td>1.00</td>
      <td>0.50</td>
      <td>0.50</td>
      <td>2.00</td>
      <td>10.00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0 days 00:10:33</td>
      <td>B2</td>
      <td>249</td>
      <td>B</td>
      <td>2</td>
      <td>GFP-Gext</td>
      <td>Plate 1</td>
      <td>2025-11-11 12:34:37</td>
      <td>11/11/2025</td>
      <td>MFG-98-tRNA-QC</td>
      <td>...</td>
      <td>AR-805</td>
      <td>120.00</td>
      <td>3.00</td>
      <td>NaN</td>
      <td>3.00</td>
      <td>1.00</td>
      <td>0.50</td>
      <td>0.50</td>
      <td>2.00</td>
      <td>10.00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0 days 00:15:33</td>
      <td>B2</td>
      <td>230</td>
      <td>B</td>
      <td>2</td>
      <td>GFP-Gext</td>
      <td>Plate 1</td>
      <td>2025-11-11 12:39:37</td>
      <td>11/11/2025</td>
      <td>MFG-98-tRNA-QC</td>
      <td>...</td>
      <td>AR-805</td>
      <td>120.00</td>
      <td>3.00</td>
      <td>NaN</td>
      <td>3.00</td>
      <td>1.00</td>
      <td>0.50</td>
      <td>0.50</td>
      <td>2.00</td>
      <td>10.00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>0 days 00:20:33</td>
      <td>B2</td>
      <td>265</td>
      <td>B</td>
      <td>2</td>
      <td>GFP-Gext</td>
      <td>Plate 1</td>
      <td>2025-11-11 12:44:37</td>
      <td>11/11/2025</td>
      <td>MFG-98-tRNA-QC</td>
      <td>...</td>
      <td>AR-805</td>
      <td>120.00</td>
      <td>3.00</td>
      <td>NaN</td>
      <td>3.00</td>
      <td>1.00</td>
      <td>0.50</td>
      <td>0.50</td>
      <td>2.00</td>
      <td>10.00</td>
    </tr>
  </tbody>
</table>
<p>5 rows × 29 columns</p>
</div>



<!-- --- -->

## 4. Plot Raw Curves

Visualize the time-series fluorescence data to inspect curve shapes and identify any issues.

- `plot_curves_by_name()` creates line plots with time on x-axis and fluorescence (Data) on y-axis
- Each line represents one well, colored by the `Name` column (experimental condition)
- If you have multiple gain data, they'll be plotted in separate subplots (but you should choose one to move forward with)
- This visualization helps you spot outliers, failed reactions, or unexpected kinetics before fitting


```python
g = pr.plot_curves(data=data)
```


    
![png](platereader_tutorial_files/platereader_tutorial_6_0.png)
    


<!-- --- -->

## 3. Normalize Data

Normalize your data to an internal fluorescence sample so that you have relative fluorescence to compare to other experiments. 


```python
data = pr.normalize_data_to_controls(data, ctrl_name = '10 uM HPTS')
```

    Data Normalized to 10 uM HPTS in col data_normalized. The active column for subsequent operations is: data_normalized


Now replot your curves to see them normalized


```python
g = pr.plot_curves(data=data)
```


    
![png](platereader_tutorial_files/platereader_tutorial_10_0.png)
    


<!-- --- -->

## 5. Kinetic Analysis

Fit sigmoid curves to the data to extract kinetic parameters: maximum velocity (Vmax), lag time, steady-state level, and drift.

- `kinetic_analysis()` fits a **sigmoid curve** (with optional drift term) to each replicate well
- The model: $y(t) = \frac{L}{1 + e^{-k(t - t_0)}} + b(t - \tau)$
  - $L$: Steady-state level (asymptote)
  - $k$: Growth rate (steepness)
  - $t_0$: Inflection point (time of max velocity)
  - $b$: Drift rate (fluorescence change after steady-state)
  - $\tau$: Drift onset time
- **Metrics extracted:**
  - **Vmax** (`Velocity Max`): Maximum rate of fluorescence increase (slope at inflection point)
  - **Lag time**: Time to reach the exponential phase
  - **Steady-state**: Final fluorescence level and time to reach 95% of asymptote
  - **Drift**: Rate of signal decay or increase after steady-state
  - **R²**: Goodness of fit


```python
# Perform kinetic analysis using sigmoid_drift model
kinetics = pr.kinetic_analysis(
    data=data,
    group_by=['Name'],  # Group by experimental condition
)

kinetics.head()
```

    PROVIDING AVERAGED KINETICS





<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead tr th {
        text-align: left;
    }

    .dataframe thead tr:last-of-type th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr>
      <th></th>
      <th colspan="3" halign="left">Velocity</th>
      <th colspan="2" halign="left">Lag</th>
      <th colspan="2" halign="left">Steady State</th>
      <th colspan="3" halign="left">Fit</th>
    </tr>
    <tr>
      <th></th>
      <th>Time</th>
      <th>data_normalized</th>
      <th>Max</th>
      <th>Time</th>
      <th>data_normalized</th>
      <th>Time</th>
      <th>data_normalized</th>
      <th>params</th>
      <th>R^2</th>
      <th>drift</th>
    </tr>
    <tr>
      <th>Name</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>NEB Positive Control</th>
      <td>0 days 01:34:45.616715696</td>
      <td>2.25</td>
      <td>2.69</td>
      <td>0 days 00:44:28.688704778</td>
      <td>0.30</td>
      <td>0 days 02:48:47.196931504</td>
      <td>4.28</td>
      <td>[4.501773951041968, 2.3866385500131293, 1.5793...</td>
      <td>1.00</td>
      <td>0.08</td>
    </tr>
    <tr>
      <th>tRNA AR-730 (Rxn Control)</th>
      <td>0 days 01:29:01.540193308</td>
      <td>2.19</td>
      <td>2.34</td>
      <td>0 days 00:32:45.112764155</td>
      <td>0.19</td>
      <td>0 days 02:51:52.382459217</td>
      <td>4.17</td>
      <td>[4.384380953592719, 2.1324521783287356, 1.4837...</td>
      <td>1.00</td>
      <td>0.07</td>
    </tr>
    <tr>
      <th>tRNA AR-836</th>
      <td>0 days 01:31:43.799320428</td>
      <td>2.52</td>
      <td>2.56</td>
      <td>0 days 00:32:30.333969522</td>
      <td>0.21</td>
      <td>0 days 02:58:55.280264960</td>
      <td>4.79</td>
      <td>[5.0426505851597225, 2.0266336639016616, 1.528...</td>
      <td>1.00</td>
      <td>0.07</td>
    </tr>
    <tr>
      <th>tRNA AR-837</th>
      <td>0 days 01:32:27.273708334</td>
      <td>2.58</td>
      <td>2.66</td>
      <td>0 days 00:34:09.146983246</td>
      <td>0.24</td>
      <td>0 days 02:58:17.284049550</td>
      <td>4.90</td>
      <td>[5.161645765443068, 2.0583942112412883, 1.5409...</td>
      <td>1.00</td>
      <td>0.07</td>
    </tr>
    <tr>
      <th>tRNA AR-838</th>
      <td>0 days 01:31:47.921783514</td>
      <td>2.31</td>
      <td>2.41</td>
      <td>0 days 00:34:09.156125597</td>
      <td>0.22</td>
      <td>0 days 02:56:39.983994240</td>
      <td>4.39</td>
      <td>[4.622649794838434, 2.081776126751595, 1.52997...</td>
      <td>1.00</td>
      <td>0.06</td>
    </tr>
  </tbody>
</table>
</div>



### Visualize Fits on Individual Wells

**What's happening:**
- `plot_kinetics_by_well()` overlays fitted curves and kinetic parameters on raw data
- Visual inspection ensures fits are reasonable (high R², smooth curves)
- Annotations show where Vmax, lag time, and steady-state occur


```python
# Plot kinetic fits 
g, kinetics = pr.plot_kinetics(data, kinetics=kinetics, group_by=["Name"])
```


    
![png](platereader_tutorial_files/platereader_tutorial_14_0.png)
    


<!-- --- -->

## 6. Summary Plots

Compare kinetic parameters across experimental conditions.
- The `plot_kinetics_summary()` function creates a comprehensive multi-panel figure with raw curves, steady-state, Vmax, and drift
- Bar plots compare kinetic metrics across conditions
- **Steady-state:** Final protein expression level (proxy for yield)
- **Vmax:** Maximum rate of protein synthesis
- **Drift:** Signal stability (photobleaching, aggregation, continued synthesis...etc)
- Error bars show std across technical replicates


```python
pr.plot_summary(data)
```


    
![png](platereader_tutorial_files/platereader_tutorial_16_0.png)
    


<!-- --- -->

## Key Metrics Explained

### 1. **Steady-State Level** (`Steady State, Data`)
- The final fluorescence value reached by the reaction
- Represents the total amount of protein produced
- Higher values indicate greater expression yield

### 2. **Maximum Velocity** (`Velocity, Max`)
- The steepest slope of the fluorescence curve (at the inflection point)
- Units: RFU per second
- Reflects the peak rate of protein synthesis
- Sensitive to enzyme activity, substrate availability, and reaction conditions

### 3. **Lag Time** (`Lag, Time`)
- Time before exponential fluorescence increase begins
- May reflect time for ribosome assembly or initial translation steps
- Shorter lag times suggest faster reaction initiation

### 4. **Drift** (`Fit, drift`)
- Rate of fluorescence change after reaching steady-state
- Positive drift: continued synthesis or aggregation
- Negative drift: photobleaching, protein degradation, or quenching
- Units: RFU per second

### 5. **R² Value** (`Fit, R^2`)
- Goodness of fit (0 to 1, higher is better)
- R² > 0.98 indicates excellent fit
- Poor fits may indicate noisy data, overflow errors, or non-sigmoid kinetics

<!-- --- -->

## Tips and Troubleshooting

- **Overflow errors:** Wells with `OVRFLW` or `NaN` values are automatically excluded from fitting
- **Poor fits (low R²):** Inspect raw curves for anomalies (bubbles, evaporation, pipetting errors)
- **Drift:** Sometimes seen in kinetics curves; use `sigmoid_drift` model
- **Multiple replicates:** Always include technical replicates and report error bars
- **Comparing conditions:** Normalize or blank data consistently across all samples

<!-- --- -->

## Next Steps

- Export kinetics results: `pr.export_kinetics(kinetics, 'results.csv')`
- Statistical analysis: Use `scipy.stats` or `statsmodels` for ANOVA/t-tests
- Parameter optimization: Vary Mg²⁺, K⁺, or other conditions to maximize Vmax or steady-state
- Mechanistic modeling: Fit ODE models to extract biological rate constants


