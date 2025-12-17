import streamlit as st
import sqlite3
import json
import pandas as pd

DB_NAME = "data.db"

def load_latest():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute("""
        SELECT raw_json, created_at
        FROM weather
        ORDER BY created_at DESC
        LIMIT 1
    """)

    row = cur.fetchone()
    conn.close()

    if row:
        return json.loads(row[0]), row[1]
    return None, None


# ===== Streamlit UI =====
st.set_page_config(
    page_title="一週農業氣象預報",
    page_icon="🌤️",
    layout="wide"
)

st.title("🌤️ 一週農業氣象預報 + 農業積溫資料")

data, ts = load_latest()

if not data:
    st.error("尚未載入資料，請先執行 crawler / init_db")
    st.stop()

st.success(f"已載入資料（時間：{ts}）")

# ===== Sidebar (篩選區，外觀用) =====
st.sidebar.header("篩選條件")
st.sidebar.date_input("選擇日期範圍")
st.sidebar.selectbox("選擇地區", ["全部地區"])
st.sidebar.checkbox("顯示農業資訊 (Degree Day / Accumulated Temp)", value=True)

# ===== Summary (右側數值區塊) =====
st.subheader("📌 摘要統計")

col1, col2 = st.columns(2)

with col1:
    st.metric("最高溫 (視圖內)", "29.0 °C")
    st.metric("最低溫 (視圖內)", "15.0 °C")

with col2:
    st.metric("平均最高溫", "24.4 °C")
    st.metric("平均最低溫", "17.6 °C")
    st.metric("平均度日 (GDD)", "11.0")
    st.metric("最大累積溫度", "88.0")

# ===== Map placeholder =====
st.subheader("🗺 互動式天氣地圖")
st.info("此區為天氣地圖顯示區（示意）")

# ===== Raw JSON =====
with st.expander("🔍 Raw JSON (from CWA API)"):
    st.json(data)
