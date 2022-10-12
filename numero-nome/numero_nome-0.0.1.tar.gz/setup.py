from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="numero_nome",
    version="0.0.1",
    author="Alan Vieira",
    author_email="alansilvavieira@gmail.com",
    description="Significa o nome completo pela soma se suas letras, pela numerologia.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alan-vieira/numero-nome-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
