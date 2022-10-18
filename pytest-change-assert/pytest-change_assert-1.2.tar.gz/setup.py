# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   PytestAssertError
# FileName:     setup.py
# Author:      Jakiro
# Datetime:    2022/10/13 18:52
# Description:
# 命名规则  文件名小写字母+下划线，类名大驼峰，方法、变量名小写字母+下划线连接
# 常量大写，变量和常量用名词、方法用动词
# -----------------------------------------------------------------------------------
from setuptools import setup, find_packages

setup(
    name='pytest-change_assert',
    author='Jakilo',
    version='1.2',
    url='https://github.com/Jakilo1996/PytestAssertErrorPlugin',
    python_requires=' >=3',
    description='修改报错中文为英文',
    classifiers=['Framework :: Pytest'],
    py_modules=['tests'],
    packages=find_packages(),
    install_require=['pytest'],
    entry_points={
        'pytest11': [
            'pytest-change_assert = pytest_assert_error',
        ],
    },
)
