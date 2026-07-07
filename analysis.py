import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Enterprise IT Helpdesk Analytics Dashboard.csv")

print(df.head())
print(df.columns)
print(df.info())
print(df["TicketType"].value_counts())
print(df["Priority"].value_counts())
print(df["Severity"].value_counts())
print(df["FiledAgainst"].value_counts().head(10))
print("\nPriority vs Severity")
print(pd.crosstab(df["Severity"], df["Priority"]))
print("\nTicket Type vs Priority")
print(pd.crosstab(df["TicketType"], df["Priority"]))
print("\nFiled Against vs Priority")
print(pd.crosstab(df["FiledAgainst"], df["Priority"]))
priority_counts = df["Priority"].value_counts()

plt.figure(figsize=(8,5))
priority_counts.plot(kind="bar")

plt.title("Ticket Priority Distribution")
plt.xlabel("Priority")
plt.ylabel("Number of Tickets")

plt.tight_layout()
plt.savefig("reports/charts/priority_distribution.png")

print("Chart saved successfully!")
severity_counts = df["Severity"].value_counts()

plt.figure(figsize=(8,5))
severity_counts.plot(kind="bar")
plt.title("Severity Distribution")
plt.tight_layout()
plt.savefig("reports/charts/severity_distribution.png")
ticket_counts = df["TicketType"].value_counts()

plt.figure(figsize=(8,5))
ticket_counts.plot(kind="bar")
plt.title("Ticket Type Distribution")
plt.tight_layout()
plt.savefig("reports/charts/tickettype_distribution.png")
filed_counts = df["FiledAgainst"].value_counts()

plt.figure(figsize=(8,5))
filed_counts.plot(kind="bar")
plt.title("Filed Against Distribution")
plt.tight_layout()
plt.savefig("reports/charts/filedagainst_distribution.png")