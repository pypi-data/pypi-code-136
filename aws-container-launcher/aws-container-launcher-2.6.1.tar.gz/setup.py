#!/usr/bin/env python3
import setuptools

setuptools.setup(
    python_requires=">3.7.0",
    install_requires=[
        'boto3 >=1.23.10',
        'amazon-ec2-best-instance >=2.2.0'
    ],
)