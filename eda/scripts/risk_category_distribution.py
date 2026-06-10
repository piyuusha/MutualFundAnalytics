from db_connection import get_data
import matplotlib.pyplot as plt
import os

query="""
SELECT risk_category,COUNT(*) total
FROM fund_master
GROUP BY risk_category
"""

df=get_data(query)

plt.figure(figsize=(8,6))

plt.bar(df["risk_category"],df["total"])

plt.xticks(rotation=30)

plt.title("Risk Category Distribution")

plt.tight_layout()

os.makedirs("../charts",exist_ok=True)

plt.savefig("../charts/risk_category_distribution.png")

plt.show()