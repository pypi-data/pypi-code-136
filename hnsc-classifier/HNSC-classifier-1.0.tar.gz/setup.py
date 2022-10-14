from setuptools import setup, find_packages
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='HNSC-classifier',
    version='1.0',
    packages=find_packages(),
    entry_points={
        "console_scripts": ['HNSC-classifier = HNSCDP.HNSC:main']
    },
    url='https://github.com/yangfangs/HNSC-classifier',
    license='GNU General Public License v3.0',
    author='Yang Fang',
    author_email='506528950@qq.com',
    description='HNSC classifier',
    install_requires=required,
    package_data={'': ['*.md',"*txt"]},
    long_description=long_description,
    long_description_content_type='text/markdown',
)
