# Bluestock MF Capstone — Data Dictionary

## 01. dim_fund (Fund Master)
| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme code (Primary Key) |
| scheme_name | TEXT | Full official fund name |
| fund_house | TEXT | AMC name (e.g. SBI Mutual Fund) |
| category | TEXT | Equity / Debt / Hybrid |
| sub_category | TEXT | Large Cap / Mid Cap / Small Cap etc. |
| plan | TEXT | Regular or Direct |
| benchmark | TEXT | Official benchmark index |
| expense_ratio_pct | REAL | Annual fee charged (0.1% to 2.5%) |
| exit_load_pct | REAL | Exit load percentage |
| fund_manager | TEXT | Primary fund manager name |
| risk_category | TEXT | Low / Moderate / High / Very High |
| launch_date | TEXT | Fund launch date |

## 02. fact_nav (NAV History)
| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER | Foreign key to dim_fund |
| date | TEXT | NAV date (business days + forward filled) |
| nav | REAL | Net Asset Value in Rs. |

## 03. fact_transactions (Investor Transactions)
| Column | Type | Description |
|---|---|---|
| investor_id | TEXT | Unique investor ID (INV000001 to INV005000) |
| transaction_date | TEXT | Date of transaction |
| amfi_code | INTEGER | Foreign key to dim_fund |
| transaction_type | TEXT | SIP / Lumpsum / Redemption |
| amount_inr | INTEGER | Transaction amount in rupees |
| state | TEXT | Investor's state |
| city | TEXT | Investor's city |
| city_tier | TEXT | T30 (Top 30) or B30 (Beyond Top 30) |
| age_group | TEXT | 18-25 / 26-35 / 36-45 / 46-55 / 56+ |
| gender | TEXT | Male / Female |
| annual_income_lakh | REAL | Annual income in lakhs |
| payment_mode | TEXT | UPI / Net Banking / Mandate / Cheque |
| kyc_status | TEXT | Verified / Pending |

## 04. fact_performance (Scheme Performance)
| Column | Type | Description |
|---|---|---|
| amfi_code | INTEGER | Foreign key to dim_fund |
| return_1yr_pct | REAL | 1 year absolute return % |
| return_3yr_pct | REAL | 3 year CAGR % |
| return_5yr_pct | REAL | 5 year CAGR % |
| benchmark_3yr_pct | REAL | Benchmark 3yr CAGR % |
| alpha | REAL | Return above benchmark |
| beta | REAL | Sensitivity to market movements |
| sharpe_ratio | REAL | Risk adjusted return (higher is better) |
| sortino_ratio | REAL | Like Sharpe but only penalises downside |
| std_dev_ann_pct | REAL | Annualised standard deviation % |
| max_drawdown_pct | REAL | Worst peak to trough decline (negative) |
| aum_crore | INTEGER | Assets under management in crore |
| expense_ratio_pct | REAL | Annual fee charged % |
| morningstar_rating | INTEGER | 1 to 5 star rating |
| risk_grade | TEXT | Low / Moderate / High / Very High |

## 05. fact_aum (AUM by Fund House)
| Column | Type | Description |
|---|---|---|
| fund_house | TEXT | AMC name |
| date | TEXT | Quarter end date |
| aum_crore | REAL | Total AUM in crore |
| num_schemes | INTEGER | Number of schemes |

## Data Sources
| Dataset | Source |
|---|---|
| NAV History | mfapi.in + AMFI India |
| Fund Master | AMFI India |
| Investor Transactions | Simulated (real distributions) |
| Scheme Performance | Computed from NAV history |
| AUM Data | AMFI Quarterly Reports |

## Data Quality Notes
- nav_history: date converted from text to datetime, forward filled for weekends/holidays
- investor_transactions: transaction_date converted to datetime, SIP capitalization fixed
- scheme_performance: all values validated, expense ratio within 0.1%-2.5% range
- All 40 AMFI codes validated across fund_master and nav_history