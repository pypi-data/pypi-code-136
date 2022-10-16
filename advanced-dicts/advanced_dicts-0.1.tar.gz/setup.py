from setuptools import setup
from advanced_dicts import __version__

with open('README.md', 'r', encoding='utf-8') as mdf:
    long_description = mdf.read()

setup(
    name="advanced_dicts",
    version=__version__,
    author="itttgg",
    author_email="aitiiigg1@gmail.com",
    description="Advanced dicts - package for simpler work with dicts",
    download_url=f"https://github.com/itttgg/advanced-dicts/tree/{__version__}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/itttgg/advanced-dicts",
    packages=['advanced_dicts'],
    classifiers = [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    zip_safe=False,
    python_requires=">=3.8"
)
