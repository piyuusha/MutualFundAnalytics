import pandas as pd
import matplotlib.pyplot as plt
import os

# Read CSV
df = pd.read_csv("../../data/raw/06_industry_folio_count.csv")

# Plot Total Folios

plt.figure(figsize=(12,6))

plt.plot(
    df["month"],
    df["total_folios_crore"],
    marker="o",
    linewidth=2
)

plt.title("Industry Folio Count Growth")
plt.xlabel("Month")
plt.ylabel("Total Folios (Crore)")

plt.xticks(rotation=45)
plt.grid(True)

plt.tight_layout()

os.makedirs("../charts", exist_ok=True)

plt.savefig("../charts/folio_growth.png")

plt.show()

print("Folio Growth Chart Saved Successfully")