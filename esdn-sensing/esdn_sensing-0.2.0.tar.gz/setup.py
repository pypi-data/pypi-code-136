from setuptools import setup

setup(
  name = 'esdn_sensing',         # How you named your package folder (MyLib)
  packages = ['esdn_sensing'],   # Chose the same as "name"
  version = '0.2.0',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Python library to deliver sensor specific support to ESDN infrastructure',   # Give a short description about your library
  author = 'Colby Sawyer',                   # Type in your name
  author_email = 'sawyerco21@ecu.edu',      # Type in your E-Mail
  url = 'https://github.com/ECU-Sensing/esdn_sensing',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/ECU-Sensing/esdn_sensing/archive/refs/tags/v_0.2.0.tar.gz',    # I explain this later on
  keywords = ['sensor', 'hydros', 'cdt-10', 'water', 'generic','shim','LoRa','sensors','pm2', 'opc', 'sen', 'sen54', 'sen53', 'air', 'quality'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pyserial',
          'py-opc-ng',
          'pyusbiss',
          'sensirion_i2c_driver',
          'sensirion_i2c_sen5x',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
#  packages=find_packages(exclude=('tests')),
)