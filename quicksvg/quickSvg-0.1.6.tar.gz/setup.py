# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setup
   Description :
   Author :       liaozhaoyan
   date：          2022/10/3
-------------------------------------------------
   Change Activity:
                   2022/10/3:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     setup.py
   Description :
   Author :       liaozhaoyan
   date：          2022/9/28
-------------------------------------------------
   Change Activity:
                   2022/9/28:
-------------------------------------------------
"""
__author__ = 'liaozhaoyan'

VERSION = '0.1.6'

import sys
from setuptools import setup

reqLists = ["treelib", "six"]

setup(name='quickSvg',
      version=VERSION,
      description="quick svg draw.",
      long_description='quick svg draw.',
      classifiers=["Topic :: Text Processing :: Markup :: XML",
                   "Programming Language :: Python",
                   "Programming Language :: Python :: 2",
                   "Programming Language :: Python :: 2.7",
                   "Programming Language :: Python :: 3",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3.6",
                   "Programming Language :: Python :: 3.7",
                   "Programming Language :: Python :: 3.8",
                   "Programming Language :: Python :: 3.9",
                   "Programming Language :: Python :: 3.10",
                   "Programming Language :: Python :: Implementation :: PyPy",
                   ],  # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='quick svg',
      author='liaozhaoyan',
      author_email='zhaoyan.liao@linux.alibaba.com',
      url="https://github.com/liaozhaoyan/quickSvg",
      license='MIT',
      packages=["quickSvg"],
      include_package_data=True,
      zip_safe=True,
      install_requires=reqLists,
      entry_points={

      }
      )

if __name__ == "__main__":
    pass

