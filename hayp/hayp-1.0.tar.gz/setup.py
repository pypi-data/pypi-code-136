import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0' 
PACKAGE_NAME = 'hayp' 
AUTHOR = 'Sebastian Yañez - Duver Hernandez - Georffrey Arevalo' 
AUTHOR_EMAIL = '' 
URL = '' 

LICENSE = 'MIT'
DESCRIPTION = 'Libreria para modelar redes de Petri' 
LONG_DESCRIPTION = (HERE / "README.md").read_text(encoding='utf-8') 
LONG_DESC_TYPE = "text/markdown"

INSTALL_REQUIRES = [
      'numpy',
      'graphviz'
      ]




setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type=LONG_DESC_TYPE,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    install_requires=INSTALL_REQUIRES,
    license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)

