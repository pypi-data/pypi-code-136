#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'numpy',
    'pyserial']

test_requirements = [ ]

setup(
    author="Tristan Cotte",
    author_email='tristan.cotte@sgs.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This package aims to manage lights thanks to the FG-PDV400W-24-8T with an UART connection protocol",
    install_requires=requirements,
    license="BSD license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='light_controller',
    name='light_controller',
    packages=find_packages(include=['light_controller', 'light_controller.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tcotte/light_controller',
    version='0.3.0',
    zip_safe=False,
)
