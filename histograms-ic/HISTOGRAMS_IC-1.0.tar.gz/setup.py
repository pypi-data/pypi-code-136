import pathlib
from setuptools import find_packages, setup

HERE = pathlib.Path(__file__).parent

VERSION = '1.0'
PACKAGE_NAME = 'HISTOGRAMS_IC'
AUTHOR = 'Irene y Cecilia'
AUTHOR_EMAIL = 'cecilia.bilbao@alumni.mondragon.edu'
# URL = 'WWW.TUPAGINAWEB.ES'

# LICENSE = 'TIPO DE LICENCIA'
DESCRIPTION = 'Esta libreria genera histogramas de las variables numericas a partir de un csv'

#Paquetes necesarios para que funcione la libreía. Se instalarán a la vez si no lo tuvieras ya instalado
INSTALL_REQUIRES = [
    'pandas'
]

setup(
    name=PACKAGE_NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    # url=URL,
    install_requires=INSTALL_REQUIRES,
    # license=LICENSE,
    packages=find_packages(),
    include_package_data=True
)