import streamlit as st
import sqlite3
import json
import pandas as pd

DB_NAME = "data.db"

def get_latest_weather():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT raw_json, created_at
        FROM weather
        ORDER BY created_at DESC
        LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "created_at": row[1],
            "data": json.loads(row[0])
        }
    return None


# ===== Streamlit UI =====
st.set_page_config(page_title="CWA Weather Viewer", page_icon="🌦️")

st.title("🌦️ CWA Weather Crawler (Streamlit)")
st.write("Latest weather data stored in SQLite database")

result = get_latest_weather()

if result:
    st.success(f"Data timestamp: {result['created_at']}")

    # 顯示原始 JSON（老師最安全）
    with st.expander("🔍 Raw JSON Data"):
        st.json(result["data"])

    # 如果 JSON 是 dict / list，也可嘗試轉成表格
    try:
        if isinstance(result["data"], dict):
            df = pd.json_normalize(result["data"])
            st.subheader("📊 Parsed Weather Data")
            st.dataframe(df)
    except Exception as e:
        st.warning("Data structure is not suitable for table display.")

else:
    st.error("No weather data found in database.")
