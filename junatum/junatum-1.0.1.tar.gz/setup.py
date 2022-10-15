#!/usr/bin/env python3
from setuptools import find_packages, setup

with open('LICENSE') as f:
    license_txt = f.read()

setup(
    name='junatum',
    version='1.0.1',
    url='https://github.com/Junatum/junatum',
    license=license_txt,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    author='Junatum',
    author_email='admin@junatum.com',
    description='Common modules for all projects.',
    packages=find_packages(exclude=('docs', 'tests')),
    zip_safe=False,
    python_requires='>=3.8',
    setup_requires=[
        'python-dateutil>=2.8.0',
        'pytz>=2020.1',
        'humanize>=2.6.0',
        'furl>=2.1.0',
        'validators>=0.18.2',
    ],
)
