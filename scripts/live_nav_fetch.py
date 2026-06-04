import requests
import pandas as pd
import os

def fetch_nav(scheme_code, scheme_name):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"Fetching: {scheme_name} (Code: {scheme_code})")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        nav_list = data['data']
        df = pd.DataFrame(nav_list)
        df['amfi_code'] = scheme_code
        df['scheme_name'] = scheme_name
        filename = f"data/raw/live_nav_{scheme_code}.csv"
        df.to_csv(filename, index=False)
        print(f"  ✅ Saved {len(df)} rows → {filename}")
        return df
    else:
        print(f"  ❌ Failed! Status: {response.status_code}")
        return None

# HDFC Top 100 Direct
fetch_nav(125497, "HDFC Top 100 Direct")

# 5 Key Schemes
schemes = [
    (119551, "SBI Bluechip"),
    (120503, "ICICI Bluechip"),
    (118632, "Nippon Large Cap"),
    (119092, "Axis Bluechip"),
    (120841, "Kotak Bluechip"),
]

all_dfs = []
for code, name in schemes:
    df = fetch_nav(code, name)
    if df is not None:
        all_dfs.append(df)

# Combine all into one master file
master_df = pd.concat(all_dfs, ignore_index=True)
master_df.to_csv("data/raw/all_live_nav.csv", index=False)
print(f"\n✅ Master file saved: {len(master_df)} total rows")