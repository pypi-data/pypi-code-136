from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image-processing-package-csrdev2",
    version="0.1.1",
    author="Charlly Ribeiro",
    author_email="charllyribeiro@gmail.com",
    description="Projeto do bootcamp da DIO, Desenvolvedora Karina Kato",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/devcharib/projeto-criacao-de-pacotes-em-python.git",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)