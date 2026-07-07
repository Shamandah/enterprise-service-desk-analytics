import pandas as pd
import sqlite3

# Load the dataset
df = pd.read_csv("data/Enterprise IT Helpdesk Analytics Dashboard.csv") # Replace with your actual filename

# Connect (or create) SQLite database
conn = sqlite3.connect("database/tickets.db")

# Load data into SQLite
df.to_sql(
    "tickets",
    conn,
    if_exists="replace",
    index=False
)

print("Data successfully loaded into SQLite!")

conn.close()