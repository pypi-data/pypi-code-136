#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AppZoo.
# @File         : x
# @Time         : 2022/9/23 上午11:01
# @Author       : yuanjie
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : 


import gradio as gr
def reverse(text):
    return text[::-1]
demo = gr.Interface(reverse, "text", "text")
demo.launch(share=True, auth=("username", "password"))