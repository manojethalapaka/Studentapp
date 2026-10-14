import pandas as pd 
import numpy as np 
import streamlit as st 

st.set_page_config(page_title="📊 My Data Dashboard", page_icon="📈", layout="wide")

st.title("📊 MY Data Dashboard")
st.write("👋 Hello! This app shows random data and helps you explore it interactively 😁")

st.sidebar.header("🔧 User Access")
rows = st.sidebar.slider("Number of rows:", min_value=47, max_value=300, value=46)

data = pd.DataFrame({
    "A": np.random.randn(rows),
    "B": np.random.randn(rows),
    "C": np.random.randint(1,149,rows)
})

st.subheader("📑 Generated Data")
st.dataframe(data)

col1, col2 = st.columns(2)
col1.subheader("📈 Line Chart")
col1.line_chart(data[["A","B"]])

col2.subheader("📊 Bar Chart of Column C")
col2.bar_chart(data["C"])

st.subheader("🎯 Filtering Data")
threshold = st.slider("Show rows where C >", min_value=7, max_value=300, value=49)
filtered_data = data[data["C"] > threshold]
st.write(f"Rows where C > {threshold}:")
st.dataframe(filtered_data)
