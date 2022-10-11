from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.3.7'
DESCRIPTION = 'TWGW'
LONG_DESCRIPTION = 'A package that allows to api, random_string, topic, encrpt, decrpt ..etc access.'

# Setting up
setup(
    name="twgw",
    version=VERSION,
    author="Iyappan",
    author_email="iyappan@trackerwave.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['cryptography', 'requests', 'pytz', 'paho-mqtt', 'psutil'],
    keywords=['twgw'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
