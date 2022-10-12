#!/usr/bin/env python
# -*- coding:utf-8 -*-

from setuptools import setup, find_packages  # 这个包没有的可以pip一下

setup(
    name="xcall",  # 这里是pip项目发布的名称
    version="0.0.6",  # 版本号，数值大的会优先被pip
    keywords=["pip", "xcall"],  # 关键字
    description="Xcall for python.",  # 描述
    long_description="Xcall for python.",
    license="MIT Licence",  # 许可证

    url="https://code.byted.org/reading/XCall",  # 项目相关文件地址，一般是github项目地址即可
    author="janking",  # 作者
    author_email="jankingwon@foxmail.com",

    packages=find_packages(),
    include_package_data=True,
    platforms="any",
    install_requires=[]  # 这个项目依赖的第三方库
)

# python3 setup.py sdist
# twine upload dist/xcall-0.0.5.tar.gz
