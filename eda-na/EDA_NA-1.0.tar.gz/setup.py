import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0'
PACKAGE_NAME = 'EDA_NA'
AUTHOR = 'Ainhoa y Nagore'
AUTHOR_EMAIL = 'nagore.bermeosolo@alumni.mondragon.edu'
#URL = 'WWW.TUPAGINAWEB.ES'
#LICENSE = 'TIPO DE LICENCIA'
DESCRIPTION = 'Esta libreria contiene diferentes funciones para llevar a cabo un análisis exploratorio de los datos a partir de un archivo csv como input.'

#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
    'pandas', 'warnings', 'itertools', 'numpy', 'math', 'seaborn', 'matplotlib'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    #url=URL,
    install_requires=INSTALL_REQUIRES,
    #license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)