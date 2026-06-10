import pandas as pd
import matplotlib.pyplot as plt
import os

df=pd.read_csv("../../data/raw/10_benchmark_indices.csv")

plt.figure(figsize=(12,6))

for name in df["index_name"].unique():
    temp=df[df["index_name"]==name]
    plt.plot(temp["date"],temp["close_value"],label=name)

plt.xticks(rotation=45)

plt.legend()

plt.title("Benchmark Comparison")

plt.tight_layout()

os.makedirs("../charts",exist_ok=True)

plt.savefig("../charts/benchmark_comparison.png")

plt.show()
