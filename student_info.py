import streamlit as st
import pandas as pd 
import numpy as np
st.title("Student Details Management App")

data=pd.read_csv(r"C:\Users\Manoj kumar\OneDrive\Desktop\manoj's python\student_data.csv")
df=pd.DataFrame(data)

#save changes
def save_changes():
    df.to_csv(r"C:\Users\Manoj kumar\OneDrive\Desktop\manoj's python\student_data.csv", index=False)
    print("Changes saved to CSV file")


#view student details
def view_students_info():
    print(df)


#add student details
def add_student():
    student_id=input('enter student id :')
    name=input("enter student name:").title()
    department=input("enter student department:").upper()
    year=int(input("enter student academic year:"))
    email=input("enter student email:")
    phone=int(input("enter student phone no:"))
    
    df.loc[len(df)]=[student_id,name,department,year,email,phone]
    
    print("student added successfully")
    
# delete student data

def delete_student():
    global df
    student_id=input("enter student id:")
    df=df[df['Student_ID']!=student_id]
    print("student data deleted successfully")

#update student data

def update_student():
    global df
    student_id=input("enter student id:")
    
    index=df[df['Student_ID']==student_id].index
    
    name=input("enter student name:").title()
    department=input("enter student department:").upper()
    year=int(input("enter student academic year:"))
    email=input("enter student email:")
    phone_no=int(input("enter student phone no:"))
    
    df.loc[index,'Name']=name
    df.loc[index,"Department"]=department
    df.loc[index,'Year']=year
    df.loc[index,'Email']=email
    df.loc[index,'Phone']=phone_no
    
    print("student details updated successfully")

#add_student()

#view_students_info()

#delete_student()

#save_changes()

st.title("Student Details Management App")

if st.button("Enter"):
    st.write("Welcome")

#for showing student data
st.subheader("Student Records")
st.dataframe(data)