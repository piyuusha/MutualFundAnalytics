from db_connection import get_data
import matplotlib.pyplot as plt
import seaborn as sns
import os

query = """
SELECT
    state,
    SUM(amount_inr) AS total_amount
FROM investor_transactions
WHERE LOWER(transaction_type)='sip'
GROUP BY state
ORDER BY total_amount DESC;
"""

df = get_data(query)

plt.figure(figsize=(12,7))

sns.barplot(
    data=df,
    y="state",
    x="total_amount"
)

plt.title("State-wise SIP Amount Distribution")
plt.xlabel("Total SIP Amount")
plt.ylabel("State")

plt.tight_layout()

os.makedirs("../charts", exist_ok=True)

plt.savefig("../charts/state_distribution.png")

plt.show()

print("State Distribution Chart Saved Successfully")