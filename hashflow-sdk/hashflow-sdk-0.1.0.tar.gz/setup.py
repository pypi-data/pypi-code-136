from setuptools import setup, find_packages

LONG_DESCRIPTION = open('README.md', 'r').read()

REQUIREMENTS = open('requirements.txt', 'r').read().split('\n')

setup(
    name='hashflow-sdk',
    version='0.1.0',
    packages=find_packages(),
    package_data={
        'hashflow': ['abi/*.json', 'deployed.json'],
    },
    description='Python SDK to interact with Hashflow Smart Contracts',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='',
    author='Hashflow Foundation',
    license='Apache 2.0',
    author_email='victor@hashflow.com',
    install_requires=REQUIREMENTS,
    keywords='hashflow exchange api defi ethereum eth',
    classifiers=[],
)
