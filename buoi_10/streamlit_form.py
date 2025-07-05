import streamlit as st  

name = st.text_input("Nhập họ tên: ")

age = st.number_input("Tuổi: ", min_value = 0.0, step = 1.0)

button = st.button("Test")

st.header("Form")
st.write(name)
st.write(age) 


# Streamlit form 
with st.form("User_form"):
    name = st.text_input("Nhập họ tên: ")
    age = st.number_input("Tuổi: ", min_value = 0.0, step = 1.0)
    submitted = st.form_submit_button("Enter") 
    
st.header("Streamlit Form")
if submitted:
    if name != "" and age != 0.0:
        st.write(name)
        st.write(age)
    else:
        st.warning("Fill in all information")
