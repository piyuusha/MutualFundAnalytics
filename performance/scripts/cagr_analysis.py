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
ORDER BY amfi_code,date
"""

df = pd.read_sql(query, engine)

df["date"] = pd.to_datetime(df["date"])

print("Minimum Date:", df["date"].min())
print("Maximum Date:", df["date"].max())

result = []

for code, group in df.groupby("amfi_code"):

    group = group.sort_values("date")

    start_nav = group.iloc[0]["nav"]
    end_nav = group.iloc[-1]["nav"]

    years = (group.iloc[-1]["date"] - group.iloc[0]["date"]).days / 365.25

    if years <= 0:
        continue

    cagr = ((end_nav / start_nav) ** (1 / years) - 1) * 100

    result.append({
        "amfi_code": code,
        "years_available": round(years,2),
        "cagr_percent": round(cagr,2)
    })

cagr_df = pd.DataFrame(result)

cagr_df = cagr_df.sort_values(
    by="cagr_percent",
    ascending=False
)

os.makedirs("../reports",exist_ok=True)

cagr_df.to_csv(
    "../reports/cagr_analysis.csv",
    index=False
)

print(cagr_df.head(10))

print("CAGR report saved successfully")