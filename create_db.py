import sqlite3

# Connect to SQLite database (creates file if not exists)
conn = sqlite3.connect("sales_data.db")
cursor = conn.cursor()

# Create the 'sales' table
cursor.execute("""
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT,
    quantity INTEGER,
    price REAL
)
""")

# Insert sample data
sales_data = [
    ("Apple", 10, 2.5),
    ("Banana", 20, 1.0),
    ("Orange", 15, 1.5),
    ("Apple", 5, 2.5),
    ("Banana", 10, 1.0)
]

cursor.executemany("INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)", sales_data)

# Commit and close
conn.commit()
conn.close()

print("✅ sales_data.db created with sample data!")
