#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

REQUIREMENTS = [
    'arrow',
    'click>=7.0',
    'python-crontab',
    'requests',
    'configparser',
    'tzlocal',
]

SETUP_REQUIREMENTS = []

TEST_REQUIREMENTS = []

setup(
    author="Edouard BATIGA",
    author_email='dev@enyosolutions.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Topic :: System :: Monitoring",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A cron shell wrapper for registering and "
                "updating cron jobs automatically in healthchecks",
    entry_points={
        'console_scripts': [
            'sch=sch.cli:main',
        ],
    },
    install_requires=REQUIREMENTS,
    license="GNU General Public License v3",
    long_description=README + '\n\n' + HISTORY,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords='sch',
    name='sch2',
    packages=find_packages(),
    setup_requires=SETUP_REQUIREMENTS,
    test_suite='tests',
    tests_require=TEST_REQUIREMENTS,
    url='https://github.com/enyosolutions-team/health-check-sch.git',
    version='0.0.1',
    zip_safe=False,
)
