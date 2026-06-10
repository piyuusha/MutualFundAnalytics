from db_connection import get_data
import seaborn as sns
import matplotlib.pyplot as plt
import os

query = """
SELECT
    age_group,
    amount_inr
FROM investor_transactions
WHERE LOWER(transaction_type)='sip';
"""

df = get_data(query)

plt.figure(figsize=(10,6))

sns.boxplot(
    data=df,
    x="age_group",
    y="amount_inr"
)

plt.title("SIP Amount by Age Group")

plt.tight_layout()

os.makedirs("../charts", exist_ok=True)

plt.savefig("../charts/sip_boxplot_age.png")

plt.show()

print("Box Plot Saved Successfully")