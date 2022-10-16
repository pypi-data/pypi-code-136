import random

from setuptools import setup, find_packages

VERSION = '1.0'
DESCRIPTION = 'Makes your text funny LiKe ThiS'
LONG_DESCRIPTION = 'Changes a string from a regular string such as \"fortnite tyler ninja fortnite blevins\" to a funny one like \"ForTniTe TyLeR NinjA fOrtNite BleViNs\"'

# setup

setup(
    name='trollspeak',
    version=VERSION,
    author='DogeDevYT',
    author_email='scrimp2006@gmail.com',
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],  # add any other packages I will need in the future here

    keywords=['troll', 'funny', 'strings'],
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ]
)
