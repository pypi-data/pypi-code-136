# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='excel_tools',
    version='1.0.14',
    author='hakaboom',
    author_email='1534225986@qq.com',
    license='Apache License 2.0',
    description='This is a tool for excel',
    url='https://github.com/hakaboom/excel_tools',
    include_package_data=True,
    packages=find_packages(),
    install_requires=["openpyxl==3.0.7", "xlrd==2.0.1"],
)