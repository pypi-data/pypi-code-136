import setuptools

with open("README.md", 'rt') as f:
    long_description = f.read()

setuptools.setup(
    name="db-join",
    version="0.1.8",
    author="Frey Waid",
    author_email="logophage1@gmail.com",
    description="NoSQL db join",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT license",
    url="https://github.com/freywaid/db-join",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['dotted-notation>=0.6.0',],
)
