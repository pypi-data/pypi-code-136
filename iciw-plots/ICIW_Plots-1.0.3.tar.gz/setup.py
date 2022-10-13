import atexit
import glob
import os
import shutil

import matplotlib
from setuptools import setup
from setuptools.command.install import install

def install_styles():
    # Find all style files
    stylefiles = glob.glob('styles/**/*.mplstyle', recursive=True)
    # Find stylelib directory (where the *.mplstyle files go)
    mpl_stylelib_dir = os.path.join(matplotlib.get_configdir(), "stylelib")
    if not os.path.exists(mpl_stylelib_dir):
        os.makedirs(mpl_stylelib_dir)
    # Copy files over
    print("Installing styles into", mpl_stylelib_dir)
    for stylefile in stylefiles:
        print(os.path.basename(stylefile))
        shutil.copy(
            stylefile,
            os.path.join(mpl_stylelib_dir, os.path.basename(stylefile)))


class PostInstallMoveFile(install):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        atexit.register(install_styles)

# Get description from README
root = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(root, 'README.md'), 'r', encoding='utf-8') as f:
    long_description_str = f.read()

setup(
    name='ICIW_Plots',
    version='1.0.3',
    description='A collection of tools for use in the Institute of Chemical Engineering at Ulm University.',
    long_description=long_description_str,
    long_description_content_type='text/markdown',
    author='Hannes Stagge',
    author_email='hannes.stagge@uni-ulm.de',
    license='MIT License',
    packages=[
        'ICIW_Plots'
    ],
    install_requires=[
        'numpy',
        'matplotlib',
    ],
    cmdclass={'install': PostInstallMoveFile, },
)