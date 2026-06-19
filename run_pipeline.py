"""
run_pipeline.py
---------------
Bluestock Fintech — Mutual Fund Analytics Capstone
Master Execution Script

Description:
    Runs the complete ETL pipeline in sequence:
    Step 1 — Data Ingestion (load & validate all 10 CSVs)
    Step 2 — Live NAV Fetch (fetch from mfapi.in)
    Step 3 — Fund Recommendation (print recommendations)

Usage:
    python run_pipeline.py

Author: Nikita Gaikwad
Date: June 2026
"""

import time
import sys
import os

# Add scripts directory to path
sys.path.append(os.path.join(os.path.dirname(__file__), "scripts"))


# ─── Imports ──────────────────────────────────────────────────────────────────

from data_ingestion import run_ingestion
from live_nav_fetch import run_nav_fetch
from recommender import load_data, recommend_funds


# ─── Pipeline Steps ───────────────────────────────────────────────────────────

def step1_ingestion() -> None:
    """Step 1: Load and validate all 10 raw CSV datasets."""
    print("\n" + "="*60)
    print("  STEP 1 — DATA INGESTION")
    print("="*60)
    run_ingestion()


def step2_nav_fetch() -> None:
    """Step 2: Fetch live NAV data from mfapi.in."""
    print("\n" + "="*60)
    print("  STEP 2 — LIVE NAV FETCH")
    print("="*60)
    run_nav_fetch()


def step3_recommender() -> None:
    """Step 3: Run fund recommender for all risk levels."""
    print("\n" + "="*60)
    print("  STEP 3 — FUND RECOMMENDER")
    print("="*60)
    df = load_data()
    for risk in ["Low", "Moderate", "High"]:
        print(f"\nTop 3 Funds — {risk} Risk:")
        print(recommend_funds(df, risk).to_string(index=False))


# ─── Main Pipeline ────────────────────────────────────────────────────────────

def main() -> None:
    """
    Master pipeline execution function.
    Runs all steps in sequence with timing.
    """
    print("\n" + "="*60)
    print("  BLUESTOCK FINTECH — MUTUAL FUND ANALYTICS PIPELINE")
    print("="*60)

    start_time = time.time()

    step1_ingestion()
    step2_nav_fetch()
    step3_recommender()

    elapsed = round(time.time() - start_time, 2)

    print("\n" + "="*60)
    print(f"  ✅ PIPELINE COMPLETE in {elapsed} seconds")
    print("="*60)


# ─── Entry Point ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    main()
