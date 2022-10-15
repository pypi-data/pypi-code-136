from setuptools import setup
from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    readme = fh.read()

setup(name='kitano',
    version='0.0.2',
    url='https://github.com/perseu912/kitano',
    license='MIT License',
    author='Reinan Br',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='slimchatuba@gmail.com',
    keywords='kit tools dev works',
    description=u'Library for development and works in python3.9+',
    packages=find_packages(),
    install_requires=['tqdm'],)
