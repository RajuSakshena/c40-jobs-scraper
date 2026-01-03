import streamlit as st
import pandas as pd

st.set_page_config(page_title="C40 Jobs Dashboard", layout="wide")
st.title("C40 – Careers Scraper Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv("output/c40_jobs.csv")

df = load_data()

st.metric("Total Jobs", len(df))
st.dataframe(df, use_container_width=True)

st.download_button(
    "Download CSV",
    df.to_csv(index=False),
    file_name="c40_jobs.csv",
    mime="text/csv"
)
