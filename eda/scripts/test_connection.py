from db_connection import get_data

query = """
SELECT name
FROM sqlite_master
WHERE type='table';
"""

print(get_data(query))