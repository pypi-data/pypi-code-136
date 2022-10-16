from setuptools import setup

setup(
    name='aws-s3-trace-log',
    version='0.0.3',
    packages=['aws-s3'],
    install_requires=[
        'requests',
        'importlib; python_version == "3.8"',
    ],
)