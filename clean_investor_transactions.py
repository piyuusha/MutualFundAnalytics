import pandas as pd

df = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

print("Rows Before:", len(df))

# Convert transaction date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"]
)

# Standardize transaction types
df["transaction_type"] = (
    df["transaction_type"]
    .str.strip()
    .str.title()
)

# Keep valid transaction types only
valid_types = [
    "Sip",
    "Lumpsum",
    "Redemption"
]

df = df[
    df["transaction_type"]
    .isin(valid_types)
]

# Amount must be positive
df = df[
    df["amount_inr"] > 0
]

# Check KYC values
print("\nKYC Status Values:")
print(df["kyc_status"].unique())

# Remove duplicates
before = len(df)

df = df.drop_duplicates()

after = len(df)

print("\nDuplicates Removed:",
      before - after)

print("Rows After:",
      len(df))

# Save cleaned data
df.to_csv(
    "data/processed/investor_transactions_cleaned.csv",
    index=False
)

print("\nSaved Successfully")