from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="rpg_pybot",
    version="0.0.1",
    author="Lucas Mateus da Silva",
    author_email="lmateus1067@outlook.com",
    description="A small RPG simulator",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/W1ndeck/RPG-PYBOT",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.10.5',
)