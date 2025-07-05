import streamlit as st 
import pandas as pd 

# Tạo tiêu đề 
st.title("Hello World") 

# Tạo header 
st.header("Header") 

# Tạo subheader
st.subheader("Subheader")

# Tạo text 
st.text("Text")

# Tạo heading level 1
st.write("Heading 1")

# Hiển thị số 
st.write(42)

# Hiển thị list 
st.write(["Apple", "Banana", "Grape"])

# Tạo một dataframe mẫu 
df = pd.DataFrame(
    {
        "column1": [1, 2, 3],
        "column2": ["An", "Viet", "Nguyen"]
    }
)

# Hiển thị dataframe lên màn hình streamlit (Cách 1)
st.write(df) 

# Cách 2
st.dataframe(df)

# Cách 3
st.table(df) 

# Hiển thị ảnh 
st.image("./Assets/image.png")

# Hiển thị audio 
st.audio("./Assets/audio.mp3")

# Hiển thị video 
st.video("./Assets/video.mp4")

# Hiển thị video youtube 
st.video("https://www.youtube.com/watch?v=eEWa7cpiyD8")