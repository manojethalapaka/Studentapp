import streamlit as st
import pandas as pd 
import numpy as np

# Page configuration
st.set_page_config(page_title="🎓 Student Management System", page_icon="📚", layout="wide")

# Custom CSS styling
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        h1 {
            color: #2E86C1;
            text-align: center;
            font-family: 'Arial Black', sans-serif;
        }
        h2, h3 {
            color: #1F618D;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #2E86C1;
            color: white;
            border-radius: 8px;
            font-size: 16px;
            padding: 8px 20px;
        }
        .stButton>button:hover {
            background-color: #1B4F72;
            color: #f9f9f9;
        }
        .stDataFrame {
            border: 2px solid #2E86C1;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("🎓 Student Details Management App")

# Load data
data = pd.read_csv(r"C:\\Users\\Manoj kumar\\OneDrive\\Desktop\\manoj's python\\student_data.csv")
df = pd.DataFrame(data)

# Save changes
def save_changes():
    df.to_csv(r"C:\\Users\\Manoj kumar\\OneDrive\\Desktop\\manoj's python\\student_data.csv", index=False)
    st.success("✅ Changes saved to CSV File")

# Sidebar navigation
menu = st.sidebar.selectbox(
    "📌 Select Action",
    ["Home", "View Students", "Add Student", "Delete Student", "Update Student"]
)

# Home Page
if menu == "Home":
    st.subheader("🏠 Welcome to Student Management System")
    st.info("Use the sidebar to navigate between different actions like viewing, adding, deleting, or updating student records.")

# View Students
elif menu == "View Students":
    st.subheader("📋 View Students Details")
    st.dataframe(df, use_container_width=True)

# Add Student
elif menu == "Add Student":
    st.subheader("➕ Add New Student")
    with st.form("add_student_form"):
        student_id = st.text_input('Enter Student ID:')
        name = st.text_input("Enter Student Name:").title()
        department = st.text_input("Enter Student Department:").upper()
        year = st.number_input("Enter Student Academic Year:", min_value=1, max_value=4, step=1)
        email = st.text_input("Enter Student Email:")
        phone = st.number_input("Enter Student Phone No:")
        add_btn = st.form_submit_button("Add Student")
        
        if add_btn:
            new_student = {
                "Student_ID": student_id,
                "Name": name,
                "Department": department,
                "Year": year,
                "Email": email,
                "Phone": phone
            }
            df.loc[len(df)] = new_student
            save_changes()

# Delete Student
elif menu == "Delete Student":
    st.subheader("🚮 Delete Student")
    delete_id = st.text_input("Enter Student ID to Delete:")
    if st.button("Delete Student"):
        df.drop(df[df["Student_ID"] == delete_id].index, inplace=True)
        save_changes()

# Update Student
elif menu == "Update Student":
    st.subheader("✒️ Update Student Details")
    update_id = st.text_input("Enter Student ID to Update")
    if update_id:
        student_row = df[df["Student_ID"] == update_id]
        if not student_row.empty:
            new_name = st.text_input("New Name:", student_row.iloc[0]["Name"]).title()
            new_department = st.text_input("New Department:", student_row.iloc[0]["Department"]).upper()
            new_year = st.number_input("New Year:", student_row.iloc[0]["Year"])
            new_email = st.text_input("New Email:", student_row.iloc[0]["Email"])
            new_phone = st.number_input("New Phone:", student_row.iloc[0]["Phone"])
            
            if st.button("Update Student"):
                df.loc[df["Student_ID"] == update_id, ["Name", "Department", "Year", "Email", "Phone"]] = [
                    new_name, new_department, new_year, new_email, new_phone
                ]
                save_changes()
        else:
            st.warning("⚠️ Student ID not Found")
