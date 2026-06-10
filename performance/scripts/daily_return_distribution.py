import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("../reports/daily_returns.csv")

df = df.dropna(subset=["daily_return"])

plt.figure(figsize=(10,6))

sns.histplot(
    df["daily_return"],
    bins=50,
    kde=True
)

plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")

plt.grid(True)

os.makedirs("../charts", exist_ok=True)

plt.savefig("../charts/daily_return_distribution.png")

plt.show()

print(df["daily_return"].describe())

print("Chart saved successfully")