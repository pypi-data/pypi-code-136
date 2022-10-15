from setuptools import find_packages, setup

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='digitalguide_reader',
    packages=find_packages(),
    version='0.0.6',
    description='A Python Library to read in a google sheet and turn it into states and actions',
    author='Soeren Etler',
    license='MIT',
    install_requires=["openpyxl",
                      "PyYAML",
                      "requests",
                      "gunicorn",
                      "google-api-python-client",
                      "google-auth-httplib2",
                      "google-auth-oauthlib",
                      "python-json-logger"],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
