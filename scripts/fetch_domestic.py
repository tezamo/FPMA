# ╔════════════════════════════════════╗
# ║             TEZAMO                 ║
# ╚════════════════════════════════════╝

import requests
import pandas as pd
from time import sleep
import os

# Step 1: Fetch all domestic commodities
url_series = "https://fpma.fao.org/giews/v4/global/price_module/api/v1/FpmaSerieDomestic/?newerThan=12 months ago"
series_data = requests.get(url_series).json()

# Output folder 
output_folder = "domestic_commodities"
os.makedirs(output_folder, exist_ok=True)

# Step 2: Loop over all commodities
for item in series_data['results']:
    uuid = item['uuid']
    commodity_name = item.get('commodity_name', 'Unknown')
    country = item.get('country_name', 'Unknown')
    market = item.get('market_name', 'Unknown')
    price_type = item.get('price_type', 'Unknown')
    unit = item.get('measure_unit_label', 'Unknown')
    currency = item.get('currency', 'Unknown')  # local currency label

    # Step 3: Fetch prices for this commodity
    url_price = (
        f"https://fpma.fao.org/giews/v4/global/price_module/api/v1/"
        f"FpmaSeriePrice/?uuid__in={uuid}&periodicity=monthly"
    )
    resp = requests.get(url_price).json()

    if resp['count'] == 0:
        continue  # no prices, skip

    datapoints = resp['results'][0]['datapoints']
    rows = []

    for dp in datapoints:
        # USD price — may be None for some periods
        price_usd = dp.get('price_value_dollar')

        # Local currency nominal — try common field names
        price_local = dp.get('price_value') or dp.get('price_value_nominal')

        # Skip only if BOTH are missing
        if price_usd is None and price_local is None:
            continue

        rows.append({
            'date': dp['date'],
            'price_usd': price_usd,
            'price_local': price_local,
            'currency': currency,
            'commodity_name': commodity_name,
            'country': country,
            'market': market,
            'price_type': price_type,
            'unit': unit,
            'price_source': 'Domestic'
        })

    if not rows:
        continue
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
removed for privacy concerns
.
.
.
.
.
.
.
.
.
.
.
.
.
    
    df.index.name = "date"
    df = df.reset_index()
    df = df[['date', 'price_usd', 'price_local', 'currency',
             'commodity_name', 'country', 'market', 'price_type', 'unit', 'price_source']]

    # Step 4: Save CSV
    safe_name = "".join(c if c.isalnum() else "_" for c in commodity_name)
    csv_path = os.path.join(output_folder, f"{safe_name}.csv")
    df.to_csv(csv_path, index=False)

    print(f"Saved {csv_path} with {len(df)} monthly rows")

    # Avoid API overload
    sleep(0.2)

print("All domestic commodities downloaded!")

# ╔════════════════════════════════════╗
# ║             TEZAMO                 ║
# ╚════════════════════════════════════╝