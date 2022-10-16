import pathlib
from setuptools import setup, find_packages
HERE = pathlib.Path(__file__).parent
VERSION = '0.0.3'
PACKAGE_NAME = 'helloworldtokenpackage'
AUTHOR = 'SJSU-CMPE295-Team3-Prof. Harry Li'
AUTHOR_EMAIL = 'test@test.com'
URL = 'https://github.com/Byuan3/CMPE-295A-Project'
LICENSE = 'Apache License 2.0'
DESCRIPTION = 'This is a simple HelloWorld token package to connect to Unity.'
LONG_DESCRIPTION = (HERE / "README.md").read_text()
LONG_DESC_TYPE = "text/markdown"
INSTALL_REQUIRES = [
      'numpy',
      'pandas'
]
setup(name=PACKAGE_NAME,
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      long_description_content_type=LONG_DESC_TYPE,
      author=AUTHOR,
      license=LICENSE,
      author_email=AUTHOR_EMAIL,
      url=URL,
      install_requires=INSTALL_REQUIRES,
      packages=find_packages()
      )