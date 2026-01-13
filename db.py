import sqlite3
from datetime import datetime

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    main_style TEXT,
    extra_style TEXT,
    updated_at TEXT
)
""")
conn.commit()


def save_result(user_id: int, main_style: str, extra_style: str):
    cursor.execute("""
    INSERT INTO users (user_id, main_style, extra_style, updated_at)
    VALUES (?, ?, ?, ?)
    ON CONFLICT(user_id) DO UPDATE SET
        main_style = excluded.main_style,
        extra_style = excluded.extra_style,
        updated_at = excluded.updated_at
    """, (user_id, main_style, extra_style, datetime.now().isoformat()))
    conn.commit()
