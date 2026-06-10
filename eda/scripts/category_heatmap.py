from db_connection import get_data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

query = """
SELECT
    it.transaction_date,
    it.amount_inr,
    fm.category
FROM investor_transactions it
JOIN fund_master fm
ON it.amfi_code = fm.amfi_code
WHERE LOWER(it.transaction_type) = 'sip'
"""

df = get_data(query)

df["transaction_date"] = pd.to_datetime(df["transaction_date"])

df["month"] = df["transaction_date"].dt.strftime("%Y-%m")

heatmap_data = (
    df.groupby(["category", "month"])["amount_inr"]
    .sum()
    .reset_index()
)

pivot_table = heatmap_data.pivot(
    index="category",
    columns="month",
    values="amount_inr"
)

plt.figure(figsize=(18,8))

sns.heatmap(
    pivot_table,
    cmap="YlGnBu"
)

plt.title("Category-wise SIP Inflow Heatmap")

plt.tight_layout()

os.makedirs("../charts", exist_ok=True)

plt.savefig("../charts/category_heatmap.png")

plt.show()

print("Heatmap saved successfully")