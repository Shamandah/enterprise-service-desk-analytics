import sqlite3
import pandas as pd

# Connect to SQLite
conn = sqlite3.connect("database/tickets.db")

# Read SQL from a file
with open("sql/02_priority_distribution.sql", "r") as file:
    query = file.read()

# Execute the query
df = pd.read_sql_query(query, conn)

# Display results
print(df)

conn.close()