from db_connection import get_data
import matplotlib.pyplot as plt
import os

query = """
SELECT
    age_group,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY age_group
ORDER BY age_group;
"""

df = get_data(query)

plt.figure(figsize=(8,8))

plt.pie(
    df["investors"],
    labels=df["age_group"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Investor Age Group Distribution")

os.makedirs("../charts", exist_ok=True)

plt.savefig("../charts/age_group_distribution.png")

plt.show()

print("Age Group Pie Chart Saved Successfully")