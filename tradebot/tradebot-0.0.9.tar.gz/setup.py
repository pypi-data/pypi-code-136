
from distutils.core import setup

from setuptools import find_packages


__version = '0.0.9'
setup(
  name = 'tradebot',         # How you named your package folder
  packages = find_packages(),   # Chose the same as "name"
  version = __version,      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A wrapper around the TDAmeritrade REST API',   # Give a short description about your library
  author = 'Adeiron Barolli',                   # Type in your name
  author_email = 'obarolli@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/abarolli/trade-bot',   # Provide either the link to your github or to your website
  download_url = f'https://github.com/abarolli/trade-bot/archive/refs/tags/v{__version}.tar.gz',
  keywords = ['stocks', 'statistics', 'rest api'],   # Keywords that define your package best
  install_requires=[  
          'requests',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.7', #Specify which python versions that you want to support
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
  ],
)