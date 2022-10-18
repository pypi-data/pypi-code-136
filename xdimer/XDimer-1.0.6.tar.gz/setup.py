from gettext import find
from setuptools import setup, find_packages

setup(name='XDimer',
      version='1.0.6',
      description='Simulation of multi-molecular emission spectra dominated by intermolecular vibrations ',
      long_description=open('README.md').read(),
      long_description_content_type ='text/markdown' ,
      license= 'MIT',
      author='Sebastian Hammer',
      author_email='sebastian.hammer@mail.mcgill.ca',
      url='https://github.com/HammerSeb/xDimer',
      packages= find_packages(),
      install_requires=['numpy', 'scipy', 'matplotlib'],
      python_requires='>=3.6',
      include_package_data = True
     )
