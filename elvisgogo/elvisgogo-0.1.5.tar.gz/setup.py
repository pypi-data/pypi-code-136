# -*- encoding: utf-8 -*-
from setuptools import setup,find_packages

setup(
    name="elvisgogo",
    version="0.1.5",
    description="数据挖掘实验4",
    author="lry",
    author_email="1224137702@qq.com",
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'xlrd',
        'xlrd3',
        'matplotlib',
        'scikit-learn',
        'LRY',
        'torch',
        'torchvision',
        'tensorflow',
        'urllib',
        'lry_timer',
        'lry_test'
    ]
)