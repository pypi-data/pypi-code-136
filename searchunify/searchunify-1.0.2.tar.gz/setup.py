#!/usr/bin/env python

import setuptools

setuptools.setup(
    include_package_data=True,
    name="searchunify",
    version='1.0.2',
    description='The SearchUnify SDK enables developers to easily work with the SearchUnify platform and build scalable solutions with search, analytics, crawlers and more.',
    author='SearchUnify',
    author_email='ankur.mahajan@grazitti.com',
    url='https://www.searchunify.com/',
    packages=[
        'searchunify',
        'searchunify.core', 
        'searchunify.client', 
        'searchunify.utils', 
    ],
    install_requires=['requests==2.23.0', 'schema==0.7.4']
)