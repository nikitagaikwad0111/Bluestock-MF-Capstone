# 🏦 Bluestock Fintech — Mutual Fund Analytics Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Power BI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)
![SQLite](https://img.shields.io/badge/SQLite-Database-green)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

A full-stack Mutual Fund Analytics Platform built during a 7-day capstone internship at **Bluestock Fintech Pvt. Ltd.** The project ingests publicly available AMFI India data, transforms it through an ETL pipeline, stores it in SQLite, and presents insights via an interactive Power BI dashboard.

---

## 📁 Project Structure

```
bluestock_mf_capstone/
├── data/
│   ├── raw/                    ← Original CSV datasets (10 files)
│   └── processed/              ← Cleaned CSVs + SQLite DB
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   ├── data_ingestion.py       ← ETL pipeline
│   ├── live_nav_fetch.py       ← mfapi.in NAV fetcher
│   └── recommender.py          ← Fund recommendation engine
├── sql/
│   ├── schema.sql              ← Database schema
│   └── queries.sql             ← 10 analytical queries
├── dashboard/
│   ├── bluestock_mf_dashboard.pbix  ← Power BI dashboard
│   ├── Dashboard.pdf
│   ├── Page1_Industry_Overview.png
│   ├── Page2_Fund_Performance.png
│   ├── Page3_Investor_Analytics.png
│   └── Page4_SIP_Market_Trends.png
├── reports/
│   ├── Final_Report.pdf
│   ├── Bluestock_MF_Presentation.pptx
│   └── rolling_sharpe_chart.png
├── requirements.txt
└── README.md
```

---

## 📊 Dataset Description

| File | Rows | Description |
|------|------|-------------|
| `01_fund_master.csv` | 40 | Master list of 40 mutual fund schemes |
| `02_nav_history.csv` | 46,000 | Daily NAV Jan 2022 – May 2026 |
| `03_aum_by_fund_house.csv` | 90 | Quarterly AUM by AMC 2022–2025 |
| `04_monthly_sip_inflows.csv` | 48 | Monthly SIP inflow data |
| `05_category_inflows.csv` | 144 | Net inflows by fund category |
| `06_industry_folio_count.csv` | 21 | Total MF folios by type |
| `07_scheme_performance.csv` | 40 | Risk-return metrics per scheme |
| `08_investor_transactions.csv` | 32,000 | SIP/Lumpsum/Redemption transactions |
| `09_portfolio_holdings.csv` | 322 | Top equity holdings per fund |
| `10_benchmark_indices.csv` | 8,050 | Daily Nifty 50, Nifty 100, BSE SmallCap |

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/nikitagaikwad0111/bluestock_mf_capstone.git
cd bluestock_mf_capstone
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Verify Dataset
```bash
ls data/raw/
# Should show all 10 CSV files
```

---

## 🚀 How to Run the ETL Pipeline

### Option 1 — Run Individual Notebooks
Open Jupyter and run notebooks in order:
```bash
jupyter notebook
```
1. `01_data_ingestion.ipynb`
2. `02_data_cleaning.ipynb`
3. `03_eda_analysis.ipynb`
4. `04_performance_analytics.ipynb`
5. `05_advanced_analytics.ipynb`

### Option 2 — Run Master Pipeline Script
```bash
python scripts/run_pipeline.py
```

### Option 3 — Fetch Live NAV Data
```bash
python scripts/live_nav_fetch.py
```

---

## 📈 How to Open the Dashboard

1. Install **Power BI Desktop** (free) from [Microsoft](https://powerbi.microsoft.com/)
2. Open `dashboard/bluestock_mf_dashboard.pbix`
3. If prompted to refresh data, point to `data/processed/` folder
4. Navigate through 4 pages:
   - **Page 1:** Industry Overview
   - **Page 2:** Fund Performance
   - **Page 3:** Investor Analytics
   - **Page 4:** SIP & Market Trends

---

## 🤖 How to Run Fund Recommender
```bash
python scripts/recommender.py
```
Enter risk appetite (Low / Moderate / High) to get top 3 fund recommendations.

---

## 📐 Key Metrics Computed

| Metric | Description |
|--------|-------------|
| CAGR | 1yr, 3yr, 5yr Compound Annual Growth Rate |
| Sharpe Ratio | Risk-adjusted return (Rf = 6.5%) |
| Sortino Ratio | Downside risk-adjusted return |
| Alpha | Excess return over benchmark |
| Beta | Market sensitivity |
| Max Drawdown | Worst peak-to-trough decline |
| VaR (95%) | Maximum daily loss at 95% confidence |
| CVaR | Expected loss beyond VaR threshold |
| HHI | Sector concentration index |

---

## 🔑 Key Findings

1. **ICICI Pru Midcap** ranks #1 in Fund Scorecard (composite score: 73.62)
2. **Small Cap funds** carry highest risk — VaR of -2.3% to -2.4% daily
3. **97.8% SIP investors** show at-risk behavior (gap > 35 days)
4. **SBI Mutual Fund** dominates AUM with ₹12.5L Cr (largest AMC)
5. **Axis Bluechip** is most concentrated fund (HHI: 2,967)

---

## 🛠️ Tech Stack

| Category | Tool |
|----------|------|
| Language | Python 3.10+ |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn, Plotly |
| Database | SQLite3, SQLAlchemy |
| Statistics | SciPy |
| Dashboard | Power BI Desktop |
| Version Control | Git + GitHub |
| API | mfapi.in |

---

## 👩‍💻 Author

**Nikita Gaikwad**
MSc Statistics | Data Analyst Intern — Bluestock Fintech
GitHub: [@nikitagaikwad0111](https://github.com/nikitagaikwad0111)

---

## ⚠️ Disclaimer

All data is sourced from publicly available AMFI India, NSE, BSE and open APIs.
This project is for **educational purposes only** and does not constitute financial advice.
