import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print("Rows Before:", len(df))

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort properly
df = df.sort_values(
    by=["amfi_code", "date"]
)

# Remove duplicates
before = len(df)

df = df.drop_duplicates()

after = len(df)

# Forward fill missing NAV
df["nav"] = (
    df.groupby("amfi_code")["nav"]
    .ffill()
)

# Keep only valid NAV
df = df[df["nav"] > 0]

print("Duplicates Removed:", before - after)

print("Rows After:", len(df))

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_cleaned.csv",
    index=False
)

print("Saved Successfully")