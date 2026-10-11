import streamlit as st
import pandas as pd 
import numpy as np
st.title("Student Details Management App")

data=pd.read_csv(r"C:\Users\Manoj kumar\OneDrive\Desktop\manoj's python\student_data.csv")
df=pd.DataFrame(data)

#save changes
def save_changes():
    df.to_csv(r"C:\Users\Manoj kumar\OneDrive\Desktop\manoj's python\student_data.csv", index=False)
    st.success("Changes saved to CSV File")


#view student details
st.subheader("view_students_details")
st.dataframe(df)


#add student details
st.subheader("➕Add New Student")
student_id=st.text_input('enter student id:')
name=st.text_input("enter student name:").title()
department=st.text_input("enter student department:").upper()
year=st.number_input("enter student academic year:",min_value=1,max_value=4,step=1)
email=st.text_input("enter student email:")
phone=st.number_input("enter student phone no:")
    
if st.button("Add new student"):
    new_student={
        "Student_ID":student_id,
        "Name":name,
        "Department":department,
        "Year":year,
        "Email":email,
        "Phone":phone
            
    }
    df.loc[len(df)]=new_student 
    save_changes()
        
#deleting student details
st.subheader("🚮Delete Student")
delete_id=st.text_input("Enter Student ID to Delete:")
if st.button("Delete Student"):
    df.drop(df[df["Student_ID"]==delete_id].index,inplace=True)
    save_changes()
    
    
#update Student Details
st.subheader("✒️ Update Student Details")
update_id=st.text_input("Enter Student ID to Update")
if update_id:
    student_row=df[df["Student_ID"]==update_id]
    if not student_row.empty:
        new_name=st.text_input("New Name:",student_row.iloc[0]["Name"]).title()
        new_department=st.text_input("New Department:",student_row.iloc[0]["Department"]).upper()
        new_year=st.number_input("New year:",student_row.iloc[0]["Year"])
        new_email=st.text_input("New Email:",student_row.iloc[0]["Email"])
        new_phone=st.number_input("New Phone:",student_row.iloc[0]["Phone"])
        
        if st.button("Update Student"):
            df.loc[df["Student_ID"]==update_id,["Name","Department","Year","Email","Phone"]]=[
                new_name,new_department,new_year,new_email,new_phone]
            save_changes()
    else:
        st.warning("StudentID not Found🤷‍♂️")
