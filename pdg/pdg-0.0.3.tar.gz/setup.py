# Customize location of .pypirc file
# Credit: https://stackoverflow.com/questions/37845125/custom-location-for-pypirc-file
import os
from distutils.command.register import register as register_orig
from distutils.command.upload import upload as upload_orig
class register(register_orig):
    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')
class upload(upload_orig):
    def _get_rc_file(self):
        return os.path.join('.', '.pypirc')


# Standard package setup
from setuptools import setup, find_packages

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name = 'pdg',
    version = '0.0.3',
    author = 'Particle Data Group',
    author_email = 'jberinger@lbl.gov',
    description = 'Python API for accessing PDG data',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://pdg.lbl.gov',
    license = 'To be determined.',
    packages = find_packages(),
    package_data={"pdg": ["pdg.sqlite"]},
    install_requires = ['SQLAlchemy'],
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Topic :: Database :: Front-Ends',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Physics'
        ],
    keywords = 'PDG, particle physics',
    cmdclass={
        'register': register,
        'upload': upload
        }
)
