import streamlit as st
import time
from datetime import time as t

st.title("Uploader")
st.markdown("---")
image = st.file_uploader("Upload image", type=["gif"])
if image is not None:
    st.image(image,use_column_width=True)

col1, col2 = st.columns(2)

st.slider("Slider", min_value=50, value=70, max_value=120)
col1.text_input("Text input")
col2.text_area("Text area")
date = st.date_input("Date input")
st.write(date, type(date))
stime = st.time_input("Time input", value=t(0,0,0))
if stime == t(0,0,0):
    st.write("Change Time")
else:
    progress = st.empty()
    bar = st.progress(0)
    tot = stime.minute + stime.hour * 60
    for i in range(tot+1):
        bar.progress(int((i)/tot*100))
        progress.write(i)
        time.sleep(1)




