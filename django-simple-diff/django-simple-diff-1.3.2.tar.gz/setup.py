#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from setuptools import setup, find_packages

from simple_diff import __version__

DESCRIPTION = 'Tracks model changes before save.'
CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django :: 2.2',
    'Framework :: Django :: 3.2',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Development Status :: 5 - Production/Stable',
    'Programming Language :: Python :: 3.8',
]

setup(
    name='django-simple-diff',
    version=__version__,
    author='Kevin Clark',
    author_email='kclark@edustaff.org',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    url='https://gitlab.com/edustaff/django-simple-diff',
    license='MIT',
    install_requires=[
        "django",
    ],
    keywords=['django', 'templates'],
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    packages=find_packages(exclude=['example', 'docs']),
    include_package_data=True,
)
