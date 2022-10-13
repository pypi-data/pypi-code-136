# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   PytestAssertError
# FileName:     setup.py
# Author:      Jakiro
# Datetime:    2022/10/13 15:00
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------


import setuptools
import os
import sys

'''
将工具打包成可执行命令
'''

# with open('DataTypeHandle.md', 'r') as fp:
#     description1 = fp.readlines()
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
setuptools.setup(
    # 项目介绍
    name='PytestAssertError',
    # 版本号
    version='0.0.1',
    # author
    author='Jakilo',
    anthor_email='17709005281@163.com',
    description='修改pytest运行报错为中文',
    # 需要安装的第三方依赖
    install_requires=[
        'pytest'
    ],
    # 此项很重要，如果不自动查找依赖包，会导致运行时的找不到包错误
    packages=setuptools.find_packages(),
    py_modules='pytest_assert_error_plugin',
    python_requires='>=3.6',
    # 可执行文件的函数入口
    entry_points={
        'pytest11': [
            # 可执行文件的名称=执行的具体代码方法
            'change_assert = pytest_assert_error_plugin'
        ]
    },
    # 决定安装位置
    zip_safe=False,
    # 是否导入MANIFEST.in目录中的文件
    include_package_data=True
)
