# FPMA — Food Price Monitoring and Analysis

A structured dataset of global food commodity prices, covering both domestic retail markets and international benchmark prices, with raw and standardized versions ready for analysis.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [Data Description](#data-description)
- [Scripts](#scripts)
- [Column Reference](#column-reference)
- [Quick Start](#quick-start)
- [Analysis](#analysis)
- [Environment Setup](#environment-setup)
- [License](#license)

---

## Overview

FPMA collects and organizes monthly food price data from two sources:

- **Domestic** — retail prices collected from local markets across many countries, covering staple foods such as grains, meats, dairy, vegetables, fruits, and oils.
- **International** — benchmark export/import prices for globally traded commodities such as wheat, maize, rice, soybeans, palm oil, fertilizers, and crude oil.

All prices are available in both their original local currency and converted to USD. A standardized version of the dataset normalizes units (e.g. converting prices to a per-kg or per-liter basis) and fills temporal gaps, making cross-country and cross-commodity comparisons straightforward.

---

## Repository Structure
```
FPMA/
│
├── all_commodity/                                          # Raw data
│   ├── all_commodity.csv                                   # All commodities combined (domestic + international)
│   ├── domestic_commodity.csv                              # All domestic commodities combined
│   ├── international_commodity.csv                         # All international commodities combined
│   ├── domestic_commodity_onebyone/                        # One CSV per domestic commodity (~240 files)
│   └── international_commodity_onebyone/                   # One CSV per international commodity (~70 files)
│
├── all_commodity_standardized/                             # Standardized data
│   ├── all_commodity_standardized.csv                      # All commodities combined (standardized)
│   ├── domestic_commodity_standardized.csv                 # All domestic commodities combined (standardized)
│   ├── international_commodity_standardized.csv            # All international commodities combined (standardized)
│   ├── domestic_commodity_standardized_onebyone/           # One CSV per domestic commodity (standardized)
│   └── international_commodity_standardized_onebyone/      # One CSV per international commodity (standardized)
│
├── scripts/
│   ├── all_commodity.ipynb                                 # Combines domestic + international into all_commodity.csv
│   ├── all_commodity_standardized.ipynb                    # Combines standardized domestic + international
│   ├── domestic_commodity.ipynb                            # Builds domestic_commodity.csv
│   ├── domestic_commodity_onebyone.ipynb                   # Splits domestic data into per-commodity files
│   ├── domestic_commodity_standardized.ipynb               # Builds domestic_commodity_standardized.csv
│   ├── domestic_commodity_standardized_onebyone.ipynb      # Splits standardized domestic into per-commodity files
│   ├── international_commodity.ipynb                       # Builds international_commodity.csv
│   ├── international_commodity_onebyone.ipynb              # Splits international data into per-commodity files
│   ├── international_commodity_standardized.ipynb          # Builds international_commodity_standardized.csv
│   ├── international_commodity_standardized_onebyone.ipynb # Splits standardized international into per-commodity files
│   └── analysis_scripts/                                   # Interactive analysis notebooks
│       ├── README.md
│       ├── RawDataAnalysis.ipynb
│       └── StandardizedDataAnalysis.ipynb
│
├── requirements.txt
├── environment.yml
└── README.md
```

---

## Data Description

### Raw Data

| File | Description |
|------|-------------|
| `all_commodity.csv` | Combined domestic and international prices |
| `domestic_commodity.csv` | Retail prices from local markets worldwide |
| `international_commodity.csv` | Global benchmark export/import prices |
| `domestic_commodity_onebyone/` | One file per domestic commodity (~240 files) |
| `international_commodity_onebyone/` | One file per international commodity (~70 files) |

- **Date range:** Domestic data starts from January 2000; international data from January 1996.
- **Frequency:** Monthly observations.
- **Coverage:** 200+ domestic commodity types and 70+ international benchmark series.

### Standardized Data

The standardized dataset extends the raw data with three additional features:

1. **Unit normalization** — prices are converted to a common unit per commodity (e.g. USD per kg, USD per liter), stored in `price_per_unit` and `unit_std`.
2. **ISO country codes** — each record includes an `iso3_country_code` column for easy merging with other datasets.
3. **Gap filling** — missing monthly observations are filled and flagged in the `fill_method` column (`original` for unmodified records).

---

## Scripts

The `scripts/` folder contains the data processing notebooks that generate all CSV files in the repository. They are organized into two groups — **raw** and **standardized** — and within each group into **combined** and **one-by-one** outputs.

### Raw Data Scripts

| Notebook | Output | Description |
|----------|--------|-------------|
| `domestic_commodity.ipynb` | `all_commodity/domestic_commodity.csv` | Collects and merges all domestic commodity price series into a single file |
| `domestic_commodity_onebyone.ipynb` | `all_commodity/domestic_commodity_onebyone/*.csv` | Splits the domestic data into individual per-commodity CSV files |
| `international_commodity.ipynb` | `all_commodity/international_commodity.csv` | Collects and merges all international benchmark price series into a single file |
| `international_commodity_onebyone.ipynb` | `all_commodity/international_commodity_onebyone/*.csv` | Splits the international data into individual per-commodity CSV files |
| `all_commodity.ipynb` | `all_commodity/all_commodity.csv` | Combines the domestic and international files into one unified dataset |

### Standardized Data Scripts

| Notebook | Output | Description |
|----------|--------|-------------|
| `domestic_commodity_standardized.ipynb` | `all_commodity_standardized/domestic_commodity_standardized.csv` | Applies unit normalization, ISO country code mapping, and gap filling to the domestic data |
| `domestic_commodity_standardized_onebyone.ipynb` | `all_commodity_standardized/domestic_commodity_standardized_onebyone/*.csv` | Splits the standardized domestic data into individual per-commodity CSV files |
| `international_commodity_standardized.ipynb` | `all_commodity_standardized/international_commodity_standardized.csv` | Applies unit normalization and gap filling to the international data |
| `international_commodity_standardized_onebyone.ipynb` | `all_commodity_standardized/international_commodity_standardized_onebyone/*.csv` | Splits the standardized international data into individual per-commodity CSV files |
| `all_commodity_standardized.ipynb` | `all_commodity_standardized/all_commodity_standardized.csv` | Combines the standardized domestic and international files into one unified dataset |

### Execution Order

If you need to regenerate the data from scratch, run the notebooks in this order:
```
1. domestic_commodity.ipynb
2. international_commodity.ipynb
3. all_commodity.ipynb
4. domestic_commodity_standardized.ipynb
5. international_commodity_standardized.ipynb
6. all_commodity_standardized.ipynb
7. domestic_commodity_onebyone.ipynb
8. international_commodity_onebyone.ipynb
9. domestic_commodity_standardized_onebyone.ipynb
10. international_commodity_standardized_onebyone.ipynb
```

---

## Column Reference

### Raw Data Columns

| Column | Description |
|--------|-------------|
| `date` | Observation date (MM/DD/YYYY) |
| `price_usd` | Price in US dollars |
| `price_local` | Price in local currency *(domestic only)* |
| `currency` | Local currency code *(domestic only)* |
| `commodity_name` | Name of the commodity |
| `country` | Country name |
| `market` | Market or city name |
| `price_type` | Type of price (e.g. `RETAIL`, `EXPORT`) |
| `unit` | Original unit of measurement |
| `price_source` | Source type (`Domestic` or `International`) |

> Note: `international_commodity.csv` does not include `price_local` or `currency` columns, as prices are already denominated in USD.

### Additional Standardized Columns

| Column | Description |
|--------|-------------|
| `price_per_unit` | Price normalized to a standard unit (USD) |
| `unit_std` | Standardized unit (e.g. `kg`, `liter`) |
| `iso3_country_code` | ISO 3166-1 alpha-3 country code |
| `fill_method` | How the record was produced (`original` or fill method used) |

---

## Quick Start
```python
import pandas as pd

# Load all standardized data
df = pd.read_csv(
    "https://raw.githubusercontent.com/tezamo/FPMA/main/all_commodity_standardized/all_commodity_standardized.csv",
    parse_dates=["date"],
    dayfirst=True
)

# Filter: domestic rice prices in Kenya
df_rice = df[
    (df["commodity_name"] == "Rice") &
    (df["country"] == "Kenya") &
    (df["price_source"] == "Domestic")
]

print(df_rice[["date", "price_per_unit", "unit_std", "market"]].head())
```

---

## Analysis

Interactive analysis notebooks are available in `scripts/analysis_scripts/`. See the [Analysis README](scripts/analysis_scripts/README.md) for details and one-click Binder launch badges.

Both notebooks (`RawDataAnalysis.ipynb` and `StandardizedDataAnalysis.ipynb`) provide:

- **Dual panel mode** — compare two commodity/country/market combinations side by side.
- **Multi-selection mode** — overlay any number of series on a single combined plot.
- **Descriptive statistics** — count, min, max, mean, median, standard deviation, % change, data length per country, date ranges, null counts, and frequency gap analysis.
- **Dynamic filtering** — cascading dropdowns for source → commodity → price type → country → market.

---

## Environment Setup

**Using Conda (recommended):**
```bash
conda env create -f environment.yml
conda activate fpma
jupyter lab
```

**Using pip:**
```bash
pip install -r requirements.txt
```

**Dependencies:** Python 3.10, pandas, plotly, ipywidgets, jupyterlab, nodejs.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

[![pages-build-deployment](https://github.com/tezamo/FPMA/actions/workflows/pages/pages-build-deployment/badge.svg)](https://github.com/tezamo/FPMA/actions/workflows/pages/pages-build-deployment)
[![contributors](https://img.shields.io/github/contributors/tezamo/FPMA.svg)](https://github.com/tezamo/FPMA/graphs/contributors)
[![GitHub release](https://img.shields.io/github/v/release/tezamo/FPMA.svg)](https://GitHub.com/tezamo/FPMA/releases/)
[![GitHub license](https://img.shields.io/github/license/tezamo/FPMA.svg)](https://github.com/tezamo/FPMA/blob/main/LICENSE)