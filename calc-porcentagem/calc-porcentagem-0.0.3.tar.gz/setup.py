#from subprocess import _TXT
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name= "calc-porcentagem",
    version= "0.0.3",
    author= "Anderson Willian",
    author_email= "anderw1ll@outlook.com",
    description= "Pacote de calculo basico de porcentagem",
    long_description= page_description,
    long_description_content_type= "text/markdown",
    url="",
    packages= find_packages(),
    install_requires= requirements,
    python_requires= '>=3'
)