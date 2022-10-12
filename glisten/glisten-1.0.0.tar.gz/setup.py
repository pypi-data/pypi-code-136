from setuptools import setup, Extension
import re

description = 'A simple python logging library.'

try:
    with open('README.md', 'r', encoding='utf-8') as f:
        long_description = f.read()
except FileNotFoundError:
    long_description = description

setup(name='glisten',
      license                        = 'MIT License',
      version                        = 'v1.0.0',
      description                    = description,
      long_description               = long_description,
      long_description_content_type  = 'text/markdown',
      author                         = "Sean Richards",
      author_email                   = "ordinarystarman@gmail.com",
      packages                       = ['glisten'],
      zip_safe                       = False,
      homepage                       = 'https://github.com/Krytic/glisten',
      install_requires               = ['colorama']
    )
