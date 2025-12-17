import sqlite3

def store_to_db(data):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        raw_json TEXT,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    """)
    cursor.execute("INSERT INTO weather(raw_json) VALUES(?)", (json.dumps(data),))
    conn.commit()
    conn.close()