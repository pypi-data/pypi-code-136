from setuptools import setup, find_packages

setup(
    name="2022_assignment1_ITIS",
    version="0.1",
    description="assignment 1",
    long_description="assignment 1, Gruppo ITIS",
    long_description_content_type='text/x-rst',
    url="https://gitlab.com/magni5/2022_assignment1_itis.git",
    author="Gruppo ITIS",
    packages=find_packages(where="src"),
    python_requires='>=3',
)
