# 🌾 FPMA — FAO Food Price Monitoring and Analysis

> Automated collection, processing, and archiving of global commodity price data from the [FAO GIEWS FPMA platform](https://fpma.fao.org/giews/fpmat4/#/dashboard/tool/international).

---

## 📌 Overview

This repository provides:

- **Python scripts** to fetch and process commodity price data from the FAO FPMA API
- **International prices** — benchmark global commodity prices (USD)
- **Domestic prices** — country-level market prices in both USD and local currency
- **CSV datasets** — gap-filled monthly time series, ready for analysis

Data is sourced from the [FAO GIEWS Price Module API](https://fpma.fao.org/giews/v4/global/price_module/api/v1/) and covers commodities such as wheat, maize, rice, soybeans, sugar, and many more across global and domestic markets.

---

## 🗂️ Repository Structure

```
FPMA/
│
├── README.md                        # This file
│
├── scripts/
│   ├── fetch_international.py       # Fetches all international commodity prices
│   └── fetch_domestic.py            # Fetches domestic commodity prices (last 12 months of active series)
│
├── commodity_prices/                # Output: International price CSVs (one file per commodity)
│   ├── Wheat.csv
│   ├── Maize.csv
│   ├── Rice.csv
│   └── ...
│
└── domestic_commodities/            # Output: Domestic price CSVs (one file per commodity)
    ├── Wheat.csv
    ├── Maize.csv
    ├── Rice.csv
    └── ...
```

---

## 📁 Data Description

### `commodity_prices/` — International Prices

Each CSV file corresponds to one internationally traded commodity and contains monthly observations.

| Column | Description |
|---|---|
| `date` | Month start date (`YYYY-MM-DD`) |
| `price_usd` | Price in US Dollars |
| `commodity_name` | Name of the commodity |
| `country` | Country or region of origin |
| `market` | Market name |
| `price_type` | Type of price (e.g., export, import, wholesale) |
| `unit` | Unit of measurement (e.g., MT, bushel) |
| `price_source` | Always `International` |

---

### `domestic_commodities/` — Domestic Prices

Each CSV file corresponds to one commodity traded in domestic markets, with both USD and local currency prices.

| Column | Description |
|---|---|
| `date` | Month start date (`YYYY-MM-DD`) |
| `price_usd` | Price converted to US Dollars (may be `NaN`) |
| `price_local` | Price in local currency |
| `currency` | Local currency label |
| `commodity_name` | Name of the commodity |
| `country` | Country of the market |
| `market` | Market name |
| `price_type` | Type of price (e.g., retail, wholesale) |
| `unit` | Unit of measurement |
| `price_source` | Always `Domestic` |

> **Note:** Missing months within a series are preserved as `NaN` rows (gap-filled) to maintain a continuous monthly time index.

---

## ⚙️ Scripts

### `scripts/fetch_international.py`

Fetches all available international commodity price series from the FPMA API, downloads monthly prices, gap-fills the time series, and saves one CSV per commodity to `commodity_prices/`.

**Run:**
```bash
python scripts/fetch_international.py
```

---

### `scripts/fetch_domestic.py`

Fetches domestic commodity price series updated within the last 12 months, downloads monthly prices (USD + local currency), gap-fills the time series, and saves one CSV per commodity to `domestic_commodities/`.

**Run:**
```bash
python scripts/fetch_domestic.py
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/FPMA.git
cd FPMA
```

### 2. Install dependencies
```bash
pip install requests pandas
```

### 3. Run the scripts
```bash
python scripts/fetch_international.py
python scripts/fetch_domestic.py
```

CSV files will be saved to `commodity_prices/` and `domestic_commodities/` respectively.

---

## 📊 Data Source

All data is retrieved from the **FAO GIEWS Food Price Monitoring and Analysis (FPMA)** tool:

- 🌐 Website: [https://fpma.fao.org](https://fpma.fao.org)
- 📡 API Base: `https://fpma.fao.org/giews/v4/global/price_module/api/v1/`

**FAO GIEWS** (Global Information and Early Warning System on Food and Agriculture) monitors food supply and demand conditions worldwide.

---

## 📋 Notes

- Scripts include a `0.2s` sleep between API calls to avoid overloading the FAO server — please respect this.
- Prices are monthly. Some series may have significant `NaN` gaps where data was not reported.
- `price_usd` for domestic series may be `NaN` for older periods where USD conversion was unavailable.
- File names are derived from the commodity name with special characters replaced by underscores.

---

## 📄 License

Data is provided by the **Food and Agriculture Organization of the United Nations (FAO)** and is subject to [FAO's terms of use](https://www.fao.org/contact-us/terms/en/).

Scripts in this repository are released under the **MIT License**.

---

## 🙏 Acknowledgements

Data sourced from the [FAO GIEWS FPMA Tool](https://fpma.fao.org/giews/fpmat4/#/dashboard/tool/international).  
This repository is not officially affiliated with or endorsed by FAO.









