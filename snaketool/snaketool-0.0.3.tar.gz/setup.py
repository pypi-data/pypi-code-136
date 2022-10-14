import os
from setuptools import setup, find_packages

def get_version():
    with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), 'snaketool', 'snaketool.VERSION')) as f:
        return f.readline().strip()

CLASSIFIERS = [
    "Environment :: Console",
    "Environment :: MacOS X",
    "Intended Audience :: Science/Research",
    "License :: OSI Approved :: MIT license",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Topic :: Scientific/Engineering :: Bio-Informatics",
]

setup(
 name='snaketool',
 packages=find_packages(),
 url='',
 python_requires='>=3.7',
 description="Snakemake-powered commandline tool to do a thing.",
 version=get_version(),
 author="Michael Roach",
 author_email="example@email.com",
 py_modules=['snaketool'],
 install_requires=["snakemake==7.14.0",
                   "pyyaml==6.0",
                   "Click==8.1.3"],
 entry_points={
  'console_scripts': [
    'snaketool=snaketool.__main__:main'
  ]},
 include_package_data=True,
)
