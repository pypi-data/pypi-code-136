from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="statisticas",
    version="0.0.1",
    author="LucasMGuima",
    author_email="lucasmguima@outlook.com",
    description="The package has the purpose of help calculate statistics",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LucasMGuima/statisticas-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)