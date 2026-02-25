# ╔════════════════════════════════════╗
# ║             TEZAMO                 ║
# ╚════════════════════════════════════╝

import requests
import pandas as pd
from time import sleep
import os

# Step 1: Fetch all international commodities
url_series = "https://fpma.fao.org/giews/v4/global/price_module/api/v1/FpmaSerieInternational/?limit=500"
series_data = requests.get(url_series).json()

# Output folder
output_folder = "commodity_prices"
os.makedirs(output_folder, exist_ok=True)

# Step 2: Loop over all commodities
for item in series_data['results']:
    uuid = item['uuid']
    commodity_name = item.get('commodity_name', 'Unknown')
    country = item.get('market_name', 'Unknown')
    market = item.get('country_name', 'Unknown')
    price_type = item.get('price_type', 'Unknown')
    unit = item.get('measure_unit_label', 'Unknown')

    # Step 3: Fetch prices for this commodity
    url_price = (
        f"https://fpma.fao.org/giews/v4/global/price_module/api/v1/"
        f"FpmaSeriePrice/?uuid__in={uuid}&periodicity=monthly"
    )
    resp = requests.get(url_price).json()

    if resp['count'] == 0:
        continue  # no prices, skip

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
    df = df[['date', 'price_usd', 'commodity_name', 'country', 'market', 'price_type', 'unit', 'price_source']]

    # Step 4: Save CSV
    safe_name = "".join(c if c.isalnum() else "_" for c in commodity_name)
    csv_path = os.path.join(output_folder, f"{safe_name}.csv")
    df.to_csv(csv_path, index=False)

    print(f"Saved {csv_path} with {len(df)} monthly rows")

    # Avoid API overload
    sleep(0.2)

print("All international commodities downloaded")

# ╔════════════════════════════════════╗
# ║             TEZAMO                 ║
# ╚════════════════════════════════════╝

