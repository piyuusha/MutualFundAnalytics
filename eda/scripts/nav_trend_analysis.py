from db_connection import get_data
import pandas as pd
import plotly.express as px
import os

# Load NAV history

query = """
SELECT *
FROM nav_history
"""

df = get_data(query)

# Convert date column

df["date"] = pd.to_datetime(df["date"])

# Check date range and scheme count

print("Minimum Date:", df["date"].min())
print("Maximum Date:", df["date"].max())
print("Unique Schemes:", df["amfi_code"].nunique())

# Create chart

fig = px.line(
    df,
    x="date",
    y="nav",
    color="amfi_code",
    title="NAV Trend Analysis (2022-2026)"
)

# Bull Run Highlight

fig.add_vrect(
    x0="2023-01-01",
    x1="2023-12-31",
    annotation_text="2023 Bull Run",
    fillcolor="green",
    opacity=0.1,
    line_width=0
)

# Correction Highlight

fig.add_vrect(
    x0="2024-01-01",
    x1="2024-06-30",
    annotation_text="2024 Correction",
    fillcolor="red",
    opacity=0.1,
    line_width=0
)

# Save html

os.makedirs("../charts", exist_ok=True)

fig.write_html("../charts/nav_trend_analysis.html")
fig.write_image("../charts/nav_trend_analysis.png")

print("Chart saved successfully")