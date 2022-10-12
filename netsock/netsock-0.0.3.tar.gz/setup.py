#!/usr/bin/env python

from io import open
from setuptools import setup

"""
:authors: two-it2022
:license: Apache License, Version 0.3, see LICENSE file
:copyright: (c) 2022 two-it2022
"""

version = '0.0.3'
'''
with open('__readme__.md', encoding='utf-8') as f:
      long_description = f.read()
'''

long_description = '''Python module for Two It project
                  management platform (TwoIt API wrapper)'''


setup(
      name='netsock',
      version=version,

      author='two-it2022',
      author_email='kodland.group@gmail.com',

      description=(
            u'Python module for writing websites.'
            u'Two It 2022 (two-it.netlify.app API wrapper)'
      ),
      long_description=long_description,
      #long_description_content_type='text/markdown',

      url='https://github.com/TwoIt202/Network',
      download_url='https://github.com/TwoIt202/Network/raw/94a179087866ef5bd41a8c6ce777ec0cbffa8268/network.zip'.format(
            version
      ),

      license='Apache License, Version 0.3, see LICENSE file',

      packages=['netsock'],
      install_requires=['wikipedia', 'translate'],

      classifiers=[
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Intended Audience :: End Users/Desktop',
            'Intended Audience :: Developers',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Programming Language :: Python :: Implementation :: CPython',
      ]

)