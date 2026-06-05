-- Bluestock MF Capstone - Analytical Queries

-- Q1: Top 5 funds by AUM
SELECT scheme_name, fund_house, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Q2: Average NAV per month for SBI Bluechip
SELECT strftime('%Y-%m', date) as month, 
       ROUND(AVG(nav), 2) as avg_nav
FROM fact_nav
WHERE amfi_code = 119551
GROUP BY month
ORDER BY month;

-- Q3: SIP inflow YoY growth
SELECT year, month, sip_inflow_crore, yoy_growth_pct
FROM fact_sip_industry
ORDER BY year, month;

-- Q4: Total transactions by state
SELECT state, 
       COUNT(*) as total_transactions,
       SUM(amount_inr) as total_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Q5: Funds with expense ratio less than 1%
SELECT f.scheme_name, f.fund_house, p.expense_ratio_pct
FROM dim_fund f
JOIN fact_performance p ON f.amfi_code = p.amfi_code
WHERE p.expense_ratio_pct < 1.0
ORDER BY p.expense_ratio_pct ASC;

-- Q6: Top 5 funds by Sharpe ratio
SELECT f.scheme_name, f.fund_house, p.sharpe_ratio
FROM dim_fund f
JOIN fact_performance p ON f.amfi_code = p.amfi_code
ORDER BY p.sharpe_ratio DESC
LIMIT 5;

-- Q7: Transaction split by type
SELECT transaction_type,
       COUNT(*) as count,
       SUM(amount_inr) as total_amount
FROM fact_transactions
GROUP BY transaction_type;

-- Q8: Average SIP amount by age group
SELECT age_group,
       ROUND(AVG(amount_inr), 2) as avg_sip_amount,
       COUNT(*) as total_transactions
FROM fact_transactions
WHERE transaction_type = 'SIP'
GROUP BY age_group
ORDER BY avg_sip_amount DESC;

-- Q9: Top 5 funds by 3 year returns
SELECT f.scheme_name, f.fund_house, p.return_3yr_pct
FROM dim_fund f
JOIN fact_performance p ON f.amfi_code = p.amfi_code
ORDER BY p.return_3yr_pct DESC
LIMIT 5;

-- Q10: AUM by fund house latest quarter
SELECT fund_house, 
       ROUND(aum_crore, 2) as aum_crore
FROM fact_aum
WHERE date = (SELECT MAX(date) FROM fact_aum)
ORDER BY aum_crore DESC;