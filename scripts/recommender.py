"""
recommender.py
--------------
Bluestock Fintech — Mutual Fund Analytics Capstone
Day 6: Fund Recommendation Engine

Description:
    Simple rule-based fund recommender.
    Input: Investor risk appetite (Low / Moderate / High)
    Output: Top 3 mutual funds by Sharpe ratio within matching risk grade.

Usage:
    python scripts/recommender.py

Author: Nikita Gaikwad
Date: June 2026
"""

import pandas as pd
import os


# ─── Configuration ────────────────────────────────────────────────────────────

PROCESSED_DIR = "data/processed/"
RAW_DIR = "data/raw/"

RISK_LEVELS = ["Low", "Moderate", "High"]


# ─── Data Loading ─────────────────────────────────────────────────────────────

def load_data() -> pd.DataFrame:
    """
    Load and merge clean_performance with fund_master to get risk categories.

    Returns:
        pd.DataFrame: Merged dataframe with performance metrics and risk category.
    """
    df_perf = pd.read_csv(os.path.join(PROCESSED_DIR, "clean_performance.csv"))
    df_master = pd.read_csv(os.path.join(RAW_DIR, "01_fund_master.csv"))

    df_merged = df_perf.merge(
        df_master[["amfi_code", "risk_category"]],
        on="amfi_code"
    )
    return df_merged


# ─── Recommender ──────────────────────────────────────────────────────────────

def recommend_funds(df: pd.DataFrame, risk_appetite: str) -> pd.DataFrame:
    """
    Recommend top 3 funds based on investor risk appetite.

    Args:
        df (pd.DataFrame): Merged performance + master dataframe.
        risk_appetite (str): One of 'Low', 'Moderate', or 'High'.

    Returns:
        pd.DataFrame: Top 3 funds sorted by Sharpe ratio.

    Raises:
        ValueError: If risk_appetite is not one of the valid options.
    """
    if risk_appetite not in RISK_LEVELS:
        raise ValueError(f"Invalid risk appetite: '{risk_appetite}'. Choose from {RISK_LEVELS}")

    filtered = df[df["risk_category"] == risk_appetite]

    top3 = filtered.nlargest(3, "sharpe_ratio")[
        ["scheme_name", "fund_house", "sharpe_ratio",
         "return_3yr_pct", "risk_category"]
    ]
    return top3


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    df = load_data()

    for risk in RISK_LEVELS:
        print(f"\n{'='*55}")
        print(f"  Top 3 Funds for {risk} Risk Appetite")
        print(f"{'='*55}")
        result = recommend_funds(df, risk)
        print(result.to_string(index=False))

    print("\n✅ Recommendation complete.")
