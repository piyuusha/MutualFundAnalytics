from db_connection import get_data
import matplotlib.pyplot as plt
import os

query="""
SELECT kyc_status,COUNT(*) total
FROM investor_transactions
GROUP BY kyc_status
"""

df=get_data(query)

plt.figure(figsize=(6,6))

plt.pie(
    df["total"],
    labels=df["kyc_status"],
    autopct="%1.1f%%"
)

plt.title("KYC Status Distribution")

os.makedirs("../charts",exist_ok=True)

plt.savefig("../charts/kyc_status_distribution.png")

plt.show()