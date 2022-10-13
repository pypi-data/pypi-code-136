
from __future__ import print_function
from setuptools import setup, find_packages

setup(
    name="bgutils_hddly",
    version="1.0.13",
    author="hddly",  #作者名字
    author_email="goodym@163.com",
    description="bigdata utils.",
    license="MIT",
    url="https://bigdata.hddly.cn",  #github地址或其他地址
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    install_requires=[
            'pandas>=0.20.0',  #所需要包的版本号
            'numpy>=1.14.0'   #所需要包的版本号
    ],
    zip_safe=True,
)
