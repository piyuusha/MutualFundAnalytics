# Mutual Fund Analytics – Data Dictionary

## Dataset: 01_fund_master.csv

**Purpose:** Master reference dataset containing details of all mutual fund schemes.

| Column Name        | Data Type | Business Definition                     | Format / Units | Allowed Values                   |
| ------------------ | --------- | --------------------------------------- | -------------- | -------------------------------- |
| amfi_code          | Integer   | Unique AMFI scheme identifier           | Numeric        | Unique positive integer          |
| fund_house         | String    | Mutual fund company managing the scheme | Text           | SBI MF, HDFC MF, ICICI MF, etc.  |
| scheme_name        | String    | Official scheme name                    | Text           | Free text                        |
| category           | String    | Broad fund category                     | Text           | Equity, Debt, Hybrid             |
| sub_category       | String    | Detailed category classification        | Text           | Large Cap, Small Cap, Gilt, etc. |
| plan               | String    | Investment plan type                    | Text           | Regular, Direct                  |
| launch_date        | Date      | Scheme launch date                      | YYYY-MM-DD     | Valid date                       |
| benchmark          | String    | Benchmark index used for comparison     | Text           | NIFTY 50, BSE 200, etc.          |
| expense_ratio_pct  | Float     | Annual management fee charged by fund   | Percentage (%) | 0.1–2.5                          |
| exit_load_pct      | Float     | Exit charge applicable on redemption    | Percentage (%) | >= 0                             |
| min_sip_amount     | Integer   | Minimum SIP investment amount           | INR            | Positive value                   |
| min_lumpsum_amount | Integer   | Minimum lump-sum investment amount      | INR            | Positive value                   |
| fund_manager       | String    | Name of scheme fund manager             | Text           | Free text                        |
| risk_category      | String    | Risk classification assigned to scheme  | Text           | Low, Moderate, High, Very High   |
| sebi_category_code | String    | SEBI category identifier                | Text           | EC01, DC02, etc.                 |

---

## Dataset: 02_nav_history.csv

**Purpose:** Historical Net Asset Value (NAV) data for each mutual fund scheme.

| Column Name | Data Type | Business Definition           | Format / Units | Allowed Values            |
| ----------- | --------- | ----------------------------- | -------------- | ------------------------- |
| amfi_code   | Integer   | Mutual fund scheme identifier | Numeric        | Must exist in fund_master |
| date        | Date      | NAV observation date          | YYYY-MM-DD     | Valid date                |
| nav         | Float     | Net Asset Value per unit      | INR            | > 0                       |

---

## Dataset: 03_aum_by_fund_house.csv

**Purpose:** Assets Under Management (AUM) statistics by fund house.

| Column Name    | Data Type | Business Definition         | Format / Units | Allowed Values      |
| -------------- | --------- | --------------------------- | -------------- | ------------------- |
| date           | Date      | Reporting date              | YYYY-MM-DD     | Valid date          |
| fund_house     | String    | Fund house name             | Text           | Existing fund house |
| aum_lakh_crore | Float     | AUM expressed in lakh crore | Lakh Crore INR | >= 0                |
| aum_crore      | Integer   | AUM expressed in crore      | Crore INR      | >= 0                |
| num_schemes    | Integer   | Number of schemes managed   | Count          | >= 0                |

---

## Dataset: 04_monthly_sip_inflows.csv

**Purpose:** Monthly SIP industry statistics.

| Column Name               | Data Type | Business Definition         | Format / Units | Allowed Values |
| ------------------------- | --------- | --------------------------- | -------------- | -------------- |
| month                     | String    | Reporting month             | YYYY-MM        | Valid month    |
| sip_inflow_crore          | Integer   | Total SIP inflow            | Crore INR      | >= 0           |
| active_sip_accounts_crore | Float     | Active SIP accounts         | Crore Accounts | >= 0           |
| new_sip_accounts_lakh     | Float     | Newly opened SIP accounts   | Lakh Accounts  | >= 0           |
| sip_aum_lakh_crore        | Float     | SIP Assets Under Management | Lakh Crore INR | >= 0           |
| yoy_growth_pct            | Float     | Year-over-year SIP growth   | Percentage (%) | Nullable       |

---

## Dataset: 05_category_inflows.csv

| Column Name      | Data Type | Business Definition      | Format / Units |
| ---------------- | --------- | ------------------------ | -------------- |
| month            | String    | Reporting month          | YYYY-MM        |
| category         | String    | Mutual fund category     | Text           |
| net_inflow_crore | Float     | Net inflow into category | Crore INR      |

---

## Dataset: 06_industry_folio_count.csv

| Column Name         | Data Type | Business Definition | Format / Units |
| ------------------- | --------- | ------------------- | -------------- |
| month               | String    | Reporting month     | YYYY-MM        |
| total_folios_crore  | Float     | Total folio count   | Crore          |
| equity_folios_crore | Float     | Equity folios       | Crore          |
| debt_folios_crore   | Float     | Debt folios         | Crore          |
| hybrid_folios_crore | Float     | Hybrid folios       | Crore          |
| others_folios_crore | Float     | Other folios        | Crore          |

---

## Dataset: 07_scheme_performance.csv

**Purpose:** Performance and risk metrics of mutual fund schemes.

Include all columns exactly as present in the dataset with definitions for returns, alpha, beta, sharpe_ratio, sortino_ratio, std_dev_ann_pct, max_drawdown_pct, aum_crore, expense_ratio_pct, morningstar_rating, and risk_grade.

---

## Dataset: 08_investor_transactions.csv

**Purpose:** Investor-level transaction records.

Include definitions for investor_id, transaction_date, transaction_type, amount_inr, state, city, city_tier, age_group, gender, annual_income_lakh, payment_mode, and kyc_status.

---

## Dataset: 09_portfolio_holdings.csv

**Purpose:** Portfolio composition of mutual fund schemes.

Include definitions for stock_symbol, stock_name, sector, weight_pct, market_value_cr, current_price_inr, and portfolio_date.

---

## Dataset: 10_benchmark_indices.csv

**Purpose:** Benchmark index historical values.

| Column Name | Data Type | Business Definition  | Format / Units |
| ----------- | --------- | -------------------- | -------------- |
| date        | Date      | Observation date     | YYYY-MM-DD     |
| index_name  | String    | Benchmark index name | Text           |
| close_value | Float     | Closing index value  | Numeric        |
