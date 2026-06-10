from db_connection import get_data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load AUM data

query = """
SELECT *
FROM aum
"""

df = get_data(query)

# Convert date

df["date"] = pd.to_datetime(df["date"])

# Extract year

df["year"] = df["date"].dt.year

# Aggregate yearly AUM

yearly_aum = (
    df.groupby(["year", "fund_house"])["aum_lakh_crore"]
    .mean()
    .reset_index()
)

# Create chart

plt.figure(figsize=(14, 7))

sns.barplot(
    data=yearly_aum,
    x="year",
    y="aum_lakh_crore",
    hue="fund_house"
)

plt.title("AUM Growth by Fund House")
plt.xlabel("Year")
plt.ylabel("AUM (Lakh Crore)")
plt.xticks(rotation=0)

# Highlight SBI dominance

plt.axhline(
    y=12.5,
    color="red",
    linestyle="--",
    linewidth=2,
    label="SBI Peak AUM (12.5 Lakh Cr)"
)

plt.legend(
    bbox_to_anchor=(1.02, 1),
    loc="upper left"
)

plt.tight_layout()

# Create charts folder if missing

os.makedirs("../charts", exist_ok=True)

# Save PNG

plt.savefig("../charts/aum_growth_analysis.png")

plt.show()

print("AUM chart saved successfully")