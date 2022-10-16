from setuptools import find_packages, setup


with open ("README.md","r", encoding="utf-8") as file_description:
    long_description = file_description.read()

setup(
    name="addressValidator",
    version="1.0.0",
    author="Camilo Cortes y Astrid Cely",
    description="validation of all addresses in colombia",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CamiloCortesM/addressValidator",
    project_urls={
        "Bug Tracker": "https://github.com/CamiloCortesM/addressValidator/issues"
    },
    classifiers = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    ],
    package_dir={"":"src"},
    packages=find_packages(where="src"),
    python_requires=">=3.6"
)