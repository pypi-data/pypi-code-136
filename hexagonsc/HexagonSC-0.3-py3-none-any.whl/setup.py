from setuptools import setup
  
# reading long description from file
with open('DESCRIPTION.txt') as file:
    long_description = file.read()
  
  
# specify requirements of your package here
REQUIREMENTS = ['requests','tabulate','opencv-python','PIL','bs4','pytesseract','keyboard']
  
# some more details
CLASSIFIERS = [
     'Star Citizen'
    ]
  
# calling the setup function 
setup(name='HexagonSC',
      version='1.0.0',
      description='contract interrogator',
      long_description=long_description,
      url='https://github.com/',
      author='TG',
      author_email='Tg3.383@gmail.com',
      license='GNU public v3',
      packages=[''],
      classifiers=CLASSIFIERS,
      install_requires=REQUIREMENTS,
      keywords='Starcitizen, Bounty-hunting,bs4,'
      )