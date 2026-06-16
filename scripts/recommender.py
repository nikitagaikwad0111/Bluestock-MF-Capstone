
import pandas as pd

# Load data
df_perf = pd.read_csv("../data/processed/clean_performance.csv")
df_master = pd.read_csv("../data/raw/01_fund_master.csv")

# Merge
df_merged = df_perf.merge(
    df_master[["amfi_code", "risk_category"]], 
    on="amfi_code"
)

def recommend_funds(risk_appetite):
    """
    Input: risk_appetite = Low / Moderate / High
    Output: Top 3 funds by Sharpe ratio
    """
    filtered = df_merged[df_merged["risk_category"] == risk_appetite]
    top3 = filtered.nlargest(3, "sharpe_ratio")[
        ["scheme_name", "fund_house", "sharpe_ratio", 
         "return_3yr_pct", "risk_category"]
    ]
    return top3

if __name__ == "__main__":
    for risk in ["Low", "Moderate", "High"]:
        print(f"\n{'='*50}")
        print(f"Top 3 Funds for {risk} Risk Appetite:")
        print("="*50)
        print(recommend_funds(risk).to_string(index=False))
