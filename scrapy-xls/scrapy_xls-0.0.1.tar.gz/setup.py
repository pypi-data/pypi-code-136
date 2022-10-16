from setuptools import setup, find_packages


# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


install_requires = [
    'scrapy',
    'pandas',
    'openpyxl',
]
setup(
    name         = 'scrapy_xls',
    version      = '0.0.1',
    description  = 'Scrapy spider for parsing XLS files.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Kenny',
    url='https://github.com/kennyaires/scrapy-xls',
    packages     = find_packages(),
    install_requires=install_requires,
    python_requires='>=3.6'
)