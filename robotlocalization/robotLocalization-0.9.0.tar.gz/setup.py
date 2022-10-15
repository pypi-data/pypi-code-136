# -*- coding: utf-8 -*-
from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='robotLocalization',
    version='0.9.0',
    packages=find_packages(),
    license='MIT',
    author='Shinichiro Kayano',
    description='Robot Framework Internationalization',
    long_description=long_description,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Framework :: Robot Framework :: Tool',
        'Topic :: Software Development :: Localization'
    ],
    install_requires=['jproperties>=2.1.1', 'requests>=2.22.0'],
    extras_require={
        'dev': ["pytest", "docutils", "pygments"],
        'optional': ["robotframework", "robotframework-seleniumlibrary" ,
            "robotframework-autorecorder", "robotframework-requests" , "opencv-python"],
    },
    keywords="localization cicd test automation",
    entry_points={
        'console_scripts': [
            'robotLocalization=robotLocalization:main',
        ],
    },

)
