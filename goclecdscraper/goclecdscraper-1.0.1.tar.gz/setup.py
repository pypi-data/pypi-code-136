from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="goclecdscraper",
    version="1.0.1",
    author="Harkame",
    description="Scraper for Goclecd",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Harkame/GoclecdScraper",
    install_requires=[
        "BeautifulSoup4 >= 4.11.1",
        "lxml >= 4.9.1",
        "requests >= 2.27.1"
    ],
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    python_requires=">=3.6",
)
