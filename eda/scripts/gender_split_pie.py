from db_connection import get_data
import matplotlib.pyplot as plt
import os

query = """
SELECT
    gender,
    COUNT(*) AS total
FROM investor_transactions
GROUP BY gender;
"""

df = get_data(query)

plt.figure(figsize=(7,7))

plt.pie(
    df["total"],
    labels=df["gender"],
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Gender Distribution")

os.makedirs("../charts", exist_ok=True)

plt.savefig("../charts/gender_distribution.png")

plt.show()

print("Gender Pie Chart Saved Successfully")