from setuptools import setup, find_packages

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pysdl',
    version='1.1.0',
    url='',
    license='',
    author='NewtonX',
    author_email='',
    python_requires='>=3.4',
    test_suite="tests.tests",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=find_packages("src", exclude="tests"),
    description='A python library that helps Stackdriver consume python logs appropriately built on madzak/python-json-logger',
)
