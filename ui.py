import pandas as pd
import streamlit as st
import os
import random
import string
import csv
from subprocess import check_output

def randomname(n):
   randlst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
   return ''.join(randlst)

def ft_post_processing(text1):
    thisdict = {}
    with open("./ft_post_processing.csv", encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            thisdict[row[0]] = row[1]
    for x, y in thisdict.items():
        text1 = text1.replace(x, y)
    return text1

st.set_page_config(page_title='簡繁轉換', page_icon=None, layout="wide", initial_sidebar_state="auto", menu_items={'About': "Simple Tradition Chinese Converter\nsource: https://github.com/wuzhonglin/jfconv-scripts"})
with st.expander('其他網站', expanded=False):
    st.markdown(f"[聽打 https://pemail.epochbase.com/asr/](https://pemail.epochbase.com/asr/)")
    st.markdown(f"[翻譯 https://pemail.epochbase.com/translate/](https://pemail.epochbase.com/translate/)")

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
            out1 = check_output(["./runjf.sh", tmpfile]).decode('utf-8')
            out = ft_post_processing(out1)
        else:
            out = check_output(["./runfj.sh", tmpfile]).decode('utf-8')
        st.session_state["default"] = out
with col3:
    txtTo = st.text_area('Output', height=600, value=st.session_state["default"])
