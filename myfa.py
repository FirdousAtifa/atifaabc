import streamlit as st
st.title("Discipline and movitated")
st.header("wallpaper")
name=st.text_input("enter your name")
age=st.number_input("enter your age",min_value=18,max_value=100,step=5)
st.write(f"name{name} your age is {age}")
gender=st.selectbox("select your gender",["Male","Female"])
subject=st.multiselect("select your choice",["Python","java","c++","mysql"])
login=st.button("login")

if login:
    st.success("submitted sucessfully")
    st.write(name)
    st.write(age)
    st.write(gender)
    st.write(subject)

st.divider()
st.image(r"C:\Users\aanis\OneDrive\Pictures\Screenshots\Screenshot 2026-08-27 150028.png")
import os
st.image(os.path.join(os.getcwd(),"static","Screenshot 2026-08-27 150043.PNG"))