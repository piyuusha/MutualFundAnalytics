from db_connection import get_data
import pandas as pd
import plotly.express as px
import os

query = """
SELECT *
FROM investor_transactions
WHERE LOWER(transaction_type) = 'sip'
"""

df = get_data(query)

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df["month"] = (
    df["transaction_date"]
    .dt.to_period("M")
    .astype(str)
)

monthly_sip = (
    df.groupby("month")["amount_inr"]
    .sum()
    .reset_index()
)

max_row = monthly_sip.loc[
    monthly_sip["amount_inr"].idxmax()
]

print("\nHighest SIP Month")
print(max_row)

fig = px.line(
    monthly_sip,
    x="month",
    y="amount_inr",
    title="Monthly SIP Inflow Trend"
)

fig.add_annotation(
    x=max_row["month"],
    y=max_row["amount_inr"],
    text="Peak SIP",
    showarrow=True
)

os.makedirs("../charts", exist_ok=True)

fig.write_html("../charts/sip_trend_analysis.html")
fig.write_image("../charts/sip_trend_analysis.png")

print("SIP chart saved successfully")