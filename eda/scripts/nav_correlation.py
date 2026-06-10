from db_connection import get_data
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

query="""
SELECT *
FROM nav_history
"""

df=get_data(query)

df["date"]=pd.to_datetime(df["date"])

pivot=df.pivot(
    index="date",
    columns="amfi_code",
    values="nav"
)

returns=pivot.pct_change()

corr=returns.corr()

plt.figure(figsize=(12,10))

sns.heatmap(
    corr,
    cmap="coolwarm",
    annot=False
)

plt.title("NAV Return Correlation Matrix")

plt.tight_layout()

os.makedirs("../charts",exist_ok=True)

plt.savefig("../charts/nav_correlation.png")

plt.show()