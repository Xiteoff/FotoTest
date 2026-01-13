import sqlite3
from datetime import datetime

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    first_seen TEXT
)
""")
conn.commit()


def save_user(user_id: int):
    cursor.execute("""
    INSERT OR IGNORE INTO users (user_id, first_seen)
    VALUES (?, ?)
    """, (user_id, datetime.now().isoformat()))
    conn.commit()


def get_users_count():
    cursor.execute("SELECT COUNT(*) FROM users")
    return cursor.fetchone()[0]
