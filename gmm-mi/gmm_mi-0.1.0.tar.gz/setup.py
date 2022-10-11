from setuptools import setup, find_packages
import shutil

PACKAGENAME = 'gmm_mi'

setup(
    name='gmm_mi',
    version="0.1.0",
    author='Davide Piras',
    author_email='dr.davide.piras@gmail.com',
    description='Estimate mutual information distribution with Gaussian mixture models',
    url='https://github.com/dpiras/GMM-MI',
    license='GNU General Public License v3.0 (GPLv3)',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires=['pytest',
                      'tqdm',
                      'matplotlib>=3.1.2',
                      'numpy>=1.17.4',
                      'scikit-learn>=1.0.2',
                      'scipy>=1.7.1']
                      )

