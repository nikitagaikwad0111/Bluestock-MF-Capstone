"""
data_ingestion.py
-----------------
Bluestock Fintech — Mutual Fund Analytics Capstone
Day 1: Data Ingestion Script

Description:
    Loads all 10 raw CSV datasets from the data/raw/ directory.
    Validates shape, data types, null values, and logs anomalies.

Usage:
    python scripts/data_ingestion.py

Author: Nikita Gaikwad
Date: June 2026
"""

import pandas as pd
import os


# ─── Configuration ────────────────────────────────────────────────────────────

RAW_PATH = "data/raw/"

CSV_FILES = [
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


# ─── Functions ────────────────────────────────────────────────────────────────

def load_and_validate(filepath: str) -> tuple[pd.DataFrame, list]:
    """
    Load a CSV file and validate for null values.

    Args:
        filepath (str): Full path to the CSV file.

    Returns:
        tuple: (DataFrame, list of anomaly messages)
    """
    anomalies = []
    df = pd.read_csv(filepath)

    nulls = df.isnull().sum()
    if nulls.any():
        anomaly_msg = f"{os.path.basename(filepath)} has null values in: {list(nulls[nulls > 0].index)}"
        anomalies.append(anomaly_msg)

    return df, anomalies


def run_ingestion() -> None:
    """
    Main ingestion function.
    Loads all 10 CSV files, prints summary, and reports anomalies.
    """
    all_anomalies = []

    for file in CSV_FILES:
        filepath = os.path.join(RAW_PATH, file)

        if not os.path.exists(filepath):
            print(f"❌ File not found: {filepath}")
            continue

        df, anomalies = load_and_validate(filepath)
        all_anomalies.extend(anomalies)

        print(f"\n{'='*55}")
        print(f"FILE: {file}")
        print(f"Shape: {df.shape}")
        print(f"Data Types:\n{df.dtypes}")
        print(f"First 3 Rows:\n{df.head(3)}")

        if anomalies:
            for a in anomalies:
                print(f"⚠️  {a}")
        else:
            print("✅ No null values found")

    # ── Summary ──
    print(f"\n{'='*55}")
    print("DATA QUALITY SUMMARY")
    print(f"{'='*55}")
    if all_anomalies:
        for a in all_anomalies:
            print(f"⚠️  {a}")
    else:
        print("✅ All files loaded cleanly with no anomalies!")


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_ingestion()
