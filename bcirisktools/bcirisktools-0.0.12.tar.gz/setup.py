from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.12'
DESCRIPTION = 'BCI risks tools'
LONG_DESCRIPTION = 'A package that compiles different risk tools used by BCI bank.'

# Setting up
setup(
    name="bcirisktools",
    version=VERSION,
    author="Mezosky",
    author_email="<imezadelajara@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['pandas', 'numpy', 'sklearn', 'matplotlib', 'plotly', 'shap>=0.41.0', 'scipy', 'tqdm', 'xgboost>=1.6.2'],
    keywords=['python', 'risk', 'tools', 'bci'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)