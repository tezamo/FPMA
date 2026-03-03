# Analysis Scripts

Interactive Jupyter notebooks for exploring and visualizing the FPMA dataset. Both notebooks load data directly from the repository and require no local data setup.

---

## Table of Contents

- [Notebooks](#notebooks)
- [Features](#features)
- [Launch on Binder](#launch-on-binder)
- [Local Setup](#local-setup)
- [How to Use](#how-to-use)

---

## Notebooks

| Notebook | Dataset Used | Description |
|----------|-------------|-------------|
| `RawDataAnalysis.ipynb` | `all_commodity.csv` | Explore raw prices in USD across all domestic and international commodities |
| `StandardizedDataAnalysis.ipynb` | `all_commodity_standardized.csv` | Explore unit-normalized prices (`price_per_unit`) with ISO country codes and gap-fill flags |

The key difference between the two notebooks is the price column used: the raw notebook plots `price_usd`, while the standardized notebook plots `price_per_unit` with `unit_std` as the unit label, enabling direct cross-country comparisons even when original units differ.

---

## Features

Both notebooks share the same interactive dashboard structure, built with `plotly` and `ipywidgets`:

### Dual Panel Mode
Two independent panels (Panel A and Panel B) allow side-by-side comparison of any two commodity/country/market combinations. Each panel has its own fully cascading filter set.

### Multi-Selection / Combined Plot Mode
A separate combined plot tool lets you add multiple series and overlay them on a single chart. Selections can be removed individually or cleared all at once.

### Cascading Filters
All dropdowns update dynamically based on upstream selections in this order:

\```
Source → Commodity → Price Type → Country → Market
\```

Selecting "All" at the Country or Market level aggregates across all available options.

### Descriptive Statistics
Each plot is accompanied by a full statistical breakdown displayed in tabbed panels per selection:

| Statistic | Description |
|-----------|-------------|
| Count | Total number of observations |
| Num Countries | Number of unique countries in the selection |
| Num Series | Number of unique country/market/price-type/commodity combinations |
| Overall start / end | Date range of the selection |
| Min / Max / Mean / Median / Std | Price distribution statistics |
| Range | Max minus Min |
| % Change | Percentage change from first to last observation |
| Data length per country | Observation count per country |
| Start / end dates per country | Date range per country |
| Null counts | Missing values per column |
| Frequency gaps (days) | Distribution of gaps between consecutive observations |

---

## Launch on Binder

No installation required. Click a badge to open the notebook directly in your browser:

### Raw Data Analysis
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tezamo/FPMA/main?urlpath=%2Fdoc%2Ftree%2Fnotebooks%2FRawDataAnalysis.ipynb)

### Standardized Data Analysis
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tezamo/FPMA/main?labpath=notebooks/StandardizedDataAnalysis.ipynb)

> Binder may take a minute to build the environment on first launch.

---

## Local Setup

**Using Conda (recommended):**

\```bash
conda env create -f environment.yml
conda activate fpma
jupyter lab scripts/analysis_scripts/RawDataAnalysis.ipynb
\```

**Using pip:**

\```bash
pip install -r requirements.txt
jupyter lab scripts/analysis_scripts/RawDataAnalysis.ipynb
\```

**Required packages:** `pandas`, `plotly`, `ipywidgets`, `jupyterlab`, `nodejs`

> `nodejs` is required for ipywidgets to render correctly in JupyterLab. If widgets appear blank, run `jupyter labextension install @jupyter-widgets/jupyterlab-manager`.

---

## How to Use

**Dual Panel Mode:**
1. Open either notebook and run all cells.
2. Under **Panel A**, select a Source, Commodity, Price Type, Country, and Market.
3. The chart and statistics table update automatically.
4. Use **Panel B** independently for a side-by-side comparison.

**Multi-Selection / Combined Plot Mode:**
1. Scroll to the combined plot section at the bottom of the notebook.
2. Use the dropdowns to configure a selection.
3. Click **➕ Add Selection** to add it to the plot.
4. Repeat to overlay additional series on the same chart.
5. Use **❌ Remove Selected** or **🗑 Clear All** to manage the list.
6. Statistics for each selection appear in separate tabs below the chart.