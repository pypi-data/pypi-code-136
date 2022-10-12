from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_Proc_Image",
    version="0.0.1",
    author="Alessandra Galvão da Silva",
    author_email="alessandragalvao@id.uff.br",
    description="Versão de teste - Processamento de imagem. Este projeto pertence a Karina Tiemi Kato, Tech Lead, Machine Learning Engineer, Data Scientist Specialist da Take. ",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlessandraGalvao/dio-image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)