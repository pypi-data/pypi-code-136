from setuptools import setup

requirements = ["tonsdk>=1.0.6", "ton>=0.24", "aiohttp>=3.8.1", "setuptools>=65.3.0"]

setup(
    name='ToNFToolz',
    version='0.9.9.6',
    packages=['ToNFToolz'],
    url='',
    license='MIT',
    author='yungwine',
    author_email='cyrbatoff@gmail.com',
    description='Explore NFT Items in TON Blockchain',
    install_requires=requirements,
)
