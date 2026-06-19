"""
live_nav_fetch.py
-----------------
Bluestock Fintech — Mutual Fund Analytics Capstone
Day 1: Live NAV Fetcher

Description:
    Fetches live historical NAV data from mfapi.in REST API
    for 6 selected mutual fund schemes and saves as CSV files.

Usage:
    python scripts/live_nav_fetch.py

API:
    GET https://api.mfapi.in/mf/{scheme_code}
    No authentication required.

Author: Nikita Gaikwad
Date: June 2026
"""

import requests
import pandas as pd
import os


# ─── Configuration ────────────────────────────────────────────────────────────

OUTPUT_DIR = "data/raw/"

SCHEMES = [
    (119551, "SBI Bluechip"),
    (120503, "ICICI Bluechip"),
    (118632, "Nippon Large Cap"),
    (119092, "Axis Bluechip"),
    (120841, "Kotak Bluechip"),
]

HDFC_TOP100 = (125497, "HDFC Top 100 Direct")


# ─── Functions ────────────────────────────────────────────────────────────────

def fetch_nav(scheme_code: int, scheme_name: str) -> pd.DataFrame | None:
    """
    Fetch historical NAV data for a single scheme from mfapi.in.

    Args:
        scheme_code (int): AMFI scheme code.
        scheme_name (str): Human-readable scheme name.

    Returns:
        pd.DataFrame or None: NAV data if successful, None if failed.
    """
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    print(f"Fetching: {scheme_name} (Code: {scheme_code})")

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()
        nav_list = data["data"]

        df = pd.DataFrame(nav_list)
        df["amfi_code"] = scheme_code
        df["scheme_name"] = scheme_name

        filename = os.path.join(OUTPUT_DIR, f"live_nav_{scheme_code}.csv")
        df.to_csv(filename, index=False)
        print(f"  ✅ Saved {len(df)} rows → {filename}")
        return df

    except requests.exceptions.RequestException as e:
        print(f"  ❌ Failed to fetch {scheme_name}: {e}")
        return None


def run_nav_fetch() -> None:
    """
    Main function to fetch NAV for all configured schemes
    and save a combined master CSV file.
    """
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    all_dfs = []

    # Fetch HDFC Top 100
    df = fetch_nav(*HDFC_TOP100)
    if df is not None:
        all_dfs.append(df)

    # Fetch 5 key schemes
    for code, name in SCHEMES:
        df = fetch_nav(code, name)
        if df is not None:
            all_dfs.append(df)

    # Save master file
    if all_dfs:
        master_df = pd.concat(all_dfs, ignore_index=True)
        master_path = os.path.join(OUTPUT_DIR, "all_live_nav.csv")
        master_df.to_csv(master_path, index=False)
        print(f"\n✅ Master file saved: {len(master_df)} total rows → {master_path}")
    else:
        print("\n❌ No data fetched. Check network connection.")


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    run_nav_fetch()
