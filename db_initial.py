import sqlite3

def init_db():
    conn = sqlite3.connect("userdata.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            email TEXT PRIMARY KEY,
            name TEXT,
            phone TEXT,
            city TEXT
        )
    """)
    conn.commit()
    return conn