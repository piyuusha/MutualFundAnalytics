from sqlalchemy import create_engine
import pandas as pd
import numpy as np
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

df["daily_return"] = df.groupby("amfi_code")["nav"].pct_change()

rf = 0.065  # 6.5%

results = []

for code, group in df.groupby("amfi_code"):

    returns = group["daily_return"].dropna()

    if len(returns) == 0:
        continue

    mean_return = returns.mean() * 252

    downside = returns[returns < 0]

    if len(downside) == 0:
        sortino = np.nan
    else:
        downside_std = downside.std()

        if downside_std == 0:
            sortino = np.nan
        else:
            sortino = (mean_return - rf) / (downside_std * np.sqrt(252))

    results.append({
        "amfi_code": code,
        "sortino_ratio": round(sortino, 4)
    })

result_df = pd.DataFrame(results)

result_df = result_df.sort_values(
    by="sortino_ratio",
    ascending=False
)

os.makedirs("../reports", exist_ok=True)

result_df.to_csv(
    "../reports/sortino_ratio.csv",
    index=False
)

print(result_df.head(10))

print("Sortino Ratio report saved successfully")