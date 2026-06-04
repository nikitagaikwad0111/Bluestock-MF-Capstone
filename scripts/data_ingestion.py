import pandas as pd
import os

# Path to raw data folder
RAW_PATH = "data/raw/"

# All 10 CSV files
csv_files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

anomalies = []

for file in csv_files:
    filepath = os.path.join(RAW_PATH, file)
    df = pd.read_csv(filepath)

    print(f"\n{'='*55}")
    print(f"FILE: {file}")
    print(f"Shape: {df.shape}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nFirst 3 Rows:\n{df.head(3)}")
    
    nulls = df.isnull().sum()
    if nulls.any():
        print(f"\n⚠️  Null Values Found:\n{nulls[nulls > 0]}")
        anomalies.append(f"{file} has null values in: {list(nulls[nulls > 0].index)}")
    else:
        print(f"\n✅ No null values found")

print(f"\n{'='*55}")
print("DATA QUALITY SUMMARY")
print(f"{'='*55}")
if anomalies:
    for a in anomalies:
        print(f"⚠️  {a}")
else:
    print("✅ All files loaded cleanly with no anomalies!")