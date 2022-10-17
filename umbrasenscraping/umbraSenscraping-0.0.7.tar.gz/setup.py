import os.path
import setuptools

setuptools.setup(
    install_requires=[
        'requests[socks]',
        'lxml',
        'beautifulsoup4',
        'pytz; python_version < "3.9.0"',
        'filelock',
    ]
)
