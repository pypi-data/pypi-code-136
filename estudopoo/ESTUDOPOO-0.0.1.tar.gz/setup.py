from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="ESTUDOPOO",
    version="0.0.1",
    author="FELIPE SOLER",
    author_email="FELIPESOLER12@GMAIL.COM",
    description="PRIMEIROS PROGRAMAS DE ESTUDO EM PY",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/felipesoler-ads",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)