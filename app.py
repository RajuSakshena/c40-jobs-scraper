import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="C40 Jobs Scraper", layout="wide")

st.title("🌍 C40 Jobs Scraper")
st.write("This app shows the latest scraped job listings from C40.")

# Path to Excel file
excel_path = "output/c40_jobs.xlsx"

if os.path.exists(excel_path):
    # Load Excel
    df = pd.read_excel(excel_path)

    # Show dataframe with search
    st.subheader("Job Listings")
    st.dataframe(df, use_container_width=True)

    # Allow download as Excel
    st.download_button(
        label="📥 Download Excel",
        data=open(excel_path, "rb").read(),
        file_name="c40_jobs.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

else:
    st.warning("⚠️ No job data found yet. Please wait for the scraper workflow to run.")
