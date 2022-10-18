from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="calculo_idade",
    version="0.0.1",
    author="DeadLock",
    description="Calculo de idade por entrada de dados",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/evertonfranca23/exercicio_pypi",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.5',
)