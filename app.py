import os
import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="C40 Jobs Dashboard",
    layout="wide"
)

st.title("🌍 C40 – Careers Dashboard")

# --------------------------------------------------
# PATH HANDLING (STREAMLIT CLOUD SAFE)
# --------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(
    BASE_DIR,
    "scraper",
    "output",
    "c40_jobs.xlsx"
)

@st.cache_data
def load_data():
    return pd.read_excel(DATA_PATH)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------
try:
    df = load_data()
except FileNotFoundError:
    st.error("Data file not found. Please wait for GitHub Action to generate the Excel file.")
    st.stop()

# --------------------------------------------------
# UI
# --------------------------------------------------
st.metric("Total Jobs", len(df))

st.dataframe(df, use_container_width=True)

st.download_button(
    label="Download Excel",
    data=open(DATA_PATH, "rb"),
    file_name="c40_jobs.xlsx",
    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
)
