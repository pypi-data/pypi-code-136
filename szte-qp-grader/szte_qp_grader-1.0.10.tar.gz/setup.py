from setuptools import setup, find_packages
import os

VERSION = '1.0.10'
DESCRIPTION = 'Grading Qiskit exercises'
LONG_DESCRIPTION = 'Grading the exercises made for the Quantum Programming course at University of Szeged'

# Setting up
setup(
    name="szte_qp_grader",
    version=VERSION,
    author="András Czégel",
    #author_email="<czegelandras@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['Qiskit', 'numpy', 'pymongo', 'pymongo[srv]', 'datetime', 'dnspython']
)