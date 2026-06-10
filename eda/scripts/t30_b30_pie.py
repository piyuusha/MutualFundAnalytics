from db_connection import get_data
import matplotlib.pyplot as plt
import os

query = """
SELECT
    city_tier,
    COUNT(*) AS total
FROM investor_transactions
GROUP BY city_tier;
"""

df = get_data(query)

plt.figure(figsize=(7,7))

plt.pie(
    df["total"],
    labels=df["city_tier"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("T30 vs B30 City Tier Distribution")

os.makedirs("../charts", exist_ok=True)

plt.savefig("../charts/t30_b30_distribution.png")

plt.show()

print("T30 vs B30 Pie Chart Saved Successfully")