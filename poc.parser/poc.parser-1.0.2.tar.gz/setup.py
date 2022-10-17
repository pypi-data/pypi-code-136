from __future__ import print_function
from setuptools import setup, find_packages


setup(
    name='poc.parser',
    version='1.0.2',
    description="poc framework",
    author="",
    author_email="",
    packages=find_packages(),
    install_requires=[
        'PyYAML>=5.3.1',
        'chardet>=3.0.2,<3.1.0',
        'idna>=2.5,<2.8',
        'urllib3>=1.21.1,<1.25',
        'certifi>=2017.4.17',
        'PySocks==1.7.1'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires=">=3.6",
    scripts=["poc_parser/proxychainwrap.sh"]
)
