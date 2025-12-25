# db.py
import sqlite3

DB_NAME = "english_map.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        lang TEXT DEFAULT 'en',
        level TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS vocab_lists (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        list_name TEXT,
        word TEXT,
        meaning TEXT
    )
    """)


    conn.commit()
    conn.close()
