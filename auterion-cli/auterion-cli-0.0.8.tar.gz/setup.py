from importlib.metadata import entry_points
from setuptools import setup, find_packages
from auterioncli.version_util import get_version


setup(name='auterion-cli',
      version=get_version(),
      description='CLI tool to interact with AuterionOS devices and apps',
      url='https://github.com/Auterion/auterion-cli',
      author='Auterion',
      author_email='support@auterion.com',
      license='proprietary',
      packages=find_packages(),
      install_requires=['tabulate', 'requests', 'zeroconf', 'websockets', 'packaging'],
      python_requires='>=3.6',
      zip_safe=False,
      entry_points={
          'console_scripts': ['auterion-cli=auterioncli.main:main']
      })
