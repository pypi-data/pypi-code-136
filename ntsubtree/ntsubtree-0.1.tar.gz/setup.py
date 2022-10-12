from setuptools import setup, find_packages
from setuptools.command.develop import develop
from setuptools.command.install import install
from ntdownload import Downloader

import sys
if not sys.version_info[0] == 3:
  sys.exit("Sorry, only Python 3 is supported")

import os
script_dir = os.path.dirname(os.path.realpath(__file__))

def post_install():
  with open("info.txt", "w") as f:
    f.write("information")

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)
        post_install()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        post_install()

def readme():
  with open('README.md') as f:
    return f.read()

setup(name='ntsubtree',
      version='0.1',
      #description='Tree representation for fast queries of '+\
      #            'the subtree of a taxon in the NCBI taxonomy tree',
      description='preliminary version',
      long_description=readme(),
      long_description_content_type="text/markdown",
      cmdclass={
          'develop': PostDevelopCommand,
          'install': PostInstallCommand,
      },
      #url="htts://github.com/ggonnella/fastsubtrees/tree/main/ntsubtree",
      keywords="bioinformatics genomics taxonomy trees",
      author='Giorgio Gonnella and and others (see CONTRIBUTORS)',
      author_email='gonnella@zbh.uni-hamburg.de',
      license='ISC',
      # see https://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Software Development :: Libraries',
      ],
      packages=find_packages(),
      scripts=['bin/ntsubtree'],
      zip_safe=False,
      include_package_data=True,
      install_requires=['tqdm>=4.57.0', 'loguru>=0.5.1', 'docopt>=0.6.2',
        "schema>=0.7.4", "sh>=1.14.2",
        "ntdownload", "fastsubtrees"],
      test_suite="pytest",
      tests_require=['pytest', 'pytest-console-scripts', 'sh'],
    )
