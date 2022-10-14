from setuptools import setup, find_packages

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name = 'PwdGen2022',
    version = '0.0.0',
    author = 'Hugo Milesi',
    author_email = 'hugogmilesi@gmail.com',
    description = 'Simple password generator',
    license = 'MIT',
    packages = find_packages(),
    keywords = 'password',
    python_requires = '>= 3.6', 
    long_description_content_type="text/markdown",
    long_description=long_description,
)
