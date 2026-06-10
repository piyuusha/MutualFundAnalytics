from db_connection import get_data

query = """
SELECT *
FROM investor_transactions
LIMIT 10
"""

df = get_data(query)

print(df)