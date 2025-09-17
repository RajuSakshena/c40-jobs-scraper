import streamlit as st
import pandas as pd

st.set_page_config(page_title="C40 Jobs Scraper", layout="wide")

st.title("🌍 C40 Jobs Scraper Results")

# Load Excel from repo
EXCEL_PATH = "output/c40_jobs.xlsx"

try:
    df = pd.read_excel(EXCEL_PATH)

    st.success(f"Loaded {len(df)} jobs from {EXCEL_PATH}")

    # Show data in an interactive table
    st.dataframe(df, use_container_width=True)

    # Download button
    st.download_button(
        label="📥 Download Excel",
        data=open(EXCEL_PATH, "rb").read(),
        file_name="c40_jobs.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

except FileNotFoundError:
    st.error("❌ No Excel file found. Please run the scraper workflow first.")
