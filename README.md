# lecture13-crawler-demo
Lecture 13 demo: Python web crawler for CWA Open Data (weather API), using SQLite and Streamlit
## 📌 Overview
This project demonstrates a simple data pipeline:

1. Fetch weather data from CWA Open Data API  
2. Store raw JSON data into a local SQLite database  
3. Display the latest weather data using Streamlit

The implementation focuses on **learning web crawling and data persistence concepts**.

---

## 📁 Project Structure

---

## 🧩 File Description

### `crawler.py`
- Requests weather data from CWA Open Data API
- Saves the response in JSON format
- Includes basic error handling

### `init_db.py`
- Creates SQLite database (`data.db`)
- Stores raw JSON data for flexibility

### `app.py`
- Reads weather data from SQLite
- Displays the latest record using Streamlit
- Shows raw JSON and parsed table (if applicable)

---

## ▶️ How to Run

```bash
pip install streamlit requests pandas
python crawler.py
python init_db.py
streamlit run app.py
