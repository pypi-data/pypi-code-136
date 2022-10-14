import os
import setuptools
import djangopebble
from m2r import parse_from_file


dirname = 'djangopebble'
version = djangopebble.version()
# print("version ================ ", version)


# with open("Readme.md", "r", encoding='utf-8') as fh:
#     long_description = fh.read()
long_description = parse_from_file('Readme.md')     # .markdown必须转换为.rst, 否则有可能报错


setuptools.setup(
    name=dirname,
    version=version,
    author="jml",
    author_email='642201822@qq.com',   # 作者邮箱
    description="Wish this package be your pebble in using Django.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitee.com/hedong-guest/djangopebble',   # 主页链接
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['pandas', 'django', 'openpyxl', 'xlrd==1.2.0', 'bdtime', 'tqdm'],      # 依赖模块
    include_package_data=True,
)
