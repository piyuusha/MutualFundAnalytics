from db_connection import get_data
import matplotlib.pyplot as plt
import os

query="""
SELECT category,COUNT(*) total
FROM fund_master
GROUP BY category
"""

df=get_data(query)

plt.figure(figsize=(8,6))

plt.bar(df["category"],df["total"])

plt.title("Fund Category Distribution")
plt.xlabel("Category")
plt.ylabel("Count")

plt.tight_layout()

os.makedirs("../charts",exist_ok=True)

plt.savefig("../charts/fund_category_distribution.png")

plt.show()