"""
@Project:bailan_bad
@File:setup.py
@Author:郑智
@Date:14:12
""" 
from setuptools import setup, find_packages
setup(name="bailan",
      version="0.0.6",
      author="zhengzhi",
      author_email="3461736320@qq.com",
      #项目主页
      url="https://gitee.com/zheng--zhi/bailan.git",
      # 你要安装的包，通过 setuptools.find_packages 找到当前目录下有哪些包
      packages=find_packages() )