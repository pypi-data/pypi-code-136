#  Created by Martin Strohalm

from setuptools import setup, find_packages

# get version
from gress import version
version = '.'.join(str(x) for x in version)

# get description
with open("README.md", "r") as fh:
    long_description = fh.read()

# set classifiers
classifiers = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: OS Independent',
    'Topic :: Utilities']

# main setup
setup(
    name = 'gress',
    version = version,
    description = 'Gress - Naive progress monitor',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/xxao/gress',
    author = 'Martin Strohalm',
    author_email = '',
    license = 'MIT',
    classifiers = classifiers,
    packages = find_packages(),
    zip_safe = False)
