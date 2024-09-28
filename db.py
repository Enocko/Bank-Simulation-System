import sqlite3

# Establish database connection
conn = sqlite3.connect('bank.db')
cursor = conn.cursor()

# Create the table if it doesn't exist
def setup_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            balance REAL DEFAULT 10000
        )
    ''')
    conn.commit()

setup_db()  # Ensures the table is created
