#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2022/5/9 15:57
# @Author  : fangmj
# @File    : setup.py


from setuptools import setup, find_packages

setup(
    name='pyodbc_sqlite_orm_fmj',  # 包名
    version='1.0.4',  # 版本
    description="基于pyodbc和sqlite的orm工具",  # 包简介
    long_description="基于pyodbc和sqlite的orm工具",  # 读取文件中介绍包的详细内容
    include_package_data=True,  # 是否允许上传资源文件
    author='fangmj',  # 作者
    author_email='1427347600@qq.com',  # 作者邮件
    # maintainer='',  # 维护者
    # maintainer_email='',  # 维护者邮件
    license='Apache License',  # 协议
    url='https://github.com/mjfang09/pyodbc-orm.git',  # github或者自己的网站地址
    packages=find_packages(),  # 包的目录
    # classifiers=[
    #     'Development Status :: 3 - Alpha',
    #     'Intended Audience :: Developers',
    #     'Topic :: Software Development :: Build Tools',
    #     'License :: OSI Approved :: Apache License',
    #     'Programming Language :: Python :: 3',  # 设置编写时的python版本
    # ],
    python_requires='>=3.8',  # 设置python版本要求
    install_requires=['pyodbc'],  # 安装所需要的库
    # entry_points={
    #     'console_scripts': [
    #         ''],
    # },  # 设置命令行工具(可不使用就可以注释掉)

)
