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

    datapoints = resp['results'][0]['datapoints']
    rows = []

    for dp in datapoints:
        price_usd = dp.get('price_value_dollar') or dp.get('price_value')
        if price_usd is None:
            continue

        date = dp['date']  # YYYY-MM-DD
        rows.append({
             'date': date,
             'price_usd': price_usd,
             'commodity_name': commodity_name,
             'country': country,
             'market': market,
             'price_type': price_type,
             'unit': unit,
             'price_source': 'International'
        })

    if not rows:
        continue

    # ---- GAP FILLING ----
    df = pd.DataFrame(rows)
    df['date'] = pd.to_datetime(df['date'])

    # Make full month range
    full_range = pd.date_range(
        start=df['date'].min(),
        end=df['date'].max(),
        freq='MS'   # Month Start
    )

    # Reindex to full monthly range → missing months become NaN
    df = df.set_index('date').reindex(full_range)

    # Restore identifying fields for all rows
    df['commodity_name'] = commodity_name
    df['country'] = country
    df['market'] = market
    df['price_type'] = price_type
    df['unit'] = unit
    df['price_source'] = 'International'

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

