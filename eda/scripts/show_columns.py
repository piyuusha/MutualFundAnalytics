from db_connection import get_data

tables = [
    "fund_master",
    "nav_history",
    "investor_transactions",
    "scheme_performance",
    "aum"
]

for table in tables:
    print(f"\n{'='*50}")
    print(table.upper())
    print('='*50)

    query = f"""
    PRAGMA table_info({table});
    """

    print(get_data(query))