import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the existing SQLite database
conn = sqlite3.connect("sales_data.db")

# SQL query to summarize total quantity and revenue per product
query = """
SELECT 
    product, 
    SUM(quantity) AS total_qty, 
    SUM(quantity * price) AS revenue 
FROM sales 
GROUP BY product
"""

# Load query result into a pandas DataFrame
df = pd.read_sql_query(query, conn)

# Print the summary table
print("📊 Sales Summary:\n")
print(df)

# Plot a bar chart for revenue by product
df.plot(kind='bar', x='product', y='revenue', legend=False, title="Revenue by Product")
plt.ylabel("Revenue ($)")
plt.tight_layout()

# Save the chart (optional)
plt.savefig("sales_chart.png")

# Show the chart
plt.show()

# Close the database connection
conn.close()
