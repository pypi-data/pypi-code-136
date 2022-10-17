#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : AppZoo.
# @File         : page
# @Time         : 2022/9/22 下午2:19
# @Author       : yuanjie
# @WeChat       : meutils
# @Software     : PyCharm
# @Description  : https://zhuanlan.zhihu.com/p/547200679


import streamlit as st
from streamlit.components.v1 import html

# html("""<marquee bgcolor="#00ccff" behavior="alternate">这是一个滚动条</marquee>""")

import inspect
import textwrap


class Page(object):

    def __init__(self, app_title="# App Title",
                 app_info="> App Info",
                 sidebar_title="## Sidebar Title",
                 page_title="AI",  # "Page Title",
                 page_icon='🔥',
                 menu_items=None,
                 show_code=False,
                 hide_st_style=True,
                 layout="centered",  # wide
                 initial_sidebar_state="auto", # "auto" or "expanded" or "collapsed"
                 ):
        # 前面不允许有 streamlit 指令
        st.set_page_config(
            page_title=page_title,
            page_icon=page_icon,
            menu_items=menu_items,
            layout=layout,
            initial_sidebar_state=initial_sidebar_state,
        )

        # 隐藏streamlit默认格式信息 https://discuss.streamlit.io/t/st-footer/6447/11
        if hide_st_style:
            _ = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
            _ = st.markdown(
                """
                <style>.css-18e3th9 {padding-top: 2rem;}
                #MainMenu {visibility: hidden;}
                header {visibility: hidden;} 
                footer {visibility: hidden;}
                footer:after {content:"Made with Betterme";visibility: visible;display: block;position: 'fixed';}
                </style>
                """,
                unsafe_allow_html=True
            )  # 隐藏右边的菜单以及页脚
            st.markdown(_, unsafe_allow_html=True)

        if app_title: st.markdown(app_title)
        if app_info: st.markdown(app_info)
        if sidebar_title: st.sidebar.markdown(sidebar_title)

        if sidebar_title and show_code: self.show_code(self.main)

    def main(self):
        raise NotImplementedError('Method not implemented!')

    def show_code(self, demo):
        """Showing the code of the demo."""
        _ = st.sidebar.checkbox("Show code", False)
        if _:
            # Showing the code of the demo.
            st.markdown("---")
            st.markdown("## Main Code")
            sourcelines, _ = inspect.getsourcelines(demo)
            st.code(textwrap.dedent("".join(sourcelines[1:])))
            st.markdown("---")

    def display_pdf(self, base64_pdf, width='100%', height=1000):
        pdf_display = f"""<embed src="data:application/pdf;base64,{base64_pdf}" width="{width}" height="{height}" type="application/pdf">"""

        st.markdown(pdf_display, unsafe_allow_html=True)

    def display_html(self, text='会飞的文字'):
        _ = f"""
        <marquee direction="down" width="100%" height="100%" behavior="alternate" style="border:solid"  bgcolor="#00FF00">

          <marquee behavior="alternate">
        
            {text}
        
          </marquee>
        
        </marquee>
        """
        st.markdown(_, unsafe_allow_html=True)


if __name__ == '__main__':
    class SPage(Page):

        def main(self):
            st.markdown("这是个`main`函数")


    SPage(sidebar_title='').main()
