# -*- coding:utf-8 -*-

from setuptools import setup, find_packages

packages = [
    'cklink',
]

setup(
    name="pycklink",
    version="0.1.1",
    author="tanjiaxi",
    author_email="jxtan@bouffalolab.com",
    description="Python interface for the T-HEAD CKLink",
    long_description="Python interface for the T-HEAD CKLink",
    license="MIT",
    url="https://pypi.org/project/PyCKLink/",
    packages=find_packages(), 
    #package_dir={'': 'cklink'},
    include_package_data=True,
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>3.0,<4.0',
    zip_safe=False,
)
