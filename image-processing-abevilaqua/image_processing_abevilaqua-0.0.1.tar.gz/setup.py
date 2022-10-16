from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_abevilaqua",
    version="0.0.1",
    author="Andre Bevilaqua",
    author_email="andrebevilaqua@hotmail.com",
    description="My short description",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/andrembevilaqua/image_processing_abevilaqua",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)