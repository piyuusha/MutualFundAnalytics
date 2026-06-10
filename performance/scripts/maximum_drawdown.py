from sqlalchemy import create_engine
import pandas as pd
import os

engine = create_engine("sqlite:///../../bluestock_mf.db")

query = """
SELECT
    amfi_code,
    date,
    nav
FROM nav_history
ORDER BY amfi_code, date
"""

df = pd.read_sql(query, engine)

df["date"] = pd.to_datetime(df["date"])

results = []

for code, group in df.groupby("amfi_code"):

    group = group.sort_values("date").copy()

    group["running_max"] = group["nav"].cummax()

    group["drawdown"] = (
        group["nav"] / group["running_max"] - 1
    )

    worst = group.loc[group["drawdown"].idxmin()]

    results.append({
        "amfi_code": code,
        "max_drawdown_percent": round(worst["drawdown"] * 100, 2),
        "worst_date": worst["date"].date()
    })

result_df = pd.DataFrame(results)

result_df = result_df.sort_values(
    by="max_drawdown_percent"
)

os.makedirs("../reports", exist_ok=True)

result_df.to_csv(
    "../reports/maximum_drawdown.csv",
    index=False
)

print(result_df.head(10))

print("Maximum Drawdown report saved successfully")