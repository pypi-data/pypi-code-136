import setuptools

with open("README.md", 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name = "TestUnusialMath",
    version = "0.0.1",
    author = "Ivan Derevitskii",
    author_email = 'iderevitskiy@gmail.com',
    description = "Test library",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/iderevitskiy/TestUnusialMath.git",
    packages = setuptools.find_packages(),
    classifiers = ["Programming Language :: Python :: 3",
                   "License :: OSI Approved :: MIT License",
                   "Operating System :: OS Independent"],
    python_requires = '>=3.6',
)