# -*- coding: utf-8 -*-
"""Setup file.

Reminder for PyPI uploading (currently manual).
 - Install twine if don't have it
 - python setup.py sdist bdist_wheel
 - Test with PyPI until it looks good, but note you can't install from there
   because it's missing dependencies
     twine upload -r testpypi dist/* -u jennirinker -p PASSWORD
 - Once it is greenlighted, upload to PyPI
     twine upload dist/* -u jennirinker -p PASSWORD
 - Tag the branch with the corresponding version
"""
from os import path
from setuptools import setup


def load_readme():
    """Load readme to put into pypi long description"""
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(name='lacbox',
      version='0.0.3',
      description='Toolbox for LAC course at DTU Wind Energy',
      long_description=load_readme(),
      long_description_content_type='text/markdown',
      url='https://gitlab.windenergy.dtu.dk/lac-course/dtulac',
      author='DTU Wind Energy',
      author_email='rink@dtu.dk',
      license='MIT',
      packages=['lacbox',  # top-level package
                ],
      install_requires=['h5py',  # for gtsdf loading
                        'jupyter',  # run demos
                        'matplotlib',  # plotting
                        'numpy',  # numberic arrays
                        'pandas',  # for gtsdf handling
                        'scipy', # Interpolation
                        ],
      zip_safe=False)
