from db_connection import get_data
import matplotlib.pyplot as plt
import os

query="""
SELECT payment_mode,COUNT(*) total
FROM investor_transactions
GROUP BY payment_mode
"""

df=get_data(query)

plt.figure(figsize=(8,6))

plt.bar(df["payment_mode"],df["total"])

plt.xticks(rotation=30)

plt.title("Payment Mode Distribution")

plt.tight_layout()

os.makedirs("../charts",exist_ok=True)

plt.savefig("../charts/payment_mode_distribution.png")

plt.show()