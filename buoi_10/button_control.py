import streamlit as st  

# def show_hide():
#     show = not show 
    
button_show = st.button("Show video") # Xong 

if button_show:
    st.video("https://www.youtube.com/watch?v=eEWa7cpiyD8")
else: 
    st.text("No video display")