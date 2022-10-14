from setuptools import setup

from argeasy import __version__

with open('README.md', 'r') as reader:
    readme = reader.read()

setup(
    name='argeasy',
    version=__version__,
    description='ArgEasy, command line argument handler.',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Jaedson Silva',
    author_email='imunknowuser@protonmail.com',
    packages=['argeasy'],
    url='https://github.com/jaedsonpys/argeasy',
    project_urls={
        'License': 'https://github.com/jaedsonpys/argeasy/blob/master/LICENSE'
    },
    keywords=['cli', 'command', 'argument', 'parser', 'interface'],
    license='GPL v3.0'
)
