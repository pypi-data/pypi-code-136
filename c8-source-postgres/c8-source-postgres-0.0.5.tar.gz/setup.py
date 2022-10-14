#!/usr/bin/env python

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='c8-source-postgres',
      version='0.0.5',
      description='C8 Source for extracting data from PostgresSQL.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Macrometa',
      url='https://github.com/Macrometacorp/c8-source-postgres',
      classifiers=[
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Programming Language :: Python :: 3 :: Only'
      ],
      install_requires=[
          'pipelinewise-singer-python==1.2.0',
          'psycopg2-binary==2.9.3',
          'strict-rfc3339==0.7',
          'c8connector==0.0.5'
      ],
      extras_require={
          "test": [
              'pytest==7.0.1',
              'pylint==2.12.*',
              'pytest-cov==4.0.0'
          ]
      },
      entry_points='''
          [console_scripts]
          c8-source-postgres=c8_source_postgres:main
      ''',
      packages=['c8_source_postgres', 'c8_source_postgres.sync_strategies']
      )
