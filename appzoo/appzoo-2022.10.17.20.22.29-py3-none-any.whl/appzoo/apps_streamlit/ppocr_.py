#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AppZoo.
# @File         : ppocr
# @Time         : 2021/11/5 下午2:40
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  : 



import numpy as np
import cv2
import streamlit as st
from paddleocr import PaddleOCR, PPStructure, draw_structure_result, save_structure_res


@st.experimental_singleton()
def ppmodel():
    return PPStructure(show_log=True)


table_engine = ppmodel()

uploaded_file = st.file_uploader(label='File uploader')

if uploaded_file is not None:
    st.image(uploaded_file)

    bytes_data = uploaded_file.read()
    np_arr = np.frombuffer(bytes_data, dtype=np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

    result = table_engine(img)

    st.markdown(result[0]['res'].replace("""<table>""", """<table style="width: 10px;">"""), True)

    st.json(result)
