import pandas as pd
import streamlit as st
import os
import random
import string
from subprocess import check_output

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

st.set_page_config(page_title='簡繁轉換', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items={'About': "Simple Tradition Chinese Converter\nreference: https://github.com/wuzhonglin/jfconv-scripts"})
st.header('Simplified/Traditional Chinese Converter :sunglasses:', divider='rainbow')
if "default" not in st.session_state:
    st.session_state["default"]=""

col1, col2, col3 = st.columns(3)
with col1:
    txtFrom = st.text_area('Input', height=600, placeholder="please paste your text here")
with col2:
    optionFrom = st.selectbox('轉換方式',('簡->繁', '繁->簡'))
    if st.button('轉換'):
        tmpfile = f"work/{randomname(32)}"
        with open(tmpfile, "w") as text_file:
            text_file.write(txtFrom)
        if optionFrom == "簡->繁":
            out = check_output(["./runjf.sh", tmpfile]).decode('utf-8')
        else:
            out = check_output(["./runfj.sh", tmpfile]).decode('utf-8')
        st.session_state["default"] = out
with col3:
    txtTo = st.text_area('Output', height=600, value=st.session_state["default"])
