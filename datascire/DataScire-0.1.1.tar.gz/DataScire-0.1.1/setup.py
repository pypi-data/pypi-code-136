from setuptools import setup, find_packages


setup(
    name='DataScire',
    version='0.1.1',
    license='MIT',
    author="Carlos Acosta",
    author_email='development@datascire.com',
    packages=find_packages('datascire'),
    package_dir={'': 'datascire'},
    url='https://github.com/DataScire/datascire',
    keywords='DataScire Project',
    install_requires=[
          'pandas',
      ],

)