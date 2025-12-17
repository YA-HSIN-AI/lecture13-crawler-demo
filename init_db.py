import sqlite3
import json
from crawler import fetch_weather

DB_NAME = "data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        raw_json TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()


def store_weather(data):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO weather (raw_json) VALUES (?)",
        (json.dumps(data, ensure_ascii=False),)
    )

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    data = fetch_weather()
    if data:
        store_weather(data)
        print("Weather data inserted into SQLite.")
