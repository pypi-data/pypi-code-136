from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="exercicio_criacao_pacote",
    version="0.0.1",
    author="Michelle Trigueiro",
    author_email="mi.mapelli@gmail.com",
    description="Criação do meu primeiro pacote",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MichelleMapelli?tab=repositories",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)