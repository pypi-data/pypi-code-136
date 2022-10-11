"""
handlr Python package is a python handler to logging services, i.e. Logstash as part of the ELK stack
By Joe Tilsed
Created: 11/10/2022
Last Updated: 11/10/2022
---
setup.py is the build script for setuptools.
It tells setuptools about this package (such as the name and version) as well as which code files to include.
"""

import os
import setuptools


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    long_description = readme.read()


setuptools.setup(
    name='handlr',
    version="0.1.0",
    author="Joe Tilsed",
    author_email="Joe@Tilsed.com",
    description="Python handler to logging services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/joetilsed/handlr/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    keywords="python logging handler logstash elk open-source",
)


# That's all folks...
