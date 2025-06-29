import streamlit as st 
import pandas as pd
import numpy as np
import Db


# st.title("Placement Eligibility Application")
# st.header('Header')
# st.subheader('This is the subheader')
# st.text("This is an interactive streamlit application") #Can handle only text type
# st.markdown("""
# # h1 tag
# ## h2 tag
# ### h3 tag
            
# :moon: <br>
 #Breaking two lines (True - understood it contains some html tags)
# :sunglasses:
            
# **Bold**
# _italic_
            
# """,True)

# write() Versatile function used to display the text/data. Handle many datatypes

# st.write("Hello World")
# st.write(st) # Passing a streamlit library, gives a detailed idea about the streamlit module

# st.write(sum)
# st.write(1,2,3,4,5)
# st.write("The numbers are",[1,2,3,4,5,6,7,8,9,10])
# st.write('## Header using write()')
# st.write('**Bold in the write**')

# #How to display different formats of data in streamlit application 

# dict ={'Name':'Ambika','Age':45,'Course':'Guvi-DS'}
# st.write(dict)

# # TO display datagrame in streamlit app

# df=pd.read_csv("C:/Users/USER/Documents/Data/Lab1Data.csv")
# st.write(df)

# st.dataframe(df) # In pd/dataframe nwwd to scroll to view the overall data
# st.table(df) # in table no need to scroll

s = thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964 ,
  "colors": ["red", "white", "blue"],
  'color_1':['green', 'oraange', 'yellow', 'black'],
  'range':['12L', '9L','15L', '10L'] }
# st.json(s)
st.json(s,expanded=False)

st.metric("Infy Stock", value=457, delta='23.5')

st.metric("Infy Stock", value=457, delta='23.5', delta_color='inverse')
st.metric("Infy Stock", value=457, delta='23.5', delta_color='off')
st.metric("Infy Stock", value=457, delta='-23.5')

# title = st.text_input('Movie Title','') 
# st.write("The current movie title is ", title) 

# num = st.number_input('Number is',value=None, placeholder='Enter a number') 
# st.write("The current number is ", num) 

# option = st.selectbox('What you want to view?', ('title','num'),) 
# st.write("You selected to view", option)
