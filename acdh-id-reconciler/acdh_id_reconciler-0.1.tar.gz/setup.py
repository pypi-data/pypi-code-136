#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()


requirements = [
    'acdh-arche-assets>=3.6,<4',
    'SPARQLWrapper>=1.8.5,<3',
]

setup_requirements = []

test_requirements = []

setup(
    author="Peter Andorfer",
    author_email='peter.andorfer@oeaw.ac.at',
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
    ],
    description="Python package to reconcile GND, GeoNames IDs via WikiData",
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    name='acdh_id_reconciler',
    packages=find_packages(include=['acdh_id_reconciler', 'acdh_id_reconciler.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/acdh-oeaw/acdh-id-reconciler',
    version="v0.1",
    zip_safe=False,
)
