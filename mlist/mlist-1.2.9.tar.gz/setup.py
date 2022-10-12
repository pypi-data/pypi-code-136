import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mlist",
    version="1.2.9",
    author="Mohit",
    author_email="mohitraj.cs@email.com",
    description="A modified list ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mohitraj/mlist",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        
        "Operating System :: OS Independent",
    ),
)