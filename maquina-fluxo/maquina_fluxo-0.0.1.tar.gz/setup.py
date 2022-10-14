from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup( 
    name="maquina_fluxo",
    version="0.0.1",
    author="Erick",
    author_email="erickhiroyuki@alunos.utfpr.edu.br",
    description="Calculo perda de carga",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/erickhiroyuki/Projeto-3-CD",
    packages=find_packages(),
    install_requires=["colebrook==0.0.5", "matplotlib==3.6.1", "numpy==1.23.4"],
    python_requires='>=3.10.8',
)