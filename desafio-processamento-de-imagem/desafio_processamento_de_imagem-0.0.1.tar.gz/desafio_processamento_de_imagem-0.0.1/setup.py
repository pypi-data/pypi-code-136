from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="desafio_processamento_de_imagem",
    version="0.0.1",
    author="Michelle Trigueiro",
    author_email="mi.mapelli@gmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MichelleMapelli/repositorio-dio",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)