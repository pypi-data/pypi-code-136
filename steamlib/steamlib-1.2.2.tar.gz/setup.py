from setuptools import setup

with open('README.md', encoding="utf-8") as f:
    long_description = f.read()

version = '1.2.2'

setup(
    name='steamlib',
    version=version,
    description='Python library for working with steam',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/hirogarugaru/steamlib',
    download_url=f'https://github.com/hirogarugaru/steamlib/archive/refs/heads/master.zip',
    license='GNU General Public License v3.0',
    packages=['steamlib'],
    install_requires=['beautifulsoup4', 'lxml', 'requests', 'rsa'],
    author='valeXeich, hirogaru',
    author_email='valerapanow03@gmail.com',
)