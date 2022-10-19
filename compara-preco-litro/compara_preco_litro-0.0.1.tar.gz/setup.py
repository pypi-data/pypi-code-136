from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="compara_preco_litro",
    version="0.0.1",
    author="pedro_oliveira",
    author_email="pedro.oliveirape@hotmail.com",
    description="Compara preço por litro a partir de um arquivo .txt",
    long_description=page_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires='>=3.8',
)