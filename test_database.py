import sqlite3

conn = sqlite3.connect("database/tickets.db")

cursor = conn.cursor()

# Count the records
cursor.execute("SELECT COUNT(*) FROM tickets")
print("Total records:", cursor.fetchone()[0])

conn.close()