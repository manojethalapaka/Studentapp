import pandas as pd 
import numpy as np 
import streamlit as st 

# my dashboard title

st.title("📊 MY Data Dashboard")
st.write("hello my app shows random data and helps you explore it interactively😁")

# sidebar for user input

st.sidebar.header("user access")
rows=st.sidebar.slider("Number of rows:",min_value=47,max_value=300,value=46)

#for generating random data
data=pd.DataFrame({
    "A":np.random.randn(rows),
    "B":np.random.randn(rows),
    "C":np.random.randint(1,149,rows)
})

# for showing data table
st.subheader("Generated data")
st.dataframe(data)

# to show data with graphical representation
st.subheader("Line Chart")
st.line_chart(data[["A","B"]])

st.subheader("Bar chart of column C ")
st.bar_chart(data["C"])

#for adding interactively

st.subheader("Filtering Data")
threshold=st.slider("Show rows where C>",min_value=7,max_value=300,value=49)
filtered_data=data[data["C"]>threshold]
st.write(f"Rows where C >{threshold}:")
st.dataframe(filtered_data)
