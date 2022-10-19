from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.6'
DESCRIPTION = 'Collection of helpfull appconfiguration extensions'
LONG_DESCRIPTION = 'Collection of helpfull appconfiguration extensions'

# Setting up
setup(
    name="paddypy",
    version=VERSION,
    author="broom (Patrik)",
    author_email="<patrikhartl@googlemail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['azure-appconfiguration>=1.1.0', 'texttable>=1.4.4', 'azure-identity>=1.5.0', 'azure-keyvault-secrets>=4.1.0'],
    keywords=['python', 'appconfiguration', 'azure'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Environment :: Web Environment"
    ]
)