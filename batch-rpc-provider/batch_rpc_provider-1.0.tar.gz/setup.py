#!/usr/bin/env python

from setuptools import setup

setup(name='batch_rpc_provider',
      version='1.0',
      # list folders, not files
      packages=['batch_rpc_provider'],
      scripts=['batch_rpc_provider/provider.py'],
      package_data={'batch_rpc_provider': ['README.txt']},
      author = 'Sieciech Czajka',
      author_email = 'sieciech.czajka@golem.network', 
      url = 'https://github.com/scx1332/provider', 
       download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',
       keywords = ['MultiCall', 'json-rpc', 'web3'], 
        classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.9',
  ],
      )