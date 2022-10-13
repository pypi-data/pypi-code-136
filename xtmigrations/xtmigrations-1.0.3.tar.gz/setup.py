from setuptools import setup, find_packages
from pathlib import Path
basedir = Path(__file__).parent
long_description = (basedir / "README.md").read_text()

setup(
    name='xtmigrations',
    description='Fast and easy to use database migration tool for Postgresql, written in Python',
    long_description = long_description,
    long_description_content_type="text/markdown",
    version='1.0.3',
    license='Apache license 2.0',
    author="Startech M",
    author_email='startechm@proton.me',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    url='https://github.com/startechm/xtmigrations',
    keywords='XTMigrations migration sql db upgrade',
    install_requires=[
          'psycopg2',  # TODO: add mysql / mariadb driver
      ],
)
