from setuptools import setup
from io import open 
with open(r'C:/Users/Admin/Desktop/DefPy/README.md', 'r', encoding='utf-8') as fh:
	long_description = fh.read()
versions = '1.1.2'

setup(name='DefPy',version=versions,author='itzkeeni.py',author_email='maratkanovartem89@mail.ru',description='Libary for python',long_description=long_description,license='License :: OSI Approved :: MIT License',packages=['DefPy'],classifiers=["Programming Language :: Python :: 3","Operating System :: OS Independent",])
