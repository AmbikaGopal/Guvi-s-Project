import streamlit as st
from Db import Database
import mysql.connector
import pandas as pd
import numpy as np

# conn = mysql.connector.connect(host="127.0.0.1", user="root", password="1GopiAmbi!", database='placement_app')
st.title('Placement Eligibility Checker')

# def fetch_students():
#     cursor=conn.cursor()
#     cursor.execute("select * from Students")
#     rows=cursor.fetchall

# fetch_students()

d=Database(host="127.0.0.1", user="root", password="1GopiAmbi!", database='placement_app')
students = d.fetch_all_students()
# st.write(students)

# option = st.selectbox('What you want to view?', ('title','num'),) 
# st.write("You selected to view", option)

option=st.sidebar.selectbox('Select a Page',('Home','Students','Check the eligibility','Analytics','Placed Students'))
st.write(option,'Page')

if option =='Home':
    st.title("Welcome to Home Page")
    st.write("Use side bar to navigate")
elif option=='Students':
    st.header('Welcome to Students Page')
    st.write("Students Table:")
    d=Database(host="127.0.0.1", user="root", password="1GopiAmbi!", database='placement_app')
    students = d.fetch_all_students()
    # st.table(students)
    st.dataframe(students)

elif option=="Check the eligibility":
    st.subheader("Please check the eligibility of student")
    min_

elif option=="Placed Students":
    st.header('List of placed students')
    
else:
    st.header("Welcome to Analytics Page")






