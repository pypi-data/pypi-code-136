from setuptools import setup, find_packages
from os.path import abspath, dirname, join

def read(rel_path):
   here = abspath(dirname(__file__))
   with open(join(here, rel_path), 'r') as fp:
      return fp.read()

def get_version(rel_path):
   for line in read(rel_path).splitlines():
      if line.startswith('__version__'):
         delim = '"' if '"' in line else "'"
         return line.split(delim)[1]

def load_readme(path:str="README.md"):
   with open(path, "r", encoding="utf-8") as file:
      return file.read()

version = get_version("speeddb/__init__.py")
readme = load_readme()

setup(
   name="speeddb",
   version=version,
   description="a simple open source multi-model database",
   long_description=readme,
   long_description_content_type='text/markdown',
   author="Nawaf Alqari",
   packages=find_packages(),
   install_requires=[
      'pyonr>=2.0.1',
      'tabulate',
      
   ],
   author_email="nawafalqari13@gmail.com",
   keywords=["speeddb", "db", "speed", "fast", "database"],
   entry_points={
      "console_scripts": ['speeddb=speeddb.cli:runner']
   },
   license="MIT",
   zip_safe=False,
   url='https://github.com/SpeedDB/SpeedDB',
   project_urls={
      'Documentation': 'https://github.com/SpeedDB/SpeedDB#readme',
      'Bug Tracker': 'https://github.com/SpeedDB/SpeedDB/issues',
      'Source Code': 'https://github.com/SpeedDB/SpeedDB',
      'Discord': 'https://discord.gg/cpvynqk4XT',
      'Donate': 'https://paypal.me/NawafHAlqari'
    },
    classifiers=[
      "Development Status :: 5 - Production/Stable",
      "Topic :: Database :: Database Engines/Servers",
      "Topic :: Software Development :: Libraries",
      "License :: OSI Approved :: MIT License",
      "Operating System :: OS Independent",
      "Intended Audience :: Developers",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.6",
    ]
)