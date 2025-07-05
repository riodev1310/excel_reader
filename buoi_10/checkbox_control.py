import streamlit as st 

checkbox = st.checkbox("Tackle")


# if checkbox:
#     st.video("https://www.youtube.com/watch?v=eEWa7cpiyD8")
# else:
#     st.text("No video display")

radio_btn = st.radio("Where are you from?", options = ["Video", "Audio", "Image", "None"])

if radio_btn == "Video":
    st.video("https://www.youtube.com/watch?v=eEWa7cpiyD8")
elif radio_btn == "Audio":
    st.audio("./Assets/audio.mp3")
elif radio_btn == "Image":
    st.image("./Assets/image.png")
# else:
#     st.write("nothing display")

# Select box
select_box = st.selectbox("Where are you from?", options = ["Video", "Audio", "Image", "None"])
if select_box == "Video":
    st.video("https://www.youtube.com/watch?v=eEWa7cpiyD8")
elif select_box == "Audio":
    st.audio("./Assets/audio.mp3")
elif select_box == "Image":
    st.image("./Assets/image.png")
else:
    st.write("nothing display")
    
    
multi_select = st.multiselect("Where are you from?", options = ["Video", "Audio", "Image", "None"])
st.write(multi_select)