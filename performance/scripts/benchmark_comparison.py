import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../../data/raw/10_benchmark_indices.csv")

df["date"] = pd.to_datetime(df["date"])

plt.figure(figsize=(12,6))

for idx in df["index_name"].unique():
    temp = df[df["index_name"] == idx]
    plt.plot(
        temp["date"],
        temp["close_value"],
        label=idx
    )

plt.title("Benchmark Comparison")
plt.xlabel("Date")
plt.ylabel("Close Value")

plt.legend()

plt.grid(True)

plt.tight_layout()

os.makedirs("../charts", exist_ok=True)

plt.savefig("../charts/benchmark_comparison.png")

plt.show()

print("Benchmark Comparison Chart Saved Successfully")