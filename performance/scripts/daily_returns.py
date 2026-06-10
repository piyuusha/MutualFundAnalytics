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
ORDER BY amfi_code,date
"""

df = pd.read_sql(query, engine)

df["date"] = pd.to_datetime(df["date"])

print("Minimum Date:", df["date"].min())
print("Maximum Date:", df["date"].max())

df["daily_return"] = (
    df.groupby("amfi_code")["nav"]
      .pct_change()
)

print(df.head(10))

os.makedirs("../reports", exist_ok=True)

df.to_csv(
    "../reports/daily_returns.csv",
    index=False
)

print("Daily returns file saved successfully")