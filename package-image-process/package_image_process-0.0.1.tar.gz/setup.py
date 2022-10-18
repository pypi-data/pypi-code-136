from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="package_image_process",
    version="0.0.1",
    author="gusmazzinghy",
    author_email="gusmazzinghy@gmail.com",
    description="Package Python to edit images",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/GusMazzinghyDev",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)