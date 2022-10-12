import os
from setuptools import setup, find_packages
_fn = os.getcwd()
print(os.listdir(f'{_fn}/src'))

version_fn = 'src/mlpreprocessor/version.py'
with open(version_fn, 'r') as f:
    verstr = f.read()
version = verstr.split('=')[1]
version = version.replace("'", "").strip()

setup(
    name="mlpreprocessor",
    version=version,
    author="wangziling100",
    author_email="wangziling100@163.com",
    description="Exposed interface tool for accessing vpc controller api",
    package_dir={"": "src"},
    packages=find_packages(where='src'),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)