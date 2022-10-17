"""
@Project:ezface_package
@File:setup.py
@Author:郑智
@Date:10:31
""" 
from setuptools import setup, find_packages
setup(name="bailan",
      version="0.0.1",
      author="zhengzhi",
      author_email="3461736320@qq.com",
      description="This project provides an easy way to recognize faces using AI",
      #项目主页
      # url="https://github.com/sunjian-github/bailan",
      # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
      packages=find_packages() )