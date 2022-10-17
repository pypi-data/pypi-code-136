"""
@Project:eaface_package
@File:setup.py
@Author:韩晓雷
@Date:9:11
"""
from setuptools import setup, find_packages
setup(
    name="veriface",
    version="0.0.1",
    author="han",
    author_email="3091002212@qq.com",
    description="This project provides an easy way to recognize faces using AI",
    # 项目主页
    url="https://github.com/sunjian-github/ezface",
    # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
    packages=find_packages()
)