from pydoc import describe
from importlib_metadata import metadata
from setuptools import setup
long_description = ""
try:
    import pypandoc
    long_description = pypandoc.convert_file('./ken_api/README.MD', 'rst')
except(IOError, ImportError):
    long_description = open('./ken_api/README.MD').read()

setup(name="tbc_ken_api",
      version='0.2',
      description="Trading Bot Club alpaca api",
      author="Kris Luangpenthong",
      author_email="krisken4699@gmail.com",
      url="https://pypi.org/project/tbc-ken-api/",
      long_description=long_description,
      long_description_content_type='text/markdown',
      install_requires=['requests'],
      packages=['ken_api'],
      zip_safe=False)
