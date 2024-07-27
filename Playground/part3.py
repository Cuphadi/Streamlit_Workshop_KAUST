import streamlit as st
import numpy as np
import plotly.express as px
import pandas as pd
import time
#import matplotlib

#form = st.form("Form 1")
#form.text_input("First Name")
#form.form_submit_button("Submit")

with st.form("Form 1"):
    f=st.text_input("First Name")
    l=st.text_input("Last Name")
    e=st.text_input("Email")
    state = st.form_submit_button("Submit")
    if state:
        if f == "" or l == "" or e == "":
            st.error("Enter Everything")
        else:
            st.success("Entered Successfully!")
#st.sidebar.write("Sidebar")

with st.sidebar:
    st.write("Sidebar")

#with st.spinner("Wait!"):
#    time.sleep(10)
#    st.write("hey")

with st.expander("open to see expander"):
    st.write("works!")

taba, tabb = st.tabs(["tab a", "tab b"])
with tabb:
    st.write("tab b test")
taba.write("tab a test")

x = np.linspace(0,10,100)
st.write(x)
plot = px.line(pd.DataFrame({"x":x, "sin":np.sin(x), "cos":np.cos(x)}), x='x', y=['sin','cos'])
st.plotly_chart(plot)

st.line_chart(pd.DataFrame({"x":x, "sin":np.sin(x), "cos":np.cos(x)}) , x='x', y=['sin','cos'])
st.area_chart(pd.DataFrame({"x":x, "sin":np.sin(x), "cos":np.cos(x)}) , x='x', y=['sin','cos'])
st.bar_chart(pd.DataFrame({"x":x, "sin":np.sin(x), "cos":np.cos(x)}) , x='x', y=['sin','cos'])

st.snow()
#st.balloons()