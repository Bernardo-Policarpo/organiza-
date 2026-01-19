from get_conn import get_conn

conn = get_conn()
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                display_name TEXT,
                has_password BOOLEAN NOT NULL DEFAULT 0,
                password_hash TEXT,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP)""")

conn.commit()

conn.close()