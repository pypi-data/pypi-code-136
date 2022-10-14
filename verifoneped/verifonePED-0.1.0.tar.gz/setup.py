from setuptools import setup, find_packages

version = '0.1.0'

setup(
    name='verifonePED',
    version=version,
    packages=find_packages(),
    license='MIT',
    description='Sends control commands to Verifone pin entry devices',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/geftactics/python-verifonePED',
    download_url = 'https://github.com/geftactics/python-verifonePED/archive/' + version + '.tar.gz',
    author='Geoff Kendal',
    author_email='Geoff@squiggle.org'
)
