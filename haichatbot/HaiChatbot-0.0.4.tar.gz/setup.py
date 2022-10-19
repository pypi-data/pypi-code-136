# -*- coding: utf-8 -*-
# @Time : 2022/10/19 13:06
# @Author : Wang Hai
# @Email : nicewanghai@163.com
# @Code Specification : PEP8
# @File : setup.py.py
# @Project : HaiHai
import setuptools

# 读取 README.md 得到详细介绍
# with open("readme.md", "r") as fh:
#     long_description = fh.read()

setuptools.setup(
    name="HaiChatbot",  # 名称
    version="0.0.4",  # 版本
    author="Wang Hai",  # 作者
    author_email="nicewanghai@163.com",  # 邮箱
    description="chatbot",  # 简介
    long_description="None",  # 详细介绍
    long_description_content_type="text/markdown",  # 详细介绍的文件类型
    url="https://github.com/Happleasei/HaiHai",  # 包的链接
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3", "License :: OSI Approved :: MIT License", "Operating System :: OS Independent"],
)

