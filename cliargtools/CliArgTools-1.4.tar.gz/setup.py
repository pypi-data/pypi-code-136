from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='CliArgTools',
    version='1.4',
    license='MIT',
    description="Small and easy to use library for working with CLI arguments",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vologin Alexander",
    author_email='chura2013c@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/neongm/CliArgTools',
    keywords='cli arguments parsing parser command line',
)