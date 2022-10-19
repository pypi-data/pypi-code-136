import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pydeohub",
    version="0.0.1",
    author="Daniel Flanagan",
    description="Python interface for Blackmagic Design Smart Videohub SDI routers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FlantasticDan/pydeohub",
    project_urls={
        "Bug Tracker": "https://github.com/FlantasticDan/pydeohub/issues",
        # "Documentation": "http://pyperdeck.readthedocs.io/"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.7",
    install_requires=[]
)