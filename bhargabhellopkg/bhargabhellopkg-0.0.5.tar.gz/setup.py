from setuptools import setup, find_packages
import codecs
import os

VERSION='0.0.5'
DESCRIPTION='A basic hello package'
LONG_DESCRIPTION='A basic hello package long desc'

setup(name='bhargabhellopkg',
      packages = find_packages(),
      version=VERSION,
      description=DESCRIPTION,

      author='Bhargab',
      author_email='bhargab.ganguli@gmail.com',
      keywords = ['keyowrd1', 'keyword2', 'keyword3'],
      license='MIT', #YOUR LICENSE HERE!

      install_requires=['numpy','pandas','scipy'],  #YOUR DEPENDENCIES HERE
  

      classifiers=[
        'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', # Your License Here  
        'Programming Language :: Python :: 3',    # List Python versions that you support Here  
        ],
)