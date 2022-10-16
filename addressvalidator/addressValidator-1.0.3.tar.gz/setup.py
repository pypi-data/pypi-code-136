from setuptools import setup


with open ("README.md","r", encoding="utf-8") as file_description:
    long_description = file_description.read()

setup(
    name="addressValidator",
    package=['addressValidator'],
    version="1.0.3",
    author="Camilo Cortes, Astrid Cely",
    author_email="",
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
    license="MIT",
    include_package_data=True,
    python_requires=">=3.6",
)