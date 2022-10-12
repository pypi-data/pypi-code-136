from setuptools import setup, find_packages

version = {}
with open("retrieval/version.py") as fp:
    exec(fp.read(), version)

with open('README.md') as fp:
    long_description = fp.read()

setup(
    name='retrieval',
    version=version["__version__"],
    author="Xing Han Lu",
    author_email="pypi@xinghanlu.com",
    url='https://github.com/xhluca/retrieval',
    description='Toolkit for dense neural retrieval.',
    long_description=long_description,
    packages=find_packages(
        where='src',
        include=["retrieval"],
        exclude=[],
    ),
    install_requires=[
        # dependencies here
    ],
    extras_require={
        # For special installation, e.g. pip install retrieval[dev]
        'dev': ['black', 'twine']
    }
)