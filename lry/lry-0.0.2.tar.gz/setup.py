# -*- encoding: utf-8 -*-
from distutils.core import setup

setup(
    name="lry",
    version="0.0.2",
    description="数据挖掘实验4",
    author="lry",
    author_email="1224137702@qq.com",
    packages=["LRY"],
    install_requires=[
        'numpy',
        'pandas',
        'xlrd',
        'xlrd3',
        'matplotlib',
        'scikit-learn'
    ]
)