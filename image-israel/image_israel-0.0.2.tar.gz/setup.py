from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_israel",
    version="0.0.2",
    author="israelclaudio",
    author_email="israelclaudio21@gmail.com",
    description="Pacote criado para processamento de imagem, a partir do curso de criação de pacotes da DIO",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/israelclaudio/image_processing_package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)