-- Top 5 funds by AUM
SELECT fund_house,
MAX(aum_crore)
FROM aum
GROUP BY fund_house
ORDER BY MAX(aum_crore) DESC
LIMIT 5;

-- Average NAV
SELECT
strftime('%Y-%m', date),
AVG(nav)
FROM nav_history
GROUP BY 1;

-- SIP Growth
SELECT
month,
yoy_growth_pct
FROM monthly_sip_inflows;

-- Transactions by state
SELECT
state,
COUNT(*)
FROM investor_transactions
GROUP BY state;

-- Expense ratio below 1%
SELECT
scheme_name,
expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1;

-- Top fund houses by schemes
SELECT
fund_house,
COUNT(*)
FROM fund_master
GROUP BY fund_house;

-- Highest Sharpe ratio
SELECT
scheme_name,
sharpe_ratio
FROM scheme_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- Highest returns
SELECT
scheme_name,
return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;

-- Investment by age group
SELECT
age_group,
AVG(amount_inr)
FROM investor_transactions
GROUP BY age_group;

-- Transactions by payment mode
SELECT
payment_mode,
COUNT(*)
FROM investor_transactions
GROUP BY payment_mode;