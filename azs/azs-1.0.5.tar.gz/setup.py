from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="azs",
    version="1.0.5",
    author="Harkame",
    description="Scraper for Amazon",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Harkame/AmaZonScraper",
    install_requires=[
        "BeautifulSoup4",
        "lxml",
        "selenium",
        "fake-useragent"
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
