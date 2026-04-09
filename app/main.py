import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from dotenv import load_dotenv
load_dotenv()  # Must come before importing supabase client
from src.db.supabase_client import supabase

st.title("💼 Salary Prediction Dashboard")

# -----------------------------
# Fetch all predictions from Supabase
# -----------------------------
response = supabase.table("predictions").select(
    "job_title, experience_level, employee_residence, company_size, remote_ratio, predicted_salary, analysis, chart_path, created_at"
).execute()

data = response.data

if not data:
    st.warning("No data available yet.")
    st.stop()

# Convert to DataFrame
df = pd.DataFrame(data)

# -----------------------------
# Show full predictions table WITHOUT analysis
# -----------------------------
st.subheader("📋 Predictions Data")
df_table = df.drop(columns=["analysis", "chart_path", "created_at"])  # remove columns you don't want in the table
st.dataframe(df_table)

# -----------------------------
# Filter by job title
# -----------------------------
st.subheader("🔎 Filter Data")
job_filter = st.selectbox("Select Job Title", df['job_title'].unique())
filtered_df = df[df['job_title'] == job_filter]

st.subheader("📊 Filtered Results")
filtered_table = filtered_df.drop(columns=["analysis", "chart_path", "created_at"])
st.dataframe(filtered_table)

# -----------------------------
# Show LLM analysis separately
# -----------------------------
st.subheader("🧠 LLM Analysis")
if not filtered_df.empty:
    latest_row = filtered_df.sort_values("created_at", ascending=False).iloc[0]
    st.write(latest_row['analysis'])

# -----------------------------
# Display charts
# -----------------------------
st.subheader("📉 Charts")
for _, row in filtered_df.iterrows():
    chart_path = row.get('chart_path')
    if chart_path and os.path.exists(chart_path):
        st.image(chart_path, caption=row['job_title'])
    else:
        st.warning(f"Chart not found: {chart_path}")