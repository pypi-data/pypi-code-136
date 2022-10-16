from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.0.0.1'
DESCRIPTION = 'test'
LONG_DESCRIPTION = 'test'

# Setting up
setup(
    name="smairio",
    version=VERSION,
    author="smairio98",
    author_email="<smairio98@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description="test",
    packages=find_packages(),
    install_requires=[],
    keywords=[],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)