import io
import re
from setuptools import setup

PACKAGE_NAME = "aws-s3"

setup(
    name='aws-s3-trace-log',
    version='0.0.2',
    packages=['aws-s3'],
    install_requires=[
        'requests',
        'importlib; python_version == "3.8"',
    ],
)