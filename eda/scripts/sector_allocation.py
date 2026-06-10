import pandas as pd
import matplotlib.pyplot as plt
import os

df=pd.read_csv("../../data/raw/09_portfolio_holdings.csv")

sector=df.groupby("sector")["weight_pct"].sum()

plt.figure(figsize=(8,8))

plt.pie(
    sector,
    labels=sector.index,
    autopct="%1.1f%%",
    startangle=90,
    wedgeprops=dict(width=0.4)
)

plt.title("Sector Allocation")

os.makedirs("../charts",exist_ok=True)

plt.savefig("../charts/sector_allocation.png")

plt.show()