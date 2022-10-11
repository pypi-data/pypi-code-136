#!/usr/bin/env python

from setuptools import setup
from setuptools.command.test import test as TestCommand
import pyhive
import sys


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


with open('README.rst') as readme:
    long_description = readme.read()

test_deps = [
    'mock>=1.0.0',
    'pytest',
    'pytest-cov',
    'requests>=1.0.0',
    'sqlalchemy>=1.3.0',
    'thrift==0.13.0',
]

setup(
    name="py-hive-iomete",
    version=pyhive.__version__,
    description="Python interface to iomete (Hive)",
    long_description=long_description,
    url='https://github.com/iomete/py-hive-iomete',
    author="Vusal Dadalov",
    author_email="vusal@iomete.com",
    license="Apache License, Version 2.0",
    packages=['pyhive', 'TCLIService'],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Topic :: Database :: Front-Ends",
    ],
    install_requires=[
        'future',
        'python-dateutil',
        'thrift==0.13.0'
    ],
    extras_require={
        'sqlalchemy': ['sqlalchemy>=1.3.0'],
        'test': test_deps,
    },
    tests_require=test_deps,
    cmdclass={'test': PyTest},
    package_data={
        '': ['*.rst'],
    },
    entry_points={
        'sqlalchemy.dialects': [
            "hive = pyhive.sqlalchemy_hive:HiveIometeDialect",
            "hive.iomete = pyhive.sqlalchemy_hive:HiveIometeDialect",
            "iomete = pyhive.sqlalchemy_iomete:IometeDialect"
        ],
    }
)
