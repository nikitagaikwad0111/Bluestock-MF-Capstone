-- Bluestock MF Capstone - Database Schema
-- Star Schema Design

-- DIMENSION TABLE 1: Fund Master
CREATE TABLE IF NOT EXISTS dim_fund (
    amfi_code       INTEGER PRIMARY KEY,
    scheme_name     TEXT NOT NULL,
    fund_house      TEXT NOT NULL,
    category        TEXT,
    sub_category    TEXT,
    plan            TEXT,
    benchmark       TEXT,
    expense_ratio_pct REAL,
    exit_load_pct   REAL,
    fund_manager    TEXT,
    risk_category   TEXT,
    launch_date     TEXT
);

-- DIMENSION TABLE 2: Date
CREATE TABLE IF NOT EXISTS dim_date (
    date_id         TEXT PRIMARY KEY,
    year            INTEGER,
    month           INTEGER,
    quarter         INTEGER,
    month_name      TEXT,
    is_weekday      INTEGER
);

-- FACT TABLE 1: NAV History
CREATE TABLE IF NOT EXISTS fact_nav (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code       INTEGER,
    date            TEXT,
    nav             REAL,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- FACT TABLE 2: Investor Transactions
CREATE TABLE IF NOT EXISTS fact_transactions (
    tx_id               INTEGER PRIMARY KEY AUTOINCREMENT,
    investor_id         TEXT,
    transaction_date    TEXT,
    amfi_code           INTEGER,
    transaction_type    TEXT,
    amount_inr          INTEGER,
    state               TEXT,
    city                TEXT,
    city_tier           TEXT,
    age_group           TEXT,
    gender              TEXT,
    annual_income_lakh  REAL,
    payment_mode        TEXT,
    kyc_status          TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- FACT TABLE 3: Fund Performance
CREATE TABLE IF NOT EXISTS fact_performance (
    id                  INTEGER PRIMARY KEY AUTOINCREMENT,
    amfi_code           INTEGER,
    return_1yr_pct      REAL,
    return_3yr_pct      REAL,
    return_5yr_pct      REAL,
    benchmark_3yr_pct   REAL,
    alpha               REAL,
    beta                REAL,
    sharpe_ratio        REAL,
    sortino_ratio       REAL,
    std_dev_ann_pct     REAL,
    max_drawdown_pct    REAL,
    aum_crore           INTEGER,
    expense_ratio_pct   REAL,
    morningstar_rating  INTEGER,
    risk_grade          TEXT,
    FOREIGN KEY (amfi_code) REFERENCES dim_fund(amfi_code)
);

-- FACT TABLE 4: AUM by Fund House
CREATE TABLE IF NOT EXISTS fact_aum (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    fund_house      TEXT,
    date            TEXT,
    aum_crore       REAL,
    num_schemes     INTEGER
);