from setuptools import setup, find_packages

version = {}
with open("retrieval/version.py") as fp:
    exec(fp.read(), version)

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name='retrieval',
    version=version["__version__"],
    author="Xing Han Lu",
    author_email="pypi@xinghanlu.com",
    url='https://github.com/xhluca/retrieval',
    description='Modular toolkit for dense retrieval with neural networks.',
    long_description=long_description,
    long_description_content_type="text/markdown",
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