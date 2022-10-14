#!/usr/bin/env python3
import subprocess

from setuptools import setup
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop
import os
import urllib
import shutil


FF_DST = './ff'
COMPILE_CMD = 'make'
FF_LINK = 'FF-v2.3.zip'
FF_FOLDER = './up_ff/FF'
long_description = \
    """============================================================
    
 ============================================================
"""


def install_FF():
    subprocess.run(['unzip',FF_LINK,'-d',FF_FOLDER])
    curr_dirr = os.getcwd()
    os.chdir(FF_FOLDER)
    subprocess.run([COMPILE_CMD,'clean'])
    subprocess.run([COMPILE_CMD])
    os.chdir(curr_dirr)

class InstallFFdevelop(develop):
    """Custom install command."""

    def run(self):
        install_FF()
        develop.run(self)

class InstallFF(build_py):
    """Custom install command."""
    def run(self):
        install_FF()
        build_py.run(self)


setup(name='up_ff',
      description='up_ff',
      author='UNIBS Team',
      author_email='enrico.scala@unibs.it',
      packages=['up_ff'],
      package_data={
          "": ["FF/ff"],
      },
      cmdclass={
          'build_py': InstallFF,
          'develop': InstallFFdevelop,
      },
      license='APACHE')
