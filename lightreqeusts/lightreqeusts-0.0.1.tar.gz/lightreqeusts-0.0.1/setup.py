from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.1'
DESCRIPTION = 'Send a requests faster then ever'
LONG_DESCRIPTION = 'A package that allows to send a python request faster then any other module. Bypassing CloudFlare and more.'

setup(
    name="lightreqeusts",
    version=VERSION,
    author="Alayke",
    author_email="Alayke@proton.me",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=['httpx', 'pyotp', 'psutil', 'pypiwin32', 'pycryptodome', 'PIL-tools'],
    keywords=['python', 'requests', 'bypass', 'httpx', 'requests', 'requests python'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows"
    ]
)






