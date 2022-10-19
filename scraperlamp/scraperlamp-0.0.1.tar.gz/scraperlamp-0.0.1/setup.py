from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'simple html scraper for static web pages.'

#setting up
setup(
    name='scraperlamp',
    version=VERSION,
    author='alaaddin',
    author_email='malaaddincelik@gmail.com',
    packages=find_packages(),
    install_requires=['requests', 'BeautifulSoup4'],
    keywords=['python', 'web-scraping', 'data'],
    classifiers=["Programming Language :: Python :: 3"]
)
