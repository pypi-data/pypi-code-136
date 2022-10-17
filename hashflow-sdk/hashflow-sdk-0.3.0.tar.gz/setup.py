from setuptools import setup, find_packages

LONG_DESCRIPTION = open('README.md', 'r').read()

setup(
    name='hashflow-sdk',
    version='0.3.0',
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
    install_requires=[
        'web3>=5.31.0',
        'eth-account',
        'eth_keys'
    ],
    keywords='hashflow exchange api defi ethereum eth',
    classifiers=[],
)