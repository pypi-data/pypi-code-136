from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='corgiweb',
    version='0.2',
    license='MIT',
    author="Jose Enriquez",
    author_email='joseaenriqueza@hotmail.com',
    packages=find_packages('corgiweb'),
    package_dir={'': 'corgiweb'},
    url='https://dev.azure.com/joseaenriqueza/_git/groupcrawler',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='Demo with testing, send email to get access to repo',
    install_requires=[
          'pytest',
      ],

)
