import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url, timeout=30)

print("Status Code:", response.status_code)

data = response.json()

nav_df = pd.DataFrame(data["data"])

nav_df.to_csv(
    "data/raw/hdfc_top100_direct_nav.csv",
    index=False
)

print("CSV Saved Successfully")