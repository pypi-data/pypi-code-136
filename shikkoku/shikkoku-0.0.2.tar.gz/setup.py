from setuptools import setup, find_packages

setup(name="shikkoku",
      package_dir={'': 'src'},
      packages=find_packages(where='src'),
      install_requires=['pysdl2', 'pysdl2-dll', 'pillow'])
