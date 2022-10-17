from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="processamento_imagem_nil",
    version="0.0.1",
    author="Elenilton Vicente de Aguiar",
    author_email="aguiar14564@gmail.com",
    description="Processamento de Imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/VicenteAguiar/Bootcamp_Data_Science_Unimed",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)
