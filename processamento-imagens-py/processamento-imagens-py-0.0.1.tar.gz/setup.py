from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento-imagens-py",
    version="0.0.1",
    author="Guilherme",
    author_email="guilhermecarvalho056@gmail.com",
    description="Image processing package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guilhermercarv/Ciencia-Analise-de-Dados-com-Python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)