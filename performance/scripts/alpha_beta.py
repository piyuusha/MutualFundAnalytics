from sqlalchemy import create_engine
import pandas as pd
import numpy as np
from scipy.stats import linregress
import os

engine = create_engine("sqlite:///../../bluestock_mf.db")

query = """
SELECT
    amfi_code,
    date,
    nav
FROM nav_history
ORDER BY amfi_code,date
"""

df = pd.read_sql(query, engine)

df["date"] = pd.to_datetime(df["date"])

# Calculate daily returns
df["daily_return"] = df.groupby("amfi_code")["nav"].pct_change()

# Create benchmark as average return across all funds
benchmark = (
    df.groupby("date")["daily_return"]
      .mean()
      .reset_index()
      .rename(columns={"daily_return":"benchmark_return"})
)

results = []

for code, group in df.groupby("amfi_code"):

    temp = group.merge(
        benchmark,
        on="date",
        how="inner"
    )

    temp = temp.dropna()

    if len(temp) < 2:
        continue

    slope, intercept, r, p, std = linregress(
        temp["benchmark_return"],
        temp["daily_return"]
    )

    alpha = intercept * 252
    beta = slope

    results.append({
        "amfi_code": code,
        "alpha": round(alpha,4),
        "beta": round(beta,4)
    })

result_df = pd.DataFrame(results)

result_df = result_df.sort_values(
    by="alpha",
    ascending=False
)

os.makedirs("../reports", exist_ok=True)

result_df.to_csv(
    "../reports/alpha_beta.csv",
    index=False
)

print(result_df.head(10))

print("Alpha Beta report saved successfully")