
    ########################
    ##  setup.py          ##
    ##  Chieh-An Lin      ##
    ##  2022.10.15        ##
    ########################

## Python
import sys
import os
import setuptools as sut
import subprocess as spc
import shutil
import platform

## Third party
import pandas as pd

## Custom
from pylinc.__init__ import __version__, PKG_NAME, AUTHOR_NAME

################################################################################
## Configuration

SRC_PATH = f'{PKG_NAME}/'
DOC_PATH = 'docs/'
DIST_PATH = 'dist/'

################################################################################
## Generate .rst files

def saveRstModule(module, verbose=True):
  path = f'{DOC_PATH}source/modules/'
  os.makedirs(path, exist_ok=True)

  name = f'{path}{module}.rst'

  with open(name, 'w') as file_:
    file_.write(f'{module}\n')
    file_.write( '{}\n'.format('='*len(module)))

    file_.write( '\n')
    file_.write(f'.. automodule:: {PKG_NAME}.{module}\n')
    file_.write( '   :members:\n')
    file_.write( '   :undoc-members:\n')
    file_.write( '   :show-inheritance:\n')

    if verbose:
      print(f'Saved \"{name}\"')
  return

def saveRstAll(verbose=True):
  for name in os.listdir(SRC_PATH):
    if not os.path.isfile(f'{SRC_PATH}{name}') or name == '__init__.py':
      continue

    module = name.split('.')[0]
    saveRstModule(module, verbose=verbose)
  return

def removeRst(verbose=True):
  shutil.rmtree(f'{DOC_PATH}source/modules/', True)

  if verbose:
    print(f'Removed .rst files')
  return

def processRst(verbose=True):
  print()
  print('################################################################################')
  print('## Regenerate rst files')
  print()

  ## Remove documentation
  if 'Windows' == platform.system():
    spc.run(['make.bat', 'clean'], shell=True, check=True, cwd=DOC_PATH)
  else:
    spc.run(['make clean'], shell=True, check=True, cwd=DOC_PATH)

  ## Remove .rst
  removeRst()
  print()

  ## Regenerate .rst
  saveRstAll(verbose=True)

  if verbose:
    print()
    print(f'Regenerated rst files')
  return

################################################################################
## Generate documentation

def saveNojekyll(verbose=True):
    out_name = f'{DOC_PATH}build/html/.nojekyll'

    with open(out_name, 'w') as out_file:
        if verbose:
            print(f'Saved \"{out_name}\"')

def processDocumentation(verbose=True):
  print()
  print('################################################################################')
  print('## Generate documentation')
  print()

  if 'Windows' == platform.system():
    spc.run(['make.bat', 'html'], shell=True, check=True, cwd=DOC_PATH)
  else:
    spc.run(['make html'], shell=True, check=True, cwd=DOC_PATH)

  ## Generate documentations
  if verbose:
    print()
    print(f'Generated documentation')
  return

################################################################################
## Make distribution

def removeDist(verbose=True):
  shutil.rmtree(DIST_PATH, True)
  os.makedirs(DIST_PATH, exist_ok=True)

  if verbose:
    print(f'Cleared \"dist/\"')
  return

def processDistribution(verbose=True):
  print()
  print('################################################################################')
  print('## Make distribution')
  print()

  removeDist(verbose=verbose)
  print()

  sut.setup(
    name=PKG_NAME,
    version=__version__,
    description='A general-purposed utility kit.',
    # long_description=long_description,
    # long_description_content_type='text/markdown',

    author=AUTHOR_NAME,
    author_email='turtlelin1210@gmail.com',
    url='https://github.com/Linc-tw/pylinc',

    packages=[PKG_NAME],
    classifiers=[
      'Development Status :: 4 - Beta',
      'Programming Language :: Python :: 3',
      'License :: OSI Approved :: MIT License',
      'Topic :: Documentation :: Sphinx',
    ],
    script_args=['sdist', 'bdist_wheel'],
    license='MIT',
    # keywords='wpc, daq, driver, usb, ethernet, wifi, data acquisition',

    install_requires=[
      'numpy>=1.15.0',
      'astropy>=4.0.0',
      'pandas>=1.2.0',
      'matplotlib>=3.0.0',
    ],
    extras_require={
      'healpy': ['healpy>=3.5.3'],
    },
    python_requires='>=3.8',
  )

  ## Generate documentations
  if verbose:
    print()
    print(f'Made distribution')
  return

################################################################################
## Upload release

def processUpload(test=False, verbose=True):
  if 'Windows' == platform.system():
    if test:
      spc.run(['twine', 'upload', '-r', 'testpypi', 'dist\*'], shell=True, check=True)
    else:
      spc.run(['twine', 'upload', 'dist\*'], shell=True, check=True)
  else:
    if test:
      spc.run(['python3.8 -m twine upload -r testpypi dist/*'], shell=True, check=True)
    else:
      spc.run(['python3.8 -m twine upload dist/*'], shell=True, check=True)

  if verbose:
    print(f'Uploaded release')
  return

################################################################################
## Main function

if __name__ == '__main__':
  if len(sys.argv) > 1:
    arg_list = sys.argv[1:]
  else:
    arg_list = ['all']

  if 'all' in arg_list or 'rst' in arg_list or 'clean' in arg_list:
    processRst()
  if 'all' in arg_list or 'docs' in arg_list:
    processDocumentation()
  if 'all' in arg_list or 'dist' in arg_list:
    processDistribution()
  if 'all' in arg_list or 'upload' in arg_list:
    processUpload()
  if 'test' in arg_list:
    processUpload(test=True)

  print()
  print('## End')
  print('################################################################################')

## End of file
################################################################################
