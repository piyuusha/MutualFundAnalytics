from db_connection import get_data
import matplotlib.pyplot as plt
import os

query="""
SELECT fund_house,COUNT(*) total
FROM fund_master
GROUP BY fund_house
ORDER BY total DESC
"""

df=get_data(query)

plt.figure(figsize=(10,6))

plt.barh(df["fund_house"],df["total"])

plt.title("Top Fund Houses")

plt.tight_layout()

os.makedirs("../charts",exist_ok=True)

plt.savefig("../charts/top_fund_houses.png")

plt.show()
