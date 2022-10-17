# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()



setup(
    name='LotoPy',
    version='0.1.2',
    url='https://github.com/flaviorabelo/lotopy',
    author='Flavio Rabelo',
    author_email='flaviorab@gmail.com',
    keywords='loteria aposta jogo aleatorio',
    long_description=page_description,
    long_description_content_type='text/markdown',
    description='pacote para geração de números aleatórios para jogos de loteria',
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.0',
)
