from db_connection import get_data

print(
    get_data("""
    SELECT name
    FROM sqlite_master
    WHERE type='table';
    """)
)