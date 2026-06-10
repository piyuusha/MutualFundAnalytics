import pandas as pd
import os

cagr = pd.read_csv("../reports/cagr_analysis.csv")
sharpe = pd.read_csv("../reports/sharpe_ratio.csv")
alpha = pd.read_csv("../reports/alpha_beta.csv")
drawdown = pd.read_csv("../reports/maximum_drawdown.csv")

df = cagr.merge(
    sharpe,
    on="amfi_code"
)

df = df.merge(
    alpha,
    on="amfi_code"
)

df = df.merge(
    drawdown,
    on="amfi_code"
)

# Rankings

df["cagr_rank"] = df["cagr_percent"].rank(ascending=False)

df["sharpe_rank"] = df["sharpe_ratio"].rank(ascending=False)

df["alpha_rank"] = df["alpha"].rank(ascending=False)

df["drawdown_rank"] = df["max_drawdown_percent"].rank(ascending=False)

# Composite Score

df["fund_score"] = (
    0.30*df["cagr_rank"] +
    0.25*df["sharpe_rank"] +
    0.20*df["alpha_rank"] +
    0.25*df["drawdown_rank"]
)

# Convert to 0-100 scale

max_score = df["fund_score"].max()

df["fund_score"] = (
    (max_score-df["fund_score"])/max_score
)*100

df = df.sort_values(
    by="fund_score",
    ascending=False
)

os.makedirs("../reports",exist_ok=True)

df.to_csv(
    "../reports/fund_scorecard.csv",
    index=False
)

print(df[[
    "amfi_code",
    "fund_score"
]].head(10))

print("Fund Scorecard saved successfully")
